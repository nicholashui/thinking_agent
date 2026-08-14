# AI Thinking Agent — Trace — m060-POS-01
**Run metadata:** single deterministic run; blinded (no human-model information provided); task = design a selection process for 12 field-technician hires; external action = none (design brief only).

## Stage 0 — META-CONTROL
- **Context:** 40-technician company, 12 hires in 8 months, 45% turnover, bad hire ≈ $18k, budget ≈ $40/applicant, local validity study supplied. **Stakes:** medium-high (repeatable decision, dollar-quantifiable). **Effort:** E3 (process design with quantified trade-offs). **Route:** complicated; data given, decision rule to be built. **Safety:** no external action. Proceed.

## Stage 1 — WHAT: Frame the Problem
- **Frame:** deliverable = signal ranking + scoring/weighting scheme + decision rule + cost-benefit vs the current process. Success metric: expected composite validity ≥ 0.45 at ≤ $40/applicant, and the process explicitly blocks the current failure (personality-weighted hiring). **Gate:** solvable from brief facts. Pass.

## Stage 2 — WHY: Diagnose and Model
- **Model: current-process validity.** Old composite ≈ conversational interview + experience + references, weights set by interview impact → de facto r ≈ 0.28. The symptoms (45% turnover, bad-hire cost) fit a process dominated by a low-validity signal. The org's own study supplies the ordering authority: work sample 0.52 > structured 0.47 > unstructured 0.21 > references 0.17 > experience 0.13.
- **Hypotheses:** H1 — unstructured interview is the dominant weight today, hence low validity · H2 — the study's ranking is the right evidence to build on · H3 — budget binds: $40/applicant must cover the top signals. **G-WHY:** evidence = study + symptom costs; alternatives considered; falsification flagged = if the study's numbers are wrong the ranking falls apart → re-validation required. Pass.

## Stage 3 — HOW: Generate, Test, and Select
- **Alternatives:** A — validity-weighted composite (work sample 50%, structured 30%, references 10%, experience 10%, unstructured 0%, screens only for the bottom two; threshold ≥ 70, work-sample tie-break) · B — keep unstructured interview weighted ≈ 20% for "culture fit" · C — cheap screen only (resume + references) · D — work sample only.
- **Verification + selection:** C fails validity (≈ 0.20 → bad-hire cost ≈ 10× the assessment cost). B fails: culture-fit weighting is how the interview illusion re-enters; the org's r = 0.21 is the verdict. D has the best raw validity but single-signal measurement error and no behavioral check on collaboration. **Select A**, weights proportional to validity. Cost check: 22 + 8 + 2 = $32/applicant ≤ $40 ✓.
- **Premortem:** the failure mode is a charismatic hire slipping through → the threshold and tie-break must be mechanical; an override path is a door for the gut → default no-override; deviations require documented evidence.

## Stage 4 — DO
- External action: none; deliverable = the design above. Verification metric: composite validity ≈ 0.50 ≥ 0.45 target; $32 ≤ $40; decision rule mechanical (threshold + tie-break + logged exceptions).

## Stage 5 — REVIEW
- **AAR + calibration:** the design is standard selection-validity practice; the main risk is the study itself (n = 120; r ± ~0.1) → annual re-validation with hire-outcome tracking. Gap: I partially re-derived why experience predicts poorly inside WHY instead of taking the supplied table as the evidence — the ranking was decided the moment the study numbers were given. Confidence: high on design, medium on study precision.

## Decision Packet
- **Conclusion:** adopt validity-weighted composite (A): work sample 50% / structured 30% / references + experience as pass-fail screens / unstructured interview removed from scoring; threshold ≥ 70; expected validity ≈ 0.50 vs old ≈ 0.28; ≈ $32/applicant against ≈ $36–54k bad-hire cost avoided. **Status:** SOLVED (design brief; no external execution).
- **Assumptions:** the org's validation study generalizes to new territories; applicant pool quality unchanged; ≈ 100 applicants for 12 hires.
- **Evidence:** org's local validity study (n = 120); documented turnover/bad-hire costs; standard selection-validity ordering (work samples and structured interviews above unstructured interviews and experience).
- **Alternatives:** B culture-fit weighting (rejected — reintroduces interview illusion) · C cheap screen (rejected — validity ≈ 0.20) · D work-sample-only (rejected — single-signal risk) · A validity-weighted composite (selected).
- **Uncertainty:** r estimates ± ~0.1 at n = 120; pool quality unknown pre-launch; team compliance with a mechanical rule is an organizational risk.
- **Risks:** charismatic hire slips through (mitigated: mechanical threshold + tie-break + logged deviations); validity drift (mitigated: annual re-validation with outcome tracking); false negatives on unconventional candidates (flagged — evidence-quality question for review).

## Comparison
**Evaluator section (provisional, appended after both runs).**

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | tie | Both produce a valid, budgeted, thresholded design |
| Logical Validity | 5 | 5 | tie | Same ranking logic; both exclude the unstructured interview |
| Coherence & Structure | 4 | 5 | AI | AI has staged trace + decision packet; human is a linear walk |
| Depth of Reasoning | 5 | 4 | Human | Human's "the room lies" framing and 0.28→0.50 math land first pass; AI re-derives known base rates in WHY |
| Efficiency | 5 | 3 | Human | Human opens with the validity table and never revisits; AI spends a stage re-deriving the ordering |
| Handling of Uncertainty | 3 | 4 | AI | AI flags CIs on r, re-validation, pool-quality risk; human asserts |
| Insight / Non-obviousness | 4 | 3 | Human | "References and experience are screens, not drivers" + interview-illusion kill is the human's signature |
| **Overall Quality** | **4.4** | **4.1** | **Human** | Both strong; human wins on first-pass base-rate anchoring, AI on auditability |

**Overall judgment:** Human clearly better (narrow). When the decision is a volume process and the validity data is given, the pure base-rate move — table first, weights from numbers, low-validity signals demoted — is the whole answer, and the human executes it in one pass; the AI's staged pipeline recovered the same design with extra steps.
