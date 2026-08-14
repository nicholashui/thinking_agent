# v6 Routed AI Trace — m006-POS-01 (blinded)
## QC dispute: A-flagged, B-passed component — which disposition?
### META (routing — blind router output)
- Signature: d:engineering,medical,organization,product,science | g:guarantee,predict | c:(none)
- Router top3: m018, m019, m070; confidence gap <= 0.5 → AMBIGUOUS → DUAL-ROUTE: m018 + m019 first-class passes, synthesized (m070 = synthesis context). Gate (R3): m003 inversion (guarantee goal → R4 prepend). Flags: P8 closed-scope fast path ON (fully specified — exact inputs, checkable outputs, memo-only); structure-first scan (S1, engineering/org). No deadline → no tempo mode.
### WHAT — frame + structure-first scan (S1)
- Decision structure: policy tree over the evidence outcomes (A∧B-pass / A∧B-fail / A-pass); all dispositions flow from one posterior chain; QC framing is decorative — the mathematics is the object under test.
### WHY — P1 input-provenance audit
- MEASURED (trust): prior 0.08 from large line audit — a measurement, not a guess; A/B operating characteristics stated as exact and validated — likelihoods, not hypotheses.
- INTERESTED PARTIES (who benefits): the "A never lies" team benefits from a never-ship-defects reputation; the "ship it" team benefits from throughput — both are self-interested framings of the same numbers.
- DECLARED ASSUMPTION (justified, not smuggled): conditional independence of A and B given status — licenses multiplying likelihoods; if false, a correlation term not given enters.
### HOW — style passes (dual-route, synthesize)
- Pass A (m018 steel-manning — both positions rebuilt strongest): "Reject now": a 61%-defective class with 39% good-part error is defensible if field-failure cost >> scrap cost. "Ship on B-pass": 30.3% is below the 50% bar and B is 90% specific on goods. Steel-manned, the dispute is a THRESHOLD dispute, not an evidence dispute — both teams agree on 61% and 30.3%; neither holds a cost function for where the cut belongs.
- Pass B (m019 red team — enumerated attacks, quantified exposure): (1) independence violation — correlated false positives (shared root cause) invalidate the joint multiplication; exposure: 30.3% not exact under violation; (2) auto-reject on A alone scraps 39% of good parts — baseline risk 0.39 × volume; (3) auto-ship at 30.3% ships a ~30%-defective class — baseline vs secondary-inspection cost; (4) prior drift (8% audit not refreshed); (5) stale characteristics (0.90/0.05, 0.75/0.10 from validation, not live).
- Synthesis (m070 context, V1–V3): evidence-graded policy table — secondary inspection survives every attack; passes AGREE with the general route → proceed, agreement recorded.
### GATES — m003 inversion (R3, completion contract)
- ≥6 failure categories ranked L×I: (1) B-pass read as noise → 30% class dispositioned as 61% (high/high); (2) B-pass read as exoneration → 30% defective shipped (high/high); (3) A-alone reject → 39% good-part scrap (high/cost); (4) cost threshold undefined → arbitrary split (high/high); (5) independence violation → wrong posterior (mod/mod); (6) prior drift (mod/mod); (7) stale characteristics (mod/low); (8) "A never lies" identity lock (mod/mod).
- Un-mitigable residual: correlated-false-positive magnitude — QA sampling study owns it. Never/always: never auto-reject when a second cheap signal exists; never ship a 30% class without disposition; always carry the posterior forward (B-pass halves it: 61% → 30.3%).
### DO — P8 closed-scope fast path (fully specified) + P3
- P3 branch table priced before commit: A∧B-fail → 270/293 ≈ 92.1% (reject); A∧B-pass → 10/33 ≈ 30.3% (secondary inspect); A-pass → ≈ 0.9% (ship). Commit: split policy — deliver numbers, not a blame verdict.
### REVIEW — insight pass (S2, packet gate)
- I1: the B-pass is not weak evidence — both B branches move the posterior ≈ 30 points (61%→30.3%; 61%→92.1%); "looks like nothing" is the mirror of "looks decisive."
- I2: evidence disputes are usually threshold disputes — neither team's position survives steel-manning without a cost function; the numbers are settled, the cut is not.
### DECISION PACKET
- Conclusion: P(D|A-fail) = 36/59 ≈ 61.0%; P(D|A-fail, B-pass) = 10/33 ≈ 30.3% (sequential ≡ joint ≡ reversed); P(D|A-fail, B-fail) ≈ 92.1%. Policy: secondary-inspect the 30% class, reject the 92% class, ship the 0.9% class.
- Status: SOLVED (every checkable number verified odds-form + joint + reversed-path; memo only).
- Assumptions: prior = line base rate (measured); characteristics exact; conditional independence; random draw.
- Evidence: 36/59, 10/33, 270/293; joint recomputation ✓; reversed path ✓; decomposition (defective mass 0.08×0.225 = 0.018; good mass 0.92×0.045 = 0.0414 → 0.018/0.0594 ✓); prior band 5/54 ≈ 0.093 – 5/9 ≈ 0.556.
- Alternatives: auto-reject-on-A (39% good-part error) · auto-ship-on-B-pass (30% defective to field) · split policy (selected).
- Uncertainty: exact under assumptions; 9.3%–55.6% over 2%–20% priors; independence violation biases upward.
- Risks: misgraded 30% class if B-pass ignored; 39% scrap if A alone; cost threshold still unset — the real open question; verdict recorded at REVIEW for KB update (invariant 11).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | identical checkable numbers (36/59, 10/33) and the same split policy |
| Logical Validity | 5 | 5 | Tie | both odds-form cross-checked; AI adds joint + reversed-path verification |
| Coherence & Structure | 4 | 5 | AI | routed dual pass + inversion gate + packet vs pure linear trace |
| Depth of Reasoning | 5 | 5 | Tie | order-invariance, population decomposition, formal prior band all matched; AI adds 8-category inversion + baseline-risk pricing (0.39 vs 0.30) |
| Efficiency | 5 | 4.5 | Human | human trace is pure; v6 gate stack costs lines, each pays |
| Handling of Uncertainty | 5 | 5 | Tie | band + independence caveat on both sides; AI formalizes via red-team attack vectors |
| Insight / Non-obviousness | 5 | 5 | Tie | negative-evidence-halves matched; AI adds symmetric-30-points + threshold-not-evidence reframe |
| Overall Quality | 4.9 | 4.9 | AI | content parity; routed contracts close v5's depth/calibration gaps (4.4 → 4.9) |

Winner: AI (narrow). Why: the routed m018/m019 dual pass + m003 gate forced the completion contracts the non-routed v5 run skipped (order-invariance recomputation, population decomposition, formal prior band, all-branch table incl. the 92% reject branch) — closing v5's 4.4-vs-4.9 margin while keeping structure's edge.
