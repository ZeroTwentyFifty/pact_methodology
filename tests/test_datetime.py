import pytest

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
    assert repr(dt) == "DateTime(2020-03-01T00:00:00Z)"
