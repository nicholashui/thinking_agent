"""Audit event service (impl §22.2): every event carries identity + version + hash."""

import threading
from dataclasses import dataclass, field
from typing import Any

from thinking_agent.canonical import sha256_hex


@dataclass
class AuditEvent:
    event_id: str
    task_id: str
    thread_id: str
    stage: str
    component: str
    event_type: str
    input_refs: list[str] = field(default_factory=list)
    output_refs: list[str] = field(default_factory=list)
    model_identity: str = ""
    policy_version: str = ""
    timestamp: str = ""
    latency_ms: float = 0.0
    cost: float = 0.0
    content_hash: str = ""


class AuditService:
    """Thread-safe in-memory audit log (repository-backed in production)."""

    def __init__(self, policy_version: str = ""):
        self._events: list[AuditEvent] = []
        self._counter = 0
        self._lock = threading.Lock()
        self.policy_version = policy_version

    def record(
        self,
        task_id: str,
        thread_id: str,
        stage: str,
        component: str,
        event_type: str,
        *,
        input_refs: list[str] | None = None,
        output_refs: list[str] | None = None,
        model_identity: str = "",
        timestamp: str = "",
        latency_ms: float = 0.0,
        cost: float = 0.0,
        payload: Any = None,
    ) -> AuditEvent:
        with self._lock:
            self._counter += 1
            event = AuditEvent(
                event_id=f"audit-{self._counter:06d}",
                task_id=task_id,
                thread_id=thread_id,
                stage=stage,
                component=component,
                event_type=event_type,
                input_refs=input_refs or [],
                output_refs=output_refs or [],
                model_identity=model_identity,
                policy_version=self.policy_version,
                timestamp=timestamp,
                latency_ms=latency_ms,
                cost=cost,
                content_hash=sha256_hex(payload) if payload is not None else "",
            )
            self._events.append(event)
            return event

    def refs(self) -> list[str]:
        return [e.event_id for e in self._events]
