import pytest
from pact_methodology.carbon_footprint.emission_factor_ds import EmissionFactorDS
from pact_methodology.carbon_footprint.emission_factor_ds_set import EmissionFactorDSSet
from pact_methodology.exceptions import DuplicateIdError

@pytest.fixture
def valid_ds():
    return EmissionFactorDS(
        name="ecoinvent",
        version="3.9.1"
    )

@pytest.fixture
def valid_ds2():
    return EmissionFactorDS(
        name="gabi",
        version="2023.1"
    )

def test_emission_factor_ds_set_exists():
    assert EmissionFactorDSSet is not None

def test_empty_initialization():
    ds_set = EmissionFactorDSSet()
    assert ds_set.emission_factor_ds_list == []

def test_initialization_with_ds(valid_ds):
    ds_set = EmissionFactorDSSet([valid_ds])
    assert len(ds_set.emission_factor_ds_list) == 1
    assert ds_set.emission_factor_ds_list[0] == valid_ds

def test_initialization_with_invalid_ds():
    with pytest.raises(ValueError) as excinfo:
        EmissionFactorDSSet([1, 2, 3])
    assert str(excinfo.value) == "emission_factor_ds_list must be a list of EmissionFactorDS objects"

def test_add_ds(valid_ds, valid_ds2):
    ds_set = EmissionFactorDSSet([valid_ds])
    ds_set.add_ds(valid_ds2)
    assert len(ds_set.emission_factor_ds_list) == 2
    assert ds_set.emission_factor_ds_list[1] == valid_ds2

def test_add_invalid_ds(valid_ds):
    ds_set = EmissionFactorDSSet([valid_ds])
    with pytest.raises(ValueError) as excinfo:
        ds_set.add_ds("invalid")
    assert str(excinfo.value) == "ds must be an instance of EmissionFactorDS"

def test_add_duplicate_ds(valid_ds):
    ds_set = EmissionFactorDSSet([valid_ds])
    duplicate_ds = EmissionFactorDS(name="ecoinvent", version="3.9.1")
    with pytest.raises(DuplicateIdError) as excinfo:
        ds_set.add_ds(duplicate_ds)
    assert str(excinfo.value) == "duplicate emission factor database reference"

def test_remove_ds(valid_ds, valid_ds2):
    ds_set = EmissionFactorDSSet([valid_ds, valid_ds2])
    ds_set.remove_ds(valid_ds)
    assert len(ds_set.emission_factor_ds_list) == 1
    assert ds_set.emission_factor_ds_list[0] == valid_ds2

def test_remove_nonexistent_ds(valid_ds, valid_ds2):
    ds_set = EmissionFactorDSSet([valid_ds])
    with pytest.raises(ValueError) as excinfo:
        ds_set.remove_ds(valid_ds2)
    assert str(excinfo.value) == "reference not found in the set"

def test_remove_invalid_ds(valid_ds):
    ds_set = EmissionFactorDSSet([valid_ds])
    with pytest.raises(ValueError) as excinfo:
        ds_set.remove_ds("invalid")
    assert str(excinfo.value) == "ds must be an instance of EmissionFactorDS"

def test_to_dict(valid_ds, valid_ds2):
    ds_set = EmissionFactorDSSet([valid_ds, valid_ds2])
    dict_output = ds_set.to_dict()
    assert len(dict_output) == 2
    expected_dict_0 = {
        'name': 'ecoinvent',
        'version': '3.9.1'
    }
    expected_dict_1 = {
        'name': 'gabi',
        'version': '2023.1'
    }
    assert dict_output[0] == expected_dict_0
    assert dict_output[1] == expected_dict_1

def test_str_representation(valid_ds):
    ds_set = EmissionFactorDSSet([valid_ds])
    expected_str = "EmissionFactorDSSet(emission_factor_ds_list=[EmissionFactorDS(name='ecoinvent', version='3.9.1')])"
    assert str(ds_set) == expected_str

def test_repr_representation(valid_ds):
    ds_set = EmissionFactorDSSet([valid_ds])
    expected_repr = "EmissionFactorDSSet(emission_factor_ds_list=[EmissionFactorDS(name='ecoinvent', version='3.9.1')])"
    assert repr(ds_set) == expected_repr

def test_equality(valid_ds, valid_ds2):
    ds_set1 = EmissionFactorDSSet([valid_ds, valid_ds2])
    ds_set2 = EmissionFactorDSSet([valid_ds, valid_ds2])
    assert ds_set1 == ds_set2

def test_inequality(valid_ds, valid_ds2):
    ds_set1 = EmissionFactorDSSet([valid_ds])
    ds_set2 = EmissionFactorDSSet([valid_ds2])
    assert ds_set1 != ds_set2

def test_inequality_with_different_type(valid_ds):
    ds_set = EmissionFactorDSSet([valid_ds])
    assert ds_set != "not a ds set"

def test_multiple_ds_types(valid_ds, valid_ds2):
    ds_set = EmissionFactorDSSet([valid_ds])
    ds_set.add_ds(valid_ds2)
    assert len(ds_set.emission_factor_ds_list) == 2
    assert ds_set.emission_factor_ds_list[0].name == "ecoinvent"
    assert ds_set.emission_factor_ds_list[0].version == "3.9.1"
    assert ds_set.emission_factor_ds_list[1].name == "gabi"
    assert ds_set.emission_factor_ds_list[1].version == "2023.1"
