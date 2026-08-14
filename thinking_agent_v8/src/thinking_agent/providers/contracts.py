"""Model adapter contract (impl §20.1). All providers implement one interface."""

from dataclasses import dataclass, field
from typing import Any, Protocol, runtime_checkable


@dataclass
class ModelCapabilities:
    structured_output: bool = True
    tool_calling: bool = False
    context_limit: int = 128_000
    reasoning_mode: bool = False
    streaming: bool = False
    temperature_support: bool = True
    provider_identity: str = ""
    endpoint_identity: str = ""


@runtime_checkable
class ModelAdapter(Protocol):
    def invoke_structured(self, schema: type, messages: list[dict], **kw: Any) -> Any: ...
    def invoke_text(self, messages: list[dict], **kw: Any) -> str: ...
    def count_tokens(self, text: str) -> int: ...
    def capabilities(self) -> ModelCapabilities: ...
    def identity(self) -> str: ...


@dataclass
class RoleAssignment:
    """Which model identity serves which role (impl §20.2)."""

    roles: dict[str, str] = field(default_factory=dict)

    def identity_for(self, role: str) -> str:
        return self.roles.get(role, self.roles.get("default", "main"))
