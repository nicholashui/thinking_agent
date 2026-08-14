# AI Thinking Agent — Trace — m093-POS-01
**Run metadata:** single deterministic run; blinded (no human-model information provided); task = produce a plain-language explanation of how a refrigerator works that survives the VP's questions, and account for Priya's stall; external action = none (explanation deliverable).

## Stage 0 — META-CONTROL
- **Context:** VP briefing; shallow account on the table ("the fridge makes cold"); Priya stalled on "where does the cold come from?". **Stakes:** medium (a go/no-go VP decision rests on the explanation's correctness). **Effort:** E2. **Route:** simple concept, deceptive vocabulary (thermodynamics hiding under "makes cold"). **Safety:** no external action. Proceed.

## Stage 1 — WHAT: Frame the Problem
- **Frame:** the deliverable is an explanation that is (a) plain-language and (b) mechanically correct. The hinge is the heat-transfer mechanism, and Priya's stall is the symptom of a gap between vocabulary and mechanism. Success metric: the child's three questions — where does the cold come from? why is the back warm? why doesn't it leak back? — answered without error. **Gate:** physics is settled; no missing facts block the deliverable. Pass.

## Stage 2 — WHY: Diagnose and Model
- **Model: heat-mover vs cold-maker.** The shallow account treats cold as a substance the fridge adds. The correct model: the fridge moves heat out — cold is the absence of heat. The child's "where does the cold come from?" is a precise instrument: it cuts the shallow story exactly at the word "makes." **G-WHY:** the breakdown point is identified; the repair is standard physics. Pass.

## Stage 3 — HOW: Generate, Test, and Select
- **Alternatives:** A — "it makes cold, the thermostat keeps it cold" · B — "it sucks the cold out" · C — heat-pump loop: refrigerant boils inside at low pressure, absorbing heat (evaporation); the compressor squeezes the gas hot (its work); back coils condense it, releasing heat to the room (that is why the back is warm); insulation slows the leak back in; the thermostat gates the pump.
- **Verification + selection:** A fails on all three child questions (it is the gap itself). B fails: it misleads on direction and physics — nothing sucks; it also leaves "why is the back warm?" unexplained. C answers all three: cold source (heat removed), warm back (condensation releases), leakage (insulation slows it, pump re-fights it). **Select C.** Premortem: if C is wrong, it is because the phase-change claim is over-reached — checked: boiling absorbs, compression heats, condensation releases; direction inside→out; no cold-as-substance anywhere.

## Stage 4 — DO
- External action: none; deliverable = the explanation. Verification: final version below is plain-worded and complete against the three questions.

## Stage 5 — REVIEW
- **AAR + calibration:** the trap was jargon-fluency without mechanism — "coolant, compressor, condenser" as words, not a loop. Gap: I started from the jargon set instead of from the child's question. Confidence: high on the mechanism; "simple enough" is defined by the child's questions.

## Decision Packet
- **Conclusion:** deliver to the VP: "Your fridge doesn't make cold — it moves heat. A refrigerant runs in a loop: inside the fridge it boils, and boiling pulls heat out of the food; the compressor squeezes the gas hot; the coils on the back let that heat escape into the room — that's why the back feels warm. The insulation just slows the heat creeping back in, and the thermostat decides when the pump runs." Priya's stall = vocabulary-to-mechanism gap. **Status:** SOLVED (explanation deliverable; no external execution).
- **Assumptions:** standard phase-change refrigeration physics; the VP's questions mirror the child's; the solar-assist feature does not alter the heat-pump core.
- **Evidence:** Priya's stall at "where does the cold come from?"; the warm back (phenomenon requiring explanation); physics (evaporation absorbs heat, compression raises temperature, condensation releases it).
- **Alternatives:** A makes-cold (rejected — it is the gap) · B sucks-cold-out (rejected — wrong direction and physics) · C heat-pump loop (selected).
- **Uncertainty:** none material for the explanation; medium confidence that "solar-assist" specifics are irrelevant to the mechanism (flagged, not asserted).
- **Risks:** the explanation slides back into jargon under pressure (mitigated: the three child questions are the acceptance test) · the sales team reverts to "it makes cold" in the field (mitigated: the one-line "moves heat, doesn't make cold" is in the packet).

## Comparison
**Evaluator section (provisional, appended after both runs).**

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | tie | Identical correct explanation; both survive the child's three questions |
| Logical Validity | 5 | 5 | tie | Same physics; neither side commits a cold-as-substance error |
| Coherence & Structure | 4 | 5 | AI | Human: linear first-pass; AI: staged trace + packet |
| Depth of Reasoning | 5 | 4 | Human | Human owns the breakdown first-pass — "cold isn't a thing to add, it's a leak to fight"; AI reaches it via rejected-alternative machinery |
| Efficiency | 5 | 3 | Human | Human hits the real wall on first reading; AI generates a full alternative set first |
| Handling of Uncertainty | 3 | 4 | AI | AI packet bounds "simple enough" and flags the solar-assist caveat |
| Insight / Non-obviousness | 5 | 4 | Human | The child's "where does the cold come from?" as diagnostic scalpel is the human's first move; AI states it later, more carefully |
| **Overall Quality** | **4.6** | **4.3** | **Human** | Same explanation; the pure style IS the method here and lands first-pass |

**Overall judgment:** Human clearly better (narrow). Learning extraction: (1) human move the AI missed first-pass: the child's question used as the diagnostic instrument on the naive sentence itself; (2) adopt: treat the user's own naive explanation as the breakdown target — WHAT should parse the on-table sentence that cannot survive a "why?"; (3) AI failure mode: alternatives-generation before the break in the given story is identified; (4) process change: WHAT gains a "would this sentence survive a 12-year-old?" check on the user's own explanation.
