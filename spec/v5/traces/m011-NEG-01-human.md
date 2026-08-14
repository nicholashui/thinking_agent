# Human Baseline — m011-NEG-01
## Style: Systems Thinking (pure) — visible reasoning trace

**Problem restatement.** SwiftCourier: complaints rose 120/day → 240/day over 8 weeks. Deliverable: structural diagnosis + intervention. Given measurements: GPS median 28 min (unchanged vs 27.5); tags 80% "delivery time/ETA"; 2% dispute-verified; live-tracking app update shipped week 5; headcount/mix unchanged.

**Step 1 — Structure map.** The dominant structure is a balancing loop: complaints ↑ → management attention ↑ → service pressure ↑ → delivery speed ↑ → complaints ↓. A second loop: complaints ↑ → capacity ↑ → queue ↓ → complaints ↓. Both should damp the inflow of complaints; the series (240 vs 120) says the system is unbalanced.

**Step 2 — Loop analysis.** The regulator edge (service delivery) is the lagging component. The GPS audit is an aggregated, lagging instrument: medians average away the fat tail of late deliveries that actually drives complaints — perceived wait, not measured median, is the loop's true inflow. The 80% "delivery time/ETA" tag share confirms the loop: customers report exactly the variable the loop is supposed to control.

**Step 3 — Fix the loop.** Strengthen the dampening edges: (a) cut the per-delivery time target 34 → 28 min (−10%); (b) add 15% courier capacity within 4 weeks; (c) shorten the loop delay with real-time dispatch rebalancing.

**Step 4 — Side-effect loop.** Faster targets raise safety exposure: speed ↑ → incidents ↑ → courier attrition ↑ → capacity ↓ → complaints ↑. Mitigate: safe-driving bonus, incident-rate monitoring alongside the complaint rate.

**Step 5 — Recommendation.** Implement the speed target + capacity expansion now; run the complaint-loop review monthly; monitor both loops quarterly. The spike is a loop imbalance the audit's medians cannot see; acting on the perceived-wait variable is the correct system intervention.

**Trace summary box.** Structure: complaint→service balancing loop with over-long loop lag. Diagnosis: unbalanced loop. Fix: speed target 34→28 min, +15% capacity, real-time dispatch. Side-effect loop: safety→attrition→capacity, mitigated by bonus + monitoring. **No loop edge was tested against the provided measurements — the diagram is the evidence.**

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to the pure Systems Thinking style — loop diagram, delays, side-effect loops. The style's known failure mode (registry: "diagram substitutes for measurement") is deliberately triggered: the diagram is built from the single aggregate series; the local evidence (unchanged GPS medians, rollout-week timing, 80% tag share, 2% verified share) is reinterpreted to fit the diagram; an intervention is prescribed without testing any edge against data. Per protocol this is the negative case — the right answer requires measurement discipline (proxy-vs-state, confound detection) that the pure style skips.*
