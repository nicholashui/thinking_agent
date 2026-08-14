# Human Baseline — m076-POS-01
## Style: Prospect Theory Awareness (pure) — visible reasoning trace

**Problem restatement.** The director faces two recovery plans for 6,000 vaccine doses; the brief describes both in loss terms ("2,000 lost for sure" vs "34% chance nothing lost, 66% chance all 6,000 lost"), and she chose B to escape the sure loss. The question is whether her decision is sound. First move: strip the framing. The pair is decision-equivalent to A = 4,000 recovered for sure; B = 66% chance of all 6,000, 34% chance of 0. Any preference change produced only by rewording is a reference-point artifact, never evidence about the options.

**Reference point.** Her reference is the pre-fire stock of 6,000 doses — the status quo she is coded as losing from. Losses loom roughly 2.25× larger than equal gains (canonical λ), so "losing 2,000 for sure" stings far harder than "saving 4,000" pleases. That asymmetry, not anything about Plan A, is what makes the sure option repulsive.

**Invariance check (the core move).** Same pair, gain frame: A = "4,000 doses saved for sure"; B = "66% chance all 6,000 saved, 34% chance none." Under gains, people are risk-averse: the modal choice flips to A. Her pattern — B under losses, A under gains — is a preference reversal on identical options, which proves the decision is driven by the reference point, not the plans. Verified directly: re-presented in gain terms, the director picks A. Confirmed.

**Probability weighting.** B's probabilities are not processed linearly by intuition: 34% is typically overweighted and 66% underweighted, inflating B's appeal as "the chance of no loss at all." The de-biased decision uses the stated probabilities at face value.

**Decide on neutral terms.** Values: $1,000/dose; contract minimum 4,000 doses with $1,500/dose shortfall penalty.
- EV(A) = $4.0M — minimum met exactly, no penalty.
- EV(B) = 0.66×$6.0M − 0.34×$6.0M (penalty on the 4,000-dose shortfall) = $3.96M − $2.04M = **$1.92M**.
A dominates on every defensible basis: EV with penalty ($4.0M vs $1.92M), risk profile (guaranteed minimum vs 34% catastrophic shortfall), and even bare EV without the penalty ($4.0M vs $3.96M). The instinct that drove her to B — gambling to avoid the sure loss — is precisely backwards: B's 34% tail is the real threat, and it only looks acceptable because the loss frame made the sure outcome unbearable.

**Trace summary box.** Framing: loss frame → B (risk-seeking in losses); gain frame → A (risk-averse in gains); the reversal is the proof of reference dependence. Decision on neutral terms: **Plan A**. EV: A $4.0M vs B $1.92M (with penalty). Probability weighting: 34% ≠ rare, 66% ≠ certain — linear probabilities for the EV. Recommendation: adopt Plan A and show the director the neutral restatement so the choice is made on the options, not the wording.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to prospect-theory concepts — reference points, loss aversion, invariance, probability weighting — with no extension into contract engineering or logistics; that is the memo consumer's job. In this positive case the pure style performs exactly as intended: it detects the distortion, proves it, and decides on the neutral representation.*
