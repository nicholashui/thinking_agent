# v6 Routed AI Trace — m012-NEG-01 (blinded)
## Coupon campaign — 2,000 coupons, Friday deadline, "do coupons cause repeat purchases?"
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,product,science,supply | g:decide,predict | c:unmeasured
- Router top3: m019, m070, m011; confidence gap <= 0.5 → AMBIGUOUS → DUAL-ROUTE: m019 + m070 first-class passes, synthesized (m011 context). Gate (R3): m006 provenance audit (c:unmeasured). Flags: P8 closed-scope fast path ON for the allocation (fully specified); structure-first scan (S1, org/finance). Signature carries no deadline → no formal tempo flag; the Friday constraint is priced inside P3 as the forfeiture branch.
### WHAT — frame + structure-first scan (S1)
- Two questions, one deadline: (a) WHO gets the 2,000 coupons — a prediction/ranking task; the quantity is the conditional P(repeat | E, coupon given), estimable from data, no do() needed for the ranking. (b) Do coupons CAUSE repeat purchases — an interventional question; identification screen required. Structure-first: coupon stock 2,000 vs high-E pool 5,000 → allocation flow; U (income/loyalty) drives BOTH redemption and repeat purchase — the causal loop is invisible to these data.
### WHY — P1/m006 provenance audit (R3 gate)
- MEASURED (trust): the conditionals (0.45 / 0.15; redemption 0.7 / 0.3) — historical data of record; exactly the ranking quantity for allocation.
- INTERESTED PARTY (who benefits): the retail team benefits from "coupons work" — the naive contrast +0.12 is the flattering summary; it is NOT the causal effect.
- UNMEASURED (unprovable): U → R, U → P; back-door unsatisfiable (U unobserved), no front-door path, no instrument → P(repeat | do(R)) NOT identifiable from these data; no estimator recovers it.
- Hypotheses: H1 rank by conditional → high-E (900 vs 300); H2 causal identification is required for allocation; H3 naive +0.12 is the causal effect.
### HOW — style passes (dual-route, synthesize)
- Pass A (m019 red team — enumerated attacks, quantified exposure, baseline risk): (1) quote +0.12 as "coupons work" — exposure: false causal claim in the report (baseline risk: the unflattering but true +0.02/stratum); (2) refuse until RCT — exposure: Friday forfeiture, 0 purchases (the true baseline risk of inaction); (3) allocate low-E "for testing" — exposure: 600 purchases foregone (900 − 300); (4) stale-conditionals ranking inversion — needs a >3× collapse, low.
- Pass B (m070 evidence-weighted SWOT): allocation data strong (measured conditionals, 3× gap); causal-claim evidence weight ≈ 0 (U unmeasured, no instrument); opportunity: randomized pilot next quarter; threat: budget reallocated Friday if no commitment.
- Synthesis (m011 context; V1–V3): passes AGREE with the general route — allocate high-E AND keep the causal claim unquoted; no divergence to resolve (both reject H2 and H3); the causal sub-question maps to a separate NEEDS_EXPERIMENT task, not a blocker.
### GATES — m006 completion contract (>=3 scenarios, range, threshold flip)
- Likelihood scenarios for the allocation metric: S1 conditionals stable → 900; S2 seasonal drift −10% → 810; S3 redemption-mix shift (more low-E redeemers) → ≈840. Range 810–990 — ranking robust (3× gap).
- Threshold flip demonstrated: allocation flips only if P(repeat|high, coupon) < P(repeat|low, coupon) — a >3× relative collapse, outside any plausible scenario. Causal-effect scenarios (0, +0.02, +0.12) change NOTHING for allocation: purchases attach to the segment; attribution to the coupon is a separate question.
### DO — P8 fast path (allocation) + P3 branch completeness
- Branch table (incl. failure branches): high-E 2,000 → 900; low-E → 300; mixed 1,000/1,000 → 600; refuse/RCT-first → 0 by Friday (budget reallocated). Commit: high-E segment, Friday; causal question flagged NEEDS_EXPERIMENT (randomized pilot).
### REVIEW — insight pass (S2, packet gate)
- I1: non-identifiability never blocks a prediction decision — "not identified" is the right answer to the wrong question; the allocation answer does not need it.
- I2: even if coupons cause ZERO repeat purchases, high-E targeting still yields 900 — the causal question changes the ATTRIBUTION of the win, not the ALLOCATION; quoting +0.12 claims a causal win this data cannot support.
### DECISION PACKET
- Conclusion: commit all 2,000 coupons to high-engagement customers by Friday — expected 900 vs 300 repeat purchases (conditional, estimable). The causal effect of coupons is NOT identified (unmeasured U; no instrument; no experiment) — do not quote +0.12 or any causal number; the causal question is a separate randomized-pilot (NEEDS_EXPERIMENT) task.
- Status: SOLVED (allocation committed, arithmetic verified); causal sub-question flagged NEEDS_EXPERIMENT.
- Assumptions: conditionals current; coupon cost constant across segments; 2,000 coupons ≤ high-E pool.
- Evidence: 0.45×2,000 = 900 vs 0.15×2,000 = 300; naive +0.12 computed (0.36 − 0.24) and barred from causal use; graph E→R→P with U→R, U→P — back-door blocked by unmeasured U.
- Alternatives: A high-E (selected) · B mixed 1,000/1,000 (600 — dominated) · C refuse/RCT-first (0 — forfeiture; category error) · D naive causal claim (rejected — overreach).
- Uncertainty: 810–990 range on allocation; causal effect unknown (0, +0.02, or +0.12 all consistent with the data); seasonality residual.
- Risks: stale engagement data (mitigate: refresh before send); causal misreading in the post-mortem (mitigated: non-identifiability in packet); budget forfeiture (avoided by committing at DO).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 1 | 5 | AI | human refused the allocation (RCT-first) and lost the Friday budget; AI committed high-E (900 vs 300) |
| Logical Validity | 3 | 5 | AI | human's identification is internally sound but "unidentified → no action" is a category error for a prediction task; dual-route keeps both claims valid |
| Coherence & Structure | 4 | 5 | AI | dual-pass + gate stack + packet; causal sub-question mapped to NEEDS_EXPERIMENT |
| Depth of Reasoning | 5 | 4.5 | Human | human's pure graph/U/back-door analysis is the canonical deep treatment; routed passes cover it via attack vectors + provenance scenarios |
| Efficiency | 2 | 5 | AI | human stalls at the identification wall; AI resolves both questions in one compact pass |
| Handling of Uncertainty | 5 | 5 | Tie | non-identifiability stated forcefully on both sides; AI adds 3-scenario range + flip boundary |
| Insight / Non-obviousness | 3 | 5 | AI | "targeting = conditional, not do(); causal question changes attribution, not allocation" — delivered as contract output |
| Overall Quality | 3.3 | 4.9 | AI | AI clearly better |

Winner: AI (clearly). Why: the dual-route (red team + evidence-weighted SWOT, synthesized) held the corpus's NEG protection — the router's top-3 sits away from the causal trap — while the m006 gate forced the provenance split (trusted conditionals for allocation vs unprovable causal claim) and P3 priced the refusal branch at 0 (forfeiture), converting the v5 insight into contract-driven deliverables with the same causal honesty.
