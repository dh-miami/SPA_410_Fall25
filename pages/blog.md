---
layout: page
title: Blog
permalink: /blog/
---

<h1>Course Blog</h1>

<ul class="post-list">
  {% for post in site.posts %}
  <li>
    <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    <p><small>{{ post.date | date: "%B %d, %Y" }}</small></p>
    <p>{{ post.excerpt }}</p>
  </li>
  {% endfor %}
</ul>