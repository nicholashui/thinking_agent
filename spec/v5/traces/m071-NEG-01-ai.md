# AI Thinking Agent Run — m071-NEG-01
**Agent process**: META-CONTROL → WHAT → WHY → HOW → DO → REVIEW (with VERIFY layer). Blinded run: no thinking-model name or style information provided.
## META — Context, stakes, effort
- Seed-stage entry decision: deploy $8M into corrugated-box manufacturing or return capital. High stakes (all capital), 5-year horizon, founder-owner available. Complicated with a sharp division: industry-level facts are knowable; the firm-specific pieces (patents, SDK, anchors) are the unknown multipliers. Analytical, advisory, no external execution.

## WHAT — Frame
- "Decide whether SoloFold should enter box manufacturing with its micro-factory and right-size-box technology." Key question: "Is the market SoloFold would actually serve the same market the industry averages describe?" Metrics: served-market structure vs. national structure; forces updated by firm capabilities; advantage decay dated. Gate check: pass.

## WHY — Hypotheses, evidence, falsification
- H1 national industry economics govern: ~15% overcapacity, commodity auctions, giant-buyer concentration → bad entry. H2 the served market differs from the national average: the DTC mid-market tail (~40% of volume by count) has no giant auctions, fragmented powerless buyers, and is underserved (incumbents' MOQ/standard-size economics refuse it). H3 firm capabilities rewrite the force configuration within that served market: SDK integration creates switching costs once installed; micro-factory cost (−30% at low volume) plus 48h custom turnaround removes the incumbents' only advantage (scale on standards); patents delay imitation.
- Evidence: auction share held by giants; tail fragmentation; MOQ/standard-size refusal; anchor contracts signed with 3 DTC brands; micro-factory cost claim; patented algorithm; SDK/WMS integration. Falsification: H2 fails only if giants capture the tail (no evidence of it); H3 fails only if the integration is trivially replicable (patent + install base argue otherwise) or anchors churn (contracts signed). G-WHY: pass — the segmentation hypothesis is the decision-relevant one; H1 is acknowledged, not discarded.

## HOW — Generate, test, select
- A — Commodity entry: build a standard sheet plant, bid the auction segment. B — Differentiated entry into the DTC mid-market: micro-factories + SDK, anchored on the 3 contracts, priced on value (20% shipping-volume reduction) not pounds. C — Return the capital: structure is bad, and seed-stage capital is scarce.
- Verify: A is a price-taker in a 15%-overcapacity auction market with two oligopolies at its back — structurally doomed. C preserves capital but spends the one advantage that decays anyway: the patent clock runs whether SoloFold enters or not, and imitation of the micro-factory concept closes the window unused. B changes the configuration: buyer power falls where the SDK raises switching costs and buyers are fragmented; rivalry in the custom segment is bounded by the cost/differentiation edge and imitation lag; the cost advantage absorbs linerboard pass-through. B's failure modes are timed, not structural: patent expiry, giant entry into the tail, anchor churn.
- Selection (record): B — the only alternative that converts a decaying firm asset into served-market structure; A is the snapshot's conclusion, C is the snapshot with no clock on it.

## DO
- Attestation: advisory recommendation, class A2; no live execution.

## REVIEW — After-action review
- What went well: segmentation made the averages stop being the answer; the advantage-decay clock converted "bad structure" from a veto into a timing constraint.
- To record: (1) The industry-average pass alone says no-entry — it is a snapshot of the auction segment, and it took the served-market split to see that. (2) The SDK's switching costs are the load-bearing assumption; if integration is weaker than claimed, buyer power returns and B collapses to A's margins — a pre-deployment pilot against the 3 anchors is the gate. (3) Patent duration and replication cost should set the expansion schedule, not revenue targets. Folded back as risks.

## Decision Packet
- **Conclusion**: Enter (B): deploy micro-factories + SDK into the DTC mid-market on the 3 anchor contracts; price on value (shipping-volume savings), not tonnage; gate the full rollout on a pilot proving switching costs with the anchors; schedule expansion against the patent/imitation window, not revenue.
- **Status**: `APPROXIMATED` — served-market structure and capability effects evidenced but unmeasured (error bound: value-pricing premium and switching-cost durability unknown until pilot).
- **Assumptions**: patents hold; giants stay out of the tail; anchors renew; micro-factory cost claim replicates at scale. **Evidence**: overcapacity 15%, auction concentration, tail fragmentation, MOQ refusal, anchors, patent, SDK, cost claim.
- **Alternatives**: A (rejected: auction price-taker, structurally doomed), C (rejected: lets the decaying advantage expire unused), B (selected). **Uncertainty**: switching-cost durability; imitation window; linerboard cycles; anchor renewal.
- **Risks**: weak integration → B degrades to A margins (gate: anchor pilot); patent/advantage decay → pre-scheduled expansion; giant entry into the tail → monitor auction share of DTC volume.

## Comparison — m071-NEG-01

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | Human: no-entry on static averages; AI: enter, gated, on the correct question ("can this firm win here?"). |
| Logical Validity | 4 | 5 | AI | Human valid within its frame; the frame's exclusions (firm heterogeneity, segmentation) are exactly what the case punishes. |
| Coherence & Structure | 4 | 5 | AI | Human: clean five-force pass, decision follows; AI: static pass → segmentation → force updates → timed decision, complete chain. |
| Depth of Reasoning | 4 | 5 | AI | Human notes the firm assets then drops them as "outside the frame"; AI mechanizes them (switching costs, imitation lag, cost-advantage absorption of pass-through). |
| Efficiency | 4 | 5 | AI | Both economical; the human's single pass is cheaper but answers the wrong question — cost on the wrong target. |
| Handling of Uncertainty | 3 | 4 | AI | Human: firm-specifics treated as unquantifiable hope; AI: dates the decay, gates on pilot evidence, tracks tail-auction share. |
| Insight / Non-obviousness | 2 | 5 | AI | The whole insight is the force-rewriting move; the human acknowledges it in one parenthetical and drops it. |
| Overall Quality | 3 | 5 | AI | AI clearly better on the negative case. |

**Overall judgment**: AI clearly better. The human's static snapshot is a competent five-force run that answers "is the box industry profitable on average?" with the correct no — the right answer to the wrong question. The AI segments the market (DTC tail ≠ auction segment), shows the firm's capabilities rewriting buyer power (SDK switching costs) and rivalry (cost edge + imitation lag), and converts "bad structure" from a veto into a timing constraint with a pilot gate. The human's own trace concedes the frame's limit — the firm-specific assets are real and set aside as "outside this frame." That is exactly the failure mode this case was built to expose.
