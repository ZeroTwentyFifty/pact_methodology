from pathfinder_framework.carbon_footprint.declared_unit import DeclaredUnit


def test_declared_unit_values():
    assert DeclaredUnit.LITER == "liter"
    assert DeclaredUnit.KILOGRAM == "kilogram"
    assert DeclaredUnit.CUBIC_METER == "cubic meter"
    assert DeclaredUnit.KILOWATT_HOUR == "kilowatt hour"
    assert DeclaredUnit.MEGAJOULE == "megajoule"
    assert DeclaredUnit.TON_KILOMETER == "ton kilometer"
    assert DeclaredUnit.SQUARE_METER == "square meter"
