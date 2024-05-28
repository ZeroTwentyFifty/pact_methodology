import pytest

from pathfinder_framework.data_model_extension.data_model_extension import DataModelExtension


@pytest.fixture
def valid_data_model_extension():
    return {
        "spec_version": "2.0.0",
        "data_schema": "https://catalog.carbon-transparency.com/shipment/1.0.0/schema.json",
        "data": {"shipmentId": "S1234567890", "consignmentId": "Cabc.def-ghi"},
        "documentation": "https://catalog.carbon-transparency.com/shipment/1.0.0/documentation.html"
    }


def test_data_model_extension_init_valid_spec_version(valid_data_model_extension):
    data_model_extension = DataModelExtension(**valid_data_model_extension)
    assert data_model_extension.spec_version == "2.0.0"


def test_data_model_extension_init_invalid_spec_version_major(valid_data_model_extension):
    invalid_data_model_extension = {**valid_data_model_extension, "spec_version": "1.0.0"}
    with pytest.raises(ValueError, match="Invalid spec version"):
        DataModelExtension(**invalid_data_model_extension)


@pytest.mark.parametrize("spec_version", ["2.1.0", "2.0.1", "invalid"])
def test_data_model_extension_init_invalid_spec_version(valid_data_model_extension, spec_version):
    invalid_data = {**valid_data_model_extension, "spec_version": spec_version}
    with pytest.raises(ValueError, match="Invalid spec version"):
        DataModelExtension(**invalid_data)


def test_data_model_extension_init_valid_data_schema(valid_data_model_extension):
    data_model_extension = DataModelExtension(**valid_data_model_extension)
    assert data_model_extension.data_schema == "https://catalog.carbon-transparency.com/shipment/1.0.0/schema.json"


def test_data_model_extension_init_invalid_data_schema_scheme(valid_data_model_extension):
    invalid_data = {**valid_data_model_extension, "data_schema": "http://catalog.carbon-transparency.com/shipment/1.0.0/schema.json"}
    with pytest.raises(ValueError, match="Invalid data schema URL scheme"):
        DataModelExtension(**invalid_data)


def test_data_model_extension_init_invalid_data_schema_netloc(valid_data_model_extension):
    invalid_data = {**valid_data_model_extension, "data_schema": "https:///shipment/1.0.0/schema.json"}
    with pytest.raises(ValueError, match="Invalid data schema URL"):
        DataModelExtension(**invalid_data)


def test_data_model_extension_init_valid_data(valid_data_model_extension):
    data_model_extension = DataModelExtension(**valid_data_model_extension)
    assert data_model_extension.data == {"shipmentId": "S1234567890", "consignmentId": "Cabc.def-ghi"}


def test_data_model_extension_init_invalid_data_type(valid_data_model_extension):
    invalid_data = {**valid_data_model_extension, "data": "Invalid data type"}
    with pytest.raises(ValueError, match="Invalid data type"):
        DataModelExtension(**invalid_data)


def test_data_model_extension_init_invalid_data_format(valid_data_model_extension):
    invalid_data = {**valid_data_model_extension, "data": {"Invalid": object()}}
    with pytest.raises(ValueError, match="Invalid data format"):
        DataModelExtension(**invalid_data)


def test_data_model_extension_init_valid_documentation(valid_data_model_extension):
    data_model_extension = DataModelExtension(**valid_data_model_extension)
    assert data_model_extension.documentation == "https://catalog.carbon-transparency.com/shipment/1.0.0/documentation.html"


def test_data_model_extension_init_invalid_documentation_scheme(valid_data_model_extension):
    invalid_data = {**valid_data_model_extension, "documentation": "http://catalog.carbon-transparency.com/shipment/1.0.0/documentation.html"}
    with pytest.raises(ValueError, match="Invalid documentation URL scheme"):
        DataModelExtension(**invalid_data)


def test_data_model_extension_init_invalid_documentation_netloc(valid_data_model_extension):
    invalid_data = {**valid_data_model_extension, "documentation": "https:///shipment/1.0.0/documentation.html"}
    with pytest.raises(ValueError, match="Invalid documentation URL"):
        DataModelExtension(**invalid_data)
