import pytest

from pathfinder_framework.carbon_footprint.carbon_footprint import CarbonFootprint
from pathfinder_framework.carbon_footprint.characterization_factors import CharacterizationFactors
from pathfinder_framework.carbon_footprint.cross_sectoral_standard import CrossSectoralStandard
from pathfinder_framework.carbon_footprint.declared_unit import DeclaredUnit
from pathfinder_framework.datetime import DateTime


def test_carbon_footprint_exists():
    assert CarbonFootprint is not None


def test_carbon_footprint_instantiation():
    carbon_footprint = CarbonFootprint(DeclaredUnit.KILOGRAM, 1.0, 0.5, 0.3, 0.2, 0.1, CharacterizationFactors.AR6, ["AR6"], [CrossSectoralStandard.GHG_PROTOCOL], "boundary processes description", 1.0, DateTime.now(), DateTime.now())
    assert isinstance(carbon_footprint, CarbonFootprint)


def test_carbon_footprint_attributes():
    carbon_footprint = CarbonFootprint(DeclaredUnit.KILOGRAM, 1.0, 0.5, 0.3, 0.2, 0.1, CharacterizationFactors.AR6, ["AR6"], [CrossSectoralStandard.GHG_PROTOCOL], "boundary processes description", 1.0, DateTime.now(), DateTime.now())
    assert carbon_footprint.declared_unit == DeclaredUnit.KILOGRAM
    assert carbon_footprint.unitary_product_amount == 1.0
    assert carbon_footprint.p_cf_excluding_biogenic == 0.5
    assert carbon_footprint.fossil_ghg_emissions == 0.3
    assert carbon_footprint.fossil_carbon_content == 0.2
    assert carbon_footprint.biogenic_carbon_content == 0.1
    assert carbon_footprint.characterization_factors == CharacterizationFactors.AR6
    assert carbon_footprint.ipcc_characterization_factors_sources == ["AR6"]
    assert carbon_footprint.cross_sectoral_standards_used == [CrossSectoralStandard.GHG_PROTOCOL]
    assert carbon_footprint.boundary_processes_description == "boundary processes description"
    assert carbon_footprint.exempted_emissions_percent == 1.0
    assert isinstance(carbon_footprint.reference_period_start, DateTime)
    assert isinstance(carbon_footprint.reference_period_end, DateTime)


def test_carbon_footprint_invalid_declared_unit():
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint("invalid unit", 1.0, 0.5, 0.3, 0.2, 0.1, CharacterizationFactors.AR6, ["AR6"], [CrossSectoralStandard.GHG_PROTOCOL], "boundary processes description", 1.0, DateTime.now(), DateTime.now())
    assert str(excinfo.value) == "declared_unit 'invalid unit' is not valid. It must be one of the following: liter, kilogram, cubic meter, kilowatt hour, megajoule, ton kilometer, square meter"


def test_carbon_footprint_invalid_unitary_product_amount():
    with pytest.raises(ValueError):
        CarbonFootprint(DeclaredUnit.KILOGRAM, 0.0, 0.5, 0.3, 0.2, 0.1, CharacterizationFactors.AR6, ["AR6"], [CrossSectoralStandard.GHG_PROTOCOL], "boundary processes description", 1.0, DateTime.now(), DateTime.now())


def test_carbon_footprint_invalid_p_cf_excluding_biogenic():
    with pytest.raises(ValueError):
        CarbonFootprint(DeclaredUnit.KILOGRAM, 1.0, -0.5, 0.3, 0.2, 0.1, CharacterizationFactors.AR6, ["AR6"], [CrossSectoralStandard.GHG_PROTOCOL], "boundary processes description", 1.0, DateTime.now(), DateTime.now())


def test_carbon_footprint_invalid_fossil_ghg_emissions():
    with pytest.raises(ValueError):
        CarbonFootprint(DeclaredUnit.KILOGRAM, 1.0, 0.5, -0.3, 0.2, 0.1, CharacterizationFactors.AR6, ["AR6"], [CrossSectoralStandard.GHG_PROTOCOL], "boundary processes description", 1.0, DateTime.now(), DateTime.now())


