"""WHAT/WHY domain models (§8.4): frame, evidence, hypotheses."""

from datetime import datetime, timezone
from typing import Any

from pydantic import BaseModel, Field

from thinking_agent.domain.enums import ActionClass, EvidenceTrust
from thinking_agent.domain.task import SituationSignature


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class ProblemFrame(BaseModel):
    goal: str = ""
    owner: str = ""
    stakeholders: list[str] = Field(default_factory=list)
    success_metrics: list[str] = Field(default_factory=list)
    constraints: list[str] = Field(default_factory=list)
    permissions: list[str] = Field(default_factory=list)
    scope: str = ""
    non_goals: list[str] = Field(default_factory=list)
    stakes: str = "low"
    declared_action_class: ActionClass | None = None
    ambiguities: list[str] = Field(default_factory=list)
    assumptions: list[str] = Field(default_factory=list)
    required_evidence: list[str] = Field(default_factory=list)
    signature: SituationSignature | None = None
    owner_unavailable: bool = False


class EvidenceItem(BaseModel):
    evidence_id: str
    content_summary: str
    source: str = ""
    source_type: str = ""
    trust: EvidenceTrust = EvidenceTrust.USER_DECLARED
    retrieved_at: datetime = Field(default_factory=utcnow)
    content_hash: str = ""
    supports_claim_ids: list[str] = Field(default_factory=list)
    contradicts_claim_ids: list[str] = Field(default_factory=list)
    expiry: datetime | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class Hypothesis(BaseModel):
    hypothesis_id: str
    statement: str
    supporting_evidence_ids: list[str] = Field(default_factory=list)
    contradicting_evidence_ids: list[str] = Field(default_factory=list)
    falsification_condition: str = ""
    estimated_probability: float | None = None
    decision_relevance: str = ""
    status: str = "OPEN"  # OPEN | CONFIRMED | REFUTED


class MissingEvidence(BaseModel):
    evidence_id: str
    description: str
    fillable: bool = False
    filled_by: str = ""  # evidence id that satisfied the gap; empty until real
    voi_estimate: float | None = None


class FalsificationRecord(BaseModel):
    claim_id: str
    falsifier: str
    evidence_refs: list[str] = Field(default_factory=list)
    outcome: str = "UNRESOLVED"  # SURVIVED | REFUTED | UNRESOLVED


class DiagnosisResult(BaseModel):
    hypotheses: list[Hypothesis] = Field(default_factory=list)
    missing_evidence: list[MissingEvidence] = Field(default_factory=list)
    falsifications: list[FalsificationRecord] = Field(default_factory=list)
    residual_uncertainty: str = ""
    probe_available: bool = False
    probe_description: str = ""
    infeasible: bool = False
    infeasibility_findings: list[str] = Field(default_factory=list)
    verifier_outage: bool = False
