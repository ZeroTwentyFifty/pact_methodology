import pytest

from pact_methodology.product_footprint.status import ProductFootprintStatus, Status



def test_product_footprint_status_values():
    assert Status.ACTIVE.value == "Active"
    assert Status.DEPRECATED.value == "Deprecated"


def test_product_footprint_status_info_initialization():
    status_info = ProductFootprintStatus(status=Status.ACTIVE, comment="Test comment")
    assert status_info.status == Status.ACTIVE
    assert status_info.comment == "Test comment"


def test_product_footprint_status_info_valid_status_update():
    status_info = ProductFootprintStatus(status=Status.ACTIVE)
    status_info.status = Status.DEPRECATED
    assert status_info.status == Status.DEPRECATED


def test_product_footprint_status_info_valid_comment_update():
    status_info = ProductFootprintStatus(status=Status.ACTIVE)
    status_info.comment = "New comment"
    assert status_info.comment == "New comment"


def test_product_footprint_status_info_invalid_status():
    status_info = ProductFootprintStatus(status=Status.ACTIVE)
    with pytest.raises(ValueError):
        status_info.status = "InvalidStatus"


def test_product_footprint_status_info_invalid_comment():
    status_info = ProductFootprintStatus(status=Status.ACTIVE)
    with pytest.raises(ValueError):
        status_info.comment = 123