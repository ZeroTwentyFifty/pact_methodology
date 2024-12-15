import pytest
from pact_methodology.carbon_footprint.emission_factor_ds import EmissionFactorDS


@pytest.fixture
def valid_emission_factor_ds():
    return {
        "name": "ecoinvent",
        "version": "3.9.1"
    }


def test_emission_factor_ds_init_valid(valid_emission_factor_ds):
    ef_ds = EmissionFactorDS(**valid_emission_factor_ds)
    assert ef_ds.name == "ecoinvent"
    assert ef_ds.version == "3.9.1"


def test_emission_factor_ds_init_invalid_name():
    with pytest.raises(ValueError, match="name must be a non-empty string"):
        EmissionFactorDS(name="", version="3.9.1")
    
    with pytest.raises(ValueError, match="name must be a non-empty string"):
        EmissionFactorDS(name=123, version="3.9.1")


def test_emission_factor_ds_init_invalid_version():
    with pytest.raises(ValueError, match="version must be a non-empty string"):
        EmissionFactorDS(name="ecoinvent", version="")
    
    with pytest.raises(ValueError, match="version must be a non-empty string"):
        EmissionFactorDS(name="ecoinvent", version=123)


def test_emission_factor_ds_to_dict(valid_emission_factor_ds):
    ef_ds = EmissionFactorDS(**valid_emission_factor_ds)
    assert ef_ds.to_dict() == {
        "name": "ecoinvent",
        "version": "3.9.1"
    }


def test_emission_factor_ds_str(valid_emission_factor_ds):
    ef_ds = EmissionFactorDS(**valid_emission_factor_ds)
    expected_str = "name=ecoinvent, version=3.9.1"
    assert str(ef_ds) == expected_str


def test_emission_factor_ds_repr(valid_emission_factor_ds):
    ef_ds = EmissionFactorDS(**valid_emission_factor_ds)
    expected_repr = "EmissionFactorDS(name='ecoinvent', version='3.9.1')"
    assert repr(ef_ds) == expected_repr


def test_emission_factor_ds_eq(valid_emission_factor_ds):
    ef_ds1 = EmissionFactorDS(**valid_emission_factor_ds)
    ef_ds2 = EmissionFactorDS(**valid_emission_factor_ds)
    ef_ds3 = EmissionFactorDS(name="different", version="1.0.0")
    
    assert ef_ds1 == ef_ds2
    assert ef_ds1 != ef_ds3
    assert ef_ds1 != "not an EmissionFactorDS"


def test_emission_factor_ds_properties(valid_emission_factor_ds):
    ef_ds = EmissionFactorDS(**valid_emission_factor_ds)
    
    # Test name property
    with pytest.raises(ValueError, match="name must be a non-empty string"):
        ef_ds.name = ""
    with pytest.raises(ValueError, match="name must be a non-empty string"):
        ef_ds.name = 123
        
    # Test version property  
    with pytest.raises(ValueError, match="version must be a non-empty string"):
        ef_ds.version = ""
    with pytest.raises(ValueError, match="version must be a non-empty string"):
        ef_ds.version = 123