def test_carbon_footprint_invalid_fossil_carbon_content():
    with pytest.raises(ValueError):
        CarbonFootprint(DeclaredUnit.KILOGRAM, 1.0, 0.5, 0.3, -0.2, 0.1, CharacterizationFactors.AR6, ["AR6"], [CrossSectoralStandard.GHG_PROTOCOL], "boundary processes description", 1.0, DateTime.now(), DateTime.now())


def test_carbon_footprint_invalid_biogenic_carbon_content():
    with pytest.raises(ValueError):
        CarbonFootprint(DeclaredUnit.KILOGRAM, 1.0, 0.5, 0.3, 0.2, -0.1, CharacterizationFactors.AR6, ["AR6"], [CrossSectoralStandard.GHG_PROTOCOL], "boundary processes description", 1.0, DateTime.now(), DateTime.now())


def test_carbon_footprint_invalid_characterization_factors():
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(DeclaredUnit.KILOGRAM, 1.0, 0.5, 0.3, 0.2, 0.1, "AR7", ["AR6"], [CrossSectoralStandard.GHG_PROTOCOL], "boundary processes description", 1.0, DateTime.now(), DateTime.now())
    assert str(excinfo.value) == "characterization_factors must be an instance of CharacterizationFactors"


def test_carbon_footprint_invalid_ipcc_characterization_factors_sources():
    with pytest.raises(ValueError):
        CarbonFootprint(DeclaredUnit.KILOGRAM, 1.0, 0.5, 0.3, 0.2, 0.1, CharacterizationFactors.AR6, [], [CrossSectoralStandard.GHG_PROTOCOL], "boundary processes description", 1.0, DateTime.now(), DateTime.now())


def test_carbon_footprint_invalid_cross_sectoral_standards_used():
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(DeclaredUnit.KILOGRAM, 1.0, 0.5, 0.3, 0.2, 0.1, CharacterizationFactors.AR6, ["AR6"], ["invalid standard"], "boundary processes description", 1.0, DateTime.now(), DateTime.now())
    assert str(excinfo.value) == "cross_sectoral_standards_used must be a list of CrossSectoralStandard"


def test_carbon_footprint_invalid_boundary_processes_description():
    with pytest.raises(ValueError):
        CarbonFootprint(DeclaredUnit.KILOGRAM, 1.0, 0.5, 0.3, 0.2, 0.1, CharacterizationFactors.AR6, ["AR6"], [CrossSectoralStandard.GHG_PROTOCOL], "", 1.0, DateTime.now(), DateTime.now())


def test_carbon_footprint_invalid_exempted_emissions_percent():
    with pytest.raises(ValueError):
        CarbonFootprint(DeclaredUnit.KILOGRAM, 1.0, 0.5, 0.3, 0.2, 0.1, CharacterizationFactors.AR6, ["AR6"], [CrossSectoralStandard.GHG_PROTOCOL], "boundary processes description", 6.0, DateTime.now(), DateTime.now())


def test_carbon_footprint_invalid_reference_period_start():
    with pytest.raises(ValueError):
        CarbonFootprint(DeclaredUnit.KILOGRAM, 1.0, 0.5, 0.3, 0.2, 0.1, CharacterizationFactors.AR6, ["AR6"], [CrossSectoralStandard.GHG_PROTOCOL], "boundary processes description", 1.0, "invalid datetime", DateTime.now())


def test_carbon_footprint_invalid_reference_period_end():
    with pytest.raises(ValueError):
        CarbonFootprint(DeclaredUnit.KILOGRAM, 1.0, 0.5, 0.3, 0.2, 0.1, CharacterizationFactors.AR6, ["AR6"], [CrossSectoralStandard.GHG_PROTOCOL], "boundary processes description", 1.0, DateTime.now(), "invalid datetime")
