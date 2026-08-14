# Human Baseline — m091-POS-01
## Style: Deliberate Practice & Chunking (pure) — visible reasoning trace

**Step 1 — Probe the current edge before planning anything.**
"You cannot design practice without knowing where ability currently ends." Baseline probe: three queries — one single-join (Riya solves), one two-join with a selectivity trap (fails), one three-join with a stats trap (fails; cannot explain why).
Edge is at the two-join level; everything is scheduled from here.

**Step 2 — Decompose the skill into chunks with mastery bars.**
Skill = production SQL tuning. Chunks, dependency-ordered: **C1 plan literacy** · **C2 index design** · **C3 statistics & join order** · **C4 integrated tuning**.
Mastery bar per chunk, measurable, non-negotiable: C1 = read any problem-bank plan, name bottleneck + fix ≤5 min, 9/10 · C2 = measured gain within 30% of prediction, 4/5 · C3 = predict plan change after stats refresh, 3/4 · C4 = ≥3 real queries ≥5×/week, Yusuf-signed. *A chunk without a bar is a topic, not a chunk.*

**Step 3 — Order, space, interleave.**
C1–C2 weeks 1–4 interleaved: every session ends with five 5-min C1 re-tests (retrieval converts mastered material to long-term skill). C3 weeks 5–6; C4 weeks 7–8 on sandbox replicas of the 120 slow queries.
Fixed cadence defeats the documented week-3 plateau: daily micro re-tests, Friday pass/fail gate per chunk.

**Step 4 — Practice at the edge, measured.**
Success band **70–85% solve rate per week** on the problem bank at current difficulty. Above 85% → raise difficulty (harder queries, tighter timebox); below 60% → drop one level or swap material; inside the band → hold.
"Hard problems" is a feeling; 70–85% is a number — the edge is where failure is frequent enough to learn and rare enough to motivate.

**Step 5 — Feedback loop, immediate and specific.**
Every session: prediction-then-check — state predicted bottleneck + fix *before* EXPLAIN ANALYZE; log misses into an error taxonomy (plan misread / selectivity misjudged / stats neglect / tool misuse).
Weekly 30-min Yusuf session reconciles predictions against actuals; the dominant error type becomes the week's micro-focus. Practice with no correction is repetition.

**Step 6 — Plateau is a planned event, not a surprise.**
From week 4, weekly gain <15% for two weeks → re-diagnose at chunk level (which bar is failing — usually C3, where intuition is built slowest), drop difficulty one level, change problem-bank subset, escalate to Yusuf for micro-coaching.
Never "practice more" — re-design the practice.

**Step 7 — The plan, week-mapped.**
W1–2: C1 bar + C2 exposure (edge band on two-join). W3–4: C2 bar + daily C1 re-tests. W5–6: C3 bar. W7–8: C4 on live-ish workloads, ≥3 signed ≥5× wins. 90 min/day fits; total 60 h.

**Trace summary box.** Probe → edge at two-join. Chunks C1→C2→C3→C4, each with a mastery bar. Edge band 70–85%, difficulty adjusted by measured rate. Feedback = prediction-then-check + taxonomy + Yusuf reconciliation. Plateau detector from week 4 with named contingencies. Verdict: fits 60 h, reaches the week-8 ≥5× bar.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Deliberate Practice & Chunking: baseline probe before planning; chunk decomposition with per-chunk measurable mastery bars; dependency-ordered scheduling with spacing and interleaving; a quantitative edge band with adjustment logic; a feedback loop with prediction-then-check and error taxonomy; plateau detection built into the schedule. Signature move: mastery bars and the edge band are one system — the bar says which chunk to push, the band says how hard.*
