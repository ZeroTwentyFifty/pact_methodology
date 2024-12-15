import pytest

from pact_methodology.assurance.assurance import (
    Assurance,
    Coverage,
    Level,
    Boundary,
)
from pact_methodology.carbon_footprint.carbon_footprint import CarbonFootprint
from pact_methodology.carbon_footprint.characterization_factors import (
    CharacterizationFactors,
)
from pact_methodology.carbon_footprint.cross_sectoral_standard import (
    CrossSectoralStandard,
)
from pact_methodology.carbon_footprint.cross_sectoral_standard_set import CrossSectoralStandardSet
from pact_methodology.carbon_footprint.declared_unit import DeclaredUnit
from pact_methodology.datetime import DateTime
from pact_methodology.carbon_footprint.reference_period import ReferencePeriod
from pact_methodology.carbon_footprint.geographical_scope import (
    CarbonFootprintGeographicalScope,
    GeographicalGranularity,
)
from pact_methodology.data_quality_indicators.data_quality_indicators import (
    DataQualityIndicators, DataQualityRating
)
from pact_methodology.carbon_footprint.biogenic_accounting_methodology import BiogenicAccountingMethodology
from pact_methodology.carbon_footprint.product_or_sector_specific_rule import ProductOrSectorSpecificRule
from pact_methodology.carbon_footprint.product_or_sector_specific_rule_operator import ProductOrSectorSpecificRuleOperator
from pact_methodology.carbon_footprint.product_or_sector_specific_rule_set import ProductOrSectorSpecificRuleSet
from pact_methodology.carbon_footprint.emission_factor_ds import EmissionFactorDS
from pact_methodology.carbon_footprint.emission_factor_ds_set import EmissionFactorDSSet

@pytest.fixture
def valid_carbon_footprint_data():
    standards_set = CrossSectoralStandardSet()
    standards_set.add(CrossSectoralStandard.GHG_PROTOCOL)
    
    emission_factor_ds_set = EmissionFactorDSSet()
    emission_factor_ds_set.add_ds(EmissionFactorDS(name="ecoinvent", version="3.9.1"))

    return {
        "declared_unit": DeclaredUnit.KILOGRAM,
        "unitary_product_amount": 1.0,
        "p_cf_excluding_biogenic": 0.5,
        "p_cf_including_biogenic": 2,
        "fossil_ghg_emissions": 0.3,
        "fossil_carbon_content": 0.2,
        "biogenic_carbon_content": 0.1,
        "characterization_factors": CharacterizationFactors.AR6,
        "ipcc_characterization_factors_sources": ["AR6"],
        "cross_sectoral_standards_used": standards_set,
        "boundary_processes_description": "boundary processes description",
        "exempted_emissions_percent": 1.0,
        "exempted_emissions_description": "Rationale for exclusion",
        "reference_period": ReferencePeriod(start=DateTime("2022-01-01T00:00:00Z"), end=DateTime("2022-12-31T23:59:59Z")),
        "packaging_emissions_included": True,
        "geographical_scope": CarbonFootprintGeographicalScope(
            global_scope=True,
            geography_country_subdivision=None,
            geography_country=None,
            geography_region_or_subregion=None,
        ),
        "primary_data_share": 50.0,
        "dqi": DataQualityIndicators(
            reference_period=ReferencePeriod(start=DateTime("2022-01-01T00:00:00Z"), end=DateTime("2022-12-31T23:59:59Z")),
            coverage_percent=80.0,
            technological_dqr=DataQualityRating(2),
            temporal_dqr=DataQualityRating(2),
            geographical_dqr=DataQualityRating(1),
            completeness_dqr=DataQualityRating(2),
            reliability_dqr=DataQualityRating(3),
        ),
        "secondary_emission_factor_sources": emission_factor_ds_set,
        "d_luc_ghg_emissions": 2,
        "land_management_ghg_emissions": 1.0,
        "other_biogenic_ghg_emissions": 1.5,
        "biogenic_carbon_withdrawal": -1.0,
        "iluc_ghg_emissions": 1.0,
        "aircraft_ghg_emissions": 1.0,
        "packaging_ghg_emissions": 1.0,
        "allocation_rules_description": "Example allocation rules description",
        "uncertainty_assessment_description": "Example uncertainty assessment description",
        "assurance": Assurance(
            assurance=True,
            provider_name="Example provider name",
            coverage=Coverage.PCF_SYSTEM,
            level=Level.REASONABLE,
            boundary=Boundary.GATE_TO_GATE,
            completed_at=DateTime.now(),
            standard_name="Example standard name",
            comments="Example comments",
        ),
        "biogenic_accounting_methodology": BiogenicAccountingMethodology.GHGP,
        "product_or_sector_specific_rules": ProductOrSectorSpecificRuleSet(
            rules=[ProductOrSectorSpecificRule(
                operator=ProductOrSectorSpecificRuleOperator.OTHER,
                rule_names=["Rule1"],
                other_operator_name="Custom Operator",
            )]
        )
    }


