import pytest

from pathfinder_framework.product_footprint.product_footprint import ProductFootprint
from pathfinder_framework.product_footprint.id import ProductFootprintId


def test_product_footprint_id_initialization():
    """Tests that a ProductFootprint instance can be initialized with a ProductFootprintId."""
    product_footprint_id = ProductFootprintId()
    product_footprint = ProductFootprint(id=product_footprint_id)
    assert product_footprint.id == product_footprint_id


def test_product_footprint_id_default_initialization():
    """Tests that a ProductFootprint instance initializes a ProductFootprintId by default."""
    product_footprint = ProductFootprint()
    assert isinstance(product_footprint.id, ProductFootprintId)


def test_product_footprint_spec_version():
    """Tests that a ProductFootprint instance has a specVersion attribute."""
    product_footprint = ProductFootprint()
    assert product_footprint.spec_version == "2.0.0"


def test_product_footprint_repr():
    """Tests that the __repr__ method returns the expected string representation."""
    product_footprint_id = ProductFootprintId()
    product_footprint = ProductFootprint(id=product_footprint_id)
    expected_repr = f"ProductFootprint(id={product_footprint_id})"
    assert repr(product_footprint) == expected_repr
