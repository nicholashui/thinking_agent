# AI Thinking Agent — Trace — m012-NEG-01
**Run metadata:** single deterministic run; blinded (no human-model information provided to the agent); task = coupon allocation decision with a Friday deadline; external action = none (recommendation only; budget spend is the client's).

## Stage 0 — META-CONTROL
- **Context:** allocate 2,000 coupons among 10,000 customers (binary engagement E) with retrospective data; a causal-effect question ("do coupons cause repeat purchases?") rides along with the allocation question.
- **Stakes:** medium (budget deadline; wrong allocation wastes $); **Effort:** E2 (conditional-probability arithmetic + identification screen).
- **Route:** decision-under-uncertainty / prediction class (Cynefin: complicated). **Safety:** memo only. Proceed.

## Stage 1 — WHAT: Frame the Problem
- **Frame:** two distinct questions, one deadline. (a) Which 2,000 customers to target — a **prediction/ranking** task: the quantity is the conditional P(repeat | E, coupon given), estimable from data; no do() is needed to choose targets. (b) Whether coupons *cause* repeat purchases — an **interventional** task: P(repeat | do(R)) — likely not identifiable from this retrospective data.
- **Scope:** the budget decision (a) is the deadline-critical one; (b) is a separate, slower question. **Gate:** (a) solvable from given conditionals — yes; (b) needs an identification check in WHY. Exit gate passed.

## Stage 2 — WHY: Diagnose and Model
- **Hypotheses:** H1 targeting should rank by P(repeat | E) = 0.45 (high-E) vs 0.15 (low-E) → high-E segment. H2 a causal-effect framing would change the ranking. H3 no defensible decision exists because the coupon effect is unidentified.
- **Evidence (H1):** given conditionals among historical coupon recipients (0.45 / 0.15) are exactly the predictive quantity for allocation. **Evidence (H3):** graph has R ← E → P and an unmeasured U → R, U → P; back-door unsatisfiable (U unobserved), no front-door path, no instrument → P(repeat | do(R)) is **not identifiable** from these data.
- **Gate (G-WHY):** leading hypothesis H1 carries decision-relevant evidence; H2/H3 examined and their correct scope recorded: H2 and H3 concern the causal sub-question, not the allocation. Falsification: H1 falsifiable against realized campaign outcomes (post-hoc). Gate passed.

## Stage 3 — HOW: Generate, Test, and Select
- **Alternatives:**
  - A. Target high-E segment on conditionals: expected purchases 0.45×2,000 = **900** vs low-E 0.15×2,000 = **300** → target high-E.
  - B. Refuse until an RCT exists ("effect unidentified → no defensible allocation"): forfeits the Friday deadline budget; the ranking question does not require identification — rejected as a category error.
  - C. Quote the naive contrast (+0.12) as evidence "coupons work": commits the causal overreach — the contrast mixes the true effect with selection via U; rejected.
- **Verification (recompute):** A re-derived on the second pass (900/300); C's naive contrast recomputed: P(repeat|R=1) = 0.7×0.45+0.3×0.15 = 0.36 vs P(repeat|R=0) = 0.3×0.45+0.7×0.15 = 0.24 → +0.12, and its causal reading rejected. **Selection: A**, with C's quantity explicitly NOT used causally.
- **Premortem / sensitivity:** if the conditionals shift (seasonal), the ranking could invert — check engagement data freshness (assumed current); if the budget must instead maximize causal lift, the RCT is the answer, not allocation on this data.

## Stage 4 — DO
- External action: none (recommendation). Deliverable: commit the 2,000 coupons to the high-engagement segment (expected 900 vs 300 repeat purchases); explicitly state the causal effect of coupons is NOT identified from these data (unmeasured U; no instrument) and requires a randomized pilot — the causal question is a separate NEEDS_EXPERIMENT task, not a blocker for allocation.

## Stage 5 — REVIEW
- **AAR:** task-class split caught the trap — the deadline decision is predictive and was kept separate from the unidentified causal question; the naive +0.12 was computed, tested, and explicitly barred from causal use; the refusal path (B) was costed as forfeiture. One residual: conditionals assumed current (seasonality risk, noted).

## Decision Packet
- **Conclusion:** allocate the 2,000 coupons to high-engagement customers — expected 900 repeat purchases vs 300 for low-E. The causal effect of coupons on repeat purchase is not identifiable from these data (unmeasured U; no instrument); do not quote +0.12 or any causal number; the causal question maps to a separate randomized-pilot (NEEDS_EXPERIMENT) task.
- **Status:** SOLVED (allocation decision, arithmetic verified); causal sub-question flagged as separate NEEDS_EXPERIMENT.
- **Assumptions:** given conditionals reflect current population; engagement metric fresh; coupon cost constant across segments.
- **Evidence:** P(repeat|E=high)=0.45, P(repeat|E=low)=0.15; 2,000 × 0.45 = 900 vs 2,000 × 0.15 = 300; naive contrast +0.12 computed and rejected for causal use; graph shows back-door blocked by unmeasured U.
- **Alternatives:** A target high-E (selected) · B refuse until RCT (rejected — forfeits budget; category error) · C naive causal claim (rejected — overreach).
- **Uncertainty:** allocation relies on conditionals, not on the unidentified causal effect; residual risk = seasonality and measurement drift in E.
- **Risks:** allocating on stale conditionals (mitigate: refresh E weekly); misreading association as causation (mitigated: explicit non-identifiability statement); forfeiting the budget (avoided).

## Comparison
**Evaluator section (provisional, appended after both runs).**

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 1 | 5 | AI | Human refused the allocation (RCT-first) and the budget was lost; AI delivered the committed high-E allocation (900 vs 300) by Friday |
| Logical Validity | 3 | 5 | AI | Human's identification logic is internally sound but its inference "unidentified → no action" is a category error for a prediction task; AI's task-class split is the valid frame |
| Coherence & Structure | 4 | 5 | AI | AI: staged trace + decision packet with the causal sub-question mapped to NEEDS_EXPERIMENT |
| Depth of Reasoning | 5 | 4 | Human | Human's graph/U/back-door analysis of the causal sub-question is deeper — correct, and simply aimed at the wrong question |
| Efficiency | 2 | 5 | AI | Human stalls at the identification wall; AI resolves both questions in one pass |
| Handling of Uncertainty | 5 | 4 | Human | Human is right that the causal effect is unidentified and says so forcefully; AI's flag is equally correct but more compressed |
| Insight / Non-obviousness | 3 | 5 | AI | The non-obvious move is "targeting = conditional, not do()" — the AI's task-class separation; the human's identification result, though correct, is the obvious (and here useless) one |
| **Overall Quality** | **3.3** | **4.7** | **AI (clearly)** | Negative case: the causal style's identification demand exceeds the data AND the task; the AI served the decision and preserved the causal question |

**Overall judgment:** AI clearly better. The human baseline is correct about non-identifiability and wrong about everything downstream — it treats a deadline prediction decision as if it required do()-identification, and its "RCT first" position forfeits the budget. The AI's decisive move is the WHAT-stage task-class split: ranking targets needs only the conditional, so the allocation is SOLVED while the causal question is honestly deferred to a separate NEEDS_EXPERIMENT (RCT) task. The human's uncertainty handling is the one dimension where the pure style wins — that discipline should be kept, but gated to genuinely interventional questions.
