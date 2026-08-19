---
layout: default
title: Home
summary: Clear, source-linked explanations of how Tennessee laws, government technologies, and civic-information systems affect privacy, identity, personal data, and civil rights.
---

<p class="project-kicker">Clear public-interest research for Tennessee</p>

# Tennessee Digital Rights Tracker

<p class="lede"><strong>Understand how Tennessee laws, government technology, and civic-information systems affect your privacy and civil rights.</strong></p>

The Tennessee Digital Rights Tracker turns complicated laws, contracts, court decisions, public records, and civic-information systems into clear explanations for everyday Tennesseans.

Use the tracker to learn what the government is doing, what personal information may be collected or shared, how civic information may be produced or distributed, who may be affected, what protections or oversight exist, what remains unknown, and what lawful actions are available.

[**Browse the tracker**](#browse-entries) · [About the project]({{ '/about/' | relative_url }})

<div class="notice">
  <strong>How this site works:</strong> Every entry keeps confirmed facts, official statements, outside criticism, project analysis, and unanswered questions separate. Sources are linked so readers can examine the evidence themselves. This project does not provide legal advice or claim access to nonpublic systems.
</div>

## What we track

<div class="coverage-grid">
  <section class="coverage-card">
    <h3>Surveillance and tracking</h3>
    <p>Police cameras, license-plate readers, facial recognition, data sharing, and other technologies used to monitor people or vehicles.</p>
  </section>
  <section class="coverage-card">
    <h3>Personal and healthcare data</h3>
    <p>Laws and government systems that collect, report, store, or share sensitive personal and medical information.</p>
  </section>
  <section class="coverage-card">
    <h3>Online identity and access</h3>
    <p>Age verification, identity checks, online speech restrictions, and rules that may require personal information to access websites or services.</p>
  </section>
  <section class="coverage-card">
    <h3>LGBTQ and transgender rights</h3>
    <p>Policies involving identity records, healthcare systems, online access, privacy, and technology that may disproportionately affect LGBTQ people.</p>
  </section>
  <section class="coverage-card">
    <h3>Government artificial intelligence</h3>
    <p>Algorithms, automated decision systems, and artificial intelligence used by Tennessee state or local government agencies.</p>
  </section>
  <section class="coverage-card">
    <h3>Digital civic information</h3>
    <p>Political media, synthetic content, information provenance, targeting, and digital systems that shape how Tennesseans encounter election, government, or public-policy information.</p>
  </section>
</div>

## Why this matters

Government technology and civic-information systems can affect where people travel, how they access healthcare, what they can view online, how their identity is recorded, and how they encounter information about elections and public life.

These systems are often described through technical language, lengthy legislation, scattered public records, or unclear ownership and production methods. This project brings the available evidence together, explains it plainly, and clearly identifies what the public still does not know.

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

## What each entry includes

Each researched issue provides a plain-language summary, links to primary sources, confirmed facts, unresolved questions, information about who may be affected, privacy or civil-rights concerns, a confidence level, a review date, and practical lawful next steps.

## Independent, careful, and privacy-conscious

This is a nonpartisan public-interest research project. It does not provide legal advice, collect dossiers about private individuals, or publish sensitive personal information.

When the available evidence does not support a conclusion, the tracker says so.

## Submit information or corrections

Use the repository’s [GitHub issue forms](https://github.com/madebytommi/tennessee-digital-rights-tracker/issues/new/choose). Do not submit sensitive personal information, confidential movement histories, medical records, or active-investigation details.
