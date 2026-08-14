# Human Baseline — m066-POS-01
## Style: Strong Inference (Platt) (pure) — visible reasoning trace

**Step 1 — Hold the competing hypotheses simultaneously.** The swelling jump has a cause, and the method forbids fixing on one before the experiment. H1: anode change (CarbonCore). H2: formation-profile change. H3: electrolyte lot (E-77 vs E-88). H4: transport temperature (reefer outage). Four hypotheses, each consistent with the facts, none privileged by salience — the supplier change is the visible event, which is precisely why it is the least trustworthy suspect.

**Step 2 — Test what the retrospective data can do.** The fatal feature of week 37: both changes shipped in the same week and nothing since has been made without both. Old anode + new profile: zero cells. New anode + old profile: zero cells. The two factors are perfectly collinear — any regression splits the blame arbitrarily. The dashboards are structurally powerless; no amount of historical data changes that.

**Step 3 — Design the discriminating experiment.** The experiment must manufacture the missing cells: 2×2 factorial — {AnodeTech, CarbonCore} × {old profile, new profile} — 30 cells per arm, using remaining AnodeTech stock and current CarbonCore stock, all built the same week, blocked on one electrolyte lot (E-88; E-77 cells flagged separately), then the standard 45 °C / 2-week swell screen. 30 per arm detects a 3× rate difference at conventional power. Cost: 120 × $26 ≈ $3.1k — against a $4–6M recall, the experiment is free.

**Step 4 — Map every outcome to elimination (the heart of the method).**
- Swelling high wherever CarbonCore is present (both profiles) → H1. Eliminate H2, H3, H4.
- High wherever the new profile is present (both anodes) → H2.
- Both main effects, no interaction → H1 and H2, independent.
- High ONLY in CarbonCore × new-profile → interaction: the anode is toxic only under the new profile — reverting either one alone fixes it. A different decision than H1+H2.
- High in all four arms, including old×old → no production factor explains it → H3 or H4. Second-stage discrimination: split arms by electrolyte lot and cross-check swelling against cells that traveled the breached reefer routes. Lot tracks, routes don't → H3. Routes track, lot doesn't → H4.

**Step 5 — Name the traps this design kills.** Trap 1: single-hypothesis fixation — "blame CarbonCore," because it is the visible change; the profile change was silent, and the data cannot tell them apart. Trap 2: the uncontrolled rollback — "revert the formation profile and watch" is not an experiment: a whole-population change with no counterfactual arm. If swelling drops you have learned nothing about the anode. The factorial runs both traps out of the room.

**Trace summary box.** 4 hypotheses (incl. silent ones) → collinearity found: week-37 changes, zero overlap → 2×2 factorial × 30, lot-blocked, $3.1k vs $4–6M → outcome map: marginals / additive / interaction-only (revert either) / all-elevated → ambient branch (lot split + route check) → traps named: supplier fixation, uncontrolled rollback.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Strong Inference — competing hypotheses first, the experiment as sole arbiter, exhaustive outcome→elimination mapping, and the two traps the method exists to kill. Signature move: manufacturing the confound-breaking (missing) cells instead of re-analyzing confounded data.*
