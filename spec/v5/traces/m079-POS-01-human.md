# Human Baseline — m079-POS-01
## Style: Confirmation Bias Hunting (pure) — visible reasoning trace

**Step 1 — State the belief, then design the kill-shot.**
Dana's belief: "the July pricing restructure caused the churn spike." The first question is never "is there more evidence for this?" — it is "what evidence, if found, would force me to abandon it?"
The answer, before anything else: churn among accounts never exposed to the new billing. If the grandfathered cohort churns at the same rate, the belief dies — no matter how loud its confirming stream is.

**Step 2 — Run the kill-shot.**
- Ledger item 2: grandfathered 3.5% vs new-tier 3.3%. Not only is there no gap — the no-price cohort churned slightly higher.
- Size is not a rescue: ≤500 seats 3.4%, >500 seats 3.5% — the old tier was size-blind and so is the churn.
- The restructure fails its own falsification test. Belief dead.

**Step 3 — Re-read the confirming pile under the dead belief.** All four items are real; none are discriminating:
- The 11 price-mentions: 8 of 11 cluster in July — the notification month, which hit every account including grandfathered ones; billing only hit >500-seat renewers.
- Four August interviewees explicitly denied price and named outages; the sales anecdote is two names, single-source.
- The 15% usage decline predates the pricing era — identical pattern in Q2 churners.
A confirmation trap: the evidence stream was real; the interpretation was not.

**Step 4 — What survives the kill-shot?**
- Reliability: SLA 99.95 → 98.6, three public incidents (Jul 8, Jul 19, Aug 2), MTR 4.2h → 11h — the collapse shares the churn timeline.
- Onboarding: 9 → 17 days to first value, after the June CS cut.
These are the variables that changed when churn changed.

**Step 5 — Revised conclusion.**
Do not roll back the tier ($1.2M ARR avoided on evidence that cannot survive its own controlled test). Fix the actual drivers: SLA/MTR and incident response; re-staff onboarding; first-to-value under 10 days.


**Trace summary box.** belief: pricing restructure → kill-shot: grandfathered-cohort churn → 3.5% ≈ 3.3% → belief falsified → confirming pile re-read under falsification (notification-month cluster 8/11; 4 denials; anecdote; non-discriminating usage) → real driver from timeline match (reliability + onboarding) → revised conclusion: keep the tier, fix ops → residual: notification effects on future >500-seat renewals, monitored.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Confirmation Bias Hunting — the disconfirming test is designed before any confirming evidence is re-read, the belief is allowed to be killed by its own ledger, and the conclusion is rebuilt only from evidence that survives the kill-shot. Signature move: the controlled experiment (grandfathered cohort) was sitting in the ledger the whole time — the hunter ran it first.*
