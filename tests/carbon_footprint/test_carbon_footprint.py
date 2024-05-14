import pytest

from pathfinder_framework.carbon_footprint.carbon_footprint import CarbonFootprint
from pathfinder_framework.carbon_footprint.characterization_factors import CharacterizationFactors


def test_carbon_footprint_exists():
    assert CarbonFootprint is not None


def test_carbon_footprint_instantiation():
    carbon_footprint = CarbonFootprint("kilogram", 1.0, 0.5, 0.3, 0.2, 0.1, CharacterizationFactors.AR6, ["AR6"], ["Standard"], "boundary processes description", 1.0)
    assert isinstance(carbon_footprint, CarbonFootprint)


def test_carbon_footprint_attributes():
    carbon_footprint = CarbonFootprint("kilogram", 1.0, 0.5, 0.3, 0.2, 0.1, CharacterizationFactors.AR6, ["AR6"], ["Standard"], "boundary processes description", 1.0)
    assert carbon_footprint.declared_unit == "kilogram"
    assert carbon_footprint.unitary_product_amount == 1.0
    assert carbon_footprint.p_cf_excluding_biogenic == 0.5
    assert carbon_footprint.fossil_ghg_emissions == 0.3
    assert carbon_footprint.fossil_carbon_content == 0.2
    assert carbon_footprint.biogenic_carbon_content == 0.1
    assert carbon_footprint.characterization_factors == CharacterizationFactors.AR6
    assert carbon_footprint.ipcc_characterization_factors_sources == ["AR6"]
    assert carbon_footprint.cross_sectoral_standards_used == ["Standard"]
    assert carbon_footprint.boundary_processes_description == "boundary processes description"
    assert carbon_footprint.exempted_emissions_percent == 1.0


def test_carbon_footprint_invalid_declared_unit():
    with pytest.raises(ValueError):
        CarbonFootprint("", 1.0, 0.5, 0.3, 0.2, 0.1, CharacterizationFactors.AR6, ["AR6"], ["Standard"], "boundary processes description", 1.0)


def test_carbon_footprint_invalid_unitary_product_amount():
    with pytest.raises(ValueError):
        CarbonFootprint("kilogram", 0.0, 0.5, 0.3, 0.2, 0.1, CharacterizationFactors.AR6, ["AR6"], ["Standard"], "boundary processes description", 1.0)


def test_carbon_footprint_invalid_p_cf_excluding_biogenic():
    with pytest.raises(ValueError):
        CarbonFootprint("kilogram", 1.0, -0.5, 0.3, 0.2, 0.1, CharacterizationFactors.AR6, ["AR6"], ["Standard"], "boundary processes description", 1.0)


def test_carbon_footprint_invalid_fossil_ghg_emissions():
    with pytest.raises(ValueError):
        CarbonFootprint("kilogram", 1.0, 0.5, -0.3, 0.2, 0.1, CharacterizationFactors.AR6, ["AR6"], ["Standard"], "boundary processes description", 1.0)


def test_carbon_footprint_invalid_fossil_carbon_content():
    with pytest.raises(ValueError):
        CarbonFootprint("kilogram", 1.0, 0.5, 0.3, -0.2, 0.1, CharacterizationFactors.AR6, ["AR6"], ["Standard"], "boundary processes description", 1.0)


def test_carbon_footprint_invalid_biogenic_carbon_content():
    with pytest.raises(ValueError):
        CarbonFootprint("kilogram", 1.0, 0.5, 0.3, 0.2, -0.1, CharacterizationFactors.AR6, ["AR6"], ["Standard"], "boundary processes description", 1.0)


def test_carbon_footprint_invalid_characterization_factors():
    with pytest.raises(ValueError):
        CarbonFootprint("kilogram", 1.0, 0.5, 0.3, 0.2, 0.1, "AR7", ["AR6"], ["Standard"], "boundary processes description", 1.0)


def test_carbon_footprint_invalid_ipcc_characterization_factors_sources():
    with pytest.raises(ValueError):
        CarbonFootprint("kilogram", 1.0, 0.5, 0.3, 0.2, 0.1, CharacterizationFactors.AR6, [], ["Standard"], "boundary processes description", 1.0)


def test_carbon_footprint_invalid_cross_sectoral_standards_used():
    with pytest.raises(ValueError):
        CarbonFootprint("kilogram", 1.0, 0.5, 0.3, 0.2, 0.1, CharacterizationFactors.AR6, ["AR6"], [], "boundary processes description", 1.0)


def test_carbon_footprint_invalid_boundary_processes_description():
    with pytest.raises(ValueError):
        CarbonFootprint("kilogram", 1.0, 0.5, 0.3, 0.2, 0.1, CharacterizationFactors.AR6, ["AR6"], ["Standard"], "", 1.0)


def test_carbon_footprint_invalid_exempted_emissions_percent():
    with pytest.raises(ValueError):
        CarbonFootprint("kilogram", 1.0, 0.5, 0.3, 0.2, 0.1, CharacterizationFactors.AR6, ["AR6"], ["Standard"], "boundary processes description", 6.0)