def test_carbon_footprint_exists():
    assert CarbonFootprint is not None


def test_carbon_footprint_instantiation(valid_carbon_footprint_data):
    carbon_footprint = CarbonFootprint(**valid_carbon_footprint_data)
    assert isinstance(carbon_footprint, CarbonFootprint)


def test_carbon_footprint_attributes(valid_carbon_footprint_data):
    carbon_footprint = CarbonFootprint(**valid_carbon_footprint_data)
    assert (
        carbon_footprint.declared_unit == valid_carbon_footprint_data["declared_unit"]
    )
    assert (
        carbon_footprint.unitary_product_amount
        == valid_carbon_footprint_data["unitary_product_amount"]
    )
    assert (
        carbon_footprint.p_cf_excluding_biogenic
        == valid_carbon_footprint_data["p_cf_excluding_biogenic"]
    )
    assert (
        carbon_footprint.p_cf_including_biogenic
        == valid_carbon_footprint_data["p_cf_including_biogenic"]
    )
    assert (
        carbon_footprint.fossil_ghg_emissions
        == valid_carbon_footprint_data["fossil_ghg_emissions"]
    )
    assert (
        carbon_footprint.fossil_carbon_content
        == valid_carbon_footprint_data["fossil_carbon_content"]
    )
    assert (
        carbon_footprint.biogenic_carbon_content
        == valid_carbon_footprint_data["biogenic_carbon_content"]
    )
    assert (
        carbon_footprint.characterization_factors
        == valid_carbon_footprint_data["characterization_factors"]
    )
    assert (
        carbon_footprint.ipcc_characterization_factors_sources
        == valid_carbon_footprint_data["ipcc_characterization_factors_sources"]
    )
    assert (
        carbon_footprint.cross_sectoral_standards_used
        == valid_carbon_footprint_data["cross_sectoral_standards_used"]
    )
    assert (
        carbon_footprint.boundary_processes_description
        == valid_carbon_footprint_data["boundary_processes_description"]
    )
    assert (
        carbon_footprint.exempted_emissions_percent
        == valid_carbon_footprint_data["exempted_emissions_percent"]
    )
    assert (
        carbon_footprint.exempted_emissions_description
        == valid_carbon_footprint_data["exempted_emissions_description"]
    )
    assert isinstance(carbon_footprint.reference_period, ReferencePeriod)
    assert (
        carbon_footprint.packaging_emissions_included
        == valid_carbon_footprint_data["packaging_emissions_included"]
    )
    assert isinstance(
        carbon_footprint.geographical_scope, CarbonFootprintGeographicalScope
    )
    assert isinstance(carbon_footprint.dqi, DataQualityIndicators)
    assert (
        carbon_footprint.d_luc_ghg_emissions
        == valid_carbon_footprint_data["d_luc_ghg_emissions"]
    )
    assert (
        carbon_footprint.land_management_ghg_emissions
        == valid_carbon_footprint_data["land_management_ghg_emissions"]
    )
    assert (
        carbon_footprint.other_biogenic_ghg_emissions
        == valid_carbon_footprint_data["other_biogenic_ghg_emissions"]
    )
    assert (
        carbon_footprint.biogenic_carbon_withdrawal
        == valid_carbon_footprint_data["biogenic_carbon_withdrawal"]
    )
    assert (
        carbon_footprint.iluc_ghg_emissions
        == valid_carbon_footprint_data["iluc_ghg_emissions"]
    )
    assert (
        carbon_footprint.aircraft_ghg_emissions
        == valid_carbon_footprint_data["aircraft_ghg_emissions"]
    )
    assert (
        carbon_footprint.packaging_ghg_emissions
        == valid_carbon_footprint_data["packaging_ghg_emissions"]
    )
    assert (
        carbon_footprint.allocation_rules_description
        == valid_carbon_footprint_data["allocation_rules_description"]
    )
    assert (
        carbon_footprint.uncertainty_assessment_description
        == valid_carbon_footprint_data["uncertainty_assessment_description"]
    )
    assert isinstance(carbon_footprint.assurance, Assurance)
    assert (
        carbon_footprint.biogenic_accounting_methodology
        == valid_carbon_footprint_data["biogenic_accounting_methodology"]
    )
    assert (
        carbon_footprint.product_or_sector_specific_rules
        == valid_carbon_footprint_data["product_or_sector_specific_rules"]
    )

