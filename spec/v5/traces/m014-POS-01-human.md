# Human Baseline — Constraint Theory / Bottleneck Thinking — m014-POS-01
**Style enforced: Constraint Theory / Bottleneck Thinking (find → exploit → subordinate → elevate → repeat). Full visible trace.**

## 1. Find the constraint
- Serial line: throughput = min(stage capacities) = min(120, 80, 100, 110) = **80/hr**. Demand 90/hr → shortfall 10/hr.
- **Empirical signature**: WIP grows ONLY at S2's input buffer; buffers before S1, S3, S4 stay empty. Work accumulates just upstream of the slowest stage and nowhere else — the system itself is pointing at S2. S2 is the binding constraint. Do not argue with the WIP.

## 2. Exploit (get everything from the constraint, free)
- S2 is idle 3% of the time (starvation: breaks, changeovers). Recover it first: staggered breaks, pre-staged changeovers, kits staged at S2's input. ~+2.4/hr for zero capex, and it widens the benefit of any later lift.

## 3. Subordinate (everything else serves S2)
- S1, S3, S4 have 20–37% slack; they must never starve S2 (buffer in front of S2) and never flood it (excess WIP is inventory, not throughput). S2 sets the drum; the rest march to it. Priority maintenance on S2. Inspection stays downstream of the constraint — it inspects what S2 actually makes.

## 4. Elevate (only the constraint gets investment; min-math decides)
- **A** (S2→100): min(120, 100, 100, 110) = **100/hr** ≥ 90 ✓ — $200k, 8 weeks, inside the 12-week deadline.
- **B** (S2→160): min(120, 160, 100, 110) = **100/hr** — identical output to A at 3× the cost. The second line is invisible: S3 caps the line at 100/hr. Reject.
- **C** (S3→140): min = **80/hr** — zero gain. Inspecting more output than the line can make.
- **D** (S4→180): min = **80/hr** — zero gain. Packaging 10/hr of air.
- **E** (S1→150): min = **80/hr** — zero gain. More prep for a line that can't eat it.
- **"Balanced upgrade" ($1.17M)**: min = 100/hr — the same 100/hr as A for 5.85× the money. While S2 binds, every dollar spent off S2 is dead money. Kill it.

## 5. Repeat (the constraint moves)
- After A, the min is a **tie: S2 = S3 = 100/hr**. The constraint is no longer singular. Demand 90/hr sits safely under 100 — but if demand ever exceeds 100/hr, the next lift must touch S2 and S3 together (or raise S3, then re-examine). Re-locate the constraint by WIP signature before spending again — the signature, not the org chart, is truth.

## Conclusion
Fund **A only**. Exploit S2 now (starvation recovery, buffer, priority) at zero cost; lift S2 to 100/hr ($200k, 8 weeks — inside the deadline); verify the new 100/hr steady state and the new S2/S3 constraint pair; re-run the loop only if demand crosses 100/hr. Total spend $200k, not $1.17M. The line's constraint was never the balanced-upgrade problem the managers imagined — it was one stage, and the rest of the money buys nothing.
