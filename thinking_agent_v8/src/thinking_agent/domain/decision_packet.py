"""The proof-carrying decision packet (impl plan §15.2 / v8 §1.3).

Every terminal path produces one. Validated before return (§15.3).
No raw private chain-of-thought appears anywhere in this structure.
"""

from datetime import datetime, timezone
from typing import Any

from pydantic import BaseModel, Field

from thinking_agent.domain.enums import TerminalStatus


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class PacketRoute(BaseModel):
    effort_level: str = ""
    signature: dict[str, Any] = Field(default_factory=dict)
    routed_styles: list[str] = Field(default_factory=list)
    routing_scores: dict[str, float] = Field(default_factory=dict)
    confidence_gate: str = ""
    historical_refs: list[str] = Field(default_factory=list)
    solo_contract_mode: bool = False


class PacketDiagnosis(BaseModel):
    hypotheses: list[dict[str, Any]] = Field(default_factory=list)
    evidence_refs: list[str] = Field(default_factory=list)
    missing_evidence: list[str] = Field(default_factory=list)
    falsifiers: list[dict[str, Any]] = Field(default_factory=list)
    residual_uncertainty: str = ""


class PacketSolution(BaseModel):
    alternatives: list[dict[str, Any]] = Field(default_factory=list)
    selected_decision: dict[str, Any] = Field(default_factory=dict)
    error_bound: str = ""
    infeasibility_findings: list[str] = Field(default_factory=list)
    approximation_details: str = ""


class PacketSafety(BaseModel):
    declared_action_class: str = ""
    attested_action_class: str = ""
    authorization_status: str = ""
    permissions: list[str] = Field(default_factory=list)
    risks: list[str] = Field(default_factory=list)
    pending_subset: list[str] = Field(default_factory=list)
    required_human_actions: list[str] = Field(default_factory=list)


class PacketVerification(BaseModel):
    candidate_reports: list[dict[str, Any]] = Field(default_factory=list)
    selected_report: dict[str, Any] = Field(default_factory=dict)
    outcome_report: dict[str, Any] = Field(default_factory=dict)
    reliability_bar: float = 0.0
    verifier_identities: list[str] = Field(default_factory=list)
    second_verifier_satisfied: bool = False
    cache_usage: list[str] = Field(default_factory=list)


class PacketExecution(BaseModel):
    plan: dict[str, Any] = Field(default_factory=dict)
    actions: list[dict[str, Any]] = Field(default_factory=list)
    observations: list[dict[str, Any]] = Field(default_factory=list)
    stop_conditions: list[str] = Field(default_factory=list)
    escalation_conditions: list[str] = Field(default_factory=list)
    compensation: list[str] = Field(default_factory=list)


class PacketReview(BaseModel):
    review_summary: str = ""
    lessons: list[dict[str, Any]] = Field(default_factory=list)
    memory_commits: list[str] = Field(default_factory=list)
    improvement_proposal_refs: list[str] = Field(default_factory=list)


class PacketResources(BaseModel):
    iterations: int = 0
    model_calls: int = 0
    verifier_calls: int = 0
    tool_calls: int = 0
    cognitive_tokens: int = 0
    bookkeeping_calls: int = 0
    elapsed_time: float = 0.0
    stop_reason: str = ""


class PacketProvenance(BaseModel):
    world_facts_version: str = ""
    model_identities: list[str] = Field(default_factory=list)
    prompt_versions: list[str] = Field(default_factory=list)
    registry_version: str = ""
    routing_kb_version: str = ""
    graph_version: str = ""
    checkpoint_refs: list[str] = Field(default_factory=list)
    audit_refs: list[str] = Field(default_factory=list)


class DecisionPacket(BaseModel):
    packet_version: str = "1"
    packet_id: str = ""
    task_id: str = ""
    thread_id: str = ""
    terminal_status: TerminalStatus
    terminal_reason: str = ""

    request_summary: str = ""
    goal: str = ""
    success_criteria: list[str] = Field(default_factory=list)
    scope: str = ""
    constraints: list[str] = Field(default_factory=list)

    route: PacketRoute = Field(default_factory=PacketRoute)
    diagnosis: PacketDiagnosis = Field(default_factory=PacketDiagnosis)
    solution: PacketSolution = Field(default_factory=PacketSolution)
    safety: PacketSafety = Field(default_factory=PacketSafety)
    verification: PacketVerification = Field(default_factory=PacketVerification)
    execution: PacketExecution = Field(default_factory=PacketExecution)
    review: PacketReview = Field(default_factory=PacketReview)
    resources: PacketResources = Field(default_factory=PacketResources)
    provenance: PacketProvenance = Field(default_factory=PacketProvenance)

    answer: str = ""
    confidence: float = 0.0
    created_at: datetime = Field(default_factory=utcnow)
    packet_hash: str = ""


class PacketValidator:
    """§15.3 — packet validation before return."""

    _FORBIDDEN_SOLVED = (
        "A DecisionPacket with terminal_status SOLVED cannot carry unresolved "
        "missing evidence, a reliability block, or missing external verification."
    )

    def validate(self, packet: DecisionPacket) -> list[str]:
        problems: list[str] = []
        if packet.terminal_status not in list(TerminalStatus):
            problems.append("status not one of the eight terminal values")
        if packet.terminal_status == TerminalStatus.SOLVED:
            if packet.diagnosis.missing_evidence:
                problems.append("SOLVED with unresolved missing_evidence")
            if packet.verification.outcome_report.get("reliability_blocked"):
                problems.append("SOLVED with reliability block")
        if packet.safety.attested_action_class and not packet.safety.authorization_status:
            problems.append("external action without authorization status")
        if packet.terminal_status == TerminalStatus.ESCALATED and not (
            packet.safety.required_human_actions
        ):
            problems.append("ESCALATED without required human actions")
        if not packet.packet_id or not packet.task_id:
            problems.append("packet_id/task_id missing")
        return problems
