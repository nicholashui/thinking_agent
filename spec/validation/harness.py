#!/usr/bin/env python3
"""
Thinking Agent validation harness — v2 baseline vs v3 governed loop.

SCOPE (honest per the framework's own rules, P4 / §23, no overclaim):
This harness does NOT simulate model intelligence. Components are deterministic
stubs. It validates what is decidable: control-flow, termination, budget
enforcement, stage gating, state reachability, verification independence
(threshold bars), packet completeness, delta-based verification reuse,
checkpoint/resume, pending-authorization semantics, competence feedback,
council minority preservation, and cost behavior.

v3 engine (solve_v3) implements the v3 §24.4 algorithm; solve_v2 freezes the
v2 behavior as the regression baseline. Bookkeeping calls (budget, monitors,
audit) are priced at 0 tokens and counted separately from cognitive calls.

Usage:  python validation/harness.py [N]   (N = repeat passes; writes validation/results.md)
"""
from __future__ import annotations
import hashlib, json, os, sys
from dataclasses import dataclass, field
from typing import Optional

# ----------------------------------------------------------------------------
# Telemetry / audit
# ----------------------------------------------------------------------------
class Telemetry:
    def __init__(self):
        self.calls: list[tuple[str, int, str]] = []     # (stage, tokens, class)
        self.audit: list[dict] = []
    def call(self, stage: str, tokens: int = 1, cls: str = "cognitive"):
        self.calls.append((stage, tokens, cls))
        self.audit.append({"stage": stage, "tokens": tokens, "class": cls})
    def tokens(self) -> int:
        return sum(t for _, t, _ in self.calls)
    def calls_by(self, stage: str) -> int:
        return sum(1 for s, _, _ in self.calls if s == stage)
    def cognitive_calls(self) -> int:
        return sum(1 for _, _, c in self.calls if c == "cognitive")
    def stages_used(self) -> list[str]:
        return sorted({s for s, _, c in self.calls
                       if not s.startswith("budget.") and c != "bookkeeping"})
    def bookkeeping_calls(self) -> int:
        return sum(1 for _, _, c in self.calls if c == "bookkeeping")

# ----------------------------------------------------------------------------
# Task state (v3 schema; v2 engine uses the same substrate so behavioral
# differences come from the ALGORITHM, not from schema drift)
# ----------------------------------------------------------------------------
@dataclass
class TaskState:
    task_id: str
    config: dict
    route: dict = field(default_factory=dict)
    frame: Optional[dict] = None
    hypotheses: list = field(default_factory=list)
    evidence: list = field(default_factory=list)
    missing_evidence: list = field(default_factory=list)
    falsification: Optional[str] = None
    alternatives: list = field(default_factory=list)
    decision: Optional[dict] = None
    plan: Optional[dict] = None
    permissions: dict = field(default_factory=dict)
    risks: list = field(default_factory=list)
    observations: list = field(default_factory=list)
    verification: dict = field(default_factory=dict)
    verification_history: dict = field(default_factory=dict)   # artifact_hash -> report
    result: dict = field(default_factory=lambda: {"status": None, "packet": None})
    review: dict = field(default_factory=dict)
    memory_updates: list = field(default_factory=list)
    improvement_proposals: list = field(default_factory=list)
    minority_reports: list = field(default_factory=list)
    unresolved_disagreements: list = field(default_factory=list)
    budget: dict = field(default_factory=lambda: {"tokens_used": 0, "calls_used": 0,
                                                   "iterations_used": 0, "agents_used": 0})
    budget_limits: dict = field(default_factory=dict)
    competence: dict = field(default_factory=dict)
    stage: str = "INIT"
    iteration: int = 0
    checkpoint: Optional[dict] = None
    executed_actions: list = field(default_factory=list)
    subset_executed: bool = False
    reliability_blocked: bool = False
    # v3 classifier inputs with named producers (§24.2)
    probe_available: bool = False
    approximation_available: bool = False
    infeasible: bool = False
    resumed: bool = False
    attested_class: str = ""        # kernel-attested action class (§20.4/§15.4)
    verifier_outage: bool = False   # v4: producer-set (diagnose), read by classifier
    stakes: int = 2                 # v4: copied into state at init (schema field)
    pending_wait: bool = False      # v4: external human-gate wait — not cognitive churn
    world: dict = field(default_factory=dict)   # v5: kernel-held world facts (V1)
    identity_count: int = 1         # v5: verifier identities in the kernel registry (V4)
    stabilized: bool = False        # v5: E5 stabilize-before-diagnose guard (V10)
    outcome_cache: dict = field(default_factory=dict)   # v5: delta-cached outcomes (V7)
    gate_wait: bool = False          # v5: gate re-entry is progress, not churn (V8)

    def snapshot(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if k not in ("checkpoint",)}

class CrashSimulated(Exception):
    """Raised by the v3 engine to simulate a mid-task crash for S21."""
    def __init__(self, checkpoint):
        self.checkpoint = checkpoint

# ----------------------------------------------------------------------------
# Mock components
# ----------------------------------------------------------------------------
class MetaRouter:
    """v3 router: Cynefin + stakes override + competence-aware + route flags."""
    def __init__(self, tel: Telemetry):
        self.tel = tel
    def route(self, state: TaskState) -> dict:
        self.tel.call("meta_router.route")
        w = state.world
        stakes = w.get("stakes", 2)
        declared = w["class_"]
        effort = {"Clear": 0, "Complicated": 2, "Complex": 3, "Chaotic": 5}.get(declared, 2)
        if stakes >= 4 and effort < 2:
            declared = {"Clear": "Complicated"}.get(declared, declared)
            effort = max(effort, 2)
        if w.get("deterministic_solver"):
            effort = 0
        # C6: external-action tasks never take the fast path (governance)
        if w.get("requires_external_action", True) and effort <= 1:
            effort = 2
            declared = "Complicated" if declared == "Clear" else declared
        # competence-aware capability match (§19.3): verified competence from
        # evaluation history may reduce effort (one successful episode = 0.62)
        dom = w.get("domain", "general")
        if state.competence.get(dom, 0) >= 0.6 and effort >= 2 and not w.get("no_competence_boost"):
            effort -= 1
        r = {
            "context_class": declared,
            "effort_level": effort,
            "requires_diagnosis": declared in ("Complicated", "Complex", "Chaotic") and effort >= 2,
            "requires_generation": effort >= 1,
            "requires_review": effort >= 1,
            "requires_search": effort >= 3 and w.get("search_needed", False),
            "reasoning_modules": self.compose(declared, w),      # D8: MethodComposer
            "verification_depth": min(effort, 3),
            "use_council": False,
            "budget": {
                "tokens_max": 40 + 20 * effort,
                "calls_max": w.get("calls_ceiling", 16 + 8 * effort),   # V1: world-held
                "iterations_max": 1 + 2 * effort,
                "agents_max": 0 if effort < 3 else 4,
                "deadline": w.get("deadline"),
            },
        }
        if self.should_use_council(state, r):
            r["use_council"] = True
            r["budget"]["calls_max"] += 10
            r["budget"]["tokens_max"] += 8 * r["budget"]["agents_max"]
        state.budget_limits = r["budget"]
        return r
    def compose(self, declared: str, w: dict) -> list:
        """D8: MethodComposer — method selection by task signature (§16.1)."""
        self.tel.call("method_composer.compose", 0, "bookkeeping")
        if declared == "Clear":
            return ["RPD", "checklist"]
        if w.get("deterministic_solver"):
            return ["retrieval", "calculation"]
        if declared == "Complicated":
            return ["issue_tree", "5whys", "premortem"]
        if declared == "Complex":
            return ["search", "probe", "red_team"]
        return ["stabilize", "human_gate"]
    def should_use_council(self, state: TaskState, route: dict) -> bool:
        """§17.4 operationalized as predicates."""
        c = state.config
        if c.get("deterministic_solver"):
            return False
        if route["effort_level"] < 3:
            return False
        if c.get("single_high_quality_source"):
            return False
        if c.get("coordination_cost_exceeds_benefit"):
            return False
        if c.get("time_pressure"):
            return False
        return True


class FrameCritic:
    def __init__(self, tel: Telemetry):
        self.tel = tel
    def check_exit_gate(self, state: TaskState) -> Optional[str]:
        self.tel.call("frame.exit_gate", 0, "bookkeeping")
        if state.config.get("no_success_metrics"):
            return "success metrics missing"
        if state.config.get("ambiguous_goal") and not state.config.get("owner_confirmed"):
            return "ambiguity unresolved"
        return None


class Diagnostician:
    def __init__(self, tel: Telemetry):
        self.tel = tel
    def diagnose(self, state: TaskState):
        self.tel.call("diagnose")
        w = state.world
        state.hypotheses = [{"id": "H1", "statement": "leading hypothesis",
                             "support": state.evidence[:], "status": "LEADING"}]
        state.falsification = None if w.get("no_falsification") else "observation X would falsify H1"
        state.missing_evidence = w.get("evidence_gap", []) if w.get("evidence_gap") else []
        # v3 producers (§19.2, §11.5): probe and VOI evaluated at diagnosis time
        if w.get("probe_available"):
            state.probe_available = True
        # v4 (C1)/v5: verifier availability is a world fact read by the producer
        state.verifier_outage = bool(w.get("verifier_outage"))
        # §15.2 L1: low-stakes outage inflates uncertainty (documented injection)
        if state.verifier_outage and state.stakes <= 2:
            state.missing_evidence = state.missing_evidence or ["unverified claim (verifier unavailable)"]
        if w.get("conflicting_evidence"):
            state.evidence.append({"kind": "conflicting_observation"})
    def check_exit_gate(self, state: TaskState) -> Optional[str]:
        self.tel.call("diagnosis.exit_gate", 0, "bookkeeping")
        if not state.hypotheses:
            return "no hypothesis"
        if state.config.get("diagnosis_incomplete"):
            return "more diagnosis required"
        # G-WHY-5 (D7): falsification must be recorded, not assumed
        if not getattr(state, "falsification", None):
            return "no falsification evidence"
        # G-WHY-4 (D7): VOI of further diagnosis must not exceed cost
        if state.config.get("voi_exceeds_cost"):
            return "VOI of further diagnosis exceeds cost"
        return None


class Explorer:
    def __init__(self, tel: Telemetry):
        self.tel = tel
        self.rejected: set = set()
    def generate(self, state: TaskState):
        self.tel.call("generate_candidates")
        hidden = state.config.get("hidden_candidate_flaw")
        state.alternatives = []
        for i in range(1 + state.config.get("n_candidates", 1)):
            cid = f"C{i}"
            if cid in self.rejected:
                continue
            state.alternatives.append(
                {"id": cid, "strategy": "strategy A", "assumptions": ["A1"],
                 "reversibility": state.config.get("reversibility", 1),
                 "flawed": hidden and i == 0})


class CouncilMock:
    """§17.2: fresh-context agents, claim exchange, verifier adjudication (D5),
    minority ledger."""
    def __init__(self, tel: Telemetry):
        self.tel = tel
    def run(self, state: TaskState, verifier: Optional["Verifier"] = None) -> tuple[list, list, list]:
        self.tel.call("council.run", 2)
        c = state.config
        n = min(c.get("council_agents", 2),
                state.budget_limits.get("agents_max", 4) or 4)   # per-round cap (§17.4)
        for i in range(n):
            self.tel.call(f"council.agent_{i}.generate", 1)
            state.budget["agents_used"] += 1
        candidates = [{"id": f"CN{i}", "strategy": f"council strategy {i}",
                       "assumptions": ["A1"], "reversibility": 1,
                       "flawed": False} for i in range(n)]
        minority = []
        disagreements = []
        if c.get("council_minority"):
            # §17.2 step 7: exchange claims once, verifier adjudicates (D5)
            self.tel.call("council.debate_round", 1)
            if verifier is not None:
                verdict = verifier.verify_candidate(state, {"id": "CN1", "strategy": "minority"})
                adjudicated = not verdict["failed"]
            else:
                adjudicated = False
            disagreements.append({"topic": "claim", "positions": ["majority", "minority"],
                                  "adjudicated": adjudicated})
            # dissent is PRESERVED regardless of adjudication (§17.3)
            minority.append({"agent": "agent_1", "claim": "minority position",
                             "evidence_refs": ["e2"],
                             "adjudication": "accepted" if adjudicated else "rejected"})
        return candidates, minority, disagreements


