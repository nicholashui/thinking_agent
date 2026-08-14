# v6 Routed AI Trace — m100-POS-01 (blinded)
## Vesper Logistics — meet 16,800 deliveries/week in 6 months (capacity sizing)
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,product,science,security,software,supply | g:decide,estimate,maximize | c:deadline
- Router top3: m100, m044, m070; confidence gap > 0.5 → CONFIDENT single route: m100 first-class (rebuild + hardest-falsification contract), m044/m070 = context. No R3 gate in route (goals carry no guarantee). Flags: tempo mode ON (P2 — decision is now, 6-month lead); P3 branch-completeness required; no P8 fast path (route norm at volume is unmeasured → not fully specified).
### WHAT — frame + structure-first scan (S1)
- Deliverable: resourcing plan sized to 2,800/day; the proposal's load-bearing claim is "vans bind." Structure: throughput = min(vans, drivers, docks, pick) × deliveries/van-day (route norm 50; union 10-hr cap with admin buffer).
### WHY — P1 input-provenance audit
- MEASURED (trust): 40 vans, 52 drivers, 4 docks (8 min → 300 van-trips/day), pick 60 loads/day (18,000/wk), 12,000/wk at 50/van-day. INTERESTED-PARTY (grade down): "40% idle = headroom" — sales director (wants no spend) and ops lead (wants vans) each read the same utilization report to their own conclusion; utilization is a van-level fact, not dispatchable capacity. Falsifier per claim: C1 "drivers bind" (falsifier: idle vans runnable without new drivers); C2 "norm 50 holds at volume" (falsifier: effective norm ~47 at 2,800/day); C3 "10-hr cap rigid in-window" (falsifier: flex available inside 6 months).
### HOW — style passes (first-class, single route)
- Pass R (rebuild + hardest-falsification contract): rebuild — 2,800 ÷ 50 = 56 van-days → 56 vans + 56 drivers; docks (300/day) and pick (18,000/wk) not binding; drivers bind first (52 < 56) → "double the vans" treats the wrong pool as the constraint. Falsify HARDEST: A1 utilization-as-headroom ("40% idle → no spend"): half-right — vans do idle (8.3 vs 12.5 trips), but filling to 70/van-day = 11.7 trips ≈ 9.85 hrs at/over the work-rule edge without OT (banned), and idle van-hours are not dispatchable without drivers: 12 spare drivers cap the fleet at 52 × 50 × 6 = 15,600/wk < 16,800 → rejected. A2 norm-degradation ("50 → ~47 at 2,800/day"): PARTIALLY SUCCEEDS — 2,800 ÷ 47 ≈ 60 van-days; a bare 56/56 plan has no buffer → revise: 20 vans + 8 drivers + pre-committed re-measure at the new load. A3 union-flex ("lift the 10-hr cap"): fails in-window (agreement 9 months, demand in 6) → not a lever.
- Pass S (stakeholder context, m044): union (contract = binding constraint), drivers (work-rule ceiling), sales (no-spend bias), ops lead (van-purchase bias) — the plan must survive the driver/union pools, not the sales narrative.
- Pass E (evidence-weighted context, m070): "40% idle" graded measured-but-misread; "don't spend on anything else" unvalidated; "demand +40%" firm (verified ops data).
- Synthesis (V1–V3): style pass and general route AGREE (20 vans + 8 drivers ≈ $1.4M) → proceed; agreement recorded.
### GATES — P3 branch-completeness (route: no R3 gate)
- Failure branch priced before DO: norm degrades beyond −6% → second tranche + re-measure gate absorbs it; demand misses → low-regret (no overbuild); hiring misses the 6-month window → start immediately, escrow tranche 2.
### DO — P2 tempo commit
- Commit: buy 20 vans + hire 8 drivers (~$1.4M, half the naive $2.8M); re-measure the effective norm at 2,800/day before tranche 2; revisit the driver cap at month 9.
### REVIEW — insight pass (S2, packet gate)
- I1: the naive 40-van plan fails its own target — 80 vans still deliver 52 × 50 × 6 = 15,600/wk; extra vans are decorative without drivers.
- I2: the utilization report is the trap: "40% idle" dissolves at the pool level — idle van-hours are a scheduling artifact, not a capacity reserve.
### DECISION PACKET
- Conclusion: meet 16,800/wk with ~20 vans + ~8 drivers (~$1.4M); the double-fleet plan is refuted by its own numbers; re-measure the norm; revisit the cap at month 9.
- Status: SOLVED (decision brief; no external execution). Assumptions: norm 50 = enforceable work-rule ceiling; cap rigid through month 9; demand firm; docks/pick steady.
- Evidence: 2,800/day = 56 van-days; drivers 52 < 56 bind; docks 300/day, pick 18,000/wk free; 70/van-day = 9.85 hrs past the work-rule edge; 52 × 50 × 6 = 15,600 < 16,800; 2,800 ÷ 47 ≈ 60 van-days.
- Alternatives: 40 vans $2.8M (rejected — 15,600/wk shortfall); headroom-only (rejected — no dispatchable capacity); bare 56/56 (rejected — zero buffer vs norm degradation); 20 vans + 8 drivers + re-measure (selected).
- Uncertainty: effective norm 47–50 band (dominant risk); demand variance; hiring lead time vs window. Risks: norm degrades beyond −6% (second tranche absorbs); hiring miss (start now); union opens early (upside).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | identical plan vs reference (~20 vans + 8 drivers ≈ $1.4M) |
| Logical Validity | 5 | 5 | Tie | same pool decomposition; same refutations of 40-van and headroom plans |
| Coherence & Structure | 4 | 5 | AI | routed first-class pass + gate + packet vs linear first-pass narrative |
| Depth of Reasoning | 5 | 5 | Tie | falsification contract now matches the baseline's attack pass, falsifier per claim, outcomes recorded |
| Efficiency | 5 | 4 | Human | human names the trap first-pass; v6 pass is targeted but contract-mandatory |
| Handling of Uncertainty | 3 | 5 | AI | AI sizes the norm band + re-measure gate in the packet; human asserts more |
| Insight / Non-obviousness | 5 | 5 | Tie | trap-dissolution and 15,600 refutation on both sides |
| Overall Quality | 4.6 | 4.9 | AI | the routed pass closes v5's depth gap and adds provenance-graded evidence |

Winner: AI (narrow). Why: the routed style pass made the hardest-falsification pass a first-class pre-selection contract (v5 ran it as a post-selection premortem — the baseline's decisive edge in v5), and added provenance-graded utilization evidence plus a packet that sizes the norm band with a re-measure gate; the baseline remains the model the pass now matches.
