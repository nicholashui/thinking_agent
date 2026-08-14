# v6 Routed AI Trace — m008-POS-01 (blinded)
## FlashSale30 redemption-rate forecast — binary, resolves day 30
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,software,strategy | g:estimate,maximize,predict | c:
- Router top3: m008, m044, m058; confidence gap <= 0.5 → AMBIGUOUS → DUAL-ROUTE: m008 + m044 first-class passes, synthesized (m058 = synthesis context). Gates (R3): none triggered (no adversarial/one_shot/unmeasured context); maximize goal → falsifiable checkpoint required (R4: day-14 triggers). P2 tempo OFF (no deadline). Fully specified (reference class + mapping + day-7 rate given) → P8 closed-scope fast path.
### WHAT — frame + structure-first scan (S1)
- Structure: single forecasting problem — level (mapping 1.35·early7 + 3.5) × error (residual sd 2.5) → tail P(final > 25%); decision tree underneath (campaign plan fixed, budget flex to day 14). Deliverable: a scoreable probability, not a point.
### WHY — P1 input-provenance audit
- MEASURED (trust): 24-campaign reference class; day-7→final mapping + residual sd 2.5 pp (both estimated from the same 24 — IN-SAMPLE: mildly optimistic, flagged). ANCHOR: none; INTERESTED PARTY: none (Brier-scored portfolio aligns incentives). Outside view is the prior, computed FIRST: 3/24 = 12.5%; normal approx Φ(−1.25) ≈ 10.6%.
### HOW — style passes (dual-route, synthesize)
- Pass m008 (contract: reference class first, >= 3 likelihood scenarios, posterior range, threshold flip, Brier-scoreable, revision rules):
  S1 given model → predicted final = 1.35×18 + 3.5 = 27.8 pp → P = Φ(1.12) ≈ 0.87; S2 in-sample optimism (true residual 5 pp) → 0.71; S3 mapping drift (slope 1.1, promo-stack override) → final 23.3 → 0.25. Main posterior 0.87, range [0.80, 0.92] (residual-driven); scenario-robust band [0.25, 0.87].
  Threshold flip: predicted final = 25 ⇔ day-14 rate = 15.9% — day-14 < 15% flips P to ≈ 0.31; > 22% → ≈ 0.98.
  Brier: 0.017 if YES at 0.87; un-updated prior (0.125) ≈ 0.77; a 50/50 prior-blend (0.5) ≈ 0.25 — 15× worse.
  Revision rules: day-14 rate < 15% / > 22%; promo-stack override; mapping-drift check (re-run the regression on day-14 data).
- Pass m044 (stakeholder): CMO's single-number demand is declined — the planning system consumes a distribution + revision rule; finance needs Brier-scoreable output for allocation; ops/data team hold the mapping-drift tail (the unconsulted party on S3); copycat risk sits with campaign ops.
- Synthesis (V1–V3): passes AGREE on 0.87 → proceed; agreement recorded in packet. m058 context: the day-14 checkpoint is a real option on the budget — hold budget flexible until the flip-point data lands; S3's 0.25 tail is exactly what the option prices.
### GATES — none (R3 not triggered)
- No mandatory gates on this signature; R4 falsifiable checkpoint = day-14 triggers above.
### DO — P8 closed-scope fast path
- Fully specified → stages compressed; commit at DO. P3: all decision branches priced — proceed+YES (0.87) revenue covers promo cost; proceed+NO (0.13) discount cost w/o pass; hold-budget-to-day-14 (option, priced); change-budget-now (rejected: no evidence). Forecast log entry: P = 0.87, [0.80, 0.92], prior 0.125, triggers set; rescored day 30.
### REVIEW — insight pass (S2, packet gate)
- I1: the weak prior makes the update decisive, but the blend-trap (50/50 → Brier 0.25) is the human error the Brier framing exposes — the residual, not the prior, sets the width.
- I2: the mapping is in-sample (fit on the same 24 campaigns) — 2.5 pp is mildly optimistic; the day-14 re-run is the cheapest hedge, priced as the m058 option.
### DECISION PACKET
- Conclusion: P(final > 25%) = 0.87, range [0.80, 0.92]; proceed with plan, no budget change; day-14 checkpoint; log entry for day-30 rescore.
- Status: SOLVED (exact arithmetic on fully-specified inputs; forecast resolves day 30). Assumptions: mapping holds; residual Gaussian 2.5 pp; class comparable.
- Evidence: 27.8 pp prediction; Φ(1.12) ≈ 0.87; scenario band [0.25, 0.87]; flip point 15.9%; Brier 0.017 vs prior 0.77.
- Alternatives: point prediction 27.8 (unscoreable, rejected); static prior 0.125 (Brier 0.77, rejected); prior-blend 0.5 (Brier 0.25, rejected).
- Uncertainty: residual sd (in-sample optimism 5 pp → 0.71); mapping slope drift → 0.25. Risks: promo-stack override; copycat discount; day-14 < 15%.
## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | both deliver the scoreable 0.87 forecast the rubric demands |
| Logical Validity | 5 | 5 | Tie | identical arithmetic; Φ(1.12) ≈ 0.87 both ways |
| Coherence & Structure | 4 | 5 | AI | routed trace: outside-view-first pass, dual-route, packet; human linear but tight |
| Depth of Reasoning | 5 | 5 | Tie | human's decomposition is the craft; AI adds scenario band + flip point + in-sample flag |
| Efficiency | 5 | 5 | Tie | closed-scope fast path keeps the routed run one-pass |
| Handling of Uncertainty | 5 | 5 | Tie | human full posterior; AI adds scenario-robust range and threshold flip |
| Insight / Non-obviousness | 4.5 | 5 | AI | flip-point calibration of the revision rule; in-sample optimism; blend-trap Brier; day-14 option |
| Overall Quality | 4.9 | 5 | AI | closes v5's ordering gap (outside view first) and adds scenario machinery the baseline lacked |

Winner: AI (narrow). Why: the routed m008 pass forced the outside view FIRST (v5's ordering gap that cost the human win) and added what the baseline only implied — a likelihood-scenario posterior band, a calibrated threshold-flip point that makes the revision rule concrete, and the in-sample-mapping provenance flag; the m058 option pass prices the day-14 checkpoint the baseline recommended but did not price.
