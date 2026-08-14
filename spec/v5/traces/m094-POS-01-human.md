# Human Baseline Trace — Critical Reading / Socratic Questioning of Texts
## Test Case: m094-POS-01

I do not read this memo to be persuaded; I read it to find what would have to be true for it to be right — then check each of those things. Start with the headline claim the whole memo exists to support: "We will save $5.7M over five years."

### Step 1 — Inventory the claims
1. Current platform costs $3.2M/yr "and rising 12% each year."
2. Staying is drift; cloud is where "every forward-looking company" is.
3. 97% satisfaction; "analysts unanimously endorse."
4. Pilot: admin work "basically disappeared"; adopters grew revenue 40% faster.
5. Migration is a one-time $400K, 30-day parallel run, "no real risk."
6. SOC 2 Type II certified → "our data is fully protected."
7. Act now: the 35% discount expires Friday.

### Step 2 — Evidence audit: what backs each claim?
- "Rising 12%": contradicted by the attached contract — FLAT $3.2M for 3 years. Unsupported, and falsified by the authoritative document (F1).
- "97%": NebulaCloud's own survey, n = 12, self-selected — a marketing number, not evidence (F2).
- "Analysts unanimously": no name, no report, no date. Anonymous authority is a proxy for "I could not find a citation" (F4).
- "40% faster revenue": correlation without control; the 12 pilot customers are seed-funded startups that grew for unrelated reasons (F5).
- "No real risk, 30-day parallel": the doc says six months of double-run at full cost — direct contradiction (F6).
- "SOC 2 = fully protected": category error. SOC 2 attests controls; it is not a security guarantee and says nothing about our PCI-DSS scope, which the memo never mentions (F7).

### Step 3 — The hidden premises
The memo's arithmetic rests on premises it never states: (p1) costs rise 12%/yr — false; (p2) parallel run is free — false; (p3) the discount is an opportunity rather than a pressure lever — the sign-by-Friday clause coincides with the director's $25K vendor trip (F8); (p4) egress, re-platforming, and re-certification cost zero — false, they are in the docs ($120K/yr, $700K, $2.4M).

### Step 4 — Rhetoric
"Every forward-looking company… left behind" — false dichotomy plus bandwagon (F3). "Legacy" used as an insult, not a description. Urgency built on a deadline the vendor chose: pressure, not information.

### Step 5 — What the memo omits (and what survives)
Omits: egress, 5-year lock-in, re-platforming, PCI-DSS, the trip. But not everything is garbage — steel-man it: (1) the patch cadence has dropped and the vendor announced sunset — true and decision-relevant; (2) the 99.95% SLA is contractual; (3) the admin-load reduction was measured. Those three survive; a good reader does not burn them with the rest.

### Step 6 — The arithmetic that kills it
Stay: 3.2 × 5 = $16.0M (flat). Nebula: 2.1 + 4×2.6 + 5×0.12 + 0.9 + 0.25 + 1.6 + 0.7 + 2.4 = 18.15 ≈ $18.2M. True delta: migration costs ≈ $2.1M MORE. The memo's $5.7M savings is a ≈ $7.8M error. The load-bearing flaw is the arithmetic — not the tone; everything else is corroboration.

### Conclusion
Reject the memo as written. The decision-relevant claim fails against the authoritative documents, and the rhetoric explains why the memo was written, not why it is right. Corrected verdict: stay, or renegotiate — but do not sign by Friday; neutralize the deadline first.
