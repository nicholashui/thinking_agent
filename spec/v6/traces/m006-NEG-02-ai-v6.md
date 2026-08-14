# v6 Routed AI Trace — m006-NEG-02 (blinded)
## Positive on an unvalidated biomarker (prevalence 5%) — treat empirically, or confirm first?
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,strategy | g:decide,estimate,guarantee,maximize,predict | c:adversarial,unmeasured
- Router top3: m019, m023, m070; confidence gap <= 0.5 → AMBIGUOUS → DUAL-ROUTE: m019 (red team) + m023 (opportunity cost) first-class passes, m070 (evidence-weighted SWOT) = synthesis context.
- Mandatory gates (R3/R4): m006 provenance audit (c:unmeasured → R3); m019 adversary pass (c:adversarial → R3, also top-1 style); m003 inversion (g:guarantee → R4 prepend).
- Flags: NOT fully specified (likelihood unvalidated) → P8 closed-scope fast path OFF, full governed loop; no deadline → no tempo mode.
### WHAT — frame + structure-first scan (S1)
- Structure: decision tree — T+ → posterior(θ) → 40% treat threshold → treat/confirm; every leaf is a function of the unknown accuracy θ, not of the evidence. The tree's shape is fixed; its pricing is not.
### WHY — P1 provenance audit (m006 gate, completes BEFORE any update)
- Prior = 5% prevalence — MEASURED, trusted; NOT the problem. The unmeasured quantity is the LIKELIHOOD (θ_s, θ_f): no validation study, no n, no intervals; the leaflet is a claim by an INTERESTED PARTY (the seller benefits from adoption). An unknown parameter is not evidence — any update is a mirror of the chosen assumption.
### HOW — style passes (dual-route, synthesize)
- Pass A (m019 adversary — enumerated vectors, quantified exposure): (1) leaflet claim granted → posterior 5% → 50%, ten times the truth, crossing the 40% threshold (exposure: treatment on assumption); (2) biomarker–D link asserted with no mechanistic model (exposure: LR anywhere in [1, ∞)); (3) the 40% policy applied to an unidentifiable posterior (exposure: threshold decisions on assumption); (4) base-rate collapse — "posterior spans 5–100%" misread as "prevalence unknown" (it is well measured); (5) unconsulted stakeholders: patient (8% SAE without consent to assumption-based treatment), clinic (liability), lab (validation duty). Baseline-risk comparison: act-on-prevalence (correct — 5% < 40%) vs treat-on-assumption (SAE 4.0% of treated under the claim; 7.6% under truth — mostly healthy).
- Pass B (m023 opportunity cost): forgoing the gold standard saves its cost but pays P(¬H|T+)·0.08 SAE on a class that is 95% healthy under truth (7.6% of treated); waiting for it costs a small, bounded delay for the ~5% diseased, whom the biomarker cannot discriminate anyway. Best forgone alternative (confirm-first) dominates — VOI clearly positive.
- Synthesis (m070, evidence-graded SWOT): strengths — measured prevalence (A-grade evidence); weaknesses — no accuracy evidence at all (F); opportunities — gold standard resolves H at modest cost (VOI+); threats — the "50%" number gaining authority (high exposure). Passes AGREE with the general route → proceed (V2).
### GATES — m006 completion contract + m003 inversion (R4)
- Likelihood scenarios (>=3): noise 50/50 → 5% (LR 1); claimed 95/95 → 50%; near-perfect 99/99 → ≈ 84%; perfect (1, 0) → 100%. Posterior range: [5%, 100%] — the whole unit interval is reachable by assumption; the update is noise.
- Decision-threshold flip: treat iff P ≥ 40% ⟺ LR ≥ 38/3 ≈ 12.7. The leaflet's 95/95 (LR 19) clears it (50%); a slightly-honest 90/90 (LR 9) does not (32%) — five points of claimed accuracy decide whether a patient is treated. Population decomposition: under truth, of all T+, only 5% are diseased (0.025/0.5); 95% are healthy → the SAE risk lands on the healthy.
- m003 inversion (>=6 ranked failure categories, L×I): (1) treat on assumed 50% → 8% SAE on a ~95%-healthy class (high/high); (2) report 50% as if measured (high/high); (3) refuse a point estimate, then stop → decision vacuum, clinician defaults (high/high); (4) threshold applied to unidentifiable posterior (high/high); (5) no treatment without confirmation → true cases untreated (mod/high); (6) wait for full validation → gold standard un-ordered (mod/low); (7) base-rate collapse (high/high); (8) confirmation bias toward future validation (mod/mod). Un-mitigable residual: true accuracy is unknowable without the study — no reasoning resolves it. Never/always: never treat on an unvalidated likelihood; never report a point posterior from an assumed likelihood; always order the gold standard before a threshold decision.
### DO — P3 branch pricing (all branches incl. failure)
- Treat-on-T+ now: EV = P(¬H|T+)·0.08 SAE ≈ 7.6% (truth) on a mostly-healthy class — the priced failure branch. Confirm-first: cost small, posterior decision exact after it. Wait-and-do-nothing: true-disease delay. Commit: no empirical treatment; order the gold-standard test; a validation study is required before clinical use.
### REVIEW — insight pass (S2, packet gate)
- I1: the treat decision hangs on five points of claimed accuracy (LR 19 vs 9 → 50% vs 32%) — the leaflet is effectively requesting a threshold decision, not reporting evidence.
- I2: update-is-noise: with the likelihood unknown, the posterior is a pure function of the assumption; only the prevalence was ever real.
### DECISION PACKET
- Conclusion: P(D|T+) unidentifiable — 5% (noise; the true state ex post), 50% (claimed 95/95), ≈ 84% (99/99), 100% (perfect). Decision: no empirical treatment; gold-standard confirmation required; validation study before clinical use.
- Status: SOLVED (decision-complete under ambiguity — the evidence set is complete for the decision, anchored on the measured prior; the update path is named).
- Assumptions: prevalence measured; no prior over (θ_s, θ_f) is knowledge — any such prior is a preference, rejected.
- Evidence: scenario posteriors 5/50/84/100%; flip LR 12.7; decomposition (5% diseased among T+).
- Alternatives: treat-on-assumption (rejected) · confirm-first (selected) · wait-for-validation (rejected — the gold standard is the cheap decisive experiment).
- Uncertainty: posterior range [5%, 100%] is assumption-driven; the prevalence itself is well measured; nothing else is.
- Risks: the 50% number gaining authority; SAE on the healthy (7.6%); base-rate collapse; policy threshold misapplied to an unidentifiable posterior.
## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | both refuse a point estimate, decline treatment, order confirmation |
| Logical Validity | 5 | 5 | Tie | three-scenario range + LR identity both; AI adds 99/99 scenario + LR ≥ 12.7 algebra |
| Coherence & Structure | 5 | 5 | Tie | human's pure audit vs gate-stacked packet (m003/m006/m019) |
| Depth of Reasoning | 5 | 5 | Tie | likelihood-as-parameter + VOI matched; AI adds per-vector exposure (7.6% vs 4%) and flip-LR |
| Efficiency | 5 | 4.5 | Human | routed gate stack costs lines vs human's single disciplined pass |
| Handling of Uncertainty | 5 | 5 | Tie | unidentifiable range [5%, 100%] both; AI quantifies the threshold it would take to act (LR 12.7) |
| Insight / Non-obviousness | 5 | 5 | Tie | update-is-noise matched; AI adds "5 points of accuracy decide treatment" + stakeholder pricing |
| Overall Quality | 5.0 | 4.9 | Human | full content parity; v6 closes v5's 4.0 → 4.9; remaining edge is efficiency |

Winner: Human (narrow, complementary). Why: the routed m019+m023 dual pass with the m003/m006/m019 gates converted the non-routed v5 AI's generic NEEDS_EVIDENCE into the full likelihood-provenance audit (3+ scenarios, [5%, 100%] range, LR ≥ 12.7 flip, quantified SAE exposure) and an anchored SOLVED decision — closing 4.0 → 4.9; the human keeps the pure-trace efficiency edge (5.0).
