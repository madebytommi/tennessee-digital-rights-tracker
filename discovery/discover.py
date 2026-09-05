#!/usr/bin/env python3
"""Tennessee Rights Scout: collect, filter, score, and surface discovery leads."""

from __future__ import annotations

import argparse
import logging
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from discovery.config import (  # noqa: E402
    DEFAULT_SEEN_PATH,
    LOOKBACK_DAYS,
    MAX_EVALUATE,
    MAX_ISSUES_PER_RUN,
    SOURCE_PAUSE_SECONDS,
)
from discovery.dedupe import (  # noqa: E402
    existing_issue_for_candidate,
    load_seen,
    mark_seen,
    match_existing_entry,
    previously_processed,
    save_seen,
)
from discovery.entries import load_tracker_entries  # noqa: E402
from discovery.evaluate import evaluate_candidate, should_surface  # noqa: E402
from discovery.issue import (  # noqa: E402
    GitHubError,
    create_discovery_issue,
    ensure_discovery_label,
    list_discovery_issues,
)
from discovery.sources import ADAPTERS, SOURCE_ORDER  # noqa: E402
from discovery.textutil import within_lookback  # noqa: E402
from discovery.types import Candidate, Evaluation  # noqa: E402

LOGGER = logging.getLogger("scout")


def configure_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Discover possible Tennessee digital-rights Tracker leads for human review."
    )
    parser.add_argument(
        "--source",
        action="append",
        dest="sources",
        choices=SOURCE_ORDER,
        help="Limit to one or more source adapters. Default: all.",
    )
    parser.add_argument("--lookback-days", type=int, default=LOOKBACK_DAYS)
    parser.add_argument("--max-evaluate", type=int, default=MAX_EVALUATE)
    parser.add_argument("--max-issues", type=int, default=MAX_ISSUES_PER_RUN)
    parser.add_argument("--dry-run", action="store_true", help="Do not create GitHub issues or write seen.json")
    parser.add_argument("--skip-gemini", action="store_true", help="Collect and filter only; do not score or open issues")
    parser.add_argument("--persist", action="store_true", help="Write discovery-data/seen.json even in dry-run")
    parser.add_argument("--no-persist", action="store_true", help="Do not write seen.json")
    parser.add_argument("--seen-path", type=Path, default=DEFAULT_SEEN_PATH)
    parser.add_argument("--repo", help="GitHub owner/name; default GITHUB_REPOSITORY")
    parser.add_argument("--verbose", action="store_true")
    return parser.parse_args(argv)


def collect_candidates(source_ids: list[str], lookback_days: int) -> list[Candidate]:
    collected: list[Candidate] = []
    for source_id in source_ids:
        adapter = ADAPTERS[source_id]
        LOGGER.info("=== source %s ===", source_id)
        try:
            kwargs = {}
            if source_id == "courtlistener":
                kwargs["lookback_days"] = lookback_days
            items = adapter(**kwargs) if kwargs else adapter()
        except Exception as exc:  # noqa: BLE001 - source failures must not abort the run
            LOGGER.warning("source %s failed: %s", source_id, exc)
            items = []
        dated = [item for item in items if within_lookback(item.published_at, lookback_days)]
        skipped_old = len(items) - len(dated)
        if skipped_old:
            LOGGER.info("source %s dropped %s item(s) outside lookback", source_id, skipped_old)
        LOGGER.info("source %s kept %s candidate(s) after lookback", source_id, len(dated))
        collected.extend(dated)
        time.sleep(SOURCE_PAUSE_SECONDS)
    return collected


def prioritize(candidates: list[Candidate]) -> list[Candidate]:
    dated = [item for item in candidates if item.published_at]
    undated = [item for item in candidates if not item.published_at]
    dated.sort(key=lambda item: item.published_at or "", reverse=True)
    return dated + undated


def collapse_same_content(candidates: list[Candidate]) -> list[Candidate]:
    """Keep one candidate per content fingerprint within a single run."""
    seen_fp: set[str] = set()
    collapsed: list[Candidate] = []
    for candidate in candidates:
        fingerprint = candidate.content_fingerprint
        if fingerprint and fingerprint in seen_fp:
            LOGGER.info(
                "REJECTED in-batch-duplicate %s same-content-as-earlier-item %s",
                candidate.candidate_id,
                candidate.title,
            )
            continue
        if fingerprint:
            seen_fp.add(fingerprint)
        collapsed.append(candidate)
    return collapsed


def matching_hint(candidate: Candidate, entries: list) -> str | None:
    match = match_existing_entry(candidate, entries)
    if not match:
        return None
    entry, reason = match
    return f"{entry.slug} ({reason})"


def should_persist(args: argparse.Namespace) -> bool:
    if args.no_persist:
        return False
    if args.persist:
        return True
    return not args.dry_run and not args.skip_gemini


