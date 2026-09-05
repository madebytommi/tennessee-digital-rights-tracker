# Tennessee Digital Rights Tracker

Clear, source-linked explanations of how Tennessee laws, government technologies, and civic-information systems affect privacy, identity, personal data, and civil rights.

The project is written first for everyday Tennesseans, while maintaining sourcing and research standards useful to journalists, advocates, researchers, and public officials.

**Live site:** https://madebytommi.github.io/tennessee-digital-rights-tracker/

## Mission

Make complicated public records understandable without exaggeration.

The tracker brings together Tennessee laws, policies, court decisions, government contracts, technology systems, and civic-information infrastructure; explains the available evidence in plain language; and clearly identifies what the public still does not know.

## Focus areas

The tracker focuses on seven areas:

1. LGBTQ and transgender rights
2. Government surveillance and tracking
3. Health-data and personal-data privacy
4. Online identity and age verification
5. Government use of artificial intelligence and automated decision systems
6. Digital civic information, political media, and information provenance
7. Election systems, voter data, eligibility verification, and election cybersecurity infrastructure

An issue belongs in the tracker when it has a meaningful connection to technology, data, records, identity systems, digital access, surveillance, automated government decision-making, election infrastructure, or civic-information infrastructure and provenance.

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

## Special Cases

Most Tracker items are ordinary entries centered on one development and one event date. A **Special Case** is reserved for a complex, ongoing investigation that requires multiple independently sourced developments to understand accurately.

Special Cases must have a meaningful Tennessee nexus, must link to at least one ordinary published Tracker entry, and must clearly distinguish documented connections from supported or merely possible relationships. They also include a mandatory section stating what the available evidence does **not** establish.

See [`docs/special-cases.md`](docs/special-cases.md) for the full rules.

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

Special Cases use [`templates/SPECIAL_CASE_TEMPLATE.md`](templates/SPECIAL_CASE_TEMPLATE.md) and are published from `_special_cases/` only after the underlying research satisfies the Special Case publication threshold.

## Repository layout

```text
.
├── _entries/                 # Published single-development tracker entries
├── _special_cases/           # Published multi-event Special Cases
├── _layouts/                 # GitHub Pages/Jekyll page layouts
├── assets/                   # CSS and other static assets
├── docs/                     # Methodology, taxonomy, policies, and roadmap
├── research/                 # Working research notes; excluded from the public site
├── discovery/                # Tennessee Rights Scout; discovery only, not publication
├── discovery-data/           # Durable scout state (seen items); not Tracker entries
├── templates/                # Authoring templates excluded from the live site
├── schemas/                  # Entry and Special Case metadata schemas
├── scripts/                  # Validation tools
├── .github/                  # Issue forms, PR template, and CI workflow
├── index.md                  # Tracker homepage
├── special-cases.md          # Special Cases landing page
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

The validator checks both ordinary entries and Special Cases, including references from entries to published Special Cases. The same validator runs in GitHub Actions for pull requests and pushes to `main`.

## Tennessee Rights Scout

The repository includes a Phase 1 discovery helper that watches a small set of public Tennessee sources and opens `discovery` GitHub Issues for human review. It does not publish entries or treat Gemini output as evidence.

See [`discovery/README.md`](discovery/README.md) for sources, scoring, local commands, and limitations.

## Publishing workflow

1. Create a branch for one entry, Special Case, or focused maintenance change.
2. Add or revise files.
3. Run the validator.
4. Open a pull request.
5. Review sourcing, uncertainty, privacy, and sensitive-data risks.
6. Merge only after validation passes.
7. Confirm the GitHub Pages result.

## Licensing

Repository code, layouts, styles, templates, and validation tooling are licensed under the [MIT License](LICENSE).

Original tracker writing is licensed under [Creative Commons Attribution 4.0 International](LICENSE-CONTENT.md), unless otherwise noted.

Government documents and third-party material retain their original legal status and ownership.
