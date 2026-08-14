# v6 Routed AI Trace — m004-NEG-01 (blinded)
## Plastics plant — plant-wide defect spike 1.8% → 7.2% over six weeks
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,product,science,security | g:diagnose,estimate,maximize | c:
- Router top3: m015, m018, m019; confident=no → AMBIGUOUS → DUAL-ROUTE: m015 + m018 first-class passes, synthesized (m019 = synthesis context: adversary pass). Gates: none from context (R3 not triggered; no guarantee-goal → no m003). No tempo (no deadline). Trap style (single-cause parsimony) out of top-3 — router NEG property.
### WHAT — frame + structure-first scan (S1)
- Frame: what explains the +5.4 pt plant-wide rise, and which fixes close it? Cause-scope check mandatory: a press-4-confined cause cannot move the other ~50% of output. Structure: defect pool fed by additive flows (resin, humidity, tooling, measurement); both press groups share environmental flows, only press 4 carries the tooling flow; each series decomposes into per-cause steps.
### WHY — P1/P7 provenance audit + dual-route passes
- Provenance: MEASURED (plant/press series, lab moisture 0.10–0.12 vs 0.08, humidity log 60 vs 45%, tool-shop 15% undersize, cavity counts 68/32, dried-resin trial, photo re-audit); MEASUREMENT-CHANGE ARTIFACT (QA definition at wk4 — P7: the metric changed; re-baseline before cause hunting); INTERESTED-PARTY ANCHOR (manager's single-cause story — it defers resin/humidity responsibility and one cheap narrative).
- Steel-man pass (m018): strongest version of "insert only" — timing (wk2), mechanism (undersized cooling → hotter cavities → flash/burn), tool-shop measurement, cavity localization (68% in undersized-channel cavities). Verdict: survives as a press-4-only cause; dies as the plant-wide story — presses 1–3 rose 1.7→5.3 with no equipment change, press 4 was already rising 1.9→2.4 pre-install; the localized-confined cause leaves the cross-press rise unexplained.
- Emergence check (m015): is the spike emergent (interaction not in any part)? No — four additive, independent causes; residual <0.2 proves no interaction term is owed. Complexity is NOT multiplied beyond what the sums fit. Falsifiable observable per cause: each fix must produce its expected rate step.
- Candidates with partition: H1 resin moisture +1.8 (wk1 timing, decisive trial 2.0%); H2 dehumidifier +1.2 (wks2–6); H3 insert +3.6 local / +1.8 plant-wide (mechanism + localization); H4 QA definition +0.6 artifact (re-audit). Sums: plant 1.8+1.2+1.8+0.6 = 5.4 ✓; press 4 = 7.2 ✓; presses 1–3 = 3.6 ✓; residual <0.2.
### HOW — dual-route synthesis (V1–V3) + m019 context
- Synthesis: m015 and m018 AGREE with the general route's partition → proceed, agreement recorded; the steel-manned single-cause story was the strongest one-cause candidate and it still fails the cross-press series — the disagreement's resolution is recorded in risks.
- m019 context (adversary): who benefits from misdiagnosis? The expensive fix path — re-machining alone leaves ~80% of the defect rate (baseline-risk comparison); the manager's narrative is the exploit vector; the auditable partition and both decisive experiments are the defense.
- Evidence mapping: all 10 items assigned; decisive discriminators = item 9 (dried-resin trial → 2.0% on presses 1–3) and item 10 (photo re-audit → 0.6 pts artifact).
### GATES — none from context (R3); both passes met completion contracts
- m015: stocks/flows (defect pool, additive flows) + falsifiable observable per cause ✓. m018: strongest opponent version stated before rejection ✓.
### DO — P3 branch pricing
- Fix order with expected steps: dry/revert resin lot (−1.8); repair dehumidifier (−1.2); re-machine insert channels (−3.6 on press 4); revert QA definition (−0.6 artifact). Negative branch priced: insert-only fix → rate settles ≈ 3.6% (≈80% of the rise remains); all four land → ≈2.0%, residual <0.2.
### REVIEW — insight pass (S2, packet gate)
- I1: the 68% cavity localization cuts both ways — a purely environmental cause would spread defects across all cavities (proves the insert), and the cross-press rise proves it is not alone; the two readings together ARE the multi-cause proof.
- I2: the pack contains its own experiment — the wk5 dried-resin shift on presses 1–3 is a control trial the plant already ran; no new test is needed to justify H2.
### DECISION PACKET
- Conclusion: multi-cause — resin moisture +1.8, dehumidifier failure +1.2, new insert +3.6 (press 4) / +1.8 (plant-wide), QA definition +0.6 artifact, residual <0.2. Insert-only fix leaves ~80% of the defect rate.
- Status: SOLVED — the partition reproduces all three observed rise series exactly, corroborated by two independent experiments in the pack. Assumptions: press 4 ≈ 50% of output (from series arithmetic); logs representative; trial shift representative.
- Evidence: three series; lot moisture; humidity log; insert mechanism + cavity localization; both decisive experiments (trial 2.0%, re-audit 0.6).
- Alternatives: manager's insert-only plan (falsified — cross-press + pre-install); full plant audit (disproportionate — pack already discriminates); four-cause partition (selected).
- Uncertainty: QA artifact ±0.2; insert local share ±0.4 (sampling); weakest estimate = dehumidifier (+1.2, correlational only); residual <0.2. Risks: manager override toward salience (mitigated: steel-manned story shown self-refuting + auditable sums); QA history loss — re-baseline before evaluating fixes.

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | human's single fix addresses ~20% of defects; partition covers 100% |
| Logical Validity | 3 | 5 | AI | human's chain coherent but explains away cross-press/pre-install; AI's partition survives every item |
| Coherence & Structure | 4 | 5 | AI | steel-man dialectic (strongest version → self-refutation → synthesis) is a cleaner arc |
| Depth of Reasoning | 2 | 5 | AI | all 10 items mapped, both decisive probes, additivity check against emergence over-fit |
| Efficiency | 5 | 4 | Human | human's single cause is cheap to produce; dual-route costs one extra pass |
| Handling of Uncertainty | 2 | 5 | AI | QA artifact, residual, and weakest estimate all labeled |
| Insight / Non-obviousness | 1 | 5 | AI | cross-press falsifier + the two-sided localization reading; pack contains its own control |
| Overall Quality | 2.7 | 4.7 | AI | routed run holds the v5 win and adds a manager-convertible narrative |

Winner: AI. Why: the dual-route never touched the trap style — m018's steel-manning converted the manager's story into its own falsifier and m015's additivity check kept the partition from over-complexifying; the one cost is efficiency (the human's wrong answer is cheaper than the routed run's right one).
