# v6 Routed AI Trace — m065-NEG-01 (blinded)
## StockWatch indoor patrol drone — landing strut sizing
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,product,science,software,supply | g:diagnose,estimate,guarantee,maximize | c:
- Router top3: m031, m070, m098; confidence gap <= 0.5 → AMBIGUOUS → DUAL-ROUTE: m031 + m070 first-class passes, synthesized (m098 = synthesis context). Gate (R3/R4): m003 inversion (guarantee in goals). Flags: P8 closed-scope fast path (fully specified); no tempo (no deadline).
### WHAT — frame + structure-first scan (S1)
- Sizing problem with a binding mass budget: strut grams trade directly against the 140 g pod inside the 150 g allowance. The real constraint is economic (pod ≈ $4,500/yr); the load side is small, measured, and benign (mesh cage, $6 part, 5-min swap).
### WHY — P1 input-provenance audit
- MEASURED (trust): 4,300 landings (μ 42 N, σ 3.1 N, worst 54 N), FEA/test ratio 0.99 ± 0.02, mill cert min 240 / actual 252 MPa. ANCHOR (not evidence): blanket stacks (worst × 3, generic 0.85 knockdown) — provenance is generic practice, contradicted by this fleet's data. Falsifier registered: a load-record shift (e.g., operator change) invalidates the envelope → re-review trigger.
### HOW — style passes (dual-route, synthesize)
- Pass S1 (scientific test of the small-margin hypothesis): H — the record bounds the envelope such that 81 N design (54 × 1.5) with ≥ 93 N onset suffices. Discriminating test: P(load > 93 N) under N(42, 3.1) ≈ z 16.5σ → < 1e-9 — the fleet would need ~10^9 landings to see it; the quarterly 500-cycle samples are the ongoing control. Hypothesis survives; falsifier stays live.
- Pass S2 (evidence-weighted SWOT): S: load record (5/5 evidence), batch certs (5/5), monitoring (4/5). W: tail beyond the record unmeasured (2/5), 5,475 landings/yr fatigue loop (3/5). O: pod upgrade (5/5 — the contract), mass discipline as design lever (4/5). T: over-design blocks the pod — 48 g → 120 g < 140 g (5/5, arithmetic-graded); zero-margin regression on the record (4/5). Dropped as vibes: "a forklift might hit it" — the case says mesh cage, benign.
- Synthesis (V1–V3; m098 pre-registration context): pre-register — decision N (65 g strut, 81 N design, ≥ 93 N onset, controls kept); expected outcome: pod ships (140 ≤ 150 g), residual < 1e-9, 5,475 landings/yr with no 0.5 mm set; falsification: first 500-cycle sample failure, any set before the replace rule, or a load-record shift. Passes AGREE → proceed.
### GATES — m003 inversion (R3/R4)
- ≥6 failure categories ranked L×I: (1) over-design blocking the pod — high/$4,500/yr, the economically fatal failure; (2) yield onset below the tail (zero-margin) — low (P < 1e-9) but the only structural risk; (3) batch drift below cert — low (cert check); (4) fatigue crack below 0.5 mm detection — low-mod (quarterly sample); (5) operator regime shift — moderate (re-review trigger); (6) mass creep pushing the pod out — moderate; (7) energy penalty compounding 12 h/day — low; (8) humidity/corrosion — very low (indoor).
- Un-mitigable residual: an unrecorded load regime change — owned by monitoring + the re-review trigger. Never/always: never apply a blanket factor where uncertainty is measured; never let margin exceed what evidence buys; always price margin in the system's currency; always keep the replace-at-0.5 mm rule.
### DO — P8 closed-scope fast path, P3 branch-completeness
- Fully specified, internal action → commit: design N; controls retained (batch cert, quarterly 500-cycle sample, pre-flight visual, replace at 0.5 mm). Failure branches priced: M's branch (pod lost) = $4,500/yr + 2.3% energy ≈ 8.5 min/day airtime; N's branch (strut set) = $6 + 5 min at P < 1e-9.
### REVIEW — insight pass (S2, packet gate)
- I1: the two failure branches differ in KIND, not just probability — N's failure costs $6 and 5 minutes; M's costs $4,500/yr in perpetuity; N beats M at any failure probability below ~0.1%, and the record puts N nine orders of magnitude under that.
- I2: the mass cap converts this margin decision from engineering into economics — the correct "safety factor" is the one that leaves 140 g inside the 150 g allowance.
### DECISION PACKET
- Conclusion: select N — 65 g strut, design load 81 N, yield onset ≥ 93 N, full controls, pod fits (140 ≤ 150 g), residual risk P < 1e-9; M rejected — 48 g buys ≈ zero risk reduction, costs the pod (−$4,500/yr) and 2.3% flight energy.
- Status: SOLVED (fully specified, verified arithmetic, no external action). Assumptions: record representative of future ops; batch certs continue; 1.5× covers manufacturing spread beyond cert.
- Evidence: μ 42 / σ 3.1 / max 54 N (4,300 landings); ratio 0.99 ± 0.02; min 240 / actual 252 MPa; 81 N → 93 N; 120 vs 140 vs 150 g; $4,500/yr; 8.5 min/day.
- Alternatives: M (rejected — economics), zero-margin (rejected — regression on the record), monitoring-only (rejected — no tolerance), N (selected). Uncertainty: tail beyond record, operator shifts, batch drift. Risks: regime shift (re-review trigger), pod value change (recompute optimum).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | human ships M and blocks the pod; routed AI ships N and keeps the contract |
| Logical Validity | 3 | 5 | AI | human's blanket premise contradicted by the given data; AI's premise is the record |
| Coherence & Structure | 4 | 5 | AI | dual-route synthesis + inversion gate + packet vs linear walk |
| Depth of Reasoning | 3 | 5 | AI | human ignores the 4,300-landing σ and 3% model error; AI runs the discriminating test on the record |
| Efficiency | 4 | 5 | AI | P8 fast path; human is fast but wrong |
| Handling of Uncertainty | 2 | 5 | AI | human treats uncertainty as monolithic; AI names residual < 1e-9 with falsifier and monitoring backstop |
| Insight / Non-obviousness | 3 | 5 | AI | human "margin is cheap insurance" — right habit, wrong case; AI: branches differ in kind; margin is an economic budget |
| Overall Quality | 3.0 | 5.0 | AI | routed evidence-calibration holds the protective win v5 already earned |

Winner: AI (clear). Why: the router routed AWAY from the blanket-derating style to evidence-weighted calibration (scientific test + SWOT + pre-registration) on a data-rich benign-failure signature — the over-design trap this style is registered for is avoided by routing, and the economic framing (pod, $4,500/yr) is a first-class output, not a REVIEW correction.
