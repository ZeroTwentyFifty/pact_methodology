import pytest

from datetime import datetime

from pact_methodology.carbon_footprint.biogenic_accounting_methodology import BiogenicAccountingMethodology
from pact_methodology.carbon_footprint.carbon_footprint import CarbonFootprint
from pact_methodology.assurance.assurance import (
    Assurance,
    Coverage,
    Level,
    Boundary,
)
from pact_methodology.product_footprint.id import ProductFootprintId
from pact_methodology.product_footprint.product_footprint import ProductFootprint
from pact_methodology.product_footprint.status import ProductFootprintStatus, Status
from pact_methodology.urn import CompanyId, ProductId
from pact_methodology.product_footprint.product_id_list import ProductIdList
from pact_methodology.product_footprint.company_id_list import CompanyIdList
from pact_methodology.product_footprint.cpc import CPCCodeLookup, CPC
from pact_methodology.product_footprint.version import Version
from pact_methodology.datetime import DateTime
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
    DataQualityIndicators,
)
from pact_methodology.data_quality_indicators.data_quality_rating import DataQualityRating

from pact_methodology.product_footprint.validity_period import ValidityPeriod
from pact_methodology.data_model_extension.data_model_extension import (
    DataModelExtension,
)
from pact_methodology.carbon_footprint.emission_factor_ds import EmissionFactorDS
from pact_methodology.carbon_footprint.emission_factor_ds_set import EmissionFactorDSSet


@pytest.fixture(scope="module")
def company_ids() -> CompanyIdList:
    return CompanyIdList([CompanyId("urn:pathfinder:company:customcode:buyer-assigned:acme-corp")])


@pytest.fixture(scope="module")
def product_ids() -> list[ProductId]:
    return [ProductId("urn:pathfinder:product:customcode:buyer-assigned:acme-product")]


@pytest.fixture(scope="module")
def valid_cpc() -> CPC:
    cpc_code_lookup = CPCCodeLookup()
    return cpc_code_lookup.lookup("0111")


@pytest.fixture(scope="module")
def version() -> Version:
    return Version(1)


@pytest.fixture(scope="module")
def start_and_end_time() -> (DateTime, DateTime):
    return DateTime.now(), DateTime.create_datetime_years_from_now(3)


@pytest.fixture
def valid_carbon_footprint_data(start_and_end_time):

    start_time, end_time = start_and_end_time

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
        "reference_period": ReferencePeriod(start=start_time, end=end_time),
        "packaging_emissions_included": True,
        "geographical_scope": CarbonFootprintGeographicalScope(
            global_scope=True,
            geography_country_subdivision=None,
            geography_country=None,
            geography_region_or_subregion=None,
        ),
        "primary_data_share": 50.0,
        "secondary_emission_factor_sources": emission_factor_ds_set,
        "dqi": DataQualityIndicators(
            reference_period=ReferencePeriod(start=DateTime.now(), end=DateTime.now()),
            coverage_percent=50.0,
            technological_dqr=DataQualityRating(3),
            temporal_dqr=DataQualityRating(3),
            geographical_dqr=DataQualityRating(3),
            completeness_dqr=DataQualityRating(3),
            reliability_dqr=DataQualityRating(3),
        ),
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
        "biogenic_accounting_methodology": BiogenicAccountingMethodology.GHGP
    }


@pytest.fixture
def carbon_footprint(valid_carbon_footprint_data):
    return CarbonFootprint(**valid_carbon_footprint_data)


