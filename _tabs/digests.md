---
layout: page
# The tab name on the sidebar.
title: Digests
icon: fas fa-robot
order: 5
---

## Daily Robotics Digests

- **CN**: posts tagged `cn`
- **EN**: posts tagged `en`

### Latest

{% assign digests = site.posts | where_exp: "p", "p.categories contains 'Digest'" %}

{% for post in digests limit: 30 %}
- {{ post.date | date: "%Y-%m-%d" }} — [{{ post.title }}]({{ post.url | relative_url }})
  {% if post.tags %}
  - Tags: {% for t in post.tags %}`{{ t }}`{% unless forloop.last %} {% endunless %}{% endfor %}
  {% endif %}
{% endfor %}

> Tip: Use the built-in **Tags** page to filter `cn` / `en`.
