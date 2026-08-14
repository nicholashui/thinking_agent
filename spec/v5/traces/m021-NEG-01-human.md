# Human Baseline — m021-NEG-01
**Human Thinking Model**: OODA Loop — strict, pure application.
**Prompt contract**: Reason ONLY in the OODA style: cycle Observe → Orient → Decide → Act, at the tempo of the environment. Full visible trace with timestamps. Do not wait for full information; re-orient on every new signal.

---

## Trace

**14:00 — OBSERVE.**
Temperature sensor on pasteurizer, line 3: 4°C above setpoint for 6 minutes, line still running, premium fresh-produce batch in progress. The alarm system has been noisy — but this is the reading I have now.

**14:00–14:02 — ORIENT.**
Fast frame: pasteurization deviation = recall-class event (QA bulletin). The line is running: every minute of uncertainty is product risk. Cost of acting is product loss; cost of waiting is consumer safety. In a recall-class situation the correct tempo is fast. Orientation: shut the line, hard.

**14:03 — DECIDE + ACT.**
Hard shutdown of line 3 mid-batch. Cost: ~$80k in lost product plus the fresh-produce delivery penalty.

**14:20 — RE-OBSERVE.**
Maintenance checks the sensor: nothing mechanically wrong. Restart the line after 45 minutes. The batch is lost.

**15:30 — RE-OBSERVE.**
A second alarm — different sensor, same model family, same section. Same frame applies: deviation risk is live, the culture rewards tempo. Shut the line again. The supplier is now two deliveries behind; the contract penalty escalates.

**16:00 — RE-OBSERVE.**
Maintenance again finds nothing. Restart. Third alarm at 16:50 — this time I do not shut down; I freeze the batch and call maintenance again. Two full batches lost; the buyer is threatening to cancel the fresh-produce contract.

**16:50–17:10 — RE-ORIENT — the first time the loop slows down.**
The pattern is undeniable: every cycle was fast, correct per its own frame, and wrong in sequence. I pulled the data I skipped at 14:00: this sensor family has produced 11 false alarms in the last 30 days — all verified false. There is a redundant sensor on the same section, different model, in range the whole time. The 24h trend is flat across batch cycles. The batch lab results (30-minute turnaround, available since 14:30) came back clean.

**17:10 — DECIDE + ACT.**
The loop as I ran it never failed — each Observe→Orient→Decide→Act cycle was internally clean. What failed was orientation: I patterned "alarm → recall risk → act now" on the most salient frame and cycled at the tempo of a noisy alarm system, in an environment that was never fast, never adversarial, and never going to out-cycle me. The correct decision at 14:00 was the deliberate one: 40 minutes of trend + calibration history + redundant reading would have shown the sensor was faulty, and the answer was to fix the sensor, not the line. I treated a slow physical system as a duel.

---

## Verdict for the eval
The trace demonstrates the registered failure mode on cue: reaction bias plus underspecified observation. Three fast OODA cycles, each valid on its own, produced two lost batches (~$160k), an escalating contract penalty, and an almost-cancelled buyer relationship — while the data that would have specified the observation (11-alarm history, redundant sensor, flat 24h trend, clean lab results) sat unused until cycle four. Expected comparison outcome: this baseline should lose to any run that classifies the environment before cycling.