@pytest.fixture
def valid_product_footprint_data(valid_carbon_footprint_data, carbon_footprint):
    company_ids = CompanyIdList([
        CompanyId("urn:pathfinder:company:customcode:buyer-assigned:acme-corp")
    ])
    product_ids = ProductIdList([
        ProductId("urn:pathfinder:product:customcode:buyer-assigned:acme-product")
    ])
    cpc_code_lookup = CPCCodeLookup()
    valid_cpc = cpc_code_lookup.lookup("0111")
    version = Version(1)

    validity_period = ValidityPeriod(reference_period_end=carbon_footprint.reference_period.end)
    extensions = [
        DataModelExtension(
            spec_version="2.0.0",
            data_schema="https://example.com/schema",
            data={"key": "value"},
        )
    ]

    return {
        "id": ProductFootprintId(),
        "version": version,
        "created": DateTime.now(),
        "updated": DateTime.now(),
        "status_info": ProductFootprintStatus(status=Status.ACTIVE, comment="This is a comment"),
        "validity_period": validity_period,
        "company_name": "Company Name",
        "company_ids": company_ids,
        "product_description": "Product Description",
        "product_ids": product_ids,
        "product_category_cpc": valid_cpc,
        "product_name_company": "Product Name Company",
        "comment": "This is a comment",
        "extensions": extensions,
        "pcf": CarbonFootprint(**valid_carbon_footprint_data),
        "preceding_pf_ids": [ProductFootprintId(), ProductFootprintId()],
    }


def test_product_footprint_initialization(valid_product_footprint_data):
    product_footprint = ProductFootprint(**valid_product_footprint_data)

    assert product_footprint.id == valid_product_footprint_data["id"]
    assert product_footprint.version == Version(1)
    assert isinstance(product_footprint.created, DateTime)
    assert isinstance(product_footprint.updated, DateTime)
    assert product_footprint.status == Status.ACTIVE
    assert product_footprint.status_comment == "This is a comment"
    assert isinstance(product_footprint.validity_period, ValidityPeriod)
    assert product_footprint.company_name == "Company Name"
    assert isinstance(product_footprint.company_ids, CompanyIdList)
    assert all(
        isinstance(company_id, CompanyId) for company_id in product_footprint.company_ids
    )
    assert product_footprint.product_description == "Product Description"
    assert isinstance(product_footprint.product_ids, ProductIdList)
    assert all(
        isinstance(product_id, ProductId) for product_id in product_footprint.product_ids
    )
    assert product_footprint.product_category_cpc == CPCCodeLookup().lookup("0111")
    assert product_footprint.product_name_company == "Product Name Company"
    assert product_footprint.comment == "This is a comment"
    assert isinstance(product_footprint.extensions, list)
    assert all(
        isinstance(ext, DataModelExtension) for ext in product_footprint.extensions
    )
    assert isinstance(product_footprint.pcf, CarbonFootprint)
    assert isinstance(product_footprint.preceding_pf_ids, list)
    assert all(
        isinstance(pf_id, ProductFootprintId) for pf_id in product_footprint.preceding_pf_ids
    )


def test_product_footprint_valid_id(valid_product_footprint_data):
    new_id = ProductFootprintId()
    product_footprint_data = {**valid_product_footprint_data, "id": new_id}
    product_footprint = ProductFootprint(**product_footprint_data)
    assert product_footprint.id == new_id


@pytest.mark.parametrize("id", [123, 1.0, "string", {}, []])
def test_product_footprint_id_invalid_value_error(valid_product_footprint_data, id):
    pf = ProductFootprint(**valid_product_footprint_data)
    with pytest.raises(ValueError, match="id must be an instance of ProductFootprintId or None"):
        pf.id = id


def test_product_footprint_spec_version(valid_product_footprint_data):
    product_footprint = ProductFootprint(**valid_product_footprint_data)
    assert product_footprint.spec_version == "2.2.0"


def test_product_footprint_invalid_spec_version(valid_product_footprint_data):
    invalid_product_footprint_data = {
        **valid_product_footprint_data,
        "spec_version": "1.0.0",
    }
    with pytest.raises(ValueError, match="Invalid spec version"):
        ProductFootprint(**invalid_product_footprint_data)


@pytest.mark.parametrize("version", [Version(1), Version(2), Version(3)])
def test_product_footprint_valid_version(valid_product_footprint_data, version):
    product_footprint_data = {**valid_product_footprint_data, "version": version}
    product_footprint = ProductFootprint(**product_footprint_data)
    assert product_footprint.version == version


@pytest.mark.parametrize("version", [1, "1", 1.0, datetime.now()])
def test_product_footprint_invalid_version(valid_product_footprint_data, version):
    product_footprint_data = {**valid_product_footprint_data, "version": version}
    with pytest.raises(ValueError, match="version must be an instance of Version"):
        ProductFootprint(**product_footprint_data)


