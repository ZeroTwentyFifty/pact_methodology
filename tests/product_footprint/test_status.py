from pact_methodology.product_footprint.status import ProductFootprintStatus


def test_product_footprint_status_values():
    assert ProductFootprintStatus.ACTIVE.value == "Active"
    assert ProductFootprintStatus.DEPRECATED.value == "Deprecated"
