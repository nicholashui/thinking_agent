# AI Thinking Agent — Trace — m066-POS-01
**Run metadata:** single deterministic run; blinded (no human-model information provided); task = design the decisive experiment and decision protocol for a Q3 cell-swelling jump; external action = none (protocol deliverable only).

## Stage 0 — META-CONTROL
- **Context:** lithium-cell maker; swelling complaints 3.1× vs baseline; two production changes in week 37; recall exposure ≈ $4–6M; answer wanted ≤ 6 weeks. **Stakes:** high (recall-scale). **Effort:** E4 (experiment design with cost/timeline). **Route:** complicated — confounded history, prospective design required. **Safety:** no external action. Proceed.

## Stage 1 — WHAT: Frame the Problem
- **Frame:** deliverable = an experiment + decision protocol that attributes the swelling cause (or bounds it) at acceptable cost, in ≤ 6 weeks, without stopping production. Success metric: every plausible outcome maps to a unique cause attribution with a named follow-up. **Gate:** design-only, solvable from brief facts. Pass.

## Stage 2 — WHY: Diagnose and Model
- **Model:** three causal layers — materials (anode, electrolyte), process (formation), logistics (transport temperature). **Structural fact:** the two week-37 changes shipped together and no cell since has old-anode+new-profile or new-anode+old-profile → perfect collinearity → retrospective data can correlate, never attribute. Hypotheses: H1 anode (CarbonCore), H2 formation profile, H3 electrolyte lot (E-77/E-88), H4 transport temperature (reefer outage), H5 interactions. **Falsification:** each hypothesis is contradicted by a specific factorial outcome pattern (e.g., high swell in old-anode arms only → H1 eliminated). **G-WHY:** no single leading hypothesis — the experiment must arbitrate; alternatives considered ✓; residual uncertainty recorded (effect size, screen fidelity) ✓; VOI ≈ $3.1k experiment vs $4–6M recall → high ✓; falsification evidence present ✓. Pass.

## Stage 3 — HOW: Generate, Test, and Select
- **Alternatives:** A — retrospective deep-dive on Q3 data (regression/time-series) · B — prospective 2×2 factorial (anode × formation profile), 30 cells/arm, lot-blocked, 45 °C/2-week swell screen, second-stage discriminator for ambient causes (electrolyte-lot split + shipping-log cross-check), interim read at 2 weeks · C — uncontrolled rollback ("revert the profile and watch") · D — lab-level accelerated-aging simulation.
- **Verification + selection:** A fails: collinearity means any regression splits blame arbitrarily — it will "find" effects it cannot identify. C is not an experiment: whole-population change, no counterfactual arm; a drop in swelling still attributes nothing. D misses the production-line interaction (H5) and transport (H4). B breaks the collinearity by manufacturing the missing cells from remaining AnodeTech stock; 30/arm sizes a 3× rate difference; ≈ 120 × $26 ≈ $3.1k ≪ recall; outcome map covers marginals, additive, interaction-only, and all-elevated (→ H3/H4 branch); every outcome has a pre-committed follow-up, including null → escalate to customer-failure-mode study. **Select B.** Premortem: if the true effect is smaller than 3×, power at 30/arm may be thin → scale arms if interim variance is high; if the screen doesn't reproduce customer-visible swelling, the protocol fails silently → screen-fidelity check first.

## Stage 4 — DO
- External action: none; deliverable = the protocol. Verification metric: hypotheses ≥ 4; 2×2 × 30 arms, lot blocking; complete outcome→inference map; second-stage discriminator; cost/timeline within constraints; interim read defined.

## Stage 5 — REVIEW
- **AAR + calibration:** the near-miss was treating the supplier change as the working hypothesis because it is the visible event — the confound makes any single-hypothesis framing untestable, and the design exists to prevent that. Residual risk is effect size: state the detectable effect explicitly (3×) and scale arms if variance is high. Confidence: high on design, medium on effect size.

## Decision Packet
- **Conclusion:** run the prospective 2×2 factorial (anode × formation profile) on 120 cells (30/arm), electrolyte-lot blocked, 45 °C/2-week screen; outcome map: marginals → H1/H2; additive → H1+H2; interaction-only arm → revert either factor; all-elevated → ambient branch (lot split + route cross-check); ≈ $3.1k; 2-week interim read; null outcome → customer-failure-mode study. **Status:** SOLVED (protocol; no external execution).
- **Assumptions:** remaining AnodeTech stock available and representative; the standard screen reproduces the customer-visible failure; the 3.1× jump is a real signal, not a reporting artifact.
- **Evidence:** production logs (two week-37 changes, zero overlap — collinearity); QA log (electrolyte lots, reefer outage, 3 routes); standard screen protocol; cost data ($25/cell, $1/screen, $4–6M recall estimate).
- **Alternatives:** A retrospective analysis (rejected — powerless under perfect collinearity) · C uncontrolled rollback (rejected — not an experiment) · D lab simulation (rejected — misses line interaction and transport) · B factorial (selected).
- **Uncertainty:** true effect size (sized for 3×; scale if variance says otherwise); screen fidelity to customer-visible swelling; customer reports may lag production by weeks.
- **Risks:** inconclusive null result (mitigated: ambient branch + escalation plan); production disruption from experimental runs (mitigated: 120 cells over one week, scheduled); limited AnodeTech stock (mitigated: block design uses it only in two arms).

## Comparison
**Evaluator section (provisional, appended after both runs).**

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | tie | Both deliver the deconfounding factorial + complete outcome map |
| Logical Validity | 5 | 5 | tie | Same elimination logic; interaction-only arm handled by both |
| Coherence & Structure | 4 | 5 | AI | Human linear walk; AI staged + packet with cost/timeline/interim reads |
| Depth of Reasoning | 5 | 4 | Human | Human's outcome map is exhaustive first pass and the "reverting either alone fixes it" consequence is drawn explicitly; AI arrives via alternative elimination |
| Efficiency | 5 | 3 | Human | Human names design + mapping in one pass; AI spends WHY/HOW exploring retrospective/rollback/lab paths it then rejects |
| Handling of Uncertainty | 3 | 4 | AI | AI flags effect-size power, screen fidelity, stock limits, null-outcome escalation; human asserts power |
| Insight / Non-obviousness | 5 | 4 | Human | Confound insight + interaction-consequence + both traps named on first pass |
| **Overall Quality** | **4.6** | **4.2** | **Human** | Both would solve the case; the pure style's first-pass elimination logic and trap-naming carry it |

**Overall judgment:** Human clearly better (narrow). On a confounded diagnosis, the strong-inference move — hold ≥ 4 hypotheses, spot the collinearity, manufacture the missing cells, map every outcome to elimination — is the entire answer, and the human executes it in one pass; the AI's staged pipeline recovered the same design with extra exploration.
