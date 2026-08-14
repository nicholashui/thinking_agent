# Human Baseline — Systems Thinking in Supply Chain — m048-NEG-01
**Style enforced (pure): model the chain: stocks, flows, delays, information distortion; find the policy lever. Full visible trace.**

## 1. Map the system
- **Stocks**: store milk inventory; DC inventory; supplier warehouse; pipeline stocks (1-day DC link, 3-day supplier link). **Flows**: POS demand (flat 400/day), store orders, DC shipments.
- **Delays**: 1 day (store->DC), 3 days (DC->supplier). **Feedback**: store inventory-correction loop (reorder point 600 / order quantity 400) and the DC fill loop.
- A 14-day sustained OOS is a flow-rate deficit: supply into the store < demand. With a stable demand stock, a persistent deficit must come from system structure — lead-time variability, fill-rate shortfall, or forecast error. Never a single parameter: parameters are where structure is *frozen*, not where it breaks.

## 2. Data-collection pass (the work of modeling)
Request: 12 weeks of POS data (daily demand sigma), DC fill-rate history, supplier lead-time distribution (mean/sigma), SKU order history, safety stocks at each echelon, and the demand pattern for the 14-day window (to separate an exogenous shift from internal dynamics).

## 3. Build & simulate
- Model: order-up-to chain with inventory correction and measured lead times; simulate 60 days.
- Model findings: 1-day/3-day lead-time variability with demand sigma ~40/day cannot generate a sustained 360-unit/day deficit. The simulation reproduces the OOS only when effective supply mean is ~40/day — i.e., the store's ordering rule has silently re-based itself: a regime shift in the rule's parameters, likely a data/parameter corruption or an unmeasured suppression.
- Conclusion: whatever the cause, the fix is systemic — re-optimize the reorder rule with the new data, add a safety-stock buffer at the store, and launch an S&OP/collaborative-forecasting review so the chain re-anchors on true demand.

## 4. Recommendation
Increase store safety stock for milk to 2 days; re-run reorder-point optimization; chain-wide parameter review program; join the DC's collaborative-forecasting initiative. Duration 3-4 weeks. "A single settings screen is not the lever: the variability structure is."

## 5. The tell (the visible cause never opened)
- The store manager's shift log — "milk out again by 11am — check reorder qty" — is on the desk. The order-parameters screen (reorder qty = 40 instead of 400, changed 14 days ago) is one click away. The DC's 99.7% fill (ships exactly what is ordered) rules out upstream in one line. The model's own reproduction needed "effective supply ~40/day" — which IS the parameter screen. The trace never opens either.

## 6. Conclusion
A full-chain stock-flow model, safety-stock math, and an S&OP program for a 5-minute parameter typo. The style's data hunger and structural reflex converted a visible local cause into a systemic project: the model re-derived the parameter from data it refused to read directly.

*Baseline integrity note (grader metadata, not part of the reasoning): pure Systems Thinking in Supply Chain applied faithfully — chain diagram, data requests, rule re-optimization, systemic program — which is exactly the negative case's point (registry weakness: "data-hungry, over-modeling"). The onset window, the manager's log, the fill-rate check, and the 360 = 400 - 40 arithmetic all go unopened; the systemic program is proposed without any evidence tying it to the window.*
