"""Gemini scoring layer. Adapters never call this; discover.py does."""

from __future__ import annotations

import json
import logging
import os
import re
import time
from collections.abc import Callable

from discovery.config import (
    COMPOSITE_THRESHOLD,
    DIGITAL_RIGHTS_THRESHOLD,
    GEMINI_API_KEY_ENV,
    GEMINI_MAX_ATTEMPTS,
    GEMINI_RATE_LIMIT_FALLBACK_SECONDS,
    GEMINI_UNAVAILABLE_INITIAL_BACKOFF_SECONDS,
    GEMINI_UNAVAILABLE_MAX_BACKOFF_SECONDS,
    SCORE_WEIGHTS,
    TENNESSEE_THRESHOLD,
    gemini_min_interval_seconds,
    gemini_model,
)
from discovery.types import Candidate, Evaluation, TrackerEntry

LOGGER = logging.getLogger("scout.evaluate")

JSON_FENCE_RE = re.compile(r"^```(?:json)?\s*|\s*```$", re.S)
DURATION_RE = re.compile(
    r"^\s*(?:(?P<hours>\d+(?:\.\d+)?)h)?(?:(?P<minutes>\d+(?:\.\d+)?)m)?"
    r"(?:(?P<seconds>\d+(?:\.\d+)?)s)?\s*$",
    re.I,
)

_last_gemini_request_start: float | None = None


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

If the hint starts with "UPDATE EXISTING", the scout already matched this candidate
to a published Tracker entry by bill number, public chapter, primary-source URL, or
similar identifier. That is a strong signal. Prefer suggested_action "UPDATE EXISTING"
and set matching_entry to that slug unless the item is clearly a distinct development.

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

Use UPDATE EXISTING when the item is likely a development on a listed entry, especially when the scout supplied an UPDATE EXISTING hint.
Use NEW ENTRY when it appears distinct and tracker-worthy.
Use WATCH when it may matter later but is too thin, too early, or too weakly connected.
"""


def reset_gemini_pacing() -> None:
    """Clear the Gemini start-to-start clock. Tests call this between cases."""
    global _last_gemini_request_start
    _last_gemini_request_start = None


def classify_gemini_error(exc: BaseException) -> str:
    """Return 'rate_limit', 'unavailable', or 'permanent'."""
    code_int: int | None
    try:
        code_int = int(getattr(exc, "code", None))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        code_int = None
    status = str(getattr(exc, "status", "") or "").upper().replace(" ", "_")
    message = str(getattr(exc, "message", "") or str(exc)).upper()

    if code_int == 429 or status == "RESOURCE_EXHAUSTED" or "RESOURCE_EXHAUSTED" in message:
        return "rate_limit"
    if code_int == 503 or status == "UNAVAILABLE":
        return "unavailable"
    return "permanent"


def _duration_to_seconds(value: object) -> float | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value) if value >= 0 else None
    if isinstance(value, dict):
        seconds = value.get("seconds", 0) or 0
        nanos = value.get("nanos", 0) or 0
        try:
            return max(0.0, float(seconds) + float(nanos) / 1_000_000_000)
        except (TypeError, ValueError):
            return None
    text = str(value).strip()
    if not text:
        return None
    try:
        return max(0.0, float(text))
    except ValueError:
        pass
    match = DURATION_RE.match(text)
    if not match or not any(match.groups()):
        return None
    hours = float(match.group("hours") or 0)
    minutes = float(match.group("minutes") or 0)
    seconds = float(match.group("seconds") or 0)
    return hours * 3600 + minutes * 60 + seconds


def _find_retry_delay(obj: object) -> float | None:
    if isinstance(obj, dict):
        for key in ("retryDelay", "retry_delay"):
            if key in obj:
                parsed = _duration_to_seconds(obj[key])
                if parsed is not None:
                    return parsed
        for value in obj.values():
            parsed = _find_retry_delay(value)
            if parsed is not None:
                return parsed
    elif isinstance(obj, (list, tuple)):
        for item in obj:
            parsed = _find_retry_delay(item)
            if parsed is not None:
                return parsed
    return None


def parse_retry_delay_seconds(exc: BaseException) -> float | None:
    """Read Google's retry delay from headers or error details when present."""
    response = getattr(exc, "response", None)
    headers = getattr(response, "headers", None) or {}
    header_value = None
    try:
        header_value = headers.get("Retry-After") or headers.get("retry-after")
    except (AttributeError, TypeError):
        header_value = None
    if header_value:
        parsed = _duration_to_seconds(header_value)
        if parsed is not None:
            return parsed
    for blob in (getattr(exc, "details", None), getattr(exc, "message", None)):
        parsed = _find_retry_delay(blob)
        if parsed is not None:
            return parsed
    return None


