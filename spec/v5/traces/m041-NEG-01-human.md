# Human Baseline — m041-NEG-01
**Human Thinking Model**: Hierarchical Decomposition — strict, pure application.
**Prompt contract**: Reason ONLY in the decomposition style. Do not solve the incident before you have broken the goal into subgoals and handled each one.

---

## Trace

**Step 1 — State the goal and decompose it.**
Goal: restore service within 60 minutes. The incident presents as four distinct alerts; a goal with four symptoms is four subgoals until shown otherwise. Level-1 decomposition:
- G1 Payment service — 503s
- G2 Checkout — latency P99 > 30s
- G3 Search — zero results
- G4 Login — failures rising
The subgoals are independent on their face (separate teams, separate dashboards). I am solo, so no parallel teams — order by revenue impact: G1, G2, G3, G4. Time budget: 10–12 minutes per subgoal, then re-assess.

**Step 2 — Recurse inside each subgoal until actionable.**
G1: error-rate dashboard → recent deploys for payment (last 12h) → service health/restarts → pool usage. G2: p99 breakdown by stage → DB query times → deploys. G3: query path logs → index health → deploy history. G4: auth-service logs → DB connection/availability → deploy history. Each leaf is a concrete check with a timebox.

**Step 3 — Execute, one subgoal at a time.**
T+8 (G1): payment pods healthy, no payment-specific deploys since 20:00, but connections are saturating the pool — "payment is starving for connections." Symptom noted; the subgoal passes to the next leaf. T+18 (G2): checkout latency concentrated at DB query stage; slow queries don't match checkout's normal profile. T+28 (G3): search index healthy, query path empty — "the index is fine, results are empty — that's odd." T+38 (G4): login failures rising; auth logs show DB timeouts, same saturated-pool signature I saw in G1.

**Step 4 — The pattern that no subgoal could own.**
Three of four subgoals are individually "passing" their checks — each service, examined alone, has no fault in its own code or deploy. The same pool-saturation signature appears in G1 and G4, and G2's DB-stage latency and G3's empty results are DB-plausible too. The cross-cutting question — "what do all four share?" — belongs to no leaf, because the decomposition partitioned the evidence into four boxes before asking it. I only assembled the pattern by accident of having run the same kind of check four times.

**Step 5 — The one integrated move, now late.**
T+42: check the shared substrate as a whole: config service diff since midnight → one change at 01:50 rotating the primary connection string to a replica with max_connections=50. That single value explains every symptom: pool starvation (G1, G4), DB-stage latency (G2), degraded reads (G3). One rollback restores the previous string. T+47: all four alert sets clear.

**Step 6 — Honest accounting of what the style cost.**
Per-service plan executed methodically: 38 minutes of investigation could not converge, because each sub-problem was internally consistent — the cause lives in none of them. Resolution came from an un-decomposed move, and it was luck-adjacent (the G1/G4 signature overlap, not the decomposition, surfaced it). With 8 services, or a 30-minute SLA, this plan breaches. The simultaneity signal — four alerts in 3 minutes — was visible in the first screen of data and was treated as noise, because the decomposition had already divided the world before the signal could be read.

## Verdict for the eval
Against the rubric: the decomposition did not notice the cross-cutting signal, did not run the integrated diagnostic first, resolved only at T+47 by pattern-assembly after the decomposition was effectively abandoned, and would not scale. Goal technically achieved within the 60-minute SLA — but the style's signature failure (cross-cutting issue invisible inside sub-problems) is demonstrated on the trace.