def test_carbon_footprint_invalid_declared_unit(valid_carbon_footprint_data):
    invalid_data = {**valid_carbon_footprint_data, "declared_unit": "invalid unit"}
    with pytest.raises(
        ValueError,
        match="declared_unit 'invalid unit' is not valid. It must be one of the following: liter, kilogram, cubic meter, kilowatt hour, megajoule, ton kilometer, square meter",
    ):
        CarbonFootprint(**invalid_data)


def test_carbon_footprint_invalid_unitary_product_amount(valid_carbon_footprint_data):
    invalid_data = {**valid_carbon_footprint_data, "unitary_product_amount": 0.0}
    with pytest.raises(
        ValueError, match="unitary_product_amount must be strictly greater than 0"
    ):
        CarbonFootprint(**invalid_data)


def test_carbon_footprint_invalid_p_cf_excluding_biogenic(valid_carbon_footprint_data):
    invalid_data = {**valid_carbon_footprint_data, "p_cf_excluding_biogenic": -0.5}
    with pytest.raises(
        ValueError, match="p_cf_excluding_biogenic must be equal to or greater than 0"
    ):
        CarbonFootprint(**invalid_data)


def test_carbon_footprint_invalid_fossil_ghg_emissions(valid_carbon_footprint_data):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["fossil_ghg_emissions"] = -0.3
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert (
        str(excinfo.value) == "fossil_ghg_emissions must be equal to or greater than 0"
    )


def test_carbon_footprint_invalid_fossil_carbon_content(valid_carbon_footprint_data):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["fossil_carbon_content"] = -0.2
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert (
        str(excinfo.value) == "fossil_carbon_content must be equal to or greater than 0"
    )


def test_carbon_footprint_invalid_biogenic_carbon_content(valid_carbon_footprint_data):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["biogenic_carbon_content"] = -0.1
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert (
        str(excinfo.value)
        == "biogenic_carbon_content must be equal to or greater than 0"
    )


def test_carbon_footprint_invalid_characterization_factors(valid_carbon_footprint_data):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["characterization_factors"] = "AR7"
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert (
        str(excinfo.value)
        == "characterization_factors must be an instance of CharacterizationFactors"
    )


def test_carbon_footprint_invalid_ipcc_characterization_factors_sources(
    valid_carbon_footprint_data,
):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["ipcc_characterization_factors_sources"] = []
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert (
        str(excinfo.value) == "ipcc_characterization_factors_sources must not be empty"
    )


def test_carbon_footprint_invalid_cross_sectoral_standards_used(
    valid_carbon_footprint_data,
):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["cross_sectoral_standards_used"] = ["invalid standard"]
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert (
        str(excinfo.value)
        == "cross_sectoral_standards_used must be an instance of CrossSectoralStandardSet"
    )


def test_carbon_footprint_invalid_boundary_processes_description(
    valid_carbon_footprint_data,
):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["boundary_processes_description"] = ""
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == "boundary_processes_description must not be empty"


def test_carbon_footprint_invalid_exempted_emissions_percent(
    valid_carbon_footprint_data,
):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["exempted_emissions_percent"] = 6.0
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert (
        str(excinfo.value) == "exempted_emissions_percent must be between 0.0 and 5.0"
    )


def test_carbon_footprint_invalid_exempted_emissions_description(valid_carbon_footprint_data):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["exempted_emissions_description"] = 123  # Invalid type
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == "exempted_emissions_description must be a string"


def test_carbon_footprint_invalid_reference_period(valid_carbon_footprint_data):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["reference_period"] = "invalid reference period"
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert (
        str(excinfo.value) == "reference_period must be an instance of ReferencePeriod"
    )


def test_carbon_footprint_invalid_packaging_emissions_included(
    valid_carbon_footprint_data,
):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["packaging_emissions_included"] = "not a boolean"
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == "packaging_emissions_included must be a boolean"


def test_carbon_footprint_valid_packaging_emissions_included(
    valid_carbon_footprint_data,
):
    carbon_footprint = CarbonFootprint(**valid_carbon_footprint_data)
    assert carbon_footprint.packaging_emissions_included is True


