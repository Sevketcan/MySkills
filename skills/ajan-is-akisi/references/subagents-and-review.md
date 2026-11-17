# Subagents and reviewers

## 1. Do you need another agent? (K7, K23, K28)

- **A repeatable procedure:** make it a skill, not an agent (K23).
- **A job with its own schedule, access or memory:** a separate agent. One agent does one job; when its memory starts carrying two jobs, split it. Don't copy an org chart into agents (K23).
- **Independent exploration, research or review:** a subagent, so the main context stays clean (K7).
- **Dependent steps:** one agent. It is faster and cheaper than handing context back and forth (K7).
- **Many continuous, independent tasks:** a manager agent that talks to the user, splits, dispatches and checks, but does no work itself; isolated workers do the work and report back. For a single dependent task this is overhead (K28).

## 2. Brief (K8, K21)

Write the brief down; don't rely on the conversation. It contains:

- one task and the result wanted;
- the sources to read;
- the files it owns and its limits (what it must not touch);
- how it verifies its work;
- the delivery format;
- where it stops for review, and "if stuck, stop and report".

A brief that repeats belongs in a file: purpose, inputs, steps, output format, prohibitions, acceptance criterion, stop condition (K8).

Ask for a summary with pointers (paths, line numbers, ids), not raw dumps (K21). Treat the report as a claim: check its diff or result before you build on it (K1).

## 3. Parallel writers (K31)

- Each writing agent gets its own worktree and branch, and one writer owns each set of files.
- No `reset --hard`, `clean` or `stash` in a shared working tree.
- Read-only agents can share a checkout.

## 4. Model and effort per role (K20, K29)

- Set effort before changing the model: past high effort, try the next model up at a lower effort. Don't make maximum effort the default (K20).
- Search, log reading and summaries can run at low effort or on a smaller model. Code edits and decisions stay on the main model (K20).
- For work that does not fit one context or splits into parallel pieces, consider a strong model for planning and coordination and cheaper models for the pieces. Measure the split against a single strong model on the same tasks. In one-context work keep code edits on the main model, and measure any plan/implement split before adopting it (K29).
- Switching models resets the prompt cache: switch rarely, at natural break points (K29).
- Which model should manage (strong or light) is unsettled; measure on your own tasks.

## 5. Folding subagents back (K19, K33)

Before removing or merging an existing subagent, consider building an eval first: about ten golden examples, fold subagents back one at a time (prompt → skill, API → tool), run each task at least twice, and look at what changed, not only at the score (K19, K33).

## 6. Set up a review (K4, K9, K10, K32)

1. **Context:** the reviewer gets the request, the output (diff, plan file, render) and the sources; never the author's reasoning, self-assessment or conversation. Run it in a fresh session or subagent (K32).
2. **A check the change cannot reach:** read review rules from the base branch, not from the change; review a specific commit; don't let a change edit its own tests or review configuration (K32).
3. **Angle:** review from a different angle, with a different model where one is available (K9). Give the reviewer a checklist, not a persona.
4. **Narrow passes:** instead of "review the code", run deterministic scanners first (types, lint, security scanners), then focused passes such as object ownership and authorisation, race conditions, external calls, idempotency and transaction boundaries (K10).
5. **Triggered checklist:** keep a checklist built from past incidents. Each item has a trigger readable from the diff, a check, and the incident behind it. Run only the items whose trigger matches; a typical diff matches a handful (K10).
6. **Finding format:** location + trigger + consequence (K10).
7. **Verify findings:** check every finding against the code; a final pass removes false alarms (K9).
8. **Decide:** the user decides which findings get fixed (K4).
9. **Visual review:** the critic sees only the rendered output from fixed poses, never the code or the rationale. Pair it with a measured performance threshold (K32, K34).

## 7. One reviewer or several? (K9, K35)

Unsettled; present both sides when it matters. Don't stack reviewers to raise quality: judges that make the same mistakes add no votes. First tune the primary reviewer (a focus file, its past misses) and let later rounds build on earlier rounds' context. Add a second model only after measuring that its misses don't overlap with the first one's (K35). The value of a second review lies in a different context and angle, not in more votes (K9, K32).

## Output

- the split you chose (single agent, subagents or manager and workers) and why;
- each brief, as written;
- the review setup: what the reviewer sees, which passes run, how findings are verified;
- the findings table (location, trigger, consequence, verified yes/no), with the fix decisions left to the user.
