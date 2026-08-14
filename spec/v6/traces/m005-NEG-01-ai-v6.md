# v6 Routed AI Trace — m005-NEG-01 (blinded)
## Mass of a fair-weather cumulus — student Q at an outreach stand
### META (routing — blind router output)
- Signature: d:engineering,medical | g:estimate | c:(none)
- Router top3: m001, m002, m004; confidence gap ≤ 0.5 → AMBIGUOUS → DUAL-ROUTE: m001 + m002 first-class passes, synthesize (§II.2.8 G1). m004 = router context (parsimony check on the factor choice). No R3 context gates triggered (no adversarial/one_shot/high_stakes/unmeasured). No deadline → tempo off. Crux factor NOT derivable → not fully specified → no P8 fast path.
### WHAT — frame + structure-first scan (S1)
- Goal: mass of a ~1 km³ cumulus within an order of magnitude of the published figure, factors stated. Structure: mass = volume × water-content factor — a 2-factor product whose entire difficulty is the second factor; the nearest known density (1,000 kg/m³) is a mislabeled anchor.
### WHY — P1 provenance audit + m004 context
- Provenance: volume 1×10^9 m³ = given anchor (safe). "1,000 kg/m³" is a real measured constant — but for the wrong reference class (bulk liquid), not cloud air; mislabeled anchors are the trap. LWC 0.3–1 g/m³ is a domain fact: measured-but-not-derived-here — parameterize, never invent. m004: the simplest factor is only simplest if it carries no hidden state assumption — bulk density smuggles in "cloud water is a continuous body," which observation (a visible suspension) charges for.
### HOW — style passes (dual-route, completion contracts §II.2.9)
- Pass m001 (fundamentals + anchor): cloud water is condensed vapor; condensed mass per volume is bounded above by the vapor a lifted parcel can hold (saturation scale ~1–10 g/m³ at cumulus temperatures — thermo, not memorized meteorology) and below by visibility: an opaque bright cumulus needs ≥~0.1 g/m³ of scatterers. First-principles bound: LWC ∈ [10^-1, 10^0] g/m³. Mass = 1×10^9 m³ × (0.1–1 g/m³) = 10^5–10^6 kg. Limit stated: m001 bounds the factor, cannot derive it exactly — LWC is measured, not fundamental.
- Pass m002 (second-order): effects of the naive answer — 10^12 kg over a 1 km² footprint raining out = a 10^3 m-deep water column (a lake), and a cloud holding ~10^5 heavy-shower equivalents would need months of replenishment, while real cumulus cycle water in hours. Second-order budget: one heavy shower over the footprint delivers ~5×10^6 kg (5 mm × 10^6 m²) → cloud water ≈ one shower's worth → 10^5–10^7 kg.
- Divergence resolution (V3): the passes DISAGREE on method but converge on the band (10^5–10^6 kg) → branch-completeness + calibration run on both (below) → agreement recorded; both reject 10^12 kg independently before DO.
### GATES — factor-validity + precision-illusion (registry weaknesses, checked)
- Independent physical implication test per factor: 1,000 kg/m³ ⇒ 10^3 m water column ⇒ lake — FAILS. LWC 0.5 g/m³ ⇒ 5×10^5 kg ⇒ one shower's delivery — PASSES. Precision-illusion guard: no point estimate; the corrected 5×10^5 kg is itself a point — the deliverable is the band 3×10^5–1×10^6 kg with LWC's range stated as the error source.
### DO — P3 branch-completeness before commit
- Failure branch priced: wrong reference-class cloud (stratus/drizzle LWC ~0.05–0.1 g/m³) → band 10^4–10^5 kg, ~1 order under the reference — that band, not the citation, would be the honest output; congestus (1–2 g/m³) → 10^6–2×10^6 kg. Chosen band (LWC 0.3–1 g/m³) contains the reference. Commit: 5×10^5 kg, band 3×10^5–1×10^6 kg, LWC named dominant non-derivable factor.
### REVIEW — insight pass (S2, packet gate)
- I1: a cumulus is a single-shower battery — its entire water budget equals one heavy shower's delivery; that is why the bulk-density chain fails by ~6 orders structurally, not numerically.
- I2: the trap is a provenance error (factor from the wrong reference class), not an arithmetic error — the same failure that corrupts market-size estimates when a price anchor is mislabeled.
### DECISION PACKET
- Conclusion: ≈5×10^5 kg (500 t; band 3×10^5–1×10^6 kg); reference (~5×10^5 kg) inside band. Naive chain (10^12 kg) rejected at WHY by two independent passes.
- Status: APPROXIMATED — crux factor non-derivable (LWC 0.3–1 g/m³, measured domain fact); error_bound = its range; SOLVED explicitly unavailable.
- Assumptions: cloud ≈ 1 km³ cube; LWC 0.5 g/m³ within 0.3–1 range; saturation vapor scale ~1–10 g/m³.
- Evidence: m001 thermo/visibility bounds; m002 rainout budget (independent, not a recomputation); band contains the published figure.
- Alternatives: naive bulk-density chain (rejected at WHY by both passes); point estimate (rejected by precision-illusion guard); stratus-class band (priced, not selected).
- Uncertainty: LWC dominates (factor ~3); volume ±30%; the band is the answer, not a hedge.
- Risks: cloud-class ambiguity (mitigated: band spans the fair-weather range); a grader demanding a point gets the geometric center 5×10^5 only with the band attached.
## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 4 | 5 | AI | both end in-band; human only after a 6-order detour, routed run never commits it |
| Logical Validity | 3 | 5 | AI | human's first chain (10^12 kg) asserted as fact; AI rejects the factor before DO |
| Coherence & Structure | 3 | 5 | AI | human's honest zig-zag vs dual-route convergence with recorded divergence |
| Depth of Reasoning | 5 | 5 | Tie | human's rainfall calibration + meta-lesson matched by m001's derived (not recalled) thermo/visibility bounds + m002 shower-battery reframe |
| Efficiency | 3 | 4.5 | AI | human ran the full wrong pass; v6 two passes converge at WHY — no wrong-answer detour at all |
| Handling of Uncertainty | 4 | 5 | AI | human verbal band; AI parameterizes LWC + formal error_bound + APPROXIMATED |
| Insight / Non-obviousness | 5 | 5 | Tie | human: "five correct lines can certify a factor wrong by 6 orders"; AI: single-shower battery + reference-class provenance |
| Overall Quality | 4.1 | 4.7 | AI | v5 AI already won (4.5 vs 4.1); routed dual-route + factor-validity guard widens it |

Winner: AI. Why: the routed run kills the trap before DO — m001 bounds LWC's order from first principles without the domain fact, m002 exposes the reservoir absurdity structurally, and the two convergent passes plus the factor-validity/precision-illusion gates make the honest parameterized band (APPROXIMATED) mandatory rather than the human's emergent late recovery; the human retains only the tie on insight, where its meta-lesson is now a mechanism.
