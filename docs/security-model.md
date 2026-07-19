# Security Model

## Protected assets

- Accuracy and integrity of published entries
- Contributor account security
- Source preservation
- Website availability
- The privacy of people discussed in public records

## Main threats

- Account takeover
- Malicious or misleading pull requests
- Doxxing submitted through issues
- Link rot
- Source alteration
- Defacement
- Scraping of unnecessarily aggregated personal data
- False claims of anonymity or safety
- Legal demands directed at the hosting platform

## Baseline controls

- Require multi-factor authentication for maintainers
- Use branch protection
- Require pull-request review
- Run metadata validation in CI
- Keep local backups
- Preserve source URLs and retrieval dates
- Avoid secrets in the repository
- Remove sensitive information from issues promptly
- Do not accept executable code from untrusted contributors without review

## Out of scope

This repository is not designed to securely store:

- Leaks
- Whistleblower identities
- Medical files
- Legal case files
- Protest plans
- Private organizational records
