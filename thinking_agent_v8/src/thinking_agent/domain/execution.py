"""DO domain models (§8.4): plans, tasks, authorization, receipts."""

from datetime import datetime, timezone
from typing import Any

from pydantic import BaseModel, Field

from thinking_agent.domain.enums import ActionClass, AuthorizationStatus


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class PlanTask(BaseModel):
    plan_task_id: str
    description: str
    tool_name: str
    arguments: dict[str, Any] = Field(default_factory=dict)
    action_class: ActionClass = ActionClass.A1
    dependencies: list[str] = Field(default_factory=list)
    reversible: bool = True
    idempotency_key: str = ""
    compensation_task_id: str = ""
    status: str = "PLANNED"  # PLANNED | EXECUTING | EXECUTED | FAILED | COMPENSATED


class ExecutionPlan(BaseModel):
    plan_id: str
    decision_id: str
    tasks: list[PlanTask] = Field(default_factory=list)
    stop_conditions: list[str] = Field(default_factory=list)
    escalation_conditions: list[str] = Field(default_factory=list)
    rollback_steps: list[str] = Field(default_factory=list)
    compensation_steps: list[str] = Field(default_factory=list)
    required_permissions: list[str] = Field(default_factory=list)
    idempotency_namespace: str = ""
    built_at: datetime = Field(default_factory=utcnow)
    plan_generation: int = 1


class Authorization(BaseModel):
    authorization_id: str = ""
    status: AuthorizationStatus = AuthorizationStatus.PENDING
    action_class: ActionClass = ActionClass.A1
    token: str = ""
    pending_deadline: datetime | None = None
    reasons: list[str] = Field(default_factory=list)
    allowed_subset: list[str] = Field(default_factory=list)


class ToolReceipt(BaseModel):
    receipt_id: str
    plan_task_id: str
    tool_name: str
    idempotency_key: str
    executed_at: datetime = Field(default_factory=utcnow)
    success: bool = False
    output_hash: str = ""
    output_summary: str = ""
    sanitized: bool = True


class Observation(BaseModel):
    observation_id: str
    content_summary: str
    content_hash: str = ""
    source: str = ""
    trust: str = "TOOL_UNTRUSTED"
    from_tool_receipt: str = ""
    noted_at: datetime = Field(default_factory=utcnow)
