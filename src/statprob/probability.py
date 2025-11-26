"""Probability distribution helpers and simulations."""

from __future__ import annotations

from typing import Sequence

import numpy as np
from scipy import stats


Number = float | int


def bernoulli_pmf(p: float) -> tuple[int, float]:
    """Return the support value (1) and its probability for a Bernoulli trial."""
    if not 0 <= p <= 1:
        msg = "Probability p must lie in [0, 1]."
        raise ValueError(msg)
    return (1, p)


def binomial_pmf(k: int, n: int, p: float) -> float:
    """Return P(X = k) for a Binomial(n, p) random variable."""
    if not 0 <= k <= n:
        msg = "k must be between 0 and n inclusive."
        raise ValueError(msg)
    if not 0 <= p <= 1:
        msg = "Probability p must lie in [0, 1]."
        raise ValueError(msg)
    return float(stats.binom.pmf(k, n, p))


def normal_cdf(x: float, mu: float = 0.0, sigma: float = 1.0) -> float:
    """Return P(X <= x) for a Normal(mu, sigma) random variable."""
    if sigma <= 0:
        msg = "Sigma must be positive."
        raise ValueError(msg)
    return float(stats.norm.cdf(x, loc=mu, scale=sigma))


def simulate_bernoulli_trials(p: float, n: int, seed: int | None = None) -> np.ndarray:
    """Simulate independent Bernoulli trials and return success indicators."""
    if not 0 <= p <= 1:
        msg = "Probability p must lie in [0, 1]."
        raise ValueError(msg)
    if n <= 0:
        msg = "Number of trials must be positive."
        raise ValueError(msg)
    rng = np.random.default_rng(seed)
    return rng.binomial(1, p, size=n)


def empirical_probability(events: Sequence[bool]) -> float:
    """Estimate probability from empirical boolean outcomes."""
    arr = np.asarray(events, dtype=int)
    if arr.size == 0:
        msg = "At least one event outcome is required"
        raise ValueError(msg)
    return float(arr.mean())
