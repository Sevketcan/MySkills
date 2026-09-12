# System GDD authoring

Design one substantial system at a time. Read the concept, systems index, direct dependencies, and relevant decision records before drafting.

## Section cycle

For each unresolved section:

1. State the design question.
2. Present viable options and their player-experience, complexity, balance, and scope consequences.
3. Recommend one option.
4. Record the user's choice as confirmed, or label the current answer provisional.
5. Define how an implementation or playtest can prove the rule works.

## System document structure

```markdown
# <System Name>

> Status: Draft | In Review | Approved | Implemented
> Last updated: YYYY-MM-DD
> Implements pillars: <names>
> Priority: MVP | Vertical Slice | Alpha | Full Vision

## Summary
## Player Purpose and Fantasy
## Responsibilities and Non-Responsibilities
## Core Rules
## States and Transitions
| State | Entry | Behavior | Valid Exits |
|---|---|---|---|

## Player Actions and Feedback
| Action/Event | Preconditions | Result | Visual/UI/Audio Feedback |
|---|---|---|---|

## Interactions With Other Systems
| System | Direction | Data or Event | Ownership |
|---|---|---|---|

## Formulas
### <Formula Name>
`output = ...`
| Variable | Type | Unit | Source/Owner | Initial Value | Safe Range |
|---|---|---|---|---|---|

## Economy Sources and Sinks
## Edge Cases and Priority Rules
| Scenario | Expected Resolution | Rationale |
|---|---|---|

## Tuning Knobs
| Parameter | Initial Value | Safe Range | Increase Effect | Decrease Effect |
|---|---|---|---|---|

## UI and Information Requirements
## Accessibility Requirements
## Save/Persistence Requirements
## Acceptance Criteria
## Telemetry and Playtest Questions
## Open Decisions
## Rejected Alternatives
## Cross-References
```

Omit irrelevant optional sections, but never omit core rules, ownership, dependencies, edge cases, tuning knobs, acceptance criteria, and open decisions from an implementation-facing GDD.

## Rule quality

- Use explicit units, timing, bounds, rounding, clamping, ordering, and tie-breaking.
- Define behavior at zero, maximum, simultaneous events, interruption, save/load, and failure.
- Identify the authoritative owner of every shared value.
- Keep tuning values data-driven; do not confuse an initial tuning guess with a fixed rule.
- Acceptance criteria must be observable and falsifiable.
- For economy systems, quantify sources, sinks, circulation time, feedback loops, and bankruptcy/stall states.
