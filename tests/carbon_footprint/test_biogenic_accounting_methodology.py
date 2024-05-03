import pytest

from pathfinder_framework.carbon_footprint.biogenic_accounting_methodology import BiogenicAccountingMethodology


def test_biogenic_accounting_methodology_values():
    assert BiogenicAccountingMethodology.PEF.value == 'PEF'
    assert BiogenicAccountingMethodology.ISO.value == 'ISO'
    assert BiogenicAccountingMethodology.GHGP.value == 'GHGP'
    assert BiogenicAccountingMethodology.QUANTIS.value == 'Quantis'

    with pytest.raises(AttributeError):
        assert BiogenicAccountingMethodology.Invalid
