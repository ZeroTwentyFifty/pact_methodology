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
