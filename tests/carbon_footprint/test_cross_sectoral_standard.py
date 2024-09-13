from pact_methodology.carbon_footprint.cross_sectoral_standard import (
    CrossSectoralStandard,
)


def test_cross_sectoral_standard_values():
    assert CrossSectoralStandard.GHG_PROTOCOL == "GHG Protocol Product standard"
    assert CrossSectoralStandard.ISO_14067 == "ISO Standard 14067"
    assert CrossSectoralStandard.ISO_14044 == "ISO Standard 14044"
