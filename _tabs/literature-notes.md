---
title: Literature Notes
icon: fas fa-book-open
order: 5
---

Notes synced from my local Obsidian vault.

{% assign notes = site.literature_notes | sort: 'published_at' | reverse %}

{% if notes.size > 0 %}
- Total published notes: **{{ notes.size }}**

{% for note in notes %}
- {{ note.published_at | date: "%Y-%m-%d" }} — [{{ note.title }}]({{ note.url | relative_url }})
{% endfor %}
{% else %}
No literature notes published yet.
{% endif %}
