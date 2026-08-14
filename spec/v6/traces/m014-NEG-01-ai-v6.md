# v6 Routed AI Trace — m014-NEG-01 (blinded)
## Insurer claims pipeline — "adjudication is the bottleneck, hire 5" plan under review; reply this week
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,product,software | g:decide,diagnose,estimate,guarantee,maximize,predict | c:— (none)
- Router top3: m018, m019, m044; confidence gap <= 0.5 → AMBIGUOUS → DUAL-ROUTE: m018 + m019 first-class passes, synthesized (m044 = synthesis context). Note: serial-capacity-framing styles held out of top-3 (learned NEG lesson). Gate (R3/R4): m003 inversion (guarantee goal). Flags: no deadline/adversarial/one_shot/high_stakes/unmeasured context → no further R3 modules; verification loop remains → full governed loop, no fast path.
### WHAT — frame + structure-first scan (S1)
- Structure first: the org chart is NOT the flow diagram. Enumerate every processing resource — including the idle engine — and the routing policy that forces all claims through one station. "Which stage binds?" is only meaningful if the flow structure is fixed; here it is policy-chosen.
- Frame: evaluate the ops diagnosis + plan; decide this week.
### WHY — P1 input-provenance audit
- Interested-party check: the ops team's "constraint = human adjudication" diagnosis feeds their own hire plan (headcount/budget benefit) — treat it as a claim to verify, not a measurement. The engine's 250/day pilot capacity and accuracy are the only verified measurements; its mothballing was organizational, not technical.
### HOW — style passes (dual-route, synthesize)
- Pass S1 (m018 steelman — strongest version): the hire plan is not stupid — adjudication genuinely runs at 105% today; the pilot is 2 years old (drift risk on new products); the 75% high-touch roadmap shifts real load onto human judgment. Under the strongest version it still fails: re-routing clears the backlog TODAY at zero capex, and at month 6 high-touch ≈ 0.75 × 470 ≈ 353 < 400 — the hires land after the constraint has dissolved.
- Pass S2 (m019 red team — contract): enumerated vectors, quantified exposure: (1) org-chart presupposition — exposure $1.2M/yr for zero throughput gain at the 6-month horizon; (2) interested-party diagnosis — exposure: backlog 20/day → ~2,400–3,600 claims + daily SLA penalties through the 6-month ramp; (3) orphaned engine (owned by nobody) — exposure: the cheap fix stalls without an owner; (4) static-horizon blindness — exposure: mix shift dissolves the constraint before hires land. Baseline-risk comparison: do-nothing (backlog + penalties) vs hire (cost + 6-month delay + zero gain at horizon) vs re-route (zero capex, reversible, 5-day verification).
- Synthesis (m044 stakeholders): hidden requirement — the engine's ownership vacuum is the real organizational constraint; assign an owner this week or the fix stalls. Stakeholders: ops team (rejected plan — give them the trigger rule as a path), claims staff (low-touch load shifts to engine), roadmap team (mix forecast authority), client (SLA optics during engine ramp).
- Divergence (V1–V3): m018 and m019 AGREE (re-route now, cancel hiring, trigger at high-touch > 400/day); general route agrees — none.
### GATES — m003 inversion (R4)
- ≥6 failure categories ranked L×I for the re-route plan: (1) engine accuracy on new products — high, 5-day pilot + keep high-touch human; (2) ownership vacuum stalls enablement — high, owner assigned this week; (3) mix forecast wrong (high-touch faster than 75%) — medium, trigger absorbs; (4) SLA optics during engine ramp — medium, 25% sample fallback; (5) low-touch classifier error (engine gets high-touch) — medium, explicit rule; (6) trigger miscalibration (share > ~85%) — low, revisit month 6. Residual: genuinely novel complex products on the engine — un-mitigable beyond pilot + trigger; keep human on anything the pilot didn't cover. Never/always: never treat the org chart as the flow diagram; always ask which policy creates the apparent constraint.
### DO — full loop (verification embedded; commit this week)
- Commit: enable the engine on low-touch claims this week; assign an owner; measure backlog/SLA daily for 5 days; if not clearing, fall back to a 25% sample ramp and re-diagnose; cancel the hire plan; standing trigger — begin hiring only when high-touch volume > 400/day (share > ~85%).
### REVIEW — insight pass (S2, packet gate)
- I1: the constraint was never a stage — it was a routing policy plus an ownership vacuum; the org chart hid a 250/day parallel path that made the apparent bottleneck an artifact.
- I2: the hire plan is worse than zero-return: its 6-month ramp guarantees the backlog and SLA penalties continue through the entire window where the cheap fix clears it in days.
### DECISION PACKET
- Conclusion: reject the hire plan; re-route low-touch → engine (210 < 250), high-touch stays human (210 < 400); every stage gains slack; backlog clears at zero capex; hire only at the trigger (high-touch > 400/day, share > ~85%).
- Status: SOLVED (decision issued; empirical verification embedded in plan).
- Assumptions: engine pilot accuracy holds on current low-touch; demand +2%/mo; mix 50 → 75% over 6 months; capacities as stated.
- Evidence: two-horizon flow arithmetic (today 210/210 split; month 6: 353/118); pilot record; utilization table under both routing policies.
- Alternatives: re-route now + trigger (selected) · hire 5 now (rejected — zero gain at month 6) · do-nothing (rejected — backlog/SLA) · 25% sample ramp (fallback).
- Uncertainty: engine accuracy on new products; mix/demand forecasts; ownership commitment.
- Risks: engine underperformance → backlog returns (fallback ready); unowned engine stalls the fix (owner assigned); ops-team politics on the rejected plan (trigger gives them a path).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | human's hire plan fails the contract; AI clears backlog at zero capex |
| Logical Validity | 2 | 5 | AI | human's chain inference is valid but its fixed-flow premise is false; AI's two-horizon arithmetic is airtight |
| Coherence & Structure | 3 | 5 | AI | elegant TOC narrative anchored to the wrong structure |
| Depth of Reasoning | 3 | 5 | AI | human misses policy-artifact + mix-shift; AI prices both horizons + trigger + ownership |
| Efficiency | 3 | 5 | AI | human commits $1.2M/yr; AI zero-capex fix this week |
| Handling of Uncertainty | 2 | 5 | AI | human asserts static mix; AI 5-day verification + fallback + trigger |
| Insight / Non-obviousness | 2 | 5 | AI | human dismisses the engine as side channel; AI: hidden parallel structure + ownership vacuum |
| Overall Quality | 2.5 | 5.0 | AI | clear — pure-bottleneck trap; routed steelman/redteam/gates avoid it entirely |

Winner: AI (clear). Why: the router's learned NEG lesson held the serial-bottleneck framing out of top-3, and the m018/m019/m044 dual-route formalized the structure-first check — steelmanning forced pricing the strongest hire-plan version, red team quantified every exposure and flagged the interested-party provenance plus the orphaned engine, m044 surfaced the ownership vacuum, and the m003 gate enumerated the re-route plan's own failure categories — moves the non-routed v5 AI reached ad hoc now arrive as contract outputs.
