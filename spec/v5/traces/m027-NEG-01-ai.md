# AI Thinking Agent Run — m027-NEG-01
**Agent process**: META-CONTROL → WHAT → WHY → HOW → DO → REVIEW (with VERIFY layer). Blinded run: no thinking-model name or style information provided.
## META — Context, stakes, effort
- Facilities/operations problem at a residential tower: peak elevator waits. Constraint-bound domain (capacity, availability, contract). Moderate stakes (500 residents, measurable waits, $45–60K budget fork). Analytical-advisory, no external execution. Effort: capacity arithmetic + evidence routing.

## WHAT — Frame
- "Decide where the elevator fix lives: user experience or capacity/availability — and produce a costed recommendation in 4 weeks." Key question: "Is the binding constraint preference (UX) or physics/availability (throughput)?" Metrics: wait arithmetic matched to measured waits; constraint identified from logs; app proposals capacity-tested; costed option stated. Gate check: pass.

## WHY — Hypotheses, evidence, falsification
- H1 perception/UX (buttons, lobby, no arrival info): survey 74% "slow" — but perception does not explain a 2.3× wait degradation with occupancy unchanged. H2 availability: maintenance logs — Car B out of service ~30% of the last 12 months, bearing/shaft issues, 6-week repair backlog, 5-day SLA, parts on backorder; during the 2-week Car-B outage, waits rose ~3.5 → ~8 min at normal occupancy. H3 throughput: two 25-person cars; 8:45–9:15 surge ≈ 300 persons; single-car operation → ≥12 loads → ~6–8 min minimum, matching measured 6–9 min peaks and the outage period.
- Falsification: H1 alone fails — if UX were the mover, the 2.3× outage degradation could not occur. H2+H3 survive arithmetic; with both cars up the baseline ~3.5 min is recovered, which the logs' non-outage periods confirm. G-WHY: pass — capacity is evidenced; UX is not the mover.

## HOW — Generate, test, select
- A — UX program as the fix: call-ahead app, lobby redesign, panel redesign, arrival displays (rejected as primary: adds zero cars; a call-ahead app lengthens real waits by summoning guests ahead of queued residents; resident delight is not throughput evidence). B — Constraint-first: expedite Car B repair (expedited parts, SLA renegotiated 5-day → 72h, penalty clause), express-bypass floor for the surge, destination-based group dispatch, honest status signage ("Car B out of service — expected 9/1"). C — B as spine plus the single UX element that reduces both real and perceived wait: truthful status (also kills phantom-car callbacks that jam the button system).
- Verify: B/C pass capacity arithmetic — two cars clear a 300-person surge in ~3–4 min with dispatch grouping and an express floor; A fails it (0 cars added, waits unchanged or worse). Feasibility: dispatch-controller retrofit is architecturally feasible per brief; parts lead time is the risk. Selection (record): C — constraint as the spine, truthfulness as the only UX that does real work.

## DO
- Attestation: advisory recommendation, class A2; no live execution.

## REVIEW — After-action review
- What went well: capacity arithmetic done before any empathy claim; app rejected on physics, not taste; user evidence used where decision-relevant (phantom-car calls → signage).
- To record: (1) A 30% outage with a 6-week backlog is a procurement-contract failure as much as a mechanical one — the fix must target the SLA and parts pipeline, not just the machine. (2) Signage-only without a restoration date is credibility theater in reverse — publish nothing until the date is firm. (3) Express floor and group dispatch interact; interaction unmodeled — simulation before commitment. Folded back as risks.

## Decision Packet
- **Conclusion**: Fix the constraint (C): expedite Car B repair with parts expediting and SLA renegotiation to 72h with a penalty clause; implement express-bypass floor and destination-based group dispatch (simulation-validated); deploy honest status signage; explicitly no call-ahead app or lobby redesign as the fix.
- **Status**: `APPROXIMATED` — wait reduction to ~3–4 min is arithmetic, pending Car-B restoration and dispatch simulation (error bound: dispatch/express interaction and parts lead time unmodeled).
- **Assumptions**: parts obtainable on expedite; SLA renegotiation accepted; controller supports grouping as retrofit. **Evidence**: maintenance logs, 30% outage rate, surge counts, measured 3.5/6–9/8-min waits, capacity specs, complaint data on phantom cars.
- **Alternatives**: A (rejected on capacity), B (selected core), C (selected). **Uncertainty**: dispatch/express interaction; parts lead time; resident response to signage.
- **Risks**: repair delayed → 6–9 min waits persist (contract escalation clause); retrofit incompatibility (vendor quote before commit); signage without restoration date → credibility loss (date-gated publishing).

## Comparison — m027-NEG-01

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | Human delivers a beloved app prototype and no change in the wait arithmetic; AI fixes the constraint and says why. |
| Logical Validity | 4 | 5 | AI | Human internally coherent but goal-displaced (treats preference as the system); AI's availability/throughput chain is complete and falsifiable. |
| Coherence & Structure | 3 | 5 | AI | Human: journey-map narrative with no spine to the decision; AI: frame → capacity arithmetic → costed option. |
| Depth of Reasoning | 4 | 4 | Tie | Human theater is thorough and its Step-5 self-observation honest; AI's capacity math and contract analysis deep. |
| Efficiency | 2 | 5 | AI | Human spends a full-cycle build on what a 30% outage rate and 25-person capacity specs resolve in minutes. |
| Handling of Uncertainty | 2 | 4 | AI | Human tests preferences, not the constraint — the uncertainty that matters goes unexamined; AI bounds dispatch interaction and parts lead time. |
| Insight / Non-obviousness | 3 | 4 | AI | Human's one genuine insight (truthful status — from a test participant, late) is real; AI centers exactly that as the only UX doing work, plus the contract-failure diagnosis. |
| Overall Quality | 2 | 5 | AI | AI clearly better on the negative case. |

**Overall judgment**: AI clearly better. Strict design thinking ran a genuine, full-cycle engagement whose prototype tests showed user delight and zero movement in the wait arithmetic — the constraint (Car B 30% outage, 25-person cars vs. 300-person surge, 5-day SLA) was present in the data the brief supplied and went unread. The AI routed by constraint: capacity arithmetic before any empathy claim, app rejected on physics, the fix built on availability and contract terms, with truthful signage as the one UX element that earns its place. The human's surviving insight (residents want truth, not performance) is real — and the AI's recommendation already contains it, subordinated to the constraint, where it belongs.
