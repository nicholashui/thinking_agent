"""Self-Directed Learning domain models (v8 Part II / impl plan §18)."""

from datetime import datetime, timezone
from typing import Any

from pydantic import BaseModel, Field

from thinking_agent.domain.enums import (
    CandidateStatus,
    GapType,
    LedgerEntryType,
    PlanStatus,
)
from thinking_agent.domain.task import SituationSignature


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class ChallengeCandidate(BaseModel):
    candidate_id: str
    source_tier: str  # Tier-1 arXiv | Tier-2 curated
    source_id: str = ""
    source_title: str = ""
    source_abstract: str = ""
    source_hash: str = ""
    retrieval_query: str = ""
    signature: SituationSignature | None = None
    proposed_challenge_class: str = ""
    proposed_prompt: str = ""
    judgeable_output_shape: str = ""
    novelty_score: float = 0.0
    well_posedness_score: float = 0.0
    estimated_cost: float = 0.0
    status: CandidateStatus = CandidateStatus.DISCOVERED
    rejection_reason: str = ""
    created_at: datetime = Field(default_factory=utcnow)


class GapMapEntry(BaseModel):
    gap_id: str
    signature: SituationSignature | None = None
    gap_type: GapType
    magnitude: float
    evidence_ref: str = ""
    last_verdict_ref: str = ""
    last_updated: datetime = Field(default_factory=utcnow)
    trend_last_three: list[float] = Field(default_factory=list)
    status: str = "OPEN"


class LearningPlanItem(BaseModel):
    item_id: str
    challenge_id: str
    source: str = ""
    signature: SituationSignature | None = None
    expected_styles: list[str] = Field(default_factory=list)
    target_gap_id: str
    expected_closure: float = 0.0
    trial_budget: int = 0
    gate_flags: list[str] = Field(default_factory=list)
    max_attempts: int = 2  # anti-obsession: two attempts, then review
    attempts: int = 0
    status: str = "PLANNED"
    verdict_ref: str = ""


class LearningPlan(BaseModel):
    plan_id: str
    review_ref: str = ""
    created_at: datetime = Field(default_factory=utcnow)
    status: PlanStatus = PlanStatus.DRAFT
    items: list[LearningPlanItem] = Field(default_factory=list)
    total_budget: int = 0
    discovery_snapshot_ref: str = ""
    gap_map_snapshot_ref: str = ""
    approval_ref: str = ""


class LedgerEntry(BaseModel):
    """Append-only, hash-chained learning ledger entry (v8 §IV.6 / impl §18.11)."""

    sequence_number: int
    entry_id: str
    entry_type: LedgerEntryType
    challenge_id: str = ""
    source: str = ""
    signature: SituationSignature | None = None
    routed_styles: list[str] = Field(default_factory=list)
    verdict: str = ""
    dimensions: dict[str, float] = Field(default_factory=dict)
    gap_delta: float = 0.0
    lessons: list[str] = Field(default_factory=list)
    when_to_use_triggers: list[str] = Field(default_factory=list)
    plan_ref: str = ""
    supersedes_entry_id: str = ""
    timestamp: datetime = Field(default_factory=utcnow)
    payload_hash: str = ""
    hash_prev: str = ""
    hash: str = ""


class ReviewReport(BaseModel):
    report_id: str
    review_kind: str  # quick | deep
    attempted: list[str] = Field(default_factory=list)
    closed: list[str] = Field(default_factory=list)
    regressed: list[str] = Field(default_factory=list)
    stale: list[str] = Field(default_factory=list)
    discovered_not_attempted: list[str] = Field(default_factory=list)
    metrics: dict[str, Any] = Field(default_factory=dict)
    gap_refresh_proposal: list[dict[str, Any]] = Field(default_factory=list)
    next_plan_proposal: dict[str, Any] = Field(default_factory=dict)
    approved: bool = False
    ledger_entry_id: str = ""
