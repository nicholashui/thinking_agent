# AI Thinking Agent Run — m029-NEG-01
**Agent process**: META-CONTROL → WHAT → WHY → HOW → DO → REVIEW (with VERIFY layer). Blinded run: no thinking-model name or style information provided.
## META — Context, stakes, effort
- Ops fix with a hard deadline (3 weeks to peak season) and a hard budget ($3,000): nightly false high-temp alarms on 40 cold-chain TMUs. Moderate stakes (vaccine integrity, SLA escalations, staff overtime). Complicated with narrow unknowns — a single failure mechanism. Balanced-analytical, advisory, no external execution. Owner available (warehouse manager).
## WHAT — Frame
- "Identify the cause of the nightly false alarms and fix it within budget before peak season." Key question: "What differs between alarming and non-alarming units, in time and space?" Metrics: root cause evidenced; fix within $3,000 and 3 weeks; certification constraint respected; verification plan with a numeric target. Gate check: pass.
## WHY — Hypotheses, evidence, falsification
- H1 condensation/PCB issue — falsified: hygrometer stable 45–60% RH, no condensation found on inspection, no seasonal pattern.
- H2 sensor/electronics fault — falsified: the 9 units with remote probes ducted to return air NEVER alarm despite identical enclosure hardware; the sensor hardware itself is fine.
- H3 door-draft transient on a fixed-threshold sensor with no hysteresis/delay — supported: alarms cluster 19:00–21:30 (restock); only units within 2m of the door/air curtain alarm; no correlation with compressor cycles; threshold fixed at 8.5°C, no delay. Falsification: H3 dies if a door-zone unit with a ducted probe alarms, or if alarms occur outside restock — neither reported. G-WHY: pass — H3 decision-relevant and evidenced, red herrings falsified, residual uncertainty recorded (causal claim is correlational until the fix is proven).
## HOW — Generate, test, select
- A — Replace all 40 TMUs: $80,000 — fails budget outright.
- B — Wireless cloud monitoring: $12,000 + 6-week install — fails budget AND timeline; heavy re-validation.
- C — Remote probe into return air ($3 × 40 = $120; documented accessory port; single-site validation) + firmware: 0.5°C hysteresis + 10-min confirmation delay (in-house, 1 week; threshold logic not in sensing path → no full re-certification) + reposition door-zone units ≥2m from the air curtain (labor). ≈ $500 total.
- Verify: C acts directly on the diagnosed mechanism (a draft transient read by a door-facing sensor with an instant-trip threshold). Every alternative screened against mechanism + budget + timeline: A and B fail constraints; non-causal options (door-curtain upgrade $4k, ML $18k/8wk, calibration $60×40) fail budget, timeline, or mechanism. C's success is falsifiable: ≤2% alarm-nights over 14 nights post-rollout, else re-open. Selection (record): C — the only alternative acting on the root cause within budget and deadline, with a numeric verification target.
## DO
- Attestation: advisory recommendation, class A2; no live execution (change executed by warehouse ops).
## REVIEW — After-action review
- What went well: falsification killed the red herrings before ideation; every HOW alternative screened against mechanism + budget + timeline.
- To record: (1) A pure ideation pass over TMU elements would have produced 15–20 recombinations (alarm-channel upgrades, desiccant, dual-sensor averaging, ML), most not on the causal path; the WHY diagnosis is what made C the obvious selection rather than one option among twenty — log this ordering as deliberate, not luck. (2) The 14-night verification window must start after firmware rollout completes. (3) Repositioning door-zone units changes the draft pattern — watch for NEW cold-spot alarms. Folded back as risks.
## Decision Packet
- **Conclusion**: Implement C: remote probes into return air on all 40 units ($120), firmware hysteresis 0.5°C + 10-min confirmation delay (in-house), reposition door-zone units ≥2m from the air curtain; target ≤2% alarm-nights over 14 nights post-rollout; escalate to B only if the target is missed.
- **Status**: `APPROXIMATED` — root cause evidenced by correlation and red-herring falsification; causal claim unproven until the 14-night trial (error bound: ≤2% target, else re-open).
- **Assumptions**: restock pattern stable; firmware path clears a threshold-logic change without full re-validation; probe relocation uses the documented accessory port. **Evidence**: alarm clustering (19:00–21:30, door zone), 9/9 ducted-probe units silent, no compressor correlation, stable humidity, budget/timeline data.
- **Alternatives**: A (rejected: $80k), B (rejected: $12k + 6 wk), C (selected). **Uncertainty**: causal vs merely correlational (trial resolves); labor availability for repositioning; post-rollout draft change.
- **Risks**: target missed → pre-specified escalation; repositioning introduces new cold-spot alarms (monitor first 14 nights); firmware regression (staged rollout with rollback point).
## Comparison — m029-NEG-01

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 3 | 5 | AI | Human never decides; AI delivers a costed fix with a verification target. |
| Logical Validity | 3 | 5 | AI | Human's recombination chain is valid but never touches the data; AI's falsification sequence (condensation, electronics, compressor) is explicit. |
| Coherence & Structure | 3 | 5 | AI | Human: 18 equal-weight recombinations, no spine; AI: diagnosis → causal-path ideation → constraint screen → verified selection. |
| Depth of Reasoning | 4 | 4 | Tie | Human's volume is thorough and its buried R3 is the right fix; AI's depth is narrower but decision-relevant, and its AAR catches the repositioning cold-spot risk. |
| Efficiency | 2 | 5 | AI | Human spends an 18-item pass mostly off the causal path and picks a $12k bundle; AI screens 3 candidates against mechanism + budget + timeline. |
| Handling of Uncertainty | 2 | 5 | AI | Human: no ranking, no budget check, no verification plan; AI: numeric target, escalation rule, staged rollout. |
| Insight / Non-obviousness | 3 | 4 | AI | Human's one genuine insight (remote probe + hysteresis, R3) is buried at position 3 of 18 and unweighted; AI builds the decision around exactly it. |
| Overall Quality | 3 | 5 | AI | AI clearly better on the negative case. |

**Overall judgment**: AI clearly better. Strict combinatorial style turned a diagnosable single-mechanism fault into 18 recombinations, most not on the causal path (alarm-channel upgrades, desiccant, calibration, ML); the true fix (remote probe + hysteresis + confirmation delay, ≈ $500) is present but unweighted, and selection-by-novelty picks a $12k cloud bundle that blows the budget and timeline. The AI's WHY diagnosis (red-herring falsification + door-zone clustering) routed ideation to the causal path, and the budget/timeline screen killed the expensive options. The human's buried R3 is exactly the AI's selected fix; the difference is structural — the human generated without filtering, the AI filtered before and after generating.
