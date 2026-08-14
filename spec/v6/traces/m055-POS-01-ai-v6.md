# v6 Routed AI Trace — m055-POS-01 (blinded)
## EmploymentFirst wage subsidy — LTU employment panel, Region A vs B (policy natural experiment)
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,product,science,security,software,strategy,supply | g:decide,estimate,maximize | c:deadline
- Router top3: m055, m044, m070; confidence gap <= 0.5 → AMBIGUOUS → DUAL-ROUTE: m055 + m044 first-class passes, synthesized (m070 = synthesis context). Route gates: none listed; R3/R4 scan (no guarantee/high_stakes/one_shot/adversarial/unmeasured) → no extra mandatory gates. Flags: tempo mode ON (P2, c:deadline); closed-scope fast-path candidate (P8, fully-specified panel).
### WHAT — frame + structure-first scan (S1)
- Structure: causal graph over the 2×2 panel — D(subsidy, Region A from Jul 2023) → Y(LTU employment); confounders by class: U_region (2019 selection), U_time (national recovery Jan 2024), W(t) time-varying × region-specific (retraining, Region A only from Jan 2024). Do-vs-see: do(subsidy) never observed; the Region-A-only rollout is the natural experiment approximating it. Deliverable: identification strategy, confounders that survive it, estimate, claim scaled to what survives.
### WHY — P1 provenance audit + identification-first contract
- GIVEN/measured (trust): 4-window panel (monthly averages, n ≈ 40k/region, cluster SE ≈ 0.25 pp); subsidy announced Jun 2023, effective Jul 2023; retraining Region A only from Jan 2024; recovery Jan 2024; Region A selected 2019 for LTU concentration. ANCHOR (reject): naive A − B = +1.8 pp "obvious effect" — same-date national shock, not evidence; the +4.3 pp press number.
- Confounder audit by threat class, BEFORE any estimator: (a) time-invariant region differences → absorbed by DiD; (b) common time shocks (recovery) → absorbed; (c) time-varying × region-specific (retraining) → SURVIVES; (d) anticipation (Jun 2023) → partial survivor; (e) spillover/SUTVA → survivor; (f) LTU-pool composition → survivor. Class (c) non-empty ⇒ no full-window estimate is attributable; the strategy must be restricted.
- Estimator-vs-structure ordering: (c) loads exactly on post × Region A, so the full-window DiD is structurally incapable of separating subsidy from retraining — window restriction is a design choice, not a robustness check. SEE-level numbers (+4.3, +1.8, +1.7 pp) are never DO-level claims.
### HOW — style passes (dual-route, synthesize)
- Pass S1 (m055 identification-first, completion contract): natural experiment named (Region-A-only staggered rollout); confounder audit (threat classes above); what survives the strategy: (c) survives → restrict to the clean pre-confunder window. Parallel-trends placebo: (51.2−50.9)−(51.0−50.8) = +0.1 pp ≈ 0 → passes. Restricted DiD Jul–Dec 2023: (52.8−50.9)−(52.0−50.8) = **+0.7 pp**, SE ≈ 0.25 → p < 0.01. Naive +4.3 pp rejected (common shock); cross-section +1.8 pp rejected (selection); full-window (55.2−50.9)−(53.4−50.8) = +1.7 pp rejected (surviving confounder (c)).
- Pass S2 (m044 stakeholder pass): ministry (needs a number; press printing +4.3), firms (hiring response; spillover unverifiable), LTU workers (pool composition), Region B (control contamination), retraining agency (owns the same +1.7 pp — its evaluators could claim the subsidy's effect as theirs). The press trap and the co-claimant problem are named before the estimate is written.
- Synthesis (m070 evidence-weighted ledger): before-after F (common shock), cross-section F (selection), full DiD F (surviving (c)), restricted DiD P (residuals (d)(e)(f) priced). Passes AGREE with the general route (V2) → proceed; agreement recorded.
### GATES — route scan clean; P3 branch-completeness + P2 tempo commit
- P3: alternative "report +1.7 pp with a caveat" priced and rejected — the caveat dies in the press; the public claim is +0.7 pp or nothing. Falsifiable observable for the claim: same-month 2022 placebo (Jul–Dec 2022) from the monthly panel; post-2023 data cannot test it (confound persists).
### DO — P8 fast path + P2 tempo commit
- Analysis report (internal action): +0.7 pp first six months (SE 0.25); +1.7 pp explicitly non-attributable (retraining confound); +4.3 pp rejected; persistence/GE effects unknown. Commit at DO — no estimator round-trip.
### REVIEW — insight pass (S2, packet gate)
- I1: the retraining program loads exactly where the treatment loads (post-period × Region A) — no placebo or robustness check will ever catch it; only the pre-confunder window restriction can. Confounder survival is a strategy question, not a check.
- I2: the design's identification ceiling is December 2023 — every post-2023 window is structurally unable to separate subsidy from retraining; the panel can never support a longer effect claim, no matter how good future data looks.
### DECISION PACKET
- Conclusion: subsidy raises LTU employment ≈ +0.7 pp over the first six months (p < 0.01); full-window +1.7 pp conflates subsidy with the Region-A retraining program; naive +4.3 pp confounded by the national recovery.
- Status: SOLVED (analysis delivered; internal report, no external action; claim scaled to the surviving strategy).
- Assumptions: parallel trends pre-treatment (placebo +0.1 pp ≈ 0); no anticipation beyond Jun 2023; no cross-region spillover; LTU-pool composition stable; cluster SE ≈ 0.25 pp valid.
- Evidence: 4-window panel arithmetic; pre-period placebo; brief facts (recovery, retraining, 2019 selection); same-month 2022 placebo to be run.
- Alternatives: before-after (rejected — common shock); cross-sectional (rejected — selection); full-window DiD (rejected — surviving confounder); restricted DiD (selected); report-with-caveat (rejected — P3).
- Uncertainty: seasonality of the 6-month window; anticipation; spillover magnitude; persistence past 6 months unidentifiable (post-2023 ceiling); composition drift.
- Risks: ministerial overclaim of +1.7 pp (non-attributability stated in report); policy scaled to a window that may not persist; the retraining agency publishing the same effect.

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | both deliver the restricted estimate + scaled claim |
| Logical Validity | 5 | 5 | Tie | identical arithmetic and rejection chain |
| Coherence & Structure | 4 | 5 | AI | routed dual-pass + gates + packet vs single walk |
| Depth of Reasoning | 5 | 5 | Tie | audit-before-estimator now a contract; human reached it purely |
| Efficiency | 5 | 5 | Tie | human one-pass; v6 tempo commit removes round-trips |
| Handling of Uncertainty | 5 | 5 | Tie | identical residual-threat set; AI adds the identification ceiling |
| Insight / Non-obviousness | 5 | 5 | Tie | human's "survival question" matched by I1/I2 + co-claimant |
| Overall Quality | 4.9 | 5.0 | AI | v5's gap (confounder seen only via verification round-trip) closed by the m055 contract; correctness and depth tie |

Winner: AI (narrow). Why: the non-routed v5 AI recovered the retraining confounder only after a verification round-trip and presented +1.7 pp before correcting it; the routed pass executes the threat-class audit and window restriction before any estimator by contract, and adds the co-claimant and identification-ceiling observations — the baseline's strongest moves are now first-class outputs, with nothing lost.
