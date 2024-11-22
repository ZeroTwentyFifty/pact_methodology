import pytest

from pact_methodology.carbon_footprint.reference_period import ReferencePeriod
from pact_methodology.data_quality_indicators.data_quality_indicators import (
    DataQualityIndicators,
)
from pact_methodology.data_quality_indicators.data_quality_rating import (
    DataQualityRating,
)
from pact_methodology.datetime import DateTime


@pytest.fixture
def valid_data():
    return {
        "reference_period": ReferencePeriod(
            start=DateTime("2025-01-01T00:00:00Z"), end=DateTime("2026-01-01T00:00:00Z")
        ),
        "coverage_percent": 80.0,
        "technological_dqr": DataQualityRating(2),
        "temporal_dqr": DataQualityRating(2),
        "geographical_dqr": DataQualityRating(1),
        "completeness_dqr": DataQualityRating(2),
        "reliability_dqr": DataQualityRating(3),
    }


@pytest.mark.parametrize(
    "missing_attribute",
    [
        "coverage_percent",
        "technological_dqr",
        "temporal_dqr",
        "geographical_dqr",
        "completeness_dqr",
        "reliability_dqr",
    ],
)
def test_dqi_missing_attributes_after_2025(valid_data, missing_attribute):
    del valid_data[missing_attribute]
    with pytest.raises(ValueError) as excinfo:
        DataQualityIndicators(**valid_data)
    assert (
        str(excinfo.value)
        == f"Attribute '{missing_attribute}' must be defined and not None for reporting periods including 2025 or later"
    )


def test_dqi_valid_before_2025():
    reference_period = ReferencePeriod(
        start=DateTime("2023-01-01T00:00:00Z"), end=DateTime("2024-01-01T00:00:00Z")
    )
    dqi = DataQualityIndicators(
        reference_period=reference_period, technological_dqr=DataQualityRating(2)
    )  # Other attributes are optional
    assert dqi.technological_dqr == DataQualityRating(2)


def test_dqi_valid_after_2025_all_attributes():
    reference_period = ReferencePeriod(
        start=DateTime("2025-01-01T00:00:00Z"), end=DateTime("2026-01-01T00:00:00Z")
    )
    dqi = DataQualityIndicators(
        reference_period=reference_period,
        coverage_percent=80.0,
        technological_dqr=DataQualityRating(2),
        temporal_dqr=DataQualityRating(2),
        geographical_dqr=DataQualityRating(1),
        completeness_dqr=DataQualityRating(2),
        reliability_dqr=DataQualityRating(3),
    )
    assert dqi.coverage_percent == 80.0


def test_dqi_missing_reference_period():
    with pytest.raises(TypeError):
        DataQualityIndicators()


def test_dqi_invalid_dqr_type():
    reference_period = ReferencePeriod(
        start=DateTime("2025-01-01T00:00:00Z"), end=DateTime("2026-01-01T00:00:00Z")
    )
    with pytest.raises(TypeError):
        DataQualityIndicators(
            reference_period=reference_period,
            coverage_percent=50,
            technological_dqr=2.0,
        )  # DQR should be a DataQualityRating instance


def test_coverage_percent_validation():
    reference_period = ReferencePeriod(
        start=DateTime("2023-01-01T00:00:00Z"), end=DateTime("2024-01-01T00:00:00Z")
    )
    with pytest.raises(ValueError, match="coverage_percent must be a number"):
        DataQualityIndicators(reference_period=reference_period, coverage_percent="80")


def test_reference_period_validation():
    with pytest.raises(ValueError, match="reference_period must be an instance of ReferencePeriod"):
        DataQualityIndicators(reference_period="invalid")


@pytest.mark.parametrize("dqr_field", [
    "technological_dqr",
    "temporal_dqr",
    "geographical_dqr",
    "completeness_dqr",
    "reliability_dqr"
])
def test_dqr_validation(dqr_field):
    reference_period = ReferencePeriod(
        start=DateTime("2023-01-01T00:00:00Z"), end=DateTime("2024-01-01T00:00:00Z")
    )
    with pytest.raises(TypeError, match=f"{dqr_field} must be an instance of DataQualityRating"):
        DataQualityIndicators(
            reference_period=reference_period,
            **{dqr_field: "invalid"}
        )


def test_getters(valid_data):
    """Test that all getters return the correct values"""
    dqi = DataQualityIndicators(**valid_data)
    
    assert dqi.reference_period == valid_data["reference_period"]
    assert dqi.coverage_percent == valid_data["coverage_percent"]
    assert dqi.technological_dqr == valid_data["technological_dqr"]
    assert dqi.temporal_dqr == valid_data["temporal_dqr"]
    assert dqi.geographical_dqr == valid_data["geographical_dqr"]
    assert dqi.completeness_dqr == valid_data["completeness_dqr"]
    assert dqi.reliability_dqr == valid_data["reliability_dqr"]


def test_none_values_before_2025():
    """Test that None values are accepted for all optional fields before 2025"""
    reference_period = ReferencePeriod(
        start=DateTime("2024-01-01T00:00:00Z"), end=DateTime("2024-12-31T23:59:59Z")
    )
    dqi = DataQualityIndicators(reference_period=reference_period)
    
    assert dqi.coverage_percent is None
    assert dqi.technological_dqr is None
    assert dqi.temporal_dqr is None
    assert dqi.geographical_dqr is None
    assert dqi.completeness_dqr is None
    assert dqi.reliability_dqr is None
