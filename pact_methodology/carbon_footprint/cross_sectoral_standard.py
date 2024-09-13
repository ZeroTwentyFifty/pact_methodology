from enum import Enum


class CrossSectoralStandard(str, Enum):
    """
    CrossSectoralStandard is the enumeration of accounting standards used for product carbon footprint calculation. Valid values are

    - GHG Protocol Product standard: for the GHG Protocol Product standard
    - ISO Standard 14067: for ISO Standard 14067
    - ISO Standard 14044: for ISO Standard 14044

    4.9.1. JSON Representation
    Each CrossSectoralStandard MUST be encoded as a JSON string.

    The value of each DeclaredUnit MUST be encoded as a JSON String.

    For more information, please refer to the official documentation:
        https://wbcsd.github.io/tr/2023/data-exchange-protocol-20231207/#dt-crosssectoralstandard
    """

    GHG_PROTOCOL = "GHG Protocol Product standard"
    ISO_14067 = "ISO Standard 14067"
    ISO_14044 = "ISO Standard 14044"
