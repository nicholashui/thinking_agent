"""HOW domain models (§8.4): alternatives, decision, verification reports."""

from pydantic import BaseModel, Field

from thinking_agent.domain.enums import ActionClass


class Alternative(BaseModel):
    alternative_id: str
    description: str
    expected_benefits: list[str] = Field(default_factory=list)
    expected_costs: list[str] = Field(default_factory=list)
    risks: list[str] = Field(default_factory=list)
    dependencies: list[str] = Field(default_factory=list)
    failure_branch: str = ""
    error_bound: str = ""
    requires_external_action: bool = False
    proposed_action_class: ActionClass | None = None
    style_artifact_refs: list[str] = Field(default_factory=list)
    content_hash: str = ""


class Decision(BaseModel):
    decision_id: str
    selected_alternative_id: str
    selection_reason: str = ""
    expected_outcome: str = ""
    error_bound: str = ""
    residual_risks: list[str] = Field(default_factory=list)
    required_conditions: list[str] = Field(default_factory=list)
    requires_external_action: bool = False
    selected_verification_report_ref: str = ""
    approximation_available: bool = False


class AltSet(BaseModel):
    """Structured generator output: the alternative set for one HOW pass."""

    alternatives: list[Alternative] = Field(default_factory=list)
    infeasible: bool = False
    infeasibility_findings: list[str] = Field(default_factory=list)


class CandidateVerificationReport(BaseModel):
    candidate_id: str
    verifier_identity: str
    verifier_kind: str
    success: bool = False
    logical_validity: float = 0.0
    evidence_adequacy: float = 0.0
    constraint_compliance: float = 0.0
    reliability: float = 0.0
    findings: list[str] = Field(default_factory=list)
    checked_at: str = ""
    cache_key: str = ""


class StylePassResult(BaseModel):
    style_id: str
    style_name: str = ""
    generation: int = 1
    summary: str = ""
    claims: list[str] = Field(default_factory=list)
    contract_met: bool = False
    contract_gaps: list[str] = Field(default_factory=list)
    alternatives: list[str] = Field(default_factory=list)
    minority_report: str = ""
    budget_spent: int = 0
    content_hash: str = ""
