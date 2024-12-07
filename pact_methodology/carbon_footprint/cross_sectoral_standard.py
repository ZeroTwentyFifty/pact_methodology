from enum import Enum


class CrossSectoralStandard(str, Enum):
    """
    CrossSectoralStandard is the enumeration of accounting standards used for product carbon footprint calculation. Valid values are

    - GHG Protocol Product standard: for the GHG Protocol Product standard
    - ISO Standard 14067: for ISO Standard 14067
    - ISO Standard 14044: for ISO Standard 14044

    Each CrossSectoralStandard MUST be encoded as a JSON string.

    For more information, please refer to the official documentation:
        https://wbcsd.github.io/data-exchange-protocol/v2/#dt-crosssectoralstandard
    """

    GHG_PROTOCOL = "GHG Protocol Product standard"
    ISO_14067 = "ISO Standard 14067"
    ISO_14044 = "ISO Standard 14044"
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return f"CrossSectoralStandard.{self.name}"
