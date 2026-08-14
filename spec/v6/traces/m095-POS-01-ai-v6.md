# v6 Routed AI Trace — m095-POS-01 (blinded)
## Brightwater chest-pain triage — 40-patient adjudicated cohort, two candidate rules
### META (routing — blind router output)
- Signature: d:medical,product | g:decide,diagnose,guarantee,predict | c:—
- Router top3: m013, m024, m039; confidence gap ≤ 0.5 → AMBIGUOUS → DUAL-ROUTE: m013 + m024 first-class passes, synthesized (m039 = synthesis context). Gate (R3/R4, "guarantee" goal): m003 inversion. Flags: no deadline → no tempo mode; cohort fully specified → closed-scope fast-path candidate (P8).
### WHAT — frame + structure-first scan (S1: decision-tree shape)
- Two exactly specified rules, 40 adjudicated rows, one deliverable: rule choice with checkable error accounting. Hinge: the 5-cue score's weights were fit on last year's 1,800 — training performance is history; the table is evidence. Structure: a 2-leaf tree vs a 5-cue weighted gate; error DIRECTION (FN vs FP) is the decision — accuracy is only a summary.
### WHY — P1 input-provenance audit
- MEASURED/given (trust): cohort rows, both rule definitions, threshold S ≥ 4, cue order ST → TRP. ANCHOR (not evidence): the 84% training-year cross-validation — benefits the score's authors; convertible only by re-counting on this cohort. H1: extra cues (SWT, AGE, PRI) are last-year signal that decayed; falsifier: they add accuracy on this cohort.
### HOW — style passes (dual-route + contracts, synthesize)
- Pass S1 (frugal-rule pass — one cue at a time, stop when clear; cue-decay audit; FN/FP asymmetry as the decision): tree admits on ST=1, else TRP=1, else monitor. Hand count: 40 rows → errors P03, P15, P30, all over-admissions → 37/40 = 92.5%; FN = 0, FP = 3. Cue-decay audit: the tree bets only on ST/TRP (23/40, 24/40) while the score's C3–C5 carry no cohort signal — 5 cues are 5 chances to misfire, 2 cues are 2. The 0-vs-7 FN asymmetry IS the decision: the score sends confirmed MIs home.
- Pass S2 (m013 root cause — fixable cause, no symptom patching): why does the score lose? Not "bad sample" (symptom patching) — the fixable cause: its weights encode last-year marginal associations that decayed; it carries stale noise into a new population. Fix: drop cues whose validity is not stable.
- Pass S3 (m024 regret — long-horizon, cuts analysis paralysis): quarter-end regret comparison — score: 7 missed MIs (irreversible); tree: 3 over-admissions (reversible bed cost). Long-horizon: the tree stays measurable — quarterly re-audit keeps the choice renewable.
- Pass S4 (general route, score check): count A exactly — S = 3·ST + 2·TRP + 2·SWT + 1.5·AGE + 1·PRI ≥ 4 → FP P03, P05, P15, P30, P32 + FN P11, P20, P21, P23, P31, P34, P40 = 28/40 = 70%. P3 branch-completeness: failure branch priced — variant C (add SWT as third stop cue) = 35/40, 0 FN but +2 FP over B: every extra cue adds misfires only.
- Synthesis (V1–V3): all passes AGREE with the general route → proceed; agreement recorded. m039 context: the asymmetry is the barbell — the tree's tail (0 FN) is where ruin lives; over-admission is the cheap tail.
### GATES — m003 inversion (R3/R4)
- ≥6 failure categories ranked L×I: (1) missed MI sent home high/catastrophic; (2) over-admission bed pressure mod; (3) ST/TRP cue decay next quarter mod; (4) cohort not representative of next quarter low/mod; (5) adjudication error in the 40 rows low; (6) mis-implementation at shift level low; (7) trusting training-year calibration low.
- Un-mitigable residual: reference-label adjudication error (audit owns it). Never/always: never send a confirmed MI home to save an admission; always hand-verify both candidates before trusting training performance; always re-audit cue validity quarterly.
### DO — P8 fast path (internal decision brief; no external action)
- Commit: run the 2-cue tree next quarter; failure branch (C) already priced in packet as dominated.
### REVIEW — insight pass (S2, packet gate)
- I1: the score's 7 FN are exactly what a 20-minute hand re-count catches — verification cost ≈ the whole case.
- I2: 0-vs-7 FN difference is decisionally decisive at n=40 regardless of SE: error DIRECTION, not the accuracy gap (92.5 vs 70), carries the decision.
### DECISION PACKET
- Conclusion: run the 2-cue tree (ST → TRP → monitor): 37/40 = 92.5% (0 FN, 3 FP) vs the 5-cue score 28/40 = 70% (7 FN, 5 FP). Status: SOLVED (decision brief; no external action).
- Assumptions: cohort represents next quarter; outcomes adjudicated; FN ≫ FP cost asymmetry.
- Evidence: hand counts — B errors P03/P15/P30; A errors 5 FP + 7 FN (listed); C 35/40 (dominated).
- Alternatives: A score (rejected: 7 missed MIs) · C 3-cue tree (rejected: +2 FP) · B 2-cue tree (selected).
- Uncertainty: n=40 SE ≈ 4–7 pts; ST/TRP validity could decay (quarterly re-audit is the holder); the 84% CV claim is not evidence.
- Risks: 3 residual over-admissions (bed cost); false comfort from 0 FN at n=40 (mitigated: quarterly audit); keeping A repeats the missed-MI pattern.

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | identical rule, identical counts (37/40 vs 28/40) |
| Logical Validity | 5 | 5 | Tie | same hand-counted arithmetic; asymmetry stated correctly |
| Coherence & Structure | 4 | 5 | AI | routed passes + gate + packet vs linear narrative |
| Depth of Reasoning | 5 | 5 | Tie | human owns "5 cues, 5 chances"; v6 owns the cue-decay audit first-pass + dominated-branch price |
| Efficiency | 5 | 4 | Human | human counts and decides in one pass; v6 is leaner than v5 (3→4) but still staged |
| Handling of Uncertainty | 3 | 4 | AI | AI prices n=40 SE and names cue decay + quarterly re-audit |
| Insight / Non-obviousness | 5 | 5 | Tie | "extra cues are last year's noise" reached first-pass; I1/I2 add verification-cost and decisiveness angles |
| Overall Quality | 4.6 | 4.7 | AI | correctness tied; routed passes closed v5's mechanism-first and asymmetry-framing gaps |

Winner: AI (narrow; margin 0.1 → contested, second judge per J1). Why: the frugal-rule pass (one-cue hand-count, cue-decay audit, FN/FP asymmetry framed as the decision) moved the two moves the non-routed v5 AI reached only in HOW/REVIEW — mechanism ownership and cost-asymmetry framing — into first-class completed outputs, matching the baseline's signature move and adding packet-level uncertainty.
