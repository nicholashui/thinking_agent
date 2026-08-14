# AI Thinking Agent — Trace — m098-NEG-01
**Run metadata:** single deterministic run; blinded; task = SEV-1 mitigation with a journaling requirement (full pre-action ritual available but its ~10 min cost is stated; timeboxed ≤2 min journal or retro-forecast permitted); external action = rollback (authorized).

## Stage 0 — META-CONTROL
- **Context / Stakes:** payments API 500s for 20 min, $12K/min; error spike 0.4% → 41% at deploy v2.3.1; DB load normal; no config change; rollback ≈ 5 min, hotfix ≈ 25, investigate-first ≈ 40+. Every minute ≈ $12K; mitigation latency dominates correctness. **Effort:** E2.
- **Route:** incident-response class (Cynefin: complicated, but the deploy-time correlation collapses the search). **Safety:** rollback = reversible external action; authorized. Proceed.

## Stage 1 — WHAT: Frame the Problem
- **Frame:** restore service with minimal time-to-mitigate; secondary goal: journal (decision, expected recovery, falsifier) without delaying the action.
- **Scope:** current evidence is the decision basis; no data collection before acting. **Gate:** not an evidence-gathering problem — the deploy-time correlation is the strongest available signal. Exit gate passed.

## Stage 2 — WHY: Diagnose and Model
- **Hypotheses:** H1 v2.3.1 broke the capture path (41% spike at T+0; DB load normal rules out DB; no config change rules out config). H2 unobserved upstream dependency. H3 partial data-path failure.
- **Evidence / Falsification:** deploy-time correlation; query-plan anomaly in capture-path logs (unindexed-query signature). H1 falsifiable cheaply — if errors persist > 10 min after rollback, H1 dies.
- **Gate (G-WHY):** H1 dominates on evidence and falsification cost; alternatives recorded. Gate passed.

## Stage 3 — HOW: Generate, Test, and Select
- **Alternatives:** A. One-click rollback v2.3.1 → ≈ 5 min converge; reversible; if wrong, ~5 min lost + redeploy. B. Hotfix forward (patch query + redeploy) → ≈ 25 min; slower for the same root cause. C. Investigate first → 40+ min; best diagnostic purity, worst downtime.
- **Verification:** A's downside is bounded (5 min + redeploy); B/C guarantee longer downtime under H1. **Selection: A — rollback now.** Premortem: if errors persist past 10 min post-rollback → redeploy and escalate; 1-min monitoring cadence.

## Stage 4 — DO
- **External action executed: rollback v2.3.1 at T+1.** Timeboxed journal (≤2 min) written in parallel: decision = rollback; E[recovery] ≈ 6 min [5, 10]; falsifier = error rate < 5% within 10 min of rollback; branch = else redeploy + escalate.
- Errors < 5% at T+6; service-restored signal at **T+6**. Incremental cost: 6 run-minutes × $12K = **$72K**.

## Stage 5 — REVIEW
- **AAR:** time-to-mitigate 6 min; rollback confirmed correct (errors < 5% at T+6). The falsifier for the rollback theory was registered while the fix ran — the instrument completed before the theory's outcome was confirmed. Learning: add a query-plan review gate to the deploy pipeline; log the unindexed-query signature to the runbook.

## Decision Packet
- **Conclusion:** v2.3.1 rolled back; service restored at T+6; root cause = new unindexed query in the payment-capture path. **Status:** SOLVED (external verify: error-rate monitor < 5% sustained; rollback executed).
- **Assumptions:** correlation = causation (validated by recovery); no second fault hidden in the old version. **Evidence:** 41% deploy-time spike; recovery within the 10-min falsifier window; query-plan anomaly.
- **Alternatives:** A (executed) · B (25 min, rejected) · C (40+, rejected). **Uncertainty:** second-fault residual ≈ 5–10%; monitoring extended 30 min. **Risks:** redeploy without the query-plan gate reintroduces the fault.

## Comparison
**Evaluator section (provisional, appended after both runs).**

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | Human restored at T+15, AI at T+6 — ~$108K delta on held-out timing |
| Logical Validity | 5 | 4 | Human | Human: full distribution over branches; AI: sound but faster correlation-based triage |
| Coherence & Structure | 4 | 5 | AI | AI staged packet; human journal linear but complete |
| Depth of Reasoning | 4 | 3 | Human | Human models all three branches; AI's dominance argument is sufficient but leaner |
| Efficiency | 1 | 5 | AI | The deciding dimension: ritual latency cost ~$120K of live outage |
| Handling of Uncertainty | 4 | 4 | Tie | Both registered a falsifier for the rollback theory; human earlier, AI in parallel |
| Insight / Non-obviousness | 3 | 4 | AI | AI's retro-forecast timing — journal written while the fix runs — preserves learning at zero latency cost |
| **Overall Quality** | **3.3** | **4.3** | **AI (clearly)** | Negative case: bureaucratic latency is the failure this case was designed to expose |

**Overall judgment:** AI clearly better. Decision quality was roughly equal (both chose rollback; both registered a falsifier), and the human's distributional reasoning is richer — but the case's gate is time-to-mitigate, and the full ritual before acting converted 6 minutes of outage into 15. The AI kept the learning instrument (falsifier pre-registered while the action ran, verified by the recovery) without paying the latency tax; that is the adaptive use of the style, and the pure form could not do it.
