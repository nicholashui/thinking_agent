# v6 Routed AI Trace — m054-POS-01 (blinded)
## InsurePaw — US pet insurance TAM/SAM + "is 1% share plausible" board brief
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,product,strategy | g:decide,estimate,maximize | c:(none)
- Router top3: m011, m023, m024; confidence gap ≤ 0.5 → AMBIGUOUS → DUAL-ROUTE: m011 + m023 first-class passes, synthesize (§II.2.8 G1). m024 = router context (regret check on the entry). Evaluated-style pass m054 runs its chain contract (§II.2.9). No R3 context gates (no adversarial/one_shot/high_stakes/unmeasured). No deadline → tempo off. All factors anchored in the brief → CLOSED-SCOPE FAST PATH (P8): stages compress to one pass.
### WHAT — frame + structure-first scan (S1)
- Goal: defensible TAM + defendable SAM + 1%-share readout, order-of-magnitude, for board/fundraise. Structure: 4-factor multiplicative chain (population → segment → penetration → price) + one segment cut; revenue unit = insured *animal* (premium per animal/yr), NOT household — household counts feed distribution, animals feed revenue.
### WHY — P1 provenance audit + factor-class gate
- Factor classes: 131M households = measured anchor (given); 66% ownership = anchor; 90M dogs / 74M cats = anchor (APPA); $700 dog / $400 cat premium = anchor (NAIC); penetration = ESTIMATE → MUST carry an external anchor: published 5–6% of dogs insured (5.4M insured, NAPHIA) + international bound (UK ≈ 30%, Sweden ≈ 40%). A guessed "software-like" 20% penetration = ESTIMATE WITHOUT ANCHOR → gated out here, never reaches HOW (v5 AI's flaw: it had to screen this in HOW). Local-data-first: US brief, not global.
### HOW — style passes (dual-route + evaluated style, completion contracts §II.2.9)
- Pass m054 (sizing contract): TAM/SAM/SOM chain, every factor shown with range. 90M dogs → penetration 5.5% (3–8%) → $700 ($500–1,000): 90M × 5.5% × $700 ≈ $3.5B; cats add 74M × 1% × $400 ≈ $0.3B → **TAM ≈ $3.8B** (order $1–10B). Dominant-factor sensitivity: penetration 3–8% swings TAM ×2.7 ($2.1–5.6B) — the band is carried by penetration. Penetration-guess caveat: 5.5% is the published base rate, a *lag* (UK 30%), never a target; unanchored guesses excluded.
- Pass m011 (systems contract): stocks = insured animals; flows = annual premiums; loop = growth loop — 20–25%/yr premium growth → bigger insured stock → claims data → better pricing → higher penetration (self-reinforcing); falsifying observable = NAPHIA insured-pet census year-over-year; local-data-first ✓; cheap-fix-as-decisive-experiment = price the UK-penetration scenario as a ceiling test, not a base.
- Pass m023 (opportunity-cost contract): entry decision's true comparison is capital-in-time — $35M ARR from seed vs next-best use of €4M; market size is decision-relevant only if binding: TAM 100× the target → not binding; opportunity cost lives in unit economics (acquisition cost vs $700 premium), which no size changes.
- Divergence resolution (V2): all passes agree — TAM ≈ $3.8B, market not the constraint → agreement recorded; no guessed-factor candidate ever admitted.
### GATES — registry-weakness gate (R2/R3 style)
- Penetration-guess gate: no unanchored penetration factor passes WHY ✓. Cross-check gate: ≥1 independent route within ~2× required — bottom-up 5.4M insured × $650 ≈ $3.5B ✓ (~10%); vet-spend share ≈ 10% of $36B ✓.
### DO — P3 branch-completeness before commit (fast path: commit once)
- Negative branches priced: penetration stalls at 3% → TAM ≈ $2.1B, 1% ≈ $21M ARR — still buildable only if unit economics hold; the binding branch is acquisition-cost-vs-LTV, not size. SAM branch: ≥$75k dog-owning households ≈ 50% → $1.8B. Commit: TAM ≈ $3.8B (band $2.1–5.6B), SAM ≈ $1.8B, 1% ≈ $35–40M ARR — plausible; market not the constraint.
### REVIEW — insight pass (S2, packet gate)
- I1: the market compounds faster than entry — at 20–25%/yr the premium base doubles in ~3 years; a "1% today" is ≈0.5% of the 2029 market, so the share target must be quoted against today's base only.
- I2: penetration is a lag, not a ceiling — the same chain run by a later entrant at UK-level 30% lands 5× higher; timing, not size, is the strategic input.
### DECISION PACKET
- Conclusion: TAM ≈ $3.8B (order $1–10B; band $2.1–5.6B), SAM ≈ $1.8B, 1% ≈ $35–40M ARR — plausible and buildable from seed if unit economics hold; the market is not the constraint.
- Status: APPROXIMATED — sizing brief; error_bound = penetration-carried band (≈±0.5 order); the 1%-plausibility verdict itself is SOLVED-grade (robust to the band).
- Assumptions: recalled public figures — 131M households, 66% ownership, 90M dogs, 5.4M insured, $700/$400 premiums; 20–25%/yr growth persists.
- Evidence: factor table with class labels + ranges; cross-checks within ~2× (bottom-up $3.5B; vet-spend ≈10%); international ceiling bound.
- Alternatives: 20% guessed penetration (gated at WHY — anchorless); bottom-up route (used as cross-check); UK-level 30% scenario (priced as upside bound, not base).
- Uncertainty: penetration dominates (×2.7 swing; anchored 3–8%, ceiling shown by UK/Sweden); premium compression if vet inflation cools.
- Risks: board reads the midpoint as a commitment (mitigated: band + SAM + share readout); fundraise anchors on a base that doubles in ~3 years (mitigated: I1 growth-loop caveat in memo).
## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | both TAM ≈ $3.8B, SAM ≈ $1.8B, 1% ≈ $35–40M; both within ~1.5× of reference |
| Logical Validity | 5 | 5 | Tie | identical chain; both catch animals-not-households + anchored-penetration |
| Coherence & Structure | 4 | 5 | AI | staged packet + factor-class table vs human's single-pass cascade |
| Depth of Reasoning | 5 | 4.5 | AI | P1 class labels, P3-priced stall/UK branches, dominant-factor sensitivity beyond human's error ranking |
| Efficiency | 5 | 4.5 | AI | fast path + no invented-factor sweep (v5 AI was 4); human's five lines still leaner |
| Handling of Uncertainty | 3 | 4.5 | AI | human states ranges then asserts; AI band-only + penetration-carried width + caveat |
| Insight / Non-obviousness | 5 | 4.5 | AI | human's "lag not ceiling" matched by I2; I1 (market doubles in 3 yrs → quote against today's base) is new |
| Overall Quality | 4.6 | 4.7 | AI | v5 AI lost 4.4 vs 4.6; routed run installs the human's first-pass moves as WHY contracts and flips the case |
Winner: AI (narrow). Why: the human's decisive moves — animal-unit reframing, published-base-rate anchoring with the international ceiling, two independent cross-checks — are now mandatory WHY-stage contract items, so the v5 AI's sole flaw (the 20% guess it had to eject in HOW) never enters; fast path recovers efficiency and the growth-loop + sensitivity statements add depth, while the human retains only marginal leanness and cleaner insight phrasing.
