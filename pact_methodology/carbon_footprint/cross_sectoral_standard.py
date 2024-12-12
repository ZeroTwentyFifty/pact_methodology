from enum import Enum

class CrossSectoralStandard(str, Enum):
    """
    CrossSectoralStandard is the enumeration of accounting standards used for product carbon footprint calculation.
    Valid values are:

    - GHG_PROTOCOL: Represents the GHG Protocol Product standard.
    - ISO_14067: Represents ISO Standard 14067.
    - ISO_14044: Represents ISO Standard 14044.

    Each CrossSectoralStandard MUST be encoded as a JSON string.

    Examples:
        Select a standard:
        >>> standard = CrossSectoralStandard.GHG_PROTOCOL
        >>> print(standard)
        GHG Protocol Product standard

        >>> print(repr(standard))
        CrossSectoralStandard.GHG_PROTOCOL

        Iterating over all standards:
        >>> for standard in CrossSectoralStandard:
        ...     print(standard)
        GHG Protocol Product standard
        ISO Standard 14067
        ISO Standard 14044
    """

    GHG_PROTOCOL = "GHG Protocol Product standard"
    ISO_14067 = "ISO Standard 14067"
    ISO_14044 = "ISO Standard 14044"

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"CrossSectoralStandard.{self.name}"
