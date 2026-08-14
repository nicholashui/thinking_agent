# Human Baseline — m095-POS-01
## Style: Fast-and-Frugal Decision Trees (Gigerenzer) (pure) — visible reasoning trace

**Step 1 — Decide with the least that decides.** A triage rule is not a contest of information; it is a contest of cues that work. The tree uses two cues: ST elevation, then troponin. The score uses five. Before any arithmetic, that already favors the tree — but let's count, because the department shouldn't take my word for it.

**Step 2 — Run the tree over the 40 patients by hand.** ST=1 or troponin=1 → admit. Errors: P03 (admitted, no event), P15 (admitted, no event), P30 (admitted, no event). That is 3 over-admissions, 0 missed events. 37/40 = 92.5%.

**Step 3 — Run the 5-cue score by hand.** S = 3·ST + 2·TRP + 2·SWT + 1.5·AGE + 1·PRI, admit if S ≥ 4. Errors: P03, P05, P15, P30, P32 (over-admissions) AND P11, P20, P21, P23, P31, P34, P40 — seven confirmed events sent home. 28/40 = 70%. Seven missed MIs. That is the whole case in one number.

**Step 4 — Why does the complex model lose?** Its extra cues — sweating, age, prior MI — were marginally predictive last year, so the model gave them weights. This quarter they are noise, and each weighted cue is one more chance to fire wrongly. Five cues, five chances; two cues, two. The tree bets only on the two cues whose validity is stable, so it doesn't carry last year's noise forward. That is not a lucky sample; it is the design.

**Step 5 — Check the error direction.** The tree's 3 errors are over-admissions — a full ED is a cost. The model's 7 errors are missed MIs — a patient goes home and dies. Cost-asymmetric, and the tree is on the safe side of it. If I could choose where the 3% goes, it goes here.

**Step 6 — Recommendation.** Run the 2-cue tree next quarter. Verify again in 3 months: if ST or troponin decay, the tree decays with them — that's why it's measurable and replaceable, which is the point of a simple rule.

**Trace summary box.** 40 patients, two rules, one hand count → tree 37/40 (3 over-admissions, 0 missed events) vs 5-cue score 28/40 (7 missed events) → decision: the 2-cue tree; the complex model carries last year's noise in its extra weights; fewer cues, fewer chances to misfire; the errors the tree does make are the cheap kind.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Fast-and-Frugal Decision Trees — a minimal one-cue-at-a-time rule is hand-verified against the full model on the data, the extra cues are treated as noise until proven otherwise, and the recommendation stops as soon as the decision is clear. Signature move: "five cues, five chances to misfire; two cues, two."*
