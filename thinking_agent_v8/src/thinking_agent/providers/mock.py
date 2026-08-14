"""Deterministic mock model adapter for scenario tests and offline development.

Structured-output calls return objects built from a scripted table keyed by
`scenario` — mirroring the legacy harness's deterministic mock components.
Unknown scenarios raise so tests fail loudly instead of hallucinating.
"""

import json
import re
from typing import Any


from thinking_agent.providers.contracts import ModelAdapter, ModelCapabilities


class MockModelAdapter(ModelAdapter):
    """Scripted adapter: `scripts` maps scenario_key -> schema-name -> payload."""

    def __init__(self, name: str = "mock-model", scripts: dict[str, dict[str, Any]] | None = None):
        self._name = name
        self._scripts = scripts or {}

    def identity(self) -> str:
        return self._name

    def capabilities(self) -> ModelCapabilities:
        return ModelCapabilities(provider_identity="mock", endpoint_identity=self._name)

    def count_tokens(self, text: str) -> int:
        return max(1, len(text) // 4)

    def _scenario(self, messages: list[dict]) -> str:
        joined = json.dumps(messages, default=str)
        m = re.search(r"scenario[\"']?\s*[:=]\s*[\"']?([A-Za-z0-9_\-]+)", joined)
        return m.group(1) if m else "default"

    def _scripted(self, scenario: str, schema_name: str, messages: list[dict]) -> Any:
        scripts = self._scripts.get(scenario)
        if scripts is None:
            raise RuntimeError(f"MockModelAdapter: no scripts for scenario {scenario!r}")
        payload = scripts.get(schema_name) or scripts.get("__any__")
        if payload is None:
            raise RuntimeError(
                f"MockModelAdapter: scenario {scenario!r} has no script for {schema_name!r}"
            )
        if callable(payload):
            # scripted callables receive (messages, kw) and may echo request
            # fields (e.g. the candidate being verified) for realism
            return payload(messages)
        return payload

    def invoke_structured(self, schema: type, messages: list[dict], **kw: Any) -> Any:
        payload = self._scripted(self._scenario(messages), schema.__name__, messages)
        return schema.model_validate(payload)

    def invoke_text(self, messages: list[dict], **kw: Any) -> str:
        payload = self._scripted(self._scenario(messages), "text", messages)
        return str(payload)
