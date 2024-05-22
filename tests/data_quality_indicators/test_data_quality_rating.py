import pytest

from pathfinder_framework.data_quality_indicators.data_quality_rating import DataQualityRating


def test_valid_data_quality_rating():
    dqr = DataQualityRating(2.0)
    assert dqr.rating == 2.0


def test_invalid_data_quality_rating():
    with pytest.raises(ValueError):
        DataQualityRating(0.5)  # Value outside the valid range


def test_valid_data_quality_rating_extremes():
    dqr_min = DataQualityRating(1.0)
    assert dqr_min.rating == 1.0

    dqr_max = DataQualityRating(3.0)
    assert dqr_max.rating == 3.0