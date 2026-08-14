# v6 Routed AI Trace — m091-POS-01 (blinded)
## Riya — 8-week production SQL tuning skill plan (fintech analyst, legacy 40TB warehouse)
### META (routing — blind router output)
- Signature: d:engineering,medical,organization,product,science,software,supply | g:decide,diagnose,guarantee,maximize,predict | c:deadline
- Router top3: m091, m031, m044; confidence gap > 0.5 → CONFIDENT → SINGLE-ROUTE: m091 first-class pass (R1). m031/m044 = router context only (baseline probe as hypothesis-test; stakeholders: Riya, Yusuf, the manager's guarantee).
- Gates (R3): m003 (R4: guarantee goal prepends inversion). Flags: c:deadline → tempo mode (P2), commit at DO; plan-only deliverable, all facts supplied → closed-scope fast path (P8): decision reduces to plan design, no external execution.
### WHAT — frame + structure-first scan (S1)
- Frame: deliverable is a skill-acquisition plan guaranteeing ≥5× on any warehouse query by week 8 — a computable practice system, not a syllabus. Structure: 60 h with week-level pass/fail gates; skill = chunks practiced at measured difficulty on true feedback.
### WHY — P1 input-provenance audit
- GIVEN/trust: problem bank (500 queries, known fixes, measured speedups) is the anchor; sandbox EXPLAIN ANALYZE is immediate plan-level feedback — TRUE and fast here (the differentiator vs the NEG pattern). MEASURED: documented week-3 plateau. INTERESTED-PARTY: Yusuf and the manager demand a guarantee — the plan must be verifiable, not aspirational.
### HOW — style passes (single-route m091, completion contract §II.2.9)
- Pass S1 (chunk decomposition + mastery bars): C1 plan literacy → C2 index design → C3 statistics/join order → C4 integrated tuning; bars measurable, non-negotiable: C1 9/10 plans read ≤5 min · C2 predicted gain within 30% of actual, 4/5 · C3 3/4 plan changes predicted after stats refresh · C4 ≥3 live ≥5× wins, Yusuf-signed. A chunk without a bar is a topic.
- Pass S2 (practice-at-the-edge, measured): baseline probe FIRST (two-join selectivity trap → edge sits at two-join); success band 70–85% weekly solve rate — above 85% raise difficulty (harder queries, tighter timebox), below 60% drop one level or swap material, inside hold. "Hard problems" is a feeling; the band is a number.
- Pass S3 (immediate feedback): prediction-then-check before every EXPLAIN ANALYZE; error taxonomy per session (plan misread / selectivity misjudged / stats neglect / tool misuse); Friday Yusuf reconciliation — dominant error type becomes the week's micro-focus. Practice with no correction is repetition.
- Pass S4 (plateau check built in): from week 4, weekly gain <15% for 2 weeks → re-diagnose which chunk's bar fails (usually C3 — intuition slowest), drop difficulty, change bank subset, escalate to Yusuf; never "practice more". Spacing/interleaving: daily 5-min C1 re-tests through W3–4.
- Divergence resolution (V2): the general route's milestone plan AGREES with the pass; the pass fixes the general route's two weak spots — verbal difficulty rule → numeric band; plateau contingency → designed-in detector. Proceed.
### GATES — m003 inversion (R3, mandatory)
- Inverted: "make this plan fail by week 8" → ≥6 failure categories ranked by likelihood × impact: (1) C3 under-allocated (hi×hi) · (2) difficulty uncalibrated (hi×hi) · (3) plateau undetected until felt (med×hi) · (4) retrieval collapse (med×med) · (5) mentor cadence lapses (lo×med) · (6) 60-h envelope breached (lo×med). Un-mitigable residual: individual variance in C3 intuition speed — absorbed by the Friday gate structure. Never/always: never practice without a measured band; always re-diagnose the failing chunk before changing material.
### DO — P2 tempo commit + P3 branch completeness
- Commit at DO (tempo): W1–2 C1 bar + C2 exposure · W3–4 C2 bar + daily C1 re-tests · W5–6 C3 bar · W7–8 C4 on sandbox replicas of the 120 slow queries, ≥3 signed ≥5× wins; 90 min/day × 5 days = 60 h. Branch completeness: every week is a pass/fail gate — failure re-plans (drop difficulty, change subset, Yusuf micro-coaching), never silent drift; negative branch pre-priced: C3 gate fails at W6 → re-run C3 on single-join→two-join stair, C4 start deferred one week.
### REVIEW — insight pass (§II.4.5)
- I1: mastery bars and the edge band are one system — the bar says which chunk to push, the band says how hard; difficulty is computable only when both exist. I2: the week-3 plateau is a design input, not a risk — fixed retrieval cadence and measured bands pre-empt it.
### DECISION PACKET
- Conclusion: adopt the chunked plan — C1→C4 with mastery bars, 70–85% edge band, prediction-then-check + taxonomy + Yusuf reconciliation, plateau detector wired from week 4, week-level pass/fail gates; delivers ≥5× on any warehouse query by week 8 within 60 h.
- Status: SOLVED — fully specified plan deliverable; advisory (A2), no external execution; deterministic under stated assumptions.
- Assumptions: problem-bank solutions correct; sandbox plan fidelity to production; Yusuf's hour stays; Riya sustains 90 min/day.
- Evidence: 500-query bank with measured speedups; instant sandbox feedback; documented week-3 plateau; 60-h envelope; snapshot (edge at two-join).
- Alternatives: syllabus (rejected — reproduces the plateau) · free-form milestones (rejected — no difficulty control) · chunked adaptive plan with gates (selected).
- Uncertainty: C3 learning curve vs 2-week allocation; band thresholds (70–85%, <15%/2wk) are standards, not learner-calibrated — the Friday gates are the calibration mechanism.
- Risks: plan degrades to ritual if gates go unenforced (guard: pass/fail, Yusuf-signed) · C3 under-allocation slips C4's start (guard: pre-priced deferral branch).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | both reach ≥5× by week 8 in 60 h; identical week map |
| Logical Validity | 5 | 5 | Tie | same chunks/bars/band logic; AI adds ranked failure categories + never/always |
| Coherence & Structure | 4 | 5 | AI | routed pass + gates + packet vs human's single dense walk |
| Depth of Reasoning | 5 | 5 | Tie | human's bars-and-band one-system now first-class (was REVIEW-late in v5); AI adds pre-priced C4 deferral branch |
| Efficiency | 4 | 5 | AI | closed-scope fast path + tempo commit at DO; decisive moves in S-passes, not REVIEW retrofits |
| Handling of Uncertainty | 4 | 4.5 | AI | both flag C3; AI prices the C3-gate-failure branch, treats bands as standards with gates as calibration |
| Insight / Non-obviousness | 5 | 5 | Tie | human: "bar says which chunk, band says how hard"; AI: same move first-class + "week-3 plateau is a design input" |
| Overall Quality | 4.7 | 4.8 | AI | v5 AI lost 4.7/3.9 on depth, insight, efficiency; the routed contract closes all three |

Winner: AI (narrow). Why: the routed m091 contract made the two decisive elements — numeric edge band and designed-in plateau detector — first-class passes instead of REVIEW retrofits (the v5 non-routed AI deferred exactly these and lost 4.7/3.9); the m003 gate adds the ranked failure categories and never/always reframing the human asserts informally.
