# Human Baseline — m038-POS-01
## Style: Margin of Safety (pure) — visible reasoning trace

**Step 1 — The official number is an estimate, not a fact.** 40 kN/m² comes from a 15-year-old mid-week survey with ±30% sampling error, and tourism has grown ≈ 60% since. The regulator's 44 is a legal floor, not a design basis. Any design that starts from 40 as truth has zero margin where the error actually lives.

**Step 2 — How wrong could the estimate be before the decision flips?** Flip point: true peak > design load → deck yields → ≈ $3.5M. The error structure is one-sided (the true peak can only be *under*stated — the survey missed the crowds). One-sided risk gets a one-sided margin.

**Step 3 — Build the cushion multiplicatively from independent error sources.** Surge: recorded 1.6× official; growth-adjusted normal ≈ 64, festival peak ≈ 96 static. Dynamics: pedestrians at resonance amplify ≈ 1.3×. Material/batch: ≈ 1.1×. Base margin design: 40 × 1.6 × 1.3 × 1.1 ≈ 91 kN/m². Cost ≈ (91−40)/40 × $400k ≈ $510k.

**Step 4 — The binding uncertainty is the surge factor itself.** It was measured once, never instrumented; ±25% is a fair bound. If surge is really 2.0× official, the true peak ≈ 96 × 1.3 ≈ 125. The margin must cover the error in the *margin's own factors*, not just the nominal numbers. Design: 40 × 2.0 × 1.3 × 1.1 ≈ 114 → round to 115 kN/m². Cost ≈ (115−40)/40 × $400k = $750k ≤ $760k budget.

**Step 5 — Cost the cushion.** 92 → 115 costs $230k. Failure costs ≈ $3.5M; the cushion is < 7% of the failure it retires. Saving $230k against a $3.5M one-sided tail is not economy, it is gambling with the resort's season. The cushion is the cheapest thing in this budget.

**Step 6 — Verify the flip point.** Design 115 is exceeded only if surge > 2.0× official AND dynamics > 1.3 AND material shortfall 1.1 — each a > 2σ miss, jointly ≈ 1%: the cushion absorbs the ±30% survey error, the ±25% surge-factor error, and the ±10% material error simultaneously. That is the margin of safety: the design survives being wrong about everything it estimated, at once.

**Trace summary box.** 40 (stale, ±30%, one-sided) → surge 1.6 × dynamic 1.3 × material 1.1 ≈ 91 → cushion the surge factor itself (±25%) → **design 115 kN/m²** → $750k vs $760k budget vs $3.5M failure → flip point at joint 2σ miss (≈ 1% probability). Decision: design to 115.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning deliberately confined to the pure Margin of Safety style — the official estimate treated as an error-bearing input, margin built multiplicatively from independent error sources, an extra cushion demanded over the binding (single-observation) uncertainty, and the flip-point question ("how wrong before the decision flips?") answered at the factor level. No expected-value hedging, no cost-benefit discounting of the tail: the cushion is non-negotiable.*
