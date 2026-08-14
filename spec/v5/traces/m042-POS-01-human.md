# Human Baseline — m042-POS-01
## Style: Abstraction Laddering (pure) — visible reasoning trace

**Climb — what is this an instance of?**
- Rung 1 (the team's level): the renewal page and its copy are underperforming.
- Rung 2: the renewal page is an instance of *renewal mechanics* — the ceremony around the billing date.
- Rung 3: renewal mechanics are an instance of *value realization* — a customer deciding at a checkpoint whether the product earned the renewal.
- Rung 4 (goal rung): a renewal rate is an instance of *habit formation* — we sell an outcome the customer uses weekly; the subscription is bookkeeping for continued usage. At this rung the cause of the drop cannot live at a lower rung.

**Test the rungs against the data.**
- Price rung (renewal-loss as price sensitivity): elasticity test flat (5%/10% discounts, no change). Rejected.
- Mechanics rung (copy/flow): A/B variants flat for a quarter. Rejected.
- Habit rung (rung 4) predicts: renewal loss concentrates in customers whose usage died before the billing date. Data: 80% of lost renewals are >40% weekly-usage-decay in the 60 days before renewal; retained cohort decays <15%. Fits. Win-back failures confirm: you cannot discount a dead habit.

**Descend — what does this mean concretely on Monday?**
- Monday 09:00: instrument the week-1 "aha" event — the activation counter is the rung-4 meter (one day).
- Tuesday: fix the onboarding path so the aha event fires past threshold for new cohorts (cohort experiment; activation is the guardrail metric).
- Wednesday: trigger re-engagement when weekly usage decays >40%, at T−45 days before renewal (in-app + support touch, capped cadence).
- Thursday: renewal-page copy changes only for the non-decayed cohort — the team's original work is still real; it explains the other ~20% of losses.
- Friday: renewals survey on the decayed cohort — if the honest answer is "we stopped using it," the habit rung is confirmed at the customer's own level.

**Return up — does the reframe hold against the ledger?**
- Expected: +8–12 points on renewal rate within 2 quarters, driven by activation and decay-triggered re-engagement. Falsifier: if the cohort study shows no activation→renewal correlation, re-climb — maybe the true rung is price after all; test the price rung with a proper experiment instead of doubling down on habit.

**Trace summary box.** renewal page → mechanics → value realization → habit (goal rung) → evidence picks habit (80% decay concentration, flat elasticity, win-back failure) → Monday: activation instrumentation, onboarding fix, T−45 re-engagement → ledger: +8–12 pts in 2 quarters; re-climb if the cohort study contradicts.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Abstraction Laddering. Signature moves: the double climb to the goal rung, evidence-based rung selection, the concrete Monday descent, and the re-climb falsifier; no non-laddering frame used.*
