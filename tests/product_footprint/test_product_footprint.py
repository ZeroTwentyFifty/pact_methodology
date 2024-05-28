import pytest

from datetime import datetime

from pathfinder_framework.carbon_footprint.carbon_footprint import CarbonFootprint
from pathfinder_framework.assurance.assurance import (
    Assurance, Coverage, Level, Boundary
)
from pathfinder_framework.product_footprint.id import ProductFootprintId
from pathfinder_framework.product_footprint.product_footprint import ProductFootprint
from pathfinder_framework.product_footprint.status import ProductFootprintStatus
from pathfinder_framework.urn import CompanyId, ProductId
from pathfinder_framework.product_footprint.cpc import CPCCodeLookup, CPC
from pathfinder_framework.product_footprint.version import Version
from pathfinder_framework.datetime import DateTime
from pathfinder_framework.carbon_footprint.characterization_factors import CharacterizationFactors
from pathfinder_framework.carbon_footprint.cross_sectoral_standard import CrossSectoralStandard
from pathfinder_framework.carbon_footprint.declared_unit import DeclaredUnit
from pathfinder_framework.datetime import DateTime
from pathfinder_framework.carbon_footprint.reference_period import ReferencePeriod
from pathfinder_framework.carbon_footprint.geographical_scope import (
    CarbonFootprintGeographicalScope, GeographicalGranularity
)
from pathfinder_framework.data_quality_indicators.data_quality_indicators import DataQualityIndicators


@pytest.fixture(scope="module")
def company_ids() -> list[CompanyId]:
    return [CompanyId("urn:pathfinder:company:customcode:buyer-assigned:acme-corp")]


@pytest.fixture(scope="module")
def product_ids() -> list[ProductId]:
    return [ProductId("urn:pathfinder:product:customcode:buyer-assigned:acme-product")]


@pytest.fixture(scope="module")
def valid_cpc() -> CPC:
    cpc_code_lookup = CPCCodeLookup()
    return cpc_code_lookup.lookup('0111')


@pytest.fixture(scope="module")
def version() -> Version:
    return Version(1)

@pytest.fixture
def valid_carbon_footprint_data():
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
        "cross_sectoral_standards_used": [CrossSectoralStandard.GHG_PROTOCOL],
        "boundary_processes_description": "boundary processes description",
        "exempted_emissions_percent": 1.0,
        "reference_period": ReferencePeriod(start=DateTime.now(), end=DateTime.now()),
        "packaging_emissions_included": True,
        "geographical_scope": CarbonFootprintGeographicalScope(global_scope=True, geography_country_subdivision=None,
                                                               geography_country=None,
                                                               geography_region_or_subregion=None),
        "primary_data_share": 50.0,
        "dqi": DataQualityIndicators(reference_period=ReferencePeriod(start=DateTime.now(), end=DateTime.now())),
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
        )
    }


@pytest.fixture
def carbon_footprint(valid_carbon_footprint_data):
    return CarbonFootprint(**valid_carbon_footprint_data)


def test_product_footprint_initialization(company_ids, product_ids, valid_cpc, version, carbon_footprint):
    product_footprint_id = ProductFootprintId()
    product_footprint = ProductFootprint(
        id=product_footprint_id,
        version=version,
        created=DateTime.now(),
        updated=DateTime.now(),
        status=ProductFootprintStatus.ACTIVE,
        status_comment="This is a comment",
        validity_period_start=DateTime.now(),
        validity_period_end=DateTime.now(),
        company_name="Company Name",
        company_ids=company_ids,
        product_description="Product Description",
        product_ids=product_ids,
        product_category_cpc=valid_cpc,
        product_name_company="Product Name Company",
        comment="This is a comment",
        extensions={"key": "value"},
        pcf=carbon_footprint
    )
    assert product_footprint.id == product_footprint_id
    assert product_footprint.version == version
    assert isinstance(product_footprint.created, DateTime)
    assert isinstance(product_footprint.updated, DateTime)
    assert product_footprint.status == ProductFootprintStatus.ACTIVE
    assert product_footprint.status_comment == "This is a comment"
    assert isinstance(product_footprint.validity_period_start, DateTime)
    assert isinstance(product_footprint.validity_period_end, DateTime)
    assert product_footprint.company_name == "Company Name"
    assert product_footprint.company_ids == company_ids
    assert product_footprint.product_description == "Product Description"
    assert product_footprint.product_ids == product_ids
    assert product_footprint.product_category_cpc == valid_cpc
    assert product_footprint.product_name_company == "Product Name Company"
    assert product_footprint.comment == "This is a comment"
    assert product_footprint.extensions == {"key": "value"}
    assert isinstance(product_footprint.pcf, CarbonFootprint)



