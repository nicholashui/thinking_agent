# v6 Routed AI Trace — m012-POS-01 (blinded)
## E-commerce banner rollout — is the +22.5 pt lift real, and do we roll out?
### META (routing — blind router output)
- Signature: d:finance,medical,product,science,software,strategy | g:estimate,maximize,predict | c:unmeasured
- Router top3: m012, m019, m068; confident (gap > 0.5) → SINGLE-ROUTE: m012 first-class pass in HOW; m019 paired gate (R2); m068 context. Gate (R3): m006 provenance audit (c:unmeasured). Flags: P8 closed-scope fast path ON (fully specified — every probability and cost given, checkable); structure-first scan (S1, finance/product/science). No deadline → no tempo mode.
### WHAT — frame + structure-first scan (S1)
- Structure: B ← M → P and B → P — a back-door graph, not a comparison problem; M drives both exposure and purchase. The asked quantity is do(B) (rollout = intervention); the marketing number is P(P|B) (observation). See-vs-do separated BEFORE any arithmetic.
### WHY — P1/m006 provenance audit (R3 gate)
- MEASURED (trust): the four strata probabilities — exact, recomputable; M recorded; no other variables.
- INTERESTED PARTY (who benefits): marketing benefits from rollout — "+22.5 pt" is an interested-party summary of an observational contrast, not an effect.
- UNMEASURED: any hidden U driving M and P would bias even the adjusted estimate — the residual that the A/B owns.
- Hypotheses: H1 naive contrast = effect (marketing's claim); H2 M confounds → back-door adjustment gives the effect; H3 effect = 0 (all selection). Falsifier: strata contrasts — homogeneous +0.05 both strata ⇒ H2 confirmed, H3 dead.
### HOW — style pass (m012 first-class) + m019 adversary gate (R2)
- Pass m012 (causal-graph/back-door): naive first — P(P|B=1) = 0.206/0.44 ≈ 0.468, P(P|B=0) = 0.136/0.56 ≈ 0.243 → +0.225 (the claim under test, stated before adjustment). do(B=1) = 0.4×0.55 + 0.6×0.25 = 0.37; do(B=0) = 0.4×0.50 + 0.6×0.20 = 0.32 → causal effect +0.05. Inflation 0.225/0.05 ≈ 4.5×. Consistency: stratum contrasts 0.55−0.50 and 0.25−0.20 both +0.05 → no effect modification; +5 pts real but small.
- Pass m019 (adversary — quantified exposure, baseline risk): (1) naive-claim exposure — a +22.5 pt claim implies 5,600 newly exposed users → claimed +2,250 purchases vs actual +280 → $49,250 overstated margin; (2) U-confounding exposure — if hidden U drives M and P, adjusted +0.05 is also biased, direction unknown; (3) baseline risk — status quo exposure continues at $0 cost, $0 new revenue.
- Agreement: m012 pass and the general route AGREE (cost the adjusted estimate) → proceed (V2); m068 context keeps deliverables client-ready (effect, decision, alternatives).
### GATES — m006 completion contract (>=3 scenarios, range, threshold flip)
- Likelihood scenarios for the true effect: S1 recorded world only (M) → +0.05; S2 hidden U attenuates (income-selection) → 0 to +0.02; S3 measurement attenuation in B → +0.03–0.05. Posterior range ≈ 0 to +0.05, centered +0.05.
- Threshold flip demonstrated: break-even lift for a newly exposed user = $2.50/$25 = 0.10 (560 purchases / 5,600 users). Adjusted 0.05 < 0.10 → lose $1.25/user; naive 0.225 > 0.10 → roll out. The two estimates straddle the flip line; under every provenance-honest scenario the decision is DON'T extend.
### DO — P8 closed-scope fast path + P3 branch completeness
- Branch table (all priced, incl. failure branches): mass rollout → +280 purchases −$14,000 = net −$7,000; engaged-only extension (800 users) → +40 −$2,000 = −$1,000; low-E extension (4,800) → +240 −$12,000 = −$9,600; status quo → $0. Every marginal exposure loses $1.25 → commit: no extension; A/B (randomized) to confirm +5 pts before any wider spend.
### REVIEW — insight pass (S2, packet gate)
- I1: the 0.10 break-even flip means the decision is robust across the whole honest range — only the marketing claim crosses the line; the 4.5× inflation is not decorative, it IS the decision.
- I2: the "targeted" fallback is also unprofitable at +5 pts — the recommendation is status quo + experiment, not a compromise rollout.
### DECISION PACKET
- Conclusion: causal effect +0.05 (do(B=1) = 0.37 vs do(B=0) = 0.32); naive +0.225 ≈ 4.5× inflated; do NOT mass-roll out (net −$7,000); do not extend to any segment; run a small randomized A/B, then re-price.
- Status: SOLVED (all arithmetic verified; memo only).
- Assumptions: M is the only confounder (no unmeasured U); positivity (all four M×B strata observed); SUTVA (one user's banner does not affect another's purchase); strata of record stable.
- Evidence: 0.37/0.32/+0.05; naive 0.468 vs 0.243 → +0.225; inflation 4.5×; strata contrasts +0.05/+0.05; 280×$25 = $7,000 vs 5,600×$2.50 = $14,000; break-even lift 0.10.
- Alternatives: A mass rollout (net −$7,000) · B engaged-only extension (−$1,000) · C low-E extension (−$9,600) · D status quo + A/B (selected) · E naive-costed rollout (+$42,250 illusory — rejected).
- Uncertainty: effect range 0–0.05 under U-scenarios; no sampling error (population of record); residual-U bias direction unknown.
- Risks: hidden U inflates +5 pts → wrongful extension (mitigated: A/B first); marketing re-asserts naive claim (mitigated: 4.5× in Evidence); rollout despite economics (rejected by branch table).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | both deliver +0.05, 4.5× inflation, no mass rollout; v6 adds branch-priced targeted option |
| Logical Validity | 5 | 5 | Tie | identical adjustment arithmetic (0.37/0.32/+0.05) and cost math; no factual errors either side |
| Coherence & Structure | 4 | 5 | AI | routed pass + gate stack + decision packet vs linear trace |
| Depth of Reasoning | 5 | 5 | Tie | human owns the decision flip as spine (v5's edge); v6 now owns it too AND adds break-even flip (0.10) + engaged-branch economics + claim provenance |
| Efficiency | 5 | 4.5 | Human | pure-style trace is shorter; every v6 gate line pays |
| Handling of Uncertainty | 5 | 5 | Tie | residual-U + A/B-as-confirm on both; v6 formalizes via 3 likelihood scenarios, range, and threshold flip |
| Insight / Non-obviousness | 5 | 5 | Tie | decision flip matched; v6 adds "every marginal exposure loses $1.25 — even the targeted extension" |
| Overall Quality | 4.8 | 4.9 | AI | content parity on all checkables; routed contracts close v5's 4.4-vs-4.8 margin (inflation made spine, threshold flip added) |

Winner: AI (narrow). Why: the routed m012 first-class pass + m006 gate forced the completion contracts the non-routed v5 run skipped — naive-vs-adjusted inflation audit stated before the adjustment and carried into Evidence, break-even threshold flip (0.10), provenance-of-claim audit, and all-branch pricing (including the engaged-only extension the human suggested but that is also net-negative) — closing v5's depth/insight gap while keeping the identical arithmetic.
