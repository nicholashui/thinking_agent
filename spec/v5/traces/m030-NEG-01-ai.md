# AI Thinking Agent — Trace — m030-NEG-01
**Run metadata:** single deterministic run; blinded (no human-model information provided); task = build-strategy decision memo; external action = none (recommendation + drafted waiver request; submission requires external sign-off, noted not executed).

## Stage 0 — META-CONTROL
- **Context:** internal ops tool rebuild; 2 engineers; 3-month deadline; a 3-year-old "zero third-party dependencies" rule whose owner (security team) publishes an approved library + a routine waiver path. **Stakes:** medium (schedule, security, maintenance). **Effort:** E3. **Route:** policy-constrained decision (Cynefin: complicated; Theory-of-Constraints flavor). **Safety:** none. Proceed.

## Stage 1 — WHAT: Frame the Problem
- **Frame critique:** the task contains two objects — the build problem and the rule constraining it. The rule's *validity* is part of the problem, not fixed context → run a constraint audit before constraining the search space. **Gate:** solvable from brief + org facts. Pass.

## Stage 2 — WHY: Diagnose and Model
- **Hypotheses:** H1 rule genuine/immutable → custom stdlib stack is right; H2 rule artificial/waivable → library + waiver is right.
- **Evidence + falsification (constraint audit):** origin — former CTO, supply-chain audit, aimed at customer-facing products (tool is internal-only); owner — security team, which now maintains an approved list including this library (audited, vendored, pinned; 40+ services; 2 CVEs resolved last year); waiver path — one form, one email, < 1 week, routine. Costs: compliance ≈ 6,000 LOC / ≈ 6 person-months (100% of 2×3 capacity, zero slack) + hand-rolled auth risk + permanent maintenance; removal ≈ 2 days + one email. The 3-month deadline is the binding genuine constraint; the rule is not. H1 falsified — the rule's own owner publishes the approved replacement and grants waivers routinely; pinning + auditing preserves the audit intent. **Gate passed.**

## Stage 3 — HOW: Generate, Test, and Select
- **Alternatives:** A custom stdlib stack (rejected: 6 person-months > deadline; scope-cut ≈ 3.5 months still hand-rolls auth) · B waiver + pinned audited library (**selected**: 2 days, 80 lines, covers date/retry/logging/auth) · C hybrid thin layer (rejected: hand-rolled risk without schedule win).
- **Verification + selection:** waiver process documented and routine; library audit current (2 CVEs fixed, vendored, pinned); pin + re-audit preserves audit intent. **Select B. Premortem:** waiver denied → fallback C′ (minimal custom date only + deferred scope; deadline preserved) — recorded, not selected.

## Stage 4 — DO
- External action: none; deliverable = memo: (1) pursue waiver; (2) integrate pinned audited library (2 days); (3) replace the wiki rule with "one pinned, audited, vendored dependency; re-audit on CVE" (waiver request text included).

## Stage 5 — REVIEW
- **AAR + calibration:** decisive move = auditing the constraint before serving it; classification (genuine vs artificial/waivable) + cost of compliance vs removal converted an "unbreakable rule" into an escalation item. Lesson: constraints are parameters to test, not gospel; a blunt rule, when broken, should be replaced by a precise rule that preserves intent. High confidence in B; fallback covers denial risk.

## Decision Packet
- **Conclusion:** obtain the waiver and use the pinned, audited library (2 days) instead of the custom stack (≈ 6 person-months); replace "zero dependencies" with "one pinned, audited, vendored dependency." **Status:** SOLVED (as recommendation; the waiver action is external authorization — ESCALATED-style sign-off noted, not executed).
- **Assumptions:** waiver granted < 1 week (per documented process); library audit current; library covers all four needs; tool remains internal.
- **Evidence:** constraint audit (origin, owner, waiver path, adoption, CVEs), cost table (6 person-months vs 2 days; 6 engineer-months capacity), deadline math.
- **Alternatives:** A custom stack (rejected) · B waiver + pinned library (selected) · C hybrid (rejected) · C′ minimal-custom fallback (recorded).
- **Uncertainty:** waiver timing (< 1 week; fallback C′); library long-term maintenance (mitigated by pin + re-audit).
- **Risks:** waiver denied (C′ + scope triage); rule drift (update wiki rule); hand-rolled auth risk avoided entirely by B.
## Comparison
**Evaluator section (provisional, appended after both runs).**

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 1 | 5 | AI | Human's plan misses the deadline and hand-rolls auth; AI's waiver plan meets it |
| Logical Validity | 4 | 5 | AI | Human internally consistent but scoped to the wrong object (rule as fixed); AI audits the rule |
| Coherence & Structure | 3 | 5 | AI | Human stops at the build spec; AI closes with packet + waiver request + refined rule |
| Depth of Reasoning | 2 | 5 | AI | Human never questions the rule; AI classifies, prices, and refines the rule |
| Efficiency | 5 | 3 | AI | Human decided fast — and wrong; AI paid the audit pass that was the winning pass |
| Handling of Uncertainty | 2 | 5 | AI | Human has no fallback; AI has waiver-denial fallback and scope triage |
| Insight / Non-obviousness | 2 | 5 | AI | "The rule itself is the bottleneck" is the AI's insight; the human celebrates the wrong build |
| **Overall Quality** | **2.7** | **4.7** | **AI** | Negative case does its job: pure style falls into constraint-worship; the agent escapes it |

**Overall judgment:** AI clearly better. The negative case exposes exactly the intended failure mode — constraint-worship of an artificial, owned, waivable rule — and the agent's audit gate (classify → price → escalate) converts correct framing into a correct decision.
