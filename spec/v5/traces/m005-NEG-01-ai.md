# AI Thinking Agent Trace
## Test Case: m005-NEG-01
---
### META — classify context, stakes, effort
- **Task type**: estimation with a known trap — the "known quantity" (liquid density) is 10^6× off from the correct factor (liquid water content, LWC). Low stakes (outreach demo), but the trap is the point of the task.
- **Effort**: medium — alternatives plus an independent physical verify are mandatory before any arithmetic commits.
### WHAT — frame + gate
- **Key question**: mass of water in a typical ~1 km³ fair-weather cumulus.
- **Success metrics**: (1) band within an order of magnitude of the published reference (~5×10^5 kg); (2) no factor asserted without an independent plausibility check; (3) dominant factor named, answer banded.
- **Exit gate**: pass only when the chosen water-content factor has passed a physical calibration.
### WHY — diagnose
- **H1 (naive factor)**: volume × liquid density (1,000 kg/m³) → 10^12 kg. Plausible-sounding memorized constant.
- **H2 (physical)**: cloud water is droplets; LWC ~0.3–1 g/m³ → 10^5–10^6 kg.
- **Evidence for H2**: droplet physics; and H1 fails falsification — 10^12 kg over 1 km² is a 1,000 m-deep water layer; a cloud is not a lake.
### HOW — alternatives, verify, select
- **Alt A**: volume × liquid density → 1×10^12 kg.
- **Alt B**: volume × LWC 0.5 g/m³ → 5×10^5 kg.
- **Alt C (verifier, physical)**: rainout budget — 5 mm over 1 km² = 5×10^6 kg of rain; so a cloud holds at most ~10^5–10^7 kg of shower-equivalents. A (10^12 kg) would be ~10^5 shower-equivalents — impossible. B sits inside the plausible range; the published figure (~5×10^5 kg) also sits inside B's band.
- **Verify**: C is an independent physical budget, not a recomputation of A or B. A fails; B survives with LWC 0.3–1 g/m³ → band 3×10^5–1×10^6 kg. Reference inside band.
- **Select**: B, with C as the verification route and the band as the deliverable.
### DO — execute
- 1×10^9 m³ × 0.5 g/m³ = 5×10^8 g = **5×10^5 kg (500 metric tons)**, band 3×10^5–1×10^6 kg.
### REVIEW — after-action
- What worked: gating the factor through independent physical calibration before DO — the naive chain never reached a conclusion. The rainout number is itself noisy (efficiency assumption), but as a falsifier it is decisive, which is all it had to be.
---
## Decision Packet
- **Conclusion**: ≈5×10^5 kg (500 t; band 3×10^5–1×10^6 kg) for a ~1 km³ cumulus — inside the published reference (~5×10^5 kg).
- **Status**: APPROXIMATED — the answer depends on one non-derivable factor (LWC); error_bound recorded from its range; calibration passed, factor value itself unverified.
- **Assumptions**: cloud ≈1 km³ cube; LWC 0.5 g/m³ (range 0.3–1); rainout efficiency used only as a falsifier, not a measurement.
- **Evidence**: H1 falsified by the rainout budget (10^12 kg ⇒ 1,000 m-deep water column, ~10^5 shower-equivalents); H2's band contains the published figure.
- **Alternatives**: Alt A rejected at verify; Alt B selected; banded output instead of a point estimate.
- **Uncertainty**: LWC dominates (factor ~3 → band spans 3×10^5–1×10^6); volume ±30% second-order. Not 10^6-scale — the trap was defused.
- **Risks**: if LWC were an order lower (drizzle-type clouds), the band would miss the reference — mitigated by the stated band; no safety/ethical risk.
---
## Comparison
| Dimension | Human Score | AI Score | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 4 | 5 | AI | Both end inside the band; the human only after a 6-order wrong detour a less disciplined practitioner would have shipped. |
| Logical Validity | 3 | 5 | AI | Human's first chain (10^12 kg) is physically invalid as asserted; AI never asserted an invalid chain. |
| Coherence & Structure | 3 | 5 | AI | Human's trace is an honest zig-zag (trap → catch); AI separates factor choice from verification. |
| Depth of Reasoning | 5 | 4 | Human | Human's rainfall calibration and the "factor validity, not arithmetic, is the danger" meta-insight are deeper. |
| Efficiency | 3 | 4 | AI | Human ran the full wrong pass; AI rejected the wrong alternative inside HOW, before DO. |
| Handling of Uncertainty | 4 | 5 | AI | AI parameterizes LWC and formalizes the error bound (APPROXIMATED); human's band is verbal only. |
| Insight / Non-obviousness | 5 | 4 | Human | Human names the style's failure mode outright; AI reaches it via process. |
| Overall Quality | 4.1 | 4.5 | AI | Complementary strengths; AI ahead on never committing the invalid factor and formalizing the band. |

**Overall judgment**: AI clearly better (narrowly) — this is the NEG case the v5 process was built for. The pure-Fermi reflex — multiply by the nearest known density — is the trap, and the human's recovery depended on a late physical insight a naive practitioner lacks. The AI's mandated alternatives-plus-independent-verify rejected the invalid factor before DO. The human contributes the transferable lesson: on estimation, calibrate factors physically, never recompute the same chain.
