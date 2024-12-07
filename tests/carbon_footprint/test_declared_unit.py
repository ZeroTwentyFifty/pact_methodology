from pact_methodology.carbon_footprint.declared_unit import DeclaredUnit


def test_declared_unit_values():
    assert DeclaredUnit.LITER == "liter"
    assert DeclaredUnit.KILOGRAM == "kilogram"
    assert DeclaredUnit.CUBIC_METER == "cubic meter"
    assert DeclaredUnit.KILOWATT_HOUR == "kilowatt hour"
    assert DeclaredUnit.MEGAJOULE == "megajoule"
    assert DeclaredUnit.TON_KILOMETER == "ton kilometer"
    assert DeclaredUnit.SQUARE_METER == "square meter"

def test_declared_unit_str():
    assert str(DeclaredUnit.LITER) == "liter"
    assert str(DeclaredUnit.KILOGRAM) == "kilogram"
    assert str(DeclaredUnit.CUBIC_METER) == "cubic meter"
    assert str(DeclaredUnit.KILOWATT_HOUR) == "kilowatt hour"
    assert str(DeclaredUnit.MEGAJOULE) == "megajoule"
    assert str(DeclaredUnit.TON_KILOMETER) == "ton kilometer"
    assert str(DeclaredUnit.SQUARE_METER) == "square meter"

def test_declared_unit_repr():
    assert repr(DeclaredUnit.LITER) == "DeclaredUnit.LITER"
    assert repr(DeclaredUnit.KILOGRAM) == "DeclaredUnit.KILOGRAM"
    assert repr(DeclaredUnit.CUBIC_METER) == "DeclaredUnit.CUBIC_METER"
    assert repr(DeclaredUnit.KILOWATT_HOUR) == "DeclaredUnit.KILOWATT_HOUR"
    assert repr(DeclaredUnit.MEGAJOULE) == "DeclaredUnit.MEGAJOULE"
    assert repr(DeclaredUnit.TON_KILOMETER) == "DeclaredUnit.TON_KILOMETER"
    assert repr(DeclaredUnit.SQUARE_METER) == "DeclaredUnit.SQUARE_METER"
