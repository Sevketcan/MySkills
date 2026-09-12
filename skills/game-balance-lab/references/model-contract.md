# Balance model contract

The bundled runner imports a trusted project-specific Python module. The model must expose:

```python
def strategies(config):
    return ["naive", "conservative", "aggressive"]

def simulate(config, strategy, rng):
    return {
        "success": True,
        "duration_ticks": 120,
        "net_worth": 15340.0,
        "max_drawdown": 0.18,
    }
```

`config` is loaded from JSON and deep-copied for every run. `rng` is a seeded `random.Random` instance unique to that run. The result must be a flat mapping containing booleans or finite numbers. String fields are ignored by statistical summaries.

Optional hook:

```python
def validate_config(config):
    # Raise ValueError for invalid or impossible configuration.
    return None
```

## Commands

```bash
python3 balance_lab.py simulate --model MODEL.py --config CONFIG.json \
  --runs 10000 --seed 42 --format json --save report.json

python3 balance_lab.py sweep --model MODEL.py --config CONFIG.json \
  --knob progression.cost_growth --values 1.08 1.12 1.16 \
  --metric completion_ticks --runs 3000 --seed 42 --format markdown
```

Sweep values are parsed as JSON literals when possible, so numbers, booleans, quoted strings, arrays, and objects are supported. A dotted knob path addresses nested objects.

## Modeling rules

- Do not read or modify live game state from `simulate`.
- Keep runs independent; no mutable module-global state.
- Use only the supplied RNG for stochastic decisions.
- Return a metric with the same type and meaning in every run.
- Do not expose hidden state to a policy unless the actual player sees it.
- Keep formulas close to their GDD/source reference and document deliberate abstractions.
