"""Unit tests for probability utilities."""

import numpy as np

from statprob import binomial_pmf, normal_cdf, simulate_bernoulli_trials


def test_binomial_pmf_matches_known_value():
    assert round(binomial_pmf(2, 4, 0.5), 3) == 0.375


def test_normal_cdf_standard_normal():
    assert round(normal_cdf(0.0), 3) == 0.5


def test_simulate_bernoulli_trials_shape_and_seed():
    trials = simulate_bernoulli_trials(p=0.3, n=5, seed=42)
    expected = np.array([1, 0, 1, 0, 0])
    assert np.array_equal(trials, expected)
