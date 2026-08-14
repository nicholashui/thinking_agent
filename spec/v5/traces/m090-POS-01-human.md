# Human Baseline — m090-POS-01
## Style: Minimum Viable Experiment (Build-Measure-Learn) (pure) — visible reasoning trace

**Step 1 — Find the one assumption the whole decision hangs on.** The $450K and 12 months rest on a single claim: executives at current accounts will actually USE a mobile analytics channel. Engineering, design, rollout — all execution. So the question is: what is the smallest test that would validate or kill THAT claim?

**Step 2 — Downgrade the non-evidence.** The 71% survey is not a signal. People say yes to anything you ask for free — asking is not measuring. And the WaveMetrics "lost deals" line is a sales story, not a funnel. I have 800 named executives I can reach today; opinion is a prior, behavior is the only evidence.

**Step 3 — Design the smallest test that produces BEHAVIOR.** Fake-door: 2 weeks, ~$2K, 3 engineer-days — put a "Mobile dashboard — get early access" gate in-app and in the weekly email to all 800 execs; count who clicks and who joins the waitlist. That is the smallest thing that makes people act, not answer. Thresholds BEFORE the data: ≥120 signups (15% of 800) or ≥20% click-through keeps the assumption alive; below that, kill.

**Step 4 — Graduate to the second loop only if the first passes.** Concierge: 20 accounts, 3 weeks, ~$12K — daily digest of 3 key metrics + a read-only mobile view on the existing API; bar: ≥40% weekly-active execs. The concierge is not a bigger survey; it is usage.

**Step 5 — State what the test does NOT test.** Retention past 3 weeks, platform lock-in, expansion revenue — none of it. Those are the NEXT experiment's questions, earned only by passing these gates. A probe validates one assumption, not the product — never confuse the two.

**Step 6 — Gate and price the option.** The 12-month build fires only if both gates clear. Kill-now costs $2K; committing now costs $450K against a 71% opinion. The survey isn't a shortcut past the test — it is a prior that made the test cheap to design. If the fake-door misses, the 4 engineers go back to the roadmap features.

**Step 7 — Recommendation.** Run the fake-door this Monday. Kill on a miss; build only on two passed gates.

**Trace summary box.** core assumption = executive WILL-USE (behavior) → survey/competitor story downgraded → smallest behavioral probe: fake-door (2 wks, ~$2K, ≥120/800 or ≥20% CTR) → second loop: concierge (3 wks, ~$12K, ≥40% weekly-active) → $450K build gated on both → not-tested declared (retention/lock-in/expansion) → option priced: $2K kill vs $450K commit.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Minimum Viable Experiment (Build-Measure-Learn) — the smallest validating test for the core assumption is designed first, non-behavioral evidence is downgraded, thresholds are pre-committed, and the commitment is gated on the results. Signature move: "asking is not measuring — only action validates."*
