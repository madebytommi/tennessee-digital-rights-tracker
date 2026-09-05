"""Gemini scoring layer. Adapters never call this; discover.py does."""

from __future__ import annotations

import json
import logging
import os
import re
import time

from discovery.config import (
    COMPOSITE_THRESHOLD,
    DIGITAL_RIGHTS_THRESHOLD,
    GEMINI_API_KEY_ENV,
    GEMINI_MODEL,
    GEMINI_PAUSE_SECONDS,
    SCORE_WEIGHTS,
    TENNESSEE_THRESHOLD,
)
from discovery.types import Candidate, Evaluation, TrackerEntry

LOGGER = logging.getLogger("scout.evaluate")

JSON_FENCE_RE = re.compile(r"^```(?:json)?\s*|\s*```$", re.S)


def composite_score(scores: dict[str, float]) -> float:
    total = 0.0
    for key, weight in SCORE_WEIGHTS.items():
        total += max(0.0, min(1.0, float(scores.get(key, 0.0)))) * weight
    return round(total, 4)


def should_surface(evaluation: Evaluation) -> bool:
    return (
        evaluation.composite >= COMPOSITE_THRESHOLD
        and evaluation.tennessee_relevance >= TENNESSEE_THRESHOLD
        and evaluation.digital_rights_relevance >= DIGITAL_RIGHTS_THRESHOLD
    )


def _clamp(value: object) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return 0.0
    return max(0.0, min(1.0, number))


def parse_evaluation_payload(text: str) -> Evaluation:
    cleaned = JSON_FENCE_RE.sub("", (text or "").strip())
    try:
        payload = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Gemini did not return JSON: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError("Gemini JSON was not an object")

    scores = {
        "tennessee_relevance": _clamp(payload.get("tennessee_relevance")),
        "digital_rights_relevance": _clamp(payload.get("digital_rights_relevance")),
        "significance": _clamp(payload.get("significance")),
        "source_quality": _clamp(payload.get("source_quality")),
        "novelty": _clamp(payload.get("novelty")),
    }
    action = str(payload.get("suggested_action") or "WATCH").strip().upper()
    if action not in {"NEW ENTRY", "UPDATE EXISTING", "WATCH"}:
        action = "WATCH"
    confidence = str(payload.get("confidence") or "Low").strip().title()
    if confidence not in {"High", "Medium", "Low"}:
        confidence = "Low"
    matching = payload.get("matching_entry")
    if matching is not None:
        matching = str(matching).strip() or None
        if matching in {"null", "None", "none", "n/a", "N/A"}:
            matching = None
    return Evaluation(
        tennessee_relevance=scores["tennessee_relevance"],
        digital_rights_relevance=scores["digital_rights_relevance"],
        significance=scores["significance"],
        source_quality=scores["source_quality"],
        novelty=scores["novelty"],
        composite=composite_score(scores),
        suggested_action=action,
        confidence=confidence,
        matching_entry=matching,
        summary=str(payload.get("summary") or "").strip(),
        why_it_matters=str(payload.get("why_it_matters") or "").strip(),
        explanation=str(payload.get("explanation") or "").strip(),
    )


def _entry_briefing(entries: list[TrackerEntry], limit: int = 40) -> str:
    lines = []
    for entry in entries[:limit]:
        summary = entry.summary.replace("\n", " ")[:240]
        lines.append(
            f"- slug={entry.slug} | category={entry.category} | "
            f"title={entry.title} | source={entry.primary_source_url} | summary={summary}"
        )
    return "\n".join(lines) if lines else "(no published entries loaded)"


def build_prompt(candidate: Candidate, entries: list[TrackerEntry], matching_hint: str | None) -> str:
    extra = json.dumps(candidate.extra, ensure_ascii=True)
    keywords = ", ".join(candidate.matched_keywords) or "(none)"
    return f"""You are triaging a discovery lead for the Tennessee Digital Rights Tracker.

This is DISCOVERY ONLY. Do not treat the source as verified. Do not invent facts,
quotations, dates, holdings, or citations. If the item is outside scope, score it low.

The tracker covers Tennessee-connected developments involving:
- privacy and personal data
- government surveillance, ALPRs/Flock, facial recognition, biometrics
- government AI and automated decision systems
- social-media regulation, age/identity verification, online speech
- LGBTQ/trans digital-rights impacts
- reproductive and health-data privacy
- election systems, voter data, and civic-information infrastructure

An item belongs only if it has a meaningful Tennessee nexus AND a meaningful
connection to technology, data, records, identity, surveillance, automation,
or civic-information infrastructure.

Published tracker entries (for matching, not as evidence of this new item):
{_entry_briefing(entries)}

Candidate:
- source: {candidate.source_name} ({candidate.source_id})
- title: {candidate.title}
- url: {candidate.url}
- published_at: {candidate.published_at or "unknown"}
- matched_keywords: {keywords}
- extra: {extra}
- source_summary: {candidate.summary[:1500]}
- possible_existing_match_hint: {matching_hint or "none"}

Return JSON only, no markdown, with this exact shape:
{{
  "tennessee_relevance": 0.0,
  "digital_rights_relevance": 0.0,
  "significance": 0.0,
  "source_quality": 0.0,
  "novelty": 0.0,
  "suggested_action": "NEW ENTRY" or "UPDATE EXISTING" or "WATCH",
  "confidence": "High" or "Medium" or "Low",
  "matching_entry": "entry-slug-or-null",
  "summary": "2-3 calm factual sentences based only on the provided text",
  "why_it_matters": "2-3 sentences on digital/civil-rights significance, labeled as analysis",
  "explanation": "short scoring rationale, including uncertainties"
}}

Scoring rules (0.0 to 1.0):
- tennessee_relevance: 1 if the development is clearly about Tennessee government, law, courts, or residents; near 0 if only incidentally mentions Tennessee.
- digital_rights_relevance: 1 if the core issue is data, surveillance, identity, speech platforms, automation, or similar; near 0 if ordinary politics, crime, or policy with no digital-rights issue.
- significance: practical importance for Tennesseans' rights or government power over data/speech.
- source_quality: official records and court opinions score higher than commentary; still usable if the source is a reputable newsroom or advocacy release.
- novelty: high if this appears new relative to the published entries; low if it is already covered.

Use UPDATE EXISTING when the item is likely a development on a listed entry.
Use NEW ENTRY when it appears distinct and tracker-worthy.
Use WATCH when it may matter later but is too thin, too early, or too weakly connected.
"""


def evaluate_candidate(
    candidate: Candidate,
    entries: list[TrackerEntry],
    matching_hint: str | None = None,
    *,
    api_key: str | None = None,
) -> Evaluation:
    key = api_key if api_key is not None else os.environ.get(GEMINI_API_KEY_ENV)
    if not key:
        raise RuntimeError(f"{GEMINI_API_KEY_ENV} is not set")
    try:
        from google import genai
    except ImportError as exc:
        raise RuntimeError("google-genai is not installed") from exc

    prompt = build_prompt(candidate, entries, matching_hint)
    client = genai.Client(api_key=key)
    response = client.models.generate_content(model=GEMINI_MODEL, contents=prompt)
    text = (getattr(response, "text", None) or "").strip()
    if not text:
        raise ValueError("Gemini returned empty text")
    time.sleep(GEMINI_PAUSE_SECONDS)
    return parse_evaluation_payload(text)
