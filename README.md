# Tennessee Digital Rights Tracker

A source-first, privacy-conscious public-interest project documenting Tennessee laws, policies, court decisions, government contracts, and technology systems that affect civil liberties and digital rights.

**Live site:** https://madebytommi.github.io/tennessee-digital-rights-tracker/

## Mission

Make complicated public records understandable without exaggeration.

The tracker focuses on five areas:

1. LGBTQ and transgender rights
2. Government surveillance
3. Health-data privacy
4. Online identity and age verification
5. Government use of artificial intelligence and automated decision systems

## Current MVP coverage

The first three entries examine different parts of the same digital-rights problem:

- **Health-data privacy:** what Tennessee requires healthcare entities to report and which implementation safeguards remain unknown
- **Government surveillance:** how White House license plate readers collect and share vehicle-location records
- **Online identity:** how Tennessee’s age-verification law connects access to online speech with identity checks and data handling

Together, they ask three consistent questions: **What data are collected? Who can access them? What rights, limits, or oversight mechanisms apply?**

## Core principles

- **Primary sources first.**
- **Fact, interpretation, and prediction stay clearly separated.**
- **Corrections are public and documented.**
- **No collection of sensitive personal stories or identities.**
- **No partisan scorekeeping.**
- **No claims of anonymity or safety that the project cannot guarantee.**
- **Every entry includes a practical, lawful action section.**

## Research and legal boundaries

This project provides public-record research and plain-language analysis. It does **not** provide legal advice or a binding legal opinion.

The project and its contributors cannot:

- guarantee that a government agency has publicly disclosed every internal implementation detail;
- independently verify nonpublic databases, security controls, retention practices, access logs, or internal data-sharing arrangements; or
- replace review by a qualified attorney, privacy professional, security expert, healthcare professional, or other relevant specialist.

When public evidence is incomplete, the tracker identifies the gap rather than guessing. Especially strong legal or technical conclusions should be independently reviewed by an appropriately qualified expert.

## What this project does not store

Do not submit or publish:

- Names or identities of private individuals
- Medical records
- Immigration information
- Transition status
- Home addresses
- Protest attendance
- Volunteer lists
- Private messages
- Doxxing material
- Unredacted screenshots containing sensitive information

## Entry structure

Every tracked item answers:

1. What happened?
2. What does the primary source literally say?
3. What are officials and advocates claiming?
4. What is confirmed?
5. What remains uncertain?
6. Who may be affected?
7. Why does it matter for privacy or civil liberties?
8. What lawful actions are available?
9. When was the item last reviewed?

Use [`templates/ENTRY_TEMPLATE.md`](templates/ENTRY_TEMPLATE.md) when preparing a new entry. Files placed under `_entries/` are treated as published tracker items by Jekyll.

## Repository layout

```text
.
├── _entries/                 # Published tracker entries only
├── _layouts/                 # GitHub Pages/Jekyll page layouts
├── assets/                   # CSS and other static assets
├── docs/                     # Methodology, taxonomy, policies, and roadmap
├── templates/                # Authoring templates excluded from the live site
├── schemas/                  # Entry metadata schema
├── scripts/                  # Validation tools
├── .github/                  # Issue forms, PR template, and CI workflow
├── index.md                  # Tracker homepage
├── about.md                  # Public project overview
├── LICENSE                   # MIT license for code
├── LICENSE-CONTENT.md        # CC BY 4.0 notice for original writing
└── _config.yml               # GitHub Pages configuration
```

## Local validation

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_entries.py
```

The same validator runs in GitHub Actions for pull requests and pushes to `main`.

## Publishing workflow

1. Create a branch for one entry or focused maintenance change.
2. Add or revise files.
3. Run the validator.
4. Open a pull request.
5. Review sourcing, uncertainty, privacy, and sensitive-data risks.
6. Merge only after validation passes.
7. Confirm the GitHub Pages result.

## Licensing

- Repository code, layouts, styles, templates, and validation tooling are licensed under the [MIT License](LICENSE).
- Original tracker writing is licensed under [Creative Commons Attribution 4.0 International](LICENSE-CONTENT.md), unless otherwise noted.
- Government documents and third-party material retain their original legal status and ownership.
