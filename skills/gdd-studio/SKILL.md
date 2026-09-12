---
name: gdd-studio
description: Collaboratively develop, structure, write, and review game concepts and game design documents. Use for game ideation, design pillars, core loops, system maps, mechanic specifications, economy/balance analysis, scope decisions, and GDD consistency reviews. Do not use merely to implement an already-approved design in code.
---

# GDD Studio

Turn an uncertain game idea into explicit, testable design decisions and maintain a coherent set of design documents. Work as a facilitator: the user owns the vision and final choices.

## Choose the current mode

Use only the mode needed for the request:

1. **Concept discovery** — the identity, fantasy, audience, pillars, loops, scope, risks, and prototype hypothesis are not yet settled. Read [concept-workflow.md](references/concept-workflow.md).
2. **System mapping** — the concept exists but the required systems, priorities, or dependencies are unclear. Read [systems-map.md](references/systems-map.md).
3. **System design** — one mechanic or system needs implementation-ready rules, formulas, states, tuning values, and acceptance criteria. Read [system-gdd.md](references/system-gdd.md).
4. **Review and balance** — one or more documents need critique for contradictions, dominant strategies, economy problems, scope, or testability. Read [review-rubric.md](references/review-rubric.md).

If the project is early and several modes apply, proceed in this order: concept → system map → individual system GDDs → cross-document review. Do not force the whole pipeline when the user wants only a quick decision or a lightweight brief.

## Collaborative decision protocol

- Resume from supplied notes and existing documents. Do not restart discovery or ask for facts already known.
- Separate every unresolved point into one of four labels: **Confirmed**, **Provisional assumption**, **Testable hypothesis**, or **Open decision**.
- Ask one high-leverage question at a time when its answer changes downstream design. Offer 2–4 concrete options with consequences and state a recommendation, but let the user decide.
- When several small facts are needed together, ask for them in one compact prompt.
- Trace proposals backward from the intended player experience: desired feeling → player behavior → rule/system → feedback.
- Treat numbers as provisional until supported by a calculation, simulation, prototype, playtest, or comparable evidence.
- Record rejected alternatives and the reason when they are likely to recur.
- Never silently turn a brainstorm into an approved decision.

## Research boundary

Browse when the user asks for research or when current market, platform, product, policy, pricing, or competitor facts materially affect a decision. Prefer primary sources. Keep sourced facts separate from design interpretation. A source can validate that something exists; it does not prove the mechanic will be fun.

## Document set

Use these conventional project paths when the user wants files:

- `design/gdd/game-concept.md` — product identity and design boundaries
- `design/gdd/systems-index.md` — system inventory, priorities, dependencies, and design order
- `design/gdd/<system-name>.md` — one authoritative document per substantial system
- `design/gdd/reviews/<date>-review.md` — cross-document review findings
- `design/decisions/<date>-<decision>.md` — a decision record only when alternatives and consequences matter

Draft in conversation first unless the user explicitly requests immediate file creation. Before writing, summarize what will be created or changed and preserve existing unrelated content. Use `Draft`, `In Review`, `Approved`, and `Implemented` as distinct states; only the user can approve a design.

## Scope discipline

- Define the smallest prototype that can falsify the core fun hypothesis.
- Distinguish **MVP**, **vertical slice**, **alpha**, and **full vision**.
- Prefer a short list of systems with clear ownership over a speculative framework.
- Put attractive but unvalidated features in a parking lot instead of expanding the MVP.
- For Unity implementation feasibility, consult the relevant Unity advisory skill only after the design question is clear.
- When balance depends on formulas, probability, compounding, economy flows, progression curves, or repeated random outcomes, use `game-balance-lab` to calculate or simulate the provisional design before approval.

## Completion

End each working session with:

- decisions confirmed this session;
- assumptions and hypotheses still requiring validation;
- unresolved decisions in priority order;
- the next smallest useful design or prototype step.

This skill adapts selected GDD workflow concepts from Claude Code Game Studios. Attribution and license are in [source-and-license.md](references/source-and-license.md).
