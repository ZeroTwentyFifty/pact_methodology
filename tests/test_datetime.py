import pytest
from datetime import datetime, timedelta, timezone

from pathfinder_framework.datetime import DateTime


def test_valid_iso_8601_string():
    dt = DateTime("2020-03-01T00:00:00Z")
    assert dt.value == "2020-03-01T00:00:00Z"


def test_valid_iso_8601_string_with_offset():
    dt = DateTime("2020-03-01T00:00:00+00:00")
    assert dt.value == "2020-03-01T00:00:00Z"


def test_invalid_iso_8601_string_with_offset():
    with pytest.raises(ValueError):
        DateTime("2020-03-01T00:00:00+01:00")  # This is a valid ISO 8601 string, but not in the correct format


def test_invalid_iso_8601_string_without_tzinfo():
    with pytest.raises(ValueError):
        DateTime("2020-03-01T00:00:00")  # This is a valid ISO 8601 string, but not in the correct format


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
    assert dt.value.endswith('Z')
    # Check that the value is within the last minute (to account for possible delays)
    assert datetime.fromisoformat(dt.value.replace('Z', '+00:00')) > datetime.now(timezone.utc) - timedelta(minutes=1)
    assert datetime.fromisoformat(dt.value.replace('Z', '+00:00')) < datetime.now(timezone.utc) + timedelta(minutes=1)


def test_now_multiple_calls():
    dt1 = DateTime.now()
    dt2 = DateTime.now()
    # Check that two consecutive calls to DateTime.now() return different values
    assert dt1 != dt2


def test_now_format():
    dt = DateTime.now()
    # Check that the value is in the correct format
    datetime.fromisoformat(dt.value.replace('Z', '+00:00'))


def test_now_timezone():
    dt = DateTime.now()
    # Check that the value has the correct timezone
    assert datetime.fromisoformat(dt.value.replace('Z', '+00:00')).tzinfo == timezone.utc


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