def run(args: argparse.Namespace) -> int:
    source_ids = list(args.sources) if args.sources else list(SOURCE_ORDER)
    LOGGER.info(
        "Tennessee Rights Scout starting sources=%s lookback=%sd dry_run=%s skip_gemini=%s",
        ",".join(source_ids),
        args.lookback_days,
        args.dry_run,
        args.skip_gemini,
    )

    seen = load_seen(args.seen_path)
    entries = load_tracker_entries()
    LOGGER.info("Loaded %s published tracker item(s) for matching", len(entries))

    issue_index: list[dict] = []
    if not args.dry_run and not args.skip_gemini and os.environ.get("GITHUB_TOKEN"):
        try:
            ensure_discovery_label(args.repo)
            issue_index = list_discovery_issues(args.repo)
        except GitHubError as exc:
            LOGGER.warning("GitHub issue index unavailable: %s", exc)

    raw_candidates = collect_candidates(source_ids, args.lookback_days)
    LOGGER.info("Collected %s keyword-matching candidate(s) before dedupe", len(raw_candidates))

    fresh: list[Candidate] = []
    for candidate in prioritize(raw_candidates):
        seen_reason = previously_processed(seen, candidate)
        if seen_reason:
            LOGGER.info("REJECTED duplicate-seen %s [%s] %s", candidate.candidate_id, seen_reason, candidate.title)
            continue
        entry_match = match_existing_entry(candidate, entries)
        if entry_match and entry_match[1].startswith(("primary-source-url", "url-in-entry", "identifier:")):
            entry, reason = entry_match
            LOGGER.info(
                "REJECTED duplicate-entry %s matches %s (%s)",
                candidate.candidate_id,
                entry.slug,
                reason,
            )
            mark_seen(seen, candidate, "duplicate-entry", matching_entry=entry.slug)
            continue
        existing_issue = existing_issue_for_candidate(candidate, issue_index)
        if existing_issue:
            LOGGER.info(
                "REJECTED duplicate-issue %s already issue #%s",
                candidate.candidate_id,
                existing_issue.get("number"),
            )
            mark_seen(
                seen,
                candidate,
                "duplicate-issue",
                issue_number=existing_issue.get("number"),
            )
            continue
        fresh.append(candidate)

    fresh = collapse_same_content(fresh)
    LOGGER.info("%s candidate(s) remain after dedupe", len(fresh))
    to_evaluate = fresh[: args.max_evaluate]
    overflow = fresh[args.max_evaluate :]
    if overflow:
        LOGGER.info(
            "Holding %s candidate(s) for a later run because max-evaluate=%s",
            len(overflow),
            args.max_evaluate,
        )

    if args.skip_gemini:
        for candidate in to_evaluate:
            LOGGER.info(
                "SKIP-GEMINI %s %s keywords=%s url=%s",
                candidate.candidate_id,
                candidate.title,
                ",".join(candidate.matched_keywords),
                candidate.url,
            )
        if should_persist(args):
            save_seen(seen, args.seen_path)
            LOGGER.info("Wrote seen state to %s", args.seen_path)
        return 0

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        LOGGER.warning("GEMINI_API_KEY is not set; collected leads will not be scored or surfaced")
        return 0

    opened = 0
    for candidate in to_evaluate:
        hint = matching_hint(candidate, entries)
        LOGGER.info("SCORING %s %s", candidate.candidate_id, candidate.title)
        try:
            evaluation: Evaluation = evaluate_candidate(candidate, entries, hint, api_key=api_key)
        except Exception as exc:  # noqa: BLE001
            LOGGER.warning("Gemini scoring failed for %s: %s", candidate.candidate_id, exc)
            continue
        LOGGER.info(
            "SCORED %s composite=%.2f tn=%.2f rights=%.2f action=%s confidence=%s match=%s",
            candidate.candidate_id,
            evaluation.composite,
            evaluation.tennessee_relevance,
            evaluation.digital_rights_relevance,
            evaluation.suggested_action,
            evaluation.confidence,
            evaluation.matching_entry or hint or "none",
        )
        if not should_surface(evaluation):
            LOGGER.info("REJECTED below-threshold %s composite=%.2f", candidate.candidate_id, evaluation.composite)
            mark_seen(
                seen,
                candidate,
                "below-threshold",
                composite=evaluation.composite,
                suggested_action=evaluation.suggested_action,
            )
            continue
        if opened >= args.max_issues:
            LOGGER.info("Holding %s; max-issues=%s already reached", candidate.candidate_id, args.max_issues)
            continue
        try:
            result = create_discovery_issue(
                candidate,
                evaluation,
                matching_entry=(hint.split()[0] if hint else evaluation.matching_entry),
                repo=args.repo,
                dry_run=args.dry_run,
            )
        except GitHubError as exc:
            LOGGER.warning("Could not open issue for %s: %s", candidate.candidate_id, exc)
            continue
        if result and not result.get("dry_run"):
            opened += 1
            mark_seen(
                seen,
                candidate,
                "issue-created",
                issue_number=result.get("number"),
                composite=evaluation.composite,
                suggested_action=evaluation.suggested_action,
            )
            LOGGER.info("SURFACED issue #%s for %s", result.get("number"), candidate.candidate_id)
        elif result and result.get("dry_run"):
            opened += 1
            LOGGER.info("SURFACED dry-run issue for %s", candidate.candidate_id)
        else:
            mark_seen(
                seen,
                candidate,
                "below-threshold",
                composite=evaluation.composite,
                suggested_action=evaluation.suggested_action,
            )

    LOGGER.info("Run complete. Surfaced %s lead(s).", opened)
    if should_persist(args):
        save_seen(seen, args.seen_path)
        LOGGER.info("Wrote seen state to %s", args.seen_path)
    elif args.dry_run:
        LOGGER.info("Dry-run: not writing %s", args.seen_path)
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    configure_logging(args.verbose)
    try:
        return run(args)
    except KeyboardInterrupt:
        LOGGER.warning("Interrupted")
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
