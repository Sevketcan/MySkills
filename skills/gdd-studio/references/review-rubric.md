# GDD review and balance rubric

Review evidence and consequences, not prose polish. Report issues by severity and point to the exact document/section when files exist.

## Single-document review

Check:

- purpose and player fantasy are consistent with the concept and pillars;
- rules are complete enough to implement without inventing design;
- state transitions, ordering, tie-breaking, and edge cases are explicit;
- formulas define units, bounds, rounding, clamps, and ownership;
- tuning values have safe ranges and a validation plan;
- dependencies identify data flow and authoritative owner;
- UI/feedback exposes the information needed for meaningful choices;
- acceptance criteria are measurable;
- open decisions are visible rather than disguised as finished prose;
- scope matches the assigned milestone.

## Cross-document review

Check:

- dependency links agree in both directions;
- the same term, item, state, or value has one meaning and one owner;
- formulas compose without unit, timing, or range contradictions;
- no two systems silently modify the same state;
- progression loops do not compete for the same scarce player attention without priority;
- onboarding order matches dependency order;
- multi-system scenarios can be walked from input to final feedback without a missing handoff.

## Dominant strategy test

For each recurring decision:

1. List the available actions.
2. Estimate expected reward, risk, information requirement, and opportunity cost.
3. Ask whether one action dominates across most states.
4. Identify whether counters are visible and realistically usable.
5. Prefer changing incentives or information over adding arbitrary punishment.

## Economy review

Map every source, sink, converter, storage cap, unlock gate, and multiplier. Then test:

- positive feedback and snowball rate;
- runaway inflation or resource irrelevance;
- hoarding incentives and dead currency;
- bankruptcy, soft-lock, and unrecoverable stall states;
- whether the optimal choice is repeatedly to wait;
- whether rewards scale faster than meaningful expenses;
- whether multiple currencies create distinct decisions.

Use calculations or simulation when balance depends on repeated compounding. Clearly label modeled assumptions.

## Scope review

Flag:

- features that do not test the current hypothesis;
- systems whose content burden exceeds their mechanical value;
- dependencies that force unrelated work into the MVP;
- “future-proof” abstractions without a current consumer;
- polish being used to postpone a core-loop decision.

## Verdict

Use one verdict:

- **Approved** — implementable, coherent, and appropriately scoped.
- **Needs revision** — usable after specific non-foundational corrections.
- **Major revision** — core rules, ownership, or player-purpose contradictions block implementation.

Organize findings as: blockers, important revisions, optional improvements, confirmed strengths, and the smallest next action. Do not modify approved documents unless the user asks for the changes.
