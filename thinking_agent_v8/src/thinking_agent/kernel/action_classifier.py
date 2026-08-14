"""Action-class attestation (impl plan §11.5 / v5 kernel taxonomy).

Unknown classes default to A5. REPLICATE-class actions are always denied.
"""

from thinking_agent.domain.enums import ActionClass

REPLICATE_TERMS = ("replicate", "self-copy", "clone-self", "autonomous propagation")


class ActionClassifier:
    def __init__(self, taxonomy: dict[str, str]):
        # taxonomy: action name -> class string (kernel-configured)
        self._taxonomy = taxonomy

    def classify(self, action_name: str) -> ActionClass:
        cls = self._taxonomy.get(action_name)
        if cls is None:
            return ActionClass.default_unknown()  # A5 — fail closed
        return ActionClass(cls)

    def classify_tool_call(self, tool_name: str, declared: str | None) -> ActionClass:
        if any(t in tool_name.lower() for t in REPLICATE_TERMS):
            return ActionClass.A5  # replication never executes (invariant 8)
        return self.classify(tool_name)

    def is_replicate(self, tool_name: str, description: str) -> bool:
        blob = f"{tool_name} {description}".lower()
        return any(t in blob for t in REPLICATE_TERMS)

    def misattested(self, declared: ActionClass | None, attested: ActionClass) -> bool:
        """Attested class exceeding the declared class = misattestation."""
        if declared is None:
            return False  # no declaration to contradict
        rank = {c: i for i, c in enumerate(ActionClass)}
        return rank[attested] > rank[declared]
