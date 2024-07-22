from datetime import datetime, timedelta

import pytest

from pathfinder_framework.datetime import DateTime
from pathfinder_framework.product_footprint.validity_period import ValidityPeriod


def test_validity_period_init():
    start = DateTime("2022-01-01T00:00:00Z")
    end = DateTime("2025-12-31T23:59:59Z")
    validity_period = ValidityPeriod(start=start, end=end)
    assert validity_period.start == start
    assert validity_period.end == end


def test_validity_period_is_valid_true():
    start = DateTime("2023-01-01T00:00:00Z")
    end = DateTime("2025-12-31T23:59:59Z")
    validity_period = ValidityPeriod(start=start, end=end)
    ref_period_end = DateTime("2022-12-31T23:59:59Z")
    assert validity_period.is_valid(ref_period_end) == True


def test_validity_period_is_valid_false_start_before_ref_period_end():
    start = DateTime("2021-12-31T23:59:59Z")
    end = DateTime("2025-12-31T23:59:59Z")
    validity_period = ValidityPeriod(start=start, end=end)
    ref_period_end = DateTime("2022-12-31T23:59:59Z")
    assert validity_period.is_valid(ref_period_end) == False


def test_validity_period_is_valid_false_end_after_ref_period_end_plus_three_years():
    start = DateTime("2022-01-01T00:00:00Z")
    end = DateTime("2026-01-01T00:00:00Z")  # more than 3 years after ref period end
    validity_period = ValidityPeriod(start=start, end=end)
    ref_period_end = DateTime("2022-12-31T23:59:59Z")
    assert validity_period.is_valid(ref_period_end) == False


def test_validity_period_init_raises_value_error_for_invalid_start_date():
    start = "2022-01-01T00:00:00Z"  # not a DateTime object
    end = DateTime("2025-12-31T23:59:59Z")
    with pytest.raises(ValueError, match="Start date must be a DateTime object"):
        validity_period = ValidityPeriod(start=start, end=end)


def test_validity_period_init_raises_value_error_for_invalid_end_date():
    start = DateTime("2022-01-01T00:00:00Z")
    end = "2025-12-31T23:59:59Z"  # not a DateTime object
    with pytest.raises(ValueError, match="End date must be a DateTime object"):
        validity_period = ValidityPeriod(start=start, end=end)


def test_validity_period_init_raises_value_error_for_start_date_not_before_end_date():
    start = DateTime("2025-01-01T00:00:00Z")
    end = DateTime("2022-12-31T23:59:59Z")
    with pytest.raises(ValueError, match="Start date must be before end date"):
        validity_period = ValidityPeriod(start=start, end=end)


def test_validity_period_default_dates():
    ref_period_end = DateTime("2022-12-31T23:59:59Z")
    validity_period = ValidityPeriod(reference_period_end=ref_period_end)
    expected_start = ref_period_end
    expected_end = DateTime((datetime.fromisoformat(ref_period_end.value.replace("Z", "+00:00")) + timedelta(days=3 * 366)).isoformat())
    assert validity_period.start == expected_start
    assert validity_period.end == expected_end


def test_validity_period_no_reference_date():
    with pytest.raises(ValueError, match="Reference period end date must be provided when start or end dates are not specified."):
        ValidityPeriod()
