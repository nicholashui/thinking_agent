# Human Baseline — Systems Thinking — systems-POS-01
**Style enforced: Systems Thinking (feedback loops, stocks & flows). Full visible trace.**

## 1. Map the system: stocks, flows, structure
- **Stocks**: cars currently on each segment (S→A, A→T, S→B, B→T). The network is a flow-conservation system: every departing car is in exactly one stock at a time.
- **Flows**: commuter departures per day; route-choice decisions — a slow, adapting flow. Drivers update based on yesterday's experience, so the system state and the choice flow are coupled with a **delay** (days–weeks of learning).
- **Feedback loops**:
  - **Balancing loop B1 (congestion equilibrium)**: more cars on a narrow bridge → longer bridge time → that route looks worse → drivers shift off it → cars redistribute. B1 is what holds the system in a stable user equilibrium: all used routes end up with equal travel time.
  - No reinforcing loop exists *today*, but the proposed connector changes the STRUCTURE. In a system with B1-style congestion feedback, the equilibrium is an emergent property of many local optimizers. I must re-derive the equilibrium after the change — not extrapolate linearly from today.

## 2. The trap in the naive argument
"More capacity → less congestion" is a one-loop, linear story. It ignores that the outcome here is a **user equilibrium** (each driver minimizes own time), and individual rationality is not the same as collective optimality. When you add a link to a congested network, you change the strategy space; drivers can be *forced* onto a route that is worse for everyone. This is the classic "the fix backfires" / more-roads-more-congestion paradox. Intuition is not evidence — compute both equilibria.

## 3. Current equilibrium (before the connector)
Narrow segments: t(x) = x/100 min. Wide segments: 45 min flat. 4,000 cars total.
- Route 1 (S→A→T): x/100 + 45
- Route 2 (S→B→T): 45 + y/100, with x + y = 4000
- Equilibrium (B1 settles all used routes to equal time): x/100 + 45 = 45 + (4000 − x)/100 → x = 2000.
- Result: **65 min per driver** (20 bridge + 45 highway).
- No-deviation check: a driver switching makes their chosen bridge slightly longer → 65.01 > 65 → nobody improves by deviating. Stable.

## 4. New equilibrium (after adding connector A→B, t = 5 min)
New option: S→A→B→T = x/100 + 5 + y/100 (uses both narrow bridges).
- Compare with Route 1: (x/100 + 45) − (x/100 + 5 + y/100) = 40 − y/100 ≥ 0 since y ≤ 4000, with equality only when y = 4000 (all traffic already on Route 2's bridge).
- So the shortcut is **always at least as fast as Route 1**, and strictly faster whenever Route 2 carries any traffic. Symmetrically it always beats Route 2. Because congestion feedback (B1) re-equilibrates any split, the only stable state is: all 4,000 cars on the shortcut.
- Result: **85 min per driver** (40 + 5 + 40).
- No-deviation check at the new equilibrium: Route 1 = 40 + 45 = 85; Route 2 = 45 + 40 = 85; shortcut = 85. All equal → no driver can improve → stable.

## 5. Unintended consequences, delays, leverage points
- The $40M connector makes 4,000 commuters **20 minutes worse off every day** (65 → 85, a 31% increase). The fix backfires in the worst possible way: a strictly dominant new route drags the whole system to a worse equilibrium.
- **Delay dynamics**: right after opening, drivers discover the shortcut gradually; times will oscillate during the learning phase. The planner must not mistake the transient for the steady state — the equilibrium prediction is the endpoint.
- **Leverage point**: the structure, not the capacity. The perverse equilibrium exists only because the connector is free at the margin. Two structural levers restore 65 min: (a) remove the connector; (b) **price the connector** so that its marginal cost re-equalizes the split (a toll worth ~25 min at the 2,000/2,000 split restores indifference). The lever is the flow's price, not the link's size.

## 6. Recommendation
- Do NOT build the connector as proposed; cancel the $40M.
- If politically forced to build: impose an immediate usage price on the connector calibrated to keep the equilibrium at 65 min, or restrict it to managed/HOV use.
- Before any final commitment: run a microsimulation with driver adaptation and verify the equilibrium numerically; then monitor 2–4 weeks post-change — B1 will reveal the true equilibrium.

## Conclusion
The council's linear reasoning is wrong. Adding the connector converts a 65-min user equilibrium into an 85-min one — verified, not intuited. Systems Thinking converts the paradox possibility into a quantitative, checkable prediction and points the intervention at the structure (price/remove the link) rather than the symptom (build more).
