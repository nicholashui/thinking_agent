"""Routing domain models (impl plan §13)."""

from pydantic import BaseModel, Field

from thinking_agent.domain.enums import RecordEvidenceStatus
from thinking_agent.domain.task import SituationSignature


class StyleModel(BaseModel):
    id: str
    name: str
    family: str
    description: str
    strengths: list[str] = Field(default_factory=list)
    weaknesses: list[str] = Field(default_factory=list)
    example_prompt: str = ""
    pos_win_rate: float | None = None
    neg_failure_rate: float | None = None
    triggers: list[str] = Field(default_factory=list)
    evidence_status: RecordEvidenceStatus = RecordEvidenceStatus.MEASURED
    completion_contract_ref: str = ""


class RoutingRecord(BaseModel):
    record_id: str
    human_model: str
    case_type: str  # POS | NEG
    signature: SituationSignature | None = None
    signature_text: str = ""
    outcome: str  # ai | human | tie | complementary | design-ai
    human_overall: float | None = None
    ai_overall: float | None = None
    strategy_lesson: str = ""
    artifacts: list[str] = Field(default_factory=list)
    evidence_status: RecordEvidenceStatus = RecordEvidenceStatus.MEASURED


class RoutingGateResult(BaseModel):
    gate: str
    fired: bool
    detail: str = ""


class RoutingDecision(BaseModel):
    signature: SituationSignature
    top_styles: list[str] = Field(default_factory=list)
    scores: dict[str, float] = Field(default_factory=dict)
    score_components: dict[str, dict[str, float]] = Field(default_factory=dict)
    confidence_gate: str = ""  # CLEAR | AMBIGUOUS | LOW
    gates_fired: list[RoutingGateResult] = Field(default_factory=list)
    mandatory_modules: list[str] = Field(default_factory=list)
    historical_refs: list[str] = Field(default_factory=list)
    solo_contract_mode: bool = False
    home_turf_promotions: list[str] = Field(default_factory=list)
    routing_kb_version: str = ""
