# Human Baseline — m098-NEG-01
## Style: Decision Pre-registration / Journaling (pure) — visible reasoning trace

**Problem restatement.** SEV-1: payments API 500s for 20 min, $12K/min, spike at deploy v2.3.1. The discipline I am sworn to: pre-register decision, expected outcome distribution, falsifiers, pre-committed branch actions — before acting. I complete the ritual, then act.

**Step 1 — Pre-register the decision.** Decision under evaluation: one-click rollback of v2.3.1 vs hotfix-forward vs investigate-first.

**Step 2 — Pre-register the expected outcome distribution.** Rollback branch: E[recovery] ≈ 8 min (1 min click + 5–7 min converge), range [5, 15] min, success probability ≈ 0.8 given the deploy-time correlation, normal DB load, no config change. Hotfix-forward: ≈ 28 min, range [25, 40]. Investigate-first: ≈ 45 min, range [40, 60], highest diagnostic certainty.

**Step 3 — Pre-register the falsifiers.** F1 (rollback theory): if error rate is not < 5% within 10 min of rollback, the deploy is not the sole cause. F2 (deploy-is-cause evidence): 41% spike at T+0 with an unindexed-query signature in the capture-path logs — present. **Falsifier for the rollback theory: recovery within 10 min of rollback.**

**Step 4 — Pre-commit the branch actions.** If F1 does not fire → cause confirmed as v2.3.1; keep the rollback, open the code fix. If F1 fires → redeploy v2.3.1, escalate to L2 with this journal attached. If errors drop within 5 min → monitor 5 more minutes before declaring restored.

**Step 5 — Act.** Rollback initiated at T+10 (ritual complete). Errors < 5% at T+14; service-restored signal at **T+15**. Incremental incident cost: 15 run-minutes × $12K = **$180K** — of which the ritual consumed 10 live minutes ≈ **$120K**.

**Step 6 — Post-hoc journal.** Decision correct; expected recovery [5, 15] matched at 15; falsifier F1 did not fire — deploy confirmed as cause. Learning: log the query signature; add a pre-deploy query-plan review gate to the pipeline.

**Trace summary box.** Pre-registered: decision = rollback; E[recovery] ≈ 8 min [5, 15]; falsifiers F1/F2; pre-commits = keep / redeploy+escalate branches. Outcome: restored T+15, $180K incremental. Learning: query-plan gate. **The falsifiers, written before the action, were written at $120K — the ritual's own price tag.**

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to the pure Decision Pre-registration / Journaling style — full ritual before action, distribution + falsifiers + pre-commitments, honest post-hoc journal. Per protocol this is the negative case: bureaucratic latency is the failure. The decision was correct and the learning is real, but $120K of the loss is the ritual's own price tag — the style supplies no speed when the urgent step is the outcome, not the journal.*
