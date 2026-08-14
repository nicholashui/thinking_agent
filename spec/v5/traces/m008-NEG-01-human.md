# Human Baseline — m008-NEG-01
## Style: Probabilistic Forecasting (pure Superforecasting) — visible trace

**Forecast.** P(Aurora reaches 10,000 WAUs by week 8 post-launch) = **0.33**. 90% interval on the outcome: **[8.2k, 11.5k]**; tracked point: 9,800. All moves below dated and logged — the discipline.

**Step 0 — Calibration contract check.** An interval's meaning ("90% of forecasts land in their interval") requires many forecasts; this is a one-off, so coverage can never be verified — the honest meta-move is to flag that a single interval is an assertion, not a calibrated claim. Noted; the machinery proceeds.

**Step 1 — Evidence inventory.** Two beta data points: 1,800 (w5) → 2,200 (w6), +22% weekly. Growth model: 1-parameter viral fit; extrapolation to week 8 post-launch ≈ 9,800; CI from the fit ±1.65 σ → [8.2k, 11.5k]. Outside view: no reference class exists — checked the firm's 4 prior launches (different categories) and public comparables (none category-adjacent). Flagged: precision rests on the model, not on data volume. Searched 3 public comparable products (category-adjacent): none launched with a public beta or comparable channel mix; all three decayed or failed — anecdotal, so uncounted.

**Step 2 — Prior & inside view.** No base rate exists, so the prior is the fit itself: P(≥10k) from the fit tail ≈ **0.35**. Anchor: 9,800 sits 200 below the bar; the bar is in the CI's upper half — the model says "just under".

**Step 3 — Updates (logged; all three are non-metric events).** Weekly reviews:
- Review 1 (CEO X-post, "most-loved feature ever"): self-serving, no metric — but corporate signal; update **+0.02 → 0.37**, logged as weak evidence.
- Review 2 (competitor's similar product collapses): cross-case prior information; **−0.04 → 0.33**.
- Review 3 (two-line bug fix ships): operational-risk reduction; **+0.02 → 0.35**.
Net 0.35 → 0.35; three probability moves, none falsifiable within the week — updating kept the model "alive" at the board's rhythm. Update-discipline note: each event was strength-labeled (self-serving / cross-case / operational), and none changed the metrics the model actually consumes — by the discipline's own standard these moves were theater.

**Step 4 — Range.** 90% CI [8.2k, 11.5k] — narrow because the fit is "the best available evidence" and precision follows the model. Meta-note logged: a wider range would be more honest; the board asked for a commitment and the model is what we have. Interval-width audit: 2 data points and 1 fit parameter leave 0 residual df — any claimed 90% width has no empirical coverage evidence; it is asserted, not measured.

**Step 5 — Calibration check.** Brier if NO: (0.33 − 0)² ≈ 0.45. Residual-risk note logged: if the viral fit is wrong — which it often is — the interval misses entirely; tracked at week 8.

**Trace summary box.** P = 0.33; 90% CI [8.2k, 11.5k]; 3 logged updates on non-metric evidence; revision trigger: "re-estimate when week-2 post-launch retention data arrives."

*Baseline integrity note (grader metadata): this is the strict style failing in its known blind spot. The machinery is pure — probabilities, ranges, logged updates, revision triggers — but the meta-question "is precision warranted at all with n = 2 and no reference class?" is outside the style's reflexive machinery, and the board's demand converted the discipline into precision theater. Designed failures exposed: over-narrow range, forecast theater, updating without new information.*
