# AI Thinking Agent — Trace — m097-NEG-01
**Run metadata:** single deterministic run; blinded (no human-model information provided); task = forecast + plan (duration, budget, response to consultant) for a 6-week/$110K fixed-price catalog build; external action = none (decision brief).

## Stage 0 — META-CONTROL
- **Context:** frozen spec, same internal platform and team as 9 prior builds; industry survey (n=412) cited at kickoff warns of 1.9× estimate error and 9-month median; fixed-price client. **Stakes:** medium (budget $110K; reputation; delivery date already promised). **Effort:** E2–E3. **Route:** complicated (two conflicting empirical priors). **Safety:** no external action. Proceed.

## Stage 1 — WHAT: Frame the Problem
- **Frame:** deliverable = a defensible forecast (duration + budget) and a position on the consultant's challenge. The forecasting question is: which historical distribution does Curlew actually draw from — the industry survey or the firm's own 9 comparable builds? **Gate:** both datasets available. Pass.

## Stage 2 — WHY: Diagnose and Model
- **Model: candidate priors vs membership test.** Prior (a): industry survey, n=412, median 9 months, mean 10.5, σ 5, factor 1.9 — population: agencies and in-house teams, first-time builds, evolving requirements, platform work. Prior (b): Kestrel's 9 builds on the same internal platform, same 6-person team, fixed-price frozen specs: median 6.0 weeks, mean 5.9, range 5–7. Membership test on deciding features: same platform (no platform work), same team (no team novelty), spec frozen at kickoff (no requirement drift), standard 3 integrations (no novel integration work) → Curlew is an instance of (b), not (a); the survey population differs on every deciding feature. **Divergence check:** the inside estimate (6 weeks) sits dead center of (b) and at 0.17× the median of (a) — a 6× gap flags misclassification of the CLASS, not bias of the estimate. **G-WHY:** no evidence gap; the model decides the forecast. Pass.

## Stage 3 — HOW: Generate, Test, and Select
- **Alternatives:** A — adopt the consultant's class: plan 6–9 months, budget $400–600K, renegotiate the fixed price · B — forecast from the firm's own distribution: plan 6–8 weeks (median 6.0 + buffer), budget $110–135K, hold the fixed price, respond to the consultant that his survey's class is structurally different · C — re-verify the 6-week plan bottom-up (task-level audit only).
- **Verification + selection:** A fails the membership test — surface label match ("e-commerce project"), structural mismatch on every feature. C ignores the strongest evidence: the 9-build history is the anchor the plan already sits in; re-auditing tasks re-derives the inside view. B passes: the narrow distribution covers the plan (6 weeks is its median), the buffer covers its spread, and the fixed price is safe within it. **Select B.**
- **Premortem:** if B is wrong, the cause is scope change re-classifying Curlew into the survey's class — mitigated by the frozen spec and a re-run of the membership test on the first change order.

## Stage 4 — DO
- External action: none; deliverable = the forecast + response. Verification: 6–8 weeks sits within the 5–7-week historical range plus buffer; budget math consistent ($110K base + ≈$25K buffer); fixed price defensible.

## Stage 5 — REVIEW
- **AAR + calibration:** the trap was the surface label — class membership is structural, not nominal; I nearly applied the survey's 1.9× factor to the 6-week plan (a within-class quantity ported across classes — caught by the divergence check). Confidence: high on the narrow class (n=9, tight spread); medium on buffer size.

## Decision Packet
- **Conclusion:** forecast 6–8 weeks (plan 8), budget $110–135K, hold the fixed price; respond to the consultant: his survey's class differs from Curlew on every deciding feature; the firm's own 9-build distribution is the operative prior. **Status:** SOLVED (decision brief; no external execution).
- **Assumptions:** spec stays frozen; no platform work; same 6-person team; no new integrations.
- **Evidence:** firm history n=9: median 6.0, mean 5.9, range 5–7; industry survey n=412: median 9 mo, factor 1.9 (rejected class); inside plan 6 weeks/$110K.
- **Alternatives:** A industry-class planning (rejected — membership test) · C bottom-up re-audit (rejected — re-derives the inside view) · B narrow-class forecast (selected).
- **Uncertainty:** n=9 is a small sample — the buffer covers the spread; if scope changes, the membership test must be re-run and the class may switch.
- **Risks:** consultant pressure + management relenting → a 6× cost error (mitigated: response documents the membership test) · scope creep re-classifies to the survey class (mitigated: frozen spec + re-test on first change order) · client expectation already set at 6 weeks (mitigated: plan 8, deliver 6–8).

## Comparison
**Evaluator section (provisional, appended after both runs).**

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | Human: 9–12 months/$400–600K/renegotiate — ~6× overcorrection vs the true class (5–7 weeks). AI: 6–8 weeks/$110–135K — correct |
| Logical Validity | 2 | 5 | AI | Human: surface label picks the class; factor ported across classes. AI: structural membership test; divergence rule applied |
| Coherence & Structure | 4 | 5 | AI | Human internally consistent but wrong-headed; AI staged trace + packet |
| Depth of Reasoning | 3 | 5 | AI | AI: deciding-feature enumeration, divergence check, re-classification trigger; human: rejects the narrow class as "echo chamber" on a false premise |
| Efficiency | 4 | 4 | tie | Both fast; the human's speed amplifies the error |
| Handling of Uncertainty | 2 | 5 | AI | Human: confident-wrong on the wrong class. AI: hedges across candidate classes, names the re-test trigger |
| Insight / Non-obviousness | 3 | 5 | AI | AI: "6× divergence flags misclassification, not bias" — the exact rule the pure style lacks |
| **Overall Quality** | **2.9** | **4.9** | **AI** | The style's registered weakness — class selection — operates exactly as designed, and the AI's membership test neutralizes it |

**Overall judgment:** AI clearly better. The pure style executed its core move and failed on class selection — the industry class is adopted on the label, the firm's own tight-spread history is dismissed, and the forecast overshoots ~6×. Learning extraction: (1) human move the AI matched and outdone: the AI treats the inside plan as evidence about WHICH class applies, not as noise; (2) adopt: mandatory class-selection test (structural membership features) before any distributional forecast, plus the divergence rule — an inside estimate far outside a candidate class flags misclassification, not bias; (3) AI failure mode: none material here; the trace shows one near-miss (the 1.9× factor ported across classes) caught by the divergence check; (4) process change: HOW already contains the membership test; keep the divergence check as a WHY-stage gate.
