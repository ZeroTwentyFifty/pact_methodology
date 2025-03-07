from pact_methodology.carbon_footprint.region_or_subregion import RegionOrSubregion


def test_region_or_subregion_values():
    assert RegionOrSubregion.AFRICA == "Africa"
    assert RegionOrSubregion.AMERICAS == "Americas"
    assert RegionOrSubregion.ASIA == "Asia"
    assert RegionOrSubregion.EUROPE == "Europe"
    assert RegionOrSubregion.OCEANIA == "Oceania"
    assert RegionOrSubregion.AUSTRALIA_AND_NEW_ZEALAND == "Australia and New Zealand"
    assert RegionOrSubregion.CENTRAL_ASIA == "Central Asia"
    assert RegionOrSubregion.EASTERN_ASIA == "Eastern Asia"
    assert RegionOrSubregion.EASTERN_EUROPE == "Eastern Europe"
    assert (
        RegionOrSubregion.LATIN_AMERICA_AND_THE_CARIBBEAN
        == "Latin America and the Caribbean"
    )
    assert RegionOrSubregion.MELANESIA == "Melanesia"
    assert RegionOrSubregion.MICRONESIA == "Micronesia"
    assert RegionOrSubregion.NORTHERN_AFRICA == "Northern Africa"
    assert RegionOrSubregion.NORTHERN_AMERICA == "Northern America"
    assert RegionOrSubregion.NORTHERN_EUROPE == "Northern Europe"
    assert RegionOrSubregion.POLYNESIA == "Polynesia"
    assert RegionOrSubregion.SOUTH_EASTERN_ASIA == "South-eastern Asia"
    assert RegionOrSubregion.SOUTHERN_ASIA == "Southern Asia"
    assert RegionOrSubregion.SOUTHERN_EUROPE == "Southern Europe"
    assert RegionOrSubregion.SUB_SAHARAN_AFRICA == "Sub-Saharan Africa"
    assert RegionOrSubregion.WESTERN_ASIA == "Western Asia"
    assert RegionOrSubregion.WESTERN_EUROPE == "Western Europe"

def test_region_or_subregion_str():
    assert str(RegionOrSubregion.AFRICA) == "Africa"
    assert str(RegionOrSubregion.AMERICAS) == "Americas"
    assert str(RegionOrSubregion.ASIA) == "Asia"
    assert str(RegionOrSubregion.EUROPE) == "Europe"
    assert str(RegionOrSubregion.OCEANIA) == "Oceania"
    assert str(RegionOrSubregion.AUSTRALIA_AND_NEW_ZEALAND) == "Australia and New Zealand"
    assert str(RegionOrSubregion.CENTRAL_ASIA) == "Central Asia"
    assert str(RegionOrSubregion.EASTERN_ASIA) == "Eastern Asia"
    assert str(RegionOrSubregion.EASTERN_EUROPE) == "Eastern Europe"
    assert str(RegionOrSubregion.LATIN_AMERICA_AND_THE_CARIBBEAN) == "Latin America and the Caribbean"
    assert str(RegionOrSubregion.MELANESIA) == "Melanesia"
    assert str(RegionOrSubregion.MICRONESIA) == "Micronesia"
    assert str(RegionOrSubregion.NORTHERN_AFRICA) == "Northern Africa"
    assert str(RegionOrSubregion.NORTHERN_AMERICA) == "Northern America"
    assert str(RegionOrSubregion.NORTHERN_EUROPE) == "Northern Europe"
    assert str(RegionOrSubregion.POLYNESIA) == "Polynesia"
    assert str(RegionOrSubregion.SOUTH_EASTERN_ASIA) == "South-eastern Asia"
    assert str(RegionOrSubregion.SOUTHERN_ASIA) == "Southern Asia"
    assert str(RegionOrSubregion.SOUTHERN_EUROPE) == "Southern Europe"
    assert str(RegionOrSubregion.SUB_SAHARAN_AFRICA) == "Sub-Saharan Africa"
    assert str(RegionOrSubregion.WESTERN_ASIA) == "Western Asia"
    assert str(RegionOrSubregion.WESTERN_EUROPE) == "Western Europe"


def test_region_or_subregion_repr():
    assert repr(RegionOrSubregion.AFRICA) == "RegionOrSubregion.AFRICA"
    assert repr(RegionOrSubregion.AMERICAS) == "RegionOrSubregion.AMERICAS"
    assert repr(RegionOrSubregion.ASIA) == "RegionOrSubregion.ASIA"
    assert repr(RegionOrSubregion.EUROPE) == "RegionOrSubregion.EUROPE"
    assert repr(RegionOrSubregion.OCEANIA) == "RegionOrSubregion.OCEANIA"
    assert repr(RegionOrSubregion.AUSTRALIA_AND_NEW_ZEALAND) == "RegionOrSubregion.AUSTRALIA_AND_NEW_ZEALAND"
    assert repr(RegionOrSubregion.CENTRAL_ASIA) == "RegionOrSubregion.CENTRAL_ASIA"
    assert repr(RegionOrSubregion.EASTERN_ASIA) == "RegionOrSubregion.EASTERN_ASIA"
    assert repr(RegionOrSubregion.EASTERN_EUROPE) == "RegionOrSubregion.EASTERN_EUROPE"
    assert repr(RegionOrSubregion.LATIN_AMERICA_AND_THE_CARIBBEAN) == "RegionOrSubregion.LATIN_AMERICA_AND_THE_CARIBBEAN"
    assert repr(RegionOrSubregion.MELANESIA) == "RegionOrSubregion.MELANESIA"
    assert repr(RegionOrSubregion.MICRONESIA) == "RegionOrSubregion.MICRONESIA"
    assert repr(RegionOrSubregion.NORTHERN_AFRICA) == "RegionOrSubregion.NORTHERN_AFRICA"
    assert repr(RegionOrSubregion.NORTHERN_AMERICA) == "RegionOrSubregion.NORTHERN_AMERICA"
    assert repr(RegionOrSubregion.NORTHERN_EUROPE) == "RegionOrSubregion.NORTHERN_EUROPE"
    assert repr(RegionOrSubregion.POLYNESIA) == "RegionOrSubregion.POLYNESIA"
    assert repr(RegionOrSubregion.SOUTH_EASTERN_ASIA) == "RegionOrSubregion.SOUTH_EASTERN_ASIA"
    assert repr(RegionOrSubregion.SOUTHERN_ASIA) == "RegionOrSubregion.SOUTHERN_ASIA"
    assert repr(RegionOrSubregion.SOUTHERN_EUROPE) == "RegionOrSubregion.SOUTHERN_EUROPE"
    assert repr(RegionOrSubregion.SUB_SAHARAN_AFRICA) == "RegionOrSubregion.SUB_SAHARAN_AFRICA"
    assert repr(RegionOrSubregion.WESTERN_ASIA) == "RegionOrSubregion.WESTERN_ASIA"
    assert repr(RegionOrSubregion.WESTERN_EUROPE) == "RegionOrSubregion.WESTERN_EUROPE"
