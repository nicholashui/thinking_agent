# Human Baseline — m055-POS-01
## Style: Causal Reasoning in Economics (pure) — visible reasoning trace

**Step 1 — State the identification question first.** "What is the identification strategy? Which confounders survive it, which don't?" Not "what does the data show" — "what claim can this data support?" The claim requested is causal: does the subsidy raise LTU employment, and by how much?

**Step 2 — Enumerate confounders before any estimator.** Threat classes, because class determines whether the strategy absorbs them: (a) time-invariant differences between regions — Region A was selected in 2019 for high LTU concentration; (b) common time shocks — the nationwide recovery from Jan 2024; (c) time-varying, region-specific shocks — the retraining program, Region A only, from Jan 2024; (d) anticipation — subsidy announced June 2023; (e) spillover/SUTVA — firms hiring across regions; (f) composition of the LTU pool.

**Step 3 — Kill the naive estimators.** Before-after, Region A: 55.2 − 50.9 = +4.3 pp. Confounded by (b): the whole economy recovered. Cross-sectional: A − B = +1.8 pp in Post-2 — confounded by (a): treated region is structurally different. Neither survives; neither is an estimate of the subsidy.

**Step 4 — DiD, with its assumptions on the table.** DiD absorbs (a) and (b). It survives only if no (c) exists, plus no anticipation (d) and no spillover (e). Verify the first before trusting it: pre-period placebo DiD = (51.2 − 50.9) − (51.0 − 50.8) = +0.1 pp ≈ 0 → parallel trends hold pre-treatment. Good.

**Step 5 — The survival question.** Now the audit that decides everything: which confounders survive the DiD? (c) is the killer — the retraining program loads exactly on the post period and only on Region A. It is indistinguishable from the subsidy in the full-window DiD: (55.2 − 50.9) − (53.4 − 50.8) = +1.7 pp — that number mixes subsidy with retraining. A parallel-trends placebo will not catch it (it is a post-period event); only the confounder audit does. Solution: restrict to the window before the confounder exists, Jul–Dec 2023: DiD = (52.8 − 50.9) − (52.0 − 50.8) = +0.7 pp.

**Step 6 — What survives the restricted strategy.** Absorbed: (a), (b). Surviving but named: (d) anticipation around June 2023; (e) spillover; and seasonality — the clean window is Jul–Dec against a full-year baseline; a same-month 2022 placebo exists in the monthly panel and should be run. What is *not* handled: anything after Dec 2023. The retraining program means the post-2023 record can never separate subsidy from retraining with this design.

**Step 7 — The claim, scaled.** "The subsidy raises LTU employment by ≈ +0.7 pp in the first six months, significant at p < 0.01 given SE ≈ 0.25 pp. The full-window +1.7 pp overstates the policy effect: a co-occurring region-only program is confounded with it. Effects beyond six months, persistence, and general-equilibrium effects: unknown — the design cannot identify them."

**Trace summary box.** Naive +4.3 pp → killed (common shock). Cross-section +1.8 pp → killed (selection). DiD full-window +1.7 pp → killed (surviving confounder: Region-A retraining, post-only). DiD restricted Jul–Dec 2023 = +0.7 pp → surviving threats named (anticipation, spillover, seasonality) → claim = +0.7 pp first six months, persistence unknown.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Causal Reasoning in Economics: identification question before estimator; confounders enumerated by threat class; every estimator paired with "which confounders survive it"; the post-period region-specific confounder treated as a strategy-survival question, not a robustness check; claim scaled to what the surviving strategy identifies. Signature move: confounder-survival audit before estimation.*
