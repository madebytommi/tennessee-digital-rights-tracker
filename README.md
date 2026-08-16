# Tennessee Digital Rights Tracker

Clear, source-linked explanations of how Tennessee laws and government technologies affect privacy, identity, personal data, and civil rights.

The project is written first for everyday Tennesseans, while maintaining sourcing and research standards useful to journalists, advocates, researchers, and public officials.

**Live site:** https://madebytommi.github.io/tennessee-digital-rights-tracker/

## Mission

Make complicated public records understandable without exaggeration.

The tracker brings together Tennessee laws, policies, court decisions, government contracts, and technology systems; explains the available evidence in plain language; and clearly identifies what the public still does not know.

## Focus areas

The tracker focuses on five areas:

1. LGBTQ and transgender rights
2. Government surveillance and tracking
3. Health-data and personal-data privacy
4. Online identity and age verification
5. Government use of artificial intelligence and automated decision systems

An issue belongs in the tracker when it has a meaningful connection to technology, data, records, identity systems, digital access, surveillance, or automated government decision-making.

## Recurring questions

Across different subjects, the tracker asks:

- What happened?
- What data are collected, created, reported, or shared?
- Who can access or use them?
- Who may be affected?
- What rights, safeguards, limits, or oversight mechanisms apply?
- What is confirmed, disputed, or still unknown?
- What lawful practical actions are available?

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
├── research/                 # Working research notes; excluded from the public site
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
python3 scripts/validate_entries.py
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
