# Quantitative design toolkit

Choose formulas by the design question and preserve units throughout.

## Probability and random rewards

- Expected value: `E[X] = Σ p_i x_i`
- Variance: `Var(X) = Σ p_i (x_i - E[X])²`
- Standard deviation: `σ = sqrt(Var(X))`
- At least one success in `n` independent attempts: `1 - (1-p)^n`
- Median attempts for independent success probability `p`: `ceil(log(0.5) / log(1-p))`
- Expected attempts without pity: `1/p`

Do not use the independent-attempt formulas for pity systems, without-replacement draws, shared pools, streak protection, or stateful RNG. Model their exact state transitions or simulate them.

## Combat and throughput

- Raw DPS: `damage_per_hit × hits_per_second`
- Sustained DPS: `cycle_damage / (active_time + cooldown_or_reload_time)`
- Simple TTK: `ceil(effective_health / damage_per_hit) / hits_per_second`, adjusted for the first hit occurring at time zero if the game behaves that way.
- Effective health under fractional damage reduction `r`: `health / (1-r)`, valid only when mitigation is uniform and `r < 1`.
- Throughput: `completed_units / time`; include downtime and capacity constraints.

Prefer event-level simulation when accuracy, crits, armor thresholds, status effects, animation timing, targeting, or resource starvation materially change outcomes.

## Growth and progression

- Linear: `y = a + b·x`
- Polynomial: `y = a + b·x^k`
- Exponential: `y = a·r^x`
- Compound growth after `n` steps: `V_n = V_0(1+g)^n`
- Logistic: `y = L / (1 + exp(-k(x-x0)))`
- Geometric series total for `n` escalating costs: `a(r^n - 1)/(r - 1)` when `r ≠ 1`
- Time to afford: `(price - current_stock) / net_income_rate`, only when the rate is stable and nonzero.

Compare the growth order of player power, challenge, income, and costs. A small difference in exponential bases can dominate the entire late game.

## Economy flows

For a period `t`:

- Gross inflow: `F_t = Σ sources`
- Gross outflow: `S_t = Σ sinks`
- Net flow: `N_t = F_t - S_t`
- Stock update: `stock_(t+1) = clamp(stock_t + N_t, floor, cap)`
- Sink coverage: `S_t / F_t` when `F_t > 0`
- Currency velocity proxy: `transaction_value_t / average_stock_t`
- Purchase affordability percentile: fraction of modeled careers able to buy by a target time.

There is no universal healthy sink/source ratio. A growing progression economy, a session-reset economy, and a persistent multiplayer economy require different targets.

## Trading and market models

- Return: `(sell_price - buy_price - fees) / total_cost`
- Profit: `sell_proceeds - purchase_cost - holding_cost - transaction_cost`
- Maximum drawdown: largest peak-to-trough decline in a value path.
- Mean reversion step: `x_(t+1) = x_t + θ(μ-x_t)Δt + σ√Δt·ε`, with `ε ~ N(0,1)`.
- Correlated factor model: asset return = market factor + category factor + idiosyncratic shock.

Validate that information available to a simulated policy matches information available to the player. A strategy with access to hidden fair value or future regimes is not a player strategy.

## Confidence and uncertainty

- Mean standard error: `s / sqrt(n)`.
- Approximate 95% mean interval: `mean ± 1.96·SE`; disclose that this relies on a sufficiently large sample and well-behaved sampling distribution.
- For rates/proportions, prefer a Wilson interval rather than `p ± 1.96√(p(1-p)/n)`, especially near 0 or 1.
- Percentiles reveal player-tail experiences that averages hide; commonly inspect 10th, 50th, 90th, 95th, and 99th percentiles.

Run convergence checks: double the sample count and verify material conclusions remain stable. Confidence intervals quantify sampling uncertainty, not model error.
