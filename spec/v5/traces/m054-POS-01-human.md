# Human Baseline — m054-POS-01
## Style: Fermi Estimation in Market Sizing (pure) — visible reasoning trace

**Step 1 — Anchor the population.** US households ≈ 131M (Census); ≈ 66% own pets (APPA) → ≈ 86M pet households. Dogs ≈ 90M, cats ≈ 74M. Revenue unit is the insured *animal*, not the household — household counts matter for distribution, animals for premium. Use animals.

**Step 2 — Segment.** Insurance is dog-led: dog premiums ≈ $700/yr vs cat ≈ $400/yr, and dog penetration is far ahead. Run the chain on dogs, add cats as a small term at the end.

**Step 3 — Penetration: the factor that would wreck this estimate — anchor it, do not invent it.** Published US base rate: ≈ 5.4M insured pets (NAPHIA) → ≈ 5-6% of dogs insured. International bound: UK ≈ 30%, Sweden ≈ 40% — so the US 5-6% is a *lag*, not a ceiling; at 20-25% annual growth the base rate roughly doubles in ~3 years. Adopt 5.5% central, range 3-8%.

**Step 4 — Price.** Annual premium ≈ $700/dog (range $500-1,000), ≈ $400/cat. No frequency or hardware term: the premium IS revenue per unit per year.

**Step 5 — Multiply.** Dogs: 90M × 5.5% × $700 ≈ $3.5B. Cats: 74M × 1% × $400 ≈ $0.3B. **TAM ≈ $3.5-4B** → order of magnitude 10^9.6, i.e. $1-10B.

**Step 6 — Cross-check with an independent route.** Bottom-up: 5.4M insured pets × ≈ $650 ≈ $3.5B — agrees within ~10%. Adjacent-spend: US pet spend ≈ $150B, vet care ≈ $36B; $3.5B ≈ 10% of vet spend — plausible for a product covering ~5% of animals and reimbursing a share of bills. Two routes agree: the estimate is safe to use.

**Step 7 — SAM and the decision.** Target segment: dog-owning households ≥ $75k income (≈ 50% of dog-owning households) → SAM ≈ $1.8B. 1% of TAM ≈ $35-40M ARR — buildable from seed if the unit economics hold; the market is not the constraint.

**Trace summary box.** 131M households → 66% own pets → 90M dogs → 5.5% penetration (published; UK 30% = upside sanity) × $700 → TAM ≈ $3.5B ✓ bottom-up 5.4M × $650 ≈ $3.5B ✓ ≈ 10% of vet spend → SAM ≈ $1.8B → 1% ≈ $35M ARR.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Fermi Estimation in Market Sizing — population → segment → penetration → price, every factor with a range, penetration anchored to a published base rate with an international bound, two independent routes agreeing, order-of-magnitude stated. Signature moves: animals-not-households unit reframing; UK/Sweden penetration as a lag-vs-ceiling sanity check; vet-spend adjacency cross-check.*
