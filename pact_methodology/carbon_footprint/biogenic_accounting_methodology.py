from enum import Enum


class BiogenicAccountingMethodology(str, Enum):
    """
    The standard followed to account for biogenic emissions and removals.
    If defined, the value MUST be one of the following:

    - PEF: For the EU Product Environmental Footprint Guide
    - ISO: For the ISO 14067 standard
    - GHGP: For the Greenhouse Gas Protocol (GHGP) Land sector and Removals Guidance
    - Quantis: For the Quantis Accounting for Natural Climate Solutions Guidance

    For more information, please refer to the official documentation:
        https://wbcsd.github.io/data-exchange-protocol/v2/#element-attrdef-carbonfootprint-biogenicaccountingmethodology
    """

    PEF = "PEF"
    ISO = "ISO"
    GHGP = "GHGP"
    QUANTIS = "Quantis"

    def __str__(self):
        return self.value
    
    def __repr__(self):
        return f"BiogenicAccountingMethodology.{self.name}"
