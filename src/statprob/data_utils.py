"""Data loading and preprocessing helpers."""

from __future__ import annotations

from pathlib import Path
from typing import Sequence

import numpy as np
import pandas as pd


def load_csv_numeric(path: str | Path, columns: Sequence[str] | None = None) -> pd.DataFrame:
    """Load a CSV file and keep only the requested numeric columns."""
    df = pd.read_csv(path)
    if columns:
        missing = set(columns) - set(df.columns)
        if missing:
            msg = f"Missing columns in file: {missing}"
            raise ValueError(msg)
        df = df[list(columns)]
    numeric_df = df.select_dtypes(include=["number"]).copy()
    if numeric_df.empty:
        msg = "No numeric columns found in provided CSV"
        raise ValueError(msg)
    return numeric_df


def z_score_normalize(values: Sequence[float] | np.ndarray) -> np.ndarray:
    """Public wrapper for z-score normalization supporting plain sequences."""
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        msg = "At least one value is required"
        raise ValueError(msg)
    mean_val = arr.mean()
    std_val = arr.std(ddof=0)
    if std_val == 0:
        msg = "Standard deviation is zero; cannot normalize"
        raise ValueError(msg)
    return (arr - mean_val) / std_val
