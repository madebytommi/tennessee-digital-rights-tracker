---
layout: default
title: Home
---

# Tennessee Digital Rights Tracker

Clear, source-linked explanations of Tennessee policies and technologies affecting privacy, civil liberties, healthcare data, LGBTQ people, and public accountability.

> This project separates verified facts from interpretation and uncertainty. It does not provide legal advice, cannot guarantee that agencies have disclosed every internal detail, and cannot independently verify nonpublic systems or security controls.

## Browse entries

{% assign sorted_entries = site.entries | sort: "date" | reverse %}
{% if sorted_entries.size > 0 %}
<ul class="entry-list">
{% for entry in sorted_entries %}
  <li>
    <a href="{{ entry.url | relative_url }}">{{ entry.title }}</a>
    <div class="entry-meta">
      {{ entry.date | date: "%B %-d, %Y" }} ·
      {{ entry.level | default: "State" }} ·
      Status: {{ entry.status | default: "Monitoring" }}
    </div>
    {% if entry.summary %}<p>{{ entry.summary }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
{% else %}
<p>No entries have been published yet. Start with the entry template.</p>
{% endif %}

## Coverage areas

- LGBTQ and transgender policy
- Government surveillance
- Health-data privacy
- Online age and identity verification
- Government AI and automated decision systems

## Submit information or corrections

Use the repository’s GitHub issue forms. Do not submit sensitive personal information.
