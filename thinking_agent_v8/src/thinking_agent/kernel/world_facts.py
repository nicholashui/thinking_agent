"""Kernel-held World Facts (impl plan §9).

The World-Facts object is immutable once loaded (`WorldFactsSnapshot`, frozen).
Task nodes may only see it through the kernel runtime facade — enforced by the
AST read-path assertion (kernel/policy_audit.py) and by construction: graph
state stores only `world_facts_ref` (version + hash).

DEEP immutability: every frozen model inherits `FrozenModel`, which
recursively converts dicts → FrozenDict and lists → tuples at validation
time. Assignment, item mutation, append, and inner-container mutation all
raise — the kernel facade can hand out references without risk.
"""

from typing import Any, ClassVar

from pydantic import BaseModel, Field, field_validator, model_validator

from thinking_agent.canonical import FrozenDict, sha256_hex
from thinking_agent.domain.enums import ActionClass


def _deep_freeze(v: Any) -> Any:
    """Recursively freeze containers: dict → FrozenDict, list/tuple → tuple."""
    if isinstance(v, dict):
        return FrozenDict({k: _deep_freeze(x) for k, x in v.items()})
    if isinstance(v, list):
        return tuple(_deep_freeze(x) for x in v)
    if isinstance(v, tuple):
        return tuple(_deep_freeze(x) for x in v)
    return v


class FrozenModel(BaseModel):
    """Frozen pydantic model with recursive container immutability.

    A mode="before" freeze is insufficient: pydantic re-materializes plain
    dicts/lists while validating field types. The freeze therefore runs
    mode="after" and rewrites fields through object.__setattr__ (the
    documented escape for frozen models) — the final instance holds only
    FrozenDicts and tuples, at every nesting level."""

    model_config = {"frozen": True}

    @model_validator(mode="after")
    def _freeze_containers(self) -> "FrozenModel":
        for name, value in self.__dict__.items():
            object.__setattr__(self, name, _deep_freeze(value))
        return self


class BudgetFacts(FrozenModel):
    iterations: int = 12
    cognitive_calls: int = 24
    tokens: int = 40000
    agents_per_round: int = 6
    deadline_seconds: int = 1800
    evoc_base: float = 10.0
    evoc_decay: float = 0.5
    novelty_plateau: int = 3
    gate_reentry_budget: int = 2
    reframe_budget: int = 2
    pending_timeout_seconds: int = 3600


class VerificationFacts(FrozenModel):

    class_bars: dict[str, float] = Field(default_factory=dict)
    verifier_identities: tuple[dict[str, Any], ...] = Field(default_factory=tuple)
    verifier_outage: bool = False
    unknown_class_defaults_to: str = "A5"
    trust_margin: float = 0.1
    consolidation_threshold: int = 3

    @field_validator("class_bars", mode="before")
    @classmethod
    def _freeze_class_bars(cls, v):
        return FrozenDict(v) if isinstance(v, dict) else v


class MemoryFacts(FrozenModel):

    trust_margin: float = 0.1
    consolidation_threshold: int = 3
    procedural_write_authorized: bool = False


class ImprovementFacts(FrozenModel):

    baseline_frozen: bool = True
    improvement_rate_cap: int = 10


class SDLFacts(FrozenModel):

    enabled: bool = False
    pool_min: int = 20
    quick_review_trials: int = 10
    deep_review_schedule: str = "monthly"
    counter_design_canary_enabled: bool = False
    discovery_budget_candidates: int = 50


class WorldFacts(FrozenModel):
    """The active kernel policy (YAML-loaded, kernel-written only).

    All sub-models are FROZEN: the policy is immutable once loaded, so the
    kernel facade can hand out references without any task node being able
    to mutate budgets, identities, allowlists, or SDL knobs (impl §9.3)."""

    version: str
    environment: str = "development"
    budgets: BudgetFacts = Field(default_factory=BudgetFacts)
    gates: dict[str, Any] = Field(default_factory=dict)  # frozen via validator below
    verification: VerificationFacts = Field(default_factory=VerificationFacts)
    memory: MemoryFacts = Field(default_factory=MemoryFacts)
    improvement: ImprovementFacts = Field(default_factory=ImprovementFacts)
    sdl: SDLFacts = Field(default_factory=SDLFacts)
    action_taxonomy: dict[str, str] = Field(default_factory=dict)  # frozen via validator below
    pending_allowlist: tuple[str, ...] = Field(default_factory=tuple)

    _SECURITY_FIELDS: ClassVar[set[str]] = {
        "budgets", "gates", "verification", "memory", "improvement",
        "sdl", "action_taxonomy", "pending_allowlist",
    }

    @field_validator("action_taxonomy")
    @classmethod
    def _valid_classes(cls, v: dict[str, str]) -> dict[str, str]:
        for cls in v.values():
            if cls not in {a.value for a in ActionClass}:
                raise ValueError(f"invalid action class {cls!r} in taxonomy")
        return v

    def bar_for(self, action_class: ActionClass) -> float:
        return self.verification.class_bars.get(action_class.value, 0.7)

    def identities_for(self, action_class: ActionClass) -> list[str]:
        return [i["identity_id"] for i in self.verification.verifier_identities if i.get("accepted", True)]

    @field_validator("action_taxonomy", "gates", mode="before")
    @classmethod
    def _freeze_dicts(cls, v):
        return FrozenDict(v) if isinstance(v, dict) else v

    def snapshot(self) -> "WorldFactsSnapshot":
        return WorldFactsSnapshot(
            version=self.version,
            content_hash=sha256_hex(self.model_dump()),
            kernel_signature="",
            policy_environment=self.environment,
            facts=self.model_copy(deep=True),
        )


class WorldFactsSnapshot(BaseModel):
    """Immutable per-run policy snapshot (impl plan §9.3)."""

    version: str
    content_hash: str
    kernel_signature: str
    policy_environment: str
    facts: WorldFacts

    def bar_for(self, action_class: ActionClass) -> float:
        return self.facts.bar_for(action_class)

    def identities(self) -> list[dict[str, Any]]:
        return self.facts.verification.verifier_identities

    def second_verifier_required(self, action_class: ActionClass) -> bool:
        """Kernel-computed second-verifier rule (v5 V4 / impl §14.2)."""
        return action_class in (ActionClass.A3, ActionClass.A4, ActionClass.A5)

    def allowed_pending_subset(self, plan_task_ids: list[str]) -> list[str]:
        """Static-table-only subset (v5 V3 / impl §11.6): kernel table ∩ plan ids."""
        return [t for t in plan_task_ids if t in set(self.facts.pending_allowlist)]
