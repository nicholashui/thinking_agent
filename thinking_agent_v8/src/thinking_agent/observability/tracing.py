"""LangSmith integration (spec-compliant observability).

Env-gated: tracing activates ONLY when LANGSMITH_TRACING=true and
LANGSMITH_API_KEY is present. What LangSmith may capture is exactly the
spec's auditable surface — structured state, gate results, tool receipts,
audit events, the decision packet. Private model chain-of-thought is never
produced by this implementation (§1.4) and is never sent (the redaction
boundary is enforced by construction: providers return structured outputs
only, and no node emits hidden reasoning fields).
"""

import os
from typing import Any


def langsmith_enabled() -> bool:
    return (
        os.getenv("LANGSMITH_TRACING", "").lower() in ("true", "1")
        and bool(os.getenv("LANGSMITH_API_KEY"))
    )


def run_metadata(task_id: str, thread_id: str, world_facts_version: str,
                 effort_level: str = "") -> dict[str, Any]:
    """Metadata attached to every LangGraph invoke config. LangSmith
    indexes these fields for filtering and grouping runs."""
    meta: dict[str, Any] = {
        "task_id": task_id,
        "thread_id": thread_id,
        "world_facts_version": world_facts_version,
        "agent": "thinking-agent-v8",
    }
    if effort_level:
        meta["effort_level"] = effort_level
    return meta


def tracing_config(metadata: dict[str, Any], project: str | None = None
                   ) -> dict[str, Any]:
    """LangSmith-tracing extras for a LangGraph invoke config."""
    cfg: dict[str, Any] = {"metadata": metadata}
    if project:
        cfg["metadata"]["langsmith_project"] = project
    return cfg
