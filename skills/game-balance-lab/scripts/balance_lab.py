#!/usr/bin/env python3
"""Reproducible Monte Carlo runner for project-specific game balance models.

The runner uses only the Python standard library. It imports a trusted local
model module; see references/model-contract.md for the required functions.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import math
import random
import statistics
import sys
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping


VERSION = "1.0.0"
Z_95 = 1.959963984540054


class BalanceLabError(Exception):
    """Raised for invalid models, inputs, or simulation outputs."""


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise BalanceLabError(f"Cannot load config {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise BalanceLabError("The configuration root must be a JSON object")
    return value


def config_hash(config: Mapping[str, Any]) -> str:
    payload = json.dumps(config, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def load_model(path: Path) -> Any:
    if not path.is_file():
        raise BalanceLabError(f"Model file not found: {path}")
    module_name = "balance_model_" + hashlib.sha256(str(path.resolve()).encode()).hexdigest()[:12]
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise BalanceLabError(f"Cannot import model: {path}")
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as exc:
        raise BalanceLabError(f"Model import failed: {exc}") from exc
    if not callable(getattr(module, "simulate", None)):
        raise BalanceLabError("Model must define simulate(config, strategy, rng)")
    if not callable(getattr(module, "strategies", None)):
        raise BalanceLabError("Model must define strategies(config)")
    return module


def validate_config(module: Any, config: dict[str, Any]) -> None:
    validator = getattr(module, "validate_config", None)
    if callable(validator):
        try:
            validator(copy.deepcopy(config))
        except Exception as exc:
            raise BalanceLabError(f"Model rejected the configuration: {exc}") from exc


def resolve_strategies(module: Any, config: dict[str, Any], requested: str | None) -> list[str]:
    if requested:
        values = [item.strip() for item in requested.split(",") if item.strip()]
    else:
        try:
            values = list(module.strategies(copy.deepcopy(config)))
        except Exception as exc:
            raise BalanceLabError(f"strategies(config) failed: {exc}") from exc
    if not values or any(not isinstance(item, str) or not item for item in values):
        raise BalanceLabError("At least one non-empty strategy name is required")
    if len(values) != len(set(values)):
        raise BalanceLabError("Strategy names must be unique")
    return values


def stable_run_seed(base_seed: int, strategy: str, run_index: int) -> int:
    payload = f"{base_seed}|{strategy}|{run_index}".encode("utf-8")
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "big")


def validate_record(record: Any, strategy: str, run_index: int) -> dict[str, bool | float]:
    if not isinstance(record, Mapping):
        raise BalanceLabError(
            f"simulate returned {type(record).__name__} for {strategy} run {run_index}; expected a mapping"
        )
    normalized: dict[str, bool | float] = {}
    for key, value in record.items():
        if not isinstance(key, str) or not key:
            raise BalanceLabError(f"Metric keys must be non-empty strings ({strategy} run {run_index})")
        if isinstance(value, bool):
            normalized[key] = value
        elif isinstance(value, (int, float)):
            number = float(value)
            if not math.isfinite(number):
                raise BalanceLabError(f"Metric {key!r} is not finite ({strategy} run {run_index})")
            normalized[key] = number
    if not normalized:
        raise BalanceLabError(f"No boolean or numeric metrics returned for {strategy} run {run_index}")
    return normalized


def percentile(sorted_values: list[float], probability: float) -> float:
    if not sorted_values:
        raise BalanceLabError("Cannot calculate a percentile from an empty sample")
    position = (len(sorted_values) - 1) * probability
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return sorted_values[lower]
    fraction = position - lower
    return sorted_values[lower] * (1 - fraction) + sorted_values[upper] * fraction


def wilson_interval(successes: int, count: int) -> tuple[float, float]:
    if count <= 0:
        return (0.0, 0.0)
    rate = successes / count
    denominator = 1 + Z_95**2 / count
    center = (rate + Z_95**2 / (2 * count)) / denominator
    margin = (
        Z_95
        * math.sqrt(rate * (1 - rate) / count + Z_95**2 / (4 * count**2))
        / denominator
    )
    return (max(0.0, center - margin), min(1.0, center + margin))


def summarize_metric(values: list[bool | float]) -> dict[str, Any]:
    if all(isinstance(value, bool) for value in values):
        successes = sum(bool(value) for value in values)
        low, high = wilson_interval(successes, len(values))
        return {
            "type": "rate",
            "count": len(values),
            "successes": successes,
            "rate": successes / len(values),
            "ci95_wilson": [low, high],
        }
    if any(isinstance(value, bool) for value in values):
        raise BalanceLabError("A metric cannot mix boolean and numeric values")
    numbers = sorted(float(value) for value in values)
    mean = statistics.fmean(numbers)
    stdev = statistics.stdev(numbers) if len(numbers) > 1 else 0.0
    margin = Z_95 * stdev / math.sqrt(len(numbers)) if len(numbers) > 1 else 0.0
    return {
        "type": "numeric",
        "count": len(numbers),
        "mean": mean,
        "stdev": stdev,
        "ci95_mean_approx": [mean - margin, mean + margin],
        "min": numbers[0],
        "p10": percentile(numbers, 0.10),
        "p25": percentile(numbers, 0.25),
        "p50": percentile(numbers, 0.50),
        "p75": percentile(numbers, 0.75),
        "p90": percentile(numbers, 0.90),
        "p95": percentile(numbers, 0.95),
        "p99": percentile(numbers, 0.99),
        "max": numbers[-1],
    }


def summarize_records(records: list[dict[str, bool | float]]) -> dict[str, Any]:
    metric_names = sorted({key for record in records for key in record})
    metrics: dict[str, Any] = {}
    for name in metric_names:
        values = [record[name] for record in records if name in record]
        summary = summarize_metric(values)
        summary["missing"] = len(records) - len(values)
        metrics[name] = summary
    return {"runs": len(records), "metrics": metrics}


def run_experiment(
    module: Any,
    config: dict[str, Any],
    strategy_names: Iterable[str],
    runs: int,
    seed: int,
) -> dict[str, Any]:
    if runs <= 0:
        raise BalanceLabError("--runs must be greater than zero")
    validate_config(module, config)
    summaries: dict[str, Any] = {}
    simulator: Callable[[dict[str, Any], str, random.Random], Any] = module.simulate
    for strategy in strategy_names:
        records: list[dict[str, bool | float]] = []
        for run_index in range(runs):
            rng = random.Random(stable_run_seed(seed, strategy, run_index))
            try:
                raw_record = simulator(copy.deepcopy(config), strategy, rng)
            except Exception as exc:
                raise BalanceLabError(
                    f"simulate failed for strategy={strategy!r}, run={run_index}, seed={stable_run_seed(seed, strategy, run_index)}: {exc}"
                ) from exc
            records.append(validate_record(raw_record, strategy, run_index))
        summaries[strategy] = summarize_records(records)
    return summaries


def parse_sweep_value(raw: str) -> Any:
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return raw


def set_dotted(config: dict[str, Any], dotted_key: str, value: Any) -> None:
    parts = dotted_key.split(".")
    if not all(parts):
        raise BalanceLabError("--knob must be a non-empty dotted path")
    cursor: dict[str, Any] = config
    for part in parts[:-1]:
        child = cursor.get(part)
        if not isinstance(child, dict):
            raise BalanceLabError(f"Knob path does not resolve to an object at {part!r}")
        cursor = child
    if parts[-1] not in cursor:
        raise BalanceLabError(f"Knob does not exist in config: {dotted_key}")
    cursor[parts[-1]] = value


def metric_estimate(metric: Mapping[str, Any]) -> tuple[float, float, float]:
    if metric["type"] == "rate":
        return (metric["rate"], metric["ci95_wilson"][0], metric["ci95_wilson"][1])
    return (
        metric["mean"],
        metric["ci95_mean_approx"][0],
        metric["ci95_mean_approx"][1],
    )


def simulate_command(args: argparse.Namespace) -> dict[str, Any]:
    model_path = Path(args.model).resolve()
    config_path = Path(args.config).resolve()
    config = load_json(config_path)
    module = load_model(model_path)
    strategies = resolve_strategies(module, config, args.strategies)
    summaries = run_experiment(module, config, strategies, args.runs, args.seed)
    return {
        "schema_version": 1,
        "command": "simulate",
        "model": str(model_path),
        "config": str(config_path),
        "config_sha256": config_hash(config),
        "runs_per_strategy": args.runs,
        "seed": args.seed,
        "strategies": summaries,
    }


def sweep_command(args: argparse.Namespace) -> dict[str, Any]:
    model_path = Path(args.model).resolve()
    config_path = Path(args.config).resolve()
    base_config = load_json(config_path)
    module = load_model(model_path)
    strategy_names = resolve_strategies(module, base_config, args.strategies)
    rows: list[dict[str, Any]] = []
    for raw_value in args.values:
        parsed_value = parse_sweep_value(raw_value)
        candidate = copy.deepcopy(base_config)
        set_dotted(candidate, args.knob, parsed_value)
        summaries = run_experiment(module, candidate, strategy_names, args.runs, args.seed)
        for strategy, strategy_summary in summaries.items():
            metric = strategy_summary["metrics"].get(args.metric)
            if metric is None:
                raise BalanceLabError(
                    f"Metric {args.metric!r} was not returned by strategy {strategy!r}"
                )
            estimate, low, high = metric_estimate(metric)
            row = {
                "value": parsed_value,
                "strategy": strategy,
                "metric_type": metric["type"],
                "estimate": estimate,
                "ci95_low": low,
                "ci95_high": high,
            }
            if metric["type"] == "numeric":
                row.update({"p10": metric["p10"], "p50": metric["p50"], "p90": metric["p90"]})
            rows.append(row)
    return {
        "schema_version": 1,
        "command": "sweep",
        "model": str(model_path),
        "config": str(config_path),
        "base_config_sha256": config_hash(base_config),
        "knob": args.knob,
        "metric": args.metric,
        "runs_per_strategy": args.runs,
        "seed": args.seed,
        "rows": rows,
    }


def format_number(value: Any) -> str:
    if isinstance(value, float):
        return f"{value:.6g}"
    return str(value)


def markdown_report(report: Mapping[str, Any]) -> str:
    lines: list[str] = ["# Balance Lab Report", ""]
    lines.append(f"- Command: `{report['command']}`")
    lines.append(f"- Model: `{report['model']}`")
    lines.append(f"- Config: `{report['config']}`")
    lines.append(f"- Runs per strategy: {report['runs_per_strategy']}")
    lines.append(f"- Seed: {report['seed']}")
    lines.append("")
    if report["command"] == "simulate":
        for strategy, summary in report["strategies"].items():
            lines.extend([f"## Strategy: {strategy}", "", "| Metric | Estimate | 95% CI | P10 | P50 | P90 |", "|---|---:|---:|---:|---:|---:|"])
            for name, metric in summary["metrics"].items():
                if metric["type"] == "rate":
                    estimate = metric["rate"]
                    low, high = metric["ci95_wilson"]
                    p10 = p50 = p90 = "—"
                else:
                    estimate = metric["mean"]
                    low, high = metric["ci95_mean_approx"]
                    p10, p50, p90 = (format_number(metric[key]) for key in ("p10", "p50", "p90"))
                lines.append(
                    f"| {name} | {format_number(estimate)} | {format_number(low)}–{format_number(high)} | {p10} | {p50} | {p90} |"
                )
            lines.append("")
    else:
        lines.extend([
            f"- Knob: `{report['knob']}`",
            f"- Metric: `{report['metric']}`",
            "",
            "| Value | Strategy | Estimate | 95% CI | P10 | P50 | P90 |",
            "|---|---|---:|---:|---:|---:|---:|",
        ])
        for row in report["rows"]:
            lines.append(
                "| {} | {} | {} | {}–{} | {} | {} | {} |".format(
                    json.dumps(row["value"], ensure_ascii=False),
                    row["strategy"],
                    format_number(row["estimate"]),
                    format_number(row["ci95_low"]),
                    format_number(row["ci95_high"]),
                    format_number(row.get("p10", "—")),
                    format_number(row.get("p50", "—")),
                    format_number(row.get("p90", "—")),
                )
            )
        lines.append("")
    lines.extend([
        "> Confidence intervals quantify sampling uncertainty, not errors in the model or its assumptions.",
        "",
    ])
    return "\n".join(lines)


def add_common_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--model", required=True, help="Trusted Python model file")
    parser.add_argument("--config", required=True, help="JSON model configuration")
    parser.add_argument("--runs", type=int, default=1000, help="Runs per strategy (default: 1000)")
    parser.add_argument("--seed", type=int, default=42, help="Base RNG seed (default: 42)")
    parser.add_argument("--strategies", help="Comma-separated strategy names; defaults to model.strategies")
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    parser.add_argument("--save", help="Optional output file; stdout is always written")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", action="version", version=VERSION)
    subparsers = parser.add_subparsers(dest="command", required=True)

    simulate_parser = subparsers.add_parser("simulate", help="Run and summarize each strategy")
    add_common_arguments(simulate_parser)
    simulate_parser.set_defaults(handler=simulate_command)

    sweep_parser = subparsers.add_parser("sweep", help="Sweep one nested configuration value")
    add_common_arguments(sweep_parser)
    sweep_parser.add_argument("--knob", required=True, help="Dotted JSON path to an existing value")
    sweep_parser.add_argument("--values", nargs="+", required=True, help="Candidate JSON values")
    sweep_parser.add_argument("--metric", required=True, help="Returned metric to compare")
    sweep_parser.set_defaults(handler=sweep_command)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        report = args.handler(args)
        rendered = (
            json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
            if args.format == "json"
            else markdown_report(report)
        )
        sys.stdout.write(rendered)
        if args.save:
            Path(args.save).write_text(rendered, encoding="utf-8")
        return 0
    except BalanceLabError as exc:
        print(f"balance-lab error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