@pytest.mark.parametrize(
    "attribute, value",
    [
        ("p_cf_including_biogenic", 1.0),
        ("d_luc_ghg_emissions", 1.0),
        ("land_management_ghg_emissions", 1.0),
        ("other_biogenic_ghg_emissions", 1.5),
        ("biogenic_carbon_withdrawal", -1.0),
    ],
)
def test_carbon_footprint_valid_attribute(
    valid_carbon_footprint_data, attribute, value
):
    valid_carbon_footprint_data[attribute] = value
    carbon_footprint = CarbonFootprint(**valid_carbon_footprint_data)
    assert getattr(carbon_footprint, attribute) == value


@pytest.mark.parametrize(
    "attribute, value, expected_error",
    [
        (
            "p_cf_including_biogenic",
            "not a number",
            "p_cf_including_biogenic must be a number",
        ),
        (
            "d_luc_ghg_emissions",
            "not a number",
            "d_luc_ghg_emissions must be a non-negative number",
        ),
        (
            "land_management_ghg_emissions",
            "not a number",
            "land_management_ghg_emissions must be a number",
        ),
        (
            "other_biogenic_ghg_emissions",
            "not a number",
            "other_biogenic_ghg_emissions must be a non-negative number",
        ),
        (
            "other_biogenic_ghg_emissions",
            -1,
            "other_biogenic_ghg_emissions must be a non-negative number",
        ),
        (
            "biogenic_carbon_withdrawal",
            "not a number",
            "biogenic_carbon_withdrawal must be a non-positive number",
        ),
        (
            "biogenic_carbon_withdrawal",
            1,
            "biogenic_carbon_withdrawal must be a non-positive number",
        ),
    ],
)
def test_carbon_footprint_invalid_attribute_type(
    valid_carbon_footprint_data, attribute, value, expected_error
):
    valid_carbon_footprint_data[attribute] = value
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**valid_carbon_footprint_data)
    assert str(excinfo.value) == expected_error


@pytest.mark.parametrize(
    "attribute",
    [
        "p_cf_including_biogenic",
        "d_luc_ghg_emissions",
        "land_management_ghg_emissions",
        "other_biogenic_ghg_emissions",
        "biogenic_carbon_withdrawal",
        "biogenic_accounting_methodology",
    ],
)
def test_carbon_footprint_attribute_optional_before_2025(
    valid_carbon_footprint_data, attribute
):
    del valid_carbon_footprint_data[attribute]
    valid_carbon_footprint_data["reference_period"] = ReferencePeriod(
        start=DateTime("2024-01-01T00:00:00Z"), end=DateTime("2024-12-31T00:00:00Z")
    )
    carbon_footprint = CarbonFootprint(**valid_carbon_footprint_data)
    assert getattr(carbon_footprint, attribute) is None


@pytest.mark.parametrize(
    "attribute",
    [
        "p_cf_including_biogenic",
        "d_luc_ghg_emissions",
        "land_management_ghg_emissions",
        "other_biogenic_ghg_emissions",
        "biogenic_carbon_withdrawal",
        "biogenic_accounting_methodology",
    ],
)
def test_carbon_footprint_missing_attributes_valid_before_2025(
    valid_carbon_footprint_data, attribute
):
    if hasattr(valid_carbon_footprint_data, attribute):
        delattr(valid_carbon_footprint_data, attribute)

    valid_carbon_footprint_data["reference_period"] = ReferencePeriod(
        start=DateTime("2024-01-01T00:00:00Z"), end=DateTime("2024-12-31T00:00:00Z")
    )

    carbon_footprint = CarbonFootprint(**valid_carbon_footprint_data)


@pytest.mark.parametrize(
    "attribute",
    [
        "p_cf_including_biogenic",
        "d_luc_ghg_emissions",
        "land_management_ghg_emissions",
        "other_biogenic_ghg_emissions",
        "biogenic_carbon_withdrawal",
        "biogenic_accounting_methodology",
    ],
)
def test_carbon_footprint_missing_attributes_invalid_after_2025(
    valid_carbon_footprint_data, attribute
):
    del valid_carbon_footprint_data[attribute]
    valid_carbon_footprint_data["reference_period"] = ReferencePeriod(
        start=DateTime("2025-01-01T00:00:00Z"), end=DateTime("2026-01-01T00:00:00Z")
    )

    with pytest.raises(ValueError):
        CarbonFootprint(**valid_carbon_footprint_data)


