"""Source adapters. Each adapter collects and normalizes candidates only."""

from __future__ import annotations

from collections.abc import Callable

from discovery.sources.aclu_tn import fetch_aclu_tn
from discovery.sources.attorney_general import fetch_attorney_general
from discovery.sources.courtlistener import fetch_courtlistener
from discovery.sources.general_assembly import fetch_general_assembly
from discovery.sources.lookout import fetch_lookout
from discovery.types import Candidate

Adapter = Callable[..., list[Candidate]]

ADAPTERS: dict[str, Adapter] = {
    "general-assembly": fetch_general_assembly,
    "attorney-general": fetch_attorney_general,
    "courtlistener": fetch_courtlistener,
    "aclu-tn": fetch_aclu_tn,
    "lookout": fetch_lookout,
}

SOURCE_ORDER = tuple(ADAPTERS.keys())
