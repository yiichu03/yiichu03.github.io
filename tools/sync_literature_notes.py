#!/usr/bin/env python3

from __future__ import annotations

import re
import shutil
from datetime import datetime, timezone
from pathlib import Path


REPO_DIR = Path(__file__).resolve().parent.parent
VAULT_DIR = REPO_DIR.parent
SOURCE_DIR = VAULT_DIR / "10 Literature Notes"
ATTACHMENTS_DIR = VAULT_DIR / "Attachments"
OUTPUT_DIR = REPO_DIR / "_literature_notes"
ASSET_DIR = REPO_DIR / "assets" / "literature"

WIKILINK_RE = re.compile(r"(!)?\[\[([^\]]+)\]\]")


def slugify(value: str) -> str:
    value = value.strip().replace("/", "-")
    value = re.sub(r"\s+", "-", value, flags=re.UNICODE)
    value = re.sub(r"[^\w\-]+", "", value, flags=re.UNICODE)
    value = re.sub(r"-+", "-", value, flags=re.UNICODE).strip("-")
    return value or "note"


def escape_yaml(value: str) -> str:
    return value.replace('"', '\\"')


def strip_front_matter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return text
    return parts[1]


def extract_title(text: str, fallback: str) -> tuple[str, str]:
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

    note_paths = sorted(SOURCE_DIR.rglob("*.md"))
    note_index = build_note_index(note_paths)

    shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
    shutil.rmtree(ASSET_DIR, ignore_errors=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / ".gitkeep").write_text("\n", encoding="utf-8")
    (ASSET_DIR / ".gitkeep").write_text("\n", encoding="utf-8")

    copied_assets: dict[Path, str] = {}

    for note_path in note_paths:
        source_text = note_path.read_text(encoding="utf-8")
        body = strip_front_matter(source_text)
        fallback_title = note_path.stem
        title, body = extract_title(body, fallback_title)
        body = render_links(body, note_path, note_index, copied_assets).rstrip() + "\n"

        rel = note_path.relative_to(SOURCE_DIR).with_suffix("")
        slug = slugify(rel.as_posix())
        updated_at = datetime.fromtimestamp(note_path.stat().st_mtime, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S %z")
        source_path = note_path.relative_to(VAULT_DIR).as_posix()
        output_path = OUTPUT_DIR / f"{slug}.md"

        output_path.write_text(
            "---\n"
            f'title: "{escape_yaml(title)}"\n'
            f'slug: "{escape_yaml(slug)}"\n'
            f'updated_at: {updated_at}\n'
            f'source_path: "{escape_yaml(source_path)}"\n'
            "---\n\n"
            f"{body}",
            encoding="utf-8",
        )

    return len(note_paths)


if __name__ == "__main__":
    count = sync()
    print(f"Synced {count} literature notes.")