def test_primary_data_share_optional_before_2025(valid_carbon_footprint_data):
    valid_carbon_footprint_data["reference_period"] = ReferencePeriod(
        start=DateTime("2024-01-01T00:00:00Z"), end=DateTime("2024-12-31T00:00:00Z")
    )
    valid_carbon_footprint_data["primary_data_share"] = None
    carbon_footprint = CarbonFootprint(**valid_carbon_footprint_data)


def test_primary_data_share_required_after_2025(valid_carbon_footprint_data):
    valid_carbon_footprint_data["reference_period"] = ReferencePeriod(
        start=DateTime("2025-01-01T00:00:00Z"), end=DateTime("2026-01-01T00:00:00Z")
    )
    valid_carbon_footprint_data["primary_data_share"] = None
    with pytest.raises(
        ValueError, match="Attribute 'primary_data_share' must be defined"
    ):
        CarbonFootprint(**valid_carbon_footprint_data)


def test_dqi_optional_before_2025(valid_carbon_footprint_data):
    valid_carbon_footprint_data["reference_period"] = ReferencePeriod(
        start=DateTime("2024-01-01T00:00:00Z"), end=DateTime("2024-12-31T00:00:00Z")
    )
    valid_carbon_footprint_data["dqi"] = None
    carbon_footprint = CarbonFootprint(**valid_carbon_footprint_data)


def test_dqi_required_after_2025(valid_carbon_footprint_data):
    valid_carbon_footprint_data["reference_period"] = ReferencePeriod(
        start=DateTime("2025-01-01T00:00:00Z"), end=DateTime("2026-01-01T00:00:00Z")
    )
    valid_carbon_footprint_data["dqi"] = None
    with pytest.raises(ValueError, match="Attribute 'dqi' must be defined"):
        CarbonFootprint(**valid_carbon_footprint_data)


def test_primary_data_share_or_dqi_required_before_2025(valid_carbon_footprint_data):
    valid_carbon_footprint_data["reference_period"] = ReferencePeriod(
        start=DateTime("2024-01-01T00:00:00Z"), end=DateTime("2024-12-31T00:00:00Z")
    )
    valid_carbon_footprint_data["primary_data_share"] = None
    valid_carbon_footprint_data["dqi"] = None
    with pytest.raises(
        ValueError,
        match="At least one of 'primary_data_share' or 'dqi' must be defined",
    ):
        CarbonFootprint(**valid_carbon_footprint_data)


def test_carbon_footprint_invalid_geographical_scope_type(valid_carbon_footprint_data):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["geographical_scope"] = "not a CarbonFootprintGeographicalScope"
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert (
        str(excinfo.value)
        == "geographical_scope must be an instance of CarbonFootprintGeographicalScope"
    )


def test_carbon_footprint_valid_geographical_scope(valid_carbon_footprint_data):
    carbon_footprint = CarbonFootprint(**valid_carbon_footprint_data)
    assert isinstance(
        carbon_footprint.geographical_scope, CarbonFootprintGeographicalScope
    )


def test_carbon_footprint_geographical_scope_attributes(valid_carbon_footprint_data):
    carbon_footprint = CarbonFootprint(**valid_carbon_footprint_data)
    assert carbon_footprint.geographical_scope.scope == "Global"
    assert (
        carbon_footprint.geographical_scope.granularity
        == GeographicalGranularity.GLOBAL
    )


@pytest.mark.parametrize("iluc_ghg_emissions", [None, 0, 1, 100, 0.0, 1.0, 100.0])
def test_carbon_footprint_valid_iluc_ghg_emissions(
    valid_carbon_footprint_data, iluc_ghg_emissions
):
    valid_data = valid_carbon_footprint_data.copy()
    valid_data["iluc_ghg_emissions"] = iluc_ghg_emissions
    CarbonFootprint(**valid_data)


@pytest.mark.parametrize(
    "iluc_ghg_emissions, expected_error",
    [
        (-1.0, "iluc_ghg_emissions must be a non-negative number"),
        ("not a number", "iluc_ghg_emissions must be a non-negative number"),
    ],
)
def test_carbon_footprint_invalid_iluc_ghg_emissions(
    valid_carbon_footprint_data, iluc_ghg_emissions, expected_error
):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["iluc_ghg_emissions"] = iluc_ghg_emissions
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == expected_error


@pytest.mark.parametrize("aircraft_ghg_emissions", [None, 0, 1, 100, 0.0, 1.0, 100.0])
def test_carbon_footprint_valid_aircraft_ghg_emissions(
    valid_carbon_footprint_data, aircraft_ghg_emissions
):
    valid_data = valid_carbon_footprint_data.copy()
    valid_data["aircraft_ghg_emissions"] = aircraft_ghg_emissions
    CarbonFootprint(**valid_data)


