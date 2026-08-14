"""Core task domain models (impl plan §8.4)."""

from datetime import datetime, timezone
from typing import Any, ClassVar

from pydantic import BaseModel, Field

from thinking_agent.domain.enums import ActionClass, EffortLevel, Stage


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class TaskRequest(BaseModel):
    """Public request. Task declarations are UNTRUSTED for security values."""

    task_id: str = ""
    input_text: str
    user_context: str = ""
    declared_goal: str = ""
    declared_constraints: list[str] = Field(default_factory=list)
    declared_permissions: list[str] = Field(default_factory=list)
    requested_output_format: str = "decision_packet"
    conversation_ref: str = ""
    submitted_at: datetime = Field(default_factory=utcnow)
    task_metadata: dict[str, Any] = Field(default_factory=dict)


class WorldFactsReference(BaseModel):
    """Pointer to the kernel snapshot — the object itself never enters graph state."""

    version: str
    content_hash: str
    loaded_at: datetime = Field(default_factory=utcnow)
    kernel_signature: str = ""
    policy_environment: str = "development"


class RouteDecision(BaseModel):
    effort_level: EffortLevel
    requires_diagnosis: bool = False
    requires_generation: bool = True
    requires_search: bool = False
    use_council: bool = False
    requires_review: bool = False
    requires_external_verification: bool = False
    estimated_complexity: float = 0.0
    route_reasons: list[str] = Field(default_factory=list)
    competence_snapshot_ref: str = ""
    budget_envelope_ref: str = ""


class SituationSignature(BaseModel):
    """Canonical routing vocabulary (v8 §IV.2.3 / v6 §II.2.2)."""

    domains: list[str] = Field(default_factory=list)
    goals: list[str] = Field(default_factory=list)
    context: list[str] = Field(default_factory=list)
    other_tags: list[str] = Field(default_factory=list)
    completeness_score: float = 0.0
    extraction_evidence_refs: list[str] = Field(default_factory=list)
    version: str = "1"

    DOMAIN_VOCAB: ClassVar[set[str]] = {
        "medical", "finance", "engineering", "software", "product",
        "strategy", "security", "supply", "science", "organization",
    }
    GOAL_VOCAB: ClassVar[set[str]] = {"guarantee", "maximize", "estimate", "predict", "decide", "diagnose"}
    CONTEXT_VOCAB: ClassVar[set[str]] = {"deadline", "high_stakes", "one_shot", "unmeasured", "adversarial"}

    def is_complete(self) -> bool:
        return self.completeness_score >= 0.8 and bool(self.domains) and bool(self.goals)


class BudgetEnvelope(BaseModel):
    iterations: int = 12
    cognitive_calls: int = 24
    tokens: int = 40000
    agents_per_round: int = 6
    deadline_seconds: int = 1800
    evoc_base: float = 10.0
    evoc_decay: float = 0.5
    novelty_plateau: int = 3
    ref: str = ""


class LoopStatus(BaseModel):
    stage: Stage = Stage.META
    iteration: int = 0
    stopped: bool = False
    stop_reason: str = ""
    plateau_count: int = 0
    gate_reentries: dict[str, int] = Field(default_factory=dict)
    reframe_count: int = 0
    # a declared action class is untrusted until attestation
    declared_action_class: ActionClass | None = None


class TaskResult(BaseModel):
    """Public result envelope (impl plan §21.2)."""

    status: "TerminalStatusLike"
    answer: str = ""
    decision_packet: "DecisionPacketLike" = None  # type: ignore[assignment]
    checkpoint_id: str = ""
    interrupt: dict[str, Any] | None = None
    required_human_actions: list[str] = Field(default_factory=list)
    audit_reference: str = ""


# late imports to avoid circularity at module import time
from thinking_agent.domain.enums import TerminalStatus as TerminalStatusLike  # noqa: E402
from thinking_agent.domain.decision_packet import DecisionPacket as DecisionPacketLike  # noqa: E402
