# Human Baseline — m021-POS-01
**Human Thinking Model**: OODA Loop — strict, pure application.
**Prompt contract**: Reason ONLY in the OODA style: cycle Observe → Orient → Decide → Act, at the tempo of the environment. Full visible trace with timestamps. Do not wait for full information; re-orient on every new signal.

---

## Trace

**T+0:00 — OBSERVE.**
SIEM: 15 GB already egressed from the analytics DB to an unknown IP, transfer still live at ~1.5 GB/min. Same batch: j.rivera's account (created 3 days ago via spear-phish, session token stolen, MFA bypassed) holds production read access. I read these as ONE chain, not two tickets: an attacker with a working credential and an active data pipe.

**T+0:01–T+0:03 — ORIENT.**
Two frames compete. Frame A — evidence-first: "confirm the attacker, then act" (60–90 min of forensics). Frame B — tempo: compare cycle speeds. Exfil→encrypt chains of this kind run 45–90 min; my delay costs 1.5 GB/min plus proximity to the encryption phase. Price the options: acting costs 2h degraded dashboards + one re-login wave — cheap and reversible. Waiting costs gigabytes, then encrypted production — expensive and irreversible. Key orientation move: I do NOT need the attacker's identity to justify rotating a stolen credential; the account's own history (phished, token stolen) justifies it. Orientation: tempo, stable frame.

**T+0:03–T+0:05 — DECIDE + ACT.**
Cut the analytics segment's egress; rotate j.rivera's credential; force re-auth on all sessions. Executed at T+5. Egress stopped at ~22 GB.

**T+5 — RE-OBSERVE + RE-ORIENT.**
Threat intel: egress IP is C2 of Kobalt-9, ransomware group; encrypts within 45–90 min of first exfil; spreads via SMB/PsExec. This confirms my frame — it is NOT new evidence against the decision. No reversal. New orientation task: verify offline backups of production DBs, prep encryption response. Decide: start backup verification now.

**T+15 — RE-OBSERVE + RE-ORIENT.**
j.rivera account: new login from Tel Aviv (HQ is Austin). The attacker is still active — the earlier decision stands. Act: force-logout every session on that account, geo-block the region, watch for lateral movement. Done within 2 minutes.

**T+25 — RE-OBSERVE + RE-ORIENT.**
Payment queue backs up. Convenient frame: "independent deploy issue" (a deploy went out at 08:30). Tempting — it keeps the incident small. Tempo discipline: check before accepting a convenient frame, but bound the check. 10-minute correlation pass: does the queue's source overlap j.rivera's reach? No overlap indicators; the backlog follows the deploy's timestamp pattern. Decide: tag as deploy-related, monitor, do NOT spin up a parallel incident that splits the team.

**T+45 — RE-OBSERVE.**
Kobalt-9 encryption confirmed on a staging environment only (no PII). Re-orient: the containment held. Egress cut at T+5, account dead at T+15, backups verified — production untouched, blast radius staging-only, total egress ~22 GB. Cycle closed.

---

## Verdict for the eval
The trace shows the method on its home ground: observe the chain, orient on tempo, price the wait in GB/min, decide on partial evidence, act, and re-orient at each signal without reversing course. The T+0 decision was made in 5 minutes against incomplete evidence, because the cheapest safe actions did not require knowing the attacker's identity — and every later signal (C2 tag, foreign login, payment backlog) was absorbed as an orientation update, not a re-litigation. Outcome: production untouched, blast radius staging-only, ~22 GB lost instead of the 100+ GB a forensics-first run would bleed before encrypting.
