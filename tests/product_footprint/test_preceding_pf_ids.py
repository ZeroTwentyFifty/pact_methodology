import pytest
from pact_methodology.product_footprint.preceding_pf_ids import PrecedingPfIds
from pact_methodology.product_footprint.id import ProductFootprintId

def test_preceding_pf_ids_empty_initialization():
    pf_ids = PrecedingPfIds()
    assert len(pf_ids) == 0

def test_preceding_pf_ids_initialization_with_valid_list():
    pf_id1 = ProductFootprintId()
    pf_id2 = ProductFootprintId()
    pf_ids = PrecedingPfIds([pf_id1, pf_id2])
    assert len(pf_ids) == 2
    assert pf_id1 in pf_ids
    assert pf_id2 in pf_ids

def test_preceding_pf_ids_initialization_with_invalid_list():
    with pytest.raises(ValueError, match="All elements in pf_ids must be instances of ProductFootprintId"):
        PrecedingPfIds([ProductFootprintId(), "invalid_id"])

def test_preceding_pf_ids_initialization_with_duplicates():
    pf_id = ProductFootprintId()
    with pytest.raises(ValueError, match="pf_ids must not contain duplicates"):
        PrecedingPfIds([pf_id, pf_id])

def test_preceding_pf_ids_add_method():
    pf_id1 = ProductFootprintId()
    pf_id2 = ProductFootprintId()
    pf_ids = PrecedingPfIds([pf_id1])
    pf_ids.add(pf_id2)
    assert len(pf_ids) == 2
    assert pf_id1 in pf_ids
    assert pf_id2 in pf_ids

def test_preceding_pf_ids_add_duplicate_method():
    pf_id = ProductFootprintId()
    pf_ids = PrecedingPfIds([pf_id])
    with pytest.raises(ValueError, match="pf_id already exists in the collection"):
        pf_ids.add(pf_id)

def test_preceding_pf_ids_iter():
    pf_id1 = ProductFootprintId()
    pf_id2 = ProductFootprintId()
    pf_ids = PrecedingPfIds([pf_id1, pf_id2])
    iter_pf_ids = list(pf_ids)
    assert len(iter_pf_ids) == 2
    assert pf_id1 in iter_pf_ids
    assert pf_id2 in iter_pf_ids

def test_preceding_pf_ids_len():
    pf_id1 = ProductFootprintId()
    pf_id2 = ProductFootprintId()
    pf_ids = PrecedingPfIds([pf_id1, pf_id2])
    assert len(pf_ids) == 2

def test_preceding_pf_ids_repr():
    pf_id1 = ProductFootprintId()
    pf_id2 = ProductFootprintId()
    pf_ids = PrecedingPfIds([pf_id1, pf_id2])
    assert repr(pf_ids) == f"PrecedingPfIds([{pf_id1!r}, {pf_id2!r}])"