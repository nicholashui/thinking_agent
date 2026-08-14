"""Style registry: loads and validates the 104-model registry (impl §13.1)."""

import io
import json
from pathlib import Path


from thinking_agent.domain.routing import StyleModel

DEFAULT_REGISTRY = Path(__file__).resolve().parents[3] / "data" / "human_thinking_models.json"


class StyleRegistry:
    def __init__(self, models: list[StyleModel]):
        self._by_id = {m.id: m for m in models}

    @classmethod
    def load(cls, path: Path | str | None = None) -> "StyleRegistry":
        p = Path(path) if path else DEFAULT_REGISTRY
        raw = json.load(io.open(p, encoding="utf-8"))
        models_raw = raw["models"] if isinstance(raw, list) else raw.get("models", [])
        models = [StyleModel.model_validate(m) for m in models_raw]
        return cls(models)

    def validate(self) -> list[str]:
        """Startup validation (impl §13.1): exactly 104 unique ids m001–m104."""
        problems: list[str] = []
        ids = sorted(self._by_id)
        if len(ids) != 104:
            problems.append(f"expected 104 models, got {len(ids)}")
        expected = [f"m{i:03d}" for i in range(1, 105)]
        if ids != expected:
            problems.append(f"ids not m001..m104: first mismatch at "
                            f"{next((a, b) for a, b in zip(ids, expected) if a != b)}")
        for m in self._by_id.values():
            if not m.name or not m.family or not m.description:
                problems.append(f"{m.id}: missing identity fields")
            if not m.strengths or not m.weaknesses:
                problems.append(f"{m.id}: missing strength/weakness fields")
        return problems

    def all(self) -> list[StyleModel]:
        return list(self._by_id.values())

    def get(self, style_id: str) -> StyleModel | None:
        return self._by_id.get(style_id)
