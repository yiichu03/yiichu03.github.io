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

- **CN**: {% if latest_cn %}[{{ latest_cn.title }}]({{ latest_cn.url | relative_url }}){% else %}(no post yet){% endif %}
- **EN**: {% if latest_en %}[{{ latest_en.title }}]({{ latest_en.url | relative_url }}){% else %}(no post yet){% endif %}

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
