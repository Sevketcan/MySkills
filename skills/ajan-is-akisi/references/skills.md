# Skills: decide, structure, vet and measure

## 1. Skill, agent or nothing? (K11, K23)

- A repeatable procedure becomes a skill. A job with its own schedule, access or memory becomes an agent (K23).
- If you explained the same thing twice, write the skill (K11).
- A one-off task needs neither.

## 2. Structure (K11, K12)

- A skill is a folder: `SKILL.md` at the centre, detail in `references/`, templates in `assets/`, repeated code in `scripts/`. Don't write what the model already knows (K12).
- Project and personal facts (names, schemas, platforms, preferences) stay out of the body. The skill tells the agent to read them from the project's manifest or rules file. Portability test: could another team use the skill with their own manifest without rewriting it? (K12)
- Personal settings live in the user's rules file, so updating the skill does not overwrite them (K12).
- Add a Gotchas section and grow it from real failures (K11).

## 3. Description (K12)

- Write it as a trigger: when should the client choose this skill?
- Say how it differs from the nearest installed skill and what it does not cover. A new skill with a similar description can break the selection of skills that already work.

## 4. After installing (K12, K13)

1. Check that each client actually loads the skill (its loader or a harness check).
2. Run a few realistic prompts and see which skill gets picked. Look for overlap with installed skills.
3. Install selectively: every installed skill adds context. Don't install the same skill twice from two sources, and track which skills get used (K13).

## 5. Third-party skills and plugins (K16)

1. Read the code before installing: scripts, hooks and install steps.
2. Pin a version or commit. Never install `@latest`, and never pipe an unpinned URL into a shell.
3. Install from the official source; watch for lookalike packages.
4. Consider waiting a couple of weeks before adopting a brand-new release.

## 6. Measure (K33, K19)

1. Collect real tasks from your own work. Keep the tasks you tune on separate from the tasks you test on.
2. Run every task with and without the skill (or old and new version), each more than once.
3. Keep some tasks that the change should not affect, as a control.
4. Compare outcomes and what changed in behaviour, not only a score. Static quality scores, public leaderboards and a single run are not enough to decide (K33).
5. Consider changing one thing at a time, so you can tell what caused a difference (K19).

## Output

- the decision (skill, agent or nothing) and why;
- for a new or revised skill: the folder layout, the description, and its closest neighbour with the difference;
- for a third-party skill: what the code does, the pinned version, risks found;
- for a measurement: a table per task (with, without, what changed) and the decision.
