from enum import Enum


class BiogenicAccountingMethodology(str, Enum):
    """
    The standard followed to account for biogenic emissions and removals.
    If defined, the value MUST be one of the following:

    - PEF: For the EU Product Environmental Footprint Guide
    - ISO: For the ISO 14067 standard
    - GHGP: For the Greenhouse Gas Protocol (GHGP) Land sector and Removals Guidance
    - Quantis: For the Quantis Accounting for Natural Climate Solutions Guidance

    The enumeration of standards above will be evolved in future revisions.
    Account for this when implementing the validation of this property.

    For more information, please refer to the official documentation:
        https://wbcsd.github.io/tr/2023/data-exchange-protocol-20231207/#element-attrdef-carbonfootprint-biogenicaccountingmethodology
    """

    PEF = "PEF"
    ISO = "ISO"
    GHGP = "GHGP"
    QUANTIS = "Quantis"
