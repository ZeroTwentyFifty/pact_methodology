from enum import Enum

import pycountry

from pact_methodology.carbon_footprint.region_or_subregion import RegionOrSubregion


class GeographicalGranularity(Enum):
    """Represents the granularity level of geographical information.

    This enum defines different levels of geographical granularity that can be used
    to specify the scope of carbon footprint data.

    Attributes:
        GLOBAL: Represents global scope with no specific geographical boundaries.
        COUNTRY_SUBDIVISION: Represents scope at a country subdivision level (e.g. state/province).
        COUNTRY: Represents scope at a country level.
        REGION_OR_SUBREGION: Represents scope at a regional or subregional level.

    Example:
        >>> granularity = GeographicalGranularity.COUNTRY
        >>> str(granularity)
        'Country'
        >>> granularity = GeographicalGranularity.COUNTRY_SUBDIVISION
        >>> str(granularity)
        'Country Subdivision'
        >>> granularity = GeographicalGranularity.GLOBAL
        >>> repr(granularity)
        'GeographicalGranularity.GLOBAL'
    """
    GLOBAL = "Global"
    COUNTRY_SUBDIVISION = "Country Subdivision"
    COUNTRY = "Country"
    REGION_OR_SUBREGION = "Region or Subregion"

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"GeographicalGranularity.{self.name}"


class CarbonFootprintGeographicalScope:
    """
    Represents the geographical scope of a Carbon Footprint.

    The geographical scope is defined by the properties `global_scope`, `geography_country_subdivision`, `geography_country`, and `geography_region_or_subregion`.
    The level of granularity of the geographical information is at the sole discretion of the company, and can be at a plant, region, or country level.
    ISO 3166-1 alpha-2 country codes (e.g. US for the United States or FR for France) are used to indicate specific countries or regions.

    The relationship between the geographic scope and the definedness or undefinedness of properties is as follows:

    * If the geographical granularity is Global, then `geography_country` and `geography_region_or_subregion` and
        `geography_country_subdivision` must be undefined.
    * If the geographical granularity is regional or sub-regional, then `geography_region_or_subregion` must be defined and `geography_country` and `geography_country_subdivision` must be undefined.
    * If the geographical granularity is country-specific, then `geography_country` must be defined and `geography_region_or_subregion` and `geography_country_subdivision` must be undefined.
    * If the geographical granularity is country subdivision-specific, then `geography_country_subdivision` must be defined and `geography_region_or_subregion` and `geography_country` must be undefined.

    Args:
        global_scope (bool): A boolean indicating whether the scope is global.
        geography_country_subdivision (str): The country subdivision (e.g. US-NY).
        geography_country (str): The country (e.g. US).
        geography_region_or_subregion (RegionOrSubregion): The region or subregion (e.g. "Africa").

    Raises:
        ValueError: If more than one field is provided, or if no field is provided.

    Attributes:
        scope (str or RegionOrSubregion): The geographical scope.
        granularity (GeographicalGranularity): The granularity of the geographical scope.
        
    Examples:
        Create a global scope:
        >>> scope = CarbonFootprintGeographicalScope(global_scope=True)
        >>> scope.granularity
        GeographicalGranularity.GLOBAL

        Create a country-specific scope:
        >>> scope = CarbonFootprintGeographicalScope(geography_country="US")
        >>> scope.scope
        'US'
        >>> scope.granularity
        GeographicalGranularity.COUNTRY
    """

    def __init__(
        self,
        *,
        global_scope: bool = False,
        geography_country_subdivision: str = None,
        geography_country: str = None,
        geography_region_or_subregion: RegionOrSubregion | str = None,
    ) -> None:

        self.scope: str | RegionOrSubregion
        self.granularity: GeographicalGranularity

        if global_scope and (
            geography_country_subdivision
            or geography_country
            or geography_region_or_subregion
        ):
            raise ValueError(
                "Cannot provide geography_country_subdivision, geography_country, or geography_region_or_subregion "
                "when global_scope is True"
            )
        if (
            geography_country_subdivision
            and geography_country
            or geography_country_subdivision
            and geography_region_or_subregion
            or geography_country
            and geography_region_or_subregion
        ):
            raise ValueError("Cannot provide more than one geographical field")

        if global_scope:
            self.scope = "Global"
            self.granularity = GeographicalGranularity.GLOBAL
        elif geography_country_subdivision:
            if pycountry.subdivisions.get(code=geography_country_subdivision) is None:
                raise ValueError(
                    f"Invalid country subdivision code: {geography_country_subdivision}"
                )
            self.scope = geography_country_subdivision
            self.granularity = GeographicalGranularity.COUNTRY_SUBDIVISION
        elif geography_country:
            if pycountry.countries.get(alpha_2=geography_country) is None:
                raise ValueError(f"Invalid country code: {geography_country}")
            self.scope = geography_country
            self.granularity = GeographicalGranularity.COUNTRY
        elif geography_region_or_subregion:
            if not isinstance(geography_region_or_subregion, RegionOrSubregion):
                raise ValueError(
                    "geography_region_or_subregion must be a RegionOrSubregion"
                )
            self.scope = geography_region_or_subregion
            self.granularity = GeographicalGranularity.REGION_OR_SUBREGION
        else:
            raise ValueError(
                "At least one argument must be provided from: global_scope, geography_country_subdivision, geography_country, or geography_region_or_subregion"
            )

    def __str__(self):
        return f"Geographical scope: {self.scope} (at {self.granularity.value} level)"
        
    def __repr__(self):
        return (
            f"CarbonFootprintGeographicalScope("
            f"scope={self.scope}, "
            f"granularity={self.granularity.value})"
        )
