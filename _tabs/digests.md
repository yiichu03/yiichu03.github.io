---
layout: page
# The tab name on the sidebar.
title: Daily Robotics News
icon: fas fa-robot
order: 5
---

## Daily Robotics News

A daily, source-linked digest of frontier robotics research and market demand signals.

{% assign digest_posts = site.posts | where_exp: "p", "p.categories contains 'Digest'" %}
{% assign cn_posts = digest_posts | where_exp: "p", "p.tags contains 'cn'" %}
{% assign en_posts = digest_posts | where_exp: "p", "p.tags contains 'en'" %}

{% assign latest_cn = cn_posts | first %}
{% assign latest_en = en_posts | first %}

### Today

<div class="d-flex flex-wrap gap-2 my-3">
  {% if latest_cn %}
  <a class="btn btn-primary" href="{{ latest_cn.url | relative_url }}">CN — Today</a>
  {% else %}
  <span class="btn btn-primary disabled">CN — Today (no post)</span>
  {% endif %}

  {% if latest_en %}
  <a class="btn btn-outline-primary" href="{{ latest_en.url | relative_url }}">EN — Today</a>
  {% else %}
  <span class="btn btn-outline-primary disabled">EN — Today (no post)</span>
  {% endif %}
</div>

<p class="text-muted mb-4">
  Latest CN: {% if latest_cn %}<a href="{{ latest_cn.url | relative_url }}">{{ latest_cn.title }}</a>{% else %}(none){% endif %}<br/>
  Latest EN: {% if latest_en %}<a href="{{ latest_en.url | relative_url }}">{{ latest_en.title }}</a>{% else %}(none){% endif %}
</p>

---

### Latest (CN)

{% for post in cn_posts limit: 14 %}
- {{ post.date | date: "%Y-%m-%d" }} — [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}

### Latest (EN)

{% for post in en_posts limit: 14 %}
- {{ post.date | date: "%Y-%m-%d" }} — [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}

> Tip: Use the built-in **Tags** page to filter `cn` / `en`.
