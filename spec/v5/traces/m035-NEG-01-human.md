# Human Baseline — m035-NEG-01
## Style: Replication & Robustness Checks (pure) — visible reasoning trace

**Step 1 — Distrust the single null.** One study, one vendor, one definition, one platform mix: control 31.4% vs treatment 31.6% (+0.2 pp, n.s., n = 20,000, 8 weeks). A null from a single measurement settles nothing. Absence of evidence is not evidence of absence — a launch decision cannot rest on this.

**Step 2 — Enumerate the robustness battery.** What would it take for this null to be trustworthy? (1) Different sample: n = 30,000, rebalanced segments, fresh cohorts; (2) different settings: Android and iOS analyzed separately, three platform mixes; (3) different method: second analytics vendor, independent instrumentation; (4) different definitions: 4-week and 8-week retention, alternate churn operationalizations; (5) different windows: weekly and monthly analysis granularity; (6) different analyses: per-cohort, per-platform, and pooled.

**Step 3 — Pre-register the replication.** 12 weeks, n = 30,000, second vendor, all five variations above, thresholds fixed in advance (reject the null only at ≥ 0.5 pp with α = 0.01). Cost: ≈ $40k and the full quarter.

**Step 4 — Defer the decision.** Until the replication reports, no launch decision is trustworthy — single-study nulls have overturned before. The feature stays gated. The seasonal dip and the competitor's window arrive while the replication runs; that is the price of rigor, and a false launch would cost more.

**Step 5 — Decision statement.** Fund and run the replication; decide at week 12. (The trace ends here: the style's prescribed path.)

**Trace summary box.** Single null → distrust → 6-variation robustness battery → 12-week, $40k replication → decision deferred past the seasonal and competitive windows. Rigor preserved; timing lost.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning deliberately confined to the pure Replication & Robustness Checks style — and it fails exactly as the registry predicts ("time cost; can become ritual"). Every move is variance-side (samples, settings, methods, definitions, windows); the measurement layer is never audited. The client-side heartbeat silently drops 31% of sessions (Android 13+ background limits, ad-blockers), missingness correlates with the very churn the feature targets, and the second vendor's SDK is the same client-side class — the replication faithfully reproduces the blind spot. The style checks whether the result varies; it never asks whether the instrument measures what it claims.*
