"""LangGraph runtime context (impl plan §8.1).

Clients, repositories, clocks, and the kernel facade are injected here —
never placed into checkpointed graph state.
"""

from dataclasses import dataclass, field
from typing import Any, Protocol

from thinking_agent.kernel.world_facts import WorldFactsSnapshot


class ModelAdapterProto(Protocol):
    async def ainvoke_structured(self, schema: type, messages: list[dict]) -> Any: ...
    async def ainvoke_text(self, messages: list[dict]) -> str: ...
    def identity(self) -> str: ...


class Clock(Protocol):
    def now(self) -> str: ...
    def monotonic(self) -> float: ...


@dataclass
class RuntimeContext:
    """Everything a graph node needs that must not be checkpointed."""

    world_facts: WorldFactsSnapshot
    models: dict[str, ModelAdapterProto] = field(default_factory=dict)
    kernel: Any = None  # kernel facade (SafetyKernel)
    memory: Any = None  # memory manager
    tools: Any = None  # tool broker
    ledger: Any = None  # learning ledger repository (judge-pipeline writer)
    gap_map: Any = None
    style_router: Any = None  # learned StyleRouter (Phase 5)
    audit: Any = None
    verification_cache: dict = field(default_factory=dict)
    candidate_cache: dict = field(default_factory=dict)
    clock: Clock = field(default_factory=lambda: SystemClock())
    seed: int = 0  # deterministic test seeding (never used in production paths)
    sdl_enabled: bool = False
    improvement_engine: Any = None  # ImprovementEngine (Phase 7)
    judge: Any = None  # external curriculum Judge (scoring only)
    judge_pipeline: Any = None  # JudgePipeline (ledger writes — judge-verdict path only)


class SystemClock:
    import time as _time
    from datetime import datetime, timezone

    def now(self) -> str:
        return self.datetime.now(self.timezone.utc).isoformat()

    def monotonic(self) -> float:
        return self._time.monotonic()
