import pytest

from pact_methodology.exceptions import DuplicateIdError
from pact_methodology.urn import ProductId
from pact_methodology.product_footprint.product_id_list import ProductIdList


def test_product_id_list_valid_product_ids():
    product_ids = [
        ProductId("urn:pathfinder:product:customcode:buyer-assigned:acme-product")
    ]
    product_id_list = ProductIdList(product_ids)
    assert len(product_id_list) == 1
    assert isinstance(product_id_list.product_ids[0], ProductId)


@pytest.mark.parametrize(
    "product_ids",
    [
        123,
        1.0,
        None,
        "string",
        {},
        ProductId("urn:pathfinder:product:customcode:buyer-assigned:acme-product"),
    ],
)
def test_product_id_list_invalid_product_ids(product_ids):
    with pytest.raises(ValueError, match="product_ids must be a list of ProductId"):
        ProductIdList(product_ids)


@pytest.mark.parametrize(
    "product_ids",
    [
        ["string"],  # list with a single invalid item
        [
            ProductId("urn:pathfinder:product:customcode:buyer-assigned:acme-product"),
            "string",
        ],  # list with a mix of valid and invalid items
        [1, 2, 3],  # list with invalid items of a different type
        [
            ProductId("urn:pathfinder:product:customcode:buyer-assigned:acme-product"),
            ProductId("urn:pathfinder:product:customcode:buyer-assigned:acme-product"),
            "string",
        ],  # list with multiple valid items and an invalid item
    ],
)
def test_product_id_list_invalid_product_ids_list(product_ids):
    with pytest.raises(ValueError, match="product_ids must be a list of ProductId"):
        ProductIdList(product_ids)


def test_product_id_list_duplicate_product_ids():
    product_ids = [
        ProductId("urn:pathfinder:product:customcode:buyer-assigned:acme-product"),
        ProductId("urn:pathfinder:product:customcode:buyer-assigned:acme-product"),
    ]
    with pytest.raises(DuplicateIdError, match="Duplicate product_ids are not allowed"):
        ProductIdList(product_ids)


def test_product_id_list_append_valid_product_id():
    product_ids = [
        ProductId("urn:pathfinder:product:customcode:buyer-assigned:acme-product")
    ]
    product_id_list = ProductIdList(product_ids)
    new_product_id = ProductId(
        "urn:pathfinder:product:customcode:buyer-assigned:acme-product2"
    )
    product_id_list.append(new_product_id)
    assert len(product_id_list) == 2
    assert product_id_list.product_ids[1] == new_product_id


def test_product_id_list_append_invalid_product_id():
    product_ids = [
        ProductId("urn:pathfinder:product:customcode:buyer-assigned:acme-product")
    ]
    product_id_list = ProductIdList(product_ids)
    with pytest.raises(ValueError, match="product_id must be an instance of ProductId"):
        product_id_list.append("string")


def test_product_id_list_append_duplicate_product_id():
    product_ids = [
        ProductId("urn:pathfinder:product:customcode:buyer-assigned:acme-product")
    ]
    product_id_list = ProductIdList(product_ids)
    with pytest.raises(DuplicateIdError, match="Duplicate product_ids are not allowed"):
        product_id_list.append(product_ids[0])


def test_product_id_list_insert_duplicate_product_id():
    product_ids = [
        ProductId("urn:pathfinder:product:customcode:buyer-assigned:acme-product")
    ]
    product_id_list = ProductIdList(product_ids)
    with pytest.raises(DuplicateIdError, match="Duplicate product_ids are not allowed"):
        product_id_list.insert(0, product_ids[0])


def test_product_id_list_insert_invalid_product_id():
    product_ids = [
        ProductId("urn:pathfinder:product:customcode:buyer-assigned:acme-product")
    ]
    product_id_list = ProductIdList(product_ids)
    with pytest.raises(ValueError, match="product_id must be an instance of ProductId"):
        product_id_list.insert(0, "string")


def test_product_id_list_remove_valid_product_id():
    product_ids = [
        ProductId("urn:pathfinder:product:customcode:buyer-assigned:acme-product")
    ]
    product_id_list = ProductIdList(product_ids)
    product_id_list.remove(product_ids[0])
    assert len(product_id_list) == 0


def test_product_id_list_remove_invalid_product_id():
    product_ids = [
        ProductId("urn:pathfinder:product:customcode:buyer-assigned:acme-product")
    ]
    product_id_list = ProductIdList(product_ids)
    with pytest.raises(ValueError, match="product_id is not in the list"):
        product_id_list.remove(
            ProductId("urn:pathfinder:product:customcode:buyer-assigned:acme-product2")
        )
