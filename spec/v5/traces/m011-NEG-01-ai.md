# AI Thinking Agent — Trace — m011-NEG-01
**Run metadata:** single deterministic run; blinded (no human-model information provided to the agent); task = operational diagnosis + intervention plan; external action = none (recommendation memo).

## Stage 0 — META-CONTROL
- **Context:** SwiftCourier complaints 120 → 240/day over 8 weeks; leadership favors speed targets + courier expansion; measurements available: GPS median 28 min (unchanged), tags 80% "delivery time/ETA", 2% dispute-verified, live-tracking app update shipped week 5, headcount/mix unchanged.
- **Stakes:** reputation, courier safety, churn risk. **Effort:** E3 (causal hypothesis testing).
- **Route:** causal-diagnosis class (Cynefin: complicated — hypothesis + falsification against measurements). **Safety:** memo only; no irreversible action. Proceed.

## Stage 1 — WHAT: Frame the Problem
- **Frame:** explain the complaint rise and recommend an intervention; the measurement set is fixed (no new data collection budget beyond the stated instruments).
- **Scope:** treat the GPS audit, tags, verification share, and rollout timeline as the evidence base. **Gate:** enough evidence to discriminate hypotheses. Exit gate passed.

## Stage 2 — WHY: Diagnose and Model
- **Hypotheses:** H1 service degradation (actual delivery time up) → complaints. H2 expectation/funnel shift: live tracking makes ETAs visible; wrong displays (12 min shown, 28 actual) generate "delivery time" complaints without any change in delivered time. H3 seasonality/order-mix change.
- **Evidence & falsification:** H1 — GPS audit refutes its causal edge: actual median unchanged (28 vs 27.5). H2 — spike begins exactly at the week-5 rollout; 80% "delivery time/ETA" tags despite unchanged actual times is consistent with an ETA-display mismatch; 2% dispute-verified share → the series is mostly unverified claims. H3 — no mix change recorded. **Gate (G-WHY):** H1 falsified by measurement; H2 leads with timing + tag evidence; falsification of H2 planned (A/B the display). Gate passed.

## Stage 3 — HOW: Generate, Test, and Select
- **Alternatives:**
  - A. Speed targets (34 → 28 min) + 15% capacity (management-favored). **Rejected:** presumes H1, whose edge the GPS audit already refuted; also feeds a safety → attrition → capacity ↓ → slower-delivery loop (fix that backfires).
  - B. ETA-display fix + measurement program (selected): correct the tracking countdown accuracy; segment complaints by tag; verify a sample through the dispute process; A/B the display; monitor churn.
  - C. Monitor-only (rejected — action window is a month; B is cheap and reversible).
- **Verification:** each alternative's causal edges mapped to a measurement that confirms/refutes it; A's premise contradicted by measurement (a); B's premise testable and reversible. **Selection: B.**
- **Premortem / sensitivity:** if H2 is wrong and service did degrade, B still surfaces it via the dispute-verification sample within 2 weeks — the measurement program is the safe path under either hypothesis.

## Stage 4 — DO
- External action: none. Recommendation memo: (1) do not impose speed targets or expand capacity; (2) fix ETA display accuracy on live tracking; (3) complaint pipeline: tag segmentation + dispute-verification sampling; (4) A/B the tracking display; (5) monitor silent-exit proxies (active-user share, reorder rate).

## Stage 5 — REVIEW
- **AAR:** decisive move = testing the loop edge (complaints ↔ actual delivery time) against the GPS audit before prescribing; the proxy-vs-state distinction (complaint count = proxy whose meaning changed; delivered time = state) resolved the case; residual uncertainty (2% verification share) is exactly why the deliverable is a measurement program.

## Decision Packet
- **Conclusion:** The complaint spike is an expectation/funnel shift from live tracking (visible ETAs mismatch actual arrivals), not service degradation. Reject speed targets/capacity; fix ETA displays; segment + verify complaints; A/B the display; watch churn.
- **Status:** SOLVED (diagnosis supported by measurements; plan issued).
- **Assumptions:** given measurements are accurate; complaint count is a proxy, not the state; no unmeasured service change (partially testable via the verification sample).
- **Evidence:** GPS audit (unchanged); rollout-week timing; 80% tag share; 2% verified share.
- **Alternatives:** A speed+capacity (rejected, falsified premise) · B display-fix + measurement (selected) · C monitor (rejected).
- **Uncertainty:** true complaint causes partially unverified (2%); ETA-display impact magnitude unknown until A/B. **Risks:** if H2 is wrong, B's measurement phase detects it within 2 weeks; imposing A instead risks safety incidents and courier attrition.

## Comparison
**Evaluator section (provisional, appended after both runs).**

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | Human prescribed speed targets + capacity (the wrong, safety-risky fix); AI correctly refused and targeted the confound |
| Logical Validity | 4 | 5 | AI | Human internally consistent but its loop edge was falsifiable by the given audit and wasn't tested; AI tested each edge |
| Coherence & Structure | 4 | 5 | AI | Human diagram elegant but self-justifying; AI packet complete |
| Depth of Reasoning | 4 | 4 | tie | Human: real loops (side-effect safety loop) but built on an unfalsified premise; AI: measurement-first depth |
| Efficiency | 3 | 5 | AI | Human jumps to intervention; AI's measurement plan is the minimal correct action |
| Handling of Uncertainty | 3 | 4 | AI | Human folds contradictory data into the diagram ("lagging instrument"); AI quantifies the verification gap |
| Insight / Non-obviousness | 2 | 5 | AI | AI: complaints are a proxy whose meaning changed; the fix that backfires; human: the diagram is the analysis |
| **Overall Quality** | **3.1** | **4.7** | **AI (clearly)** | Negative case: the pure style's diagram substituted for data; measurement discipline wins |

**Overall judgment:** AI clearly better. The human's loop diagram was elegant and wrong — built from the single aggregate series, it reclassified the contradictory measurements as instrument lag and prescribed the very speed-target policy whose safety→attrition loop it had itself drawn. The AI tested the loop edge against the GPS audit, identified the expectation-shift confound, and made measurement (not intervention) the deliverable.