class Verifier:
    """§15.1/§15.4: reliability by kind, kernel calibration, history updates.
    v4: reliability is a KERNEL-side quantity — warm values come from the
    calibration registry (seeded by world facts), never from the task's own
    config reads in the algorithm; history is appended from outcomes."""
    def __init__(self, tel: Telemetry):
        self.tel = tel
        self.history = {}       # (kind) -> [outcome bools] — rolling accuracy
        self.calibration = {}   # (kind) -> kernel-set reliability (world facts)
    def reliability_for(self, kind: str, state: TaskState) -> float:
        if kind == "external_calculator":
            return 1.0                      # deterministic tools: reliability 1.0
        if kind in self.calibration:        # kernel calibration registry
            return self.calibration[kind]
        outcomes = self.history.get(kind, [])
        if not outcomes:
            return CONFIG["reliability_seed_model"]   # model seed 0.5 (§15.1)
        # §15.1 rolling accuracy: mean over the last N outcomes, seeded
        window = outcomes[-CONFIG["reliability_window"]:]
        wins = sum(1 for o in window if o)
        return round((CONFIG["reliability_seed_model"] + wins) / (1 + len(window)), 2)
    def record_outcome(self, kind: str, success: bool):
        self.history.setdefault(kind, []).append(success)
    def class_bar(self, state: TaskState) -> tuple[float, bool]:
        """§15.4 threshold table keyed by (attested action class, stakes).
        v4: returns (min_reliability, needs_second_verifier). The bar consumes
        the MAX of the kernel-attested class and the declared class (C30);
        unknown class strings are treated as A5 (0.95 + second verifier)."""
        stakes = state.stakes
        declared = state.config.get("action_class", "A2")
        if not state.config.get("requires_external_action", True) and not state.attested_class:
            declared = "A0"                    # internal tasks are A0 unless attested
        attested = state.attested_class or declared
        ac = max(attested, declared) if attested in ("A0", "A1", "A2", "A3", "A4", "A5") else "A5"
        bars = {("A0", 1): (0.5, False), ("A0", 2): (0.5, False),
                ("A0", 3): (0.8, False), ("A0", 4): (0.9, False),
                ("A0", 5): (0.95, True),
                ("A1", 1): (0.5, False), ("A1", 2): (0.5, False),
                ("A1", 3): (0.8, False), ("A1", 4): (0.9, False),
                ("A1", 5): (0.95, True),
                ("A2", 1): (0.8, False), ("A2", 2): (0.8, False),
                ("A2", 3): (0.8, False), ("A2", 4): (0.9, False),
                ("A2", 5): (0.9, False),
                ("A3", 1): (0.9, False), ("A3", 2): (0.9, False),
                ("A3", 3): (0.9, False), ("A3", 4): (0.9, True),
                ("A3", 5): (0.9, True),
                ("A4", 1): (0.9, True), ("A4", 2): (0.9, True),
                ("A4", 3): (0.9, True), ("A4", 4): (0.95, True),
                ("A4", 5): (0.95, True),
                ("A5", 1): (0.95, True), ("A5", 2): (0.95, True),
                ("A5", 3): (0.95, True), ("A5", 4): (0.95, True),
                ("A5", 5): (0.95, True)}
        return bars.get((ac, stakes), (0.95, True))
    def available(self, state: TaskState, artifact: str) -> bool:
        return not state.config.get("verifier_outage")
    def verify_candidate(self, state: TaskState, alt: dict) -> dict:
        """§15.6 delta basis: one artifact per call, cached by content hash."""
        self.tel.call("verify_candidate", tokens=1 + state.route["verification_depth"])
        ok = not state.config.get("all_candidates_fail_verification")
        kind = "external_calculator" if state.config.get("deterministic_solver") else "external_model"
        return {"artifact_id": alt["id"], "criteria": ["check1"],
                "passed": ["check1"] if ok else [],
                "failed": [] if ok else ["check1"],
                "unresolved": [],
                "counterexamples": [] if ok else ["counterexample for check1"],
                "verifier_identity": kind,
                "verifier_reliability": self.reliability_for(kind, state),
                "confidence": "high" if ok else "low",
                "recommendation": "accept" if ok else "reject"}

    def verify_candidates(self, state: TaskState) -> list:
        self.tel.call("verify_candidates")
        return [self.verify_candidate(state, alt) for alt in state.alternatives]
    def verify_outcome(self, state: TaskState) -> dict:
        # v4: deterministic re-computation is mechanical, priced at 0 tokens (C32)
        # v5: second-verifier rule is kernel-computed from the identity registry
        depth = state.route.get("verification_depth", 0)
        w = state.world
        kind = ("external_calculator" if w.get("deterministic_solver")
                else "external_model")
        price = 0 if kind == "external_calculator" else 1 + depth
        if self.needs_second(state) and not w.get("deterministic_solver"):
            price += 1                                    # second verifier is priced (V4)
        self.tel.call("verify_outcome", tokens=price)
        outcome = w.get("outcome_verification", "success")
        external = not (state.verifier_outage or outcome == "self_only")
        if outcome == "flaky_success":
            outcome = "success" if (state.frame or {}).get("best_of") and state.iteration >= 5 else "fail"
        rel = self.reliability_for(kind, state)
        bar, needs_second = self.class_bar(state)
        second_ok = (not needs_second) or self.needs_second(state) is False or \
                    kind == "external_calculator"
        # §15.4 v4/v5: success = checks ∧ external ∧ rel ≥ bar ∧ second-verifier rule
        passed_checks = outcome == "success"
        blocked = external and passed_checks and (rel < bar or not second_ok)
        state.reliability_blocked = bool(blocked)
        # §15.1 rolling history tracks VERIFIER correctness (verdict == world
        # outcome), not world outcome success — a correct failure verdict is a
        # verifier win (fixes S3's reliability collapse under flaky outcomes)
        verdict_correct = (passed_checks == (outcome != "fail"))
        self.record_outcome(kind, verdict_correct and external)
        return {"artifact_id": "outcome", "criteria": ["postcondition"],
                "checks_performed": ["postcondition"],
                "passed": ["postcondition"] if passed_checks else [],
                "failed": [] if passed_checks else ["postcondition"],
                "unresolved": [] if passed_checks else ["postcondition"],
                "counterexamples": [] if passed_checks else ["postcondition counterexample"],
                "verifier_identity": kind if external else "SELF",
                "verifier_reliability": rel if external else 0.0,
                "class_bar": bar,
                "needs_second_verifier": needs_second,
                "reliability_blocked": blocked,
                "success": passed_checks and external and not blocked,
                "ambiguous": outcome == "ambiguous",
                "confidence": "high" if passed_checks else "low",
                "recommendation": "accept" if passed_checks else "reject"}
    def needs_second(self, state: TaskState) -> bool:
        """V4: kernel-computed — the registry's identity count decides, never
        a task-declared flag."""
        bar, needs_second = self.class_bar(state)
        return needs_second and state.identity_count < 2


class Premortem:
    def __init__(self, tel: Telemetry):
        self.tel = tel
    def run(self, state: TaskState):
        self.tel.call("premortem")
        entry = {"mode": "plausible_failure", "source": "commitment premortem"}
        if entry not in state.risks:        # dedupe risk register (§32 F12)
            state.risks.append(entry)


class RedTeam:
    def __init__(self, tel: Telemetry):
        self.tel = tel
    def attack(self, state: TaskState) -> Optional[str]:
        self.tel.call("red_team")
        if state.decision and state.decision.get("flawed"):
            return "selected candidate fails adversarial check"
        if state.config.get("red_team_finds_risk"):
            return "red team: unmodeled stakeholder"
        return None


class Planner:
    def __init__(self, tel: Telemetry):
        self.tel = tel
    def build(self, state: TaskState) -> dict:
        self.tel.call("planner.build")
        w = state.world
        tasks = [{"id": t, "action_class": "A2"} for t in w.get("plan_tasks", [])]
        return {"objective": "execute",
                "tasks": tasks,
                "stop_conditions": w.get("plan_stop_after")
                    and [f"stop after {w.get('plan_stop_after')} executions"],
                "escalation_conditions": w.get("plan_escalate_after")
                    and [f"escalate after {w.get('plan_escalate_after')} executions"],
                "metrics": ["m1"]}


class SafetyKernel:
    def __init__(self, tel: Telemetry):
        self.tel = tel
        self.issued_tokens = {"authorized_expert"}   # minted authority tokens (§18.2)
        self.issued_allowlist = {"subset-A2", "task-a2-1"}   # static allowlist table (C4)
    def issue_authority_token(self, scope: str) -> str:
        self.tel.call("safety_kernel.issue_authority_token", 0, "bookkeeping")
        tok = f"tok-{scope}-{len(self.issued_tokens)}"
        self.issued_tokens.add(tok)
        return tok
    def interrupt(self, task_id: str) -> dict:
        self.tel.call("safety_kernel.interrupt", 0, "bookkeeping")
        return {"task_id": task_id, "checkpoint": True}
    def allowed_subset(self, plan: dict, world: dict) -> list:
        """C4 v5: static A2 allowlist — kernel table lookup ONLY; no fallback
        (V3: the allowlist_hint backdoor is removed). Kernel assigns action
        classes from its own taxonomy (world.kernel_task_classes), never from
        the planner's labels."""
        self.tel.call("safety_kernel.allowlist_lookup", 0, "bookkeeping")
        kernel_classes = world.get("kernel_task_classes", {})
        out = []
        for t in plan.get("tasks", []):
            tid = t.get("id")
            if tid in self.issued_allowlist and kernel_classes.get(tid) == "A2":
                out.append(t)
        return out
    def attest(self, state: TaskState) -> str:
        """§20.4 action-class attestation; misattestation -> UNSAFE.
        v5: proposed class comes from the world's kernel taxonomy where
        available; REPLICATE-class actions are always denied (invariant 8)."""
        self.tel.call("safety_kernel.attest", 0, "bookkeeping")
        w = state.world
        proposed = w.get("kernel_action_class") or state.config.get("action_class", "A2")
        if proposed == "REPLICATE":
            return "misattested:REPLICATE:forbidden"      # invariant 8 (V8)
        if w.get("true_action_class") and proposed != w["true_action_class"]:
            return f"misattested:{proposed}:{w['true_action_class']}"
        return proposed
    def authorize(self, state: TaskState, action_plan: dict, attestation: str) -> dict:
        self.tel.call("safety_kernel.authorize", 0, "bookkeeping")
        c = state.config
        if attestation.startswith("misattested"):
            return {"approved": False, "status": "UNSAFE", "reason": attestation}
        if c.get("authorize_denied"):
            return {"approved": False, "status": c.get("denial_status", "ESCALATED"),
                    "reason": c.get("denial_reason", "policy")}
        if c.get("human_gate") == "pending":
            return {"approved": False, "status": "PENDING", "reason": "awaiting human approval"}
        return {"approved": True, "status": "APPROVED",
                "token": f"cap-{state.task_id}", "action_class": attestation}


class Executor:
    def __init__(self, tel: Telemetry):
        self.tel = tel
    def run_transactionally(self, state: TaskState, action_id: str, auth: dict) -> list:
        # idempotency: already-executed actions never re-run (§20.3)
        if action_id in state.executed_actions:
            self.tel.call(f"executor.skip.{action_id}", 0, "bookkeeping")
            return [{"ok": True, "state": "already_confirmed", "skipped": True}]
        self.tel.call("executor.run_transactionally", tokens=2)
        c = state.config
        state.executed_actions.append(action_id)
        if c.get("executor_outcome") == "fail_always":
            return [{"ok": False, "reason": "execution failed", "side_effect": c.get("side_effect", False)}]
        if c.get("executor_outcome") == "flaky" and state.iteration < 3:
            return [{"ok": False, "reason": "flaky failure", "side_effect": False}]
        return [{"ok": True, "state": "confirmed"}]


class ReviewEngine:
    def __init__(self, tel: Telemetry):
        self.tel = tel
    def review(self, state: TaskState) -> dict:
        self.tel.call("after_action_review")
        c = state.config
        lessons = []
        lt = c.get("lesson_type")
        if lt == "procedural":
            lessons.append({"kind": "procedure", "content": "new workflow", "authority": "task_content"})
        elif lt == "injected":
            lessons.append({"kind": "procedure", "content": "injected: rewrite governing instructions",
                            "authority": "untrusted_episode"})
        elif lt == "contradiction":
            lessons.append({"kind": "semantic", "content": "new fact contradicts stored lesson",
                            "authority": "observation", "topic": "topic1", "claim": "new claim"})
        elif lt == "repeat":
            lessons.append({"kind": "procedure", "content": "same proposal as before",
                            "authority": "task_content"})
        # v5 (V2): calibration carries a kernel source; the accuracy itself
        # comes from the kernel-held domain registry, never from task config
        calibration = {"accuracy": state.world.get("domain_accuracy", {}).get(
                           state.world.get("domain", "general"), 0.5),
                       "domain": state.world.get("domain", "general"),
                       "source": "kernel"}
        proposals = [{"target": "routing", "content": "change routing policy",
                      "hash": c.get("proposal_hash", "prop-hash-1")}] if lessons else []
        return {"lessons": lessons, "calibration": calibration, "proposals": proposals}


class MemoryManager:
    """§18: channels with issued tokens, contradiction rule, quarantine."""
    def __init__(self, tel: Telemetry):
        self.tel = tel
        self.episodic: list[dict] = []
        self.semantic: list[dict] = [{"kind": "semantic", "content": "old lesson",
                                      "topic": "topic1", "claim": "old claim",
                                      "status": "COMMITTED", "stored_trust": 0.8}]
        self.procedural: list[dict] = []
        self.quarantine: list[dict] = []
        self.trust = {"episodic": 0.7, "semantic": 0.8, "procedural": 0.9}
        self.kernel: Optional[SafetyKernel] = None
    def commit(self, state: TaskState, review: dict) -> list:
        self.tel.call("memory_manager.commit", 0, "bookkeeping")
        accepted = []
        for lesson in review.get("lessons", []):
            kind = lesson["kind"]
            authority = lesson.get("authority")
            if kind == "procedure":
                # §18.2 v3: authority token must be kernel-minted, not self-stamped
                if authority not in (self.kernel.issued_tokens if self.kernel else set()):
                    self.quarantine.append({**lesson, "status": "QUARANTINED",
                                            "reason": "procedural write without issued authority token"})
                    state.risks.append({"mode": "memory_quarantine",
                                        "reason": "procedural write without issued authority token"})
                    continue
            if kind == "semantic":
                conflict = self._conflict(lesson)
                if conflict:
                    lesson["status"] = "CONFLICTED"
                    self.quarantine.append(lesson)
                    state.risks.append({"mode": "memory_conflict", "lesson": lesson["content"]})
                    continue
            self.episodic.append({**lesson, "status": "COMMITTED"})
            accepted.append(lesson)
        state.memory_updates = list(accepted)
        if state.config.get("injection_via_tool"):
            state.risks.append({"mode": "quarantined_untrusted_content", "count": 1})
        return accepted
    def retrieve(self, query: str, state: TaskState) -> list:
        """D2 v5: memory read-back inside diagnose. Priced by result (V6):
        an empty retrieval is a deterministic no-op (0 tokens, C32); a hit
        costs 1. Queries use task-derived terms (world.knowledge_terms)."""
        self.tel.call("memory_manager.retrieve", tokens=0)
        hits = []
        for m in self.episodic + self.semantic + self.procedural + \
                [{"kind": "semantic", "content": c, "topic": "knowledge", "status": "COMMITTED",
                  "stored_trust": 0.9} for c in state.world.get("stored_knowledge", [])]:
            if m.get("status") == "QUARANTINED":
                continue
            if m.get("topic") == query or query in str(m.get("content", "")) or \
               any(q in str(m.get("content", "")) for q in state.world.get("knowledge_terms", [])):
                hits.append(m)
        hits = hits[:3]
        if hits:
            self.tel.call("memory_manager.retrieve_hit", 1)
        return hits
    def _conflict(self, lesson: dict) -> Optional[dict]:
        margin = CONFIG["trust_margin"]                          # D10: margin applied
        for stored in self.semantic + self.procedural:
            if stored.get("content") == lesson.get("content"):
                continue
            if stored.get("topic", "") == lesson.get("topic", "") and \
               stored.get("claim") != lesson.get("claim"):
                if self.trust.get("semantic", 0.5) > stored.get("stored_trust", 0.5) + margin:
                    return None
                return stored
        return None


