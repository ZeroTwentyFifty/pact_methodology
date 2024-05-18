import pytest

from pathfinder_framework.carbon_footprint.carbon_footprint import CarbonFootprint
from pathfinder_framework.carbon_footprint.characterization_factors import CharacterizationFactors
from pathfinder_framework.carbon_footprint.cross_sectoral_standard import CrossSectoralStandard
from pathfinder_framework.carbon_footprint.declared_unit import DeclaredUnit
from pathfinder_framework.datetime import DateTime


@pytest.fixture
def valid_carbon_footprint_data():
    return {
        "declared_unit": DeclaredUnit.KILOGRAM,
        "unitary_product_amount": 1.0,
        "p_cf_excluding_biogenic": 0.5,
        "fossil_ghg_emissions": 0.3,
        "fossil_carbon_content": 0.2,
        "biogenic_carbon_content": 0.1,
        "characterization_factors": CharacterizationFactors.AR6,
        "ipcc_characterization_factors_sources": ["AR6"],
        "cross_sectoral_standards_used": [CrossSectoralStandard.GHG_PROTOCOL],
        "boundary_processes_description": "boundary processes description",
        "exempted_emissions_percent": 1.0,
        "reference_period_start": DateTime.now(),
        "reference_period_end": DateTime.now(),
        "packaging_emissions_included": True
    }


def test_carbon_footprint_exists():
    assert CarbonFootprint is not None


def test_carbon_footprint_instantiation(valid_carbon_footprint_data):
    carbon_footprint = CarbonFootprint(**valid_carbon_footprint_data)
    assert isinstance(carbon_footprint, CarbonFootprint)


def test_carbon_footprint_attributes(valid_carbon_footprint_data):
    carbon_footprint = CarbonFootprint(**valid_carbon_footprint_data)
    assert carbon_footprint.declared_unit == valid_carbon_footprint_data["declared_unit"]
    assert carbon_footprint.unitary_product_amount == valid_carbon_footprint_data["unitary_product_amount"]
    assert carbon_footprint.p_cf_excluding_biogenic == valid_carbon_footprint_data["p_cf_excluding_biogenic"]
    assert carbon_footprint.fossil_ghg_emissions == valid_carbon_footprint_data["fossil_ghg_emissions"]
    assert carbon_footprint.fossil_carbon_content == valid_carbon_footprint_data["fossil_carbon_content"]
    assert carbon_footprint.biogenic_carbon_content == valid_carbon_footprint_data["biogenic_carbon_content"]
    assert carbon_footprint.characterization_factors == valid_carbon_footprint_data["characterization_factors"]
    assert carbon_footprint.ipcc_characterization_factors_sources == valid_carbon_footprint_data["ipcc_characterization_factors_sources"]
    assert carbon_footprint.cross_sectoral_standards_used == valid_carbon_footprint_data["cross_sectoral_standards_used"]
    assert carbon_footprint.boundary_processes_description == valid_carbon_footprint_data["boundary_processes_description"]
    assert carbon_footprint.exempted_emissions_percent == valid_carbon_footprint_data["exempted_emissions_percent"]
    assert isinstance(carbon_footprint.reference_period_start, DateTime)
    assert isinstance(carbon_footprint.reference_period_end, DateTime)
    assert carbon_footprint.packaging_emissions_included == valid_carbon_footprint_data["packaging_emissions_included"]


def test_carbon_footprint_invalid_declared_unit(valid_carbon_footprint_data):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["declared_unit"] = "invalid unit"
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == "declared_unit 'invalid unit' is not valid. It must be one of the following: liter, kilogram, cubic meter, kilowatt hour, megajoule, ton kilometer, square meter"


def test_carbon_footprint_invalid_unitary_product_amount(valid_carbon_footprint_data):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["unitary_product_amount"] = 0.0
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == "unitary_product_amount must be strictly greater than 0"


def test_carbon_footprint_invalid_p_cf_excluding_biogenic(valid_carbon_footprint_data):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["p_cf_excluding_biogenic"] = -0.5
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == "p_cf_excluding_biogenic must be equal to or greater than 0"


def test_carbon_footprint_invalid_fossil_ghg_emissions(valid_carbon_footprint_data):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["fossil_ghg_emissions"] = -0.3
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == "fossil_ghg_emissions must be equal to or greater than 0"


def test_carbon_footprint_invalid_fossil_carbon_content(valid_carbon_footprint_data):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["fossil_carbon_content"] = -0.2
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == "fossil_carbon_content must be equal to or greater than 0"


def test_carbon_footprint_invalid_biogenic_carbon_content(valid_carbon_footprint_data):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["biogenic_carbon_content"] = -0.1
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == "biogenic_carbon_content must be equal to or greater than 0"


def test_carbon_footprint_invalid_characterization_factors(valid_carbon_footprint_data):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["characterization_factors"] = "AR7"
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == "characterization_factors must be an instance of CharacterizationFactors"


def test_carbon_footprint_invalid_ipcc_characterization_factors_sources(valid_carbon_footprint_data):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["ipcc_characterization_factors_sources"] = []
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == "ipcc_characterization_factors_sources must not be empty"


def test_carbon_footprint_invalid_cross_sectoral_standards_used(valid_carbon_footprint_data):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["cross_sectoral_standards_used"] = ["invalid standard"]
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == "cross_sectoral_standards_used must be a list of CrossSectoralStandard"


def test_carbon_footprint_invalid_boundary_processes_description(valid_carbon_footprint_data):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["boundary_processes_description"] = ""
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == "boundary_processes_description must not be empty"


def test_carbon_footprint_invalid_exempted_emissions_percent(valid_carbon_footprint_data):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["exempted_emissions_percent"] = 6.0
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == "exempted_emissions_percent must be between 0.0 and 5.0"


def test_carbon_footprint_invalid_reference_period_start(valid_carbon_footprint_data):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["reference_period_start"] = "invalid datetime"
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == "reference_period_start must be an instance of DateTime"


def test_carbon_footprint_invalid_reference_period_end(valid_carbon_footprint_data):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["reference_period_end"] = "invalid datetime"
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == "reference_period_end must be an instance of DateTime"


def test_carbon_footprint_invalid_packaging_emissions_included(valid_carbon_footprint_data):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["packaging_emissions_included"] = "not a boolean"
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == "packaging_emissions_included must be a boolean"


def test_carbon_footprint_valid_packaging_emissions_included(valid_carbon_footprint_data):
    carbon_footprint = CarbonFootprint(**valid_carbon_footprint_data)
    assert carbon_footprint.packaging_emissions_included is True


def test_carbon_footprint_valid_p_cf_including_biogenic(valid_carbon_footprint_data):
    valid_carbon_footprint_data["p_cf_including_biogenic"] = 1.0
    carbon_footprint = CarbonFootprint(**valid_carbon_footprint_data)
    assert carbon_footprint.p_cf_including_biogenic == 1.0


def test_carbon_footprint_invalid_p_cf_including_biogenic_type(valid_carbon_footprint_data):
    valid_carbon_footprint_data["p_cf_including_biogenic"] = "not a number"
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**valid_carbon_footprint_data)
    assert str(excinfo.value) == "p_cf_including_biogenic must be a number"


def test_carbon_footprint_p_cf_including_biogenic_optional_before_2025(valid_carbon_footprint_data):
    valid_carbon_footprint_data["reference_period_start"] = DateTime("2024-12-31T00:00:00Z")
    carbon_footprint = CarbonFootprint(**valid_carbon_footprint_data)
    assert carbon_footprint.p_cf_including_biogenic is None
