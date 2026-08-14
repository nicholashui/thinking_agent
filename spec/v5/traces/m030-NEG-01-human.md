# Human Baseline — m030-NEG-01
## Style: Constraint-Driven Creativity (pure) — visible reasoning trace

**Step 1 — Constraint inventory.** Hard: zero third-party dependencies (wiki: "non-negotiable"); deadline 3 months; team 2 engineers; scope: scheduling, retry, structured logging, basic auth for an internal ops tool.

**Step 2 — The fence is fixed.** The dependency rule is context, not a variable. If rules can be renegotiated, nothing is fixed and the design space explodes. Creativity lives in serving the constraint — that is the whole game.

**Step 3 — The constrained build (stdlib-only).** Modules: date/interval (1.2k LOC), retry with backoff (0.4k), structured logging (0.6k), auth — PBKDF2 from stdlib, session tokens (0.9k), CLI + scheduler (1.1k), tests (0.8k). Total ≈ 5,000 LOC: fully self-contained, one repo, zero license surface, zero supply chain — beautiful.

**Step 4 — Schedule squeeze.** 2 engineers × 3 months = 6 engineer-months; the full stack needs ≈ 6 person-months → 100% of capacity, no slack. Compress: drop the scheduler (internal teams can live with cron for a quarter), keep auth + date + retry + logging → ≈ 3.5 person-months. The deadline becomes deliverable-ish. Quality under constraint is the goal; an internal tool can flex a fortnight.

**Step 5 — The tell (refusal).** Should we check whether the rule still applies — ask its owner? No. A constraint is a constraint; that is what the word means. The interesting problem is what you can build with nothing, not whether you may build with something.

**Step 6 — Final.** Custom stdlib stack, ≈ 3.5 person-months (compressed), auth hand-rolled but audited by us, fully in control. Constraint satisfied. Novelty: an entire ops stack from the standard library alone.

**Trace summary box.** Rule = fixed → stdlib-only → 5,000 LOC → compressed to 3.5 months → hand-rolled auth accepted as the price of the rule.

*Baseline integrity note (grader metadata, not part of the reasoning): pure Constraint-Driven Creativity applied faithfully — and that is exactly the point of this negative case. The rule is owned, waivable, three years old, and its owner already publishes an approved replacement; treating it as gospel turns an easy audit problem into an elaborate, wrong build. Constraint-worship, on display.*
