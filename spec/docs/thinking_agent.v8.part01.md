# Thinking Agent

***

# Part I — The v7 Specification (verbatim)

*Part I is the complete v7 document, included unchanged so that v8 contains all of v7. Part II overrides where noted.*

## A Generalized, Governed AI Thinking Model for Broad Problem Solving and AGI/ASI Research

**Version:** 8.0\
**Research cutoff:** August 7, 2026\
**Status:** Research and engineering blueprint (validated — see §32)\
**Source policy:** Primary arXiv papers and official xAI materials were prioritized over third-party commentary.\
**Change policy:** v8 supersedes v7 and is SELF-CONTAINED BY CONSTRUCTION. Part I is the complete v7 specification, verbatim (all v5 + v6 + v7 sections), including the INSTANTIATED ROUTER CONFIGURATION — 212 historical strategy references (§II.2.6) plus the four counter-design records (§III.3). Part II is the complete v8 SELF-DIRECTED LEARNING (SDL) layer: the challenge-discovery tool (arXiv/internet scan), the gap-map curriculum planner, the learning ledger with its periodic review cycle, and the SDL governance (invariants 13–14, rules 42–48) — so the agent not only routes dynamically to the best human thinking model for any situation, but plans its own learning: it discovers challenge classes it has not met, selects the ones its gap map says it is weakest at, practices them under judge verdicts, and reviews its own learning history on a standing cadence. No external document is required (companion files: `extra_model.md`, `validation/v8_research_report.md`). Companion executable artifacts: `validation/harness.py`, `validation/style_router.py`, `human_thinking_models.json`, `style_routing_kb.json`, `v5/test_cases/`, `v5/traces/`, `v6/` (the `v7/` regression corpus is pending measurement).

***

## 1. Executive Summary

Thinking Agent combines:

1. A ranked portfolio of 40 traditional human thinking frameworks (Cynefin, Premortem, AAR, Double-Loop Learning, RPD, root-cause methods at the top).
2. The `WHAT → WHY → HOW → DO → REVIEW` process.
3. The memory, multi-agent, metacognitive, and self-evolution concepts from the earlier architecture drafts.
4. Research on cognitive architectures, reasoning, planning, tool use, reflection, verification, multi-agent systems, memory, self-improving scaffolds, and agent security.
5. Production patterns documented by xAI: adaptive reasoning, parallel subagents, plan-review workflows, verification, synthesis, tool-oriented agent harnesses.

Its central operating loop:

> **META-CONTROL → WHAT → WHY → HOW → DO → REVIEW**

A continuous **VERIFY** layer surrounds every stage; a **governed loop** (loop monitors, budget envelope, stage gates, state-only classifier, delta verification, checkpoint/resume, progress gating) guarantees termination, graceful failure, and cost-boundedness.

v5's advance over v4 is **trust-boundary completion**: v4 narrated kernel-holding; v5 executes it. Specifically, v5: (a) moves every security knob onto a **world-facts read path** — the v5 engine's own body contains zero task-scope reads of the knob list (`pending_timeout`, `calls_ceiling`, `evoc`, calibration, identities, outage, baseline-frozen, write-authorization); the world object is seeded from the scenario (the world model), and a **code-level read-path assertion** (`assert_read_path`) runs with every suite pass (V1); (b) feeds competence from a **kernel-sourced calibration registry with a provenance gate** — the doc's own rule, "self-reported accuracy is not evaluation history," is now enforced by the code (V2, S45); (c) removes the **allowlist backdoor** — PENDING subset execution is kernel-table membership only (V3, S38 negative case); (d) makes the **second-verifier rule kernel-computed** from the identity registry, not a task flag, and blocks below-bar/second-missing execution before DO (V4, S39); (e) fires **L3 at attest time on the attested class**, making the ladder's third level genuinely reachable (V5, S29); (f) makes **memory retrieval real** — priced by hits, querying task-derived terms, genuinely filling gaps (V6/V11, S40/S34); (g) **delta-caches outcome verification** and gates the in-loop and epilogue reviews and the planner, removing unchanged-state work the v4 claims promised but didn't deliver (V7); (h) exercises the previously-dead mechanisms — owner-unavailable ESCALATED, G-WHY-4/-5, novelty-plateau→RESOURCE\_LIMITED, invariant-8 replication denial (V8, S41–S44); (i) adds the **E5 stabilize-before-diagnose** pass (V10, Cynefin's act→sense→respond); (j) checks the bar on the **selected decision's** verifier, not the candidate max (V14). Every change is demonstrated: **v4 baseline 177/177 asserts, v5 187/187 asserts, 44 scenarios, deterministic across runs** (§32).

Thinking Agent is not a claim that one architecture can literally solve every mathematically, physically, or computationally possible problem. Some problems are undecidable, intractable, underspecified, unsafe, or impossible with available evidence and resources.

Here, **universal problem solving** means that the system can recognize a wide range of problem classes and return the most responsible available outcome: a verified solution; a bounded approximation; a set of ranked alternatives; a request for missing evidence; a safe experiment or probe; a demonstration that the current specification is infeasible; a calibrated statement of uncertainty; or a refusal or human escalation when action would be unsafe.

Every task terminates in exactly one of the eight graceful states (§3.3), and every terminal state produces the proof-carrying decision packet (§15.4).

Thinking Agent should be viewed as a scaffold for researching AGI, not as proof that AGI or ASI follows automatically from adding more agents or more inference-time computation.

***

## 2. Core Thesis

A generally capable AI system is not just a large model. It is a governed system that combines:

```text
Foundation-model capability
× adaptive cognitive control
× grounded world interaction
× structured memory
× planning and search
× independent verification
× continual learning
× safety and governance
```

This is a multiplicative design heuristic rather than a mathematical identity. A severe weakness in any component can limit the whole system.

Thinking Agent separates the functions of generating an answer, determining whether it is true, determining whether the action is safe, executing the action, learning from the result, and changing the system that generated the result. These functions must not be collapsed into one unconstrained model call — and in v5, the **authority to set the numbers those functions depend on** is separated from the model that benefits from setting them at the *code level*: the algorithm's read path for security knobs is the world object (kernel-held), and the harness asserts that no security knob is read from the task's declaration channel (V1, §32 S45).

***

