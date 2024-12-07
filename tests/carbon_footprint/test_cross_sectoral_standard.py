from pact_methodology.carbon_footprint.cross_sectoral_standard import (
    CrossSectoralStandard,
)


def test_cross_sectoral_standard_values():
    assert CrossSectoralStandard.GHG_PROTOCOL == "GHG Protocol Product standard"
    assert CrossSectoralStandard.ISO_14067 == "ISO Standard 14067"
    assert CrossSectoralStandard.ISO_14044 == "ISO Standard 14044"

def test_cross_sectoral_standard_str():
    assert str(CrossSectoralStandard.GHG_PROTOCOL) == "GHG Protocol Product standard"
    assert str(CrossSectoralStandard.ISO_14067) == "ISO Standard 14067"
    assert str(CrossSectoralStandard.ISO_14044) == "ISO Standard 14044"

def test_cross_sectoral_standard_repr():
    assert repr(CrossSectoralStandard.GHG_PROTOCOL) == "CrossSectoralStandard.GHG_PROTOCOL"
    assert repr(CrossSectoralStandard.ISO_14067) == "CrossSectoralStandard.ISO_14067"
    assert repr(CrossSectoralStandard.ISO_14044) == "CrossSectoralStandard.ISO_14044"
