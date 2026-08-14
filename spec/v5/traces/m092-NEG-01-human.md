# Human Baseline — m092-NEG-01
## Style: Spaced Repetition & Memory Science (pure) — visible reasoning trace

**Step 1 — The scientific plan.** The problem is retention: 21 days from today to first-bug-fix readiness, and everything she reads today will decay by then. The answer is expanding intervals: 1-2-4-7-14-30. Convert the platform documentation into 500 items — endpoints, config flags, table schemas, retry policies, error codes. ~12 hours of production, ~16 hours of reviews. It is a plan with a shape.

**Step 2 — Itemize.** Every endpoint is a card: POST /v1/payments — what it takes, what it returns. Every flag: RETRY_MAX = 3, its default, where it lives. Every error code: what it means, where it is thrown. The schedule is the method: review when decay bites, widen the gaps as the half-life grows. By day 21 every item has been seen six times with growing gaps — that is how you make knowledge durable.

**Step 3 — Execute.** Days 1–7: production — the cards themselves force the reading; the encoding is the first exposure. Days 7–21: daily 45-minute reviews on the expanding schedule. Day 14 check-in: recall is above 90% per the curve. The curve never lies.

**Step 4 — Day 21: the failure.** She can recite the endpoint list, every retry policy, every error code. And she cannot trace one payment request end-to-end. The team's own data said exactly this would happen: recall of facts has near-zero correlation with the first bug fix; the ability to trace money flow predicts it. I optimized what decays — but nothing had been understood yet, so there was nothing for decay to protect. The first pass was the problem, and I never touched it.

**Step 5 — What the overhead cost.** 28 of 30 hours went to cards and reviews; ~2 remained for the actual task. The comprehension-first path — reading the code in dependency order, tracing one real request, writing it down, explaining it — is ~10 hours, and it is the only thing the data says predicts readiness. My schedule ran perfectly and solved the wrong variable.

**Step 6 — The partition I missed.** Facts — endpoint names, flags, codes — are items: they can be scheduled. Understanding is not an item: you cannot decompose "how money flows through the system" into 500 cards and expect recall of the pieces to compose into the model. Retention engineering applies AFTER comprehension exists, to the residue — not before, to the whole.

**Trace summary box.** plan: 500 cards, 1-2-4-7-14-30, 12h production + 16h reviews · executed on schedule · day-21 result: recall ~90%, trace = fail · team data: recall ≈ 0 correlation with first PR; tracing predicts · cost: 28 of 30 hours, ~2 left · diagnosis: bottleneck was first-pass comprehension, not decay · partition missed: facts are schedulable, understanding is not decomposable.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Spaced Repetition & Memory Science — which is the point: the style's own machinery (itemize → schedule → execute → expect durable retention) is applied correctly and fails, because the scenario's bottleneck is comprehension and the overhead consumes the budget. This is the registered weakness: system overhead; not for comprehension alone.*
