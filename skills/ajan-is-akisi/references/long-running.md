# Scheduled and always-on agents

Routines on a schedule, event-driven agents, long unattended runs and the files that carry work between sessions.

## 1. Should it be an agent? (K23)

- A procedure is a skill; it needs an agent only when it has its own schedule, access or memory.
- One agent, one job. When its memory starts carrying a second job, split it.

## 2. Task file (K1, K4, K8)

Before writing it, question the user one point at a time and leave unknowns as `[blank]` (K4). The file contains:

- purpose;
- inputs and where they come from;
- steps;
- output format;
- prohibitions;
- an acceptance criterion that is countable or yes/no (K1);
- "if stuck, stop and report" (K8).

## 3. Caps (K15)

- Set a ceiling on turns and spend for every run (for example the client's max-turns and max-budget options).
- A step that fails three times stops the run with a short report.
- Output that fails its check gets one retry at most; then it is marked "failed check" and the run stops. A broken result never goes out looking like a good one.

## 4. How a run ends (K24)

- Decide in advance that every run ends in exactly one of three ways: send the result; say "nothing to send"; or ask for approval and stop.
- Every run writes its own log line: time, what it checked, how it ended.
- Before scheduling, run it by hand at least twice. During the first week, read every output yourself.
- Consider the slowest schedule the job tolerates, or a narrow event trigger instead of a timer, and a cheap "has anything changed?" check in front of the expensive part.
- Consider starting quiet: report little at first and earn the user's attention over time.

## 5. Approval and access (K14, K26)

- Start with the outward-facing layer switched off: the agent drafts, a human presses the last button (K14).
- Reversible work may finish unattended. Irreversible work (deploys, payments, outgoing messages, deletions, schema changes) is prepared and waits for approval; where the client supports it, use a deferred tool call or an approval request (K14).
- Give the agent only the tools it needs, one folder to write to, and read-only access to connected services where possible. Keep credentials out of the agent's environment; let a proxy outside it add them (K26).
- An agent that reads outside content (web pages, email, issues) must not be able to give orders to an agent that can spend or write. Scan that content for prompt injection inside the run (K26).

## 6. Handoff between sessions (K22)

Keep one handoff file and update it at the end of each session or before a tool switch:

- what was done, and which files changed;
- what is unfinished;
- what was tried and failed, and why;
- the next step.

Update the file; don't stack new ones. A long-running agent keeps a progress entry per open job and reads the index at the start of every run.

## 7. Memory (K17, K30)

- The raw record (logs, transcripts) is the base. Notes and curated pages sit on top; a small index loads every session.
- Store only what cannot be looked up again; for data that lives in another system, store a pointer.
- Run a periodic consolidation pass: check notes against the raw record, merge duplicates, prune what is stale.
- Tell the agent what memory is for and leave the how to it. Strict recording rules can make memory worse.
- Before adding a memory layer or product, measure a baseline on your own data: raw history plus search with a strong model (K17). Whether a curated layer beats plain search is unsettled and likely depends on the size of the corpus and on whether the layer is maintained; measure (K30).

## 8. Parallel and long runs (K21, K31)

- Parallel agents in one repository each get their own worktree and branch (K31).
- Long tool output goes to a file with a pointer and a summary in context; truncate past a limit and note where the rest is (K21).

## Before switching it on

- [ ] Task file complete, acceptance criterion countable or yes/no
- [ ] Turn and spend caps set; three-failure stop and one-retry rule written in
- [ ] Each of the three endings defined, and a log line per run
- [ ] At least two manual runs read by a human
- [ ] Irreversible actions behind approval; outward layer off at first
- [ ] Tools, folders and credentials limited to the job
- [ ] Handoff or progress file in place
