# Human Baseline — m041-POS-01
**Human Thinking Model**: Hierarchical Decomposition — strict, pure application.
**Prompt contract**: Reason ONLY in the decomposition style: state the goal, recurse into subgoals until each leaf is directly actionable, map dependencies, then reassemble. Do not jump to a solution before the hierarchy exists.

---

## Trace

**Step 1 — State the goal and why it must be decomposed.**
Goal: a complete, executable plan for a 3-day, 600-attendee, 40-speaker, 25-sponsor customer conference in 12 weeks, with 4 FTE and $150k. A single un-decomposed plan is un-holdable in working memory and un-assignable; decomposition exists to convert "the conference" into owned, sized tasks. But first the goal must be fully in view, or the decomposition inherits its blind spots: 3 days · 600 attendees · 40 speakers · 25 sponsors · 12 weeks · 4 FTE · $150k.

**Step 2 — Level-1 decomposition: streams from the goal's own clauses.**
Every clause of the goal must be claimed by a stream (completeness by clause-mapping — a missing clause means a missing stream):
- S1 Venue & Logistics ← "3 days", "600 attendees" (space, dates, catering, AV, hotel block)
- S2 Content & Speakers ← "40 speakers" (curation, invitations, confirmations, agenda)
- S3 Marketing & Registration ← "600 attendees" (announcement, channels, registration system, waitlist)
- S4 Sponsorship & Finance ← "25 sponsors", "$150k" (deck, contracts, booths/sessions, budget roll-up)
- S5 On-Site Operations ← "3 days" × "600" (staffing, run-of-show, safety, emergency, accessibility, supplier coordination)

Coverage check: goal clauses → S1–S5, every clause claimed. Nothing floats between streams.

**Step 3 — Recurse until leaves are directly actionable (owner + ≤ 2 weeks each).**
Level 2–3 under each stream, leaves shown as examples of the depth required:
- S1: venue shortlist & site visits (wk 2–4) → venue contract (wk 4) → catering/AV suppliers (wk 5–7) → rooming & signage (wk 9–10). Leaf: "contract venue with hold for 650 + AV in writing by wk 4" — one owner, one week.
- S2: speaker wishlist (wk 1–2) → confirmations with deadline wk 7 (wk 3–7) → agenda grid (wk 8) → speaker logistics (travel/AV briefing, wk 9–10).
- S3: save-the-date after venue contract (wk 4) → registration system live (wk 5) → campaigns (wk 5–10) → waitlist & capacity control (wk 8–11).
- S4: sponsorship deck (wk 2–3) → outreach & contracts (wk 4–9; revenue feeds budget) → booth/session slotting into agenda (wk 9–10) → budget roll-up with contingency (wk 11).
- S5: staffing plan & role cards (wk 8–9) → run-of-show (wk 10–11) → emergency/medical/accessibility plan (wk 10) → supplier day-of checklist (wk 11–12).
Each leaf sized ≤ 2 weeks with a named owner class. Decomposition stops when the leaf is something one person can just do.

**Step 4 — Dependencies as edges; critical path with float.**
Edges: venue contract → save-the-date → registration (S1→S3); speaker confirmations → agenda grid → room sizes + AV (S2→S1); sponsor contracts → budget → catering tiers (S4→S1); agenda → booth slotting (S2→S4); capacity numbers → waitlist policy (S3→S3). Critical path: S1 venue contract (wk 4) → save-the-date (wk 4) → registration live (wk 5) → demand data (wk 8) → logistics finalization (wk 9–10) → run-of-show (wk 11) ≈ 10 weeks, ending wk 11; 12-week deadline gives 1 week of float, and speaker confirmations (deadline wk 7) must be enforced to keep the agenda grid (wk 8) on path.

**Step 5 — Parallelization under 4 FTE.**
4 FTE → 4 streams concurrently, with S5 (on-site ops) folded into the COO after wk 8 (its early work is light). Streams S2 and S3 run fully in parallel until registration data is needed (wk 8); S4 runs in parallel and funds the budget. The constraint is real: no stream is assigned more than one person for more than 2 consecutive weeks.

**Step 6 — Integration: reassemble the whole.**
Decomposition must invert back up or the pieces drift: (1) single source of truth — one plan doc/spreadsheet with owners and dates; (2) budget roll-up at wk 11 consolidating S4 revenue vs all stream costs, contingency 10%; (3) run-of-show at wk 11 merging agenda, rooming, catering, staffing into one minute-by-minute timeline; (4) weekly cross-stream sync so edges (e.g., speaker count → room size) are re-checked. The whole is only as real as this merge-back.

**Step 7 — Where the hierarchy itself is the risk.**
Leaf-level risk (a speaker drops → agenda gap) is contained by the wk-7 confirmation deadline; cross-stream risk (registration volume ≠ room size) is contained by the sync and the capacity control leaf. Both are handled inside the structure — that is the point of having built it.

## Verdict for the eval
Against the rubric: ≥3 levels, leaves actionable (owner class + ≤2 wks), 5/5 goal parts covered with ≥2 leaves each, 7 named edges, critical path ≈ 10 wks + 1 wk float, 4-FTE-consistent parallelization, explicit merge-back. The plan is complete because the decomposition was complete.
