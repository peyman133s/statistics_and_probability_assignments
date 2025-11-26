"""Unit tests for descriptive statistics helpers."""

from statprob import five_number_summary, mean, median, mode, standard_deviation, variance


def test_mean_matches_numpy_average():
    data = [2, 4, 6, 8]
    assert mean(data) == 5


def test_median_handles_even_sample():
    data = [1, 9, 5, 7]
    assert median(data) == 6


def test_mode_returns_all_modal_values():
    data = [1, 2, 2, 3, 3]
    assert set(mode(data)) == {2.0, 3.0}


def test_variance_sample_vs_population():
    data = [1, 3, 5, 7]
    assert variance(data, sample=True) == 6.666666666666667
    assert variance(data, sample=False) == 5.0


def test_standard_deviation_positive():
    data = [10, 12, 14]
    assert round(standard_deviation(data), 3) == 2.0


def test_five_number_summary_structure():
    data = [1, 2, 3, 4, 5]
    summary = five_number_summary(data)
    assert summary["min"] == 1
    assert summary["median"] == 3
    assert summary["max"] == 5