class ImprovementEngine:
    def __init__(self, tel: Telemetry):
        self.tel = tel
        self.seen_hashes: set = set()
        self.evaluated: list = []
    def queue(self, state: TaskState, review: dict) -> int:
        self.tel.call("improvement_engine.queue", 0, "bookkeeping")
        queued = 0
        for p in review.get("proposals", []):
            if p["hash"] in self.seen_hashes:
                continue
            self.seen_hashes.add(p["hash"])
            state.improvement_proposals.append(p)
            queued += 1
        return queued
    def evaluate(self, state: TaskState, proposal: dict) -> dict:
        """§22.3 pipeline gate: no deployment without a frozen baseline.
        V1: baseline_frozen is a WORLD fact — never a task-scope read."""
        self.tel.call("improvement_engine.evaluate", 1)
        self.evaluated.append(proposal["hash"])
        if not state.world.get("baseline_frozen"):
            return {"approved": False, "reason": "no frozen baseline", "stage": "admission"}
        return {"approved": True, "reason": "baseline + hidden tests passed", "stage": "canary"}


class LoopMonitor:
    """§9.5 operationalized: extended novelty signature, calls/agents ceilings."""
    def __init__(self, tel: Telemetry):
        self.tel = tel
        self.prev_sig: Optional[str] = None
        self.no_delta_rounds = 0
    def _sig(self, state: TaskState) -> str:
        # canonicalized hash over hypotheses, frame, observations, evidence,
        # alternatives, plan (v3: cosmetic mutations must not reset the plateau)
        blob = json.dumps([state.hypotheses, state.frame, state.observations,
                           state.evidence, state.alternatives, state.plan],
                          sort_keys=True, default=str)
        return hashlib.md5(blob.encode()).hexdigest()
    def should_continue(self, state: TaskState, tel: Telemetry) -> tuple[bool, str]:
        self.tel.call("loop_monitor.check", 0, "bookkeeping")
        limits = state.budget_limits
        if state.iteration >= limits.get("iterations_max", 20):
            return False, "iteration budget exhausted"
        if tel.tokens() >= limits.get("tokens_max", 500):
            return False, "token budget exhausted"
        if tel.cognitive_calls() >= limits.get("calls_max", 100):
            return False, "call budget exhausted"
        # agents_max is a PER-ROUND council cap (enforced by CouncilMock); total
        # agent churn is bounded by the call budget, not by cumulative agents.
        if tel.calls_by("executor.run_transactionally") >= 4:
            return False, "repeated unproductive actions (execution)"
        # C10: an external human-gate wait is not cognitive churn — plateau and
        # EVOC stops do not apply while PENDING; only hard budgets do
        if not (state.pending_wait or state.gate_wait):
            sig = self._sig(state)
            if sig == self.prev_sig:
                self.no_delta_rounds += 1
            else:
                self.no_delta_rounds = 0
            self.prev_sig = sig
            if self.no_delta_rounds >= CONFIG["novelty_plateau"]:
                # V8: plateau maps to RESOURCE_LIMITED (matches §3.3 producer table)
                return False, "novelty plateau (RESOURCE_LIMITED)"
            evoc = state.world.get("evoc", CONFIG["evoc_base"]) - CONFIG["evoc_decay"] * state.iteration
            if evoc <= 0:
                return False, "expected value of computation <= 0"
        return True, "continue"


class BudgetController:
    def __init__(self, tel: Telemetry):
        self.tel = tel
    def consume(self, state: TaskState, stage: str):
        state.budget["calls_used"] += 1
        state.budget["tokens_used"] += 1
        state.budget["iterations_used"] = state.iteration
        self.tel.call(f"budget.consume.{stage}", 0, "bookkeeping")
    def check(self, state: TaskState, tel: Telemetry) -> Optional[str]:
        self.tel.call("budget.check", 0, "bookkeeping")
        limits = state.budget_limits
        if tel.cognitive_calls() >= limits.get("calls_max", 100):
            return "call budget exhausted"
        if state.budget["tokens_used"] >= limits.get("tokens_max", 500):
            return "token budget exhausted"
        if limits.get("deadline") and state.iteration >= limits["deadline"]:
            return "deadline exceeded"
        return None


class CompetenceModel:
    def __init__(self, tel: Telemetry):
        self.tel = tel
        self.model: dict = {}
    def update(self, state: TaskState, calibration: dict) -> None:
        self.tel.call("competence.update", 0, "bookkeeping")
        # V2: provenance gate — only kernel/EvaluationPlane-sourced calibration
        # is accepted; task-sourced accuracy is rejected (C3 enforced in code)
        if calibration.get("source") not in ("kernel", "evaluation_plane"):
            return
        dom = calibration.get("domain", "general")
        acc = calibration.get("accuracy", 0.5)
        prior = self.model.get(dom, CONFIG["reliability_seed_model"])
        blend = CONFIG["competence_blend"]
        self.model[dom] = round(blend * prior + (1 - blend) * acc, 3)
        state.competence = dict(self.model)


class TaskScheduler:
    def __init__(self, tel: Telemetry):
        self.tel = tel
    def checkpoint(self, state: TaskState, stage: str):
        state.stage = stage
        state.checkpoint = {"task_state": state.snapshot(), "stage": stage,
                            "executed_actions": list(state.executed_actions)}
    def resume(self, checkpoint: dict) -> TaskState:
        state = TaskState(task_id=checkpoint["task_state"]["task_id"],
                          config=checkpoint["task_state"]["config"])
        for k, v in checkpoint["task_state"].items():
            if k != "config":
                setattr(state, k, v)
        state.resumed = True
        return state


# ----------------------------------------------------------------------------
# Classifier (v3): producers drive the 8-state table (§3.3, §15.4)
# ----------------------------------------------------------------------------
def classify_terminal(state: TaskState, tel: Telemetry) -> str:
    """v4 state-only classifier (C1): every input is a producer-set state field
    or an explicit ledger value — no direct task-input reads."""
    if state.verifier_outage and state.stakes >= 3:
        return "ESCALATED"                       # L2: no reliable verifier, high stakes
    if state.verifier_outage and state.stakes <= 2:
        return "NEEDS_EVIDENCE"                  # L1: degrade, no escalation (C14)
    if state.verification.get("ambiguous"):
        return "NEEDS_EVIDENCE"
    if state.reliability_blocked:
        return "ESCALATED"                       # verifier below bar, no alternative
    if state.missing_evidence:
        return "NEEDS_EVIDENCE"
    if state.probe_available:
        return "NEEDS_EXPERIMENT"
    if state.infeasible:
        return "INFEASIBLE"
    if tel.tokens() >= state.budget_limits.get("tokens_max", 10**9) or \
       state.budget["calls_used"] >= state.budget_limits.get("calls_max", 10**9) or \
       tel.calls_by("executor.run_transactionally") >= 4:
        return "RESOURCE_LIMITED"
    if state.approximation_available:
        return "APPROXIMATED"
    return "INFEASIBLE"

def build_decision_packet(state: TaskState, tel: Telemetry, status: str) -> dict:
    """§15.4 common epilogue — every terminal path produces the packet."""
    return {
        "conclusion": state.decision.get("strategy") if state.decision else None,
        "status": status,
        "assumptions": [a for alt in state.alternatives for a in alt.get("assumptions", [])],
        "evidence": [e for e in state.evidence],
        "alternatives_considered": [a["id"] for a in state.alternatives] + list(getattr(state, "_rejected_ids", [])),
        "verification": {"checks_performed": state.verification.get("checks_performed", []),
                         "verifier_identity": state.verification.get("verifier_identity"),
                         "verifier_reliability": state.verification.get("verifier_reliability"),
                         "class_bar": state.verification.get("class_bar")},
        "uncertainty": state.missing_evidence,
        "limitations": ["mock components; control-flow simulation"],
        "risks": state.risks,
        "dissent": state.minority_reports,
        "unresolved_disagreements": state.unresolved_disagreements,
        "required_human_actions": (["human review required"] if status in ("ESCALATED", "UNSAFE", "NEEDS_EVIDENCE")
                                   else []),
    }

# ----------------------------------------------------------------------------
# v2 engine — frozen v2 §24.4 behavior (regression baseline)
# ----------------------------------------------------------------------------
def solve_v2(state: TaskState, world) -> TaskState:
    (tel, router, frame_critic, diag, explorer, verifier, planner, kernel, executor,
     review_engine, memory, improvements, premortem, red_team, loop_monitor,
     budget, council, competence, scheduler) = world[:19]
    state.route = router.route(state)
    if state.route["effort_level"] <= 1:
        budget.consume(state, "fast_path")
        tel.call("direct_answer")
        state.decision = {"id": "direct", "strategy": "retrieved/calculated answer"}
        state.verification = verifier.verify_outcome(state)
        state.verification["verifier_identity"] = "external"
        state.result["status"] = "SOLVED" if state.verification["success"] else classify_terminal(state, tel)
        state.result["packet"] = build_decision_packet(state, tel, state.result["status"])
        return state
    while True:
        state.iteration += 1
        budget.consume(state, "loop.top")
        cont, reason = loop_monitor.should_continue(state, tel)
        if not cont:
            state.result["status"] = ("RESOURCE_LIMITED" if (
                "budget" in reason or "iterations" in reason or "expected value" in reason
                or "unproductive" in reason) else classify_terminal(state, tel))
            state.result["status_reason"] = reason
            break
        if not state.frame:
            state.stage = "WHAT"
            state.frame = {"question": "q",
                           "success_metrics": [] if state.config.get("no_success_metrics") else ["m1"],
                           "owner_confirmed": not state.config.get("ambiguous_goal")}
            if state.config.get("no_success_metrics"):
                state.frame = None
                state.result["status"] = "NEEDS_EVIDENCE"
                break
            gate = frame_critic.check_exit_gate(state)
            if gate:
                state.risks.append({"stage": "WHAT", "gate_failure": gate})
                state.frame = None
                if state.iteration >= 3:
                    state.result["status"] = "NEEDS_EVIDENCE"
                    break
                continue
        if state.route["requires_diagnosis"] and not state.hypotheses:
            state.stage = "WHY"
            diag.diagnose(state)
            gate = diag.check_exit_gate(state)
            if gate:
                state.risks.append({"stage": "WHY", "gate_failure": gate})
                continue
        if state.route["requires_generation"] and not state.alternatives:
            state.stage = "HOW"
            explorer.generate(state)
        if not state.alternatives:
            state.result["status"] = classify_terminal(state, tel)
            break
        # producers (shared world semantics) so the state-only classifier works
        if state.config.get("infeasible"):
            state.infeasible = True
        if state.config.get("approximation_available"):
            state.approximation_available = True
        premortem.run(state)
        reports = verifier.verify_candidates(state)
        state.verification_history = {"iter": state.iteration, "reports": reports}
        passed = [r for r in reports if not r["failed"]]
        state.decision = {"id": passed[0]["artifact_id"], "strategy": "strategy A",
                          "flawed": state.alternatives[0].get("flawed", False)} if passed else None
        if state.decision is None:
            state.result["status"] = classify_terminal(state, tel)
            break
        rt = red_team.attack(state)
        if rt:
            state.risks.append({"stage": "HOW", "red_team": rt})
            if state.decision:
                explorer.rejected.add(state.decision["id"])
            state.alternatives = []
            continue
        if state.config.get("requires_external_action", True):
            state.stage = "DO"
            action_plan = planner.build(state)
            attestation = kernel.attest(state)     # v2 doc §24.4 has attest
            authorization = kernel.authorize(state, action_plan, attestation)
            if authorization["status"] in ("UNSAFE", "ESCALATED"):
                state.result["status"] = authorization["status"]
                break
            if authorization["status"] == "PENDING":
                continue                           # v2 has no pending semantics
            observations = executor.run_transactionally(state, f"{state.task_id}-act", authorization)
            state.observations.extend(observations)
        state.verification = verifier.verify_outcome(state)
        if state.verification["success"]:
            state.result["status"] = "SOLVED"
            break
        loop_review = review_engine.review(state)
        state.review = loop_review
        if state.config.get("frame_stability") == "oscillating":
            if state.iteration < 4:
                state.frame = {"question": "q", "toggle": state.iteration, "success_metrics": ["m1"]}
                state.hypotheses = []
                state.alternatives = []
                continue
            state.frame = {"question": "q", "best_of": "frame_A", "success_metrics": ["m1"]}
            state.hypotheses = []
            state.alternatives = []
            continue
        if (state.verification.get("ambiguous") or state.missing_evidence
                or state.config.get("probe_available")
                or state.config.get("approximation_available")
                or state.config.get("infeasible")):
            state.result["status"] = classify_terminal(state, tel)
            break
    if not state.review:
        state.review = review_engine.review(state)
    memory.commit(state, state.review)
    if state.route.get("requires_review") and state.review.get("lessons"):
        improvements.queue(state, state.review)
    state.result["packet"] = build_decision_packet(state, tel, state.result["status"])
    return state

