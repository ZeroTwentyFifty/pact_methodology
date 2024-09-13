from enum import Enum


class DeclaredUnit(str, Enum):
    """
    DeclaredUnit is the enumeration of accepted declared units with values.

    The values are based on the International System of Units (SI) as defined by the International Committee for Weights and Measures (ICWM).

    - LITER: for special SI Unit litre
    - KILOGRAM: for SI Base Unit kilogram
    - CUBIC_METER: for cubic meter, the Derived Unit from SI Base Unit metre
    - KILOWATT_HOUR: for kilowatt-hour, the Derived Unit from special SI Unit watt
    - MEGAJOULE: for megajoule, the Derived Unit from special SI Unit joule
    - TON_KILOMETER: for ton kilometer, the Derived Unit from SI Base Units kilogram and metre
    - SQUARE_METER: for square meter, the Derived Unit from SI Base Unit metre

    The value of each DeclaredUnit MUST be encoded as a JSON String.

    For more information, please refer to the official documentation:
        https://wbcsd.github.io/data-exchange-protocol/v2/#dt-declaredunit
    And the SI Unit reference:
        https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf/2d2b50bf-f2b4-9661-f402-5f9d66e4b507
    """

    LITER = "liter"
    KILOGRAM = "kilogram"
    CUBIC_METER = "cubic meter"
    KILOWATT_HOUR = "kilowatt hour"
    MEGAJOULE = "megajoule"
    TON_KILOMETER = "ton kilometer"
    SQUARE_METER = "square meter"