@pytest.mark.parametrize("created", [DateTime.now()])
def test_product_footprint_valid_created(valid_product_footprint_data, created):
    product_footprint_data = {**valid_product_footprint_data, "created": created}
    product_footprint = ProductFootprint(**product_footprint_data)
    assert product_footprint.created == created


@pytest.mark.parametrize("created", [1, "1", 1.0, datetime.now()])
def test_product_footprint_invalid_created(valid_product_footprint_data, created):
    product_footprint_data = {**valid_product_footprint_data, "created": created}
    with pytest.raises(ValueError, match="created must be an instance of DateTime"):
        ProductFootprint(**product_footprint_data)


@pytest.mark.parametrize("updated", [DateTime.now(), None])
def test_product_footprint_valid_updated(valid_product_footprint_data, updated):
    product_footprint_data = {**valid_product_footprint_data, "updated": updated}
    product_footprint = ProductFootprint(**product_footprint_data)
    assert product_footprint.updated == updated


@pytest.mark.parametrize(
    "updated", ["2022-01-01", datetime.now(), 1643723400, 1.0]
)
def test_product_footprint_invalid_updated(valid_product_footprint_data, updated):
    product_footprint_data = {**valid_product_footprint_data, "updated": updated}
    with pytest.raises(ValueError, match="updated must be an instance of DateTime"):
        ProductFootprint(**product_footprint_data)


def test_product_footprint_status_info(valid_product_footprint_data):
    product_footprint = ProductFootprint(**valid_product_footprint_data)
    assert isinstance(product_footprint.status_info, ProductFootprintStatus)


@pytest.mark.parametrize("status_info", [123, 1.0, "string", {}, []])
def test_product_footprint_status_info_invalid_value_error(valid_product_footprint_data, status_info):
    pf = ProductFootprint(**valid_product_footprint_data)
    with pytest.raises(ValueError, match="status_info must be an instance of ProductFootprintStatus"):
        pf.status_info = status_info


@pytest.mark.parametrize(
    "status", [Status.ACTIVE, Status.DEPRECATED]
)
def test_product_footprint_valid_status(valid_product_footprint_data, status):
    product_footprint_data = {**valid_product_footprint_data, "status_info": ProductFootprintStatus(status=status, comment="This is a comment")}
    product_footprint = ProductFootprint(**product_footprint_data)
    assert product_footprint.status == status


@pytest.mark.parametrize("status", ["Active", "Deprecated", 1, 1.0, datetime.now()])
def test_product_footprint_invalid_status(valid_product_footprint_data, status):
    pf = ProductFootprint(**valid_product_footprint_data)
    with pytest.raises(
        ValueError, match="status must be an instance of Status"
    ):
        pf.status = status


@pytest.mark.parametrize("status_comment", ["This is a comment", "Another comment", None])
def test_product_footprint_valid_status_comment(
    valid_product_footprint_data, status_comment
):
    pf = ProductFootprint(**valid_product_footprint_data)
    pf.status_comment = status_comment
    assert pf.status_comment == status_comment


@pytest.mark.parametrize("status_comment", [1, 1.0, datetime.now()])
def test_product_footprint_invalid_status_comment(
    valid_product_footprint_data, status_comment
):
    pf = ProductFootprint(**valid_product_footprint_data)
    with pytest.raises(ValueError, match="comment must be a string or None"):
        pf.status_comment = status_comment


@pytest.mark.parametrize("company_name", [123, 1.0, None, [], {}, ""])
def test_product_footprint_invalid_company_name(
    valid_product_footprint_data, company_name
):
    invalid_product_footprint_data = {
        **valid_product_footprint_data,
        "company_name": company_name,
    }
    with pytest.raises(ValueError, match="company_name must be a non-empty string"):
        ProductFootprint(**invalid_product_footprint_data)


def test_product_footprint_company_name(valid_product_footprint_data):
    product_footprint = ProductFootprint(**valid_product_footprint_data)
    assert product_footprint.company_name == "Company Name"


