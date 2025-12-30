from __future__ import annotations

import argparse
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class MeanIntervalResult:
    lower: float
    upper: float
    k: float


def chebyshev_mean_interval(mean: float, std: float, confidence: float) -> MeanIntervalResult:
    if not math.isfinite(mean):
        raise ValueError("mean must be a finite number")
    if not math.isfinite(std) or std < 0:
        raise ValueError("std must be a finite, non-negative number")
    if not math.isfinite(confidence) or confidence < 0 or confidence >= 1:
        raise ValueError("confidence must be a finite number in [0, 1)")

    if std == 0:
        return MeanIntervalResult(lower=float(mean), upper=float(mean), k=0.0)

    k = 1.0 / math.sqrt(1.0 - confidence)
    lower = float(mean) - k * float(std)
    upper = float(mean) + k * float(std)
    return MeanIntervalResult(lower=lower, upper=upper, k=k)


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="mean_interval",
        description=(
            "Compute an interval around the mean using only mean/std and a confidence in [0,1). "
            "Uses Chebyshev's inequality (distribution-free)."
        ),
    )
    p.add_argument("--mean", type=float, required=True)
    p.add_argument("--std", type=float, required=True)
    p.add_argument("--confidence", type=float, required=True)
    return p


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    res = chebyshev_mean_interval(mean=args.mean, std=args.std, confidence=args.confidence)
    print(f"k={res.k:.6g}")
    print(f"interval=[{res.lower:.6g}, {res.upper:.6g}]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
