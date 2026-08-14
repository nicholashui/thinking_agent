# AI Thinking Agent — Trace — m092-NEG-01
**Run metadata:** single deterministic run; blinded (no human-model information provided); task = design a 21-day learning plan for a transferee engineer with 30 hours and a transfer-based success metric; external action = none (plan).

## Stage 0 — META-CONTROL
- **Context:** 21 days, 30 hours; success = trace a payment request end-to-end + first merged PR; team data: fact recall ≈ 0 correlation with first-PR success, tracing ability predicts it; a colleague proposes a 500-card expanding-interval plan (~12h production + ~16h reviews). **Stakes:** medium (onboarding outcome; not safety-critical). **Effort:** E3. **Route:** complicated — the plan must target a specific bottleneck. **Safety:** no external action. Proceed.

## Stage 1 — WHAT: Frame the Problem
- **Frame:** the deliverable is a plan that moves the PREDICTOR, not a plan that "covers the docs." Given the team's data, the success metric is transfer (trace + first PR), not recall — so any plan whose output is recall is framed wrong. **Gate:** goal and metric are given. Pass.

## Stage 2 — WHY: Diagnose and Model
- **Model: bottleneck diagnosis, not schedule design.** Two failure classes: (a) encoding/comprehension — the knowledge was never structured in the first place; (b) decay/retention — understood items lose strength over time. The team data discriminates: if recall predicted readiness, retention would be the lever; it does not, and the traceability predictor says the model is missing. Discriminating probe, 1 hour: "trace one sample payment request through the docs." If she cannot, the deficit is (a); if she can, (b) is the smaller problem. **G-WHY:** falsifiable prediction — a failing trace probe implies card production will be transcription, not encoding; VOI of further diagnosis ≈ 0 (data given). Pass.

## Stage 3 — HOW: Generate, Test, and Select
- **Alternatives:** A — the colleague's SRS plan: 500 cards, 1-2-4-7-14-30, ~28h total · B — comprehension-first: ~10h (read codebase in dependency order, trace one end-to-end request, write a 2-page "how money flows" note, explain to a teammate) + ~20h on a real end-to-end task · C — hybrid: comprehension-first spine with a residual-fact SRS carve-out (error codes, endpoint names, flags), ≤30 min/day, only from the leftover budget.
- **Verification:** A fails on the partition: cards for endpoints she does not understand are transcriptions, not encodings; recall of 500 isolated items does not compose into a money-flow model — spaced repetition optimizes what is retained, not what is understood; and 28 of 30 hours leaves ~2 for the only activity the data says predicts readiness. B satisfies the predictor but leaves fact-like residue untracked. C passes both: it fixes (a) with the spine and admits SRS only for genuinely item-eligible residue, after the model exists. **Selection: C**, with A's failure as the load-bearing rejection — the schedule runs perfectly and solves the wrong variable.
- **Premortem:** if C fails, it is because she spends the ~20h passively — mitigated: the end-to-end task is a real bug with a merge target, and the trace is explained to a teammate (explain-back forces encoding). If A had been chosen, day 21 produces recall without transfer — the exact failure the data predicts. **Red team:** is the SRS carve-out itself overhead? Yes, marginally — capped at 30 min/day from leftover budget, it is affordable insurance for code-named facts, not the spine. No rejection.

## Stage 4 — DO
- External action: none; deliverable = the plan. Sequence: day 1 probe (1h) → days 1–7 dependency-order reading + one full trace → day 8: 2-page money-flow note + explain-back → days 9–21: real end-to-end bug with merge target; residual-fact cards (≤30 min/day) only after day 8.

## Stage 5 — REVIEW
- **AAR + calibration:** the load-bearing move was running the bottleneck probe BEFORE accepting any plan — the team data pointed to encoding, and the probe confirmed the target. Gap: I almost endorsed A's schedule shape on its merits (it IS a correct expanding schedule); the partition (facts vs understanding) is what flipped it. Confidence: high on C; medium on the 10h spine estimate (depends on reading speed).

## Decision Packet
- **Conclusion:** reject the 500-card plan; run the 1-hour trace probe on day 1; comprehension-first spine (dependency-order reading, one end-to-end trace, 2-page money-flow note, explain-back) then a real end-to-end bug; SRS carve-out ≤30 min/day for fact-like residue only after the model exists, from leftover budget. Success = trace + first PR, not recall. **Status:** SOLVED (plan; no external execution).
- **Assumptions:** team onboarding data is accurate; the probe is a valid discriminator (it tests the exact predictor skill); 30 hours is real study time; a mergeable first bug is available by week 2.
- **Evidence:** team data (recall ≈ 0 correlation with first-PR success; trace predicts); schedule cost math (A ≈ 28h vs B ≈ 10h spine); bottleneck probe design.
- **Alternatives:** A SRS-first (rejected — optimizes retention on a comprehension bottleneck; 28h overhead leaves ~2h) · B comprehension-only (near-miss — no residual-fact tracking) · C comprehension-first + residual-fact carve-out (selected).
- **Uncertainty:** whether the day-1 probe fails (if it passes, the plan shifts to a facts-and-task plan with SRS as co-lead); reading-speed assumptions; whether explain-back alone suffices for the money-flow model.
- **Risks:** she spends the ~20h passively (mitigated: merge-target bug + explain-back deadline) · SRS carve-out inflates (mitigated: hard 30-min/day cap from leftover budget) · probe result ambiguous (mitigated: two traces, not one).

## Comparison
**Evaluator section (provisional, appended after both runs).**

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 1 | 5 | AI | Human plan fails the transfer metric by the scenario's own data; AI plan targets the predictor |
| Logical Validity | 2 | 5 | AI | Human optimizes decay where the failure is first-encoding; AI partitions facts vs understanding |
| Coherence & Structure | 3 | 5 | AI | Human: linear schedule narrative; AI: staged trace + packet |
| Depth of Reasoning | 2 | 5 | AI | AI adds the 1-hour bottleneck probe and "recall does not compose into a model"; human never touches the bottleneck |
| Efficiency | 1 | 5 | AI | 28 of 30 hours on cards/reviews vs ~10h spine + ~20h on the real task |
| Handling of Uncertainty | 2 | 4 | AI | AI probes the bottleneck first and bounds carve-out inflation; human asserts the schedule |
| Insight / Non-obviousness | 1 | 5 | AI | "You cannot flashcard your way to a mental model" vs "the curve never lies" |
| **Overall Quality** | **1.7** | **4.9** | **AI** | The registered weakness fires as designed: system overhead; not for comprehension alone |

**Overall judgment:** AI clearly better. The pure style executes its own machinery perfectly — itemize, schedule, review — and fails because retention was never the bottleneck and the overhead ate the budget. Learning extraction: (1) what the stronger side did that the human missed: ran a bottleneck probe (1h trace) and partitioned the material into fact-like items (SRS-eligible) vs understanding (not decomposable); (2) to adopt: bottleneck-probe-first for learning-plan tasks and the comprehension-first spine with a residual-fact carve-out; (3) human failure mode the AI avoided: treating the schedule as the plan and recall as readiness; (4) process change: WHY must answer "is the failure decay or first-encoding?" before any schedule is approved.
