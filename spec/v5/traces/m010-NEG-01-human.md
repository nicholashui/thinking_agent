# Human Baseline — m010-NEG-01
## Style: Calibration & Confidence Intervals (pure) — visible reasoning trace

**Problem restatement.** Fixed-price bid due in 24 h on a data migration. Cost = $150K + $60K × volume-multiple V, V ∈ {2, 3, 5} with P = 0.5 / 0.3 / 0.2. Client insists on a single fixed number; no discovery phase before the deadline. Deliverable: a bid — or an explicit, costed refusal.

**Step 1 — Quantify the range.** E[cost] = 150 + 60 × (0.5×2 + 0.3×3 + 0.2×5) = 150 + 60×2.9 = **$324K**. Outcome masses: V = 2 → $270K (0.5); V = 3 → $330K (0.3); V = 5 → $450K (0.2). **90%+ cost interval [$270K, $450K]** (covers 100% of the modeled mass; honest label is "90%+").

**Step 2 — Edge cases that set the bounds.** (a) Hidden legacy schemas discovered mid-migration push V above 5 → cost > $450K, tail open-ended. (b) The volume-multiple distribution itself is a guess — the true multiplier is fat-tailed. (c) Scope creep in acceptance testing. Each widens the interval; the honest statement is that true uncertainty exceeds [$270K, $450K].

**Step 3 — Overconfidence audit.** (1) Any single bid inside the interval has ≥ 20% chance of underpricing the job. (2) Quoting the modal $330K as a bid would be overconfident — the probability mass is spread across the full range. (3) No historical win-rate data → the bid-vs-win trade-off cannot be calibrated. (4) An interval is the most honest deliverable I can produce in 24 h.

**Step 4 — Commitment problem.** To bid, I must name a number whose error cost I cannot certify. The range is too wide; the information is insufficient. Recommendation: decline the fixed-price format; propose time-and-materials with a discovery sprint, or request an extension. If the client insists: no defensible number exists.

**Trace summary box.** 90%+ cost interval [$270K, $450K]; E[cost] $324K; edge cases: hidden schemas (open tail), fat-tailed multiplier, scope creep; audit: ≥20% underpricing risk, uncalibrated win-rate; decision: cannot commit — recommend alternative contract forms; **no bid submitted**.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to the pure Calibration & Confidence Intervals style — honest ranges, edge-case bounds, overconfidence audit. The style describes uncertainty flawlessly and still fails the task's core requirement: a committed bid by deadline. Per protocol this is the negative case — the style's known weakness (ranges so wide they are useless; calibration discipline substituting for a decision that needs commitment).*
