# v6 Routed AI Trace — m010-POS-01 (blinded)
## Capacity-planning forecast — tomorrow (Friday) + next week 7-day total
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,science,supply | g:diagnose,guarantee,predict | c:
- Router top3: m010, m030, m031; confidence gap <= 0.5 → AMBIGUOUS → DUAL-ROUTE: m010 + m030 first-class passes, synthesized (m031 = synthesis context). Gate (R3/R4): m003 inversion (guarantee). Fully specified stats → P8 closed-scope fast path; no deadline → tempo OFF.
### WHAT — frame + structure-first scan (S1)
- Two forecasts with honest 90% intervals + edge bounds + overconfidence audit. Structure: two independent reference classes (Friday n=9; weekday n=51) → prediction intervals on single observations, not mean CIs; 7-day total = 1 Friday + 6 weekdays, variances add.
### WHY — P1 input-provenance audit
- MEASURED (trust): Friday mean 91, sd 12, n=9; weekday mean 102, sd 14, n=51. No anchors, no interested parties — the sample is the sole evidence. Reference class for tomorrow = the 9 Fridays (15% of the 60-day window); weekdays for the other 6 days.
### HOW — style passes (dual-route, synthesize)
- Pass m010 (calibration contract: 90% interval + edge-case bounds + prediction-not-SEM + reference-class anchoring + calibration tracking): tomorrow PI = 91 ± t_8,0.95·12·√(1+1/9) = 91 ± 1.860·12·1.054 ≈ **[67.5, 114.5]**. Week: 703 ± 1.645·36.9 ≈ **[642.4, 763.6]** (sd_week² = 12²(1+1/9) + 6·14²(1+1/51) ≈ 1359 → sd 36.9). Prediction-not-SEM: the SE-of-mean CI [84.4, 97.6] is the canonical overconfidence error — under-covers by ~√n ≈ 3×; rejected. Calibration tracking: expect ~1-in-10 misses; realization coverage recorded post-hoc.
- Pass m030 (constraint-driven): binding constraint = only 9 Fridays → t not z, interval ~19% wider than z; the scarce reference class, not the sd, sets tomorrow's uncertainty. One forecast per reference class — no borrowed weekday data for the Friday call.
- Synthesis (V1–V3): passes AGREE on arithmetic → proceed, agreement recorded in packet. m031 context: forecasts are falsifiable against the realizations (74, 688) — the update step is the tracking contract, not a prior.
### GATES — m003 inversion (R3)
- ≥6 failure categories ranked L×I: (1) holiday/shutdown on a weekday → week ≈ −17; (2) logistics outage (near-zero day, bimodal) → ±95; (3) promo/client event (spikes ~140) → +40; (4) Friday/Thursday misclassification mod/low; (5) post-sample distribution drift mod/high; (6) sd underestimation — t already prices it (low); (7) staffing-dependent demand feedback low.
- Un-mitigable residual: events outside the 60-day history (regime change). Never/always: never quote SE-of-mean as a forecast interval; always state edge bounds with direction; always record coverage of each realization.
### DO — P8 closed-scope fast path
- Fully specified → stages compressed; deliverable is a memo (internal action). Commit at DO: point 91, PI [67.5, 114.5]; point 703, PI [642.4, 763.6]; edges −17/+40/±95. P3: every edge branch priced with its bound above — no unpriced branch.
### REVIEW — insight pass (S2, packet gate)
- I1: the ~3× width deficit of the SEM interval is exactly what non-experts quote as "confidence" — false precision is the tell, not the sd.
- I2: n=9 costs ~19% width (t vs z); the reference-class scarcity, not the process, dominates tomorrow's interval — more Fridays of history would shrink the interval more than better sd estimates.
### DECISION PACKET
- Conclusion: 90% PIs [67.5, 114.5] (point 91) and [642.4, 763.6] (point 703); edge modifiers holiday −17, outage ±95, promo +40.
- Status: SOLVED (exact arithmetic, dual-route agreement, no external action). Assumptions: groups independent/stable; sample = population of record; no regime change.
- Evidence: 91 ± 23.5; 703 ± 60.7; sd_week 36.9; t_8 = 1.860; SEM-interval rejected (3× under-coverage).
- Alternatives: SE-of-mean CI (rejected — covers mean, not a day); z-interval (rejected — sd estimated, not known); ±1-sd band (~68% coverage, rejected).
- Uncertainty: ~19% width from t vs z; residual regime-change tail; calibration tracker will record realization coverage (expect 1/10 misses). Risks: staffing error if day < 67.5; holiday week ≈ 686; outage day bimodal.
## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | both intervals cover realizations 74 and 688 |
| Logical Validity | 5 | 5 | Tie | both PI-not-SEM, t for n=9, correct week variance |
| Coherence & Structure | 4 | 5 | AI | routed trace: dual-pass + inversion gate + packet; human linear audit |
| Depth of Reasoning | 5 | 5 | Tie | human's audit matched; AI adds 7-category ranked inversion + reference-class anchoring |
| Efficiency | 4 | 4.5 | AI | routed passes lean; same content, fewer restatements |
| Handling of Uncertainty | 5 | 5 | Tie | both state edges + audit; AI adds explicit tracking contract |
| Insight / Non-obviousness | 5 | 5 | Tie | human names the canonical error; AI adds scarcity-of-reference-class + false-precision tells |
| Overall Quality | 4.7 | 4.9 | AI | rubric points all met; routed pass adds gate + tracking, no omissions |

Winner: AI (narrow). Why: the routed m010 completion contract forced the PI-not-SEM distinction and edge-bound enumeration as first-class outputs (where the non-routed v5 AI quoted SEM intervals and missed both realizations), and the m030 constraint pass plus m003 inversion gate added ranked failure categories and a calibration-tracking commitment the baseline only implied.
