from __future__ import annotations

from pathlib import Path
from typing import Sequence

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

Number = float | int

def generate_sample_scores(num_students: int = 40, seed: int | None = 42) -> np.ndarray:
    if num_students <= 0:
        msg = "Number of students must be positive."
        raise ValueError(msg)
    rng = np.random.default_rng(seed)
    scores = rng.normal(loc=12, scale=3.5, size=num_students)
    return np.clip(np.rint(scores), 0, 20).astype(int)


def plot_score_histogram(
    scores: Sequence[Number] | np.ndarray,
    save_path: str | Path | None = None,
) -> tuple[plt.Figure, plt.Axes]:
    arr = np.asarray(scores, dtype=float)
    if arr.size == 0:
        msg = "At least one score is required."
        raise ValueError(msg)
    if np.any((arr < 0) | (arr > 20)):
        msg = "Scores must lie between 0 and 20 inclusive."
        raise ValueError(msg)

    bins = np.arange(-0.5, 21.5, 1.0)
    fig, ax = plt.subplots(figsize=(10, 6))
    
    counts, _, patches = ax.hist(arr, bins=bins, density=True, edgecolor="black", 
                                   color="#4c78a8", alpha=0.7, label="Histogram")
    
    mu, sigma = arr.mean(), arr.std()
    skewness = stats.skew(arr)
    kurtosis = stats.kurtosis(arr)
    
    x = np.linspace(arr.min(), arr.max(), 200)
    kde = stats.gaussian_kde(arr)
    ax.plot(x, kde(x), 'r-', linewidth=2, label='Density Curve (KDE)')
    
    ax.set_xticks(np.arange(0, 21, 2))
    ax.set_xlim(-0.5, 20.5)
    ax.set_xlabel("Score (0-20)")
    ax.set_ylabel("Density")
    ax.set_title(f"Class Score Distribution (n={arr.size})\n" +
                 f"μ={mu:.2f}, σ={sigma:.2f}, Skewness={skewness:.2f}, Kurtosis={kurtosis:.2f}")
    ax.grid(axis="y", linestyle="--", alpha=0.6)
    ax.legend()
    fig.tight_layout()

    if save_path is not None:
        save_path = Path(save_path)
        fig.savefig(save_path, dpi=150)
        plt.show()
    else:
        plt.show()

    return fig, ax


if __name__ == "__main__":
    sample_scores = generate_sample_scores(num_students=40, seed=7)
    plot_score_histogram(sample_scores, save_path="scores_hist.png")