@pytest.mark.parametrize(
    "aircraft_ghg_emissions, expected_error",
    [
        (-1.0, "aircraft_ghg_emissions must be a non-negative number"),
        ("not a number", "aircraft_ghg_emissions must be a non-negative number"),
    ],
)
def test_carbon_footprint_invalid_aircraft_ghg_emissions(
    valid_carbon_footprint_data, aircraft_ghg_emissions, expected_error
):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["aircraft_ghg_emissions"] = aircraft_ghg_emissions
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == expected_error


@pytest.mark.parametrize(
    "packaging_ghg_emissions, packaging_emissions_included",
    [
        (0.0, True),
        (1.0, True),
        (100.0, True),
        (None, False),
    ],
)
def test_carbon_footprint_valid_packaging_ghg_emissions(
    valid_carbon_footprint_data, packaging_ghg_emissions, packaging_emissions_included
):
    valid_data = valid_carbon_footprint_data.copy()
    valid_data["packaging_ghg_emissions"] = packaging_ghg_emissions
    valid_data["packaging_emissions_included"] = packaging_emissions_included
    CarbonFootprint(**valid_data)


@pytest.mark.parametrize(
    "packaging_ghg_emissions, packaging_emissions_included, expected_error",
    [
        (
            -1.0,
            True,
            "packaging_ghg_emissions must be a non-negative number if packaging_emissions_included is true",
        ),
        (
            "not a number",
            True,
            "packaging_ghg_emissions must be a non-negative number if packaging_emissions_included is true",
        ),
        (
            1.0,
            False,
            "packaging_ghg_emissions must not be defined if packaging_emissions_included is false",
        ),
        (
            None,
            True,
            "packaging_ghg_emissions must be a non-negative number if packaging_emissions_included is true",
        ),
    ],
)
def test_carbon_footprint_invalid_packaging_ghg_emissions(
    valid_carbon_footprint_data,
    packaging_ghg_emissions,
    packaging_emissions_included,
    expected_error,
):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["packaging_ghg_emissions"] = packaging_ghg_emissions
    invalid_data["packaging_emissions_included"] = packaging_emissions_included
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == expected_error


@pytest.mark.parametrize(
    "allocation_rules_description", [None, "Example allocation rules description"]
)
def test_carbon_footprint_valid_allocation_rules_description(
    valid_carbon_footprint_data, allocation_rules_description
):
    valid_data = valid_carbon_footprint_data.copy()
    valid_data["allocation_rules_description"] = allocation_rules_description
    CarbonFootprint(**valid_data)


@pytest.mark.parametrize(
    "allocation_rules_description, expected_error",
    [
        (1, "allocation_rules_description must be a string"),
    ],
)
def test_carbon_footprint_invalid_allocation_rules_description(
    valid_carbon_footprint_data, allocation_rules_description, expected_error
):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["allocation_rules_description"] = allocation_rules_description
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == expected_error


@pytest.mark.parametrize(
    "uncertainty_assessment_description", [None, "uncertainty assessment description"]
)
def test_carbon_footprint_valid_uncertainty_assessment_description(
    valid_carbon_footprint_data, uncertainty_assessment_description
):
    valid_data = valid_carbon_footprint_data.copy()
    valid_data["uncertainty_assessment_description"] = (
        uncertainty_assessment_description
    )
    CarbonFootprint(**valid_data)


@pytest.mark.parametrize(
    "uncertainty_assessment_description, expected_error",
    [
        (1, "uncertainty_assessment_description must be a string"),
    ],
)
def test_carbon_footprint_invalid_uncertainty_assessment_description(
    valid_carbon_footprint_data, uncertainty_assessment_description, expected_error
):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["uncertainty_assessment_description"] = (
        uncertainty_assessment_description
    )
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == expected_error


@pytest.mark.parametrize(
    "assurance",
    [
        None,
        Assurance(
            assurance=True,
            provider_name="Example provider name",
            coverage=Coverage.PCF_SYSTEM,
            level=Level.REASONABLE,
            boundary=Boundary.GATE_TO_GATE,
            completed_at=DateTime.now(),
            standard_name="Example standard name",
            comments="Example comments",
        ),
    ],
)
def test_carbon_footprint_valid_assurance(valid_carbon_footprint_data, assurance):
    valid_data = valid_carbon_footprint_data.copy()
    valid_data["assurance"] = assurance
    CarbonFootprint(**valid_data)


