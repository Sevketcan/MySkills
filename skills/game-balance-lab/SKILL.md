---
name: game-balance-lab
description: Model, calculate, simulate, and review quantitative game balance. Use for game economies, trading markets, progression curves, RNG/drop systems, difficulty pacing, dominant strategies, Monte Carlo analysis, confidence intervals, and parameter tuning. Do not use for purely qualitative concept ideation or visual design.
---

# Game Balance Lab

Convert design intent into measurable hypotheses, then use transparent calculations or reproducible simulations to test them. Mathematical balance and player enjoyment are separate gates: pass the model first, then validate feel through playtesting.

## Select the lightest adequate method

1. **Direct calculation** — closed-form formulas are sufficient. Read [math-toolkit.md](references/math-toolkit.md).
2. **Flow/economy audit** — map resources, sources, sinks, pools, converters, feedback loops, affordability, and stall states. Read [economy-and-progression.md](references/economy-and-progression.md).
3. **Monte Carlo simulation** — randomness, interacting rules, strategies, or path dependence make closed-form analysis unreliable. Read [simulation-protocol.md](references/simulation-protocol.md) and [model-contract.md](references/model-contract.md).
4. **Parameter tuning** — a measurable target band exists and one or more tuning knobs need testing. Use the same simulation model and sweep candidate values; never tune against an undefined goal.

Do not build a simulation when a spreadsheet-sized formula answers the question. Do not use a formula that hides important state transitions or player behavior.

## Required balance brief

Before calculating or simulating, record:

- **Design question** — the uncertainty being resolved.
- **Target metric and band** — measurable success/failure criteria, chosen for this game rather than copied from another title.
- **Authoritative inputs** — GDD tables, configuration assets, code, telemetry, or explicitly labeled assumptions.
- **Tuning knobs** — adjustable values and allowed ranges.
- **Player policies** — plausible strategies or skill profiles, including at least one naive and one optimizing policy when strategy matters.
- **Scenarios** — early/mid/late game, platform/input differences, market regimes, or difficulty tiers that materially change outcomes.
- **Failure modes** — bankruptcy, soft-lock, infinite growth, dead currency, dominant strategy, excessive tail risk, or impossible milestones.

Ask for a missing value only when it materially changes the model and cannot be bounded. Otherwise model a documented range and report sensitivity.

## Evidence hierarchy

Prefer inputs in this order:

1. current game configuration or source data;
2. telemetry from representative players;
3. controlled playtest observations;
4. GDD values;
5. clearly labeled assumptions.

Never silently mix versions of a design. Record the source and units of every input. Use integer/fixed-point semantics when the game does; reproduce rounding, clamping, caps, tick order, and pity/reset behavior exactly.

## Simulation workflow

The bundled runner is dependency-free:

```bash
python3 scripts/balance_lab.py simulate \
  --model tools/balance_model.py \
  --config design/balance/config.json \
  --runs 10000 --seed 42 --format markdown
```

For a one-knob sweep:

```bash
python3 scripts/balance_lab.py sweep \
  --model tools/balance_model.py \
  --config design/balance/config.json \
  --knob market.volatility --values 0.05 0.08 0.12 \
  --runs 3000 --seed 42 --metric net_worth
```

Only execute trusted local model files; importing a model runs its Python code. Keep the game model project-specific rather than embedding guessed game rules in this skill.

## Interpretation rules

- Report distributions and tails, not only averages.
- Use seeded runs and confirm candidates with a different seed.
- Treat point estimates near a target boundary as inconclusive unless the confidence interval supports the verdict.
- Compare multiple plausible player policies; optimal-only simulation hides accessibility problems, while random-only simulation hides exploitable strategies.
- Sweep one knob at a time for attribution. After locating promising ranges, test important interactions explicitly.
- Re-run economy careers after difficulty or timing changes because completion speed changes earnings per minute.
- A simulation validates the encoded model, not the real game. Calibrate against observed gameplay before sign-off.

## Outputs

Return or save:

- balance brief and assumptions;
- formulas/model version and seed;
- strategy/scenario matrix;
- sample counts, means, standard deviations, percentiles, rates, and 95% confidence intervals;
- target-band verdicts;
- sensitivity findings and dominant strategies;
- proposed tuning changes with old/new values and expected effect;
- limitations and the next human playtest question.

When used during GDD work, write provisional formulas and target bands into the relevant system GDD, but keep generated simulation reports under `design/balance/` unless the user chooses another path. Never mark a design approved without the user's decision.

Source acknowledgements and licenses are in [source-and-license.md](references/source-and-license.md).