def test_product_footprint_default_initialization(company_ids, product_ids, valid_cpc, version, carbon_footprint):
    """Tests that a ProductFootprint instance initializes with default values for optional attributes."""
    product_footprint = ProductFootprint(
        version=version,
        created=DateTime.now(),
        updated=DateTime.now(),
        status=ProductFootprintStatus.ACTIVE,
        status_comment="This is a comment",
        validity_period_start=DateTime.now(),
        validity_period_end=DateTime.now(),
        company_name="Company Name",
        company_ids=company_ids,
        product_description="Product Description",
        product_ids=product_ids,
        product_category_cpc=valid_cpc,
        product_name_company="Product Name Company",
        comment="This is a comment",
        extensions={"key": "value"},
        pcf=carbon_footprint
    )
    assert isinstance(product_footprint.id, ProductFootprintId)


def test_product_footprint_spec_version(company_ids, product_ids, valid_cpc, version, carbon_footprint):
    """Tests that a ProductFootprint instance has a specVersion attribute."""
    product_footprint = ProductFootprint(
        version=version,
        created=DateTime.now(),
        updated=DateTime.now(),
        status=ProductFootprintStatus.ACTIVE,
        status_comment="This is a comment",
        validity_period_start=DateTime.now(),
        validity_period_end=DateTime.now(),
        company_name="Company Name",
        company_ids=company_ids,
        product_description="Product Description",
        product_ids=product_ids,
        product_category_cpc=valid_cpc,
        product_name_company="Product Name Company",
        comment="This is a comment",
        extensions={"key": "value"},
        pcf=carbon_footprint
    )
    assert product_footprint.spec_version == "2.0.0"


def test_product_footprint_repr(company_ids, product_ids, valid_cpc, version, carbon_footprint):
    """Tests that the __repr__ method returns the expected string representation."""
    product_footprint_id = ProductFootprintId()
    product_footprint = ProductFootprint(
        id=product_footprint_id,
        version=version,
        created=DateTime.now(),
        updated=DateTime.now(),
        status=ProductFootprintStatus.ACTIVE,
        status_comment="This is a comment",
        validity_period_start=DateTime.now(),
        validity_period_end=DateTime.now(),
        company_name="Company Name",
        company_ids=company_ids,
        product_description="Product Description",
        product_ids=product_ids,
        product_category_cpc=valid_cpc,
        product_name_company="Product Name Company",
        comment="This is a comment",
        extensions={"key": "value"},
        pcf=carbon_footprint
    )
    expected_repr = f"ProductFootprint(id={product_footprint_id})"
    assert repr(product_footprint) == expected_repr

def test_product_footprint_pcf_validation(company_ids, product_ids, valid_cpc, version, carbon_footprint):
    with pytest.raises(ValueError):
        ProductFootprint(
            version=version,
            created=DateTime.now(),
            updated=DateTime.now(),
            status=ProductFootprintStatus.ACTIVE,
            status_comment="This is a comment",
            validity_period_start=DateTime.now(),
            validity_period_end=DateTime.now(),
            company_name="Company Name",
            company_ids=company_ids,
            product_description="Product Description",
            product_ids=product_ids,
            product_category_cpc=valid_cpc,
            product_name_company="Product Name Company",
            comment="This is a comment",
            extensions={"key": "value"},
            pcf="Invalid pcf"
        )

def test_product_footprint_pcf_validation_success(company_ids, product_ids, valid_cpc, version, carbon_footprint):
    product_footprint = ProductFootprint(
        version=version,
        created=DateTime.now(),
        updated=DateTime.now(),
        status=ProductFootprintStatus.ACTIVE,
        status_comment="This is a comment",
        validity_period_start=DateTime.now(),
        validity_period_end=DateTime.now(),
        company_name="Company Name",
        company_ids=company_ids,
        product_description="Product Description",
        product_ids=product_ids,
        product_category_cpc=valid_cpc,
        product_name_company="Product Name Company",
        comment="This is a comment",
        extensions={"key": "value"},
        pcf=carbon_footprint
    )
    assert isinstance(product_footprint.pcf, CarbonFootprint)