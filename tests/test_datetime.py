import pytest
from datetime import datetime, timedelta, timezone

from pact_methodology.datetime import DateTime


def test_valid_iso_8601_string():
    dt = DateTime("2020-03-01T00:00:00Z")
    assert dt.iso_string == "2020-03-01T00:00:00Z"


def test_valid_iso_8601_string_with_offset():
    dt = DateTime("2020-03-01T00:00:00+00:00")
    assert dt.iso_string == "2020-03-01T00:00:00Z"


def test_invalid_iso_8601_string_with_offset():
    with pytest.raises(ValueError):
        DateTime(
            "2020-03-01T00:00:00+01:00"
        )  # This is a valid ISO 8601 string, but not in the correct format


def test_invalid_iso_8601_string_without_tzinfo():
    with pytest.raises(ValueError):
        DateTime(
            "2020-03-01T00:00:00"
        )  # This is a valid ISO 8601 string, but not in the correct format


def test_invalid_iso_8601_string_different_timezone():
    with pytest.raises(ValueError):
        DateTime("2020-03-01T00:00:00-05:00")


def test_equality():
    dt1 = DateTime("2020-03-01T00:00:00Z")
    dt2 = DateTime("2020-03-01T00:00:00Z")
    assert dt1 == dt2


def test_inequality():
    dt1 = DateTime("2020-03-01T00:00:00Z")
    dt2 = DateTime("2020-03-02T00:00:00Z")
    assert dt1 != dt2


def test_repr():
    dt = DateTime("2020-03-01T00:00:00Z")
    assert repr(dt) == "DateTime('2020-03-01T00:00:00Z')"


def test_str():
    dt = DateTime("2020-03-01T00:00:00Z")
    assert str(dt) == "2020-03-01T00:00:00Z"


def test_now():
    dt = DateTime.now()
    assert dt.iso_string.endswith("Z")
    # Check that the value is within the last minute (to account for possible delays)
    assert datetime.fromisoformat(dt.iso_string.replace("Z", "+00:00")) > datetime.now(
        timezone.utc
    ) - timedelta(minutes=1)
    assert datetime.fromisoformat(dt.iso_string.replace("Z", "+00:00")) < datetime.now(
        timezone.utc
    ) + timedelta(minutes=1)


def test_now_multiple_calls():
    dt1 = DateTime.now()
    dt2 = DateTime.now()
    # Check that two consecutive calls to DateTime.now() return different values
    assert dt1 != dt2


def test_now_format():
    dt = DateTime.now()
    # Check that the value is in the correct format
    datetime.fromisoformat(dt.iso_string.replace("Z", "+00:00"))


def test_now_timezone():
    dt = DateTime.now()
    # Check that the value has the correct timezone
    assert (
        datetime.fromisoformat(dt.iso_string.replace("Z", "+00:00")).tzinfo == timezone.utc
    )


def test_year():
    dt = DateTime("2020-03-01T00:00:00Z")
    assert dt.year == 2020


def test_month():
    dt = DateTime("2020-03-01T00:00:00Z")
    assert dt.month == 3


def test_day():
    dt = DateTime("2020-03-01T00:00:00Z")
    assert dt.day == 1


def test_time():
    dt = DateTime("2020-03-01T12:34:56Z")
    assert dt.time == "12:34:56"


def test_less_than():
    dt1 = DateTime("2020-03-01T00:00:00Z")
    dt2 = DateTime("2020-03-02T00:00:00Z")
    assert dt1 < dt2


def test_less_than_or_equal():
    dt1 = DateTime("2020-03-01T00:00:00Z")
    dt2 = DateTime("2020-03-02T00:00:00Z")
    assert dt1 <= dt2
    dt3 = DateTime("2020-03-01T00:00:00Z")
    assert dt1 <= dt3


def test_greater_than():
    dt1 = DateTime("2020-03-02T00:00:00Z")
    dt2 = DateTime("2020-03-01T00:00:00Z")
    assert dt1 > dt2


def test_greater_than_or_equal():
    dt1 = DateTime("2020-03-02T00:00:00Z")
    dt2 = DateTime("2020-03-01T00:00:00Z")
    assert dt1 >= dt2
    dt3 = DateTime("2020-03-02T00:00:00Z")
    assert dt1 >= dt3


@pytest.mark.parametrize("years, expected_year", [
    (1, 2025),
    (2, 2026),
    (3, 2027),
    (0, 2024),
    (-1, 2023)
])
def test_from_years_from_now(years: int, expected_year: int):
    future_date = DateTime.create_datetime_years_from_now(years)
    future_year = future_date.year

    assert future_year == expected_year


def test_same_day_with_same_date():
    dt1 = DateTime("2023-07-31T01:00:00Z")
    dt2 = DateTime("2023-07-31T12:30:00Z")
    assert DateTime.same_day(dt1, dt2) is True

def test_same_day_with_different_date():
    dt1 = DateTime("2023-07-31T01:00:00Z")
    dt2 = DateTime("2023-08-01T12:30:00Z")
    assert DateTime.same_day(dt1, dt2) is False

def test_same_day_with_different_year():
    dt1 = DateTime("2023-07-31T01:00:00Z")
    dt2 = DateTime("2024-07-31T12:30:00Z")
    assert DateTime.same_day(dt1, dt2) is False

@pytest.mark.parametrize("dt1_str, dt2_str, expected", [
    ("2023-07-31T01:00:00Z", "2023-07-31T12:30:00Z", True),
    ("2023-07-31T01:00:00Z", "2023-08-01T12:30:00Z", False),
    ("2023-07-31T01:00:00Z", "2024-07-31T12:30:00Z", False),
])
def test_same_day_with_different_parametrizations(dt1_str, dt2_str, expected):
    dt1 = DateTime(dt1_str)
    dt2 = DateTime(dt2_str)
    assert DateTime.same_day(dt1, dt2) is expected