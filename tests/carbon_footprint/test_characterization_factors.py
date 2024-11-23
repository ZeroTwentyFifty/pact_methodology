import pytest

from pact_methodology.carbon_footprint.characterization_factors import (
    CharacterizationFactors,
)


def test_characterization_factors_values():
    assert CharacterizationFactors.AR5 == "AR5"
    assert CharacterizationFactors.AR6 == "AR6"

    with pytest.raises(AttributeError):
        assert CharacterizationFactors.Invalid


def test_characterization_factors_str():
    assert str(CharacterizationFactors.AR5) == "AR5"
    assert str(CharacterizationFactors.AR6) == "AR6"


def test_characterization_factors_repr():
    assert repr(CharacterizationFactors.AR5) == "CharacterizationFactors.AR5"
    assert repr(CharacterizationFactors.AR6) == "CharacterizationFactors.AR6"
