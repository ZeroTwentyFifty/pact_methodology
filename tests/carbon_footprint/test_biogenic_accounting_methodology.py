import pytest

from pact_methodology.carbon_footprint.biogenic_accounting_methodology import (
    BiogenicAccountingMethodology,
)


def test_biogenic_accounting_methodology_values():
    assert BiogenicAccountingMethodology.PEF.value == "PEF"
    assert BiogenicAccountingMethodology.ISO.value == "ISO"
    assert BiogenicAccountingMethodology.GHGP.value == "GHGP"
    assert BiogenicAccountingMethodology.QUANTIS.value == "Quantis"

    with pytest.raises(AttributeError):
        assert BiogenicAccountingMethodology.Invalid

def test_biogenic_accounting_methodology_str():
    assert str(BiogenicAccountingMethodology.PEF) == "PEF"
    assert str(BiogenicAccountingMethodology.ISO) == "ISO"
    assert str(BiogenicAccountingMethodology.GHGP) == "GHGP"
    assert str(BiogenicAccountingMethodology.QUANTIS) == "Quantis"

def test_biogenic_accounting_methodology_repr():
    assert repr(BiogenicAccountingMethodology.PEF) == "BiogenicAccountingMethodology.PEF"
    assert repr(BiogenicAccountingMethodology.ISO) == "BiogenicAccountingMethodology.ISO"
    assert repr(BiogenicAccountingMethodology.GHGP) == "BiogenicAccountingMethodology.GHGP"
    assert repr(BiogenicAccountingMethodology.QUANTIS) == "BiogenicAccountingMethodology.QUANTIS"
