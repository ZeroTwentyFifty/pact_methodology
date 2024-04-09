import uuid

import pytest

from pathfinder_framework.product_footprint.id import ProductFootprintId


def test_product_footprint_id_init():
    pf_id = ProductFootprintId()
    assert isinstance(pf_id, uuid.UUID)


def test_product_footprint_id_init_with_value():
    value = uuid.uuid4().hex
    pf_id = ProductFootprintId(value)
    assert pf_id.hex == value


def test_product_footprint_id_eq():
    pf_id1 = ProductFootprintId()
    pf_id2 = ProductFootprintId(pf_id1.hex)
    assert pf_id1 == pf_id2


def test_product_footprint_id_neq():
    pf_id1 = ProductFootprintId()
    pf_id2 = ProductFootprintId()
    assert pf_id1 != pf_id2


def test_product_footprint_id_version():
    pf_id = ProductFootprintId()
    assert pf_id.version == 4


def test_product_footprint_id_init_invalid_uuid():
    with pytest.raises(ValueError):
        ProductFootprintId('invalid-uuid-string')
