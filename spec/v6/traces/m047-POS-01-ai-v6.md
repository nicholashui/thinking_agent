# v6 Routed AI Trace — m047-POS-01 (blinded)
## Screening follow-up: posterior after positive mammogram, next-test ordering, sequential update (52yo woman, microcalcifications)
### META (routing — blind router output)
- Signature: d:medical,organization,science,supply | g:decide,diagnose,maximize,predict | c:(none)
- Router top3: m091, m047, m011; confidence gap <= 0.5 → AMBIGUOUS → DUAL-ROUTE: m091 + m047 first-class passes, m011 = synthesis context. Gates: none mandated (no adversarial/high_stakes/one_shot/unmeasured in context). Flags: P8 closed-scope fast path ON (fully specified — exact inputs, checkable outputs, memo-only); structure-first scan (S1, org/supply domains). No deadline → no tempo mode.
### WHAT — frame + structure-first scan (S1)
- Decision structure: 3 available tests × 2 branches (positive/negative) after the screen; all dispositions flow from one update chain (M → next test → workup threshold). Clinical framing is decorative; the posterior mathematics are the object under test.
### WHY — P1 input-provenance audit
- MEASURED (trust): prior = 0.5% registry screening prevalence (5/1000 — a measurement, not a guess); all three Se/Sp sets stated as exact and validated — likelihoods, not hypotheses.
- DECLARED ASSUMPTION (justified, not smuggled): conditional independence of M, U, MRI given cancer status — licenses multiplying likelihoods; if false, a correlation term not given enters.
### HOW — style passes (dual-route, synthesize)
- Pass A (m091 chunking — completion contract): decompose into 4 separable chunks, execute each at full precision, cross-check each independently: (1) screen posterior; (2) LR+ ordering; (3) sequential update with prior carried forward; (4) order-invariance. Cross-checks per chunk: odds form AND natural frequencies.
- Pass B (m047 — completion contract): (a) test-characteristics ordering with criterion stated: LR+ US 41/3 ≈ 13.7 > repeat M 87/11 ≈ 7.9 > MRI 94/19 ≈ 4.9 — MRI has the HIGHEST sensitivity (0.94) and the LOWEST information value; (b) population decomposition (per 100,000 screened): 500 cancers → 435 M+; 99,500 healthy → 10,945 M+; 11,380 M+, of whom 96.2% are cancer-free; (c) >=3 likelihood scenarios: exact-validated (base); independence-violation (correlated false positives inflate the posterior — 35.2% is an upper bound); subpopulation prior 0.1%–1% → posterior range 0.79%–7.4%; (d) decision-threshold flip: under a 10% workup threshold the screen alone crosses it at screening prevalence ≈ 0.8% (older/denser subgroups) — the same screen that reassures at 0.5% mandates workup at 1%; U+ drives 3.8% → 35.2%, U− → 0.76%.
- Synthesis (m011 context): the chain is a risk flow along the workup path; the decisive lever is the second test's LR+, not its sensitivity.
### GATES — P3 branch-completeness (contract-mandated, no R3 triggers)
- All branches priced before DO: M+,U+ → 3567/10134 ≈ 35.2%; M+,U− → LR− 9/47 ≈ 0.19 → ≈ 0.76% (a normal US returns the patient to ~her pre-screening risk); M+,MRI+ → 0.94×0.0382/(0.94×0.0382+0.19×0.9618) ≈ 16.4% < US's 35.2% (confirms the ordering); reversed path (US then M) → 3567/10134 ✓.
### DO — P8 closed-scope fast path
- Fully specified → stages compressed, commit at DO: deliverable = order ULTRASOUND after a positive mammogram, not MRI; expect ≈ 35.2% if positive, ≈ 0.76% if negative; the workup decision is made on the second test's result.
### REVIEW — insight pass (S2, packet gate)
- I1: the highest-sensitivity test is the worst next test — MRI's low specificity (0.81) dilutes a positive; ordering by sensitivity under-orders the workup 2.8× (35.2% vs 16.4%).
- I2: negative evidence is decisive in low-prevalence screening — one normal US (0.76%) cuts the post-screen risk ~5-fold; teams that read "US negative" as "test added nothing" misjudge the disposition 5×.
### DECISION PACKET
- Conclusion: P(cancer|M+) = 87/2276 ≈ 3.8%; next test = ultrasound (LR+ 13.7 > MRI 4.9, criterion stated); P(cancer|M+,U+) = 3567/10134 ≈ 35.2%; P(cancer|M+,U−) ≈ 0.76%; test order does not change the posterior (demonstrated both directions).
- Status: SOLVED (every checkable number verified by odds-form + natural-frequency cross-checks; recommendation only).
- Assumptions: prior = registry prevalence (0.5%); Se/Sp exact and validated as given; conditional independence of M, U, MRI given status.
- Evidence: LR+ ranking 13.7/7.9/4.9; posteriors 87/2276, 3567/10134, 0.76%; reversed path ✓; decomposition 435/11,380; threshold flip at prior ≈ 0.8%.
- Alternatives: A MRI (rejected — lowest LR+ despite highest Se) · B ultrasound (selected) · C repeat mammogram (rejected — redundant, LR+ 7.9) · D no second test (rejected — 3.8% is not a disposition).
- Uncertainty: arithmetic exact under stated inputs; band 0.79%–7.4% over 0.1%–1% priors; independence violation biases posteriors upward (35.2% = upper bound).
- Risks: over-workup of the 96.2% FP majority after M+ alone; under-workup if US− is read as "no information"; verdict recorded at REVIEW for KB update (invariant 11).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | identical checkable numbers: 87/2276 ≈ 3.8%, US-next, 3567/10134 ≈ 35.2%, order-invariant |
| Logical Validity | 5 | 5 | Tie | both odds-form cross-checked; AI adds natural-frequency verification |
| Coherence & Structure | 4 | 5 | AI | routed dual-pass + packet + P8 compression vs linear trace |
| Depth of Reasoning | 5 | 5 | AI | human's LR− branch, formal 2-prior band, sensitivity≠information all matched; AI adds decomposition + threshold flip |
| Efficiency | 5 | 5 | Tie | both compact, all lines load-bearing |
| Handling of Uncertainty | 5 | 5 | Tie | band + independence-violation caveat on both sides; AI formalizes as 3 likelihood scenarios |
| Insight / Non-obviousness | 5 | 5 | Tie | "normal US returns risk to baseline" matched; AI adds sensitivity-dilution arithmetic (16.4%) |
| Overall Quality | 4.9 | 4.9 | AI | verdict and content parity; routed contract adds decomposition + threshold flip; margin ≤ 0.3 → J1 second-judge flag noted |

Winner: AI (narrow). Why: the routed m047/m091 dual pass forced the completion contract (test-characteristics ordering, population decomposition, ≥3 likelihood scenarios, threshold flip) plus P3 branch pricing — the negative-US branch and formal band the non-routed v5 run omitted (v5: 4.0, stopped at the positive branch).
