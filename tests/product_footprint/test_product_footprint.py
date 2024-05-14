import pytest

from datetime import datetime

from pathfinder_framework.product_footprint.id import ProductFootprintId
from pathfinder_framework.product_footprint.product_footprint import ProductFootprint
from pathfinder_framework.product_footprint.status import ProductFootprintStatus
from pathfinder_framework.urn import CompanyId, ProductId
from pathfinder_framework.product_footprint.cpc import CPCCodeLookup, CPC


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


def test_product_footprint_initialization(company_ids, product_ids, valid_cpc):
    """Tests that a ProductFootprint instance can be initialized with all required attributes."""
    product_footprint_id = ProductFootprintId()
    product_footprint = ProductFootprint(
        id=product_footprint_id,
        version=1,
        created=datetime.now(),
        updated=datetime.now(),
        status=ProductFootprintStatus.ACTIVE,
        status_comment="This is a comment",
        validity_period_start=datetime.now(),
        validity_period_end=datetime.now(),
        company_name="Company Name",
        company_ids=company_ids,
        product_description="Product Description",
        product_ids=product_ids,
        product_category_cpc=valid_cpc,
        product_name_company="Product Name Company",
        comment="This is a comment",
        extensions={"key": "value"}
    )
    assert product_footprint.id == product_footprint_id
    assert product_footprint.version == 1
    assert isinstance(product_footprint.created, datetime)
    assert isinstance(product_footprint.updated, datetime)
    assert product_footprint.status == ProductFootprintStatus.ACTIVE
    assert product_footprint.status_comment == "This is a comment"
    assert isinstance(product_footprint.validity_period_start, datetime)
    assert isinstance(product_footprint.validity_period_end, datetime)
    assert product_footprint.company_name == "Company Name"
    assert product_footprint.company_ids == company_ids
    assert product_footprint.product_description == "Product Description"
    assert product_footprint.product_ids == product_ids
    assert product_footprint.product_category_cpc == valid_cpc
    assert product_footprint.product_name_company == "Product Name Company"
    assert product_footprint.comment == "This is a comment"
    assert product_footprint.extensions == {"key": "value"}


def test_product_footprint_default_initialization(company_ids, product_ids, valid_cpc):
    """Tests that a ProductFootprint instance initializes with default values for optional attributes."""
    product_footprint = ProductFootprint(
        version=1,
        created=datetime.now(),
        updated=datetime.now(),
        status=ProductFootprintStatus.ACTIVE,
        status_comment="This is a comment",
        validity_period_start=datetime.now(),
        validity_period_end=datetime.now(),
        company_name="Company Name",
        company_ids=company_ids,
        product_description="Product Description",
        product_ids=product_ids,
        product_category_cpc=valid_cpc,
        product_name_company="Product Name Company",
        comment="This is a comment",
        extensions={"key": "value"}
    )
    assert isinstance(product_footprint.id, ProductFootprintId)


def test_product_footprint_spec_version(company_ids, product_ids, valid_cpc):
    """Tests that a ProductFootprint instance has a specVersion attribute."""
    product_footprint = ProductFootprint(
        version=1,
        created=datetime.now(),
        updated=datetime.now(),
        status=ProductFootprintStatus.ACTIVE,
        status_comment="This is a comment",
        validity_period_start=datetime.now(),
        validity_period_end=datetime.now(),
        company_name="Company Name",
        company_ids=company_ids,
        product_description="Product Description",
        product_ids=product_ids,
        product_category_cpc=valid_cpc,
        product_name_company="Product Name Company",
        comment="This is a comment",
        extensions={"key": "value"}
    )
    assert product_footprint.spec_version == "2.0.0"


def test_product_footprint_repr(company_ids, product_ids, valid_cpc):
    """Tests that the __repr__ method returns the expected string representation."""
    product_footprint_id = ProductFootprintId()
    product_footprint = ProductFootprint(
        id=product_footprint_id,
        version=1,
        created=datetime.now(),
        updated=datetime.now(),
        status=ProductFootprintStatus.ACTIVE,
        status_comment="This is a comment",
        validity_period_start=datetime.now(),
        validity_period_end=datetime.now(),
        company_name="Company Name",
        company_ids=company_ids,
        product_description="Product Description",
        product_ids=product_ids,
        product_category_cpc=valid_cpc,
        product_name_company="Product Name Company",
        comment="This is a comment",
        extensions={"key": "value"}
    )
    expected_repr = f"ProductFootprint(id={product_footprint_id})"
    assert repr(product_footprint) == expected_repr