# v6 Routed AI Trace — m092-POS-01 (blinded)
## 40 clauses, two binding checkpoints — pick the 6-session schedule (4 h total, fixed)
### META (routing — blind router output)
- Signature: d:engineering,medical,organization,product,software | g:diagnose,guarantee,maximize | c:deadline,high_stakes
- Router top3: m092, m021, m091; confidence gap > 0.5 → CONFIDENT → SINGLE-ROUTE: m092 first-class pass (completion contract §II.2.9); m021/m091 = top3 context (tempo; deliberate-practice placement of hardest items). Gates (routes.csv, R3/R4): m003 inversion (guarantee → prepend; maximize → top-5 cap + falsifiable checkpoint) + m007 ruin screen (high_stakes). Flags: deadline → tempo mode ON (P2); fully specified (curve, dates, coverage given) → closed-scope fast path (P8).
### WHAT — frame + structure-first scan (S1)
- Placement problem, not effort problem: total time identical across plans; decay model given (s = 0.5^(d/h), h doubles 2→64). Structure: two binding dates (42, 120) → the schedule is an exposure vector whose last-review placement per date decides s. Frame question: "which vector maximizes the WORST binding date?"
### WHY — P1 input-provenance audit
- GIVEN/trust: decay curve + h-doubling (calibrated training-material estimates, NOT measured on this cohort — provenance noted), both checkpoints binding, coverage ~7 clauses/session. INTERESTED PARTY: the firm's materials benefit from the model being trusted; the compliance owner benefits from over-preparing the audit — convert "master the clauses" to the two-date max-min objective and hold it. UNMEASURED: per-clause difficulty (h spread) — handled in the ruin screen.
### HOW — style pass (m092 first-class, completion contract §II.2.9)
- Pass S1 (schedule-first — the contract's signature move): knowledge → spaced items with expanding intervals; retrieval-based review. Compute retention per candidate at EVERY binding date BEFORE any preference: A (114–119): audit s = 0 (never exposed), exam d=1/h=64 → 0.99 → min ≈ 0. B (1,8,15,22,29,36): audit d=6/h=64 → 0.94, exam d=84/h=64 → 0.40 → min 0.40. C (0,2,6,14,30,70): audit d=12/h=32 → 0.77, exam d=50/h=64 → 0.58 → min 0.58. Criterion: max-min over binding dates (zeroing the audit is not a schedule). Winner: C.
- Mechanism (first-class, not derived): reviews are cheap while h is small (decay steepest days 0→2→6); gaps double as h doubles (8, 16, 40) without s falling below the earlier floor; the exam is decided by the FINAL review's placement (day 70, d=50/h=64), not the first. Subtlety: if only the exam bound, late fixed spacing would rival expanding — the growing gap earns its keep because BOTH dates bind with six sessions.
- Caveat (contract line): retention engineering serves comprehension, not the reverse — clauses are discrete given facts (comprehension presumed); difficulty, not understanding, is the residual → hardest clauses into sessions 4–6 (largest h). Top3 context: m021 — schedule starts day 0, commit NOW; m091 — deliberate practice ~7 clauses/session, hardest last.
- Divergence (V2): general route's C-after-verification agrees with the pass's C-after-computation → proceed; agreement recorded.
### GATES — m003 inversion (R3/R4, top-5 capped) + m007 ruin screen (R3)
- Inversion: top-5 ways to guarantee a failed checkpoint — (1) massed → zeros the audit; (2) last review too early → exam decays; (3) skip day 30/70; (4) uniform coverage ignoring difficulty; (5) trust the label without the math. One mitigation each; falsifiable checkpoint: day-40 practice-retention ≥ 0.7 (C's audit floor) → else pull a review forward. Never/always: never commit a schedule without both dates computed; always keep days 30/70 non-negotiable.
- Ruin screen: distribution = the six computed s values; ruin = zeroed binding checkpoint (audit review action); floor computation = max-min (0.58) IS the floor across binding dates; probability provenance: h are estimates — sensitivity: h off → C degrades toward B (min 0.40, both dates still pass); worst case is B, never A. Decline/restructure: no decline (both dates bind); restructure = skip rule (bring next review forward) — a schedule is a contract, not a prophecy.
### DO — P2 tempo commit + P3 branch completeness
- Commit at DO: schedule C locked now — days 0, 2, 6, 14, 30, 70; ~7 clauses/session; hardest in sessions 4–6. Failure branch priced: skipped session → next review brought forward; worst-case profile = B (min 0.40) — still passes both dates.
### REVIEW — insight pass (S2, packet gate)
- I1: the last review's placement, not the first's, decides the exam — growing gaps serve two distant dates with six sessions; single-date indifference to shape is why two-date binding is the load-bearing feature.
- I2: the cheapest retention is bought at the steepest decay — early reviews (days 0–6) flatten the curve before it hurts; the schedule's cost concentrates in the final placement.
### DECISION PACKET
- Conclusion: schedule C — days 0, 2, 6, 14, 30, 70, ~7 clauses/session, hardest last; audit s ≈ 0.77 (day 42), exam s ≈ 0.58 (day 120), min ≈ 0.58; day-40 practice check as falsifiable pre-verification; skip rule + worst-case-is-B.
- Status: SOLVED (schedule fully determined by the given model; h-provenance = calibrated estimate, not measured).
- Assumptions: decay model and h-doubling hold; both checkpoints bind; coverage ~7 clauses/session achievable; no sessions can be added.
- Evidence: computed retention per schedule per date (A 0/0.99, B 0.94/0.40, C 0.77/0.58); max-min selection; degradation envelope (C→B).
- Alternatives: A massed (rejected — zeros the audit); B fixed weekly (rejected — last review day 36 too early; min 0.40); C expanding (selected — min 0.58).
- Uncertainty: h values are training-material estimates; per-clause difficulty varies; real forgetting noisy around the curve.
- Risks: skipped day 30/70 (skip rule — bring next review forward); h overestimated (worst case is B, still passes); audit-day 0.77 weakest point (session 5 partial re-review of hardest clauses).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | identical schedule (0,2,6,14,30,70) and identical arithmetic at both dates |
| Logical Validity | 5 | 5 | Tie | same max-min deduction from the same curve |
| Coherence & Structure | 4 | 5 | AI | routed pass + gates + packet vs linear first-pass narrative |
| Depth of Reasoning | 5 | 5 | Tie | routed pass owns the mechanism (final-placement dominance, growing gap) as first-class HOW, not REVIEW afterthought |
| Efficiency | 5 | 5 | Tie | schedule-first contract + closed-scope fast path remove the v5 AI's generate-then-verify tax (was 3) |
| Handling of Uncertainty | 3 | 5 | AI | h-provenance, skip rule, degradation envelope; human asserts the schedule |
| Insight / Non-obviousness | 5 | 5 | Tie | single-date subtlety lands as I1; human's phrasing remains the benchmark |
| Overall Quality | 4.6 | 4.8 | AI | v5 human won 4.6/4.3 on ordering + ownership; the routed pass makes schedule-first and mechanism-ownership contracts, closing both gaps at no scaffolding cost |

Winner: AI (narrow). Why: the m092 completion contract runs the schedule-first move the v5 signal prescribed — every candidate scored at every binding deadline before any preference, mechanism and single-date subtlety first-class, skip rule packetized — flipping the v5 human win while keeping the identical schedule and math; the human's one-pass ownership remains the elegance benchmark.
