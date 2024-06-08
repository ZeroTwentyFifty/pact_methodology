from enum import Enum


class RegionOrSubregion(str, Enum):
    """The RegionOrSubregion data type represents a geographic region or subregion.

    It MUST be encoded as a String with value equal to one of the following values:

    - Africa: for the UN geographic region Africa
    - Americas: for the UN geographic region Americas
    - Asia: for the UN geographic region Asia
    - Europe: for the UN geographic region Europe
    - Oceania: for the UN geographic region Oceania
    - Australia and New Zealand: for the UN geographic subregion Australia and New Zealand
    - Central Asia: for the UN geographic subregion Central Asia
    - Eastern Asia: for the UN geographic subregion Eastern Asia
    - Eastern Europe: for the UN geographic subregion Eastern Europe
    - Latin America and the Caribbean: for the UN geographic subregion Latin America and the Caribbean
    - Melanesia: for the UN geographic subregion Melanesia
    - Micronesia: for the UN geographic subregion Micronesia
    - Northern Africa: for the UN geographic subregion Northern Africa
    - Northern America: for the UN geographic subregion Northern America
    - Northern Europe: for the UN geographic subregion Northern Europe
    - Polynesia: for the UN geographic subregion Polynesia
    - South-eastern Asia: for the UN geographic subregion South-eastern Asia
    - Southern Asia: for the UN geographic subregion Southern Asia
    - Southern Europe: for the UN geographic subregion Southern Europe
    - Sub-Saharan Africa: for the UN geographic subregion Sub-Saharan Africa
    - Western Asia: for the UN geographic subregion Western Asia
    - Western Europe: for the UN geographic subregion Western Europe

    For more information, please refer to the official documentation:
        https://wbcsd.github.io/tr/2023/data-exchange-protocol-20231207/#dt-regionorsubregion
    """

    AFRICA = "Africa"
    AMERICAS = "Americas"
    ASIA = "Asia"
    EUROPE = "Europe"
    OCEANIA = "Oceania"
    AUSTRALIA_AND_NEW_ZEALAND = "Australia and New Zealand"
    CENTRAL_ASIA = "Central Asia"
    EASTERN_ASIA = "Eastern Asia"
    EASTERN_EUROPE = "Eastern Europe"
    LATIN_AMERICA_AND_THE_CARIBBEAN = "Latin America and the Caribbean"
    MELANESIA = "Melanesia"
    MICRONESIA = "Micronesia"
    NORTHERN_AFRICA = "Northern Africa"
    NORTHERN_AMERICA = "Northern America"
    NORTHERN_EUROPE = "Northern Europe"
    POLYNESIA = "Polynesia"
    SOUTH_EASTERN_ASIA = "South-eastern Asia"
    SOUTHERN_ASIA = "Southern Asia"
    SOUTHERN_EUROPE = "Southern Europe"
    SUB_SAHARAN_AFRICA = "Sub-Saharan Africa"
    WESTERN_ASIA = "Western Asia"
    WESTERN_EUROPE = "Western Europe"