def wait_for_gemini_slot(
    *,
    clock: Callable[[], float] | None = None,
    sleeper: Callable[[float], None] | None = None,
    min_interval: float | None = None,
) -> None:
    """Sleep only as needed so Gemini request starts stay at least min_interval apart."""
    global _last_gemini_request_start
    clock = clock or time.monotonic
    sleeper = sleeper or time.sleep
    interval = gemini_min_interval_seconds() if min_interval is None else min_interval
    now = clock()
    last = _last_gemini_request_start
    if last is not None and interval > 0:
        remaining = interval - (now - last)
        if remaining > 0:
            LOGGER.debug("Pacing Gemini: waiting %.1fs before next request", remaining)
            sleeper(remaining)
            now = clock()
    _last_gemini_request_start = now


def unavailable_backoff_seconds(failed_attempt: int) -> float:
    """Bounded exponential backoff after a 503/UNAVAILABLE failure."""
    exponent = max(0, failed_attempt - 1)
    delay = GEMINI_UNAVAILABLE_INITIAL_BACKOFF_SECONDS * (2**exponent)
    return min(delay, GEMINI_UNAVAILABLE_MAX_BACKOFF_SECONDS)


def invoke_gemini(prompt: str, api_key: str, model: str) -> str:
    try:
        from google import genai
    except ImportError as exc:
        raise RuntimeError("google-genai is not installed") from exc

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(model=model, contents=prompt)
    text = (getattr(response, "text", None) or "").strip()
    if not text:
        raise ValueError("Gemini returned empty text")
    return text


def call_gemini_with_retry(
    generate: Callable[[], str],
    *,
    candidate_id: str = "",
    sleeper: Callable[[float], None] | None = None,
    clock: Callable[[], float] | None = None,
    min_interval: float | None = None,
    max_attempts: int | None = None,
) -> str:
    """Pace Gemini calls and retry transient 429/503 errors for one candidate."""
    sleeper = sleeper or time.sleep
    clock = clock or time.monotonic
    attempts = GEMINI_MAX_ATTEMPTS if max_attempts is None else max_attempts
    last_error: BaseException | None = None

    for attempt in range(1, attempts + 1):
        wait_for_gemini_slot(clock=clock, sleeper=sleeper, min_interval=min_interval)
        try:
            return generate()
        except Exception as exc:  # noqa: BLE001 - classify API and transport errors
            last_error = exc
            kind = classify_gemini_error(exc)
            if kind == "rate_limit" and attempt < attempts:
                delay = parse_retry_delay_seconds(exc)
                if delay is None:
                    delay = GEMINI_RATE_LIMIT_FALLBACK_SECONDS
                LOGGER.warning(
                    "Gemini rate-limited (HTTP 429/RESOURCE_EXHAUSTED) for %s; "
                    "waiting %.1fs before retry %s/%s",
                    candidate_id or "candidate",
                    delay,
                    attempt + 1,
                    attempts,
                )
                sleeper(delay)
                continue
            if kind == "unavailable" and attempt < attempts:
                delay = unavailable_backoff_seconds(attempt)
                LOGGER.warning(
                    "Gemini temporarily unavailable (HTTP 503/UNAVAILABLE) for %s; "
                    "waiting %.1fs before retry %s/%s",
                    candidate_id or "candidate",
                    delay,
                    attempt + 1,
                    attempts,
                )
                sleeper(delay)
                continue
            if kind == "unavailable":
                LOGGER.warning(
                    "Gemini unavailable for %s after %s attempts; giving up: %s",
                    candidate_id or "candidate",
                    attempts,
                    exc,
                )
            elif kind == "rate_limit":
                LOGGER.warning(
                    "Gemini still rate-limited for %s after %s attempts; giving up: %s",
                    candidate_id or "candidate",
                    attempts,
                    exc,
                )
            raise

    assert last_error is not None  # pragma: no cover - loop always sets last_error
    raise last_error


def evaluate_candidate(
    candidate: Candidate,
    entries: list[TrackerEntry],
    matching_hint: str | None = None,
    *,
    api_key: str | None = None,
    sleeper: Callable[[float], None] | None = None,
    clock: Callable[[], float] | None = None,
    min_interval: float | None = None,
    generate_text: Callable[[str, str, str], str] | None = None,
) -> Evaluation:
    key = api_key if api_key is not None else os.environ.get(GEMINI_API_KEY_ENV)
    if not key:
        raise RuntimeError(f"{GEMINI_API_KEY_ENV} is not set")

    prompt = build_prompt(candidate, entries, matching_hint)
    model = gemini_model()
    producer = generate_text or invoke_gemini

    text = call_gemini_with_retry(
        lambda: producer(prompt, key, model),
        candidate_id=candidate.candidate_id,
        sleeper=sleeper,
        clock=clock,
        min_interval=min_interval,
    )
    return parse_evaluation_payload(text)
