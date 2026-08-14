"""Public Python API (impl §21.1): the ThinkingAgent facade.

The task-model plane may call invoke/stream/resume/get_*; SDL administrative
methods enforce caller authorization and the plan gate (invariant 14).
"""

from pathlib import Path
from typing import Any

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command

from thinking_agent.domain.enums import PlanStatus
from thinking_agent.observability.tracing import langsmith_enabled, run_metadata
from thinking_agent.domain.sdl import LearningPlan
from thinking_agent.domain.task import TaskRequest, TaskResult
from thinking_agent.graphs.task_graph import compile_task_graph
from thinking_agent.kernel.authority_tokens import AuthorityTokenStore
from thinking_agent.kernel.safety_kernel import SafetyKernel
from thinking_agent.kernel.world_facts_store import WorldFactsStore
from thinking_agent.memory.manager import MemoryManager
from thinking_agent.runtime.context import RuntimeContext, SystemClock
from thinking_agent.sdl.curriculum_planner import CurriculumPlanner
from thinking_agent.sdl.discovery import DiscoveryPipeline
from thinking_agent.sdl.gap_map import GapMap
from thinking_agent.sdl.ledger import JudgePipeline, Ledger
from thinking_agent.sdl.review_cycle import ReviewCycle
from thinking_agent.styles.registry import StyleRegistry
from thinking_agent.styles.router import StyleRouter, load_routing_records
from thinking_agent.tools.broker import ToolBroker, builtin_tools


