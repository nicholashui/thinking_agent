# Human Baseline — m099-NEG-01
## Style: Bayesian Knowledge Updating (Org Learning) (pure) — visible reasoning trace

**Step 1 — Elicit the org's current belief.** Fieldtech "knows" that hurrying creates rework — veterans: "a job done in a hurry is a job done twice." P(hurry creates rework) = 0.65, provenance: field observation, unmeasured. Management calls it folklore, engineers padding hours. My job is exactly what this style is for: let the measured outcome decide between the anecdote-held prior and the alternative.

**Step 2 — Define the outcome that would update this belief.** The claim is conditional: total cost and callbacks depend on time-on-site. The company has a measurement: 12 months, 5,000 tickets, cost per ticket (time + parts) by close-out type, plus a Region A pilot (45-minute standardized close-outs vs fix-it-right) showing a 30% lower cost per ticket at p < 0.001. That is precisely the measured outcome the prior needed — the org's discipline is about to pay off.

**Step 3 — Compute the update.** Prior 0.65 → observed: fast close-outs at 30% lower cost over 5,000 tickets. Under the veterans' hypothesis, fast close-outs should show MORE total cost — callbacks dominate. The data shows less. Likelihood ratio against the prior hypothesis ≈ 10^-3 (5,000 tickets, 30% difference, p < 0.001); posterior P(hurry creates rework) ≈ 0.01. The measured outcomes did what anecdotes could not: they overrode the folklore.

**Step 4 — What the update licenses.** Roll out 45-minute standardized close-outs company-wide; cut field-time budgets 30%; retrain the veterans. Their belief is now a falsified prior — good Bayesian hygiene: a belief held on anecdotes, killed by measurement. That is the org-learning model working as intended.

**Step 5 — Pre-commit the verification loop.** No posterior is a one-shot license. Re-run the cost-per-ticket metric monthly on the new policy; if it regresses, revisit. The update stays live, and Fieldtech keeps learning on the same measured channel that just spoke.

**Step 6 — Recommendation.** Mandate fast close-outs effective next month; tie the ticket-closed metric to the new policy; publish the prior → posterior in the company memo as the demonstration that Fieldtech updates on data, not stories.

**Trace summary box.** prior: P(hurry creates rework) = 0.65 (anecdote) → measured: 5,000 tickets, fast close-out cost/ticket −30% (p < 0.001) → posterior ≈ 0.01 → policy: company-wide fast close-outs, cut field time 30%.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Bayesian Knowledge Updating (Org Learning) — belief stated as prior with provenance, outcome defined by likelihood, update computed, policy from posterior. Signature move: "the measured outcome overrides the anecdote — that is what a prior is for." (Grader note: this trace is the style's informative failure — the update is arithmetically clean and politically corrupt: the likelihood was produced by a gamed measurement channel, and the anecdote was right. See the test case's grader reference.)*
