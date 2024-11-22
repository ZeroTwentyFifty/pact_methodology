import pytest

from pact_methodology.data_quality_indicators.data_quality_rating import (
    DataQualityRating,
)


@pytest.mark.parametrize("rating", [1, 2, 3])
def test_valid_data_quality_rating(rating):
    dqr = DataQualityRating(rating)
    assert dqr.rating == rating
    assert str(dqr) == str(rating)
    assert repr(dqr) == f"DataQualityRating({rating})"


@pytest.mark.parametrize("rating", [0, 4])
def test_invalid_data_quality_rating(rating):
    with pytest.raises(ValueError, match="Data quality rating must be between 1 and 3 \(inclusive\)"):
        DataQualityRating(rating)


@pytest.mark.parametrize("rating", ["a", 2.0, None])
def test_non_integer_data_quality_rating(rating):
    with pytest.raises(TypeError, match="Data quality rating must be an integer"):
        DataQualityRating(rating)


def test_data_quality_rating_equality():
    dqr1 = DataQualityRating(2)
    dqr2 = DataQualityRating(2)
    dqr3 = DataQualityRating(3)
    assert dqr1 == dqr2
    assert dqr1 != dqr3


def test_data_quality_rating_immutable():
    dqr = DataQualityRating(2)
    with pytest.raises(AttributeError, match="cannot assign to field 'rating'"):
        dqr.rating = 3
