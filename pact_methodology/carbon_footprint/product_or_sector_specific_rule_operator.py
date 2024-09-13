from enum import Enum


class ProductOrSectorSpecificRuleOperator(str, Enum):
    """
    A ProductOrSectorSpecificRuleOperator is the enumeration of Product Category Rule (PCR) operators. Valid values are:

    - PEF: for EU / PEF Methodology PCRs
    - EPD International: for PCRs authored or published by EPD International
    - OTHER: for a PCR not published by the operators mentioned above

    4.13.1. JSON Representation
    Each value is encoded as a JSON String.

    For more information, please refer to the official documentation:
        https://wbcsd.github.io/tr/2023/data-exchange-protocol-20231207/#dt-productorsectorspecificruleoperator
    """

    PEF = "PEF"
    EPD_INTERNATIONAL = "EPD International"
    OTHER = "Other"
