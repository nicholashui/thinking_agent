# Human Baseline — m096-POS-01
## Style: Ensemble Thinking (Diverse Views Averaging) (pure) — visible reasoning trace

**Step 1 — Collect the estimates; lay out what each one IS.** Ten numbers from ten different measurement systems: shifts-observed tags, dock counts, credit-memo/RMA volume, scaled complaint tickets, a 3% inspection extrapolation, ERP return entries, a 3-day manual count, supplier defect records, one visual read. Let me table them:

| Channel | Type | Estimate |
|---|---|---|
| Ops manager | observed damage tags | 3,420 |
| Warehouse lead | dock defect counts | 2,780 |
| Finance | credit memos / RMAs | 3,350 |
| Customer service | complaint tickets scaled | 2,850 |
| Carrier | transit claims scaled | 3,320 |
| Quality engineer | 3% sample extrapolation | 2,900 |
| Data analyst | ERP return entries | 3,240 |
| Dock supervisor | 3-day manual count ×7 | 2,980 |
| Supplier | line defect records | 3,190 |
| Line worker | visual read | 3,020 |

**Step 2 — Verify independence, not just diversity.** Ten different labels is not the same as ten independent signals. Independence means: no shared input, no draft-sharing, no common anchor. Here the channels are structurally separate — dock counts and credit memos and carrier claims catch each other's gross errors precisely because they cannot share one. No one saw anyone else's number. Precondition holds.

**Step 3 — Average.** Mean = 3,105. (Cross-check: median 3,105, trimmed mean 3,106 — the aggregation is stable. That stability is itself the fingerprint of independence.)

**Step 4 — State the spread.** SD ≈ 216, range 640. Interval: 3,105 ± 430 (95% band 2,675–3,535). The average without the spread is a lie — the spread is the honest output.

**Step 5 — Why the average beats the best single estimate.** Whoever's closest is luck; the average is structure. The ops manager overshot (3,420) and the warehouse lead undershot (2,780) — neither "bias" is information, they are noise, and noise cancels. One of these ten will turn out to be the closest single — almost certainly not the one anyone would have predicted — and the average will still beat nearly all of them.

**Step 6 — Do not trim without a cause.** The line worker's 3,020 is a real channel with real access; dropping it would not be robustness, it would be cherry-picking. Trim only a source that fails the independence check.

**Step 7 — Recommendation.** Forecast: 3,105 units/week steady-state; interval 2,675–3,535. Condition stated: this works ONLY because the channels are independent — if all ten had read the same report, averaging would be herding and the spread would be a lie.

**Trace summary box.** 10 channels audited (distinct measurement systems; no shared input; no draft-sharing) → mean 3,105 / median 3,105 / trimmed 3,106 → SD ≈ 216, interval ±430 → ensemble justified by error cancellation; failure condition (dependence) declared.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Ensemble Thinking (Diverse Views Averaging) — collect independent estimates, verify structural independence of sources, average, state the spread. Signature move: "Whoever's closest is luck; the average is structure — but only when the sources are independent."*
