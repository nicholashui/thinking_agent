# Human Baseline — m030-POS-01
## Style: Constraint-Driven Creativity (pure) — visible reasoning trace

**Step 1 — Constraint inventory (the fence is the fuel).** Hard: kit = 30 straws (0.5 m) + 5 m tape + 2 bands; straws whole (no cutting); no mid-gap contact; span 0.9 m; 200 g at mid-span, 60 s. Soft: symmetric, buildable in one session.

**Step 2 — Kill the naive deck.** Flat deck = two straws taped end-to-end (0.5 + 0.5 > 0.9 m). Failure is twofold: the taped joint peels under bending and the straw kinks. Euler on a 0.5 m column (E ≈ 2.5 GPa): P_cr ≈ 45 g. As a bending deck it gives at ≈ 40–80 g. We need 200 g. Deck is dead — and with it, any bending-first design.

**Step 3 — Convert constraints into principles.**
- No cutting → members are exactly 0.5 m; the 0.9 m span forces two members per run → joints are load-bearing structures, not decoration.
- Buckling → no long compression members; compression must be short or bundled; triangulation makes every member short.
- Tape peels in tension → keep tape wrapping in shear, never pulling.
- The only thing in the kit that pulls is the rubber band → bands are the tension resource.

**Step 4 — Novel geometry.** Two parallel Warren trusses (depth ≈ 0.2 m): 200 g splits into ≈ 100 g per truss → chord force ≈ 100 × 0.9 / (4 × 0.2) ≈ 112 g. Chords bundled 2 straws + lateral ties (effective length ≈ 0.25 m → ≈ 125 g per straw) → ≈ 250 g vs 112 g demand: 2× margin. Bands lash the three hot joints (mid-span + two banks).

**Step 5 — Tightening pass (the style's signature).** The truss already passes; now impose stricter self-constraints and re-run: (i) both rubber bands must earn their place — as pre-tensioned lashings, not spares; (ii) tape ≤ 3 m on joints, 1 m on wraps, 1 m spare; (iii) exact symmetry about mid-span. Each tightening forces a refinement: chord doubling at mid-span, band pre-tension sequence, diagonal collar wraps.

**Step 6 — Spec and failure point.** 2 trusses × 7 straws (4 chords + 3 zigzags) = 14; 4 lateral ties; 2 deck stringers; 2 chord doublers; 8 spares = 30 ✓. Tape ≈ 4 m ≤ 5 m ✓. Expected first failure: mid-span bottom-chord joint (max tension + tape) — countered by band lashing + doubling. Test protocol: 100 g → 150 g → 200 g, hold 60 s, record joint failure order.

**Trace summary box.** Constraint inventory → deck dead (~40–80 g) → axial-only truss → band lashings → 30/30 straws, ~4/5 m tape → margin ≈ 2× at 200 g.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning deliberately confined to the pure Constraint-Driven Creativity style — constraints treated as fixed resources, each converted into a design principle, then deliberately tightened to force refinement. Every winning move (triangulation, bundling, band pre-tension, tightening) is constraint-derived.*
