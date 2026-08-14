# Human Baseline — m008-POS-01
## Style: Probabilistic Forecasting (pure Superforecasting) — visible trace

**Forecast first.** P(FlashSale30 final redemption rate > 25%) = **0.87**, range **[0.80, 0.92]**. Updated from a 0.13 prior on the day-7 report (rate = 18%). Not a point prediction — a scoreable probability with a revision rule.

**Step 0 — Decomposition.** The question "will the final rate exceed 25%?" splits into three sub-forecasts: (a) the level — mapping prediction 27.8 pp; (b) the error — residual sd 2.5 pp; (c) the tail — probability that level minus error crosses 25%. Each sub-forecast is separately checkable; this decomposition is the craft.

**Step 1 — Outside view (reference class).** 24 historical FlashSale campaigns; 3 of 24 cleared 25% → base rate = **3/24 = 12.5%**. Normal approx (mean 20, sd 4): P(Z > (25−20)/4) = P(Z > 1.25) ≈ 10.6%. Outside view: **prior ≈ 11–13%.** The CMO's single-number demand is declined — the answer is a distribution, not a point.

**Point prediction, declined.** "Final ≈ 27.8 pp" satisfies the CMO's form but cannot be Brier-scored, cannot be updated, and implies precision the 2.5 pp residual does not support — the planning system gets a distribution and a revision rule instead.

**Step 2 — Update on day-7 evidence.** Mapping: final ≈ 1.35 × early7 + 3.5 pp, residual sd 2.5. Predicted final = 1.35 × 18 + 3.5 = **27.8 pp**. Evidence strength check: 27.8 vs class mean 20 → 7.8 pp ≈ 3 sd above the class — a strong signal; updating is warranted, and the posterior should not be anchored to the weak prior.

**Step 3 — Posterior.** P(final > 25%) = P(Z > (25 − 27.8)/2.5) = P(Z > −1.12) ≈ **0.87**. Range [0.80, 0.92] (probability scale, ±1.5 sd of the residual). The evidence-to-outcome error (2.5 pp), not the prior, sets the width.

**Step 4 — Revision rules (what moves it).** Down: day-14 rate < 15% (maps to final < 24); promo-stack override of the code; a copycat discount. Up: day-14 rate > 22%. Scheduled checkpoints at day 14 and day 21; the forecast is rescored at day 30.

**Step 5 — Calibration honesty.** Brier if YES at p = 0.87: ≈ 0.017. The un-updated prior (0.125) would score ≈ 0.77 — updating is the difference. A point prediction is unscoreable and has no revision rule: that is precisely this case's point.

**Decision translation (not a forecast).** Recommend proceeding with the campaign plan; passing the 25% threshold is probable; no budget change; rerun the mapping on day-14 data. Forecast log entry: m008-POS-01, P = 0.87, range [0.80, 0.92], prior 0.125, revision triggers set.

**Track record.** The firm Brier-scores every forecast quarterly; the discipline is the log — score, compare against the reference class, and re-estimate the mapping. That feedback loop is what makes the next prior better; without it the style decays into numerology.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to the Superforecasting discipline — probability form, reference class first, mapping-based update with residual error, revision rules, Brier framing. The pure style's strength in its positive case: exact, checkable, and calibrated.*
