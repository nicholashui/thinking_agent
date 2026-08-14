# v6 Routed AI Trace — m030-POS-01 (blinded)
## Straw-bridge across a 0.9 m gap — 30 whole straws, 5 m tape, 2 rubber bands; 200 g mid-span, 60 s
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,science,supply | g:diagnose,estimate,guarantee,predict | c:high_stakes
- Router top3: m030, m024, m031; confidence gap > 0.5 → CONFIDENT → single route: m030 first-class pass; m024, m031 = router context only
- Gate (R3/R4): m003 inversion (guarantee prepends it) + m007 ruin screen (high_stakes mandatory). Flags: no deadline → no tempo mode; open design brief → no P8 fast path
### WHAT — frame + P5 constraint screen (hard/soft classification FIRST)
- HARD (physical, non-waivable): 30 straws (0.5 m, uncut), 5 m tape, 2 bands, 0.9 m span, no mid-gap contact, 200 g/60 s. SOFT (self-chosen tightening targets): symmetry, ≤ 4 m tape, both bands load-bearing. Frame: a kit-compliant geometry carrying 200 g mid-span for 60 s; success = predicted capacity ≥ 2× demand + test protocol
### WHY — P1 provenance audit
- GIVEN: kit, span, load, hold (brief). ESTIMATED (provenance-labeled, ±50%): straw E ≈ 2.5 GPa (PP literature, unmeasured); Euler P_cr ≈ 45 g @ 0.5 m; deck peel ≈ 40–80 g. INTERESTED PARTY: rubric asks "design + margin" — grader-checkable, not a measured bound; the margin absorbs the ±50%
- Hypotheses: H1 flat deck (≈ 40–80 g < 200 g → falsified); H2 Warren truss, bundled compression chords, band-lashed hot joints; H3 band suspension (150 mm loops cannot span 0.9 m without tension tape → falsified). H2 survives
### HOW — style passes (completion contracts §II.2.9)
- Pass A (m030 first-class, contract met): (a) hard/soft classification FIRST — done (all kit constraints hard; soft targets chosen); (b) severe-constraint solution: constraints → principles — no cutting → 0.5 m members vs 0.9 m span → joints are load-bearing structures; bending unavailable → axial-only; long compression buckles (≈ 45 g) → short or bundled; tape peels in tension → shear-wrap only; the ONLY kit element that pulls is the band → bands are the tension resource → two Warren trusses (depth 0.2 m), 2-straw bundled chords + lateral ties (L_eff 0.25 m → ≈ 125 g/straw → ≈ 250 g vs ≈ 112 g demand → 2× margin), band pre-tensioned lashings at the 3 hot joints; (c) compatibility check on output: 30 straws ✓ whole ✓, ≈ 4 m ≤ 5 m tape ✓, 2/2 bands ✓, no mid-gap contact ✓; (d) tightening iteration: impose stricter self-constraints (both bands pre-tensioned, tape cap 3 m joints / 1 m wraps, exact mid-span symmetry) → refinements: mid-span chord doubling, lash-then-twist pre-tension sequence, diagonal collar wraps. Contract met
- Pass B (m031 context): falsifiable claim — "bundled-chord truss holds ≥ 200 g, 60 s"; discriminating test = 100 g → 150 g → 200 g; update rule: peel @ 100 g → more pre-tension; buckle @ 150 g → +ties. m024 (context): regret lens — capacity-first; margin rule (≥ 1.5×) binds the search
- Divergence resolution (V2): Pass A and the general route agree on the truss → agreement recorded; only swap-in spare members added
### GATES — m003 inversion + m007 ruin screen (R3/R4, mandatory)
- Inversion: "how does this bridge fail under the weight?" 6 ranked categories: (1) mid-span bottom-chord joint peel (max tension, tape) H/H; (2) chord buckling, longest unsupported run H/H; (3) lateral sway → truss fold M/H; (4) deck stringer sag M/L; (5) band slip at lashings L/M; (6) tape creep over 60 s L/L. Mitigations: (1) pre-tension + doubling; (2) lateral ties; (3) cross-ties; (4) stiffeners from spares; (5) twist-lash + collar; (6) shear-wrap + protocol. Un-mitigable residual: material variance (E ±50%, adhesion) — absorbed by 2× margin, detected by the 100 g probe step. Never/always: never tape in tension; always axial, short members
- Ruin screen: distribution over kit variance — worst case (E −50%): bending dominates → peel ≈ 40–80 g → RUIN (200 g falls). Floor: guaranteed capacity ≥ 1.5× only within ±25% E; below that the 100 g probe catches it before the 200 g hold — the probe IS the floor check. Provenance: every number traced to Euler + chord-force derivations, none asserted
### DO — P3 branch-completeness (advisory deliverable, no tempo)
- Failure branches priced before spec: peel @ 100 g → band re-lash + doublers (≤ 2 min); buckle @ 150 g → +2 ties from spares; sag @ 200 g → stiffeners. All within the 30-straw budget. Deliverable = build spec + 3-step test protocol (external action: none; build is the team's)
### REVIEW — insight pass (S2, packet gate)
- I1: the band is the only tension element in the kit — the constraint list dictates the load path (axial compression + band tension), so the truss is a forced geometry, not a choice
- I2: member length = half the span makes joints load-bearing structures — the jointing plan IS the capacity plan
### DECISION PACKET
- Conclusion: 2 Warren trusses (depth 0.2 m), bundled 2-straw compression chords + lateral ties, band pre-tensioned lashings at the 3 hot joints, mid-span chord doubling; ≈ 2× margin at 200 g; 30/30 straws, ≈ 4/5 m tape, 2/2 bands
- Status: APPROXIMATED — all constraints cleared on paper with 2× margin; physical capacity ±50% (material props) until the 3-step test runs (error bound: E-driven estimates)
- Assumptions: E ≈ 2.5 GPa PP; tape wraps hold in shear; band pre-tension static; 200 g static at mid-span
- Evidence: Euler (deck ≈ 40–80 g), chord force (≈ 112 g/truss), bundled capacity (≈ 250 g), budget table, provenance labels
- Alternatives: flat deck (falsified) · suspension (falsified, reach) · V-girder (member-hungry) · truss (selected)
- Uncertainty: material props ±50% → margin + probe protocol arbitrate; joint behavior until built
- Risks: joint peel (pre-tension + doubling + probe), buckling (ties), sway (cross-ties) — all in-spec, all gated by 100→150→200 g

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | Same truss, ≈ 2× margin, full budget; rubric 6/6 both |
| Logical Validity | 5 | 5 | Tie | Same physics chain (Euler ≈ 45 g, deck ≈ 40–80 g, chord ≈ 112 g, bundled ≈ 250 g); no errors |
| Coherence & Structure | 4 | 5 | AI | Human is a linear build-up; routed pass + gates + packet is checkable end-to-end |
| Depth of Reasoning | 5 | 5 | Tie | Tightening pass and band pre-tension — the human's home-turf win — are now contract outputs (m030 iteration) |
| Efficiency | 5 | 4.5 | AI | Human lands the refined truss in one sweep; v6 pays no second sweep — tightening lives inside the pass, packet is heavier |
| Handling of Uncertainty | 3 | 5 | AI | Human asserts estimates; v6 provenance-labels every number (±50%) + probe-gated floor from the ruin screen |
| Insight / Non-obviousness | 5 | 5 | Tie | "Bands are the tension resource" + "joints are load-bearing" are now pass outputs and S2 insight entries |
| Overall Quality | 4.6 | 4.9 | AI | Routed m030 owns the style's home turf; inversion + ruin gates add failure structure the baseline lacked |

Winner: AI (narrow). Why: the v5 AI's admitted gap — no tightening pass — is now the m030 contract's third item (deliberate severe-constraint solution + constraint-augmentation), so the human's signature moves are produced first-class; the m003/m007 gates add ranked failure structure and a probe-gated floor the baseline asserted away.
