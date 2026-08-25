# Agent Instructions

These instructions apply to coding, browser, research, and autonomous agents working in this repository, regardless of vendor or tool.

## Repository authority

Repository-specific policies, schemas, templates, and validation rules are authoritative and mandatory. Read the documents governing the task before substantive work; do not rely on memory or summaries when the current file is available.

Use task routing rather than reading every policy for every task. When this file conflicts with a more specific authoritative repository document for its subject, the more specific document governs.

- Research procedure: `docs/research-protocol.md`
- Evidence standards and research boundaries: `docs/methodology.md`
- Public-facing tone and corrections: `docs/editorial-policy.md`
- Entry categories and tags: `docs/taxonomy.md`
- Special Case rules: `docs/special-cases.md`
- Machine-valid entry metadata: `schemas/entry.schema.json` and `scripts/validate_entries.py`
- Machine-valid Special Case metadata: `schemas/special-case.schema.json` and `scripts/validate_entries.py`
- Entry structure: `templates/ENTRY_TEMPLATE.md`
- Special Case structure: `templates/SPECIAL_CASE_TEMPLATE.md`
- Privacy and security: `docs/privacy-policy.md`, `docs/security-model.md`, and `SECURITY.md`
- Contribution and pull-request process: `CONTRIBUTING.md` and `.github/pull_request_template.md`

## Required reading by task

### Any substantive repository change

Read `README.md` and `CONTRIBUTING.md`.

### Researching a possible Tracker issue

Read `docs/research-protocol.md` and `docs/methodology.md`. The research protocol is the operational authority for issue research.

When a substantive investigation needs a persistent working record, use `templates/RESEARCH_NOTES_TEMPLATE.md` as the standard structure. A full research note is not required for a trivial source check or tiny factual correction where it would add unnecessary overhead.

For surveillance, ALPR, or police-technology research, also follow the Atlas of Surveillance discovery-source rules in `docs/methodology.md`.

### Creating a new published Tracker entry

Read `docs/research-protocol.md`, `docs/methodology.md`, `docs/editorial-policy.md`, `docs/taxonomy.md`, `templates/ENTRY_TEMPLATE.md`, `schemas/entry.schema.json`, and `CONTRIBUTING.md`.

### Creating or updating a Special Case

Read everything required for a new published Tracker entry plus `docs/special-cases.md`, `templates/SPECIAL_CASE_TEMPLATE.md`, and `schemas/special-case.schema.json`.

A Special Case is a synthesis layer, not a shortcut around entry-level research. Do not create a published Special Case until its Tennessee nexus is supported, at least one related ordinary entry is publication-ready and linked, and the case satisfies the publication threshold in `docs/special-cases.md`.

Do not treat chronology, shared institutions, policy similarity, or political context as proof of coordination, motive, causation, or operational linkage. Use the relationship labels in `docs/special-cases.md` and preserve material evidence that weakens the working theory.

### Updating an existing entry

Read everything required for a new entry, plus the existing entry, its revision history, and relevant prior sources where necessary.

If the entry has `special_case_id`, also read the linked Special Case and `docs/special-cases.md` so the relationship remains accurate.

### Correcting a factual error

Read the target entry, `docs/research-protocol.md`, `docs/methodology.md`, `docs/editorial-policy.md`, and `CONTRIBUTING.md`.

### Changing categories, statuses, confidence values, or front matter

Read `docs/taxonomy.md`, `schemas/entry.schema.json`, `templates/ENTRY_TEMPLATE.md`, and the relevant status and confidence sections of `docs/methodology.md`.

For Special Case metadata, also read `docs/special-cases.md`, `schemas/special-case.schema.json`, and `templates/SPECIAL_CASE_TEMPLATE.md`.

The schema and validator control literal machine-valid front-matter values. Do not use the conceptual prose label `Blocked or Enjoined` where the schema requires either `Blocked` or `Enjoined`. Likewise, `Repealed`, `Expired`, and `Resolved` are distinct schema values.

### Website, layout, CSS, or navigation work

Read `README.md` and the relevant implementation files. Also read `docs/privacy-policy.md` if the feature could affect tracking, embeds, forms, accounts, or data collection.

### Analytics, forms, embeds, comments, accounts, tracking, or data collection

Read `docs/privacy-policy.md`, `docs/security-model.md`, `README.md`, and `docs/roadmap.md`. Do not introduce functionality that violates those policies.

