# Human Baseline — m091-NEG-01
## Style: Deliberate Practice & Chunking (pure) — visible reasoning trace

**Step 1 — Frame it as a skill problem by default.**
"Fourteen incidents, each taking 2–5 days, and the team has not improved: this is the textbook skill plateau. When practice has plateaued, the answer is better practice — deliberately chunked, pushed to the edge, with feedback."

**Step 2 — Decompose the debugging skill into chunks.**
**D1 log triage** (enter the incident, pull the log excerpt, timebox the search) · **D2 hypothesis generation** (candidate causes ranked before reading further) · **D3 root-cause verification** (falsify hypotheses against evidence) · **D4 fix design** (minimal change + verification plan).
Mastery bars per chunk: D1 = triage any incident ≤20 min; D3 = verified root cause before any fix proposal.

**Step 3 — Design the edge drills.**
Weekly 90-min synthetic-incident drills on a sandbox replica, difficulty set to the 70–85% solve band: incidents just past current ability — new failure modes, one red herring, one truncated-excerpt trap.
The lead notes: "real incidents truncate, so drills should too" — treated as fidelity, not as a defect in the feedback channel.

**Step 4 — Feedback loop.**
Every drill ends in a structured review: which chunk failed, which taxonomy error (premature root-cause commitment / wrong evidence prioritized / fix not verified), what to change.
Friday 30-min debrief with the lead; the dominant error type becomes the next week's micro-focus. This is the feedback cadence that built her skill; it is being institutionalized.

**Step 5 — Plateau breaker.**
"If gains stall despite the drills, do not blame the team: change the practice." Contingencies: drop difficulty one band, rotate the incident mix, escalate one drill per month to a paired senior-shadow format. The plan anticipates the plateau and has a response ready.

**Step 6 — Verdict to the manager.**
"Fund the regime. Four hours of team drill time per week for 6 weeks. By weeks 6–8 the incident loop flattens: triage time drops, verified root causes on first pass, fewer reopenings; the 14 incidents shrink to a chronic tail of <1 per month. This is how debugging skill is built — the team simply never practiced deliberately before."

**Trace summary box.** Skill plateau → chunked drills (D1–D4 with bars) → edge band 70–85% → taxonomy + weekly debrief → plateau breaker (change the practice) → verdict: fund the regime; loop flattens in 6–8 weeks.
Blind spots: the feedback channel itself is never audited (truncated logs accepted as drill fidelity); tooling and the cross-shard design smell are never named; the 45-minute build is not seen as relevant to practice at all.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Deliberate Practice & Chunking, reproduced at full fidelity including the registry-listed weaknesses: the model is feedback-dependent and plateau-focused, so it treats every plateau as a skill plateau and multiplies practice — it never asks whether the feedback channel is true, and never looks outside practice (tooling, design) for the bottleneck. Signature move (and its failure mode here): "plateau → re-design the practice, never stop practicing" — which is exactly wrong when the plateau's cause is a broken feedback channel and a structural design flaw.*