@pytest.mark.parametrize(
    "company_ids",
    [
        CompanyIdList([
            CompanyId("urn:pathfinder:company:customcode:buyer-assigned:acme-corp")
        ]),  # list with a single item
        CompanyIdList([
            CompanyId("urn:pathfinder:company:customcode:buyer-assigned:acme-corp"),
            CompanyId("urn:pathfinder:company:customcode:buyer-assigned:acme-corp2"),
        ]),  # list with multiple items
    ],
)
def test_product_footprint_company_ids(valid_product_footprint_data, company_ids):
    product_footprint_data = {
        **valid_product_footprint_data,
        "company_ids": company_ids,
    }
    product_footprint = ProductFootprint(**product_footprint_data)
    assert isinstance(product_footprint.company_ids, CompanyIdList)
    assert len(product_footprint.company_ids) == len(company_ids)
    for company_id in product_footprint.company_ids:
        assert isinstance(company_id, CompanyId)


@pytest.mark.parametrize(
    "company_ids",
    [
        123,
        1.0,
        None,
        "string",
        {},
        CompanyId("urn:pathfinder:company:customcode:buyer-assigned:acme-corp"),
        [CompanyId("urn:pathfinder:company:customcode:buyer-assigned:acme-corp")],
    ],
)
def test_product_footprint_invalid_company_ids(
    valid_product_footprint_data, company_ids
):
    invalid_product_footprint_data = {
        **valid_product_footprint_data,
        "company_ids": company_ids,
    }
    with pytest.raises(ValueError, match="company_ids must be an instance of CompanyIdList"):
        ProductFootprint(**invalid_product_footprint_data)


@pytest.mark.parametrize("product_description", [123, 1.0, None, [], {}, ""])
def test_product_footprint_invalid_product_description(
    valid_product_footprint_data, product_description
):
    invalid_product_footprint_data = {
        **valid_product_footprint_data,
        "product_description": product_description,
    }
    with pytest.raises(
        ValueError, match="product_description must be a non-empty string"
    ):
        ProductFootprint(**invalid_product_footprint_data)


def test_product_footprint_product_description(valid_product_footprint_data):
    product_footprint = ProductFootprint(**valid_product_footprint_data)
    assert product_footprint.product_description == "Product Description"


@pytest.mark.parametrize(
    "product_ids",
    [
        ProductIdList([
            ProductId("urn:pathfinder:product:customcode:buyer-assigned:acme-product")
        ]),  # list with a single item
        ProductIdList([
            ProductId("urn:pathfinder:product:customcode:buyer-assigned:acme-product"),
            ProductId("urn:pathfinder:product:customcode:buyer-assigned:acme-product2"),
        ]),  # list with multiple items
    ],
)
def test_product_footprint_product_ids(valid_product_footprint_data, product_ids):
    product_footprint_data = {
        **valid_product_footprint_data,
        "product_ids": product_ids,
    }
    product_footprint = ProductFootprint(**product_footprint_data)
    assert isinstance(product_footprint.product_ids, ProductIdList)
    assert len(product_footprint.product_ids) == len(product_ids)
    for product_id in product_footprint.product_ids:
        assert isinstance(product_id, ProductId)

def test_product_footprint_product_ids_invalid_value_error(valid_product_footprint_data):
    product_footprint = ProductFootprint(**valid_product_footprint_data)
    with pytest.raises(ValueError, match="product_ids must be an instance of ProductIdList"):
        product_footprint.product_ids = "string"


def test_product_footprint_product_category_cpc(valid_product_footprint_data):
    product_footprint = ProductFootprint(**valid_product_footprint_data)
    assert isinstance(product_footprint.product_category_cpc, CPC)


@pytest.mark.parametrize("product_category_cpc", [123, 1.0, None, "string", {}, []])
def test_product_footprint_invalid_product_category_cpc(
    valid_product_footprint_data, product_category_cpc
):
    invalid_product_footprint_data = {
        **valid_product_footprint_data,
        "product_category_cpc": product_category_cpc,
    }
    with pytest.raises(
        ValueError, match="product_category_cpc must be an instance of CPC"
    ):
        ProductFootprint(**invalid_product_footprint_data)


@pytest.mark.parametrize("product_name_company", [123, 1.0, None, [], {}, ""])
def test_product_footprint_invalid_product_name_company(
    valid_product_footprint_data, product_name_company
):
    invalid_product_footprint_data = {
        **valid_product_footprint_data,
        "product_name_company": product_name_company,
    }
    with pytest.raises(
        ValueError, match="product_name_company must be a non-empty string"
    ):
        ProductFootprint(**invalid_product_footprint_data)


