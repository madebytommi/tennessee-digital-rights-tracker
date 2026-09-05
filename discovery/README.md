# Tennessee Rights Scout

The scout is a Phase 1 discovery helper. It watches a small set of public Tennessee sources, keeps items that look relevant to this Tracker's existing topics, scores them with Gemini, and opens GitHub Issues for human review.

It does **not** publish Tracker entries, edit `_entries/`, or treat model output as evidence.

## What Phase 1 does

1. Collect records from source adapters.
2. Normalize them into a common candidate format.
3. Filter by digital-rights keyword/topic lists already covered by the Tracker.
4. Deduplicate against `discovery-data/seen.json`, published entries, and open `discovery` issues.
5. Ask Gemini to score remaining candidates.
6. Open a `discovery` GitHub Issue for high-scoring leads.
7. Record processed items in `discovery-data/seen.json`.

## Sources

| Adapter | What it collects | Method |
| --- | --- | --- |
| `general-assembly` | Current-session bills matching legislative search terms | Tennessee General Assembly bill search HTML |
| `attorney-general` | AG news releases and formal opinions | `tn.gov` HTML |
| `courtlistener` | Recent Sixth Circuit and Tennessee federal-court opinions | CourtListener Search API v4 |
| `aclu-tn` | ACLU of Tennessee press releases | `https://www.aclu-tn.org/press-releases/feed/` |
| `lookout` | Tennessee Lookout stories | `https://tennesseelookout.com/feed/` |

Adapters only collect and normalize. Gemini evaluation is a separate layer in `evaluate.py`. If one source is down, the run continues.

## Scoring

Gemini (`gemini-2.5-flash`, the same model already used by the repository's PR review workflows) assigns 0–1 scores for:

- Tennessee relevance
- digital/civil-rights relevance
- significance
- source quality
- novelty

It also suggests `NEW ENTRY`, `UPDATE EXISTING`, or `WATCH`, names a possible matching entry when it can, and writes a short summary. Those values are triage aids. They are not findings and must not be copied into a published entry without independent research.

A candidate is surfaced only when:

- composite score ≥ 0.62
- Tennessee relevance ≥ 0.45
- digital-rights relevance ≥ 0.45

Each run also caps Gemini evaluations and issue creation so a noisy day cannot flood the issue tracker.

## GitHub Issues

High-scoring leads open an issue labeled `discovery` with:

- title
- source
- source URL
- short summary
- relevance scores
- confidence
- suggested action
- possible matching Tracker entry
- why it may matter

The issue body states that the item is an automated lead, not a published entry.

## Local use

From the repository root:

```bash
python3 -m pip install -r requirements-dev.txt -r discovery/requirements.txt
python3 -m unittest discover -s discovery/tests -t .
python3 -m discovery.discover --help
python3 -m discovery.discover --dry-run --skip-gemini
```

Useful flags:

- `--source lookout` (repeatable)
- `--dry-run` — no GitHub issues, no `seen.json` write unless `--persist`
- `--skip-gemini` — collect and filter only
- `--max-evaluate 10 --max-issues 3`

Environment:

- `GEMINI_API_KEY` — required to score and surface leads (same secret as the existing Gemini PR workflows)
- `GITHUB_TOKEN` and `GITHUB_REPOSITORY` — required to create issues
- `COURTLISTENER_TOKEN` — optional; anonymous CourtListener requests are attempted first

## GitHub Actions

`.github/workflows/discovery.yml` runs once a day and on `workflow_dispatch`. It installs dependencies, runs unit tests, runs the scout, creates issues with `GITHUB_TOKEN`, and commits `discovery-data/seen.json` when the state changes.

If branch protection later blocks the bot from pushing to `main`, issues can still be created; duplicate protection then relies more on open `discovery` issues than on `seen.json`. A maintainer would need to allow the workflow to update the state file.

## Known Phase 1 limitations

- General Assembly search results do not include reliable action dates, so bill candidates are current-session matches rather than “filed today.”
- Keyword filters will miss jargon-only records and will over-include some weakly related hits; Gemini is the second filter, not a substitute for human review.
- CourtListener coverage is recent Sixth Circuit plus Tennessee federal district opinions, not every state trial court.
- The ACLU site-wide `/feed/` is stale; the scout uses the press-release feed instead.
- Items marked seen are not re-scored when keywords later expand.
- The scout does not archive pages, fetch bill PDFs, or verify current operational status.
- No Atlas of Surveillance, procurement, or local-government meeting adapters yet.

## Phase 2 ideas

- Atlas of Surveillance and local procurement/meeting sources
- Bill last-action dates and companion-bill pairing from bill-info pages
- Stronger matching against open research issues, not just published entries
- Human accept/reject workflow that feeds back into `seen.json`
- Optional digest instead of one GitHub Issue per lead
- Broader court coverage and docket filings, not only opinions
