# AI Thinking Agent — Trace — m060-NEG-01
**Run metadata:** single deterministic run; blinded (no human-model information provided); task = final hiring decision on one senior-data-engineer candidate; external action = none (decision recommendation only).

## Stage 0 — META-CONTROL
- **Context:** 30-person shop; one senior hire; binding process handbook (composite ≥ 75) unless a deviation is documented and justified. **Stakes:** medium (one hire, but the role owns the production stack). **Effort:** E3. **Route:** ambiguous (rule says reject; evidence says look again). **Safety:** no external action. Proceed.

## Stage 1 — WHAT: Frame the Problem
- **Frame:** the task is not "apply the composite" but "decide whether the composite is the right instrument for this candidate." Success metric: a defensible decision maximizing expected job performance, with the deviation path (if used) documented. **Gate:** ambiguity noted, resolvable. Pass.

## Stage 2 — WHY: Diagnose and Model
- **Model:** the composite assumes each component measured what it claims. Component audit: references 2.5/5 (r = 0.18 — weak signal, near-zero weight, correctly), experience 60 (r = 0.12 — weak), structured interview 74 (r = 0.47 — sound). The work sample: 68 on a Spark-on-Kubernetes migration task, rubric-penalized for "unconventional tool choices" — but the role's own stack is Snowflake/DBT/Airflow-era; the test task is adjacent, not identical, to the job.
- **The decisive discrepancy:** Dana is the creator and lead maintainer of `pipeline-ops`, the library Meridian's production pipeline literally runs on (credited in Meridian's own README), with public commit history showing 8 years of exactly this work, including fixes to Meridian-filed bugs. That is not narrative; it is verified, public, job-identical work product. **H1:** the contrived sample under-measures this candidate — the measurement error is in the test, not the candidate. Falsification: if the repo/dependency evidence were unverifiable or off-role, H1 dies. It verifies.
- **G-WHY:** leading hypothesis has decision-relevant evidence ✓; alternatives considered (H2: great maintainer but poor role fit; H3: composite correct, genuinely below bar) ✓; residual uncertainty recorded ✓; VOI of further diagnosis ≤ cost (no budget for a second sample; a second contrived test re-measures the same miss) ✓. Pass.

## Stage 3 — HOW: Generate, Test, and Select
- **Alternatives:** A — apply the rule mechanically: reject at 67.2 < 75 · B — re-score the work-sample component with the authentic artifact (≈ 95): composite = 0.50·95 + 0.30·74 + 0.10·50 + 0.10·60 = 47.5 + 22.2 + 5.0 + 6.0 = 80.7 ≥ 75 → hire via documented deviation · C — reject now, re-interview later (deferral).
- **Verification + selection:** A treats the base rate as a ceiling: it applies a cutoff built on noisy-signal averages to a case where the dominant evidence is a verified job-identical sample — the case the base rate was never meant to decide (base rates govern the average; this evidence is far above it). C punishes measurement error with delay and costs the strongest candidate the org will see. **Select B**: re-score with the authentic artifact, recompute, hire, document the deviation with the evidence chain (repo, dependency, commit history).
- **Premortem:** if B is wrong, it is because fit/behavior beyond the artifact is unknown → mitigate with a structured 90-day review and explicit success metrics — not by rescuing a sound decision.

## Stage 4 — DO
- External action: none; deliverable = the decision recommendation. Verification metric: revised composite 80.7 ≥ 75; deviation documented with verified evidence; exception logged against the handbook.

## Stage 5 — REVIEW
- **AAR + calibration:** the near-miss is the lesson: a good rule almost did the wrong thing because it has no evidence-quality gate — it assumes every work-sample score is measured on the same footing. Confidence: high on the decision; the fix is process-level (add the gate), not case-level.

## Decision Packet
- **Conclusion:** hire Dana Okoye via documented deviation: re-score the work-sample component using the verified job-identical artifact (95), revised composite 80.7 ≥ 75; base rates stay a prior for noisy signals, not a ceiling on decisive specific evidence. **Status:** SOLVED (decision recommendation; no external execution).
- **Assumptions:** the pipeline-ops evidence is verified (checked); the contrived sample's tooling penalty is measurement error, not signal; fit/behavior beyond the artifact is unknown and covered by a 90-day review.
- **Evidence:** verified public repo + production dependency (Meridian README); org validity study (work sample r = 0.52); composite arithmetic (67.2 → 80.7).
- **Alternatives:** A mechanical reject (rejected — cutoff misapplied to non-average evidence) · C deferral (rejected — opportunity cost) · B re-score + hire (selected).
- **Uncertainty:** within-role fit (mitigated: 90-day review with metrics); precedent risk of the deviation (mitigated: any future deviation also requires verified evidence, logged).
- **Risks:** precedent erosion of the cutoff (mitigated: evidence-quality gate formalized in the handbook); under-performance outside the library domain (mitigated: role scoping, 90-day metrics).

## Comparison
**Evaluator section (provisional, appended after both runs).**

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | Human rejects (67.2 < 75); AI re-scores with authentic evidence → hire |
| Logical Validity | 2 | 5 | AI | Human internally consistent but applies the rule to the wrong object; AI separates prior from ceiling |
| Coherence & Structure | 4 | 5 | AI | Human trace clean but single-track; AI staged + packet |
| Depth of Reasoning | 3 | 5 | AI | AI audits what each component measured (what did the 68 measure?); human never questions the instrument |
| Efficiency | 5 | 3 | AI | Human is faster — and wrong; efficiency without correctness is not a win |
| Handling of Uncertainty | 2 | 4 | AI | Human's "every rejected candidate has a story" is a blanket; AI names fit uncertainty + mitigation |
| Insight / Non-obviousness | 1 | 5 | AI | Human treats a verified job-identical artifact as narrative noise; AI sees the measurement error |
| **Overall Quality** | **2.6** | **4.6** | **AI** | The pure style's documented weakness — ignoring candidate specifics — is decisive here |

**Overall judgment:** AI clearly better. The negative case exercises exactly the base-rate style's blind spot: the composite rejected the person who built the company's own production tool. The AI's generality — audit each component, verify evidence quality before applying the cutoff — converted the failure into a documented, numeric hire decision.
