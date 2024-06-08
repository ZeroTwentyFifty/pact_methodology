import pytest

from pathfinder_framework.product_footprint.cpc import CPCCodeLookup, CPC


@pytest.fixture
def cpc_code_lookup():
    return CPCCodeLookup()


def test_cpc_class():
    cpc = CPC("0111", "Wheat")
    assert cpc.code == "0111"
    assert cpc.title == "Wheat"
    assert cpc.section == "0"
    assert cpc.division == "01"
    assert cpc.group == "011"
    assert cpc.class_ == "0111"
    assert cpc.subclass == "0111"


@pytest.mark.parametrize(
    "cpc_code, expected_title",
    [
        ("1202", "Natural gas, liquefied or in the gaseous state"),
        ("1410", "Iron ores and concentrates, other than roasted iron pyrites"),
        ("43310", "Ball or roller bearings"),
        ("97120", "Dry-cleaning services (including fur product cleaning services)"),
    ],
)
def test_lookup_valid_cpc_code(cpc_code_lookup, cpc_code, expected_title):
    cpc = cpc_code_lookup.lookup(cpc_code)
    assert cpc.code == cpc_code
    assert cpc.title == expected_title


def test_lookup_cpc_code(cpc_code_lookup):
    cpc = cpc_code_lookup.lookup("0")
    assert cpc.code == "0"
    assert cpc.title == "Agriculture, forestry and fishery products"
    assert cpc.section == "0"
    assert cpc.division == "0"
    assert cpc.group == "0"
    assert cpc.class_ == "0"
    assert cpc.subclass == "0"


@pytest.mark.parametrize(
    "cpc_code",
    [
        "99999",  # invalid code
    ],
)
def test_lookup_invalid_cpc_code(cpc_code_lookup, cpc_code):
    cpc = cpc_code_lookup.lookup(cpc_code)
    assert cpc is None


def test_lookup_cpc_code_with_leading_zeros(cpc_code_lookup):
    cpc = cpc_code_lookup.lookup("0112")
    assert cpc.code == "0112"
    assert cpc.title == "Maize (corn)"
    assert cpc.section == "0"
    assert cpc.division == "01"
    assert cpc.group == "011"
    assert cpc.class_ == "0112"
    assert cpc.subclass == "0112"


@pytest.mark.parametrize(
    "cpc_code",
    [
        "",
        "abcde",
        "123abc",
        "123456",  # code too long
        "abcde",  # non-numeric code
    ],
)
def test_lookup_invalid_cpc_code_format(cpc_code_lookup, cpc_code):
    with pytest.raises(ValueError):
        cpc_code_lookup.lookup(cpc_code)
