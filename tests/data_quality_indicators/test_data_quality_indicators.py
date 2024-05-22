import pytest

from pathfinder_framework.carbon_footprint.reference_period import ReferencePeriod
from pathfinder_framework.data_quality_indicators.data_quality_indicators import DataQualityIndicators
from pathfinder_framework.datetime import DateTime


def test_valid_dqi_before_2025():
    reference_period = ReferencePeriod(start=DateTime("2023-01-01T00:00:00Z"), end=DateTime("2024-01-01T00:00:00Z"))
    dqi = DataQualityIndicators(reference_period=reference_period,
                                technological_dqr=2.0)  # Other attributes are optional
    assert dqi.technological_dqr == 2.0


def test_valid_dqi_after_2025():
    reference_period = ReferencePeriod(start=DateTime("2025-01-01T00:00:00Z"), end=DateTime("2026-01-01T00:00:00Z"))
    dqi = DataQualityIndicators(
        reference_period=reference_period, coverage_percent=80.0, technological_dqr=2.0, temporal_dqr=2.5,
        geographical_dqr=1.8, completeness_dqr=2.2, reliability_dqr=3.0)
    assert dqi.coverage_percent == 80.0


def test_missing_dqi_attributes_after_2025():
    reference_period = ReferencePeriod(start=DateTime("2025-01-01T00:00:00Z"), end=DateTime("2026-01-01T00:00:00Z"))
    with pytest.raises(ValueError):
        DataQualityIndicators(technological_dqr=2.0, reference_period=reference_period)  # Missing other attributes


def test_invalid_dqr_values():
    reference_period = ReferencePeriod(start=DateTime("2025-01-01T00:00:00Z"), end=DateTime("2026-01-01T00:00:00Z"))
    with pytest.raises(ValueError):
        DataQualityIndicators(reference_period=reference_period,
                              technological_dqr=0.5)  # DQR value must be between 1 and 3

def test_missing_reference_period():
    with pytest.raises(TypeError):
        DataQualityIndicators()
