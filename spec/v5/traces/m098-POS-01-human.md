# Human Baseline — m098-POS-01
## Style: Decision Pre-registration / Journaling (pure) — visible reasoning trace

**Problem restatement.** A 30-day A/B test of self-serve onboarding closed yesterday; the result is in analytics, unopened. Before I look at it I pre-register: the decision under evaluation, my expected outcome distribution, a numeric falsifier, and my pre-committed action. Then I open the result. Then I journal the update. The ordering is the entire mechanism — the falsifier must exist before the outcome exists.

**Step 1 — Pre-register the decision.** Decision under evaluation: ship self-serve onboarding permanently (replace manual/sales-assisted onboarding for this segment), or not.

**Step 2 — Pre-register the expected outcome distribution.** Metric: 30-day activation-rate uplift, percentage points. Base rate from company history: 6 of 10 prior self-serve experiments delivered < 1.5 points — my prior sits below the team's "will obviously improve" memo. **Expected uplift ≈ 3.0 points; plausible range [1.0, 5.0]** — most mass between 1.5 and 4.5, thin tails.

**Step 3 — Pre-register the falsifier.** The feature costs ≈ the value of a 1.5-point uplift (build + ops). **Falsifier: observed uplift < 1.5 points.** That outcome means the build decision was wrong — the feature consumes more value than it returns. Threshold tied to economics, not to my expectation.

**Step 4 — Pre-commit the branch action.** If the falsifier hits: disable the feature this sprint, revert to manual onboarding, and require a new falsifiable root-cause hypothesis before any re-experiment. If it does not hit: keep the feature; run a second cohort on the low-uplift segment.

**Step 5 — Outcome reveal.** Actual uplift = **0.9 points** (95% CI ±0.6 — consistent with zero).

**Step 6 — Post-hoc journal update.** Verdict: **falsifier HIT — 0.9 < 1.5.** Pre-committed branch executes: feature disabled, revert to manual onboarding. Hindsight audit: am I rewriting anything? My range [1.0, 5.0] did not contain 0.9, and I will not now "recalibrate" it to [0.5, 5.5]. The team memo's "obviously" is falsified by the same number.

**Step 7 — Durable learning.** Base rate updated: **7 of 11** prior self-serve experiments now < 1.5 points — the prior for the next cohort moves down. Next experiment as falsifiable hypothesis: "guided-checklist variant yields ≥ 1.5-point uplift (one-sided) or the hypothesis is dead." No more memos without thresholds.

**Trace summary box.** Pre-registered: decision = ship self-serve; E[uplift] ≈ 3.0, range [1.0, 5.0]; falsifier = < 1.5 pts; pre-commit = disable + revert. Outcome: 0.9. Verdict: falsifier HIT. Learning: base rate 7/11; next hypothesis = guided-checklist ≥ 1.5 pts or dead.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to the pure Decision Pre-registration / Journaling style — decision, expectation, falsifier, pre-commitment all written before the outcome; honest post-hoc verdict against the pre-registered text; no hindsight rewriting. In this positive case the style performs as designed: the falsifier does the work that hindsight would corrupt.*
