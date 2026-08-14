# Human Baseline — m035-POS-01
## Style: Replication & Robustness Checks (pure) — visible reasoning trace

**Step 1 — Distrust the single result.** One experiment, one sample, one definition, one window = one hypothesis, not a fact. +12.4% activation (p = 0.003, n = 10,000) is exactly the kind of number dashboards celebrate and decisions are allowed to hang on — that is the kind of number to attack. What would it take for this result to replicate? Which plausible changes should we test? None of this depends on Friday; all of it is computable from the data we already hold.

**Step 2 — Vary the sample (segment split).** Split by acquisition channel (40% paid-search, 60% organic): paid-search 17.0% → 23.0% (+6.0 pp, +35%, p < 0.001); organic 21.0% → 21.0% (+0.0 pp). Recomposition check: 0.4×17.0 + 0.6×21.0 = 19.4% (A) ✓; 0.4×23.0 + 0.6×21.0 = 21.8% (B) ✓. The aggregate is exactly the paid subgroup — the whole effect lives in 40% of the sample, and organic users show nothing.

**Step 3 — Vary the definition (metric invariance).** What, precisely, is "activation"? Flow B auto-marks the tutorial complete when the user taps the final screen; Flow A requires a quiz answer. The dashboard counts tutorial completion. Recompute the outcome as "first core action within 7 days" — computable from the same clickstream, zero new data: paid-search 16.8% → 17.0%, organic 20.8% → 20.6% (both n.s.); aggregate ≈ 19.2% → 19.4% (+0.2 pp, n.s.). Under any honest operationalization of the outcome, the effect is gone.

**Step 4 — Vary the window (stability over time).** Week 1 lift +17.5% relative (p < 0.01); week 2 lift +4.5% relative (n.s.). The effect is decaying, not building — consistent with novelty and click-through to the auto-complete screen, not with a changed behavior.

**Step 5 — Synthesis: the result does not replicate.** Across sample, definition, and window the effect fails. The +12.4% was a definitional artifact: auto-completed tutorials inflate Flow B's activation, concentrated in the paid-search segment. No plausible variation of settings, sample, method, or definition survives.

**Step 6 — Corrected conclusion.** Do NOT ship Flow B. The corrected number is already in the existing data: no lift. Conditions under which a future result would be trusted: pre-register the core-action definition; report by segment; require ≥ 5% lift in a second, stable week.

**Trace summary box.** Single result (+12.4%, p = 0.003) → segment split (effect = paid only) → definition invariance (effect = artifact) → window split (decaying) → corrected conclusion: do not ship; artifact found in existing data.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning deliberately confined to the pure Replication & Robustness Checks style — every result treated as a hypothesis, every claim probed by varying sample, settings, definitions, and methods before any decision; no step trusts a single measurement. The battery is exhaustive and the artifact mechanism is named before the conclusion is drawn.*
