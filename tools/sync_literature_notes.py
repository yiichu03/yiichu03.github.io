#!/usr/bin/env python3

from __future__ import annotations

import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path


REPO_DIR = Path(__file__).resolve().parent.parent
VAULT_DIR = REPO_DIR.parent
SOURCE_DIR = VAULT_DIR / "10 Literature Notes"
ATTACHMENTS_DIR = VAULT_DIR / "Attachments"
OUTPUT_DIR = REPO_DIR / "_literature_notes"
ASSET_DIR = REPO_DIR / "assets" / "literature"

WIKILINK_RE = re.compile(r"(!)?\[\[([^\]]+)\]\]")
FRONT_MATTER_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S %z"


def format_front_matter_datetime(value: datetime) -> str:
    return value.astimezone(timezone.utc).strftime(FRONT_MATTER_DATETIME_FORMAT)


def parse_datetime(value: str) -> datetime | None:
    text = value.strip()
    if not text:
        return None

    for date_format in (
        FRONT_MATTER_DATETIME_FORMAT,
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%S.%f%z",
    ):
        try:
            return datetime.strptime(text, date_format)
        except ValueError:
            continue

    try:
        return datetime.fromisoformat(text)
    except ValueError:
        return None


def format_display_date(value: str) -> str:
    parsed = parse_datetime(value)
    if parsed is None:
        return value
    return parsed.astimezone(timezone.utc).strftime("%Y-%m-%d")


def format_display_datetime(value: str) -> str:
    parsed = parse_datetime(value)
    if parsed is None:
        return value
    return parsed.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def slugify(value: str) -> str:
    value = value.strip().replace("/", "-")
    value = re.sub(r"\s+", "-", value, flags=re.UNICODE)
    value = re.sub(r"[^\w\-]+", "", value, flags=re.UNICODE)
    value = re.sub(r"-+", "-", value, flags=re.UNICODE).strip("-")
    return value or "note"


def escape_yaml(value: str) -> str:
    return value.replace('"', '\\"')


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def parse_front_matter_block(block: str) -> dict[str, object]:
    data: dict[str, object] = {}
    current_list_key: str | None = None

    for raw_line in block.splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue

        if current_list_key and line.lstrip().startswith("- "):
            item = strip_quotes(line.lstrip()[2:])
            current_items = data.setdefault(current_list_key, [])
            if isinstance(current_items, list):
                current_items.append(item)
            continue

        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not match:
            current_list_key = None
            continue

        key, raw_value = match.groups()
        raw_value = raw_value.strip()

        if not raw_value:
            data[key] = []
            current_list_key = key
            continue

        if raw_value.startswith("[") and raw_value.endswith("]"):
            inner = raw_value[1:-1].strip()
            items = [] if not inner else [strip_quotes(part.strip()) for part in inner.split(",")]
            data[key] = items
            current_list_key = None
            continue

        data[key] = strip_quotes(raw_value)
        current_list_key = None

    return data


def split_front_matter(text: str) -> tuple[dict[str, object], str]:
    if not text.startswith("---\n"):
        return {}, text

    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, text

    block = parts[0][4:]
    return parse_front_matter_block(block), parts[1]


def normalize_tags(value: object) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip().lower() for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip().lower()]
    return []


def should_publish(metadata: dict[str, object]) -> bool:
    publish = str(metadata.get("publish", "")).strip().lower()
    tags = normalize_tags(metadata.get("tags"))
    return publish == "github" or "github" in tags


def extract_title(text: str, fallback: str, metadata: dict[str, object] | None = None) -> tuple[str, str]:
    if metadata:
        frontmatter_title = str(metadata.get("title", "")).strip()
        if frontmatter_title:
            return frontmatter_title, text.lstrip()

    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("# "):
            title = line[2:].strip()
            remaining = lines[:index] + lines[index + 1 :]
            body = "\n".join(remaining).lstrip()
            return title or fallback, body
    return fallback, text.lstrip()


def heading_anchor(value: str) -> str:
    return slugify(value).lower()


def copy_asset(path: Path, copied_assets: dict[Path, str]) -> str:
    resolved = path.resolve()
    if resolved in copied_assets:
        return copied_assets[resolved]

    if resolved.is_relative_to(ATTACHMENTS_DIR.resolve()):
        rel = resolved.relative_to(ATTACHMENTS_DIR.resolve())
        destination = ASSET_DIR / "attachments" / rel
    else:
        destination = ASSET_DIR / "files" / path.name

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(resolved, destination)
    rel_url = destination.relative_to(REPO_DIR).as_posix()
    copied_assets[resolved] = rel_url
    return rel_url


def resolve_asset(raw_target: str, note_path: Path) -> Path | None:
    candidates = []
    target = raw_target.strip()
    if not target:
        return None

    candidates.append(note_path.parent / target)
    candidates.append(ATTACHMENTS_DIR / target)

    target_path = Path(target)
    if not target_path.suffix:
        for extension in (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".pdf"):
            candidates.append(note_path.parent / f"{target}{extension}")
            candidates.append(ATTACHMENTS_DIR / f"{target}{extension}")

    for candidate in candidates:
        if candidate.exists() and candidate.is_file():
            return candidate
    return None