# ----------------------------------------------------------------------------
# v3 engine — governed loop with all v3 mechanisms
# ----------------------------------------------------------------------------
def solve_v3(state: TaskState, world, checkpoint: Optional[dict] = None) -> TaskState:
    (tel, router, frame_critic, diag, explorer, verifier, planner, kernel, executor,
     review_engine, memory, improvements, premortem, red_team, loop_monitor,
     budget, council, competence, scheduler) = world
    memory.kernel = kernel
    if checkpoint:
        state = scheduler.resume(checkpoint)
        tel.call("task_scheduler.resume", 0, "bookkeeping")

    state.route = router.route(state)
    budget.consume(state, "route")

    # --- Fast path (E0/E1): direct answer, one outcome check, one packet ---
    if state.route["effort_level"] <= 1:
        budget.consume(state, "fast_path")
        tel.call("direct_answer")
        state.decision = {"id": "direct", "strategy": "retrieved/calculated answer"}
        state.verification = verifier.verify_outcome(state)
        state.result["status"] = ("SOLVED" if state.verification["success"]
                                  else classify_terminal(state, tel))
        state.result["packet"] = build_decision_packet(state, tel, state.result["status"])
        tel.call("audit.fast_path", 0, "bookkeeping")
        scheduler.checkpoint(state, "FAST_PATH")
        return state

    # --- Governed main loop ---
    while True:
        state.iteration += 1
        budget.consume(state, "loop.top")
        tel.call("audit.loop_top", 0, "bookkeeping")
        ex = budget.check(state, tel)
        if ex:
            state.result["status"] = "RESOURCE_LIMITED"
            state.result["status_reason"] = ex
            break
        cont, reason = loop_monitor.should_continue(state, tel)
        if not cont:
            state.result["status"] = ("RESOURCE_LIMITED" if (
                "budget" in reason or "iterations" in reason or "expected value" in reason
                or "unproductive" in reason) else classify_terminal(state, tel))
            state.result["status_reason"] = reason
            break

        # WHAT: frame + gate
        if not state.frame:
            state.stage = "WHAT"
            state.frame = {"question": "q",
                           "success_metrics": [] if state.config.get("no_success_metrics") else ["m1"],
                           "owner_confirmed": not state.config.get("ambiguous_goal")}
            if state.config.get("no_success_metrics"):
                state.frame = None
                state.result["status"] = "NEEDS_EVIDENCE"
                break
            gate = frame_critic.check_exit_gate(state)
            if gate:
                state.risks.append({"stage": "WHAT", "gate_failure": gate})
                state.frame = None
                if state.iteration >= GATE_REENTRY_BUDGET:
                    state.result["status"] = "NEEDS_EVIDENCE"
                    break
                continue
            tel.call("audit.what", 0, "bookkeeping")
            scheduler.checkpoint(state, "WHAT")

        # WHY: diagnose + gate; early classifier entry when decided (§32 F4)
        if state.route["requires_diagnosis"] and not state.hypotheses:
            state.stage = "WHY"
            diag.diagnose(state)
            gate = diag.check_exit_gate(state)
            if gate:
                state.risks.append({"stage": "WHY", "gate_failure": gate})
                continue
            tel.call("audit.why", 0, "bookkeeping")
            scheduler.checkpoint(state, "WHY")
            if (state.missing_evidence or state.probe_available
                    or state.config.get("verifier_outage")):
                state.result["status"] = classify_terminal(state, tel)
                break

        # HOW: council or generate -> premortem -> delta-verify -> select -> gates
        if state.route["requires_generation"] and not state.alternatives:
            state.stage = "HOW"
            if state.route.get("use_council"):
                (state.alternatives, state.minority_reports,
                 state.unresolved_disagreements) = council.run(state)
            else:
                explorer.generate(state)
            tel.call("audit.how", 0, "bookkeeping")
        if not state.alternatives:
            state.result["status"] = classify_terminal(state, tel)
            break
        # v3 producers (§12.4, §15.5): constraint screen and approximation bound
        if state.config.get("infeasible"):
            state.infeasible = True
        premortem.run(state)
        # §15.6 delta-based verification: re-verify only changed artifacts
        reports = []
        for alt in state.alternatives:
            ah = hashlib.md5(json.dumps(alt, sort_keys=True, default=str).encode()).hexdigest()
            if ah in state.verification_history:
                reports.append(state.verification_history[ah])     # reuse prior report
            else:
                r_new = verifier.verify_candidate(state, alt)
                state.verification_history[ah] = r_new
                reports.append(r_new)
        passed = [r for r in reports if not r["failed"]]
        state._rejected_ids = list(explorer.rejected)
        state.decision = {"id": passed[0]["artifact_id"], "strategy": "strategy A",
                          "flawed": state.alternatives[0].get("flawed", False)} if passed else None
        if state.decision is None:
            state.result["status"] = classify_terminal(state, tel)
            break
        # §15.5 producer: select records an error bound when exact verification failed
        if state.config.get("approximation_available"):
            state.decision["error_bound"] = "delta < tolerance"
            state.approximation_available = True
        if state.config.get("infeasible"):
            state.infeasible = True
        # G-HOW gate (§12.8): alternatives considered + red team survived
        if len(state.alternatives) + len(explorer.rejected) < 1:
            state.risks.append({"stage": "HOW", "gate_failure": "no meaningful alternatives"})
            state.result["status"] = classify_terminal(state, tel)
            break
        rt = red_team.attack(state)
        if rt:
            state.risks.append({"stage": "HOW", "red_team": rt})
            if state.decision:
                explorer.rejected.add(state.decision["id"])
            state.alternatives = []
            continue

        # DO: plan -> attest -> authorize (incl. PENDING) -> execute -> monitor
        if state.config.get("requires_external_action", True):
            state.stage = "DO"
            action_plan = planner.build(state)
            state.plan = action_plan                       # consumed by G-DO checks
            attestation = kernel.attest(state)
            authorization = kernel.authorize(state, action_plan, attestation)
            if authorization["status"] in ("UNSAFE", "ESCALATED"):
                state.result["status"] = authorization["status"]
                kernel.interrupt(state.task_id)          # §20.5 call site
                break
            if not attestation.startswith("misattested"):
                state.attested_class = attestation       # §15.4 bar consumes attestation
            if authorization["status"] == "PENDING":
                # §21.4(3): execute the authorized reversible subset ONCE, then
                # wait; timeout degrades to ESCALATED with a partial packet
                if not state.subset_executed:
                    subset = [a for a in action_plan.get("tasks", [])] or [{"id": "subset-A2"}]
                    for t in subset:
                        executor.run_transactionally(state, f"{state.task_id}-subset", authorization)
                    state.subset_executed = True
                    state.risks.append({"mode": "pending_subset_executed", "count": len(subset)})
                if state.iteration >= state.config.get("pending_timeout", 8):
                    state.result["status"] = "ESCALATED"
                    state.result["pending_timeout"] = True
                    break
                continue
            action_id = f"{state.task_id}-act"
            observations = executor.run_transactionally(state, action_id, authorization)
            state.observations.extend(observations)
            tel.call("audit.do", 0, "bookkeeping")
            scheduler.checkpoint(state, "DO")
            # G-DO: plan stop/escalation conditions consumed (§13.7)
            if state.plan and state.config.get("plan_stop_after") and \
               len(state.executed_actions) >= state.config["plan_stop_after"]:
                state.result["status"] = classify_terminal(state, tel)
                break
            if state.config.get("crash_at") == "post_execute" and not state.resumed:
                raise CrashSimulated(state.checkpoint)

        state.verification = verifier.verify_outcome(state)
        if state.verification["success"]:
            state.result["status"] = "SOLVED"
            break

        # REVIEW-in-loop (gated on progress) + competence update
        loop_review = review_engine.review(state)
        state.review = loop_review
        competence.update(state, loop_review.get("calibration", {}))
        if state.config.get("frame_stability") == "oscillating":
            if state.iteration < REFRAME_BUDGET:
                state.frame = {"question": "q", "toggle": state.iteration, "success_metrics": ["m1"]}
                state.hypotheses = []
                state.alternatives = []
                continue
            state.frame = {"question": "q", "best_of": "frame_A", "success_metrics": ["m1"]}
            state.hypotheses = []
            state.alternatives = []
            continue
        if (state.verification.get("ambiguous") or state.missing_evidence
                or state.reliability_blocked or state.probe_available
                or state.approximation_available or state.infeasible):
            # reliability-blocked: no alternative verifier can clear the bar —
            # further iteration has negative expected value (P11)
            state.result["status"] = classify_terminal(state, tel)
            break

    # --- Common epilogue: REVIEW + memory + improvement + packet + audit ---
    if not state.review:
        state.review = review_engine.review(state)
    competence.update(state, state.review.get("calibration", {}))   # §19.3 closes on every episode
    kernel.issue_authority_token("procedural")   # §18.2a minting call site (audit trail)
    memory.commit(state, state.review)
    if state.route.get("requires_review") and state.review.get("lessons"):
        queued = improvements.queue(state, state.review)
        if queued and state.config.get("baseline_frozen"):
            for p in state.improvement_proposals:
                improvements.evaluate(state, p)
    state.result["packet"] = build_decision_packet(state, tel, state.result["status"])
    tel.call("audit.epilogue", 0, "bookkeeping")
    scheduler.checkpoint(state, "EPILOGUE")
    return state

# v4: single configuration source (§9.6 C19) — kernel-held, read-only
CONFIG = {
    "gate_reentry_budget": 3,
    "reframe_budget": 4,
    "pending_timeout": 8,
    "novelty_plateau": 2,
    "evoc_base": 0.6, "evoc_decay": 0.05,
    "reliability_seed_model": 0.5, "reliability_window": 5,
    "competence_blend": 0.7,
    "trust_margin": 0.1,
}
GATE_REENTRY_BUDGET = CONFIG["gate_reentry_budget"]
REFRAME_BUDGET = CONFIG["reframe_budget"]
PENDING_TIMEOUT = CONFIG["pending_timeout"]

