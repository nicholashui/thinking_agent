# AI Thinking Agent — Trace — m092-POS-01
**Run metadata:** single deterministic run; blinded (no human-model information provided); task = choose a study schedule for 40 clauses under a given retention curve with two binding checkpoints; external action = none (plan).

## Stage 0 — META-CONTROL
- **Context:** 6 sessions × 40 min = 4 hours total; clauses are discrete facts; checkpoints at day 42 (audit) and day 120 (exam); decay model given: s = 0.5^(d/h), h doubles per exposure (2→64 days). **Stakes:** medium (audit review action; certification). **Effort:** E2. **Route:** clear (given model, fixed time). **Safety:** no external action. Proceed.

## Stage 1 — WHAT: Frame the Problem
- **Frame:** total time is fixed and equal across plans — the deliverable is a PLACEMENT decision (which days to study), not a study-effort decision. Success metric: expected retention at BOTH dates; the audit is unmissable. **Gate:** both checkpoints and the model are given; no missing evidence blocks scheduling. Pass.

## Stage 2 — WHY: Diagnose and Model
- **Model: retention as a function of the schedule.** s(date) = 0.5^(d/h) from the last exposure; h depends only on exposure count, so later exposures carry more survival. Two dates bind, so a single-date optimum is not the solution — the schedule must maximize the WORST date (max-min). Memory retrieval: no stored knowledge on this standard; the decay curve is authoritative and given — no evidence gap. **G-WHY:** the decision-relevant variable (placement) is fully characterized by the model; further diagnosis has ~0 VOI. Pass.

## Stage 3 — HOW: Generate, Test, and Select
- **Alternatives:** A — massed: sessions days 114–119 · B — fixed weekly: days 1, 8, 15, 22, 29, 36 · C — expanding: days 0, 2, 6, 14, 30, 70 (gaps 2, 4, 8, 16, 40).
- **Verification (computed from the given curve):** A — audit day 42: s = 0 (no exposure); exam day 120: d = 1, h = 64 → ≈ 0.99; min ≈ 0. B — h = 64 after day 36; audit: d = 6 → 0.5^(6/64) ≈ 0.94; exam: d = 84 → 0.5^(84/64) ≈ 0.40; min ≈ 0.40. C — audit: last exposure day 30, h = 32, d = 12 → 0.5^(12/32) ≈ 0.77; exam: last exposure day 70, h = 64, d = 50 → 0.5^(50/64) ≈ 0.58; min ≈ 0.58.
- **Selection:** max-min: C (0.58) > B (0.40) > A (~0). A fails because it zeros the audit; B's last review (day 36) is too early to carry the exam. C wins: reviews early while h is small (cheap, steep decay), gaps double with h, final review placed as late as the audit allows. If only the exam bound, late fixed spacing would rival C — the growing gap is what serves BOTH dates with six sessions. **Premortem:** if C fails, it is because a session was skipped or the h-doubling estimate is wrong — mitigated: skip rule (bring the next review forward); expanding schedules degrade gracefully under h-error because gaps track h. **Red team:** is the audit really binding? Given: unmissable. Is max-min right? Yes — a plan that fails a binding checkpoint is not a schedule. No rejection.

## Stage 4 — DO
- External action: none; deliverable = the schedule. Executability: ~7 clauses/session; hardest clauses in sessions 4–6 (largest h survive to day 120); days 30 and 70 marked non-negotiable.

## Stage 5 — REVIEW
- **AAR + calibration:** the load-bearing move was computing s at both dates per schedule before any preference — max-min came out of the arithmetic, not out of the label "spaced." Gap: I generated and verified the full alternative set before the pattern (growing gaps track growing h) was obvious; the answer wants to be reached faster. Confidence: high on the decision; medium on the h-model itself (given, not measured).

## Decision Packet
- **Conclusion:** schedule C — six sessions on days 0, 2, 6, 14, 30, 70, ~7 clauses per session, hardest clauses last; expected retention 0.77 at the day-42 audit and 0.58 at the day-120 exam — the best binding minimum of the three schedules. **Status:** SOLVED (plan; no external execution).
- **Assumptions:** decay model and h-doubling hold as given; both checkpoints bind; session coverage ~7 clauses is achievable; no sessions can be added.
- **Evidence:** given curve s = 0.5^(d/h) with h: 2→64 per exposure; computed schedule retention: A ≈ 0 / 0.99, B ≈ 0.94 / 0.40, C ≈ 0.77 / 0.58.
- **Alternatives:** A massed (rejected — zeros the audit) · B fixed weekly (rejected — last review too early for the exam; min 0.40) · C expanding (selected — min 0.58).
- **Uncertainty:** h values are training-material estimates; individual clause difficulty varies; real forgetting is noisy around the curve.
- **Risks:** skipped day-30 or day-70 session (mitigated: skip rule — bring the next review forward; the schedule is a contract, not a prophecy) · h overestimated → C degrades toward B's profile (mitigated: worst case is B, which still passes both dates) · audit-day retention 0.77 is the weakest point (mitigated: session 5 includes a partial re-review of the hardest clauses).

## Comparison
**Evaluator section (provisional, appended after both runs).**

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | tie | Identical schedule (days 0, 2, 6, 14, 30, 70) and identical math at both dates |
| Logical Validity | 5 | 5 | tie | Same max-min deduction from the same curve; same arithmetic |
| Coherence & Structure | 4 | 5 | AI | Human: linear pass; AI: staged trace + decision packet |
| Depth of Reasoning | 5 | 4 | Human | Human names "the exam is decided by the final review's placement" and the single-date subtlety as first-class insights; AI reaches them via verification |
| Efficiency | 5 | 3 | Human | Human computes the three schedules and commits in one pass; AI generates and verifies the full alternative set first |
| Handling of Uncertainty | 3 | 4 | AI | AI packet bounds h-estimate risk, adds skip rule and worst-case-is-B; human asserts the schedule |
| Insight / Non-obviousness | 5 | 4 | Human | "Grow the gap as the half-life grows" and "placement, not effort, decides" are the human's lines; AI states them later, derived |
| **Overall Quality** | **4.6** | **4.3** | **Human** | Same decision; the pure style computes-and-lands first-pass and owns the mechanism; AI adds packet auditability at scaffolding cost |

**Overall judgment:** Human clearly better (narrow). The pure style IS the schedule problem, and it lands first-pass; the AI matches the math and adds uncertainty handling but pays scaffolding overhead. Learning extraction: (1) human move the AI missed first-pass: compute expected retention per candidate schedule from the decay model BEFORE generating the alternative set; (2) adopt: the max-min-over-binding-deadlines criterion and the "last-review placement dominates" check; (3) AI failure mode: alternatives-generation before the arithmetic makes the winner obvious; (4) process change: for time-placement problems with a given model, HOW should make "score every candidate against every binding deadline" the first verification pass.
