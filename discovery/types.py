"""Shared candidate and scoring types for the Tennessee Rights Scout."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


SUGGESTED_ACTIONS = ("NEW ENTRY", "UPDATE EXISTING", "WATCH")
CONFIDENCE_LABELS = ("High", "Medium", "Low")


@dataclass(frozen=True)
class Candidate:
    """Normalized discovery record collected by a source adapter."""

    candidate_id: str
    source_id: str
    source_name: str
    title: str
    url: str
    summary: str
    published_at: str | None = None
    extra: dict[str, Any] = field(default_factory=dict)
    matched_keywords: tuple[str, ...] = ()
    content_fingerprint: str = ""


@dataclass(frozen=True)
class Evaluation:
    """Gemini scoring result. This is a ranking aid, not evidence."""

    tennessee_relevance: float
    digital_rights_relevance: float
    significance: float
    source_quality: float
    novelty: float
    composite: float
    suggested_action: str
    confidence: str
    matching_entry: str | None
    summary: str
    why_it_matters: str
    explanation: str


@dataclass
class SeenRecord:
    candidate_id: str
    url: str
    title: str
    source_id: str
    status: str
    first_seen: str
    last_seen: str
    content_fingerprint: str = ""
    issue_number: int | None = None
    composite: float | None = None
    suggested_action: str | None = None


@dataclass
class TrackerEntry:
    slug: str
    path: str
    title: str
    summary: str
    category: str
    tags: tuple[str, ...]
    primary_source_url: str
    body_excerpt: str
