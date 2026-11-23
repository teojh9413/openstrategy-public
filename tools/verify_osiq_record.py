#!/usr/bin/env python3
"""Verify the internally consistent fields of the public OSIQ 30 record.

This utility operates only on the aggregate public record. It does not contain
strategy-selection logic, constituent identities, or proprietary evidence.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen


LOCAL_RECORD = Path(__file__).resolve().parents[1] / "openstrategy/data/osiq-30-record.json"
LIVE_RECORD = "https://openstrategy.trade/api/index/record.json"
TOLERANCE = 1e-7


class VerificationError(ValueError):
    """Raised when a published-record invariant does not hold."""


def load_record(source: str) -> dict[str, Any]:
    if source.startswith(("https://", "http://")):
        request = Request(source, headers={"User-Agent": "OpenStrategy-public-verifier/1.0"})
        with urlopen(request, timeout=15) as response:
            payload = response.read()
    else:
        payload = Path(source).read_bytes()

    record = json.loads(payload)
    if not isinstance(record, dict):
        raise VerificationError("record root must be a JSON object")
    return record


def require_number(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise VerificationError(f"{field} must be numeric")
    result = float(value)
    if not math.isfinite(result):
        raise VerificationError(f"{field} must be finite")
    return result


def close_enough(actual: float, expected: float, field: str) -> None:
    if not math.isclose(actual, expected, rel_tol=TOLERANCE, abs_tol=TOLERANCE):
        raise VerificationError(f"{field}: calculated {actual}, published {expected}")


def verify(record: dict[str, Any]) -> dict[str, Any]:
    required = {
        "schema_version",
        "classification",
        "inception_date",
        "base_level",
        "latest_level",
        "since_inception_return_pct",
        "maximum_drawdown_pct",
        "maximum_drawdown_date",
        "observation_count",
        "history",
    }
    missing = sorted(required.difference(record))
    if missing:
        raise VerificationError(f"missing required fields: {', '.join(missing)}")

    history = record["history"]
    if not isinstance(history, list) or not history:
        raise VerificationError("history must be a non-empty array")
    if record["observation_count"] != len(history):
        raise VerificationError("observation_count does not equal history length")

    dates: list[str] = []
    levels: list[float] = []
    for index, observation in enumerate(history):
        if not isinstance(observation, dict):
            raise VerificationError(f"history[{index}] must be an object")
        date = observation.get("date")
        if not isinstance(date, str) or not date:
            raise VerificationError(f"history[{index}].date must be a string")
        if observation.get("observation_status") != "Final":
            raise VerificationError(f"history[{index}] is not Final")
        dates.append(date)
        levels.append(require_number(observation.get("index_level"), f"history[{index}].index_level"))

    if dates != sorted(dates) or len(set(dates)) != len(dates):
        raise VerificationError("history dates must be strictly increasing and unique")
    if dates[0] != record["inception_date"]:
        raise VerificationError("first history date does not match inception_date")

    base_level = require_number(record["base_level"], "base_level")
    latest_level = require_number(record["latest_level"], "latest_level")
    close_enough(levels[0], base_level, "base_level")
    close_enough(levels[-1], latest_level, "latest_level")

    calculated_return = (latest_level / base_level - 1.0) * 100.0
    published_return = require_number(record["since_inception_return_pct"], "since_inception_return_pct")
    close_enough(calculated_return, published_return, "since_inception_return_pct")

    running_peak = levels[0]
    calculated_drawdown = 0.0
    calculated_drawdown_date = dates[0]
    for date, level in zip(dates, levels):
        running_peak = max(running_peak, level)
        drawdown = (level / running_peak - 1.0) * 100.0
        if drawdown < calculated_drawdown:
            calculated_drawdown = drawdown
            calculated_drawdown_date = date

    published_drawdown = require_number(record["maximum_drawdown_pct"], "maximum_drawdown_pct")
    close_enough(calculated_drawdown, published_drawdown, "maximum_drawdown_pct")
    if calculated_drawdown_date != record["maximum_drawdown_date"]:
        raise VerificationError("maximum_drawdown_date does not match the calculated series")

    return {
        "verified": True,
        "schema_version": record["schema_version"],
        "classification": record["classification"],
        "data_date": record.get("data_date", dates[-1]),
        "observations": len(history),
        "latest_level": round(latest_level, 8),
        "since_inception_return_pct": round(calculated_return, 8),
        "maximum_drawdown_pct": round(calculated_drawdown, 8),
        "maximum_drawdown_date": calculated_drawdown_date,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "source",
        nargs="?",
        default=str(LOCAL_RECORD),
        help="path or HTTP(S) URL to a public OSIQ record",
    )
    parser.add_argument(
        "--live",
        action="store_true",
        help=f"verify the canonical live record at {LIVE_RECORD}",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = LIVE_RECORD if args.live else args.source
    try:
        summary = verify(load_record(source))
    except (OSError, json.JSONDecodeError, VerificationError) as error:
        print(f"verification failed: {error}", file=sys.stderr)
        return 1

    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
