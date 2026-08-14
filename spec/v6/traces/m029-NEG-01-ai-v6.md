# v6 Routed AI Trace — m029-NEG-01 (blinded)
## Cold-chain TMU false alarms — 40 rooms, 3-week deadline, $3k hard budget
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,product,software,supply | g:diagnose,guarantee,maximize | c:deadline
- Router top3: m031, m044, m091; confidence gap ≤ 0.5 → NOT CONFIDENT → DUAL-ROUTE: m031 + m044 first-class passes; m091 = router context only (reference class: TMU false-alarm episodes of this class are sensor-path transients, not hardware failures). Gate (R3/R4): m003 inversion (guarantee goal). Flags: deadline → TEMPO mode (cost-of-delay, commit at DO); mechanism judgment required → no P8 fast path.
### WHAT — frame + structure-first scan (S1)
- Frame: "Fix the nightly false alarms within $3k and 3 weeks without breaking certification" — success = mechanism evidenced from the data + fix clearing budget/timeline/certification + numeric verification target.
- Structure-first scan: single-mechanism diagnosis — the alarm dataset IS the experiment; screen every ideation candidate against the diagnosed mechanism, not novelty.
### WHY — P1 provenance audit + m031 diagnosis (contract: hypothesis → discriminating test → update)
- Given-data audit: alarms cluster 19:00–21:30 (restock window); only units within 2m of the loading door alarm; the 9 units with remote probes ducted to return air NEVER alarm; no compressor correlation; RH stable 45–60%, no PCB condensation. This falsifies the red herrings before ideation: condensation/electronics (silent units share identical hardware), compressor cycles (no correlation). INTERESTED PARTY: manager's "fix before peak" = hard deadline; SLA escalations = reputational pressure that favors flashy options — weight evidence over visibility.
- H (m031): door-draft transient read by a door-facing sensor behind the display with a fixed 8.5°C threshold, no hysteresis, no delay. Discriminating test: the supplied data already discriminates — H dies if a door-zone ducted-probe unit alarms (none do) or if alarms occur outside restock (they don't). H survives, unlabeled in the scenario.
### HOW — style passes (dual-route, completion contracts)
- Pass A (m031, contract): hypothesis stated; discriminating test = data pattern (above) + post-fix 14-night alarm-nights read; update rule: ≤2% alarm-nights → confirmed, >2% → re-open diagnosis (repositioning changed the draft pattern). Contract met.
- Pass B (m044, contract — for each stakeholder: want / can do / will do): night staff (false-alarm fatigue → may under-report: use alarm-log audit, not self-report); manager (SLA exposure → rewards a visible fix: weight against evidence); certifier (sensing-path change → re-validation; firmware threshold logic exempt); customers (escalated concerns → need a demonstrable numeric target); vendor ($2k/unit replacement incentive). Constraint screen per option (budget $3k / 3wk / certification): cloud $12k ✗ budget+timeline · ML $18k ✗ budget+timeline · replacement $80k ✗ budget · curtain upgrade $4k ✗ budget+off-mechanism · calibration visits $2.4k ✗ won't catch transients · remote probes into return air $120 + firmware 0.5°C hysteresis + 10-min confirmation delay (in-house, 1 wk, not sensing path → no re-validation) + reposition door-zone units ≥2m (labor) ≈$500 ✓ — the only option acting on H inside all three screens.
- Divergence resolution (V2): m031's mechanism and m044's screens agree on the same fix → proceed; agreement recorded.
### GATES — m003 inversion (R3, mandatory)
- Invert: "How does this fix fail to fix within 3 weeks?" 6 ranked: (1) certifier rejects the firmware change → probe-only fallback still on causal path; (2) repositioning moves the draft to new units → new cold-spot alarms; (3) staff under-report → alarm-log read, not self-report; (4) restock pattern shifts → verification window must span a restock night; (5) probes misinstalled (not into return air) → checklist + single-site validation; (6) budget creep via overtime → labor capped. Un-mitigable residual: a hardware fault co-occurring with the draft transient — detected by alarm-log review, not prevented. Never/always: never ship a fix without a numeric verification target; always screen every option against budget + timeline + certification.
### DO — P3 branch-completeness before commit (tempo mode)
- Failure branches priced: verification misses target → escalate to cloud monitoring ($12k + 6wk vs vaccine-discard risk — cost-of-delay stated); firmware slips past week 1 → deploy probes + reposition first, firmware second (partial fix remains on the causal path).
### REVIEW — insight pass (S2, packet gate)
- I1: the 9 silent ducted-probe units are a free randomized experiment — the data already ran the discriminating test; the fix is a replication, not a guess.
- I2: every flashy option fails on the same constraint row (budget or timeline) — the screens, not novelty, do the selecting.
### DECISION PACKET
- Conclusion: remote probes into return air on all 40 units ($120) + firmware hysteresis 0.5°C + 10-min confirmation delay (in-house, 1 wk) + reposition door-zone units ≥2m from the air curtain; ≈$500; target ≤2% alarm-nights over 14 nights post-rollout, else escalate to cloud monitoring.
- Status: APPROXIMATED — mechanism evidenced (correlational); causal proof at the 14-night trial (error bound: ≤2% target, else re-open).
- Assumptions: restock pattern stable; threshold-logic change exempt from re-validation; probe relocation uses the documented accessory port. Evidence: restock clustering, 9/9 silent ducted units, no compressor correlation, stable RH, price list.
- Alternatives: cloud $12k (rejected: budget+timeline), ML $18k (rejected: budget+timeline+8wk), replacement $80k (rejected: budget), curtain upgrade $4k (rejected: budget, off-mechanism), calibration $2.4k (rejected: no transient coverage), selected fix ≈$500.
- Uncertainty: causal-vs-correlational until the 14-night read; post-rollout draft change; restock stability.
- Risks: repositioning creates new cold-spot alarms (monitor first 14 nights); firmware regression (staged rollout + rollback point); staff under-reporting (audit-log read); target missed → pre-specified escalation.

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 3 | 5 | AI | Human never decides (18 unweighted recombinations, $12k bundle pick); AI delivers a costed fix with a verification target |
| Logical Validity | 3 | 5 | AI | Human's chain never touches the alarm data; AI's falsification sequence (condensation, electronics, compressor) is explicit and discriminating |
| Coherence & Structure | 3 | 5 | AI | Human: equal-weight volume, no spine; AI: diagnosis → causal-path screen → gate → packet |
| Depth of Reasoning | 4 | 4.5 | AI | Human's volume is thorough with the right fix buried at #3; AI adds stakeholder incentives + inversion failure enumeration of the fix itself |
| Efficiency | 2 | 5 | AI | Human spends an 18-item pass mostly off-causal-path; AI screens 6 options against mechanism + budget + timeline in one pass |
| Handling of Uncertainty | 2 | 5 | AI | Human: no ranking, no budget check, no verification plan; AI: numeric target, escalation rule, staged rollout |
| Insight / Non-obviousness | 3 | 4.5 | AI | Human's one insight (probe + hysteresis) is unweighted; AI surfaces the silent-9 as a free experiment and screens-as-selection |
| Overall Quality | 3 | 5 | AI | v5 verdict held: 3.0/5.0 → routed run keeps the AI win and makes the winning structure contract-driven |

Winner: AI (clearly). Why: the router held the recombination style out of the route on this signature (the NEG lesson is installed) and ran m031+m044 first-class — hypothesis with the data as the discriminating experiment, stakeholder screens with recorded rejects — plus the m003 inversion gate enumerating how the fix itself fails; the human baseline's informative failure (volume without weight, novelty selects the $12k cloud bundle) is structurally reproduced and rejected by contract.