def test_product_footprint_product_name_company(valid_product_footprint_data):
    product_footprint = ProductFootprint(**valid_product_footprint_data)
    assert product_footprint.product_name_company == "Product Name Company"


def test_product_footprint_comment(valid_product_footprint_data):
    product_footprint = ProductFootprint(**valid_product_footprint_data)
    assert isinstance(product_footprint.comment, str)


@pytest.mark.parametrize("comment", [123, 1.0, None, {}, []])
def test_product_footprint_invalid_comment(valid_product_footprint_data, comment):
    invalid_product_footprint_data = {
        **valid_product_footprint_data,
        "comment": comment,
    }
    with pytest.raises(ValueError, match="comment must be a string"):
        ProductFootprint(**invalid_product_footprint_data)


def test_product_footprint_extensions(valid_product_footprint_data):
    product_footprint = ProductFootprint(**valid_product_footprint_data)
    assert isinstance(product_footprint.extensions, list)
    assert all(
        isinstance(ext, DataModelExtension) for ext in product_footprint.extensions
    )


@pytest.mark.parametrize("extensions", [123, 1.0, "string", {}])
def test_product_footprint_invalid_extensions(valid_product_footprint_data, extensions):
    invalid_product_footprint_data = {
        **valid_product_footprint_data,
        "extensions": extensions,
    }
    with pytest.raises(
        ValueError, match="extensions must be a list of DataModelExtension objects"
    ):
        ProductFootprint(**invalid_product_footprint_data)


def test_product_footprint_pcf(valid_product_footprint_data):
    product_footprint = ProductFootprint(**valid_product_footprint_data)
    assert isinstance(product_footprint.pcf, CarbonFootprint)


@pytest.mark.parametrize("pcf", [123, 1.0, None, "string", {}, []])
def test_product_footprint_invalid_pcf(valid_product_footprint_data, pcf):
    invalid_product_footprint_data = {**valid_product_footprint_data, "pcf": pcf}
    with pytest.raises(ValueError, match="pcf must be an instance of CarbonFootprint"):
        ProductFootprint(**invalid_product_footprint_data)


@pytest.mark.parametrize(
    "preceding_pf_ids",
    [
        [ProductFootprintId(), ProductFootprintId()],  # list with multiple items
        [],  # empty list
    ],
)
def test_product_footprint_preceding_pf_ids(valid_product_footprint_data, preceding_pf_ids):
    product_footprint_data = {
        **valid_product_footprint_data,
        "preceding_pf_ids": preceding_pf_ids,
    }
    product_footprint = ProductFootprint(**product_footprint_data)
    assert len(product_footprint.preceding_pf_ids) == len(preceding_pf_ids)
    for pf_id in product_footprint.preceding_pf_ids:
        assert isinstance(pf_id, ProductFootprintId)


@pytest.mark.parametrize(
    "preceding_pf_ids",
    [
        123,
        1.0,
        "string",
        {},
        ProductFootprintId(),
    ],
)
def test_product_footprint_invalid_preceding_pf_ids(valid_product_footprint_data, preceding_pf_ids):
    invalid_product_footprint_data = {
        **valid_product_footprint_data,
        "preceding_pf_ids": preceding_pf_ids,
    }
    with pytest.raises(ValueError, match="preceding_pf_ids must be a list of ProductFootprintId"):
        ProductFootprint(**invalid_product_footprint_data)


def test_product_footprint_duplicate_preceding_pf_ids(valid_product_footprint_data):
    pf_id = ProductFootprintId()
    preceding_pf_ids = [pf_id, pf_id]
    product_footprint_data = {
        **valid_product_footprint_data,
        "preceding_pf_ids": preceding_pf_ids,
    }
    with pytest.raises(ValueError, match="preceding_pf_ids must not contain duplicates"):
        ProductFootprint(**product_footprint_data)


