import pytest

from pathfinder_framework.carbon_footprint.characterization_factors import CharacterizationFactors


def test_characterization_factors_values():
    assert CharacterizationFactors.AR5 == 'AR5'
    assert CharacterizationFactors.AR6 == 'AR6'

    with pytest.raises(AttributeError):
        assert CharacterizationFactors.Invalid
