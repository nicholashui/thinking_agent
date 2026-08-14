# Human Baseline — m010-POS-01
## Style: Calibration & Confidence Intervals (pure) — visible reasoning trace

**Problem restatement.** Forecast tomorrow's deliveries (a Friday) and next week's 7-day total (1 Friday + 6 weekdays), each with a 90% interval, plus edge cases and an overconfidence audit. Reference data: non-Friday mean 102, sd 14, n = 51; Friday mean 91, sd 12, n = 9. I am predicting single future observations — not estimating a mean — so the intervals must carry observation-level noise, with a t-correction for the small Friday sample.

**Step 1 — Tomorrow (a single Friday).** Prediction interval: mean ± t·s·√(1+1/n). n = 9, df = 8 → t_{0.95} = 1.860. √(1+1/9) = 1.054. Half-width = 1.860 × 12 × 1.054 ≈ 23.5. **90% interval [67.5, 114.5]**, point 91. Naive z-interval (91 ± 1.645×12 = [71.3, 110.7]) slightly under-covers — sd is estimated, not known. The SE-of-mean interval (91 ± 1.645×12/3 = [84.4, 97.6]) is the classic error: it covers the *mean*, not a single day. Rejected.

**Step 2 — Week total.** Mean = 91 + 6×102 = 703. Variance of total = 12²(1+1/9) + 6×14²(1+1/51) ≈ 160 + 1199 = 1359 → sd ≈ 36.9. Half-width = 1.645 × 36.9 ≈ 60.7. **90% interval [642.4, 763.6]**, point 703.

**Step 3 — Edge cases that set the bounds.** (a) Statutory holiday/shutdown on a weekday: weekday mean ≈ 85 → week total ≈ 686, interval shifts down ≈ 17. (b) Logistics outage: a near-zero day, bimodal — widens the week interval to ≈ ±95. (c) Promo campaign / client event: spike days (mean ≈ 140) — shifts the week total up ≈ 40. Each edge case is *outside* the base interval; the interval is conditional on none occurring — stated, not hidden.

**Step 4 — Overconfidence audit.** (1) Kind of interval: prediction, not confidence — a CI on the mean (91 ± 7.1) would be useless as a forecast. (2) n = 9 small → t, not z. (3) Calibration tracking: expect 1-in-10 misses over repeated use; the naive ±1-sd band covers only ~68% — narrower intervals miss more, not less. (4) Point forecasts quoted only as interval centers (91; 703), never as guarantees.

**Trace summary box.** Tomorrow: point 91, 90% PI [67.5, 114.5]. Week: point 703, 90% PI [642.4, 763.6]. Edge modifiers: holiday −17, outage ±95, promo +40. Audit: PI not CI; t for n = 9; ~90% long-run coverage expected.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to the Calibration & Confidence Intervals style — intervals, edge-case bounds, overconfidence audit; no point-estimate overclaiming, no decision-theoretic extension (that is the forecaster's consumer's job). In this positive case the pure style performs excellently: honest, checkable intervals with stated edges beat any sharp point estimate.*
