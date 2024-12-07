from enum import Enum


class ProductOrSectorSpecificRuleOperator(str, Enum):
    """
    A ProductOrSectorSpecificRuleOperator is the enumeration of Product Category Rule (PCR) operators. Valid values are:

    - PEF: for EU / PEF Methodology PCRs
    - EPD International: for PCRs authored or published by EPD International
    - OTHER: for a PCR not published by the operators mentioned above

    For more information, please refer to the official documentation:
        https://wbcsd.github.io/data-exchange-protocol/v2/#dt-productorsectorspecificrule
    """

    PEF = "PEF"
    EPD_INTERNATIONAL = "EPD International"
    OTHER = "Other"

    def __str__(self):
        return self.value
    
    def __repr__(self):
        return f"ProductOrSectorSpecificRuleOperator.{self.name}"
