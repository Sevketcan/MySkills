# Systems mapping

Use after the concept and core loops are coherent enough to identify implementation responsibilities.

## Method

1. Extract systems explicitly named in the concept.
2. Infer only the support systems required to make the documented loop function. Mark inferred systems.
3. Merge responsibilities that do not justify independent state, rules, or ownership.
4. For each system record inputs, outputs, owned data, dependencies, priority, design risk, and proof method.
5. Draw dependency direction from provider to consumer and flag cycles.
6. Sort design order by dependency and uncertainty. A high-risk prototype may precede an otherwise foundational system.

## Priority definitions

- **MVP** — required to test the core fun hypothesis.
- **Vertical Slice** — required for one representative polished loop.
- **Alpha** — required for feature-complete play with placeholder content.
- **Full Vision** — polish, content expansion, and nonessential depth.

## Systems index structure

```markdown
# Systems Index: <game title>

> Status: Draft | In Review | Approved
> Source concept: design/gdd/game-concept.md

## Overview

## Systems
| System | Category | Priority | Status | Owns | Inputs | Outputs | Depends On | Risk | Proof |
|---|---|---|---|---|---|---|---|---|---|

## Dependency Layers
### Foundation
### Core
### Feature
### Presentation
### Polish

## Circular Dependencies

## Recommended Design Order
| Order | System | Why Now | Required Evidence |
|---|---|---|---|

## High-Risk Systems
| System | Risk Type | Falsifiable Question | Cheapest Validation |
|---|---|---|---|

## Deferred Systems
| System | Earliest Tier | Why Deferred |
|---|---|---|
```

## Mapping checks

- Every step of the core loop has an owning system.
- Every MVP system is necessary for the stated prototype hypothesis.
- No value has two authoritative owners.
- Dependencies are bidirectional in documentation: consumer names provider and provider names consumer.
- Circular dependencies are broken by ownership or an interface, not ignored.
- UI displays state but does not silently own gameplay truth.
