"""The Safety Kernel facade (impl plan §5.2 Boundary B).

The ONLY interface through which task nodes may touch security-sensitive
facts. Nodes receive this facade via runtime context; they never hold the
snapshot or its mutable policy.
"""

from dataclasses import dataclass, field
from typing import Any

from thinking_agent.domain.enums import ActionClass, AuthorizationStatus
from thinking_agent.kernel.action_classifier import ActionClassifier
from thinking_agent.kernel.authority_tokens import AuthorityTokenStore
from thinking_agent.kernel.world_facts import WorldFactsSnapshot


@dataclass
class KernelDecision:
    status: AuthorizationStatus
    action_class: ActionClass
    reasons: list[str] = field(default_factory=list)
    token: str = ""
    allowed_subset: list[str] = field(default_factory=list)
    second_verifier_required: bool = False
    required_identities: list[str] = field(default_factory=list)
    class_bar: float = 0.0
    replicate_denied: bool = False


class SafetyKernel:
    """Composes the kernel-owned capabilities behind one facade."""

    def __init__(self, snapshot: WorldFactsSnapshot, token_store: AuthorityTokenStore | None = None):
        self._snapshot = snapshot
        self._classifier = ActionClassifier(snapshot.facts.action_taxonomy)
        self._tokens = token_store or AuthorityTokenStore()

    # ---- read facade (the only reads task nodes may make) ----
    def bar_for(self, action_class: ActionClass) -> float:
        return self._snapshot.bar_for(action_class)

    def verifier_identities(self) -> list[dict[str, Any]]:
        return self._snapshot.identities()

    def second_verifier_required(self, action_class: ActionClass) -> bool:
        return self._snapshot.second_verifier_required(action_class)

    def pending_allowed_subset(self, plan_task_ids: list[str]) -> list[str]:
        return self._snapshot.allowed_pending_subset(plan_task_ids)

    @property
    def verifier_outage(self) -> bool:
        return self._snapshot.facts.verification.verifier_outage

    @property
    def sdl_enabled(self) -> bool:
        return self._snapshot.facts.sdl.enabled

    @property
    def baseline_frozen(self) -> bool:
        return self._snapshot.facts.improvement.baseline_frozen

    @property
    def budgets(self):
        return self._snapshot.facts.budgets

    def pending_timeout_seconds(self) -> int:
        return self._snapshot.facts.budgets.pending_timeout_seconds

    # ---- authorization ----
    def authorize(
        self,
        tool_name: str,
        declared_class: ActionClass | None,
        description: str = "",
        permissions: list[str] | None = None,
        plan_task_ids: list[str] | None = None,
        requested_human_approval: bool = False,
    ) -> KernelDecision:
        """Attest + authorize one action (impl §11.5/§11.6)."""
        if self._classifier.is_replicate(tool_name, description):
            return KernelDecision(
                status=AuthorizationStatus.DENIED_UNSAFE,
                action_class=ActionClass.A5,
                reasons=["replication-class action denied (invariant 8)"],
                replicate_denied=True,
            )
        attested = self._classifier.classify(tool_name)
        if self._classifier.misattested(declared_class, attested):
            return KernelDecision(
                status=AuthorizationStatus.DENIED_UNSAFE,
                action_class=attested,
                reasons=[f"misattestation: declared {declared_class}, attested {attested}"],
            )
        if attested in (ActionClass.A4, ActionClass.A5) or requested_human_approval:
            return KernelDecision(
                status=AuthorizationStatus.PENDING,
                action_class=attested,
                reasons=["human approval required"],
                class_bar=self.bar_for(attested),
                second_verifier_required=self.second_verifier_required(attested),
                required_identities=[
                    i["identity_id"]
                    for i in self.verifier_identities()
                    if i.get("accepted", True)
                ],
            )
        if attested == ActionClass.A3 and self.verifier_outage:
            # A3+ outage at attestation → L3 ESCALATED (v5 V5 / S29)
            return KernelDecision(
                status=AuthorizationStatus.DENIED_ESCALATE,
                action_class=attested,
                reasons=["A3+ verifier outage at attestation (L3)"],
            )
        return KernelDecision(
            status=AuthorizationStatus.APPROVED,
            action_class=attested,
            reasons=["static policy satisfied"],
            class_bar=self.bar_for(attested),
            second_verifier_required=self.second_verifier_required(attested),
            required_identities=[
                i["identity_id"] for i in self.verifier_identities() if i.get("accepted", True)
            ],
        )
