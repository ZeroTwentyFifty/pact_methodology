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
        start = "2022-01-01T00:00:00"  # missing 'Z'
        end = DateTime("2022-12-31T23:59:59Z")
        ReferencePeriod(start, end)

def test_reference_period_init_invalid_end():
    with pytest.raises(ValueError):
        start = DateTime("2022-01-01T00:00:00Z")
        end = "2022-12-31T23:59:59"  # missing 'Z'
        ReferencePeriod(start, end)