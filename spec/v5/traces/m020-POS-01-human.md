# Human Baseline — m020-POS-01
**Human Thinking Model**: Pre-Mortem Analysis — strict, pure application.
**Prompt contract**: Reason ONLY in the Pre-Mortem style. Full visible trace. Begin by assuming the plan has failed; back-cast to causes; then mitigate. Do not evaluate the plan's merits until the failure has been reconstructed.

---

## Trace

**Step 1 — The plan as given.**
Volt-2 holiday launch: design done, pricing set, $4M media (non-refundable at T+6), retail agreements signed (liquidated damages for late delivery), manufacturing at TianTech, $8M committed by T+12. Asked: commit or not. The plan reads as confident — production "on track," channel slots locked.

**Step 2 — PRE-MORTEM. Assume the failure.**
It is one year from today. Volt-2 is called a disaster: the season was missed, the channel relationship is damaged, and — the part that hurts most when I look back — the competitor's spring product owns the slot Volt-2 was expected to take. I write the obituary first, in the past tense: "Volt-2 missed the holiday window entirely. Media spend was wasted, retail penalties were paid, and the channel slot passed to the competitor, permanently."

**Step 3 — Back-cast: what happened?**
Working backward from that failure, I generate causes and force each to be plausible against the scenario data — a cause with no supporting fact is discarded.
1–3. Generic candidates — marketing miss, pricing, product quality: plausible but unsupported by scenario data (Volt-1 shipped fine from the same CM); the back-cast discards unsupported causes.
4. **Capacity: TianTech's line went to its largest customer during peak season.** The contract's capacity-first clause, which never bit during Volt-1's off-season production, now bites exactly when it matters. This is IN the data, unhighlighted.
5. **Lane: the single LA/Long Beach lane congested again (2 of the last 5 Q4 seasons ≥10-day delays); no force-majeure carve-out in the retailer contracts; zero buffer stock.**
6. **Compounding: the missed window wasn't a quarter — it was the channel. The competitor's spring product took the slot.** The year-later failure is worse than "we sold less."
Causes 4–6 are the ones the plan's own confidence hid; 1–3 survive only as generic filler. The back-cast separates them by refusing to accept an unsupported cause.

**Step 4 — Rank by likelihood × impact.**
| Rank | Cause | L | I | L×I |
|---|---|---|---|---|
| 1 | Capacity-first clause + no buffer (4+5) | High | Catastrophic | **Killer** |
| 2 | Channel displacement (6) | Med | Permanent | **Critical** |
| 3 | Marketing miss (1) | Med | Moderate | Medium |
| 4 | Pricing (2) | Low | Moderate | Low |
| 5 | Quality (3) | Low | High | Low |

Not equal weight. One killer risk dominates; the mitigation budget goes there.

**Step 5 — Mitigate the top cause BEFORE commitment.**
1. **Qualify a backup manufacturer now** — sample production run at a second CM within 10 weeks; a no-go at T+10 on this is itself a decision signal.
2. **Build buffer stock of the hero SKU** to cover 4 weeks of peak demand by T+10, landed via the lane while it is still calm.
3. **Add a second shipping route** (air-freight fallback for hero SKUs) and renegotiate a force-majeure/partial-delivery clause with retailers.
4. **Gate the commitment**: T+6 media buy proceeds only if backup qualification and buffer plan are on schedule; T+12 full commitment only if the T+10 checkpoints pass. If either fails — delay to spring deliberately, before the money is non-refundable.

**Step 6 — The commitment decision, as changed by the pre-mortem.**
Without the pre-mortem: approve as-is, $8M committed, all risk behind one clause nobody flagged. With it: conditional approval — "commit, but the gate rules the calendar." And the second-order consequence is now visible: the failure is not $8M lost; it is a permanently surrendered channel slot to a competitor whose product ships spring. That consequence is what makes the mitigation urgent rather than nice-to-have. This is not paralysis: we commit, with conditions and a stop rule.

---

## Verdict for the eval
The trace demonstrates the method on its home ground: assume failure → back-cast → rank → mitigate before commitment. The killer risk (capacity-first clause + single lane + zero buffer) was buried in scenario data and surfaced because the failure was assumed first; the mitigation changes the commitment itself (gate at T+6/T+10) and names the permanent-displacement consequence. All rubric items met.
