import pytest

from pact_methodology.carbon_footprint.geographical_scope import (
    CarbonFootprintGeographicalScope,
    GeographicalGranularity,
)
from pact_methodology.carbon_footprint.region_or_subregion import RegionOrSubregion


@pytest.mark.parametrize(
    "global_scope, geography_country_subdivision, geography_country, geography_region_or_subregion",
    [
        (True, None, None, None),
        (False, "US-NY", None, None),
        (False, None, "FR", None),
        (False, None, None, RegionOrSubregion.AFRICA),
    ],
)
def test_carbon_footprint_geographical_scope_successful_instantiation(
    global_scope,
    geography_country_subdivision,
    geography_country,
    geography_region_or_subregion,
):
    CarbonFootprintGeographicalScope(
        global_scope=global_scope,
        geography_country_subdivision=geography_country_subdivision,
        geography_country=geography_country,
        geography_region_or_subregion=geography_region_or_subregion,
    )


@pytest.mark.parametrize(
    "global_scope, geography_country_subdivision, geography_country, geography_region_or_subregion, expected_error",
    [
        (True, "US-NY", None, None, ValueError),
        (False, "US-NY", "FR", None, ValueError),
        (False, "US-NY", None, "Region", ValueError),
        (False, None, "FR", "Region", ValueError),
    ],
)
def test_carbon_footprint_geographical_scope_failed_instantiation(
    global_scope,
    geography_country_subdivision,
    geography_country,
    geography_region_or_subregion,
    expected_error,
):
    with pytest.raises(expected_error):
        CarbonFootprintGeographicalScope(
            global_scope=global_scope,
            geography_country_subdivision=geography_country_subdivision,
            geography_country=geography_country,
            geography_region_or_subregion=geography_region_or_subregion,
        )


def test_global_scope():
    scope = CarbonFootprintGeographicalScope(global_scope=True)
    assert scope.scope == "Global"


def test_geography_country_subdivision_scope():
    scope = CarbonFootprintGeographicalScope(geography_country_subdivision="US-NY")
    assert scope.scope == "US-NY"


def test_geography_country_scope():
    scope = CarbonFootprintGeographicalScope(geography_country="FR")
    assert scope.scope == "FR"


def test_geography_region_or_subregion_scope():
    scope = CarbonFootprintGeographicalScope(
        geography_region_or_subregion=RegionOrSubregion.AFRICA
    )
    assert scope.scope == RegionOrSubregion.AFRICA


def test_global_scope_granularity():
    scope = CarbonFootprintGeographicalScope(global_scope=True)
    assert scope.granularity == GeographicalGranularity.GLOBAL


def test_geography_country_subdivision_scope_granularity():
    scope = CarbonFootprintGeographicalScope(geography_country_subdivision="US-NY")
    assert scope.granularity == GeographicalGranularity.COUNTRY_SUBDIVISION


def test_geography_country_scope_granularity():
    scope = CarbonFootprintGeographicalScope(geography_country="FR")
    assert scope.granularity == GeographicalGranularity.COUNTRY


def test_geography_region_or_subregion_scope_granularity():
    scope = CarbonFootprintGeographicalScope(
        geography_region_or_subregion=RegionOrSubregion.AFRICA
    )
    assert scope.granularity == GeographicalGranularity.REGION_OR_SUBREGION


def test_geographical_granularity_enum():
    assert GeographicalGranularity.GLOBAL.value == "Global"
    assert GeographicalGranularity.COUNTRY_SUBDIVISION.value == "Country Subdivision"
    assert GeographicalGranularity.COUNTRY.value == "Country"
    assert GeographicalGranularity.REGION_OR_SUBREGION.value == "Region or Subregion"


def test_geographical_granularity_enum_str():
    assert str(GeographicalGranularity.GLOBAL) == "Global"
    assert str(GeographicalGranularity.COUNTRY_SUBDIVISION) == "Country Subdivision"
    assert str(GeographicalGranularity.COUNTRY) == "Country"
    assert str(GeographicalGranularity.REGION_OR_SUBREGION) == "Region or Subregion"


def test_geographical_granularity_enum_repr():
    assert repr(GeographicalGranularity.GLOBAL) == "GeographicalGranularity.GLOBAL"
    assert repr(GeographicalGranularity.COUNTRY_SUBDIVISION) == "GeographicalGranularity.COUNTRY_SUBDIVISION"
    assert repr(GeographicalGranularity.COUNTRY) == "GeographicalGranularity.COUNTRY"
    assert repr(GeographicalGranularity.REGION_OR_SUBREGION) == "GeographicalGranularity.REGION_OR_SUBREGION"


@pytest.mark.parametrize("country_code", ["US", "FR", "GB", "CN", "JP"])
def test_carbon_footprint_geographical_scope_valid_country_codes(country_code):
    scope = CarbonFootprintGeographicalScope(geography_country=country_code)
    assert scope.granularity == GeographicalGranularity.COUNTRY
    assert scope.scope == country_code


@pytest.mark.parametrize("country_code", ["XX", "ABC", "123", "", "  ", None])
def test_carbon_footprint_geographical_scope_invalid_country_codes(country_code):
    with pytest.raises(ValueError):
        CarbonFootprintGeographicalScope(geography_country=country_code)


@pytest.mark.parametrize(
    "subdivision_code", ["US-CA", "FR-IDF", "GB-ENG", "CN-SH", "JP-13"]
)
def test_carbon_footprint_geographical_scope_valid_subdivision_codes(subdivision_code):
    scope = CarbonFootprintGeographicalScope(
        geography_country_subdivision=subdivision_code
    )
    assert scope.granularity == GeographicalGranularity.COUNTRY_SUBDIVISION
    assert scope.scope == subdivision_code


@pytest.mark.parametrize(
    "subdivision_code", ["US-XX", "FR-ABC", "GB-123", "CN-11", "CN-", "JP-  ", None]
)
def test_carbon_footprint_geographical_scope_invalid_subdivision_codes(
    subdivision_code,
):
    with pytest.raises(ValueError):
        CarbonFootprintGeographicalScope(geography_country_subdivision=subdivision_code)


def test_no_scope_raises_value_error():
    with pytest.raises(
        ValueError,
        match="At least one argument must be provided from: global_scope, geography_country_subdivision, geography_country, or geography_region_or_subregion",
    ):
        CarbonFootprintGeographicalScope()
