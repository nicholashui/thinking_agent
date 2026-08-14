"""World-Facts Store: loads, validates, and snapshots kernel policy (impl §9.2/9.3)."""

from pathlib import Path

import yaml
from pydantic import ValidationError

from thinking_agent.exceptions import KernelPolicyError
from thinking_agent.kernel.world_facts import WorldFacts, WorldFactsSnapshot


class WorldFactsStore:
    """Loads YAML kernel policy. Fails closed — never invents defaults."""

    def __init__(self, path: Path | str):
        self.path = Path(path)

    def load(self) -> WorldFactsSnapshot:
        if not self.path.exists():
            raise KernelPolicyError(f"kernel policy missing: {self.path}")
        try:
            raw = yaml.safe_load(self.path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            raise KernelPolicyError(f"kernel policy unparseable: {exc}") from exc
        if not isinstance(raw, dict):
            raise KernelPolicyError("kernel policy must be a mapping")
        try:
            facts = WorldFacts(**raw)
        except ValidationError as exc:
            raise KernelPolicyError(f"kernel policy invalid: {exc}") from exc
        if facts.environment == "production" and not facts.snapshot().kernel_signature:
            # production snapshots must be signed (operator supplies signature out-of-band)
            raise KernelPolicyError("production kernel policy requires a signature")
        return facts.snapshot()
