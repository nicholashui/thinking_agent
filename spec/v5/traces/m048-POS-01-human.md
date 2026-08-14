# Human Baseline — Systems Thinking in Supply Chain — m048-POS-01
**Style enforced (pure): model the chain: stocks, flows, delays, information distortion; find the bullwhip's policy lever. Full visible trace.**

## 1. Map the system: stocks, flows, delays, loops
- **Stocks**: inventory at each echelon (retailer, distributor, factory) plus pipeline stocks (1 week in transit per link). **Flows**: customer demand (exogenous), orders, shipments.
- **Delays**: 1-week order-shipment delay per echelon — the loop's inertia; the correction signal lags the flow.
- **Feedback loops**: (a) inventory-correction loop per echelon — order-up-to: order = forecast + (target - position), correction 100% per period, so inventory error feeds straight into order variance; (b) the *information loop*: each echelon re-forecasts its downstream partner's order stream as if it were demand. Loop (b) is the bullwhip engine: orders are a noisier transformation of demand, and the next echelon amplifies the transformation again. The chain is a cascade of variance multipliers whose size is set by the RULE (forecast window p, lead time L) — not by the factory, not by demand.

## 2. Quantify the multiplier (checkable arithmetic)
Order-up-to + moving-average forecast of p periods, lead time L: variance multiplier = 1 + 2L/p + 2L^2/p^2 (Chen et al. bound, tight here).
- Today: p = 1, L = 1 -> multiplier = 1 + 2 + 2 = **5 per echelon**.
- Customer demand var 100 (sigma 10) -> retailer orders var 500 (sigma ~22.4) -> distributor orders var 2,500 (sigma 50) -> factory orders var 12,500 (sigma ~112).
- The distributor's "demand is 5x more volatile at our level" is exactly sigma 50 vs 10 — the multiplier made visible at the first echelon, *before any production is involved*.

## 3. Where the bullwhip comes from — and where it doesn't
- Not customer demand (sigma 10, stable). Not the factory: its input IS the distorted signal; it amplifies because it responds to orders, not demand. The cause is the per-echelon decision rule + the missing information link: no echelon sees end-customer demand.
- The CEO's $2M flexible-production investment attacks a symptom (factory swing) by adding capacity to absorb an artificial signal 11x louder than real demand (sigma 112 vs 10). It leaves the rule that manufactures the variance untouched — the structure re-expresses the same swings, just at lower capacity utilization.

## 4. Policy levers, ranked with numbers
- **L1 — Share end-customer demand** (all echelons forecast the same series; order-up-to applies once): compounding removed -> factory sigma ~22 (var 500). Weeks, ~$50k. ~5x sigma reduction.
- **L2 — Smooth the forecast (p = 1 -> 4)**: multiplier 5 -> 1.625. With L1: factory sigma ~12.7 (var 162.5). Combined ~9x sigma reduction vs today (~77x variance).
- **L3 — Shorten lead times (L = 1 -> 0.5)**: multiplier 5 -> 1 + 1 + 0.5 = 2.5. Attacks the delay — the loop's inertia.
- **L4 — De-batch orders; end price promotions**: removes amplifiers the bound assumes away.
- Inverse check: add capacity but no rule change -> factory still receives var 12,500 orders; $2M chases a signal the chain manufactured. The lever is upstream of the factory, in the rule and the information flow.

## 5. Verification & limitations
- The bound is exact for i.i.d. input; compounding across echelons is approximate (order streams are serially correlated) — confirm with a 1-week spreadsheet/simulation before rollout.
- Transient: rule changes take effect over a planning cycle; do not judge during the adaptation phase.

## 6. Recommendation
Adopt L1 + L2 first (demand-info sharing; p=4 smoothing): weeks, ~$50-100k, expected factory order sigma 112 -> ~13. Defer the $2M flexibility CAPEX until the rule fix lands (likely unneeded). Re-simulate; then consider L3 with suppliers.

## Conclusion
The bullwhip is manufactured by decision rules and missing information, not by demand or production. The leverage point is the ordering rule (smoothing) and the information flow (shared demand data) — verified: 5x per echelon today, 1.625 with p=4, sigma 112 -> ~13 with both levers. The loop model found the lever; the checkable math proves it.