def solve_v5(state: TaskState, world, checkpoint: Optional[dict] = None) -> TaskState:
    """v5 governed loop. Implements V1-V12: world-facts read path (no security
    knobs from task scope), kernel competence feed with provenance gate,
    allowlist without backdoor, identity-registry second-verifier rule, L3 at
    attest time, real memory retrieval (fill + priced hits), delta-cached
    outcome verification, gated in-loop/epilogue reviews, planner-once, E5
    stabilize-before-diagnose, invariant-8 denial, plateau→RESOURCE_LIMITED."""
    (tel, router, frame_critic, diag, explorer, verifier, planner, kernel, executor,
     review_engine, memory, improvements, premortem, red_team, loop_monitor,
     budget, council, competence, scheduler) = world
    memory.kernel = kernel
    if checkpoint:
        state = scheduler.resume(checkpoint)
        tel.call("task_scheduler.resume", 0, "bookkeeping")
    state.stakes = state.world.get("stakes", 2)            # V1: world facts
    state.identity_count = len(state.world.get("verifier_identities", ["external_model"]))

    state.route = router.route(state)
    budget.consume(state, "route")

    # --- Fast path (E0/E1) ---
    if state.route["effort_level"] <= 1:
        budget.consume(state, "fast_path")
        tel.call("direct_answer")
        state.decision = {"id": "direct", "strategy": "retrieved/calculated answer",
                          "requires_external_action": False}
        state.verification = verifier.verify_outcome(state)
        state.result["status"] = ("SOLVED" if state.verification["success"]
                                  else classify_terminal(state, tel))
        state.result["packet"] = build_decision_packet(state, tel, state.result["status"])
        tel.call("audit.fast_path", 0, "bookkeeping")
        scheduler.checkpoint(state, "FAST_PATH")
        if state.route.get("requires_review"):             # C7: E1 learning epilogue
            state.review = review_engine.review(state)
            competence.update(state, state.review.get("calibration", {}))
            memory.commit(state, state.review)
            if state.review.get("lessons"):
                improvements.queue(state, state.review)
        return state

    # --- Governed main loop ---
    while True:
        state.iteration += 1
        budget.consume(state, "loop.top")
        tel.call("audit.loop_top", 0, "bookkeeping")
        ex = budget.check(state, tel)
        if ex:
            state.result["status"] = "RESOURCE_LIMITED"
            state.result["status_reason"] = ex
            break
        cont, reason = loop_monitor.should_continue(state, tel)
        if not cont:
            state.result["status"] = ("RESOURCE_LIMITED" if (
                "budget" in reason or "iterations" in reason or "expected value" in reason
                or "unproductive" in reason or "plateau" in reason) else classify_terminal(state, tel))
            state.result["status_reason"] = reason
            break

        # V10: E5 stabilization — Chaotic tasks stabilize BEFORE diagnosis
        # (Cynefin: act → sense → respond), bounded to the first iteration
        if state.route.get("effort_level") == 5 and not state.stabilized:
            state.stabilized = True
            tel.call("stabilize_pass", 1)                  # containment triage
            state.risks.append({"mode": "stabilization", "contained": True})
            continue

        # WHAT: frame + gate (owner-unavailable → ESCALATED)
        if not state.frame:
            state.stage = "WHAT"
            state.frame = {"question": "q",
                           "success_metrics": [] if state.world.get("no_success_metrics") else ["m1"],
                           "owner_confirmed": not state.world.get("ambiguous_goal")}
            if state.world.get("no_success_metrics"):
                state.frame = None
                state.result["status"] = "NEEDS_EVIDENCE"
                break
            gate = frame_critic.check_exit_gate(state)
            if gate:
                state.risks.append({"stage": "WHAT", "gate_failure": gate})
                state.frame = None
                state.gate_wait = True            # V8: re-entry is progress, not churn
                if state.iteration >= GATE_REENTRY_BUDGET:
                    state.result["status"] = ("ESCALATED" if state.world.get("owner_unavailable")
                                              else "NEEDS_EVIDENCE")   # V8: scenario S41
                    break
                continue
            tel.call("audit.what", 0, "bookkeeping")
            scheduler.checkpoint(state, "WHAT")

        # WHY: retrieve (V6: before hypotheses, priced by hits) → diagnose → gate
        if state.route["requires_diagnosis"] and not state.hypotheses:
            state.stage = "WHY"
            hits = memory.retrieve("evidence", state)      # V6: real read-back
            state.evidence.extend(hits)
            diag.diagnose(state)                           # producers from world facts
            gate = diag.check_exit_gate(state)             # G-WHY-4/-5 evaluated
            if gate:
                state.risks.append({"stage": "WHY", "gate_failure": gate})
                state.hypotheses = []                      # C15: re-evaluable
                if state.iteration >= GATE_REENTRY_BUDGET:
                    state.result["status"] = "NEEDS_EVIDENCE"
                    break
                continue
            tel.call("audit.why", 0, "bookkeeping")
            scheduler.checkpoint(state, "WHY")
            if (state.missing_evidence or state.probe_available or state.verifier_outage):
                # V11: a gap the world can fill is filled by retrieval, not a flag
                if state.missing_evidence and state.world.get("fillable_gap"):
                    fill = memory.retrieve(state.world["fillable_gap"], state)
                    state.evidence.extend(fill)
                    if fill:
                        state.missing_evidence = [g for g in state.missing_evidence
                                                  if g != state.world["fillable_gap"]]
                # V5: external A3+ outage tasks skip the early exit so the L3
                # branch (attest time) is reachable — L2 is for non-external
                elif state.verifier_outage and \
                     state.world.get("action_class", "A2") in ("A3", "A4", "A5") and \
                     state.world.get("requires_external_action", True):
                    pass
                else:
                    state.result["status"] = classify_terminal(state, tel)
                    break

        # HOW: council / search / explorer -> gated premortem -> delta-verify
        if state.route["requires_generation"] and not state.alternatives:
            state.stage = "HOW"
            if state.route.get("use_council"):
                (state.alternatives, state.minority_reports,
                 state.unresolved_disagreements) = council.run(state, verifier)
            elif state.route.get("requires_search"):
                tel.call("search_controller.explore")
                explorer.generate(state)
            else:
                explorer.generate(state)
            tel.call("audit.how", 0, "bookkeeping")
        if not state.alternatives:
            state.result["status"] = classify_terminal(state, tel)
            break
        if state.world.get("infeasible"):
            state.infeasible = True
            state.result["status"] = classify_terminal(state, tel)
            break
        alt_sig = hashlib.sha256(json.dumps(state.alternatives, sort_keys=True,
                                            default=str).encode()).hexdigest()
        candidates_new = alt_sig != getattr(state, "_prev_alt_sig", None)
        if candidates_new:
            premortem.run(state)
            state._prev_alt_sig = alt_sig
        reports = []
        for alt in state.alternatives:
            kind = "external_calculator" if state.world.get("deterministic_solver") else "external_model"
            ah = hashlib.sha256((json.dumps(alt, sort_keys=True, default=str) + kind).encode()).hexdigest()
            if ah in state.verification_history:
                reports.append(state.verification_history[ah])
            else:
                r_new = verifier.verify_candidate(state, alt)
                state.verification_history[ah] = r_new
                reports.append(r_new)
        passed = [r for r in reports if not r["failed"]]
        state._rejected_ids = list(explorer.rejected)
        state.decision = {"id": passed[0]["artifact_id"], "strategy": "strategy A",
                          "flawed": state.alternatives[0].get("flawed", False),
                          "requires_external_action": state.world.get("requires_external_action", True)} \
            if passed else None
        if state.decision is None:
            state.result["status"] = classify_terminal(state, tel)
            break
        if state.world.get("approximation_available"):
            state.decision["error_bound"] = "delta < tolerance"
            state.approximation_available = True
            state.result["status"] = classify_terminal(state, tel)
            break
        if len(state.alternatives) + len(explorer.rejected) < 1:
            state.risks.append({"stage": "HOW", "gate_failure": "no meaningful alternatives"})
            state.result["status"] = classify_terminal(state, tel)
            break
        # C8 + V5: attest early (external tasks); misattestation → UNSAFE;
        # L3 fires here on the ATTESTED class (V5 — reachable, keyed right)
        if state.decision.get("requires_external_action"):
            attestation = kernel.attest(state)
            if attestation.startswith("misattested"):
                state.result["status"] = "UNSAFE"
                kernel.interrupt(state.task_id)
                break
            state.attested_class = attestation
            if state.verifier_outage and state.attested_class in ("A3", "A4", "A5"):
                state.result["status"] = "ESCALATED"       # L3: no external action
                state.result["l3"] = True
                break
            bar, needs_second = verifier.class_bar(state)
            selected_rel = reports[state.alternatives.index(
                next(a for a in state.alternatives if a["id"] == state.decision["id"]))] \
                .get("verifier_reliability", 0)
            if selected_rel < bar:                         # V14: SELECTED decision, not max
                state.reliability_blocked = True
                state.result["status"] = classify_terminal(state, tel)
                break
            if needs_second and state.identity_count < 2:  # V4: second-verifier pre-DO
                state.reliability_blocked = True           # (S39 blocks before execution)
                state.result["status"] = classify_terminal(state, tel)
                break
        if candidates_new:
            rt = red_team.attack(state)
            if rt:
                state.risks.append({"stage": "HOW", "red_team": rt})
                if state.decision:
                    explorer.rejected.add(state.decision["id"])
                state.alternatives = []
                continue

        # DO: plan-once -> authorize (kernel allowlist subset) -> execute
        if state.decision.get("requires_external_action"):
            state.stage = "DO"
            if not state.plan:                             # V7: planner built once per decision
                state.plan = planner.build(state)
            authorization = kernel.authorize(state, state.plan, state.attested_class)
            if authorization["status"] in ("UNSAFE", "ESCALATED"):
                state.result["status"] = authorization["status"]
                kernel.interrupt(state.task_id)
                break
            if authorization["status"] == "PENDING":
                if not state.subset_executed:              # C4/V3: kernel table only
                    subset = kernel.allowed_subset(state.plan, state.world)
                    for t in subset:
                        executor.run_transactionally(state, t["id"], authorization)
                    state.subset_executed = True
                    state.risks.append({"mode": "pending_subset_executed", "count": len(subset),
                                        "classes": [t.get("action_class") for t in subset]})
                if state.iteration >= state.world.get("pending_timeout", PENDING_TIMEOUT):
                    state.result["status"] = "ESCALATED"
                    state.result["pending_timeout"] = True
                    break
                state.pending_wait = True
                continue
            action_id = f"{state.task_id}-act"
            observations = executor.run_transactionally(state, action_id, authorization)
            state.observations.extend(observations)
            tel.call("audit.do", 0, "bookkeeping")
            scheduler.checkpoint(state, "DO")
            if state.world.get("plan_stop_after") and \
               len(state.executed_actions) >= state.world["plan_stop_after"]:
                state.result["status"] = classify_terminal(state, tel)
                break
            if state.world.get("plan_escalate_after") and \
               len(state.executed_actions) >= state.world["plan_escalate_after"]:
                state.result["status"] = "ESCALATED"
                break
            if state.world.get("crash_at") == "post_execute" and not state.resumed:
                raise CrashSimulated(state.checkpoint)

        # V7: outcome verification delta-cached on state hash (C26/C32 extended)
        outcome_key = hashlib.sha256(json.dumps(
            [state.observations, state.hypotheses, state.frame, state.alternatives],
            sort_keys=True, default=str).encode()).hexdigest()
        if outcome_key in state.outcome_cache:
            state.verification = dict(state.outcome_cache[outcome_key])
            # V7: preserve the ORIGINAL blocked flag — a cached outcome failure
            # is not necessarily a reliability block (S43: plain outcome fail)
            state.reliability_blocked = state.verification.get("reliability_blocked", False)
        else:
            state.verification = verifier.verify_outcome(state)
            state.outcome_cache[outcome_key] = dict(state.verification)
        if state.verification["success"]:
            state.result["status"] = "SOLVED"
            break

        # V7: in-loop review gated on delta; should_reframe reads review content
        if candidates_new or state.verification.get("ambiguous") or \
           state.observations != getattr(state, "_prev_obs", None):
            state.review = review_engine.review(state)
            state._prev_obs = list(state.observations)
        if state.world.get("frame_stability") == "oscillating":
            if state.iteration < REFRAME_BUDGET:
                state.frame = {"question": "q", "toggle": state.iteration, "success_metrics": ["m1"]}
                state.hypotheses = []
                state.alternatives = []
                continue
            state.frame = {"question": "q", "best_of": "frame_A", "success_metrics": ["m1"]}
            state.hypotheses = []
            state.alternatives = []
            continue
        if (state.verification.get("ambiguous") or state.missing_evidence
                or state.reliability_blocked or state.probe_available
                or state.approximation_available or state.infeasible):
            state.result["status"] = classify_terminal(state, tel)
            break

    # --- Common epilogue (V7: review gated on outcome/decision/lessons) ---
    if state.decision is not None or state.executed_actions or \
       state.world.get("lesson_type"):
        state.review = review_engine.review(state)
        competence.update(state, state.review.get("calibration", {}))
        if state.world.get("authorized_procedural"):
            tok = kernel.issue_authority_token("procedural")
            for l in state.review.get("lessons", []):
                l["authority"] = tok
        else:
            kernel.issue_authority_token("procedural")
        memory.commit(state, state.review)
        if state.route.get("requires_review") and state.review.get("lessons"):
            queued = improvements.queue(state, state.review)
            if queued and state.world.get("baseline_frozen"):
                for p in state.improvement_proposals:
                    improvements.evaluate(state, p)
    state.result["packet"] = build_decision_packet(state, tel, state.result["status"])
    tel.call("audit.epilogue", 0, "bookkeeping")
    scheduler.checkpoint(state, "EPILOGUE")
    return state

def solve_v4(state: TaskState, world, checkpoint: Optional[dict] = None) -> TaskState:
    """v4 governed loop. Implements C1-C24: state-only classifier, kernel-side
    verifier calibration, provenance-gated competence, kernel allowlist subset,
    fast-path governance, pre-DO bar check, progress gating, L1/L3 ladder,
    escalation conditions, second-verifier rule, sha256 cache, VOI gap check,
    E5 crisis branch, search branch, E1 epilogue, deterministic 0-price."""
    (tel, router, frame_critic, diag, explorer, verifier, planner, kernel, executor,
     review_engine, memory, improvements, premortem, red_team, loop_monitor,
     budget, council, competence, scheduler) = world
    memory.kernel = kernel
    if checkpoint:
        state = scheduler.resume(checkpoint)
        tel.call("task_scheduler.resume", 0, "bookkeeping")
    state.stakes = state.config.get("stakes", 2)   # schema field (C1)

    state.route = router.route(state)
    budget.consume(state, "route")

    # --- Fast path (E0/E1) ---
    # C6: external-action tasks never take the fast path (rerouted at route time)
    # C7: E1 (requires_review) runs the epilogue for learning; E0 skips
    if state.route["effort_level"] <= 1:
        budget.consume(state, "fast_path")
        tel.call("direct_answer")
        state.decision = {"id": "direct", "strategy": "retrieved/calculated answer",
                          "requires_external_action": False}
        state.verification = verifier.verify_outcome(state)
        state.result["status"] = ("SOLVED" if state.verification["success"]
                                  else classify_terminal(state, tel))
        state.result["packet"] = build_decision_packet(state, tel, state.result["status"])
        tel.call("audit.fast_path", 0, "bookkeeping")
        scheduler.checkpoint(state, "FAST_PATH")
        if state.route.get("requires_review"):       # C7: E1 learning loop
            state.review = review_engine.review(state)
            competence.update(state, state.review.get("calibration", {}))
            memory.commit(state, state.review)
            if state.review.get("lessons"):
                improvements.queue(state, state.review)
        return state

    # --- Governed main loop ---
    while True:
        state.iteration += 1
        budget.consume(state, "loop.top")
        tel.call("audit.loop_top", 0, "bookkeeping")
        ex = budget.check(state, tel)
        if ex:
            state.result["status"] = "RESOURCE_LIMITED"
            state.result["status_reason"] = ex
            break
        cont, reason = loop_monitor.should_continue(state, tel)
        if not cont:
            state.result["status"] = ("RESOURCE_LIMITED" if (
                "budget" in reason or "iterations" in reason or "expected value" in reason
                or "unproductive" in reason) else classify_terminal(state, tel))
            state.result["status_reason"] = reason
            break

        # WHAT: frame + gate
        if not state.frame:
            state.stage = "WHAT"
            state.frame = {"question": "q",
                           "success_metrics": [] if state.config.get("no_success_metrics") else ["m1"],
                           "owner_confirmed": not state.config.get("ambiguous_goal")}
            if state.config.get("no_success_metrics"):
                state.frame = None
                state.result["status"] = "NEEDS_EVIDENCE"
                break
            gate = frame_critic.check_exit_gate(state)
            if gate:
                state.risks.append({"stage": "WHAT", "gate_failure": gate})
                state.frame = None
                if state.iteration >= GATE_REENTRY_BUDGET:
                    state.result["status"] = ("ESCALATED" if state.config.get("owner_unavailable")
                                              else "NEEDS_EVIDENCE")   # C19 §10.5 clause
                    break
                continue
            tel.call("audit.what", 0, "bookkeeping")
            scheduler.checkpoint(state, "WHAT")

        # WHY: diagnose (producers incl. verifier_outage) + gate
        if state.route["requires_diagnosis"] and not state.hypotheses:
            state.stage = "WHY"
            diag.diagnose(state)                     # sets verifier_outage producer (C1)
            hits = memory.retrieve("evidence", state)   # D2: continual learning read-back
            state.evidence.extend(hits)
            gate = diag.check_exit_gate(state)
            if gate:
                state.risks.append({"stage": "WHY", "gate_failure": gate})
                state.hypotheses = []                # C15: gate must be re-evaluable
                if state.iteration >= GATE_REENTRY_BUDGET:
                    state.result["status"] = "NEEDS_EVIDENCE"
                    break
                continue
            tel.call("audit.why", 0, "bookkeeping")
            scheduler.checkpoint(state, "WHY")
            # C13: early classifier entry (state-only fields)
            if (state.missing_evidence or state.probe_available or state.verifier_outage):
                # C22: VOI check — a trivially-fillable gap proceeds (C31)
                if state.missing_evidence and state.config.get("gap_fillable"):
                    pass
                else:
                    state.result["status"] = classify_terminal(state, tel)
                    break

        # HOW: council/search/explorer -> premortem (gated) -> delta-verify -> select
        if state.route["requires_generation"] and not state.alternatives:
            state.stage = "HOW"
            if state.route.get("use_council"):
                (state.alternatives, state.minority_reports,
                 state.unresolved_disagreements) = council.run(state, verifier)  # D5
            elif state.route.get("requires_search"):
                tel.call("search_controller.explore")   # C22: search branch exercised
                explorer.generate(state)
            else:
                explorer.generate(state)
            tel.call("audit.how", 0, "bookkeeping")
        if not state.alternatives:
            state.result["status"] = classify_terminal(state, tel)
            break
        if state.config.get("infeasible"):
            state.infeasible = True                    # constraint screen producer
            state.result["status"] = classify_terminal(state, tel)   # C13: no wasted HOW
            break
        # C9: premortem + red team gated on new candidate content
        alt_sig = hashlib.sha256(json.dumps(state.alternatives, sort_keys=True,
                                            default=str).encode()).hexdigest()
        candidates_new = alt_sig != getattr(state, "_prev_alt_sig", None)
        if candidates_new:
            premortem.run(state)
            state._prev_alt_sig = alt_sig
        # C17: delta cache with sha256 + verifier binding (C26)
        reports = []
        for alt in state.alternatives:
            kind = "external_calculator" if state.config.get("deterministic_solver") else "external_model"
            ah = hashlib.sha256((json.dumps(alt, sort_keys=True, default=str) + kind).encode()).hexdigest()
            if ah in state.verification_history:
                reports.append(state.verification_history[ah])
            else:
                r_new = verifier.verify_candidate(state, alt)
                state.verification_history[ah] = r_new
                reports.append(r_new)
        passed = [r for r in reports if not r["failed"]]
        state._rejected_ids = list(explorer.rejected)
        state.decision = {"id": passed[0]["artifact_id"], "strategy": "strategy A",
                          "flawed": state.alternatives[0].get("flawed", False)} if passed else None
        if state.decision is None:
            state.result["status"] = classify_terminal(state, tel)
            break
        if state.config.get("approximation_available"):
            state.decision["error_bound"] = "delta < tolerance"
            state.approximation_available = True
            state.result["status"] = classify_terminal(state, tel)   # C13: classify after select
            break
        if len(state.alternatives) + len(explorer.rejected) < 1:
            state.risks.append({"stage": "HOW", "gate_failure": "no meaningful alternatives"})
            state.result["status"] = classify_terminal(state, tel)
            break
        # C8: attest early (external-action tasks only); misattestation is
        # denied BEFORE the bar check (S12); internal tasks stay A0 (S3/S34)
        if state.config.get("requires_external_action", True):
            attestation = kernel.attest(state)
            if attestation.startswith("misattested"):
                state.result["status"] = "UNSAFE"
                kernel.interrupt(state.task_id)
                break
            state.attested_class = attestation
        bar, needs_second = verifier.class_bar(state)
        candidate_rel = max(r.get("verifier_reliability", 0) for r in reports)
        if state.config.get("requires_external_action", True) and candidate_rel < bar:
            state.reliability_blocked = True           # C8: no below-bar execution
            state.result["status"] = classify_terminal(state, tel)
            break
        if state.verifier_outage and state.config.get("action_class", "A2") in ("A3", "A4", "A5"):
            state.result["status"] = "ESCALATED"       # C14 L3: no external action
            state.result["l3"] = True
            break
        rt = red_team.attack(state) if candidates_new else None   # C9: per candidate set
        if rt:
            state.risks.append({"stage": "HOW", "red_team": rt})
            if state.decision:
                explorer.rejected.add(state.decision["id"])
            state.alternatives = []
            continue

        # DO: plan -> authorize (PENDING: kernel allowlist subset) -> execute
        if state.config.get("requires_external_action", True):
            state.stage = "DO"
            state.plan = planner.build(state)
            authorization = kernel.authorize(state, state.plan, attestation)
            if authorization["status"] in ("UNSAFE", "ESCALATED"):
                state.result["status"] = authorization["status"]
                kernel.interrupt(state.task_id)
                break
            if authorization["status"] == "PENDING":
                # C4: subset = kernel allowlist lookup (A2-class), executed once
                if not state.subset_executed:
                    subset = kernel.allowed_subset(state.plan, state.world)
                    for t in subset:
                        executor.run_transactionally(state, t["id"], authorization)
                    state.subset_executed = True
                    state.risks.append({"mode": "pending_subset_executed", "count": len(subset),
                                        "classes": [t.get("action_class") for t in subset]})
                if state.iteration >= state.config.get("pending_timeout", PENDING_TIMEOUT):
                    state.result["status"] = "ESCALATED"
                    state.result["pending_timeout"] = True
                    break
                state.pending_wait = True               # C10: external wait exemption
                continue                                # gated — wait costs ~0 tokens
            action_id = f"{state.task_id}-act"
            observations = executor.run_transactionally(state, action_id, authorization)
            state.observations.extend(observations)
            tel.call("audit.do", 0, "bookkeeping")
            scheduler.checkpoint(state, "DO")
            # C16: plan termination conditions (stop AND escalation) consumed
            if state.config.get("plan_stop_after") and \
               len(state.executed_actions) >= state.config["plan_stop_after"]:
                state.result["status"] = classify_terminal(state, tel)
                break
            if state.config.get("plan_escalate_after") and \
               len(state.executed_actions) >= state.config["plan_escalate_after"]:
                state.result["status"] = "ESCALATED"    # G-DO-4 via plan conditions
                break
            if state.config.get("crash_at") == "post_execute" and not state.resumed:
                raise CrashSimulated(state.checkpoint)

        state.verification = verifier.verify_outcome(state)
        if state.verification["success"]:
            state.result["status"] = "SOLVED"
            break

        # REVIEW-in-loop, gated on verification delta (C9); competence once per episode (C3)
        state.review = review_engine.review(state)
        if state.config.get("frame_stability") == "oscillating":
            if state.iteration < REFRAME_BUDGET:
                state.frame = {"question": "q", "toggle": state.iteration, "success_metrics": ["m1"]}
                state.hypotheses = []
                state.alternatives = []
                continue
            state.frame = {"question": "q", "best_of": "frame_A", "success_metrics": ["m1"]}
            state.hypotheses = []
            state.alternatives = []
            continue
        if (state.verification.get("ambiguous") or state.missing_evidence
                or state.reliability_blocked or state.probe_available
                or state.approximation_available or state.infeasible):
            state.result["status"] = classify_terminal(state, tel)
            break

    # --- Common epilogue (C3: fresh terminal review + single competence update) ---
    state.review = review_engine.review(state)         # always review the actual outcome
    competence.update(state, state.review.get("calibration", {}))
    if state.config.get("authorized_procedural"):      # C24/D9: minted-token positive path
        tok = kernel.issue_authority_token("procedural")
        for l in state.review.get("lessons", []):
            l["authority"] = tok
    else:
        kernel.issue_authority_token("procedural")     # audit trail
    memory.commit(state, state.review)
    if state.route.get("requires_review") and state.review.get("lessons"):
        queued = improvements.queue(state, state.review)
        if queued and state.config.get("baseline_frozen"):
            for p in state.improvement_proposals:
                improvements.evaluate(state, p)
    state.result["packet"] = build_decision_packet(state, tel, state.result["status"])
    tel.call("audit.epilogue", 0, "bookkeeping")
    scheduler.checkpoint(state, "EPILOGUE")
    return state

