# Human Baseline — m022-NEG-01
**Human Thinking Model**: Decision Trees & Scenario Planning — strict, pure application.
**Prompt contract**: Reason ONLY as a decision-tree analyst: build the tree, roll back, then run sensitivity on the INPUTS (probabilities AND branch values), check calibration and verifiability, bound the tree, and decide. Full visible trace.

---

## Trace

**Step 1 — Build the tree (bounded).** One decision node (choose A/B/C) → three macro chance nodes (Growth .5 / Stagnant .3 / Crisis .2, as given) → project chance (Good/Weak). 18 leaves. The 72-leaf draft (formats × phasing) adds arithmetic, not decision — rejected before enumeration: no leaf outside the 18 can change the choice.

**Step 2 — Roll back (as given).**
- A: Growth 0.7(60)+0.3(10)=45 ; Stagnant 0.6(30)+0.4(−5)=16 ; Crisis 0.3(15)+0.7(−25)=−13 → 0.5(45)+0.3(16)+0.2(−13) = **24.7**
- B: Growth 21 ; Stagnant 8.4 ; Crisis 0.5(−7)+0.5(−11)=−9 → 0.5(21)+0.3(8.4)+0.2(−9) = **11.2**
- C: Growth 17 ; Stagnant 8.1 ; Crisis −3 → 0.5(17)+0.3(8.1)+0.2(−3) = **10.3**
As given: A. Fine arithmetic, garbage inputs.

**Step 3 — Attack the inputs (sensitivity = calibration + verifiability, not just number-shuffling).**
- Calibration: where does crisis p=0.2 come from? A 5-year window containing one downturn. The region's last 6 retail cycles held 2 crises → calibrated p_crisis = **0.35** (renormalize: Growth 0.45, Stagnant 0.20).
- Verifiability: which branches rest on data? B and C have real histories (8 years; 3 downturns) — stand. A is a new metro with zero history: every A probability is a guess, and "Crisis → Good(0.3)+15" is fabricated — a new metro has no tenant pipeline in a downturn. Downturn comparables: A crisis = −40 (0.6) / −60 (0.4) → node **−48**, not −13.

**Step 4 — Re-fold with corrected inputs.**
- A: 0.45(45) + 0.20(16) + 0.35(−48) = 20.25 + 3.20 − 16.80 = **6.65**
- B: 0.45(21) + 0.20(8.4) + 0.35(−9) = 9.45 + 1.68 − 3.15 = **7.98**
- C: 0.45(17) + 0.20(8.1) + 0.35(−3) = 7.65 + 1.62 − 1.05 = **8.22**
The verdict flips: C > B > A. A was overstated by $18.05M (−5.80M probability correction, −12.25M branch correction). What the naive tree hid: the entire A−C gap rode on four unverifiable numbers.

**Step 5 — Where the EV is noise, the rule decides.** B vs C (7.98 vs 8.22) is a 0.24M gap inside input error. Apply rules that need no fabricated numbers: **maximin** (best worst case: A −60, B −11, C −6) → C. **Ruin line**: A's worst case −60 crosses Nordmart's $45M capital buffer; C's −6 does not. Both rules say C, and the corrected EV agrees.

**Step 6 — Principle + decision.** When the pivot branch is unverifiable, the robust rule decides, not the EV. **Decision: C — home-region expansion.** (Follow-on: revisit A as a pilot once one season of real data exists.)

---

## Verdict for the eval
The strict tree rescued itself: calibration (0.2 → 0.35), verifiability (A crisis −13 → −48), corrected re-fold with the flip (A 6.65 < C 8.22), maximin + ruin line → C, 72-leaf explosion bounded at the 18-leaf tree. The naive rollback (A, $24.7M, "decisive") is exactly the trap the discipline avoids.
