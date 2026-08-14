"""REVIEW domain models (§8.4): review result, lessons, competence, improvement."""

from pydantic import BaseModel, Field


class Lesson(BaseModel):
    lesson_id: str
    content: str
    when_to_use_triggers: list[str] = Field(default_factory=list)
    procedural: bool = False
    provenance: str = ""
    authority_token: str = ""
    quarantined: bool = False


class ReviewResult(BaseModel):
    what_happened: str = ""
    what_was_expected: str = ""
    gaps: list[str] = Field(default_factory=list)
    lessons: list[Lesson] = Field(default_factory=list)
    calibration: dict[str, float] = Field(default_factory=dict)
    reframe_required: bool = False
    procedural_write_proposals: list[str] = Field(default_factory=list)
    improvement_proposals: list[str] = Field(default_factory=list)


class CompetenceProfile(BaseModel):
    profile_id: str
    domain: str = ""
    model_id: str = ""
    reliability: float = 0.0
    provenance: str = ""  # kernel/evaluation-plane only
    updated_at: str = ""


class ImprovementProposal(BaseModel):
    proposal_id: str
    canonical_hash: str
    description: str
    risk_level: str = "R1"  # R1 scenario | R2 gate | R3 module
    status: str = "QUEUED"
    evaluation_ref: str = ""
