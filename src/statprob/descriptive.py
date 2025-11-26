"""Descriptive statistics helpers used across assignment solutions."""

from __future__ import annotations

from typing import Iterable, List, Sequence

import numpy as np


Number = float | int


def _to_array(values: Sequence[Number] | np.ndarray) -> np.ndarray:
    """Convert sequences to a 1-D NumPy array of floats."""
    arr = np.asarray(values, dtype=float)
    if arr.ndim != 1:
        msg = "Input must be a 1-D sequence of numeric values"
        raise ValueError(msg)
    return arr


def mean(values: Sequence[Number] | np.ndarray) -> float:
    """Return the arithmetic mean."""
    arr = _to_array(values)
    return float(np.mean(arr))


def median(values: Sequence[Number] | np.ndarray) -> float:
    """Return the median of the values."""
    arr = _to_array(values)
    return float(np.median(arr))


def mode(values: Sequence[Number] | np.ndarray) -> List[float]:
    """Return all modal values sorted ascending."""
    arr = _to_array(values)
    uniques, counts = np.unique(arr, return_counts=True)
    max_count = counts.max()
    return [float(v) for v in uniques[counts == max_count]]


def variance(values: Sequence[Number] | np.ndarray, sample: bool = True) -> float:
    """Return the (sample) variance. Set sample=False for population variance."""
    arr = _to_array(values)
    ddof = 1 if sample else 0
    if arr.size - ddof <= 0:
        msg = "Variance requires at least two data points for sample mode"
        raise ValueError(msg)
    return float(np.var(arr, ddof=ddof))


def standard_deviation(values: Sequence[Number] | np.ndarray, sample: bool = True) -> float:
    """Return the (sample) standard deviation."""
    return float(np.sqrt(variance(values, sample=sample)))


def five_number_summary(values: Sequence[Number] | np.ndarray) -> dict[str, float]:
    """Return min, Q1, median, Q3, max as a dictionary for quick reporting."""
    arr = _to_array(values)
    q1, median_value, q3 = np.percentile(arr, [25, 50, 75])
    return {
        "min": float(np.min(arr)),
        "q1": float(q1),
        "median": float(median_value),
        "q3": float(q3),
        "max": float(np.max(arr)),
    }
