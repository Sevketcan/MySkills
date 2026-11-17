# Plan and verify

From request to proven result. Steps 1-4 happen before any code changes.

## 1. Does it need to be written? (K5)

Ask in order and stop at the first yes:

1. Does it need to exist at all? Ask "why?" about any use case nobody asked for and drop the invented ones.
2. Does the codebase already do it?
3. Does the standard library or the platform do it?

Only then write new code, and write the least that solves the problem.

**Broad sweeps** ("find every hidden state machine and improve everything"): first produce an inventory only, folder by folder, as a table. Implement afterwards in separate small steps the user picks (K5).

## 2. Plan (K3, K6)

- For work of three or more steps, write a short plan first. Each step names the check that proves it: a test, a typecheck, a build, a request to the running system.
- Before the first real run, rehearse the steps in text and look for the step you cannot check (K3).
- If the request is ambiguous, write down your interpretation and the trade-off. Ask one short question only when the answer changes the plan (K6).

## 3. Define done (K1)

- Write acceptance criteria that are countable or yes/no. "Good quality" is not a criterion.
- Prefer a check the model cannot fake. Where the client allows it, attach the check to the end of the run (a stop hook or a goal condition that runs the tests), so the agent cannot finish without passing it.

## 4. Challenge the plan (K4, K32)

Don't ask "is this plan good?". Use one of these:

- **Interrogation:** before the plan or task file is written, question the user one point at a time. Leave anything unresolved as `[blank]` instead of guessing.
- **Fresh reviewer:** save the plan to a file and give it to a reviewer that has not seen the conversation (a new session or a subagent). It reads only the plan file and the sources the plan cites (K32).
- **Premortem:** assume the plan has failed and work backwards to the reasons.

The user decides which findings to act on (K4).

## 5. Execute (K3, K5)

- One step at a time; run its check before moving on.
- When a step goes wrong, stop and re-plan instead of patching forward (K3).
- Make surgical changes: touch only what the step needs. List unrelated problems for the user; don't fix them on the way (K5).

## 6. Verify (K34, K21, K1)

1. Run the change for real: first the end-to-end user flow (browser, simulator, rendered output), then narrower tests (K34).
2. If the project verifies often, consider giving the agent a fast, stable `verify` skill or script that drives the running system and returns evidence (screenshots, responses, logs) (K34).
3. For visual work, use fixed camera poses or screenshots, a motion capture where movement matters, and a measured performance threshold (K34).
4. Read the full output of the checks you rely on; filtered or summarised output can hide the failure (K21).
5. Before reporting a number, reopen its source; don't quote it from memory (K1).
6. A flaky test is a finding, not an obstacle. Don't rerun it until it passes, skip it or add `sleep`; report it with what you know about the cause (K34).

## 7. Stop conditions (K15)

- If the same check fails after three rounds, stop. Write what you tried and what blocks you, then ask.
- Output that fails its check gets at most one retry; then mark it "failed check" and stop. Never present a broken result as good.
- In any loop, set a ceiling on turns and spend before starting.

## 8. Report (K1, K5)

- each check that ran, with its command and result;
- checks you could not run, and why; an unrun test is never reported as passed;
- remaining uncertainty;
- unrelated problems you noticed.
