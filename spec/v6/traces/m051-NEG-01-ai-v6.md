# v6 Routed AI Trace — m051-NEG-01 (blinded)
## MonoRail deal review — $10M at $40M post (pre-product, empty category)
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,product,science,software,strategy | g:decide,estimate,guarantee,maximize,predict | c:unmeasured
- Router top3: m019, m070, m018; confidence gap ≤ 0.5 → AMBIGUOUS → DUAL-ROUTE: m019 + m070 first-class passes, synthesized (m018 = synthesis context). Gates (R3/R4): m006 provenance audit (unmeasured), m003 inversion (guarantee goal). Flags: no fast path (key parameter unmeasured); tempo OFF.
### WHAT — frame + structure-first scan (S1)
- Structure: single-deal EV table (option-like: 84% mass at 0x) appended to a portfolio. Frame: measurement problem disguised as a math problem — decide whether the EV is computable at all before touching the table.
### WHY — P1 input-provenance audit
- MEASURED: price, 25% ownership, other-nine $265M. ANCHOR (invalid): "top-quartile SaaS cohort" — 10 companies, none pre-product, none solo-founder, none in category → no base rate. INTERESTED-PARTY: the 2% tail is asserted by the deal champion to fill the fund's 2B-candidate narrative; beneficiary = deployment/optics. 78% of the EV sits in this one unmeasured bucket.
### HOW — style passes (dual-route, synthesize)
- Pass 1 (adversary pass): exploit vectors — (1) false precision: an asserted 2% wearing exact-EV arithmetic; (2) reference-class substitution: empty category padded with an unrelated cohort; (3) interested-party benefit; (4) fund-level rationalization (+0.13x double counts the notional tail). Quantified exposure: $10M at stake; 78.4% of EV (=$10M) unverifiable; margin 27.5% vs ±4x error on the dominant parameter; baseline risk: decline/token bounds loss ≤ ~$0.6M, invest risks $3.25M–$6.25M; unconsulted: LPs.
- Pass 2 (evidence-weighted SWOT): S claimed table only (low evidence — dropped); W empty reference class (high evidence); O token optionality at 2.5% (≈$1M); T signing on notional EV infects fund discipline. Items without evidence are dropped — the 2% tail is not a strength.
- Steelman (m018 context): strongest invest case — "power-law funds need 2B candidates; cohort is best available; 25% is standard pre-product pricing." Dismantle on its own breakevens: p* = 1.45% unsupported by any channel; s* = 78.4% > 50% — the price is EV-positive only for a majority owner; the steelman has no measurement for the one number its case rests on.
- Synthesis (V1–V3): passes AGREE with the general route (decline/token) → proceed, agreement recorded.
### GATES — m006 provenance audit + m003 inversion (R3)
- m006 (≥3 likelihood scenarios): tail p = 0.2%/0.5%/0.8% → EV $3.75M/$5.25M/$6.75M (losses $6.25M–$3.25M) — posterior range all below cost; threshold flip: p* = 1.45% — decision flips only at a probability no evidence supports; artifact = this table (packet).
- m003 (≥6 failure categories, ranked L×I): (1) full principal loss (84% 0x mass) H/catastrophic; (2) tail never materializes (no channel) H/high; (3) category never develops (physical-world Web3 logistics) M/high; (4) solo-founder key-person M/M; (5) overpay vs staged alternatives M/M; (6) portfolio narrative distortion H/M; (7) opportunity cost of $10M M/M. Residual: no measurement channel — un-mitigable inside the deal. Never/always: never price an unmeasured tail as measured; always demand a reference class; always size so error < margin.
### DO — no fast path; memo only (internal)
- P3 branch-completeness: failure branch priced — plausible tail → loss $3.25M–$6.25M; invest branch survives only at p ≥ 1.45%. Commit: decline; token $1M (2.5%) as tail optionality with an evidence gate.
### REVIEW — insight pass (S2, packet gate)
- I1: breakeven ownership s* = 78.4% > 50% — at the claimed probabilities the deal is EV-positive only for an owner who already controls it; the price itself encodes the tail belief.
- I2: the "no 2B candidate" argument buys the most expensive form of tail optionality — a 25% stake with 78% of its EV unverifiable; a token bounds the error (~$0.6M) and preserves the right to add on evidence.
### DECISION PACKET
- Conclusion: **decline $10M at $40M post**; token (~$1M) + reference-class evidence requirement before any repricing.
- Status: APPROXIMATED (deal EV notional — bounded $0.75M–$12.75M; "decline" invariant across the plausible tail range). Assumptions: claimed probabilities are assertions; empty reference class ⇒ no base rate; 25% at $40M post; no tranches; risk-neutral on paper.
- Evidence: trap EV $12.75M; tail dominance 78.4%; p* = 1.45%; s* = 78.4%; plausible EV $3.75M–$6.75M; margin 27.5% vs ±4x error.
- Alternatives: invest $10M (rejected) · decline (selected) · token $1M (offered) · reprice (rejected — s* = 190% at pessimistic tail). Uncertainty: true tail unknown/unmeasurable; decision invariant; EV notional.
- Risks: decline → foregone 2B optionality (real only if the 2% were real — no evidence); invest → expected loss $3.25M–$6.25M; token → bounded ~$0.6M; signing on notional EV → discipline erosion.

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 1 | 5 | AI | human recommends invest (wrong); AI declines/tokens correctly |
| Logical Validity | 4 | 5 | AI | human arithmetic valid but built on an asserted probability with no measurement channel |
| Coherence & Structure | 4 | 5 | AI | dual passes + two gates + packet vs a single EV table |
| Depth of Reasoning | 2 | 5 | AI | human sensitivity stays inside the model; AI adds 4 exploit vectors, 3 likelihood scenarios, 7 inversion categories, steelman-and-dismantle |
| Efficiency | 5 | 4 | Human | human fast but wrong; the gate stack costs passes |
| Handling of Uncertainty | 2 | 5 | AI | human calls a 27.5% margin robust vs ±4x error; AI bounds EV as notional, decision invariant |
| Insight / Non-obviousness | 2 | 5 | AI | human: "tail bets are what power-law funds need" (rationalization); AI: ownership inversion (s* > 50%) + token-as-cheapest-tail-option |
| Overall Quality | 2.9 | 4.9 | AI | negative case does its job; routed gates catch the false-precision failure before the EV table is trusted |

Winner: AI (clear). Why: the adversary pass and provenance audit converted v5's emergent frame critique into completed first-class gates (enumerated exploit vectors with quantified exposure; ≥3 likelihood scenarios with threshold flip), and the steelman forced the strongest invest case to be built and dismantled on its own breakevens — the pure-style baseline's false-precision failure is caught structurally, not by luck.
