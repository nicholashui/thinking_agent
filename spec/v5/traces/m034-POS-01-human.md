# Human Baseline Trace — Measurement & Operationalization
## Test Case: m034-POS-01

The word "engagement" is not a quantity; it is a wish. I will not ship or kill anything until the construct is measurable.

### Step 1 — Decompose the construct
Candidate sub-constructs: (1) interaction (time, clicks), (2) activation (reached value), (3) retention (comes back). These measure different things; arguing about "engagement" without picking is the dispute the VP would happily start. Pick ONE primary: activation — reaching first value — because it is a clean binary outcome with a traceable event.

### Step 2 — Operational definition of the primary metric
Activation rate = (new signups whose first GENUINE project is created within 7 days of signup) / (new signups in the experiment window).
- Numerator: users with event `project_created` AND a project quality gate (≥ 1 board, ≥ 3 cards, ≥ 1 user edit).
- Denominator: signups per arm. Cohort: experiment arm. Window: 7 days from signup.

### Step 3 — Instrument audit (before reading any number)
An instrument is valid only if it fires when the construct occurs and does NOT fire when it does not. Check: can `first_project_created` fire without the construct? Yes — untouched template clones. That is a validity defect, not a statistics defect. Leakage per the instrumentation note: B 55% clones, A 20%.

### Step 4 — Measure on the corrected instrument
- A: 1,650 × (1 − 0.20) = 1,320 → 1,320 / 5,000 = 26.4%.
- B: 1,800 × (1 − 0.55) = 810 → 810 / 5,000 = 16.2%.
The naive comparison (36% vs 33%, ship B) inverts on the leak-free metric: A beats B by 10.2 pp.

### Step 5 — Guardrails
Retention of activators: A 62% vs B 60% — favors A. Time-to-first-project: B 38 h vs A 41 h — B's only win, and it is the shortcut: the flow does the work, so users "finish" faster. Both guardrails point the same way.

### Step 6 — Uncertainty
Clone shares (55%/20%) are estimates: even at B's clone share = 40%, B = 1,080 → 21.6% < A 26.4% — the verdict survives a 15-pp misspecification. Sampling: n = 5,000/arm, CI ≈ ±1.3 pp on a 50% rate; a 10.2-pp gap is far beyond noise.

### Conclusion
Verdict: DO NOT ship B. Re-run with the corrected event definition and a pre-registered rule: ship iff corrected activation ≥ control + 2 pp (95% CI) and retention guardrail not more than 1 pp below control. The vague objective was the only real blocker: operationalized with a leak-free instrument, the decision inverts, and shipping B would have been a measurement error presented as a product win.