class ThinkingAgent:
    """One governed worker: builds the runtime context, compiles the graph,
    and exposes the public surface."""

    def __init__(self, *, policy_path: Path | str | None = None,
                 models: dict[str, Any] | None = None,
                 registry_path: Path | str | None = None,
                 records_dir: Path | str | None = None,
                 checkpointer: Any = None,
                 sqlite_db: Path | str | None = None):
        policy = policy_path or (
            Path(__file__).resolve().parents[1] / "configs" / "kernel"
            / "world_facts.development.yaml")
        self.snapshot = WorldFactsStore(policy).load()
        self.tokens = AuthorityTokenStore()
        self.kernel = SafetyKernel(self.snapshot, self.tokens)
        self.registry = StyleRegistry.load(registry_path)
        problems = self.registry.validate()
        if problems:
            raise RuntimeError(f"registry invalid: {problems[:3]}")
        self.router = StyleRouter(self.registry.all(),
                                  load_routing_records(records_dir))
        self.memory = MemoryManager()
        self.tools = ToolBroker(builtin_tools())
        self.ledger = Ledger()
        self.judge = JudgePipeline(self.ledger)
        self.gap_map = GapMap()
        self.review_cycle = ReviewCycle(
            quick_review_trials=self.snapshot.facts.sdl.quick_review_trials)
        self.planner = CurriculumPlanner(self.gap_map,
                                         pool_min=self.snapshot.facts.sdl.pool_min)
        self._models = models or {}
        # persistence: durable SQLite checkpointer when requested (native,
        # no Docker — impl §19.1 development profile); InMemory otherwise
        if sqlite_db is not None:
            import os
            import sqlite3

            from langgraph.checkpoint.sqlite import SqliteSaver
            db_path = Path(sqlite_db)
            db_path.parent.mkdir(parents=True, exist_ok=True)
            if str(sqlite_db) != ":memory:":
                # least-privilege: checkpoints carry decision packets and
                # state — restrict the DB to owner-only before connecting.
                # POSIX: 0600 applies directly. Windows: os.chmod only maps
                # the read-only bit; enforcement is the account-scoped user
                # profile directory (NTFS ACLs) — do not place the DB on a
                # shared volume.
                db_path.touch(mode=0o600, exist_ok=True)
                os.chmod(str(db_path), 0o600)
            conn = sqlite3.connect(str(sqlite_db), check_same_thread=False)
            checkpointer = SqliteSaver(conn)
        self._graph = compile_task_graph().compile(
            checkpointer=checkpointer or InMemorySaver())

    def _context(self, thread_id: str = "") -> dict[str, Any]:
        ctx = RuntimeContext(
            world_facts=self.snapshot,
            kernel=self.kernel,
            models=self._models,
            memory=self.memory,
            tools=self.tools,
            style_router=self.router,
            ledger=self.ledger,
            gap_map=self.gap_map,
            clock=SystemClock(),
            sdl_enabled=self.snapshot.facts.sdl.enabled,
        )
        return {"configurable": {"ctx": ctx, "thread_id": thread_id}}

    # ---- task surface ----
    def invoke(self, request: TaskRequest | dict[str, Any],
               thread_id: str | None = None) -> TaskResult:
        req = request.model_dump() if isinstance(request, TaskRequest) else dict(request)
        tid = thread_id or req.get("thread_id") or f"th-{req.get('task_id', 'anon')}"
        config = self._context(tid)
        if langsmith_enabled():
            # spec-compliant tracing: structured audit surface only, never
            # hidden reasoning (§1.4) — see observability/tracing.py
            config.update({"metadata": run_metadata(
                req.get("task_id", ""), tid, self.snapshot.version)})
        out = self._graph.invoke({"request": req, "thread_id": tid}, config=config)
        return TaskResult(
            status=out.get("terminal_status", "ESCALATED"),
            answer=out.get("decision_packet", {}).get("answer", ""),
            decision_packet=out.get("decision_packet", {}),
            checkpoint_id=tid,
            interrupt=out.get("__interrupt__"),
            required_human_actions=out.get("required_human_actions", []),
            audit_reference=",".join(out.get("audit_refs", [])),
        )

    async def ainvoke(self, request: TaskRequest | dict[str, Any],
                      thread_id: str | None = None) -> TaskResult:
        req = request.model_dump() if isinstance(request, TaskRequest) else dict(request)
        tid = thread_id or req.get("thread_id") or f"th-{req.get('task_id', 'anon')}"
        out = await self._graph.ainvoke({"request": req, "thread_id": tid},
                                        config=self._context(tid))
        return TaskResult(status=out.get("terminal_status", "ESCALATED"),
                          decision_packet=out.get("decision_packet", {}))

    def stream(self, request: TaskRequest | dict[str, Any],
               thread_id: str | None = None):
        req = request.model_dump() if isinstance(request, TaskRequest) else dict(request)
        tid = thread_id or req.get("thread_id") or f"th-{req.get('task_id', 'anon')}"
        return self._graph.stream({"request": req, "thread_id": tid},
                                  config=self._context(tid), stream_mode="updates")

    def resume(self, thread_id: str, response: Any) -> TaskResult:
        out = self._graph.invoke(Command(resume=response), config=self._context(thread_id))
        return TaskResult(status=out.get("terminal_status", "ESCALATED"),
                          decision_packet=out.get("decision_packet", {}))

    def get_state(self, thread_id: str) -> Any:
        return self._graph.get_state(self._context(thread_id))

    def get_packet(self, packet_id: str) -> dict[str, Any] | None:
        for tid in (packet_id,):
            state = self.get_state(tid)
            if state and state.values.get("decision_packet", {}).get("packet_id") == packet_id:
                return state.values["decision_packet"]
        return None

    # ---- SDL administration (caller-authorization enforced by the operator) ----
    def discover_challenges(self, source: Any, query: str, budget: int) -> list[Any]:
        pipe = DiscoveryPipeline(source, self.gap_map)
        return pipe.scan(query, budget)

    def propose_learning_plan(self, candidates: list[Any],
                              review_ref: str = "") -> LearningPlan:
        return self.planner.propose_plan(candidates, review_ref=review_ref)

    def approve_learning_plan(self, plan: LearningPlan,
                              approval_ref: str = "") -> LearningPlan:
        plan.status = PlanStatus.APPROVED
        plan.approval_ref = approval_ref
        return plan

    def execute_next_trial(self, plan: LearningPlan) -> str:
        """Invariant 14: a draft plan cannot execute."""
        if plan.status != PlanStatus.APPROVED:
            raise PermissionError("draft learning plan cannot execute (invariant 14)")
        pending = [i for i in plan.items if i.status == "PLANNED"]
        if not pending:
            # plan closeout: judge pipeline appends a PLAN_CLOSEOUT entry
            self.judge.record_plan_closeout(plan_ref=plan.plan_id,
                                            challenge_id=plan.plan_id)
            plan.status = PlanStatus.CLOSED
            return "plan-closed"
        item = pending[0]
        if item.attempts >= item.max_attempts:
            return "re-entry-required (anti-obsession rule)"
        item.attempts += 1
        item.status = "ATTEMPTED"
        return item.item_id

    def run_quick_review(self, candidate_pool: list[Any] | None = None):
        return self.review_cycle.run("quick", self.ledger, self.gap_map,
                                     candidate_pool or [])

    def run_deep_review(self, candidate_pool: list[Any] | None = None):
        return self.review_cycle.run("deep", self.ledger, self.gap_map,
                                     candidate_pool or [])
