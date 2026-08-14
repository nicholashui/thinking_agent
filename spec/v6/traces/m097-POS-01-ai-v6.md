# v6 Routed AI Trace — m097-POS-01 (blinded)
## Project Comet: plan-of-record (duration, budget, contract) vs a 9-month/$1.5M bottom-up plan
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,product,software,supply | g:diagnose,estimate,predict | c:(none)
- Router top3: m044, m097, m011; confidence gap ≤ 0.5 → AMBIGUOUS → DUAL-ROUTE: m044 + m097 first-class passes, m011 synthesis context. Gates (R3): none fire (context empty); R4: no guarantee goal → no inversion prepend. Flags: P8 ON (fully specified — all statistics given, memo-only brief); S1 scan (finance/org/supply); tempo off (no deadline).
### WHAT — frame + structure-first scan (S1)
- Decision structure: a forecast hidden inside a plan — one-point promise (9 mo/$1.5M) vs a 60-sample base-rate distribution; the contract is the mechanism that lets the two negotiate. Deliverable: plan-of-record number + contract + reasoning.
### WHY — P1 input-provenance audit
- MEASURED (trust): the 60-migration post-mortem DB — the firm's own measurements. INTERESTED PARTIES: Marta (account director — the 9-month story closes the LOI; her incentive is deal shape, not duration truth), vendor commitments (promises from parties who win 14 engineers of work), "we did Aurora in 8 months" (anecdote chosen for the sales story). DECLARED: DB scope family matches Comet on every deciding feature (≥30M records, ≥10 integrations, compliance) — a checkable class-membership claim.
### HOW — style passes (dual-route)
- Pass A (m044 multi-perspective): the bank's real need is a plan-of-record that survives ITS audit committee — a tail-false 9-month promise becomes their risk, not a gift; engineers staff against 21-month reality either way; vendor commitments are the weakest evidence in the room (the forecast's most interested parties).
- Pass B (outside-view reference-class pass — completion contract): reference class NAMED = the 60 comparable legacy-to-modern migrations (≥30M records, ≥10 integrations, 12 vendors, 8 years); base-rate distribution STATED — median 21, mean 22.5 (σ 7.5), 10/90 = 14/31, range 11–42; inside/outside SEPARATED — the bottom-up plan is refused as a forecasting instrument (execution work, never a promise); planning-fallacy KILLED — estimates in this class average 1.8× below actual, the plan sits at (9−22.5)/7.5 ≈ −1.8σ ≈ 3rd percentile ≡ the empirical 2/60, Aurora (8 mo) is one of those two — a tail event, not a precedent; class-selection note (weakness gate) — structural membership met on every feature, "we're better" bounded by the team's own ceiling (Aurora: 8 months, once), and the 1.8× ratio confirms the class (estimates cluster 1.8× below center) instead of licensing factor-on-anchor (16 mo still misses the center); sanity check: if Comet were typical, it takes 21 months — the plan says 9; either Comet is special (evidence, please) or the plan is.
- Synthesis (m011): migration = stock/flow system — 40M records move at a rate gated by integrations and compliance sign-off; the class distribution is that system's realized throughput across 12 vendors; the 9-month plan implies a flow rate the system achieved in 2/60 projects.
- Divergence (V1–V3): style passes and general route (P10 — DB is the ordering authority) AGREE on class-center ≈21 months → proceed, agreement recorded.
### GATES — R3: none fire; weakness gate: class-selection test passed (Pass B) — the only adjustment the data supports is the team's own ceiling
### DO — P8 fast path + P3 branch-completeness
- P3 priced before commit: (a) fixed 9/$1.5M — at 21-month reality the vendor eats ≈2.3× overrun → contract death (failure branch); (b) factor band 16 mo/$2.7M — still below class center, under-capitalized; (c) class-banded contract 14–31 mo / ≈$3.5–3.8M (burn $1.5M/9 mo ≈ $167K/mo) with phase gates + hard month-14 checkpoint (kill/scope-trim if not tracking the class's early tail) — SELECTED; (d) no-quote loses the LOI.
- Commit: plan-of-record = median ≈21 mo, 80% ≈14–31, budget ≈$3.5–3.8M, range-banded contract; client expectation reset at the class — the LOI is non-binding, so the honest reset is free this quarter.
### REVIEW — insight pass (S2, packet gate)
- I1: the one success story is the worst data point in the room — Aurora is the base rate's own tail (2/60), cited as if it were the norm.
- I2: the 9-month plan is not "optimistic" — it is a 3–5% claim; a plan 1.8× below class center is this class's steady state of underestimation; the outside view governs what we promise, the inside plan governs how we work. Verdict recorded at REVIEW for KB update (invariant 11).
### DECISION PACKET
- Conclusion: forecast from the class — median ≈21 mo; 80% ≈14–31; P(≤9 mo) ≈ 3–5% (2/60); budget ≈$3.5–3.8M; range-banded contract with month-14 gate; Aurora = tail, not precedent.
- Status: SOLVED (decision brief; every number checkable against the given database; memo-only).
- Assumptions: DB representative of Comet's scope family; constant burn ≈$167K/mo; client accepts a range; no scope change.
- Evidence: DB n=60 — median 21, mean 22.5, σ 7.5, 10/90 = 14/31, range 11–42; 1.8× estimate-to-actual; 2/60 sub-12-month; plan 9 mo/$1.5M.
- Alternatives: fixed 9/$1.5M (rejected — failure branch priced) · factor band 16 mo (rejected — anchor survives) · external review (rejected — same evidence genre) · class contract (selected).
- Uncertainty: σ 7.5 spread; team-vs-class quality unmeasured (adjustment bounded by Aurora ceiling); class tail real (2/60).
- Risks: client insists on 9 mo (mitigate: range floor + month-14 gate) · under-quote against class center (mitigated: class-banded price) · Aurora-style speed (option value, not promise).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | identical plan-of-record: median 21, 80% 14–31, $3.5–3.8M, month-14 gate, range-banded |
| Logical Validity | 5 | 5 | Tie | same percentile placement (≈3rd pct ≡ 2/60) and sanity check; no fudge-factor adjustment either side |
| Coherence & Structure | 4 | 5 | AI | pure linear trace vs routed dual pass + gate + packet |
| Depth of Reasoning | 5 | 5 | Tie | human: Aurora-as-tail + bounded adjustment; AI adds P1 provenance (Marta/vendors) + class-selection test |
| Efficiency | 5 | 4.5 | Human | the pure style is one move — the class; the v6 gate stack costs lines, each pays |
| Handling of Uncertainty | 5 | 5 | Tie | distribution band + percentile + bounded adjustment on both sides |
| Insight / Non-obviousness | 5 | 5 | Tie | "worst data point in the room" matched; AI adds free-reset-this-quarter + plan-is-not-promise |
| Overall Quality | 4.9 | 4.9 | Tie | content parity on the reference answer; complementary strengths (human purity, AI completeness) |

Winner: Tie (roughly equal — complementary).
Why: the routed outside-view pass lands every reference-answer element first-pass — the non-routed v5 AI instead factor-calibrated the anchor (16 mo, 3.6 vs 4.9) and missed the percentile/Aurora analysis; v6 closes that gap to parity, adding provenance and the weakness gate at a small efficiency cost.
