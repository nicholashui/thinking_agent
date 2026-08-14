# v6 Routed AI Trace — m038-POS-01 (blinded)
## pedestrian suspension bridge — design load under a stale ±30% survey
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,science | g:estimate,guarantee,maximize | c:∅
- Router top3: m002 m004 m014; confidence gap ≤ 0.5 → AMBIGUOUS → dual-route m002+m004 first-class, m014 third. Gates (R4): m003 inversion (guarantee). P8 closed-scope fast path (fully specified); no c:deadline → tempo off.
### WHAT — frame + structure-first scan (S1)
- Decision: design load L. Structure: one error-bearing estimate (official 40) × multiplicative error chain (surge × dynamic × material); the regulator floor 44 is a legal minimum, not a load basis; $760k budget vs ≈ $3.5M failure tail. The decisive object is the cushion — and the cushion's weakest link is its own inputs.
### WHY — P1 input-provenance audit
- MEASURED: official peak 40 ±30% (stale 15-yr mid-week sample); festival surge 1.6× (single event, never instrumented → n = 1); dynamic 1.3; material 1.1. ASSERTED: tourism growth +60% (operator-claimed); floor 44. WHO BENEFITS from a cheap design? The operator — the n=1 surge factor is adverse to cheapness, the tell it is real. Error is one-sided (surveys under-count crowds) → one-sided margin.
### HOW — style passes (dual-route, first-class)
- m002 (second-order): after 92 survives → plate yielding + 6-wk closure + ≈ $340k, and at surge 2.0 → deck yield ≈ $3.5M; after 115 survives → nothing. Pick the design whose downstream is boring.
- m004 (Occam): simplest model consistent with all evidence = the recorded 1.6× surge is real and repeatable; "the surge won't recur" is the complex claim and carries the burden. 44 already fails the simplest model (growth-adjusted normal ≈ 64).
- m014 (constraint): the binding constraint is the surge factor — one non-instrumented observation; cushioning it lifts the whole design; every other factor's error is tolerable.
- m038 pass (target-style contract): margin-quantified — flip-points: 44 flips at any festival (static ≈ 96); 92 flips if surge > 1.6, dynamics > 1.3, or material > 1.1 (each ≈ 2σ; joint ≈ 1%); 115 flips only at a joint 2σ+ miss. Chain 40 → 91 (multiplicative) → 115 (cushion the binding factor). Cost (115−40)/40 × $400k = $750k ≤ $760k. Over-conservatism check: 92→115 costs $230k and retires a $340k–3.5M one-sided tail — opportunity cost ≈ 15× smaller than the failure it retires; no derating — every factor evidence-backed, none blanket.
### GATES
- m003 inversion (R4): ranked categories — (1) floor-as-basis 44: high L, catastrophic I; (2) surge underestimated (n=1, ±25%): med L, catastrophic I; (3) crowd resonance at peak: med L, high I; (4) material batch shortfall: med L, med I; (5) cost overrun derates spec at construction: low L, high I; (6) regulator cost scrutiny: low L, med I. Residual: wind+festival joint 2σ miss (unmodeled; survivable at 115 with ≈ 24% reserve). Never: treat the estimate as truth; always: cushion the n=1 factor.
### DO — P8 closed-scope + P3 branch completeness
- Failure branch priced: 92 under a 93 kN/m² event → yield → ≈ $3.5M; 115 under the same event → 24% reserve. Style passes (115) vs general route (92-on-EV) DISAGREE → V3: P3+P4 on both — the general route's EV math (1% × $3.5M = $35k < $230k) treats the n=1 factor as a stable parameter; P1 showed it is not. Resolution: 115. Commit: design 115 kN/m².
### REVIEW — insight pass (S2, packet gate)
- I1: the binding uncertainty lives inside the margin — the design must cover the error in its own factors (surge ±25%), not just the nominal numbers; a sensitivity note is not a cushion.
- I2: the cushion is the cheapest item in the budget — $230k buys off a $340k–3.5M one-sided tail; EV that discounts it prices the wrong object.
### DECISION PACKET
- Conclusion: design 115 kN/m² (40 × 2.0 × 1.3 × 1.1), $750k ≤ $760k, ≈ 24% reserve at the 93 event. Status: SOLVED (design spec).
- Assumptions: growth +60% and surge bound ±25% asserted (P1-flagged); amplification at resonance only; no crowd-management change.
- Evidence: stale survey ±30%; recorded 1.6× surge; dynamic 1.3; material 1.1; flip-point table (44/92/115); tail $340k–3.5M vs cushion $230k.
- Alternatives: 44 (fails first festival) · 92 ($520k, EV-picked, yields at 93) · 115 (selected) · detuning retro (construction-phase option).
- Uncertainty: n=1 surge factor ±25%; wind-event coincidence; cost-model linearity. Risks: joint 2σ miss; cost overrun; regulator cost scrutiny.

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | both 115; survives 93 with reserve |
| Logical Validity | 5 | 5 | Tie | identical chain 40×1.6×1.3×1.1 → 115; no errors |
| Coherence & Structure | 4 | 5 | AI | routed passes + gates + packet auditable vs linear build-up |
| Depth of Reasoning | 5 | 5 | Tie | human cushions n=1 factor; v6 AI makes it structural (P1 + m003 + P3) |
| Efficiency | 4 | 4 | Tie | human 6 linear steps; AI dual-route + gates in one P8 pass, no repair |
| Handling of Uncertainty | 5 | 5 | Tie | one-sided margin both; AI adds measured-vs-asserted provenance |
| Insight / Non-obviousness | 5 | 5 | Tie | human: cushion the margin's own factors; AI: I1/I2 + constraint lens |
| Overall Quality | 4.7 | 4.9 | AI | v5 gap (EV-discounting the one-sided tail) closed in-frame |

Winner: AI (narrow). Why: the routed m038 pass makes "cushion the binding n=1 factor" load-bearing (flip-point table, P1 provenance, m003 categories, P3 failure price) where the v5 AI traded it away on EV grounds and lost to the 93 kN/m² event — same 115 design, now the only defensible one.