@pytest.mark.parametrize(
    "assurance, expected_error",
    [
        (1, "assurance must be an instance of Assurance"),
    ],
)
def test_carbon_footprint_invalid_assurance(
    valid_carbon_footprint_data, assurance, expected_error
):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["assurance"] = assurance
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == expected_error


@pytest.mark.parametrize(
    "product_or_sector_specific_rules",
    [
        None,
        ProductOrSectorSpecificRuleSet([ProductOrSectorSpecificRule(
            operator=ProductOrSectorSpecificRuleOperator.OTHER,
            rule_names=["Rule1"],
            other_operator_name="Custom Operator",
        )]),
    ],
)
def test_carbon_footprint_valid_product_or_sector_specific_rules(valid_carbon_footprint_data, product_or_sector_specific_rules):
    valid_data = valid_carbon_footprint_data.copy()
    valid_data["product_or_sector_specific_rules"] = product_or_sector_specific_rules
    CarbonFootprint(**valid_data)


@pytest.mark.parametrize(
    "product_or_sector_specific_rules, expected_error",
    [
        ([1], "product_or_sector_specific_rules must be an instance of ProductOrSectorSpecificRuleSet"),
    ],
)
def test_carbon_footprint_invalid_product_or_sector_specific_rules(
    valid_carbon_footprint_data, product_or_sector_specific_rules, expected_error
):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["product_or_sector_specific_rules"] = product_or_sector_specific_rules
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == expected_error


def test_carbon_footprint_secondary_emission_factor_sources(valid_carbon_footprint_data):
    carbon_footprint = CarbonFootprint(**valid_carbon_footprint_data)
    assert isinstance(carbon_footprint.secondary_emission_factor_sources, EmissionFactorDSSet)


@pytest.mark.parametrize(
    "secondary_emission_factor_sources, expected_error",
    [
        (1, "secondary_emission_factor_sources must be an instance of EmissionFactorDSSet"),
    ],
)
def test_carbon_footprint_invalid_secondary_emission_factor_sources(
    valid_carbon_footprint_data, secondary_emission_factor_sources, expected_error
):
    invalid_data = valid_carbon_footprint_data.copy()
    invalid_data["secondary_emission_factor_sources"] = secondary_emission_factor_sources
    with pytest.raises(ValueError) as excinfo:
        CarbonFootprint(**invalid_data)
    assert str(excinfo.value) == expected_error


def test_carbon_footprint_str(valid_carbon_footprint_data):
    carbon_footprint = CarbonFootprint(**valid_carbon_footprint_data)
    assert str(carbon_footprint) == (
        f"CarbonFootprint("
        f"declared_unit=kilogram, "
        f"unitary_product_amount=1.0, "
        f"p_cf_excluding_biogenic=0.5, "
        f"p_cf_including_biogenic=2, "
        f"fossil_ghg_emissions=0.3, "
        f"fossil_carbon_content=0.2, "
        f"biogenic_carbon_content=0.1, "
        f"characterization_factors=AR6, "
        f"ipcc_characterization_factors_sources=['AR6'], "
        f"cross_sectoral_standards_used={{'GHG Protocol Product standard'}}, "
        f"boundary_processes_description='boundary processes description', "
        f"exempted_emissions_percent=1.0, "
        f"exempted_emissions_description='Rationale for exclusion', "
        f"reference_period=ReferencePeriod(start=2022-01-01T00:00:00Z, end=2022-12-31T23:59:59Z), "
        f"packaging_emissions_included=True, "
        f"geographical_scope=Geographical scope: Global (at Global level), "
        f"primary_data_share=50.0, "
        f"dqi=DataQualityIndicators("
        f"reference_period=ReferencePeriod(start=2022-01-01T00:00:00Z, end=2022-12-31T23:59:59Z), "
        f"coverage_percent=80.0, "
        f"technological_dqr=2, "
        f"temporal_dqr=2, "
        f"geographical_dqr=1, "
        f"completeness_dqr=2, "
        f"reliability_dqr=3), "
        f"secondary_emission_factor_sources=EmissionFactorDSSet(emission_factor_ds_list=[EmissionFactorDS(name='ecoinvent', version='3.9.1')]), "
        f"d_luc_ghg_emissions=2, "
        f"land_management_ghg_emissions=1.0, "
        f"other_biogenic_ghg_emissions=1.5, "
        f"biogenic_carbon_withdrawal=-1.0, "
        f"iluc_ghg_emissions=1.0, "
        f"aircraft_ghg_emissions=1.0, "
        f"packaging_ghg_emissions=1.0, "
        f"allocation_rules_description='Example allocation rules description', "
        f"uncertainty_assessment_description='Example uncertainty assessment description', "
        f"assurance=Assurance(assurance=True, provider_name='Example provider name', coverage=PCF system, "
        f"level=reasonable, boundary=Gate-to-Gate, completed_at={carbon_footprint.assurance.completed_at}, "
        f"standard_name='Example standard name', comments='Example comments'), "
        f"biogenic_accounting_methodology=GHGP, "
        f"product_or_sector_specific_rules=ProductOrSectorSpecificRuleSet(rules=[ProductOrSectorSpecificRule(operator=ProductOrSectorSpecificRuleOperator.OTHER, rule_names=['Rule1'], other_operator_name='Custom Operator')]))"
    )

