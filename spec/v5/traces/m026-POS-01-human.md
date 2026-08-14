# Human Baseline — m026-POS-01
## Style: Analogical Reasoning / Pattern Transfer (pure) — visible reasoning trace

**Problem restatement.** Frost at -4 °C for 6 hours tonight; 1,000 apricot trees in a basin; damage below -2 °C for more than 2 hours. I have 12 fans (each plume +0.7 °C, rises additive at ≥3 overlapping plumes), 24 crew-hours; central heater +0.3 °C at the orchard; sprinklers break ~40% of twigs at -4 °C; one wind machine +0.4 °C. I must choose tonight's plan. Rule of the style: before solving, ask what known situation has the same *structure* — map it explicitly, then transfer the relations, not the objects.

**Step 1 — Abstract the problem to its relations.** The load-bearing structure: (a) an effect must cross a threshold at one target point (need +2.0 °C, from -4 to above -2 °C); (b) every single available unit of the effect is below threshold (+0.7 °C < +2.0 °C); (c) units are harmless along their path below a damage bound (+0.7 °C ≤ +1.0 °C forest bound); (d) effects add where they arrive together (additivity at ≥3 overlaps).

**Step 2 — Find the known situation with the same structure.** This is the converging-forces family: many weak forces, harmless individually along different paths, exceed a threshold only where they *converge*. The fortress siege: the general cannot take the fortress with one large force (the single road is mined); he splits the army into small groups that arrive simultaneously — each group alone would be slaughtered; together they take it. Radiation therapy: many low-intensity beams aimed at the tumor so the dose sums at the focus while healthy tissue along each beam stays below harm. A phased array focuses radio energy the same way. The orchard is the fortress.

**Step 3 — Map surface to structure explicitly.**
| Source (fortress siege) | Target (orchard frost) |
|---|---|
| small army divisions | fan plumes (+0.7 °C each) |
| fortress (must fall) | orchard canopy (must cross -2 °C: need +2.0 °C) |
| each division alone too weak | each plume alone +0.7 °C < +2.0 °C |
| territory along each march route | hillside forest (+1.0 °C harm bound) |
| divisions converge simultaneously | ≥3 plumes overlap → rises add |

**Step 4 — Transfer the relations and compute.** Place fans on separate ridgelines so their plumes converge on the basin center. Need: -4 → above -2 °C = +2.0 °C. Three overlapping plumes: 3 × +0.7 = +2.1 °C → canopy -1.9 °C. Thin — margin only +0.1 °C. Four plumes: +2.8 °C → canopy -1.2 °C, margin +0.8 °C. Choose 4 fans (4 × 2 h = 8 crew-hours ≤ 24). Hillsides: each plume +0.7 °C ≤ +1.0 °C bound → forest unharmed; additivity is confined to the basin center, where the orchard is.

**Step 5 — Check against the in-domain options.** Central heater: +0.3 °C < +2.0 °C — fails. Sprinklers: 40% twig breakage — the cure damages more than the disease. Single wind machine: +0.4 °C — fails. Status quo: 100% loss. Only the converged arrangement crosses the threshold — with the same 12 fans the team already has.

**Step 6 — Uncertainty and robustness.** If the event runs colder than forecast: at -4.5 °C need +2.5 °C — 4 plumes (+2.8 °C) still cover; at -5 °C need +3.0 °C — add a 5th fan (+3.5 °C); capacity exists (12 fans, 24 crew-hours). Fallback if a fan fails: the reserve fleet replaces it; the convergence pattern tolerates unit loss better than any single-unit plan. The 3-fan option is explicitly rejected on margin (+0.1 °C).

**Trace summary box.** Structure: threshold at target; sub-threshold units; path-harm bound; arrival-additivity. Source: converging-forces family (fortress siege / radiation beams / phased array); 5 correspondences mapped. Decision: 4 fans on 4 ridgelines converging on the basin → +2.8 °C, canopy -1.2 °C, forest unharmed, 8 crew-hours. In-domain options rejected by their own numbers. Margin +0.8 °C; fallback: 5th/6th fans for colder events.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to the Analogical style — abstract to relations, name a known domain with the same structure, map surface vs structure explicitly, transfer the relations, verify with the fixed numbers. The pure style performs excellently here: the mapping pass is what generates the candidate class (convergent arrangements) that the in-domain frame hides, and the transfer is fully checkable against the fixed facts (threshold, additivity, bounds, crew budget).*
