import pytest

from pathfinder_framework.carbon_footprint_geographical_scope import CarbonFootprintGeographicalScope


@pytest.mark.parametrize(
    "global_scope, geography_country_subdivision, geography_country, geography_region_or_subregion",
    [
        (True, None, None, None),
        (False, "US-NY", None, None),
        (False, None, "FR", None),
        (False, None, None, "Region"),
    ],
)
def test_carbon_footprint_geographical_scope_successful_instantiation(
    global_scope, geography_country_subdivision, geography_country, geography_region_or_subregion
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
    global_scope, geography_country_subdivision, geography_country, geography_region_or_subregion, expected_error
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
    scope = CarbonFootprintGeographicalScope(geography_region_or_subregion="Region")
    assert scope.scope == "Region"


def test_no_scope_raises_value_error():
    with pytest.raises(
            ValueError,
            match="At least one argument must be provided from: global_scope, geography_country_subdivision, geography_country, or geography_region_or_subregion"
    ):
        CarbonFootprintGeographicalScope()
