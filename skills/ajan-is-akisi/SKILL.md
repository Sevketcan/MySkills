---
name: ajan-is-akisi
description: "Set up how a coding agent works so its results are proven: plan in steps that each carry a check and get the plan challenged, define done as a check the agent cannot fake, brief subagents and set up reviewers that never see the author's reasoning, keep AGENTS.md / CLAUDE.md short and true to the code, decide when a procedure becomes a skill and measure skills with paired runs, and design scheduled or always-on agents with caps, handoffs and approval lines. Use for the working method; it does not hunt bugs in a diff, generate skill files or create the schedule itself."
---

# Coding Agent Workflow

An agent's "done" is a claim until a check it cannot fake confirms it. Plan in small checked steps, keep the main context clean, let someone who did not write the work review it, turn every repeated mistake into a rule, and stop before anything that cannot be undone. This skill sets up or repairs that method in a project; it does not replace the project's own rules.

## Before starting

- Read the project's rules files first (`AGENTS.md`, `CLAUDE.md` and anything they import) and its decision or architecture documents. Project rules override the generic rules here. Where a rules file and the code disagree, don't silently pick a side: list each mismatch for the user (K27).
- Find the project's own checks: test, typecheck, lint, build and end-to-end commands. They define "done". If there are none, propose one cheap check first (K1, K34).
- Establish what is irreversible here: does a push deploy, do migrations run on merge, does anything pay, send messages or delete data? Those steps need the user's approval (K14).
- Note which client runs the agent (Claude Code, Codex or another). Hooks, subagents, worktrees and schedulers differ; name the feature you rely on and fall back to a written step where it is missing.
- In a repository you did not write, read its rules files before letting an agent run there: they are instructions to the agent (K26).

## Choose the mode

Use only the mode the request needs:

1. **Plan and verify**: a code change or multi-step task, from plan to proven result. Read [plan-and-verify.md](references/plan-and-verify.md).
2. **Subagents and reviewers**: whether to split the work, how to brief a subagent, how to run parallel writers, how to set up a review that is not the author grading itself. Read [subagents-and-review.md](references/subagents-and-review.md).
3. **Rules files and lessons**: write, trim or audit `AGENTS.md` / `CLAUDE.md`, and turn repeated mistakes into rules. Read [rules-files.md](references/rules-files.md).
4. **Skills**: decide whether a procedure should be a skill, check a skill's structure, description and overlap, vet a third-party skill, measure whether a skill helps. Read [skills.md](references/skills.md).
5. **Scheduled and always-on agents**: routines, long unattended runs, handoffs between sessions and agent memory. Read [long-running.md](references/long-running.md).

If the request is unclear and touches code, start with mode 1.

## Principles

- Done means a check the model cannot fake has passed: a test, a build, a real response. The model does not grade its own work (K1).
- Plan first, attach a check to every step, and re-plan when a step goes wrong (K3).
- Write the least code that solves the problem. Ask whether it needs to exist at all, don't widen the scope silently, and report unrelated problems instead of fixing them (K5).
- When something is ambiguous, state your reading and the trade-off. Ask one short question only when the answer matters; make small decisions yourself (K6).
- Keep dependent steps in one agent; use subagents for independent search, research and review (K7).
- A reviewer sees the request, the output and the sources, never the author's reasoning (K32).
- Fix the rule, not the output. A mistake that comes back becomes a rule; an explanation given twice becomes a skill (K11).
- Keep raw tool output out of the main context, but read the full output when verifying (K21).
- Tune effort before switching models. Search and summaries can run cheap; code edits and decisions stay on the main model (K20).

## Guardrails

- **Approval line:** finish what is reversible; prepare what is not (a push that deploys, production data, schema changes, payments, outgoing messages, deletion) and stop for approval. Push and deploy only on explicit instruction (K14).
- **Hard rules in code:** a rule that must never break also goes into a hook, a deny rule or a repository rule; a line in a rules file is context the agent can skip (K14).
- **Stop rule:** if the same check still fails after three rounds, stop and report what you tried and what blocks you. Never present a failed or unrun check as passed (K1, K15).
- **Flaky tests:** don't make a flaky test pass by rerunning it, skipping it or adding `sleep` (K34).
- **Third-party code:** read a skill, plugin or package before installing it, pin the version, never install `@latest`, and use the official source (K16).
- **Least privilege:** give each agent only the tools and accounts its job needs. An agent that reads outside content must not be able to give orders to an agent that can spend or write (K26).
- **Shared checkout:** parallel writers get separate worktrees and branches; no `reset --hard`, `clean` or `stash` in a shared working tree (K31).
- **Secrets:** never print secrets or put them in briefs, rules files, logs or commits.

## Boundaries

- Finding bugs in a specific diff is the reviewer's job; this skill decides how that review is set up (mode 2).
- Generating a new skill's files belongs to the client's skill-authoring tool, if it has one; this skill supplies the decision and the checks (mode 4).
- Creating the schedule itself belongs to the client's scheduler; this skill decides what the routine does and how each run ends (mode 5).
- The user's personal setup (global settings, installed plugins, hooks) is theirs: propose changes, don't install them.

## Completion

End each task with:

- what changed, with each check that ran and its result;
- what was not verified, and why;
- proposals, listed separately from changes;
- decisions waiting for the user;
- any lesson worth one line in the project's rules file (K11).

The (Kn) markers point to [kurallar.md](references/kurallar.md) (Turkish), which lists each rule's sources and evidence level. It is compiled from the owner's research notes in Twitter Notes (taslak v0.1).