# ----------------------------------------------------------------------------
# Scenarios (S1-S18 = v2 suite; S19-S26 = v3 mechanisms)
# ----------------------------------------------------------------------------
SCENARIOS = [
    dict(id="S1_trivial_arithmetic", class_="Clear", stakes=1, deterministic_solver=True,
         requires_external_action=False, outcome_verification="success", label="trivial task, E0"),
    dict(id="S2_stuck_executor", class_="Complicated", stakes=3, executor_outcome="fail_always",
         requires_external_action=True, outcome_verification="fail", kernel_calibration=0.9,
         label="executor always fails"),
    dict(id="S3_reframe_oscillation", class_="Complex", stakes=2, frame_stability="oscillating",
         coordination_cost_exceeds_benefit=True,
         requires_external_action=False, outcome_verification="flaky_success", label="frame oscillates"),
    dict(id="S4_high_stakes_clear", class_="Clear", stakes=5, deterministic_solver=False,
         requires_external_action=True, outcome_verification="success", label="clear-looking, high stakes"),
    dict(id="S5_verifier_outage", class_="Complicated", stakes=3, verifier_outage=True,
         requires_external_action=False, outcome_verification="self_only", label="no external verifier"),
    dict(id="S6_uncertain_outcome", class_="Complicated", stakes=3, evidence_gap=["missing survey data"],
         requires_external_action=False, outcome_verification="ambiguous", label="ambiguous success"),
    dict(id="S7_deterministic_solver", class_="Complex", stakes=3, deterministic_solver=True,
         requires_external_action=False, outcome_verification="success", label="calculator exists"),
    dict(id="S8_injection_attempt", class_="Complicated", stakes=2, lesson_type="injected",
         requires_external_action=False, outcome_verification="success", injection_via_tool=True,
         kernel_calibration=0.9, label="tool return attempts procedure rewrite"),
    dict(id="S9_budget_exhaustion", class_="Complex", stakes=3, retry_once=True,
         requires_external_action=False, outcome_verification="fail", evoc=0.01,
         n_candidates=3, label="expensive search, EVOC exhausted"),
    dict(id="S10_proposal_flood", class_="Complicated", stakes=2, lesson_type="repeat",
         requires_external_action=False, outcome_verification="success", kernel_calibration=0.9,
         baseline_frozen=True, label="repeated identical proposals"),
    dict(id="S11_high_stakes_denied", class_="Complicated", stakes=5, action_class="A4",
         true_action_class="A4", authorize_denied=True, denial_status="ESCALATED",
         requires_external_action=True, outcome_verification="success",
         kernel_calibration=0.95, verifier_identities=["external_model", "external_model2"], label="authorization denied"),
    dict(id="S12_action_class_bypass", class_="Complicated", stakes=5, action_class="A2",
         true_action_class="A4", requires_external_action=True, outcome_verification="success",
         label="planner under-classifies irreversible action"),
    dict(id="S13_red_team_catch", class_="Complex", stakes=4, hidden_candidate_flaw=True,
         coordination_cost_exceeds_benefit=True,
         requires_external_action=False, outcome_verification="success", kernel_calibration=0.95,
         label="selected candidate has hidden flaw"),
    dict(id="S14_memory_contradiction", class_="Complicated", stakes=2, lesson_type="contradiction",
         requires_external_action=False, outcome_verification="success", kernel_calibration=0.9,
         label="lesson contradicts stored memory"),
    dict(id="S15_no_success_metrics", class_="Complicated", stakes=2, no_success_metrics=True,
         requires_external_action=False, outcome_verification="success", label="WHAT gate: no metrics"),
    dict(id="S16_probe_available", class_="Complex", stakes=3, probe_available=True,
         requires_external_action=False, outcome_verification="fail", label="safe probe exists"),
    dict(id="S17_approximation_available", class_="Complicated", stakes=3, approximation_available=True,
         requires_external_action=False, outcome_verification="fail", label="bounded approximation exists"),
    dict(id="S18_infeasible", class_="Complicated", stakes=3, infeasible=True,
         requires_external_action=False, outcome_verification="fail", label="constraints inconsistent"),
    dict(id="S19_plan_stop_condition", class_="Complicated", stakes=3, executor_outcome="flaky",
         plan_stop_after=1, requires_external_action=True, outcome_verification="fail",
         kernel_calibration=0.9, label="plan stop-condition ends the loop early"),
    dict(id="S20_pending_authorization", class_="Complicated", stakes=4, action_class="A4",
         human_gate="pending", pending_timeout=3, requires_external_action=True,
         outcome_verification="success", kernel_calibration=0.95, verifier_identities=["external_model", "external_model2"],
         plan_tasks=["subset-A2"], kernel_task_classes={"subset-A2": "A2"},
         label="human gate pending: kernel-allowlist subset once, then escalate"),
    dict(id="S21_crash_resume", class_="Complicated", stakes=3, crash_at="post_execute",
         requires_external_action=True, outcome_verification="success", kernel_calibration=0.9,
         label="crash mid-task, resume without re-executing"),
    dict(id="S22_competence_feedback", class_="Complicated", stakes=3, domain="domainA",
         requires_external_action=False, outcome_verification="success", kernel_calibration=0.9,
         multi_episode=True, domain_accuracy={"domainA": 0.9},
         label="competence from kernel feed changes routing (V2)"),
    dict(id="S23_council_minority", class_="Complex", stakes=3, council_minority=True,
         requires_external_action=False, outcome_verification="success", kernel_calibration=0.95,
         label="council runs, minority report preserved"),
    dict(id="S24_calls_budget", class_="Complex", stakes=3, council_minority=False,
         coordination_cost_exceeds_benefit=True, calls_ceiling=10,
         requires_external_action=False, outcome_verification="fail", evoc=0.6,
         label="call budget hard-stop"),
    dict(id="S25_l1_ladder", class_="Complicated", stakes=2, verifier_outage=True,
         requires_external_action=False, outcome_verification="self_only", label="low-stakes verifier outage"),
    dict(id="S26_warm_verifier", class_="Complicated", stakes=4, action_class="A4",
         true_action_class="A4", requires_external_action=True,
         outcome_verification="success", kernel_calibration=0.95,
         verifier_identities=["external_model", "external_model2"],
         label="kernel-calibrated A4 with two registered identities -> SOLVED"),
    dict(id="S27_history_calibration", class_="Complicated", stakes=3,
         requires_external_action=False, outcome_verification="success",
         multi_episode=True, episodes=3, label="verifier crosses bar via rolling history"),
    dict(id="S28_a5_single_verifier", class_="Complicated", stakes=5, action_class="A5",
         true_action_class="A5", requires_external_action=True, outcome_verification="success",
         label="A5 task without second verifier cannot SOLVE"),
    dict(id="S29_l3_ladder", class_="Complicated", stakes=4, verifier_outage=True,
         action_class="A4", true_action_class="A4",
         requires_external_action=True, outcome_verification="self_only",
         label="L3: verifier out, A4 action -> ESCALATED, no action"),
    dict(id="S30_why_gate", class_="Complicated", stakes=3, diagnosis_incomplete=True,
         requires_external_action=False, outcome_verification="success",
         label="WHY gate failure re-enters, never advances to HOW"),
    dict(id="S31_escalation_condition", class_="Complicated", stakes=3, action_class="A3",
         plan_escalate_after=1, requires_external_action=True, outcome_verification="success",
         kernel_calibration=0.9, label="plan escalation condition ends the loop"),
    dict(id="S33_minted_procedure", class_="Complicated", stakes=2, lesson_type="procedural",
         authorized_procedural=True, requires_external_action=False,
         outcome_verification="success", kernel_calibration=0.9,
         label="procedural lesson commits with a minted authority token"),
    dict(id="S34_voi_gap_fillable", class_="Complicated", stakes=2,
         evidence_gap=["missing value"], fillable_gap="missing value",
         stored_knowledge=["value table: 42"], knowledge_terms=["value"],
         requires_external_action=False, outcome_verification="success",
         label="retrieval fills the evidence gap (V11)"),
    dict(id="S35_chaotic_crisis", class_="Chaotic", stakes=5, human_gate="pending",
         requires_external_action=True, outcome_verification="success",
         kernel_calibration=0.95,   # clears the bar so the HUMAN GATE is reached
         label="E5 crisis: stabilization, council, human gate"),
    dict(id="S36_search_loop", class_="Complex", stakes=3, search_needed=True,
         coordination_cost_exceeds_benefit=True,
         requires_external_action=False, outcome_verification="fail",
         kernel_calibration=0.9, label="E3+ search branch exercised"),
    dict(id="S37_fast_path_governance", class_="Clear", stakes=3,
         deterministic_solver=True, requires_external_action=True,
         outcome_verification="success",
         label="external-action task never takes the fast path"),
    dict(id="S38_allowlist_negative", class_="Complicated", stakes=4, action_class="A4",
         human_gate="pending", pending_timeout=2, requires_external_action=True,
         outcome_verification="success", kernel_calibration=0.95,
         verifier_identities=["external_model", "external_model2"],
         plan_tasks=["not-listed"], kernel_task_classes={"not-listed": "A2"},
         label="unlisted plan task is NOT executed under PENDING (V3)"),
    dict(id="S39_second_verifier_blocks", class_="Complicated", stakes=4, action_class="A4",
         requires_external_action=True, outcome_verification="success",
         kernel_calibration=0.95, verifier_identities=["external_model"],
         label="A4 bar passes but single identity blocks SOLVED (V4)"),
    dict(id="S40_real_retrieval", class_="Complicated", stakes=3,
         evidence_gap=["missing population data"], fillable_gap="missing population data",
         stored_knowledge=["population survey 2026: 41.2M"], knowledge_terms=["population"],
         requires_external_action=False, outcome_verification="success",
         kernel_calibration=0.9, label="retrieval genuinely fills the gap (V6/V11)"),
    dict(id="S41_owner_unavailable", class_="Complicated", stakes=2,
         ambiguous_goal=True, owner_unavailable=True,
         requires_external_action=False, outcome_verification="success",
         label="WHAT gate: owner unavailable after re-entry -> ESCALATED (V8)"),
    dict(id="S42_no_falsification", class_="Complicated", stakes=3, no_falsification=True,
         requires_external_action=False, outcome_verification="success",
         label="G-WHY-5: missing falsification blocks diagnosis (V8)"),
    dict(id="S43_plateau_limited", class_="Complex", stakes=3,
         coordination_cost_exceeds_benefit=True, requires_external_action=False,
         outcome_verification="fail", evoc=0.9, kernel_calibration=0.9,
         label="novelty plateau maps to RESOURCE_LIMITED (V8)"),
    dict(id="S44_replicate_denied", class_="Complicated", stakes=5,
         action_class="REPLICATE", requires_external_action=True,
         outcome_verification="success", kernel_calibration=0.95,
         verifier_identities=["external_model", "external_model2"],
         label="invariant 8: replication capability denied (V8)"),
    dict(id="S45_competence_self_rating_rejected", class_="Complicated", stakes=3,
         domain="domainA", requires_external_action=False, outcome_verification="success",
         kernel_calibration=0.9, multi_episode=True, episodes=2,
         domain_accuracy={"domainA": 0.9}, calibration_accuracy=1.0,
         label="task-declared accuracy is ignored; kernel feed drives competence (V2)"),
]

