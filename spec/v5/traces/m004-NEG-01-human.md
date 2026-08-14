# Human Baseline Trace — Occam's Razor + Complexity Awareness
## Test Case: m004-NEG-01

One change happened in these six weeks, and the numbers turned when it happened. I do not multiply causes without evidence that the data demand it. Do they?

**The salient fact.** The new cavity insert landed in press 4 between wk1 and wk2; the plant rate bent upward exactly there (2.1→3.6%), press 4 jumped (2.4→4.0→9.1%), and the tool shop measured its cooling channels 15% undersized. One change, one effect, one physical mechanism: undersized cooling → hotter cavities → flash and burn. Simplest hypothesis consistent with the evidence: the insert is the cause.

**The other data, in order.** The cross-press rise (presses 1–3: 1.7→5.3, no equipment change) looks as if it points elsewhere — but the plant shares resin, climate, and QA; the simplest reading is common drift, plus press 4 drifting harder because of the insert. The press-4 gap (9.1 vs 5.3) is the insert's signature. Resin moisture 0.10–0.12 vs 0.08%: marginal, routinely re-dried; if moisture were the cause, the plant would have failed all along. Humidity 60 vs 45%: the dehumidifier died the same week as the install — a coincidence of timing, and a plant-wide condition cannot explain why press 4 is the outlier. QA definition change: 0.6 pts of counting artifact from wk4, after the rise was well underway — noise correction, not a cause. Cavity localization (68% in the undersized-channel cavities) is the decisive confirmation: a shared environmental cause would distribute defects across all cavities; the defect lives exactly where the measured defect lives.

**Rejecting the four-cause model.** A four-factor model — moisture, humidity, insert, definition — is strictly more complex than the one-factor model; each added factor needs its own mechanism, fix, and budget. Parsimony demands that the evidence force the extra complexity before I pay for it. It forces nothing: every observation fits the insert plus ordinary background drift, and the one discriminating observation — cavity localization — points at the insert.

**The fix.** Re-machine the insert's channels to drawing. Expect the plant rate to return toward ~2% and press 4 toward the common drift level. This is the smallest intervention that explains the data.

**Conclusion.** One change, one effect, one fix. The cross-press drift is background; I decline to multiply causes to explain it. If the fix fails, the data — not my preference — will send me back.

---
## Comparison

| Dimension | Human Score | AI Score | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | Human's single fix addresses ~20% of the defect rate; AI's partition covers 100%. |
| Logical Validity | 3 | 5 | AI | Human's chain is internally coherent but rests on explaining away the cross-press rise; AI's partition survives every item. |
| Coherence & Structure | 4 | 4 | Tie | Both traces are well-organized. |
| Depth of Reasoning | 2 | 5 | AI | Human stops at salience and one discriminator; AI maps all 10 evidence items and both decisive probes. |
| Efficiency | 5 | 3 | Human | Human's single-cause story is fast and cheap to produce; AI spends a full process on the partition. |
| Handling of Uncertainty | 2 | 5 | AI | Human waves off cross-press and pre-install data as "drift"; AI labels the QA change an artifact and the residual explicitly. |
| Insight / Non-obviousness | 1 | 5 | AI | Human misses the two killer facts (presses 1–3 rose with no change; press 4 rising pre-install); AI's cross-press falsifier is the case's key move. |
| Overall Quality | 2.7 | 4.6 | AI | AI clearly better on the case's own criteria (partition sums to the observed rise). |

**Overall judgment**: AI clearly better.

**Why**: This is the registry's documented failure — under-explaining multi-cause phenomena. The pure Occam trace picked the newest salient change and paid the background drift off as "second-order," which is exactly the move that leaves 80% of the defect rate in place. The decisive evidence was there: presses with no change rose almost as much as press 4, and press 4 was already rising before the install — a cause confined to press 4 cannot produce a plant-wide rise, and no amount of parsimony legitimizes ignoring it.