### Security-sensitive changes

Read `SECURITY.md`, `docs/security-model.md`, and the relevant implementation files.

### Sensitive submissions or personal information

Read `SECURITY.md`, `docs/security-model.md`, and `docs/privacy-policy.md`.

### New feature planning or architectural expansion

Read `README.md` and `docs/roadmap.md`. Read the privacy and security policies when the proposed work could affect those areas.

### Preparing or opening a pull request

Read `CONTRIBUTING.md` and `.github/pull_request_template.md`.

### Changing validation, schema, templates, or entry tooling

Read `schemas/entry.schema.json`, `schemas/special-case.schema.json` when applicable, `scripts/validate_entries.py`, `templates/ENTRY_TEMPLATE.md`, `templates/SPECIAL_CASE_TEMPLATE.md` when applicable, and representative files under `_entries/`.

Do not load unrelated implementation files for pure research tasks. `docs/roadmap.md` is primarily for feature planning and architectural expansion; privacy and security policies become mandatory when a task touches data collection, tracking, sensitive content, accounts, embeds, or security.

## Repository-wide non-negotiable rules

- Do not invent sources, citations, facts, quotations, dates, or document contents.
- Do not claim to have inspected a document or URL that was not actually opened.
- Do not treat AI-generated text or search-result snippets as evidence.
- Do not force evidence to support the starting hypothesis.
- Preserve uncertainty and contradictory evidence.
- Do not infer absence from failure to locate a public record.
- Do not state motive as fact without direct evidence.
- Do not publish or unnecessarily reproduce sensitive personal information.
- Do not claim anonymity or guaranteed safety.
- Do not automatically publish AI-generated research.
- Do not perform unrelated cleanup, refactoring, formatting, or policy rewriting during focused tasks.
- Do not bypass branch protection or required checks.
- Do not force-push protected `main` or push directly to it.
- Use focused branches, focused commits, and pull requests for changes.
- Research quality and technical validity are separate requirements; satisfy both.

## Research behavior

Follow `docs/research-protocol.md` throughout research and handoff work.

- Treat discovery sources as leads, not automatic proof.
- Seek primary records whenever reasonably available.
- Verify important current-status claims separately from historical evidence.
- Do not infer local configuration from a vendor's available capabilities.
- Report material contradictions, inaccessible sources, and unresolved questions.
- Allow evidence to confirm, narrow, qualify, contradict, or leave the original lead unresolved.

## Public-facing writing

Follow `docs/editorial-policy.md`. Public Tracker prose must use plain, calm language; attribute interpretations; distinguish fact from analysis and prediction; avoid unsupported motive claims and outrage-style framing; and document material corrections.

## Entry authoring

Use `templates/ENTRY_TEMPLATE.md` for new published entries and conform front matter to `schemas/entry.schema.json` and the validator.

Files under `_entries/` are published Tracker items, not scratch research notes. Do not create a new `_entries/` file until the underlying research is publication-ready under `docs/research-protocol.md`.

Use `templates/SPECIAL_CASE_TEMPLATE.md` for published Special Cases and conform front matter to `schemas/special-case.schema.json`, `docs/special-cases.md`, and the validator.

Files under `_special_cases/` are published synthesis records, not scratch research notes. Substantive Special Case investigations should maintain their working evidence under `research/` before publication.

## Validation and diff review

For changes touching `_entries/`, `_special_cases/`, `templates/ENTRY_TEMPLATE.md`, `templates/SPECIAL_CASE_TEMPLATE.md`, `schemas/entry.schema.json`, `schemas/special-case.schema.json`, or `scripts/validate_entries.py`, run at minimum:

```bash
python3 scripts/validate_entries.py
```

For repository changes, also run:

```bash
git diff --check
```

Use `python3`, not `python`, because `python` may not exist in common macOS environments. For other changes, run the relevant repository checks without inventing unnecessary validation work.

Before committing, inspect the complete diff and remove unrelated changes or generated artifacts from the proposed commit.

## Git and pull requests

- Start from current remote state and work on a focused branch.
- Keep commits limited to the authorized task.
- Push the branch and open a pull request into `main`.
- Complete the repository pull-request checklist.
- Wait for required checks to pass and obtain human review where appropriate.
- Do not merge unless the task explicitly authorizes it.
- Never bypass repository protections to complete a task.
