# Human Baseline Trace — Principal-Agent Analysis
## Test Case: m083-POS-01 (Positive)

Method discipline: strictly principal–agent. Every claim is a payoff function, a derivative, or an equilibrium; people are treated as expected-value maximizers of their own contract, never as moral characters. The model's strength — predict misbehavior before it happens, then fix it by contract — is applied end to end.

### 1. Map the game: principal, agent, and each payoff
- Principal: the firm. Residual per engagement at discount d: (1 − d) − 0.80 = **0.20 − d** ($M).
- Agent: the account manager, paid α = 2% of revenue: per engagement **0.02(1 − d)**.
- Volume: N(d) = 10(1 + 4d). Both payoffs scale with N(d).

### 2. Agent's equilibrium — her derivative, not her character
- Her payoff: Π_a(d) = 0.02·10(1+4d)(1−d) = 0.2(1 + 3d − 4d²).
- dΠ_a/dd = 0.2(3 − 8d): zero at d = 0.375, positive through the cap. Under d ≤ 25% she chooses **d = 25%**.
- Outcome: revenue 20×0.75 = **$15M**; her pay 0.02×15M = **$300k** (up 50%); firm profit 20×(0.20 − 0.25) = **−$1M**.
- The agent is doing exactly what the contract pays her to do. "Dishonest" is not an explanatory category.

### 3. Principal's optimum and the break-even threshold
- Π_f(d) = 10(1+4d)(0.20−d) = 10(0.20 − 0.2d − 4d²); derivative −0.2 − 8d < 0 throughout ⇒ firm optimum **d = 0**, profit **$2M**.
- Break-even per deal: 0.20 − d = 0 ⇒ **d = 20%**. Every engagement signed below 20% margin destroys value — and the contract pays the agent 2% of every dollar of that destruction. The entire conflict lives in the region d ≥ 20%.

### 4. Redesign — make the agent's pay a function of the residual
- Pay on profit, not revenue: β = 10% of per-deal profit. Π_a'(d) = 0.10·10(1+4d)(0.20−d) — the same shape as the firm's, scaled. Her derivative is now the firm's derivative; her optimum is **d = 0**.
- Verification (the non-negotiable step): recompute her choice under the new contract — same derivative sign as the firm's (negative throughout) ⇒ equilibrium d = 0, firm profit **$2M**, her pay 0.10×2M = **$200k**.
- Pay-neutrality check: she earned $200k at list under the old contract too. The redesign removes the premium on the value-destroying boundary without asking her to take a haircut at the aligned point.

### 5. Second-best if profit share is infeasible
- Price floor d ≤ 15% (< break-even 20%): her optimum hits the floor; firm profit 16×0.05 = **$0.8M** — damage capped, conflict not removed. Profit-linked pay is first-best; a floor is a bound, not a fix.

### 6. Interpretation (the point of the exercise)
- The observed data (revenue +45%, profit −$0.4M) is the equilibrium, not a scandal. Fire the agent and the same contract reproduces the same behavior from the replacement.
- General rule: the agent's pay must move with the principal's residual (sign-matched derivative). Any pay tied to a number the principal does not keep (revenue, bookings) invites the agent to buy it with the principal's margin.
- The board's question inverts: not "is the manager dishonest?" but "whose optimum is the contract implementing?" — hers. Redesign the contract.

### 7. Final answer
- Status quo: d = 25%, revenue $15M, firm −$1M, manager $300k. Firm optimum d = 0 ($2M); break-even d = 20%. Fix: 10% profit share ⇒ equilibrium d = 0, firm $2M, manager $200k, pay-neutral. The agent is rational; the contract is the actor.