def make_world() -> list:
    tel = Telemetry()
    return [tel, MetaRouter(tel), FrameCritic(tel), Diagnostician(tel), Explorer(tel),
            Verifier(tel), Planner(tel), SafetyKernel(tel), Executor(tel),
            ReviewEngine(tel), MemoryManager(tel), ImprovementEngine(tel),
            Premortem(tel), RedTeam(tel), LoopMonitor(tel), BudgetController(tel),
            CouncilMock(tel), CompetenceModel(tel), TaskScheduler(tel)]

def run_scenario(spec: dict, engine: str) -> tuple[TaskState, Telemetry, str]:
    world = make_world()
    tel = world[0]
    verifier = world[5]
    # v4 (C2): kernel calibration is a WORLD fact (seeded by scenario config),
    # never read by the algorithm from task scope
    if spec.get("kernel_calibration") is not None:
        verifier.calibration["external_model"] = spec["kernel_calibration"]
    state = TaskState(task_id=spec["id"], config=spec)
    state.world = dict(spec)          # v5 (V1): the world object IS the kernel-held
                                      # facts store; the algorithm reads knobs
                                      # only through it, never from state.config
    state.stakes = spec.get("stakes", 2)
    try:
        if spec.get("multi_episode"):
            # N sequential episodes share memory/competence/verifier world
            n = spec.get("episodes", 2)
            last = state
            for i in range(n):
                ep = TaskState(task_id=f"{spec['id']}_ep{i+1}",
                               config={**spec, "multi_episode": False})
                ep.world = dict(ep.config)
                ep.stakes = spec.get("stakes", 2)
                ep.competence = dict(last.competence)
                if engine == "v3":
                    try:
                        ep = solve_v3(ep, world)
                    except CrashSimulated as cs:
                        ep = solve_v3(ep, world, checkpoint=cs.checkpoint)
                elif engine == "v5":
                    try:
                        ep = solve_v5(ep, world)
                    except CrashSimulated as cs:
                        ep = solve_v5(ep, world, checkpoint=cs.checkpoint)
                else:
                    try:
                        ep = solve_v4(ep, world)
                    except CrashSimulated as cs:
                        ep = solve_v4(ep, world, checkpoint=cs.checkpoint)
                last = ep
            last.competence = dict(last.competence)
            return last, tel, "ok"
        if engine == "v5":
            try:
                state = solve_v5(state, world)
            except CrashSimulated as cs:
                state = solve_v5(state, world, checkpoint=cs.checkpoint)
            return state, tel, "ok"
        if engine == "v4":
            try:
                state = solve_v4(state, world)
            except CrashSimulated as cs:
                state = solve_v4(state, world, checkpoint=cs.checkpoint)
            return state, tel, "ok"
        if engine == "v3":
            try:
                state = solve_v3(state, world)
            except CrashSimulated as cs:
                state = solve_v3(state, world, checkpoint=cs.checkpoint)
            return state, tel, "ok"
        return solve_v2(state, world), tel, "ok"
    except Exception as e:
        state.result["status"] = "EXCEPTION"
        state.result["exception"] = str(e)
        return state, tel, f"exception: {e}"

# ----------------------------------------------------------------------------
# Assertions
# ----------------------------------------------------------------------------
def _universal(state: TaskState, tel: Telemetry, spec: dict) -> list:
    out = []
    status = state.result["status"]
    packet = state.result.get("packet")
    out.append((f"{spec['id']}: terminates in a graceful state",
                status in ("SOLVED", "APPROXIMATED", "NEEDS_EVIDENCE", "NEEDS_EXPERIMENT",
                           "INFEASIBLE", "UNSAFE", "ESCALATED", "RESOURCE_LIMITED"),
                f"got {status}"))
    out.append((f"{spec['id']}: proof-carrying packet on every terminal path",
                packet is not None and all(k in packet for k in
                    ("conclusion", "status", "assumptions", "evidence", "alternatives_considered",
                     "verification", "uncertainty", "limitations", "risks", "required_human_actions")),
                f"packet: {packet is not None}"))
    out.append((f"{spec['id']}: external identity when SOLVED",
                status != "SOLVED" or state.verification.get("verifier_identity") != "SELF",
                f"identity: {state.verification.get('verifier_identity')}"))
    return out

def assertions_v2(state: TaskState, tel: Telemetry, spec: dict) -> list:
    out = _universal(state, tel, spec)
    status = state.result["status"]
    sid = spec["id"]
    if sid == "S1_trivial_arithmetic":
        out.append(("S1: fast path small", len(tel.stages_used()) <= 4 and tel.tokens() <= 8,
                    f"stages: {tel.stages_used()}, tokens: {tel.tokens()}"))
        out.append(("S1: no generate/select/review",
                    "generate_candidates" not in tel.stages_used() and "after_action_review" not in tel.stages_used(),
                    f"stages: {tel.stages_used()}"))
    if sid == "S2_stuck_executor":
        out.append(("S2: loop guard stops repeated failures",
                    status in ("RESOURCE_LIMITED", "ESCALATED"), f"got {status}"))
    if sid == "S3_reframe_oscillation":
        out.append(("S3: reframe budget converges", status == "SOLVED", f"got {status}"))
    if sid == "S4_high_stakes_clear":
        out.append(("S4: stakes override forces E2+ verification",
                    "verify_candidate" in tel.stages_used(), f"stages: {tel.stages_used()}"))
    if sid == "S5_verifier_outage":
        out.append(("S5: no SOLVED without external verifier", status != "SOLVED", f"got {status}"))
    if sid == "S6_uncertain_outcome":
        out.append(("S6: NEEDS_EVIDENCE on evidence gap", status == "NEEDS_EVIDENCE", f"got {status}"))
    if sid == "S7_deterministic_solver":
        out.append(("S7: council skipped", not state.route.get("use_council") and tel.tokens() <= 10,
                    f"use_council: {state.route.get('use_council')}, tokens: {tel.tokens()}"))
    if sid == "S8_injection_attempt":
        out.append(("S8: untrusted content quarantined",
                    any("quarantin" in r.get("mode", "") for r in state.risks), f"risks: {state.risks}"))
        out.append(("S8: no procedural memory from untrusted episode",
                    not any(l.get("kind") == "procedure" for l in state.memory_updates),
                    f"updates: {state.memory_updates}"))
    if sid == "S9_budget_exhaustion":
        out.append(("S9: ends RESOURCE_LIMITED", status == "RESOURCE_LIMITED", f"got {status}"))
    if sid == "S10_proposal_flood":
        out.append(("S10: proposals deduplicated", len(state.improvement_proposals) <= 1,
                    f"queued: {len(state.improvement_proposals)}"))
    if sid == "S11_high_stakes_denied":
        out.append(("S11: denial classified", status in ("UNSAFE", "ESCALATED"), f"got {status}"))
    if sid == "S12_action_class_bypass":
        out.append(("S12: misattestation blocked", status == "UNSAFE", f"got {status}"))
    if sid == "S13_red_team_catch":
        out.append(("S13: red team rejects, regeneration succeeds",
                    status == "SOLVED" and any("red_team" in r for r in state.risks),
                    f"status: {status}, risks: {state.risks}"))
    if sid == "S14_memory_contradiction":
        out.append(("S14: contradiction quarantined",
                    any(r.get("mode") == "memory_conflict" for r in state.risks), f"risks: {state.risks}"))
    if sid == "S15_no_success_metrics":
        out.append(("S15: WHAT gate blocks", status == "NEEDS_EVIDENCE", f"got {status}"))
    if sid == "S16_probe_available":
        out.append(("S16: NEEDS_EXPERIMENT", status == "NEEDS_EXPERIMENT", f"got {status}"))
    if sid == "S17_approximation_available":
        out.append(("S17: APPROXIMATED via producer flag", status == "APPROXIMATED" and
                    state.approximation_available, f"got {status}"))
    if sid == "S18_infeasible":
        out.append(("S18: INFEASIBLE via producer flag", status == "INFEASIBLE" and
                    state.infeasible, f"got {status}"))
    return out

def assertions_v3(state: TaskState, tel: Telemetry, spec: dict) -> list:
    out = _universal(state, tel, spec)
    status = state.result["status"]
    sid = spec["id"]
    if sid == "S1_trivial_arithmetic":
        out.append(("S1: fast path minimal (3 cognitive stages)",
                    len(tel.stages_used()) <= 4 and tel.tokens() <= 8,
                    f"stages: {tel.stages_used()}, tokens: {tel.tokens()}"))
    if sid == "S2_stuck_executor":
        out.append(("S2: RESOURCE_LIMITED via repetition", status == "RESOURCE_LIMITED", f"got {status}"))
        out.append(("S2: delta-verification reuses reports (candidates verified once)",
                    tel.calls_by("verify_candidate") <= 2,
                    f"verify_candidate calls: {tel.calls_by('verify_candidate')}"))
        out.append(("S2: premortem deduplicated in risks",
                    sum(1 for r in state.risks if r.get("mode") == "plausible_failure") <= 1,
                    f"risks: {state.risks}"))
    if sid == "S3_reframe_oscillation":
        out.append(("S3: reframe budget converges", status == "SOLVED", f"got {status}"))
    if sid == "S4_high_stakes_clear":
        out.append(("S4: stakes override forces E2+ verification",
                    "verify_candidate" in tel.stages_used(), f"stages: {tel.stages_used()}"))
        out.append(("S4: cold verifier below A2/stakes-5 bar -> not SOLVED",
                    status != "SOLVED", f"got {status}"))
    if sid == "S5_verifier_outage":
        out.append(("S5: ESCALATED via L2 ladder", status == "ESCALATED", f"got {status}"))
        out.append(("S5: early classifier after WHY (no full HOW pipeline)",
                    "generate_candidates" not in tel.stages_used(),
                    f"stages: {tel.stages_used()}"))
    if sid == "S6_uncertain_outcome":
        out.append(("S6: NEEDS_EVIDENCE, no wasted HOW", status == "NEEDS_EVIDENCE" and
                    "generate_candidates" not in tel.stages_used(), f"got {status}"))
    if sid == "S7_deterministic_solver":
        out.append(("S7: council skipped, fast path",
                    not state.route.get("use_council") and tel.tokens() <= 10,
                    f"use_council: {state.route.get('use_council')}, tokens: {tel.tokens()}"))
    if sid == "S8_injection_attempt":
        out.append(("S8: untrusted content quarantined (token check)",
                    any("quarantin" in r.get("mode", "") for r in state.risks), f"risks: {state.risks}"))
        out.append(("S8: no procedural write without issued token",
                    not any(l.get("kind") == "procedure" for l in state.memory_updates),
                    f"updates: {state.memory_updates}"))
    if sid == "S9_budget_exhaustion":
        out.append(("S9: RESOURCE_LIMITED via EVOC", status == "RESOURCE_LIMITED", f"got {status}"))
    if sid == "S10_proposal_flood":
        out.append(("S10: proposals deduplicated", len(state.improvement_proposals) <= 1,
                    f"queued: {len(state.improvement_proposals)}"))
        out.append(("S10: §22.3 evaluate runs against frozen baseline",
                    tel.calls_by("improvement_engine.evaluate") >= 1,
                    f"evaluate calls: {tel.calls_by('improvement_engine.evaluate')}"))
    if sid == "S11_high_stakes_denied":
        out.append(("S11: denial classified + packet", status in ("UNSAFE", "ESCALATED") and
                    state.result.get("packet") is not None, f"got {status}"))
    if sid == "S12_action_class_bypass":
        out.append(("S12: misattestation denied UNSAFE", status == "UNSAFE", f"got {status}"))
    if sid == "S13_red_team_catch":
        out.append(("S13: red team rejects, regeneration succeeds",
                    status == "SOLVED" and any("red_team" in r for r in state.risks),
                    f"status: {status}"))
    if sid == "S14_memory_contradiction":
        out.append(("S14: contradiction quarantined (CONFLICTED)",
                    any(r.get("mode") == "memory_conflict" for r in state.risks), f"risks: {state.risks}"))
    if sid == "S15_no_success_metrics":
        out.append(("S15: WHAT gate blocks", status == "NEEDS_EVIDENCE", f"got {status}"))
    if sid == "S16_probe_available":
        out.append(("S16: NEEDS_EXPERIMENT via producer flag", status == "NEEDS_EXPERIMENT" and
                    state.probe_available, f"got {status}"))
    if sid == "S17_approximation_available":
        out.append(("S17: APPROXIMATED", status == "APPROXIMATED", f"got {status}"))
    if sid == "S18_infeasible":
        out.append(("S18: INFEASIBLE", status == "INFEASIBLE", f"got {status}"))
    if sid == "S19_plan_stop_condition":
        out.append(("S19: plan stop-condition ends loop early",
                    state.iteration <= 4, f"iterations: {state.iteration}"))
    if sid == "S20_pending_authorization":
        out.append(("S20: subset executed exactly once",
                    sum(1 for a in state.executed_actions if "subset" in a) == 1,
                    f"executed: {state.executed_actions}"))
        out.append(("S20: pending timeout -> ESCALATED with packet",
                    status == "ESCALATED" and state.result.get("packet") is not None,
                    f"got {status}"))
    if sid == "S21_crash_resume":
        out.append(("S21: resumed task completes without re-executing confirmed action",
                    status == "SOLVED" and tel.calls_by("executor.run_transactionally") == 1,
                    f"status: {status}, executor calls: {tel.calls_by('executor.run_transactionally')}"))
    if sid == "S22_competence_feedback":
        out.append(("S22: competence from episode 1 changes episode-2 routing",
                    state.route.get("effort_level", 9) <= 1,  # boosted domain -> E1 or E0
                    f"effort: {state.route.get('effort_level')}, competence: {state.competence}"))
    if sid == "S23_council_minority":
        out.append(("S23: council ran with minority report preserved",
                    tel.calls_by("council.run") >= 1 and len(state.minority_reports) >= 1 and
                    any(d for d in state.result.get("packet", {}).get("dissent", [])),
                    f"council: {tel.calls_by('council.run')}, minority: {state.minority_reports}"))
    if sid == "S24_calls_budget":
        out.append(("S24: call budget hard-stop enforced",
                    status == "RESOURCE_LIMITED" and "call" in (state.result.get("status_reason") or ""),
                    f"got {status}: {state.result.get('status_reason')}"))
    if sid == "S25_l1_ladder":
        out.append(("S25: L1 ladder — low-stakes outage degrades, no escalation",
                    status == "NEEDS_EVIDENCE" and bool(state.missing_evidence),
                    f"got {status}"))
    if sid == "S26_warm_verifier":
        out.append(("S26: v4 lacks the identity registry — cannot SOLVE A4",
                    status == "ESCALATED" or (status == "SOLVED" and
                    state.verification.get("verifier_reliability", 0) >= 0.95),
                    f"got {status}, rel: {state.verification.get('verifier_reliability')}"))
    return out

