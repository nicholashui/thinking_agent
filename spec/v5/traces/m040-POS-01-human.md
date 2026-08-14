# Human Baseline — m040-POS-01
## Style: Leverage Points Identification (pure) — visible reasoning trace

**Step 1 — See the system first.** Two loops dominate. Reinforcing loop R: page → context switch → hasty change → new page. Inflow loop: hire → onboard → on-call rotation — every new engineer joins R as another body in the same loop; the loop's failure-generation rate is untouched by headcount. That is why 18 hires moved nothing. Process gates only add delay to the change step; they never cut failure generation at the source.

**Step 2 — Place candidates on the leverage scale.** Parameters/numbers: headcount, review count — lowest; a number change is a no-op when the loop structure is the problem. Delays: rotation periods, release cadence — tweak, no structural change. Negative-feedback strength: canary/staged rollout raises the detection loop's strength — good. Information flows: aggregating the incident tags = adding a missing link in the feedback path — the classic high-leverage, low-effort move. Rules: a canary mandate for the five recurring change classes — high. Goals: SLO with teeth — high but political, slow.

**Step 3 — Score every candidate: effort × effect.** (25 hires + exec reviews) effort $4.5M/yr + 6–12 mo lag, effect ≈ 0 — loop R unchanged, exactly what natural experiment #1 showed. (Process refresh) effort months, effect ≈ 0 — natural experiment #2. (Exec reviews) effort 1 hr/wk × 20, effect ≈ 0 — adds delay, adds no information. (Canary rule) effort ≈ 3 weeks, effect ≈ 30% of incidents at the source. (Feedback pipeline) effort ≈ 2 weeks, effect = unlocks the 43%, makes every later lever aimable. (SLO with teeth) effort months + political capital, effect high — sequence later.

**Step 4 — Rank by change per effort.** 1) Information flow (≈ 2 weeks): the 43% concentration is sitting in a database nobody reads — releasing it turns every other lever from guesswork into targeting. 2) Rules (≈ 3 weeks): canary the five classes → ≈ 30% of incidents stopped at the source. 3) Negative-loop strength — contained in 2. 4) Goals (SLO teeth) — high effect, high political effort; sequence later. 5) Parameters: 25 hires + exec reviews — lowest of all: $4.5M/yr, 6–12 month lag, and each hire walks straight into unchanged loop R. The board is paying for the weakest intervention point on the scale.

**Step 5 — Choose and compose.** Pipeline first (2 weeks) → the data names the rule's target → canary rule (3 weeks) → weekly 30-minute incident-class review keeps the loop learning. The two levers compose: information flow makes the rules lever aimable; neither requires headcount.

**Step 6 — Expected behavior + metric.** ≈ 43% of pages concentrated; canary catches ≈ 70% → ≈ 30% incident reduction → on-call 55–60% → ≈ 40%; SLO back to ≥ 99.9% within two quarters, zero new hires. Verify: quarterly SLO, pages-per-quarter from the five classes, on-call hours. Falsifier: if the five-class share has not fallen within 60 days, the rule is mis-scoped.

**Trace summary box.** Loop R + inflow loop → leverage scale → info-flow (2 wks) + rules (3 wks) top, hires bottom → compose → −30% incidents, SLO ≥ 99.9% in 2 quarters, 0 hires.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Leverage Points Identification — system map first, then intervention points positioned on the leverage scale, ranked by change per effort. The signature moves are first-sight structure recognition (the firefighting loop makes headcount a no-op) and the information-flow lever (point 6, not point 12).*
