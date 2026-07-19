# Tennessee Digital Rights Tracker

A source-first, privacy-conscious public-interest project documenting Tennessee laws, policies, court decisions, government contracts, and technology systems that affect civil liberties and digital rights.

## Mission

Make complicated public records understandable without exaggeration.

The tracker focuses on five areas:

1. LGBTQ and transgender rights
2. Government surveillance
3. Health-data privacy
4. Online identity and age verification
5. Government use of artificial intelligence and automated decision systems

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
7. What lawful actions are available?
8. When was the item last reviewed?

See [`_entries/ENTRY_TEMPLATE.md`](_entries/ENTRY_TEMPLATE.md).

## Repository layout

```text
.
├── _entries/                 # Published tracker entries
├── _layouts/                 # GitHub Pages/Jekyll page layouts
├── assets/                   # CSS and other static assets
├── docs/                     # Methodology, taxonomy, policies, roadmap
├── schemas/                  # Entry metadata schema
├── scripts/                  # Validation tools
├── .github/                  # Issue forms, PR template, CI workflow
├── index.md                  # Tracker homepage
├── about.md                  # Public project overview
└── _config.yml               # GitHub Pages configuration
```

## Local validation

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_entries.py
```

## Suggested MVP

Publish three well-sourced entries before adding advanced features.

Recommended first topics:

- Tennessee gender-related healthcare reporting and privacy
- Automated license plate readers and Flock Safety use
- Online age or identity verification proposals

## Publishing

This scaffold is designed for GitHub Pages with Jekyll.

1. Create a new GitHub repository.
2. Copy these files into it.
3. In **Settings → Pages**, select **Deploy from a branch**.
4. Choose the `main` branch and `/ (root)`.
5. Add entries under `_entries/`.

## Licensing

Suggested approach:

- Code: MIT License
- Original written content: Creative Commons Attribution 4.0
- Government documents and third-party sources retain their original status and ownership

Add the final license files before public launch.
