---
layout: default
title: Home
---

<p class="project-kicker">Source-first civic technology for Tennessee</p>

# Tennessee Digital Rights Tracker

Clear, source-linked explanations of Tennessee policies and technologies affecting privacy, civil liberties, healthcare data, LGBTQ people, and public accountability.

<div class="notice">
  <strong>How to read this tracker:</strong> verified facts, official positions, outside criticism, project analysis, and unresolved questions are kept separate. This project does not provide legal advice or claim access to nonpublic systems.
</div>

## What the MVP covers

<div class="coverage-grid">
  <section class="coverage-card">
    <h3>Health-data privacy</h3>
    <p>What Tennessee requires healthcare entities to report, what privacy protections exist, and which implementation details remain unknown.</p>
  </section>
  <section class="coverage-card">
    <h3>Government surveillance</h3>
    <p>How local license plate readers collect and share location records, what state safeguards apply, and what oversight records are missing.</p>
  </section>
  <section class="coverage-card">
    <h3>Online identity</h3>
    <p>How age-verification laws connect access to online speech with identity checks, data retention, security, and exclusion risks.</p>
  </section>
</div>

Together, these entries examine three connected questions: **what data are collected, who can access them, and what rights or safeguards apply.**

## Browse entries

{% assign sorted_entries = site.entries | sort: "date" | reverse %}
{% if sorted_entries.size > 0 %}
<p class="entry-count">{{ sorted_entries.size }} published entries.</p>
<ul class="entry-list">
{% for entry in sorted_entries %}
  {% assign category_label = entry.category | replace: "-", " " | capitalize %}
  <li>
    <div class="entry-list-top">
      <span class="badge">{{ category_label }}</span>
      <span class="entry-meta">{{ entry.jurisdiction | default: entry.level }}</span>
    </div>
    <h3><a href="{{ entry.url | relative_url }}">{{ entry.title }}</a></h3>
    <div class="entry-meta">
      Status: {{ entry.status | default: "Monitoring" }} ·
      Confidence: {{ entry.confidence | default: "Medium" }} ·
      Reviewed {{ entry.last_reviewed | default: entry.date | date: "%B %-d, %Y" }}
    </div>
    {% if entry.summary %}<p>{{ entry.summary }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
{% else %}
<p>No researched entries have been published yet.</p>
{% endif %}

## Coverage areas

The tracker may expand into LGBTQ and transgender policy, government surveillance, health-data privacy, online identity and age verification, and government AI or automated decision systems.

## Submit information or corrections

Use the repository’s [GitHub issue forms](https://github.com/madebytommi/tennessee-digital-rights-tracker/issues/new/choose). Do not submit sensitive personal information, confidential movement histories, medical records, or active-investigation details.
