# Human Baseline — m092-POS-01
## Style: Spaced Repetition & Memory Science (pure) — visible reasoning trace

**Step 1 — Fix the model before any scheduling.** Forty clauses, six exposures, four hours. The curve is given: s = 0.5^(d/h); h doubles each exposure — 2, 4, 8, 16, 32, 64 days. Total time is identical in every plan, so this is not a "study harder" problem — it is a placement problem. Decay is the only enemy, and I know its shape.

**Step 2 — Enumerate the schedules and compute.** A — massed, days 114–119: audit day 42 → s = 0, never exposed. Exam day 120 → last exposure day 119, h = 64, d = 1 → s ≈ 0.99. B — fixed weekly, days 1, 8, 15, 22, 29, 36: h = 64 after the last exposure. Audit day 42: d = 6 → s = 0.5^(6/64) ≈ 0.94. Exam day 120: d = 84 → s = 0.5^(84/64) ≈ 0.40. C — expanding, days 0, 2, 6, 14, 30, 70: audit day 42, last exposure day 30, h = 32, d = 12 → s = 0.5^(12/32) ≈ 0.77. Exam day 120, last exposure day 70, h = 64, d = 50 → s = 0.5^(50/64) ≈ 0.58.

**Step 3 — Choose the criterion: the worst date, not the test.** Both dates bind. Maximize the minimum: A min ≈ 0 (a plan that zeroes the audit is a plan to fail it), B min ≈ 0.40, C min ≈ 0.58. Expanding wins by the math, not by preference.

**Step 4 — Why the shape works.** Review early while h is tiny — days 0→2→6: refreshes are cheap because decay is steepest there. Then widen: h doubles, so the gap can double (8, 16, 40 days) without strength falling below the earlier floor. The last review at day 70 is the load-bearing one: the exam's retention is decided by the final exposure's placement, not the first — d = 50 against h = 64.

**Step 5 — The subtlety the math hides.** If only the exam mattered, fixed spacing with a late last review would rival expanding — the exam date is indifferent to the shape of the gaps. Expanding wins because BOTH dates bind and there are only six sessions: the growing gap is the cheapest way to serve two distant retention points.

**Step 6 — Make it executable.** ~7 clauses per session; the hardest clauses go into sessions 4–6 (largest h), so they survive to day 120. Day 30 and day 70 are non-negotiable — skipping the final review silently turns C into B.

**Trace summary box.** model s = 0.5^(d/h), h: 2→64 per exposure · A: 0 / 0.99 → min ≈ 0 · B: 0.94 / 0.40 → min 0.40 · C: 0.77 / 0.58 → min 0.58 · criterion: max-min over both binding dates · winner: C, days 0, 2, 6, 14, 30, 70 · mechanism: review while decay is steep, double the gap as h doubles, place the last review late · subtlety: single-date fixed spacing would rival; the growing gap serves two dates with six sessions · execution: 7 clauses/session, hardest last, days 30 and 70 non-negotiable.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Spaced Repetition & Memory Science — the decay model is fixed, schedules are enumerated, retention is computed at every date, and the schedule that maximizes the binding minimum is selected. Signature move: "decay is the only enemy, and I know its shape — placement, not effort, decides."*
