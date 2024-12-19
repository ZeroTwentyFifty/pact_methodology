import pytest
from pact_methodology.product_footprint.cpc import CPCCodeLookup, CPC


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
        ("0", "Agriculture, forestry and fishery products"),
        ("01", "Products of agriculture, horticulture and market gardening"),
        ("011", "Cereals"),
        ("0111", "Wheat"),
        ("01111", "Wheat, seed"),
        ("0112", "Maize (corn)"),
        ("43110", "Internal combustion piston engines, other than for motor vehicles and aircraft"),
        ("43132", "Turbo-jets and turbo-propellers"),
        ("97990", "Other miscellaneous services n.e.c."),
        ("98000", "Domestic services"),
    ],
)
def test_lookup_valid_cpc_code(cpc_code_lookup, cpc_code, expected_title):
    cpc = cpc_code_lookup.lookup(cpc_code)
    assert cpc is not None
    assert cpc.code == cpc_code
    assert cpc.title == expected_title


@pytest.mark.parametrize(
    "cpc_code",
    [
        "99999",  # Non-existent code
        "54321",  # Non-existent code
        "00000",  # Non-existent code (assuming leading zeros are valid)
        "12345",  # Non-existent code
    ],
)
def test_lookup_non_existent_cpc_code(cpc_code_lookup, cpc_code):
    cpc = cpc_code_lookup.lookup(cpc_code)
    assert cpc is None


@pytest.mark.parametrize(
    "cpc_code",
    [
        "",        # Empty string
        "abc",     # Non-numeric string
        "123abc",  # Mixed numeric and non-numeric
        "CPC01",   # Prefixed with non-numeric characters
        "123456",  # Exceeds maximum length
        "001234",  # Exceeds maximum length with leading zeros
        "12 34",   # Contains spaces
        "12-34",   # Contains hyphen
        "12.34",   # Contains period
    ],
)
def test_lookup_invalid_cpc_code_format(cpc_code_lookup, cpc_code):
    with pytest.raises(ValueError):
        cpc_code_lookup.lookup(cpc_code)


def test_cpc_equality():
    cpc1 = CPC("0111", "Wheat")
    cpc2 = CPC("0111", "Wheat")
    cpc3 = CPC("0112", "Maize (corn)")
    assert cpc1 == cpc2
    assert cpc1 != cpc3
    assert cpc1 != "0111"  # Should not be equal to a non-CPC object