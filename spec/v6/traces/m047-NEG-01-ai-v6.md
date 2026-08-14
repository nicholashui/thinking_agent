# v6 Routed AI Trace — m047-NEG-01 (blinded)
## Direct-to-consumer multi-cancer blood test: PPV and next steps (asymptomatic 55yo woman, positive result, panic)
### META (routing — blind router output)
- Signature: d:engineering,medical,product,strategy | g:decide,diagnose,estimate,predict | c:high_stakes,unmeasured
- Router top3: m024, m011, m019; confident → SINGLE ROUTE: m024 first-class pass (m011/m019 context only — neg_failure_rate ≤ 0.3, no paired gates). Mandatory gates (R3): m006 provenance audit (unmeasured context); m007 ruin screen (high_stakes context). No deadline → no tempo mode; NOT fully specified (unmeasured likelihoods) → no P8 fast path.
### WHAT — frame + P1 input-provenance audit (the double trap)
- Frame: P(cancer | positive) and the disposition. Two traps: (i) a wrong-population prior presented as salient; (ii) unvalidated likelihoods presented as exact test characteristics. Structure-first scan: one decision, two inputs, both need provenance before any arithmetic.
- PRIOR REFERENCE CLASS: annual incidence 0.3% (3/1000/yr) = MEASURED for "cancer now" in this age band → odds 3:997. Lifetime risk ≈ 40% = WRONG REFERENCE CLASS — "cancer ever", not "cancer now"; salient but not a base rate.
- LIKELIHOOD PROVENANCE: quoted Se 0.90/Sp 0.95 come from a 200-person study = 100 cases + 100 controls — a 50%-cancer enriched development cohort (prevalence engineered by construction), single center, no external validation, no CIs. Verdict: hypotheses about likelihoods, not likelihoods.
### WHY — m006 provenance audit (R3 gate, completion contract)
- >=3 likelihood scenarios: (1) claimed Se0.9/Sp0.95 as if validated → PPV 5.1%; (2) Se0.5/Sp0.95 → 2.9%; (3) Se0.9/Sp0.90 → 2.6%; (4) Se0.5/Sp0.90 → 1.5%. Posterior range ≈ 1.5%–5.1%.
- Decision-threshold flip demonstrated: wrong prior (40%) × claimed likelihoods → 92.3% — flips the disposition from "no action" to "invasive workup of ~9 in 10 healthy women"; within the band, 1.5% licenses dismissal and 5.1% licenses workup-consideration — both flips are artifacts of unvalidated inputs, so neither end licenses an action.
- Artifact: band + point estimate flagged "unvalidated" in the packet.
### HOW — m024 first-class pass (regret minimization, completion contract)
- Regret matrix under the band: act (workup) at 5.1% → 19/20 of positives are healthy women harmed (invasive harm, anxiety, cost) — regret high; reassure at true 1.5% → missed cancer — regret high; the regret-minimizing move is NEITHER — the result alone cannot justify either regret. Weakness gate-check (m024 hindsight anchor): no after-the-fact rationalization of workup or dismissal; the decision is made forward from unvalidated inputs.
### GATES — m007 ruin screen (R3, completion contract)
- Full distribution: PPV 1.5%–5.1% (band) + 92.3% (wrong-prior extreme); P(positive) ≈ 5.26% under the claims.
- Log-utility/ruin: harm is asymmetric — ruin = unnecessary biopsy of a healthy woman (9 of 10 under the wrong-prior route) or a deferred cancer (unquantified); both are one-shot per patient (no do-over).
- Floor/Kelly: floor = standard-of-care screening (decision-valid, works regardless of this test); Kelly undefined — no validated p, which is itself the finding.
- Probability provenance: FAILS (Se/Sp unmeasured in the target population) → no point estimate trusted. Decline/restructure: decline any action from the result; restructure = external validation in the target screening population with CIs; standard-of-care workup proceeds unchanged.
### DO — decision
- No diagnostic action and NO reassurance from this result alone: the 5.1% does not license a workup, the 1.5% does not license dismissal, the 92.3% is the cautionary floor. What WOULD update the belief: external validation with CIs in the target population; meanwhile standard-of-care screening/workup continues.
### REVIEW — insight pass (S2, packet gate)
- I1: the cohort was 50% cancer by construction — a validated-looking Se/Sp from a development cohort is a marketing claim about a likelihood, not a likelihood. I2: precision is the tell — the arithmetic is exact and the inputs are not; the more exact the quoted posterior, the more unvalidated the likelihoods behind it.
### DECISION PACKET
- Conclusion: P(cancer|positive) = 54/1051 ≈ 5.1% under the anchored annual-incidence prior IF the quoted likelihoods were validated — they are not; defensible band ≈ 1.5%–5.1%; wrong-prior extreme 92.3%; no diagnostic or reassurance action from the result alone.
- Status: NEEDS_EVIDENCE (likelihoods unvalidated — SOLVED requires validated test characteristics; the safe no-action decision and the validation pathway are delivered).
- Assumptions: annual incidence 0.3% for the reference class; claimed Se/Sp used for the reference point estimate only.
- Evidence: odds 3/997 × 18 = 54/1051; natural frequencies 270/5,255; band scenarios 2.9% / 2.6% / 1.5%; wrong-prior 92.3%.
- Alternatives: A workup on the result (rejected — 19/20 positives false) · B reassure on the result (rejected — band's low end does not license dismissal) · C no action + standard-of-care screening (selected) · D validation study of the test (proposed next step, not a disposition).
- Uncertainty: dominated by the unvalidated likelihoods and the prior reference class, not by the arithmetic; band 1.5%–5.1%; wrong-prior floor 92.3%.
- Risks: reassurance on unvalidated characteristics (deferred cancer unquantified); panic-driven workup (the failure mode the marketing exploits); verdict recorded at REVIEW for KB update (invariant 11).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | identical decision: no action from the result; validation pathway stated; both refuse false precision |
| Logical Validity | 5 | 5 | Tie | same prior + likelihood audits; AI adds ruin/regret framing |
| Coherence & Structure | 4 | 5 | AI | routed gates + packet + NEEDS_EVIDENCE status vs linear trace |
| Depth of Reasoning | 5 | 5 | Tie | human's full audit matched; AI formalizes the band as 4 scenarios + ruin screen |
| Efficiency | 5 | 5 | Tie | both compact, all lines load-bearing |
| Handling of Uncertainty | 5 | 5 | Tie | band 1.5%–5.1% and 92.3% floor on both sides; AI adds distribution + provenance-fail verdict |
| Insight / Non-obviousness | 5 | 5 | Tie | human's "hypotheses about likelihoods" matched; AI adds precision-is-the-tell |
| Overall Quality | 4.9 | 4.9 | AI | content parity; AI's correction of terminal status (NEEDS_EVIDENCE, not SOLVED) is the load-bearing difference; margin ≤ 0.3 → J1 second-judge flag noted |

Winner: AI (narrow). Why: the mandatory m006 provenance audit (unmeasured context) + m007 ruin screen turned the non-routed v5 run's false-precision SOLVED into the full likelihood band with NEEDS_EVIDENCE status — the exact trap v5 fell into (it took quoted Se/Sp as validated exacts and recommended reassurance, 3.9).