def test_carbon_footprint_repr(valid_carbon_footprint_data):
    carbon_footprint = CarbonFootprint(**valid_carbon_footprint_data)
    assert repr(carbon_footprint) == (
        f"CarbonFootprint(declared_unit={carbon_footprint.declared_unit!r}, "
        f"unitary_product_amount={carbon_footprint.unitary_product_amount!r}, "
        f"p_cf_excluding_biogenic={carbon_footprint.p_cf_excluding_biogenic!r}, "
        f"p_cf_including_biogenic={carbon_footprint.p_cf_including_biogenic!r}, "
        f"fossil_ghg_emissions={carbon_footprint.fossil_ghg_emissions!r}, "
        f"fossil_carbon_content={carbon_footprint.fossil_carbon_content!r}, "
        f"biogenic_carbon_content={carbon_footprint.biogenic_carbon_content!r}, "
        f"characterization_factors={carbon_footprint.characterization_factors!r}, "
        f"ipcc_characterization_factors_sources={carbon_footprint.ipcc_characterization_factors_sources!r}, "
        f"cross_sectoral_standards_used={carbon_footprint.cross_sectoral_standards_used!r}, "
        f"boundary_processes_description={carbon_footprint.boundary_processes_description!r}, "
        f"exempted_emissions_percent={carbon_footprint.exempted_emissions_percent!r}, "
        f"exempted_emissions_description={carbon_footprint.exempted_emissions_description!r}, "
        f"reference_period={carbon_footprint.reference_period!r}, "
        f"packaging_emissions_included={carbon_footprint.packaging_emissions_included!r}, "
        f"geographical_scope={carbon_footprint.geographical_scope!r}, "
        f"primary_data_share={carbon_footprint.primary_data_share!r}, "
        f"dqi={carbon_footprint.dqi!r}, "
        f"secondary_emission_factor_sources={carbon_footprint.secondary_emission_factor_sources!r}, "
        f"d_luc_ghg_emissions={carbon_footprint.d_luc_ghg_emissions!r}, "
        f"land_management_ghg_emissions={carbon_footprint.land_management_ghg_emissions!r}, "
        f"other_biogenic_ghg_emissions={carbon_footprint.other_biogenic_ghg_emissions!r}, "
        f"biogenic_carbon_withdrawal={carbon_footprint.biogenic_carbon_withdrawal!r}, "
        f"iluc_ghg_emissions={carbon_footprint.iluc_ghg_emissions!r}, "
        f"aircraft_ghg_emissions={carbon_footprint.aircraft_ghg_emissions!r}, "
        f"packaging_ghg_emissions={carbon_footprint.packaging_ghg_emissions!r}, "
        f"allocation_rules_description={carbon_footprint.allocation_rules_description!r}, "
        f"uncertainty_assessment_description={carbon_footprint.uncertainty_assessment_description!r}, "
        f"assurance={carbon_footprint.assurance!r}, "
        f"biogenic_accounting_methodology={carbon_footprint.biogenic_accounting_methodology!r}, "
        f"product_or_sector_specific_rules={carbon_footprint.product_or_sector_specific_rules!r})"
    )

def test_carbon_footprint_eq(valid_carbon_footprint_data):
    carbon_footprint1 = CarbonFootprint(**valid_carbon_footprint_data)
    carbon_footprint2 = CarbonFootprint(**valid_carbon_footprint_data)
    assert carbon_footprint1 == carbon_footprint2

def test_carbon_footprint_not_eq(valid_carbon_footprint_data):
    carbon_footprint1 = CarbonFootprint(**valid_carbon_footprint_data)
    carbon_footprint2 = CarbonFootprint(**{**valid_carbon_footprint_data, "unitary_product_amount": 2.0})
    assert carbon_footprint1 != carbon_footprint2
