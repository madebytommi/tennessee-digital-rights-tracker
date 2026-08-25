---
layout: default
title: Special Cases
permalink: /special-cases/
summary: Living evidence records for complex Tennessee digital-rights investigations that span multiple events, systems, agencies, or court decisions.
---

# Special Cases

Special Cases are living evidence records for subjects that cannot be represented accurately as a single dated Tracker entry. They connect individually sourced developments while keeping documented facts, supported relationships, possible relationships, and unresolved questions separate.

A Special Case must have a meaningful Tennessee nexus and at least one related published Tracker entry. National context may be included only when it is necessary to understand the Tennessee-facing system or development.

{% assign sorted_cases = site.special_cases | sort: "last_reviewed" | reverse %}
{% if sorted_cases.size > 0 %}
<ul class="special-case-list">
{% for case in sorted_cases %}
  {% assign related_entries = site.entries | where: "special_case_id", case.case_id %}
  <li class="special-case-card">
    <p class="special-case-label">Special Case · {{ case.status }}</p>
    <h2><a href="{{ case.url | relative_url }}">{{ case.title }}</a></h2>
    <p>{{ case.summary }}</p>
    <div class="entry-meta">
      {{ case.jurisdiction }} · Updated {{ case.last_reviewed | date: "%B %-d, %Y" }} · {{ related_entries.size }} related entr{% if related_entries.size == 1 %}y{% else %}ies{% endif %}
    </div>
  </li>
{% endfor %}
</ul>
{% else %}
<p>No Special Cases have been published yet.</p>
{% endif %}