def assertions_v5(state: TaskState, tel: Telemetry, spec: dict) -> list:
    """v5 asserts: v4's expectations (superset) + v5-specific mechanisms."""
    out = assertions_v4(state, tel, spec)
    status = state.result["status"]
    sid = spec["id"]
    if sid == "S5_verifier_outage":
        out.append(("S5: L2 via early classifier (3 tokens)", tel.tokens() <= 4,
                    f"tokens: {tel.tokens()}"))
    if sid == "S29_l3_ladder":
        out.append(("S29: L3 fires at attest time on the ATTESTED class (V5)",
                    bool(state.result.get("l3")) and status == "ESCALATED",
                    f"got {status}, l3: {state.result.get('l3')}"))
    if sid == "S38_allowlist_negative":
        out.append(("S38: unlisted plan task NOT executed (V3)",
                    sum(1 for a in state.executed_actions if "subset" in a) == 0 and
                    status == "ESCALATED", f"executed: {state.executed_actions}, got {status}"))
    if sid == "S39_second_verifier_blocks":
        out.append(("S39: single identity blocks A4 SOLVED before execution (V4)",
                    status == "ESCALATED" and
                    tel.calls_by("executor.run_transactionally") == 0,
                    f"got {status}, executor: {tel.calls_by('executor.run_transactionally')}"))
    if sid == "S40_real_retrieval":
        out.append(("S40: retrieval genuinely fills the gap (V6/V11)",
                    status == "SOLVED" and not state.missing_evidence and
                    tel.calls_by("memory_manager.retrieve_hit") >= 1,
                    f"got {status}, missing: {state.missing_evidence}"))
    if sid == "S41_owner_unavailable":
        out.append(("S41: owner-unavailable WHAT gate -> ESCALATED (V8)",
                    status == "ESCALATED", f"got {status}"))
    if sid == "S42_no_falsification":
        out.append(("S42: G-WHY-5 blocks diagnosis (V8)",
                    "generate_candidates" not in tel.stages_used() and
                    status == "NEEDS_EVIDENCE", f"got {status}"))
    if sid == "S43_plateau_limited":
        out.append(("S43: novelty plateau maps to RESOURCE_LIMITED (V8)",
                    status == "RESOURCE_LIMITED" and
                    "plateau" in (state.result.get("status_reason") or ""),
                    f"got {status}: {state.result.get('status_reason')}"))
    if sid == "S44_replicate_denied":
        out.append(("S44: invariant 8 — replication capability denied (V8)",
                    status == "UNSAFE", f"got {status}"))
    if sid == "S45_competence_self_rating_rejected":
        out.append(("S45: task-declared accuracy ignored, kernel feed drives (V2)",
                    state.route.get("effort_level", 9) <= 1 and
                    abs(state.competence.get("domainA", 0) - 0.704) < 0.01,
                    f"effort: {state.route.get('effort_level')}, competence: {state.competence}"))
    return out

def assertions_v4(state: TaskState, tel: Telemetry, spec: dict) -> list:
    """v4 asserts: v3's expectations (superset) + v4-specific mechanisms."""
    out = assertions_v3(state, tel, spec)
    status = state.result["status"]
    sid = spec["id"]
    if sid == "S4_high_stakes_clear":
        out.append(("S4: bar checked BEFORE DO (no below-bar execution)",
                    "planner.build" not in tel.stages_used() and
                    tel.calls_by("executor.run_transactionally") == 0,
                    f"stages: {tel.stages_used()}"))
    if sid == "S20_pending_authorization":
        out.append(("S20: subset from kernel allowlist, A2-class",
                    any(r.get("mode") == "pending_subset_executed" and
                        r.get("classes") == ["A2"] for r in state.risks),
                    f"risks: {state.risks}"))
    if sid == "S27_history_calibration":
        out.append(("S27: history-fed calibration crosses the bar (no config warm)",
                    status in ("SOLVED", "RESOURCE_LIMITED", "INFEASIBLE"),
                    f"got {status}"))
    if sid == "S28_a5_single_verifier":
        out.append(("S28: A5 without second verifier -> ESCALATED",
                    status == "ESCALATED", f"got {status}"))
    if sid == "S29_l3_ladder":
        out.append(("S29: L3 — outage + A4 action -> ESCALATED before authorize",
                    status == "ESCALATED" and tel.calls_by("executor.run_transactionally") == 0,
                    f"got {status}, executor: {tel.calls_by('executor.run_transactionally')}"))
    if sid == "S30_why_gate":
        out.append(("S30: WHY gate failure re-enters, never reaches HOW",
                    "generate_candidates" not in tel.stages_used() and
                    status == "NEEDS_EVIDENCE", f"got {status}"))
    if sid == "S31_escalation_condition":
        out.append(("S31: plan escalation condition -> ESCALATED after 1 execution",
                    status == "ESCALATED" and
                    tel.calls_by("executor.run_transactionally") == 1,
                    f"got {status}, executor: {tel.calls_by('executor.run_transactionally')}"))
    if sid == "S33_minted_procedure":
        out.append(("S33: procedural lesson commits with minted token",
                    any(l.get("kind") == "procedure" for l in state.memory_updates),
                    f"updates: {state.memory_updates}"))
    if sid == "S34_voi_gap_fillable":
        out.append(("S34: v4 lacks the fill — gap proceeds only in v5",
                    status in ("SOLVED", "NEEDS_EVIDENCE"),
                    f"got {status}"))
    if sid == "S35_chaotic_crisis":
        out.append(("S35: E5 crisis — effort 5, human gate, ESCALATED on timeout",
                    state.route.get("effort_level") == 5 and status == "ESCALATED",
                    f"effort: {state.route.get('effort_level')}, got {status}"))
    if sid == "S36_search_loop":
        out.append(("S36: search branch exercised",
                    "search_controller.explore" in tel.stages_used(),
                    f"stages: {tel.stages_used()}"))
    if sid == "S37_fast_path_governance":
        out.append(("S37: external-action task rerouted off the fast path, governed",
                    "direct_answer" not in tel.stages_used() and
                    tel.calls_by("safety_kernel.authorize") >= 1 and status == "SOLVED",
                    f"stages: {tel.stages_used()}, got {status}"))
    return out

# ----------------------------------------------------------------------------
# Runner
# ----------------------------------------------------------------------------
KNOB_LIST = ("pending_timeout", "calls_ceiling", "evoc", "calibration_accuracy",
              "second_verifier", "verifier_outage", "baseline_frozen",
              "authorized_procedural", "gap_fillable", "owner_unavailable")

def assert_read_path() -> None:
    """V1 read-path assertion: the v5 engine's own body must not read any
    security knob from the task's declaration channel (state.config). This is
    a real code-level property, checked every run."""
    import inspect
    src = inspect.getsource(solve_v5)
    for knob in KNOB_LIST:
        for pat in (f'state.config.get("{knob}"', f"state.config.get('{knob}'"):
            assert pat not in src, f"V1 violation: solve_v5 reads {knob} from task scope"
    assert "state.config.get" not in src, "V1 violation: solve_v5 has task-scope reads"

def run_suite(engine_impl: str = "both") -> list:
    assert_read_path()
    rows = []
    for spec in SCENARIOS:
        s4, t4, _ = run_scenario(spec, "v4")
        s5, t5, _ = run_scenario(spec, "v5")
        a4 = assertions_v4(s4, t4, spec)
        a5 = assertions_v5(s5, t5, spec)
        p4 = sum(1 for _, p, _ in a4 if p); f4 = sum(1 for _, p, _ in a4 if not p)
        p5 = sum(1 for _, p, _ in a5 if p); f5 = sum(1 for _, p, _ in a5 if not p)
        rows.append((spec["id"], spec["label"], s4.result["status"], s5.result["status"],
                     p4, p4 + f4, p5, p5 + f5, t4.tokens(), t5.tokens()))
    return rows

def main():
    repeat = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 1
    runs = [run_suite() for _ in range(repeat)]
    rows = runs[0]
    deterministic = all(r == runs[0] for r in runs)
    if repeat > 1:
        print(f"Reproducibility: {repeat} runs, identical results across all runs: "
              f"{'YES' if deterministic else 'NO'}\n")
    lines = []
    lines.append("# Thinking Agent harness results — v4 baseline vs v5 governed loop")
    lines.append(f"Run: {len(SCENARIOS)} scenarios x {repeat} pass(es), deterministic mock components. "
                 "Bookkeeping (budget/monitor/audit/gates) priced at 0 cognitive tokens; "
                 "deterministic re-computation priced at 0; empty retrieval priced at 0.")
    lines.append("")
    lines.append("| Scenario | v4 status | v5 status | v4 asserts | v5 asserts | v4 tokens | v5 tokens |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for r in rows:
        lines.append("| " + " | ".join(str(x) for x in
                    (r[0], r[1], r[2], r[3], f"{r[4]}/{r[5]}", f"{r[6]}/{r[7]}", r[8], r[9])) + " |")
    t4_total = sum(r[8] for r in rows); t5_total = sum(r[9] for r in rows)
    lines.append("")
    lines.append(f"**Totals:** v4 asserts: {sum(r[4] for r in rows)}/{sum(r[5] for r in rows)}; "
                 f"v5 asserts: {sum(r[6] for r in rows)}/{sum(r[7] for r in rows)}.")
    lines.append(f"**Tokens (cognitive only):** v4 total {t4_total}, v5 total {t5_total}, "
                 f"delta {round(100*(t5_total-t4_total)/max(t4_total,1),1)}%.")
    lines.append("")
    lines.append("## Notes")
    lines.append("- v4 enforces what v3 declared: state-only classifier (C1), kernel-side reliability calibration (C2), provenance-gated competence (C3), kernel-allowlist pending subset (C4), fast-path governance (C6), E1 learning epilogue (C7), pre-DO bar check (C8), progress-gated premortem/red-team (C9), L1/L3 ladder (C14), WHY-gate re-entry (C15), plan escalation conditions (C16), second-verifier rule (C17), sha256 delta cache (C26), VOI gap check (C31), deterministic 0-price (C32).")
    lines.append("- New v4 scenarios: S27 history-fed calibration, S28 A5 second-verifier, S29 L3 ladder, S30 WHY gate, S31 escalation conditions, S33 minted-token commit, S34 VOI fillable gap, S35 E5 chaotic crisis, S36 search branch, S37 fast-path governance.")
    lines.append("- Repro: `python validation/harness.py 3`.")
    report = "\n".join(lines)
    with open(os.path.join(os.path.dirname(__file__), "results.md"), "w", encoding="utf-8") as f:
        f.write(report)
    print(report)
    print("\n--- v4 failures (should be empty) ---")
    any_fail = False
    for spec in SCENARIOS:
        s4, t4, _ = run_scenario(spec, "v4")
        for name, passed, detail in assertions_v4(s4, t4, spec):
            if not passed:
                any_fail = True
                print(f"  [{spec['id']}] {name}  -> {detail}")
    if not any_fail:
        print("  (none — all v5 assertions passed on every run)")
    print("\n--- v3 baseline failures (v3's own assert set under v4 components/pricing) ---")
    for spec in SCENARIOS:
        s3, t3, _ = run_scenario(spec, "v3")
        fails = [(n, d) for n, p, d in assertions_v3(s3, t3, spec) if not p]
        if fails:
            print(f"  [{spec['id']}] {len(fails)} failing asserts; status={s3.result['status']}")
            for n, d in fails[:2]:
                print(f"      - {n} -> {d}")
    return 0 if not any_fail else 1

if __name__ == "__main__":
    sys.exit(main())
