# v6 Routed AI Trace — m091-NEG-01 (blinded)
## Payments startup — flaky-query incident loop: verdict on the deliberate-practice regime
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,product,science,software | g:decide,diagnose,guarantee | c: (none flagged)
- Router top3: m028, m018, m019; confidence gap > 0.5 → CONFIDENT → SINGLE-ROUTE: m028 first-class pass (R1) — escape-the-fixation: the plateau may not be skill. m018/m019 = router context only (steelman the regime's strongest form; adversary vectors on the feedback channel).
- Gates (R3): m003 (R4: guarantee goal prepends inversion). Flags: no c: → no tempo mode; verdict question, all facts supplied → closed-scope fast path (P8): decision reduces to the verdict, no external execution.
### WHAT — frame + structure-first scan (S1)
- Frame: not "is this a good training plan?" but "what generates the 14 incidents, and does the regime remove the generator?" Structure: incident-loop = f(skill, feedback channel, system design) — audit all three before attributing to skill.
### WHY — P1 input-provenance audit
- MEASURED: 14 incidents, 2–5 engineer-days each; 9/14 share one root cause (cross-shard join, no retry/idempotency); the failing SQL statement is TRUNCATED in the shared log, and the team mis-diagnosed that exact root cause twice BECAUSE of truncation. ANCHORED: two "synthetic drill" incidents built from that mis-diagnosis. INTERESTED-PARTY: the lead built her career on practice — plausible bias to keep practicing; no telemetry; 45-min build.
- Key provenance finding: the skill-plateau claim is UNMEASURED — no telemetry, truncated evidence, drills built from a corrupted lesson. The practice signal is false, so the regime automates the wrong lesson.
### HOW — style passes (single-route m028, escape + completeness, §II.2.9)
- Pass S1 (lateral escape from the practice frame): the plateau's cause sits outside practice — design (9/14) and tooling (truncation, no telemetry, 45-min build). Non-obvious options the fixation hides: shard-local pre-aggregation or retry+idempotency on the join path; structured logging with full statement capture; lock-wait/query-timing telemetry; CI fast-feedback ≤10 min; deterministic repro harness.
- Pass S2 (m018 steelman — strongest form of the regime): granting the lead everything — clean drills, weekly 90 min, taxonomy, structured review — the regime cannot touch the 9/14 generator (design, not skill) and cannot verify drills (45-min build). The strongest form still fails.
- Pass S3 (m019 adversary — quantified exposure per vector): truncated statement destroys the evidence class that matters (lock-wait stack); drills reproduce truncation as "fidelity" — a corrupted lesson at scale; cost: 4 h/wk × 6 wk of team time with 0 expected incident reduction.
- Divergence resolution (V2/V3): the general route's diagnosis (feedback-validity audit) AGREES with the escape pass — the practice frame is the error; branch-completeness re-checks: no branch where "keep practicing" wins the evidence. Proceed.
### GATES — m003 inversion (R3, mandatory)
- Inverted: "make the incident loop permanent" → ≥6 failure categories ranked by likelihood × impact: (1) regime funded on a corrupted signal (hi×hi) · (2) 45-min build makes drills unverifiable (hi×med) · (3) mis-diagnosis baked into drill material (med×hi) · (4) no telemetry → blind verification (hi×med) · (5) 4 h/wk cost with 0 incident reduction (med×med) · (6) skill attribution delays the real fix (med×hi). Un-mitigable residual: none on the evidence side — every named fact is tooling-fixable; the residual is whether a true skill gap remains AFTER the channel is clean. Never/always: never scale practice on an unaudited feedback channel; always fix the generator before the skill.
### DO — P3 branch completeness (no tempo flag)
- Verdict: reject the wholesale regime. Branches priced incl. failure: (a) fund as-is — 6 weeks, ~24 team-hours, 0 incident reduction expected (fails generator + feedback validity) · (b) tooling + design fix first — structured logging (100% failing-statement capture), telemetry, CI ≤10 min, repro harness, then the shard fix; metrics: first-fix rate >80%, incidents <3 in 8 weeks · (c) hybrid — b now, drills resumed at week 4–5 ONLY if a skill gap is demonstrated on the clean harness (selected). Failure branch of (c): design fix lands but incidents stay high → escalate to vendor/architecture review, not more drills.
### REVIEW — insight pass (§II.4.5)
- I1: practice is only as good as its feedback signal — drills built on a mis-diagnosis don't just fail to help, they automate the wrong lesson. I2: the lead's plateau detector was pointed at the wrong variable — the plateau is in the feedback channel (truncation), not the team's skill; re-point the detector before running it.
### DECISION PACKET
- Conclusion: do not fund the regime as proposed. The incident loop is a tooling+design ceiling, not a skill plateau: 9/14 share one root cause the team twice mis-diagnosed because logs truncate it; drills on that material automate the wrong lesson; a 45-min build makes them unverifiable. Ship observability + the design fix first; resume deliberate practice, gated on a clean repro harness, only if a skill gap is then demonstrated.
- Status: SOLVED — fully specified verdict; advisory (A2), no external execution; deterministic under stated facts.
- Assumptions: post-mortems accurate when the statement is visible (supported); no hidden capacity issue; incidents not driven by load growth alone (unverified).
- Evidence: 14 logs with truncation pattern; 9/14 shared root cause; 2 drills built from the mis-diagnosis; 45-min build; no telemetry.
- Alternatives: (a) fund as-is (rejected — corrupt signal, generator untouched) · (b) tooling+design only (necessary, alone insufficient — practice un-re-gated) · (c) hybrid gated (selected).
- Uncertainty: whether a true skill gap persists after the channel is clean — unmeasurable until the harness exists; the 3/8-week incident floor is a target, not a prediction.
- Risks: verdict read as "training is useless" (guard: drills explicitly unlock at week 4–5, taxonomy habit survives) · design fix slips (guard: named metrics + 4-week re-check).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 1 | 5 | AI | human endorses a regime that cannot touch the 9/14 generator; AI fixes it |
| Logical Validity | 2 | 5 | AI | human accepts truncation as "drill fidelity"; AI reads it as a corrupted signal (provenance finding) |
| Coherence & Structure | 4 | 5 | AI | human's plan is internally coherent and wrong; AI verdict is fact-anchored + packet |
| Depth of Reasoning | 2 | 5 | AI | human never leaves the practice frame; AI: escape pass + steelman + adversary + inversion gate |
| Efficiency | 3 | 5 | AI | ~24 team-hours on 0 expected reduction vs tooling-first with named metrics |
| Handling of Uncertainty | 2 | 4.5 | AI | human asserts a flattening date; AI labels the residual skill gap unmeasurable-until-clean with a re-check |
| Insight / Non-obviousness | 2 | 5 | AI | "drills built on a mis-diagnosis automate the wrong lesson"; "the plateau detector was pointed at the wrong variable" |
| Overall Quality | 2.3 | 4.9 | AI | pure style reproduced its registry weakness (feedback-dependent, plateau-focused) at full fidelity |

Winner: AI (clearly). Why: the route replaced the practice frame with escape styles first-class (m028) plus steelman (m018), adversary (m019), and the m003 gate — the v5 AI already had the feedback-validity audit in WHY, so v6's gain is structural (quantified vectors, branch-priced verdict, never/always) rather than a new conclusion; the human baseline never audited the feedback channel and multiplied practice against a tooling/design ceiling.
