import pytest

from pathfinder_framework.data_quality_indicators.data_quality_rating import (
    DataQualityRating,
)


@pytest.mark.parametrize("rating", [1, 2, 3])
def test_valid_data_quality_rating(rating):
    dqr = DataQualityRating(rating)
    assert dqr.rating == rating


@pytest.mark.parametrize("rating", [0, 4])
def test_invalid_data_quality_rating(rating):
    with pytest.raises(ValueError):
        DataQualityRating(rating)


@pytest.mark.parametrize("rating", ["a", 2.0, None])
def test_non_integer_data_quality_rating(rating):
    with pytest.raises(TypeError):
        DataQualityRating(rating)
