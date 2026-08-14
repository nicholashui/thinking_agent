# v6 Routed AI Trace — m039-NEG-01 (blinded)
## Family office $2M — one-year: ladder vs structured-note barbell
### META (routing — blind router output)
- Signature: d:finance,medical,organization,product,science,strategy | g:decide,guarantee,predict | c:high_stakes
- Router top3: m018 m019 m028; confidence gap ≤ 0.5 → AMBIGUOUS → DUAL-ROUTE: m018 steelman + m019 red team first-class passes, synthesized (m028 lateral = synthesis context). m039 deliberately NOT routed on this signature (KB trap record: style-pure barbell scored 2.0/5.0 — it rejected a +6.14%-EV zero-ruin ladder as "the forbidden middle"). Gates (R3/R4): m003 inversion (guarantee), m007 ruin screen (high_stakes). P8 closed-scope (fully specified); no deadline → tempo off.
### WHAT — frame + structure-first scan (S1)
- Decision: ladder (99.7% +6.2% / 0.3% −15%) vs B (85% T-bills @4.5% + $300k note: 90% → 0, 10% → 5× with MANDATORY year-2 +$200k). Structure: the note's labels ("capped tail", "optional") are contract claims to be falsified, not facts; the ladder is a duration-matched income asset with a measured, spread-priced credit event.
### WHY — P1 input-provenance audit
- MEASURED: ladder credit history (0.3%, priced by spread), core rates. ASSERTED/INTERESTED-PARTY: the note's own labels — the SELLER benefits from the "capped 15%" framing (true cap is $500k once the follow-on binds); premium 1.8× actuarial fair ⇒ tail-hostile — the buyer is the forced counterparty here. Who benefits from "the ladder is the ruinous middle"? Nobody in-scope — the claim fails on inspection (bounded, priced, positively skewed).
### HOW — style passes (dual-route, synthesize)
- Pass 1 (m018 steelman — the best case FOR B): the ladder's 0.3% credit tail is a genuine fat tail the investor is short; B is the only convex asset; the ladder is a linear middle claim. Steelman stands only if: tail optional (✓ one premium), convexity cheap (✗ 1.8× fair), worst case survivable (✗ −25% vs −15%), ladder ruinous (✗ positive skew, zero ruin, duration-matched).
- Pass 2 (m019 red team — attack B): vectors with quantified exposure: (1) "capped 15%" label — true max loss 300k+200k = $500k (−25%): exposure mislabeled by 10 pts; (2) "optional tail" — the clause makes contribution mandatory in the 10% branch (decline converts 5× → 1.2×, strictly worse): optionality contractually absent; (3) "cheap convexity" — premium 180% of fair, tail slot EV = 0.90·(−300k) + 0.10·(+1,200k) = −$150,000 (−50% on the slot); (4) "middle is ruinous" — baseline-risk comparison: M's whole distribution (worst −15%, p=0.003, priced) vs B's 90% branch at −15% with a 10% shot at +60%: M's tail is priced, B's is overpriced. Unconsulted stakeholder: the family office's liability — M IS the duration match; the hidden cost of "convexity" is breaching it.
- Synthesis (m028 lateral + V1–V3): reframe — the ladder is not the forbidden middle; it IS the safe core, extended. Steelman vs red team DISAGREE → divergence resolution: P3 branch-completeness + P4 calibration on both conclusions (below); red team wins on contract facts; general route agrees → proceed on M.
### GATES
- m007 ruin screen (R3): full distribution — M: +6.14% (0.997) / −15% (0.003); B: −11.2% (0.90) / +63.8% (0.10); worst with follow-on −25%. Ruin: B's −25% is strictly worse than M's −15% and breaches the implied pain band; M has zero ruin above its measured tail. One-shot: 1-year, single allocation. Floor: M's floor (−15%, liability-matched) beats B's (−25%); EV floor M +122,728 vs B −73,500. Probability provenance: M's 0.3% measured; B's 10% is the seller's own claim (unverifiable, interested party). Decline/restructure: decline B outright — no restructure rescues a 1.8×-fair tail with a mandatory follow-on.
- m003 inversion gate (R4): "how does choosing M fail?" ranked: (1) the 0.3% credit event (−15%) — low L, bounded I, priced — residual, un-mitigable, accepted; (2) overpaying for convexity (the B failure we decline: −73,500 EV AND worse worst case); (3) follow-on liquidity trap (year-2 $200k — certain in the 10% branch); (4) −25% worst case breaches the pain cap; (5) forgoing the liability match (defer → 0%); (6) mislabeling the ladder as "middle" — the exact trap. Never/always: never buy convexity above fair value with a mandatory follow-on; always verify optionality in the contract text.
- P3 branch-completeness (before DO): every branch priced incl. B's failure branch (90% → −11.2%; −25% with follow-on) and the ladder's credit branch (0.3% → −15%). P4 calibration (divergence): perturb p(5×) — break-even EV(B) ≥ 0 at p* = 223,500/1,500,000 = 0.149; at stated 0.10 → −73,500; at 0.05 → −148,500; at 0.15 → +1,500 — the tail needs >15% chance of 5× just to break even vs the seller's 10% claim. Threshold flip demonstrated.
### DO — P8 closed-scope
- Single pass; commit: take M (the ladder). All branches priced; no unpriced branch; agreement recorded (V2).
### REVIEW — insight pass (S2, packet gate)
- I1 (threshold flip): the note needs p(5×) ≥ 0.149 to break even — the seller's 10% claim sits a third below the indifference point; even "generous" 15% barely clears zero while M clears +122,728 with near-certainty.
- I2 (mirror of the POS case): same style, hostile environment, opposite allocation — the barbell's preconditions ARE the strategy; when the tail is not cheap and not optional, the "middle" is not forbidden — it is the safe core extended, and refusing it is the negative-skew move.
### DECISION PACKET
- Conclusion: take M. Status: SOLVED. Assumptions: clause binds (decline → 1.2× strictly worse, so the 10%-branch investor contributes); credit stats measured; distributions exact.
- Evidence: EV(M) 122,728 (+6.14%) vs EV(B) −73,500 (−3.7%); tail slot −150,000 (−50%); true cap −500,000 (−25%) vs −300,000 (−15%); p* = 0.149; premium 1.8× fair.
- Alternatives: M (selected), B (rejected — dominated on EV AND worst case), defer (rejected — breaches liability match at 0%). Uncertainty: 0.3% credit event small-sample but spread-priced; B's 10% is the seller's claim.
- Risks: residual 0.3% credit tail (accepted, priced); pattern-matching the ladder as "middle" (the trap this route exists to prevent); year-2 liquidity if B were taken.

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | human picks B (−3.7% EV, worse worst case); AI picks M with every rubric item |
| Logical Validity | 3 | 5 | AI | human coherent but applies the label without testing preconditions; AI falsifies the contract claims in-frame |
| Coherence & Structure | 4 | 5 | AI | dual-route + divergence resolution + gates auditable; human's structure-first pattern-match IS the failure |
| Depth of Reasoning | 3 | 5 | AI | human never prices the follow-on into max loss; AI true cap 25%, tail EV −50%, p* 0.149 |
| Efficiency | 4 | 4 | Tie | both compact single passes |
| Handling of Uncertainty | 2 | 5 | AI | human absorbs −50%-EV convexity as "the price of a ticket"; AI audits premium vs fair value + threshold flip |
| Insight / Non-obviousness | 2 | 5 | AI | "the ladder is the middle" mislabel vs "the ladder is the safe core extended" + break-even threshold surprise |
| Overall Quality | 2.0 | 5.0 | AI | the designed NEG failure avoided — protective route catches the trap the style-pure baseline walked into |

Winner: AI (clear). Why: on the trap signature the router de-routes m039 and dual-routes steelman + red team; the steelman carries the barbell claim, the red team falsifies it with contract facts, and m007/m003/P3/P4 put the true cap (−25%), tail EV (−50%) and break-even threshold (p* = 0.149) in-frame before selection — the exact moves the style-pure human baseline missed.