def test_product_footprint_valid_validity_period(valid_product_footprint_data):
    validity_period = ValidityPeriod(
        start=DateTime("2022-01-01T00:00:00Z"), end=DateTime("2025-12-31T23:59:59Z")
    )
    product_footprint_data = {
        **valid_product_footprint_data,
        "validity_period": validity_period,
    }
    product_footprint = ProductFootprint(**product_footprint_data)
    assert product_footprint.validity_period == validity_period


def test_product_footprint_empty_validity_period(valid_product_footprint_data):
    product_footprint_data = {
        **valid_product_footprint_data,
        "validity_period": None,
    }
    product_footprint = ProductFootprint(**product_footprint_data)
    assert isinstance(product_footprint.validity_period, ValidityPeriod)


def test_product_footprint_default_reference_period(valid_product_footprint_data):
    product_footprint = ProductFootprint(**valid_product_footprint_data)
    # The start date of the validity period should be equal to the end date of the reference period.
    expected_start_date = product_footprint.pcf.reference_period.end
    assert DateTime.same_day(product_footprint.validity_period.start, expected_start_date)

    # The end date should be 3 years after the start date.
    expected_end_date = ValidityPeriod.three_years_from_end(product_footprint.validity_period.start)
    assert product_footprint.validity_period.end == expected_end_date


@pytest.mark.parametrize("validity_period", [123, 1.0, "string", {}, []])
def test_product_footprint_validity_period_invalid_value_error(valid_product_footprint_data, validity_period):
    pf = ProductFootprint(**valid_product_footprint_data)
    with pytest.raises(ValueError, match="validity_period must be an instance of ValidityPeriod or None"):
        pf.validity_period = validity_period


def test_product_footprint_str(valid_product_footprint_data):
    product_footprint = ProductFootprint(**valid_product_footprint_data)
    expected_str = (
        f"ProductFootprint(id={product_footprint.id}, spec_version={product_footprint.spec_version}, version={product_footprint.version}, "
        f"created={product_footprint.created}, updated={product_footprint.updated}, status={product_footprint.status}, status_comment='{product_footprint.status_comment}', "
        f"validity_period={product_footprint.validity_period}, company_name='{product_footprint.company_name}', company_ids={product_footprint.company_ids}, "
        f"product_description='{product_footprint.product_description}', product_ids={product_footprint.product_ids}, "
        f"product_category_cpc={product_footprint.product_category_cpc}, product_name_company='{product_footprint.product_name_company}', "
        f"comment='{product_footprint.comment}', extensions={product_footprint.extensions}, pcf={product_footprint.pcf}, preceding_pf_ids={product_footprint.preceding_pf_ids})"
    )
    assert str(product_footprint) == expected_str


def test_product_footprint_repr(valid_product_footprint_data):
    product_footprint = ProductFootprint(**valid_product_footprint_data)
    expected_repr = (
        f"ProductFootprint(id={product_footprint.id!r}, spec_version={product_footprint.spec_version!r}, version={product_footprint.version!r}, "
        f"created={product_footprint.created!r}, updated={product_footprint.updated!r}, status={product_footprint.status!r}, status_comment={product_footprint.status_comment!r}, "
        f"validity_period={product_footprint.validity_period!r}, company_name={product_footprint.company_name!r}, company_ids={product_footprint.company_ids!r}, "
        f"product_description={product_footprint.product_description!r}, product_ids={product_footprint.product_ids!r}, "
        f"product_category_cpc={product_footprint.product_category_cpc!r}, product_name_company={product_footprint.product_name_company!r}, "
        f"comment={product_footprint.comment!r}, extensions={product_footprint.extensions!r}, pcf={product_footprint.pcf!r}, preceding_pf_ids={product_footprint.preceding_pf_ids!r})"
    )
    assert repr(product_footprint) == expected_repr


def test_product_footprint_eq(valid_product_footprint_data):
    product_footprint1 = ProductFootprint(**valid_product_footprint_data)
    product_footprint2 = ProductFootprint(**valid_product_footprint_data)
    assert product_footprint1 == product_footprint2


def test_product_footprint_ne(valid_product_footprint_data):
    product_footprint1 = ProductFootprint(**valid_product_footprint_data)
    product_footprint2 = ProductFootprint(**{**valid_product_footprint_data, "company_name": "Different Company Name"})
    assert product_footprint1 != product_footprint2
