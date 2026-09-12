# Simulation protocol

## 1. Define the falsifiable question

Write one primary question and target band before coding. Secondary metrics diagnose why the primary metric passes or fails; they must not silently replace it after results arrive.

## 2. Reproduce the real rules

Extract current values from authoritative project data where possible. Match:

- units and time step;
- ordering of simultaneous operations;
- integer/floating-point behavior;
- rounding and clamps;
- caps and cooldowns;
- RNG distributions, pity, and reset behavior;
- information visible to each policy.

Hash or record the input configuration so reports can be reproduced.

## 3. Model player policies

Policies should differ by decisions, knowledge, reaction/attention, and risk tolerance—not by secretly changing game rules. Give each a plain-language behavioral definition.

Use scenarios to represent external conditions such as difficulty tier, input method, market regime, session length, or content stage. Run the policy × scenario matrix.

## 4. Search and sign-off

- Early search: enough runs to reject clearly poor regions quickly.
- Candidate comparison: larger samples and common seeds where useful to reduce comparison noise.
- Sign-off: fresh seeds, convergence check, full policy/scenario matrix, and calibration against real gameplay.

Do not declare a universal run count. Rare events and heavy tails may require far more samples than ordinary outcomes.

## 5. Sensitivity and interactions

Start with one-factor-at-a-time sweeps for attribution. Rank knobs by movement of the primary metric. Then test interactions among the few influential knobs; one-at-a-time analysis cannot reveal synergy or cancellation.

Keep candidate values inside documented safe ranges. Do not mutate production configuration during exploratory analysis unless explicitly requested.

## 6. Report uncertainty

Include sample count, seed, mean, standard deviation, percentiles, rate intervals, and missing/invalid run counts. Separate:

- stochastic sampling uncertainty;
- uncertainty in input values;
- uncertainty in player behavior;
- structural model error.

## 7. Calibrate

Compare a small set of representative model cells against actual game results. If model and game diverge, repair the model before increasing simulation volume. More runs do not correct a wrong model.

## 8. Human gate

After numerical targets pass, ask a playtest question tied to the intended experience. Examples: whether waiting feels tense or empty; whether recovery feels earned; whether a rare reward feels exciting rather than obligatory.
