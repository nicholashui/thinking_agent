# Human Baseline — Systems Thinking — systems-NEG-01
**Style enforced: Systems Thinking (feedback loops, stocks & flows). Full visible trace.**

## 1. Map the system: stocks, flows, loops
- **Stocks**: work-in-process (orders inside the DC), the mislabel/rework queue (returned parcels), the late-shipment backlog.
- **Flows**: order inflow (flat, ~steady), pick→pack→ship flow, rework flow (returned parcels re-enter processing after ~2 days), outflow of shipped orders.
- **Feedback loops**:
  - **Reinforcing loop R1 (spiral)**: late deliveries → client complaints → account-loss risk → budget pressure / cost-cutting → under-resourcing → more late deliveries.
  - **Balancing loop B1 (rework)**: mislabels → rework → higher WIP → congestion and time pressure → more mislabels. A "worse-before-worse" loop with a rework delay of ~2 days.
  - **B2 (capacity response)**: delays → management adds capacity → delays decrease (this is management's preferred narrative — but in a flat-volume regime B2 has no driver).
- **Key delays**: rework adds ~2 days; R1 operates on a 3–8 week timescale (complaints, contract cycles).
- **Leverage points** (from structure): (1) break R1 at its source — stabilize the client relationship and add buffer stock so the spiral cannot amplify; (2) the fast, high-leverage entry is the rework loop B1 — smooth WIP, change batching rules, cross-train to absorb variance; (3) demand-side smoothing of inbound orders.

## 2. Reading the data through the model
- Station-3's 30% error rate (vs ~2% elsewhere): a local station is where system stress *manifests* — stations always express pressure differentially. Treating the station treats the symptom; the stress will re-express elsewhere (the bottleneck shifts). The diagram explains this before any measurement: it is B1 running hot at its weakest node.
- Flat order volume: superficially it weakens R1 — but R1 can run on **internal rework** alone; the delay data *lags* the loop by design, so the absence of demand growth does not falsify the spiral.
- Delay–error correlation (r ≈ 0.97): correlation is not mechanism. The error rate is *itself driven* by the rework loop (pressure → errors → more rework), so the correlation is exactly what B1 predicts. The maintenance flag on the printer is likewise downstream noise — a worn part is what a stressed system breaks.
- The model is consistent with every datum; no datum is inconsistent with the model. The structure is the explanation.

## 3. Prescription (structural, leverage-point driven)
- Implement the structural intervention (8–12 weeks): WIP smoothing + batching redesign + cross-training, piloted on one shift, with before/after delay-distribution measurement.
- Do NOT replace the printer as the primary intervention: after the "fix," error rates will re-emerge at another station; a one-off equipment replacement is treating the symptom and buys at most a week.
- Negotiate the client timeline: present a roadmap with early wins (e.g., batch-level priority lanes) rather than promising a one-week cure that the system will not deliver.

## 4. What this analysis does not do
- I have not measured the loop variables (WIP levels, rework fraction over time, complaint escalation rates). I reason from the structure; the data on hand is consistent with the diagram, so the diagram stands. Station 3 is where the loop shows itself *today*; tomorrow it will be another station — that is the signature of a system problem.

## Conclusion
This is a systemic delay-and-rework problem, not an equipment failure. The correct intervention is structural (redesign the batching/rework flows and stabilize the client-facing loop), not local. Fixing Station 3's printer would be addressing a symptom, and the delays would return.
