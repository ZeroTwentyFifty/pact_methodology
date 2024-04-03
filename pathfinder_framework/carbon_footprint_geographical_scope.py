class CarbonFootprintGeographicalScope:
    """
    Represents the geographical scope of a Carbon Footprint.

    The geographical scope is defined by the properties `global_scope`, `geography_country_subdivision`, `geography_country`, and `geography_region_or_subregion`.
    The level of granularity of the geographical information is at the sole discretion of the company, and can be at a plant, region, or country level.
    ISO 3166-1 alpha-2 country codes (e.g. US for the United States or FR for France) are used to indicate specific countries or regions.

    The relationship between the geographic scope and the definedness or undefinedness of properties is as follows:

    * If the geographical granularity is Global, then `geography_country` and `geography_region_or_subregion` and `geography_country_subdivision` must be undefined.
    * If the geographical granularity is regional or sub-regional, then `geography_region_or_subregion` must be defined and `geography_country` and `geography_country_subdivision` must be undefined.
    * If the geographical granularity is country-specific, then `geography_country` must be defined and `geography_region_or_subregion` and `geography_country_subdivision` must be undefined.
    * If the geographical granularity is country subdivision-specific, then `geography_country_subdivision` must be defined and `geography_region_or_subregion` and `geography_country` must be undefined.

    :param global_scope: A boolean indicating whether the scope is global.
    :param geography_country_subdivision: The country subdivision (e.g. US-NY).
    :param geography_country: The country (e.g. US).
    :param geography_region_or_subregion: The region or subregion (e.g. Region).
    :raises ValueError: If more than one field is provided, or if no field is provided.
    """
    def __init__(
        self,
        *,
        global_scope=False,
        geography_country_subdivision=None,
        geography_country=None,
        geography_region_or_subregion=None,
    ):
        if global_scope and (
            geography_country_subdivision or geography_country or geography_region_or_subregion
        ):
            raise ValueError(
                "Cannot provide geography_country_subdivision, geography_country, or geography_region_or_subregion when global_scope is True"
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
        elif geography_country_subdivision:
            self.scope = geography_country_subdivision
        elif geography_country:
            self.scope = geography_country
        elif geography_region_or_subregion:
            self.scope = geography_region_or_subregion
        else:
            raise ValueError(
                "At least one argument must be provided from: global_scope, geography_country_subdivision, geography_country, or geography_region_or_subregion"
            )