def build_note_index(note_paths: list[Path]) -> dict[str, str]:
    index: dict[str, str] = {}
    for path in note_paths:
        rel = path.relative_to(SOURCE_DIR).with_suffix("")
        key_variants = {
            path.stem,
            rel.as_posix(),
            rel.name,
        }
        slug = slugify(rel.as_posix())
        for key in key_variants:
            index[key] = slug
    return index


def load_existing_output_metadata() -> dict[str, dict[str, object]]:
    metadata_by_source_path: dict[str, dict[str, object]] = {}
    if not OUTPUT_DIR.exists():
        return metadata_by_source_path

    for path in OUTPUT_DIR.glob("*.md"):
        if not path.is_file() or path.name == ".gitkeep":
            continue
        metadata, _ = split_front_matter(path.read_text(encoding="utf-8"))
        source_path = str(metadata.get("source_path", "")).strip()
        if source_path:
            metadata_by_source_path[source_path] = metadata

    return metadata_by_source_path


def git_first_added_at(path: Path) -> str | None:
    rel_path = path.relative_to(REPO_DIR).as_posix()
    result = subprocess.run(
        ["git", "log", "--diff-filter=A", "--format=%aI", "--", rel_path],
        cwd=REPO_DIR,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return None

    lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    if not lines:
        return None

    parsed = parse_datetime(lines[-1])
    if parsed is None:
        return None
    return format_front_matter_datetime(parsed)


def render_links(text: str, note_path: Path, note_index: dict[str, str], copied_assets: dict[Path, str]) -> str:
    def replace(match: re.Match[str]) -> str:
        is_embed = bool(match.group(1))
        raw = match.group(2).strip()
        target_and_alias = raw.split("|", 1)
        target = target_and_alias[0].strip()
        label = target_and_alias[1].strip() if len(target_and_alias) == 2 else ""

        note_target, section = (target.split("#", 1) + [""])[:2] if "#" in target else (target, "")

        asset_path = resolve_asset(note_target, note_path)
        if is_embed and asset_path is not None:
            rel_url = copy_asset(asset_path, copied_assets)
            alt = label or asset_path.stem
            return f"![{alt}]({{{{ '/{rel_url}' | relative_url }}}})"

        slug = note_index.get(note_target) or note_index.get(Path(note_target).stem)
        if slug:
            text_label = label or Path(note_target).name or note_target
            anchor = f"#{heading_anchor(section)}" if section else ""
            return f"[{text_label}]({{{{ '/literature/{slug}/' | relative_url }}}}{anchor})"

        return match.group(0)

    return WIKILINK_RE.sub(replace, text)


def sync() -> int:
    if not SOURCE_DIR.exists():
        raise SystemExit(f"Source directory not found: {SOURCE_DIR}")

    all_note_paths = sorted(path for path in SOURCE_DIR.glob("*.md") if path.is_file())

    published_note_paths: list[Path] = []
    parsed_sources: dict[Path, tuple[dict[str, object], str]] = {}
    for note_path in all_note_paths:
        source_text = note_path.read_text(encoding="utf-8")
        metadata, body = split_front_matter(source_text)
        parsed_sources[note_path] = (metadata, body)
        if should_publish(metadata):
            published_note_paths.append(note_path)

    note_index = build_note_index(published_note_paths)
    existing_output_metadata = load_existing_output_metadata()
    synced_at = format_front_matter_datetime(datetime.now(timezone.utc))

    shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
    shutil.rmtree(ASSET_DIR, ignore_errors=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / ".gitkeep").write_text("\n", encoding="utf-8")
    (ASSET_DIR / ".gitkeep").write_text("\n", encoding="utf-8")

    copied_assets: dict[Path, str] = {}

    for note_path in published_note_paths:
        metadata, body = parsed_sources[note_path]
        fallback_title = note_path.stem
        title, body = extract_title(body, fallback_title, metadata)
        body = render_links(body, note_path, note_index, copied_assets).rstrip() + "\n"

        rel = note_path.relative_to(SOURCE_DIR).with_suffix("")
        slug = slugify(rel.as_posix())
        source_path = note_path.relative_to(VAULT_DIR).as_posix()
        output_path = OUTPUT_DIR / f"{slug}.md"
        updated_at = format_front_matter_datetime(datetime.fromtimestamp(note_path.stat().st_mtime, tz=timezone.utc))
        published_at = str(existing_output_metadata.get(source_path, {}).get("published_at", "")).strip()
        if not published_at:
            published_at = git_first_added_at(output_path) or synced_at

        metadata_block = (
            f"> Published: {format_display_date(published_at)}\n"
            f"> Updated: {format_display_datetime(updated_at)}\n\n"
        )

        output_path.write_text(
            "---\n"
            f'title: "{escape_yaml(title)}"\n'
            f'slug: "{escape_yaml(slug)}"\n'
            f'date: {published_at}\n'
            f'published_at: {published_at}\n'
            f'updated_at: {updated_at}\n'
            f'source_path: "{escape_yaml(source_path)}"\n'
            "---\n\n"
            f"{metadata_block}{body}",
            encoding="utf-8",
        )

    return len(published_note_paths)


if __name__ == "__main__":
    count = sync()
    print(f"Synced {count} literature notes.")
