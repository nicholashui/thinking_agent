"""Live OpenAI-compatible provider adapter (impl §20.1).

Works against any OpenAI-compatible endpoint (DeepSeek's /anthropic and
/chat/completions styles, xAI, local servers). Structured output goes
through Pydantic model_validate_json; schema failures follow §20.3:
one repair attempt, then a fault.
"""

import json
from typing import Any, TypeVar

import httpx
from pydantic import BaseModel

from thinking_agent.providers.contracts import ModelAdapter, ModelCapabilities

T = TypeVar("T", bound=BaseModel)


class OpenAICompatibleAdapter(ModelAdapter):
    def __init__(self, *, api_key: str, base_url: str, model: str,
                 identity: str = "", timeout: float = 300.0,
                 json_mode: bool = False, temperature: float = 0.0):
        self._api_key = api_key
        self._base_url = base_url.rstrip("/")
        self._model = model
        self._identity = identity or model
        self._timeout = timeout
        self._json_mode = json_mode  # some providers need response_format json_object
        self._temperature = temperature
        self._client = httpx.Client(timeout=timeout)

    def identity(self) -> str:
        return self._identity

    def capabilities(self) -> ModelCapabilities:
        return ModelCapabilities(provider_identity="openai-compatible",
                                 endpoint_identity=self._base_url,
                                 structured_output=True)

    def count_tokens(self, text: str) -> int:
        return max(1, len(text) // 4)

    def _chat(self, messages: list[dict], response_format: dict | None = None) -> str:
        payload: dict[str, Any] = {
            "model": self._model,
            "messages": messages,
            "temperature": self._temperature,
        }
        if response_format is not None:
            payload["response_format"] = response_format
        url = f"{self._base_url}/chat/completions"
        resp = self._client.post(url, json=payload,
                                 headers={"Authorization": f"Bearer {self._api_key}"})
        resp.raise_for_status()
        data = resp.json()
        if "choices" not in data or not data["choices"]:
            raise RuntimeError(f"empty response: {str(data)[:200]}")
        return data["choices"][0]["message"]["content"]

    def invoke_structured(self, schema: type[T], messages: list[dict], **kw: Any) -> T:
        """§20.3: one repair attempt with validation errors, then a fault."""
        content = self._chat(messages, {"type": "json_object"} if self._json_mode else None)
        try:
            return schema.model_validate_json(content)
        except Exception as first_error:
            repaired = self._chat(
                messages + [
                    {"role": "assistant", "content": content},
                    {"role": "user", "content": (
                        f"Your output failed schema validation: {first_error}. "
                        f"Repair it to match this JSON schema: "
                        f"{json.dumps(schema.model_json_schema())}. "
                        "Return ONLY valid JSON.")},
                ],
                {"type": "json_object"} if self._json_mode else None,
            )
            try:
                return schema.model_validate_json(repaired)
            except Exception as second_error:
                raise RuntimeError(
                    f"structured output failed validation after repair: {second_error}"
                ) from second_error

    def invoke_text(self, messages: list[dict], **kw: Any) -> str:
        return self._chat(messages)
