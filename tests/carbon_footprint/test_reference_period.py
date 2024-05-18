import pytest

from pathfinder_framework.carbon_footprint.reference_period import ReferencePeriod
from pathfinder_framework.datetime import DateTime


def test_reference_period_init():
    start = DateTime("2022-01-01T00:00:00Z")
    end = DateTime("2022-12-31T23:59:59Z")
    ref_period = ReferencePeriod(start, end)
    assert ref_period.start == start
    assert ref_period.end == end


def test_reference_period_init_invalid_start():
    with pytest.raises(ValueError):
        start = "2022-01-01T00:00:00"
        end = DateTime("2022-12-31T23:59:59Z")
        ReferencePeriod(start, end)


def test_reference_period_init_invalid_end():
    with pytest.raises(ValueError):
        start = DateTime("2022-01-01T00:00:00Z")
        end = "2022-12-31T23:59:59"
        ReferencePeriod(start, end)


def test_reference_period_end_before_start():
    with pytest.raises(ValueError, match="Start date must be before end date"):
        start = DateTime("2022-01-01T00:00:00Z")
        end = DateTime("2021-01-01T00:00:00Z")
        ReferencePeriod(start, end)


def test_reference_period_includes_2025_or_later():
    start = DateTime("2024-01-01T00:00:00Z")
    end = DateTime("2026-12-31T23:59:59Z")
    ref_period = ReferencePeriod(start, end)
    assert ref_period.includes_2025_or_later()


def test_reference_period_does_not_include_2025_or_later():
    start = DateTime("2022-01-01T00:00:00Z")
    end = DateTime("2023-12-31T23:59:59Z")
    ref_period = ReferencePeriod(start, end)
    assert not ref_period.includes_2025_or_later()
