"""Verification domain models (§8.4)."""

from pydantic import BaseModel, Field


class OutcomeVerification(BaseModel):
    success: bool = False
    reliability: float = 0.0
    external_identity_present: bool = False
    second_verifier_satisfied: bool = False
    class_bar: float = 0.0
    reliability_blocked: bool = False
    ambiguous: bool = False
    findings: list[str] = Field(default_factory=list)
    outcome_hash: str = ""
    cache_used: bool = False


class VerifierIdentity(BaseModel):
    identity_id: str
    endpoint: str = ""
    model_id: str = ""
    lineage: str = ""  # kernel-defined independence lineage
    accepted: bool = True
