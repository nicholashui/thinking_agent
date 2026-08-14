# AI Thinking Agent — Trace — m091-POS-01
**Run metadata:** single deterministic run; blinded (no human-model information provided); task = design an 8-week skill-acquisition plan so an analyst reaches senior-level SQL performance tuning; external action = none (plan deliverable).

## Stage 0 — META-CONTROL
- **Context:** coaching/HR outcome with a hard 60-hour budget and a documented week-3 plateau pattern. **Stakes:** medium (one person's skill, not a safety-critical system). **Effort:** E3 (planning). **Route:** moderately complicated. **Safety:** none — no external effects; plan-only. Proceed.

## Stage 1 — WHAT: Frame the Problem
- **Frame:** deliverable = a plan that is *verifiably* skill-building, not a study syllabus: chunks, difficulty targeting, feedback, schedule, plateau response — all within 60 h. **Gate:** success metric = "a grader can check each required element against the facts." Pass.

## Stage 2 — WHY: Diagnose and Model
- **Model of skill growth:** skill = f(chunks practiced at appropriate difficulty, feedback quality, retrieval over time). Failure modes: unstructured repetition (documented: everyone plateaus at week 3), uncalibrated difficulty (too easy = no growth, too hard = demotivation), no measurement (cannot detect the plateau until it is felt). The 60-hour envelope is the hard constraint; the problem bank + sandbox give instant plan-level feedback, which is an asset to exploit.

## Stage 3 — HOW: Generate, Test, and Select
- **Alternatives:** A) syllabus approach — topic list + reading + "practice weekly" (feasible but reproduces the documented plateau; rejected) · B) milestone approach — weekly targets, free-form practice (no difficulty control; rejected) · C) chunked plan with per-chunk bars, adaptive difficulty, spaced retrieval, feedback cadence, plateau contingency (selected).
- **Verification:** walk C against the facts: chunks C1 plan literacy → C2 index design → C3 statistics/join order → C4 integrated tuning, each with a mastery bar (C1: 9/10 plans read ≤5 min; C2: predicted gain within 30%, 4/5; C3: 3/4 plan changes predicted; C4: ≥3 real queries ≥5×/week, Yusuf-signed). Interleave C1 re-tests through weeks 3–4 for retrieval; C4 only in weeks 7–8 (sandbox replicas of the 120 slow queries). *Verifier pass (budget check):* W1–2 C1+C2 exposure, W3–4 C2 bar, W5–6 C3, W7–8 C4 — fits 90 min/day × 5 days. Difficulty: "calibrate sessions so problems are challenging but solvable; raise weekly." Feedback: nightly 10-min error log, Friday Yusuf reconciliation.
- **Premortem:** most likely failure = the plan looks complete but degrades into ritual by week 5 when gains flatten — mitigations named in REVIEW below.

## Stage 4 — DO
- External action: none. Deliverable = the selected plan (chunks/bars, schedule, feedback cadence, Friday gates).
## Stage 5 — REVIEW
- **AAR + calibration:** plan structure is sound, but two elements were underspecified until review forced them: (1) the difficulty rule is a verbal band ("challenging but solvable"), not a numeric one — it should be a measured success rate (70–85%) with explicit raise/lower triggers; (2) plateau handling was added as a contingency ("if gains stall, re-diagnose the failing chunk, change material") rather than a designed-in detector with a trigger metric from week 4. Confidence: high on chunk order/bars; medium on the difficulty and plateau mechanics as currently specified.

## Decision Packet
- **Conclusion:** adopt the chunked plan — C1→C2→C3→C4 with per-chunk mastery bars, interleaved retrieval, nightly error log + Friday mentor review, and a plateau contingency; refine difficulty to a measured 70–85% band and wire the plateau detector to a weekly-gain metric before week 4.
- **Status:** SOLVED (analysis/plan delivered; no external execution required).
- **Assumptions:** problem-bank solutions are correct; sandbox fidelity to production; Yusuf's hour stays available; Riya can sustain 90 min/day.
- **Evidence:** problem bank (500 queries + known fixes), sandbox replica, analyst skill snapshot, documented week-3 plateau pattern, 60-h budget.
- **Alternatives:** A syllabus (rejected — reproduces plateau) · B free-form milestones (rejected — no difficulty control) · C chunked adaptive plan (selected).
- **Uncertainty:** actual learning curve of C3 (intuition-heavy) vs. the 2-week allocation; difficulty-band thresholds not yet empirically tuned to this learner.
- **Risks:** plan degrades to ritual at the week-5 gain flattening if the plateau trigger is not instrumented; C3 under-allocated → C4 fails at the Friday gate.

## Comparison
**Evaluator section (provisional, appended after both runs).**

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 4 | Human | Both deliver a feasible plan; human's week map reaches the ≥5× bar with gates wired to it |
| Logical Validity | 5 | 4 | Human | AI's plateau response is a contingency; human's is a designed-in detector |
| Coherence & Structure | 4 | 5 | AI | Staged v5 trace + decision packet; human is one dense walk |
| Depth of Reasoning | 5 | 3 | Human | Human unifies bars and edge band into one system; AI's difficulty rule is verbal until REVIEW |
| Efficiency | 4 | 4 | Tie | Comparable length; both stay on the critical path |
| Handling of Uncertainty | 4 | 4 | Tie | Both flag C3 risk; neither has empirical thresholds (fair) |
| Insight / Non-obviousness | 5 | 3 | Human | "The bar says which chunk to push, the band says how hard" — AI recovers it only in REVIEW |
| **Overall Quality** | **4.7** | **3.9** | **Human** | Same bones; the human's edge rule and plateau detector are first-class, the AI's are afterthoughts |
**Overall judgment:** Human clearly better. The AI built the correct skeleton but treated the two decisively gradeable elements — a numeric edge band and an instrumented plateau detector — as post-hoc refinements, while the pure model made them the load-bearing structure of the plan.
