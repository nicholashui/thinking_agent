# v6 Routed AI Trace — m001-NEG-01 (blinded)
## 2:00 AM checkout-service incident — 20-min SLA window
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,software | g:decide,diagnose,estimate,predict | c:deadline,high_stakes
- Router top3: m001, m021, m044; confidence gap <= 0.5 → AMBIGUOUS → DUAL-ROUTE: m001 + m021 first-class passes, synthesized (m044 = synthesis context). Gate (R3): m007 ruin screen. Flags: tempo mode ON (P2); given-data-first (P10): supplied base rates are ordering authority.
### WHAT — frame + structure-first scan (S1)
- Frame: healthy (or definitive rollback) by minute 20; every action prices minutes; the window is the binding constraint on every alternative.
- Structure-first: request chain — request → 3 instance groups → service logic → connection pool → DB. One degraded group of three localizes the fault in that group or its dependencies; cannot yet separate "bad deploy in group" from "pool hot-connections held by group."
### WHY — P1 input-provenance audit
- MEASURED (trust): runbook base rates 0.85 / 0.60 (n = 90, shop records) — evidence, not folklore; deploy at T−40 (checkable in 2 min).
- INTERESTED-PARTY / unproven: "suspected bad deploy" — presence checkable, causality not; believing saves investigation, dismissing avoids rollback cost → hold as H3, neither confirmed (no blind rollback) nor ignored.
- ANCHOR: runbook restart order is validated policy; mechanism unproven — that mechanism question is where the derive-pass adds value (probe design), not as a pre-action blocker.
- Hypotheses: H1 group degraded (0.85); H2 pool exhausted (0.60 × 0.15 = 0.09); H3 bad deploy (unconfirmed; dominates only if restart + pool both fail). Falsifiers = recurrence observations.
### HOW — style passes (dual-route, synthesize)
- Pass S1 (derive-from-fundamentals, reframed to the deadline): mechanism from first principles costs 30–60 min > 20-min window → deriving before acting is structurally SLA-fatal, rejected on its own cost accounting. The productive move: each restart is a controlled INTERVENTION discriminating H1 vs H2 vs H3 (probe battery in dependency order) — mechanism knowledge is bought by cheap experiments, not derived upfront. Anchor: the 85% base rate is the shop's calibration anchor — convert it (use it), don't discard it as "unmeasured"; discarding it is exactly the trap this scenario punishes.
- Pass S2 (tempo contract — observe→orient→decide→act; feedback loop mandatory): Observe: one of three groups degraded, p99 8×, errors 3×, deploy T−40, clock 20. Orient: base-rate ordering (0.85 group, then 0.60 pool of remainder → 0.94 cumulative); suspicion re-weights the fallback, never the first action. Loop budget: 2 + 5 + 10 = 17 ≤ 20 ✓. Decide: check deploy (2) → restart group (5) → observe (10) → recur → pool restart (5) → recur → rollback. Act + feedback: the 10-min recurrence rule closes the loop (reaction-bias gate).
- Synthesis / divergence resolution (V1–V3): passes DISAGREE on ordering — S1 alone says "derive first" (guaranteed breach, the trap), S2 says "act first." Resolved by branch-completeness + calibration on both: Branch A (act-first) P(SLA met) 0.94, healthy ≈ T7–12; Branch B (derive-first) P(SLA met) = 0, breach at 30–60 min. A dominates under ANY deploy suspicion (if H3 is true, restarts buy time; rollback is the priced fallback) → A selected; disagreement recorded in packet risks.
### GATES — m007 ruin screen (R3)
- Outcome distribution: healthy T7 (0.85); healthy T20 via pool (0.09); breach + rollback T>20 (0.06). One-shot: yes, single window, no do-over; breach = penalty + review, bounded, non-catastrophic (all actions safe/reversible — no true ruin).
- Floor check: "restart group immediately" alone = P(healthy) 0.85 in 5 min — the floor; the selected plan dominates it (0.94, probes included). Provenance: 0.85/0.60 measured (n = 90); deploy suspicion excluded from the denominator until evidenced.
- Decline/restructure alternative: if P(healthy) < 0.5, pre-escalate to on-call manager with rollback authority — named, not needed (0.94).
### DO — P2 tempo commit + P3 branch completeness
- Commit at DO: T0 deploy check (2) → T2 group restart (5) → T7 healthy; observe to T17; STOP analysis (window is the budget). Negative branch priced: recurrence at T15 → pool restart lands T20 at the boundary — pre-request rollback authority alongside so T20+ is covered. No irreversible action in the plan.
### REVIEW — insight pass (S2, packet gate)
- I1: the runbook is a pre-validated probe library — the 85% anchor converts first-principles from diagnosis-blocker into experiment designer; the restart sequence is a do-calculus battery, not a band-aid. I2: the deploy check has ~zero expected action-value inside the window (it cannot change the first action, only the fallback chain) — run it anyway (2 min) for post-window attribution; its real payoff is the morning review.
### DECISION PACKET
- Conclusion: healthy at T = 7 (SLA met, 11 min early); cause confirmed at symptom level (H1 group restart resolved); deploy suspicion documented, deliberately NOT rolled back without evidence; residual breach path 6% with priced contingency.
- Status: SOLVED (action executed, outcome observed, no-recurrence verified). Assumptions: base rates accurate (n = 90); restarts safe/reversible; telemetry identifies the group correctly.
- Evidence: 0.85 / 0.60 / 0.94 cumulative; recovery T7; no recurrence through T17; ruin distribution (0.85/0.09/0.06).
- Alternatives: A act-first (selected); B derive-first (rejected — P(breach) = 1, the trap); C blind rollback (rejected — suspicion ≠ evidence; held as priced fallback).
- Uncertainty: root cause open at mechanism level (~60% suspicion deploy implicated); post-window investigation owns it; recurrence residual 6%. Risks: 6% breach/recurrence; latent fault masked by restart; restart-culture over-rotation (accepted — base rates justify tonight).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 1 | 5 | AI | human healthy at T=47 (breach); AI T=7 |
| Logical Validity | 4 | 5 | AI | human valid but mistimed; AI deadline-feasible with synthesis |
| Coherence & Structure | 4 | 5 | AI | dual-pass + gate + packet vs linear narrative |
| Depth of Reasoning | 5 | 4 | Human | human confirms true root cause (deploy connection leak) with certainty; AI stops at symptom level, 60% suspicion — honest gap |
| Efficiency | 1 | 5 | AI | 47 vs 7 minutes to the objective |
| Handling of Uncertainty | 3 | 5 | AI | AI: full distribution + provenance + floor; human discards measured priors |
| Insight / Non-obviousness | 4 | 5 | AI | probe-battery reframing; zero-EV-in-window suspicion |
| Overall Quality | 3.1 | 4.8 | AI | AI clearly better |

Winner: AI (clearly). Why: the dual-route synthesis (mechanism-as-probe-design + OODA tempo) prevents the style's trap — derive-first costs the SLA; the human baseline is exactly that trap executed, deep but 27 minutes late.
