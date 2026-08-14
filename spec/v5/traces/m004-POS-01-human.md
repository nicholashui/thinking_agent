# Human Baseline Trace — Occam's Razor + Complexity Awareness
## Test Case: m004-POS-01

Rule: buy all observations with the fewest unobserved entities; charge full price for every complexity the evidence demands.

**Inventory — six observations**: flicker tracks the compressor (11/12 within 3 s; none with the fridge unplugged; resumes at replug); panel voltage sags 119→109 V at compressor start; knocking falls inside the HVAC runtime log (9/10, 1 on the water heater); panel buzzes at 60 Hz and stops at the main breaker; kitchen outlet reads 118 V idle / 114 V at 1.5 kW, faceplate 31 °C.

**Simple hypothesis — a loose neutral in the panel.** One fault condition buys the set: a high-resistance neutral sags voltage under load — 10 V at a compressor start is exactly that signature, and the compressor is simply the load that pulls hardest, so the correlation is *required by the mechanism*, not mysterious. The bad joint arcs faintly at 60 Hz — the hum, localized by the main-breaker test; the dog just hears it at its loudest point. Knocking is duct thermal expansion while the furnace runs (9/10, and the 10th is another burner). The hot outlet is a 30-year-old kitchen splice — a resistive joint; 31 °C at 1.5 kW is consistent.
Entities required: one loose lug, one hot duct system, one old splice — touchable, testable, repairable. Zero unobserved agents.

**Price the complex hypothesis.** The haunting must add: an agent with existence, location, and motive; a mechanism to modulate house voltage in sync with the compressor; a reason to knock only when the furnace runs; a way to heat one specific outlet; an emitter the dog senses at the panel. ≥5 unobserved entities, none verifiable, none falsifiable — it buys the same six observations at a strictly higher price. It loses without further inspection.

**Decisive probe, cheap and first.** Log voltage during a compressor start (done — 10 V sag), open the main breaker, inspect the neutral lug; tighten; observe. Falsifiers stated in advance: flicker with no load kills H1; no sag kills the whole story; knocking with the HVAC off kills the duct story. Every part of my story is designed to be killable — that is what makes it the right story.

**Uncertainty, separated.** Instrument-verified: the sag, the correlations, the hum localization. Inferred: the hum's source — the breaker test confirms it. Genuinely unverified: that the splice alone explains 31 °C — I check it when the panel is open.

**Conclusion.** One loose neutral explains the flicker and the hum; ducts explain the knocking; one old splice explains the heat. The demonstration is the argument: tighten the lug, show the lights steady. The house is not haunted — it is under-maintained. Complexity was charged at every step, and nothing was owed to the dark.

---
## Comparison

| Dimension | Human Score | AI Score | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | Both identify the loose neutral; both resolve with the lug fix. |
| Logical Validity | 5 | 5 | Tie | Both mechanisms are sound and checkable. |
| Coherence & Structure | 5 | 4 | Human | Human is a single parsimony chain; AI carries a dead paranormal branch. |
| Depth of Reasoning | 5 | 4 | Human | Human prices the complexity (≥5 unverified entities) and gives a falsifier per mechanism; AI enumerates but does not price. |
| Efficiency | 5 | 4 | Human | Human orders the 10-minute probe first and never analyzes a dead hypothesis. |
| Handling of Uncertainty | 5 | 4 | Human | Human separates verified/inferred and flags the one open item; AI's packet is thinner. |
| Insight / Non-obviousness | 4 | 4 | Tie | Both catch the dog-buzz move and the demonstration-not-argument close. |
| Overall Quality | 4.8 | 4.3 | Human | Roughly equal on correctness; human ahead on parsimony discipline. |

**Overall judgment**: Human ahead (roughly equal on the answer, human better on method).

**Why**: Both solved the case; the difference is the price ledger. The human's trace makes the comparison explicit — six observations bought with three touchable entities, or with ≥5 unverified ones — and converts parsimony into a checkable account (falsifier per mechanism, probe first). The AI reached the same fix but carried a hypothesis the evidence had already priced out of the market.
