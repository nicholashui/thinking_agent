"""ExecutionMonitor + compensation (impl §11.6/§16.5): post-execution
policy checks, stop/escalation conditions, and failure compensation."""

from dataclasses import dataclass, field
from typing import Any



@dataclass
class MonitorReport:
    stop_condition: str = ""
    escalation_condition: str = ""
    compensation_required: bool = False
    policy_deviation: bool = False
    partial_failure: bool = False
    findings: list[str] = field(default_factory=list)


class ExecutionMonitor:
    """Deterministic post-execution checks over receipts + plan conditions."""

    def check(self, plan: dict[str, Any], actions: list[dict[str, Any]],
              budget: Any | None = None) -> MonitorReport:
        report = MonitorReport()
        tasks = plan.get("tasks") or []
        failures = [a for a in actions if not a.get("success")]
        report.partial_failure = bool(failures) and len(failures) < len(actions)

        # stop conditions: declared in the plan
        for cond in plan.get("stop_conditions") or []:
            if self._cond_hit(cond, actions):
                report.stop_condition = cond
        for cond in plan.get("escalation_conditions") or []:
            if self._cond_hit(cond, actions):
                report.escalation_condition = cond

        # compensation: a failed A3+ task with a declared compensation step
        for a in failures:
            task = next((t for t in tasks if t.get("plan_task_id") == a.get("plan_task_id")
                         or t.get("idempotency_key") == a.get("idempotency_key")), None)
            if task and task.get("action_class") in ("A3", "A4", "A5") \
                    and task.get("compensation_task_id"):
                report.compensation_required = True
                report.findings.append(
                    f"{task.get('plan_task_id')}: compensation {task.get('compensation_task_id')} required")

        # budget overrun check (if a budget snapshot is supplied)
        if budget is not None:
            used = getattr(budget.snapshot, "tokens_used", 0)
            cap = budget.snapshot.facts.tokens
            if used > cap:
                report.stop_condition = "cost overrun"
        return report

    @staticmethod
    def _cond_hit(cond: str, actions: list[dict[str, Any]]) -> bool:
        blob = str(actions).lower()
        key = cond.lower().replace("condition:", "").strip()
        return bool(key) and key in blob


def run_compensation(plan: dict[str, Any], actions: list[dict[str, Any]],
                     broker: Any, authorization: dict[str, Any], state: dict[str, Any],
                     ctx: Any) -> list[dict[str, Any]]:
    """Executes declared compensation tasks for failed A3+ plan tasks.

    Compensation actions pass through the SAME broker checks (allowlist,
    authorization, idempotency) — compensation is not a bypass."""
    if broker is None:
        return []
    tasks = plan.get("tasks") or []
    failures = [a for a in actions if not a.get("success")]
    out: list[dict[str, Any]] = []
    for a in failures:
        task = next((t for t in tasks
                     if t.get("idempotency_key") == a.get("idempotency_key")), None)
        if not task or not task.get("compensation_task_id"):
            continue
        comp = next((t for t in tasks
                     if t.get("plan_task_id") == task["compensation_task_id"]), None)
        if comp is None:
            continue
        comp_plan = {"plan_id": plan.get("plan_id"), "tasks": [comp]}
        comp_actions, _ = broker.execute_plan(comp_plan, authorization, state, ctx)
        for ca in comp_actions:
            ca["compensation_for"] = a.get("idempotency_key")
        out.extend(comp_actions)
    return out
