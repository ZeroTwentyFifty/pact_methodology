from enum import Enum


class CharacterizationFactors(str, Enum):
    """
    The IPCC version of the GWP characterization factors used in the calculation of the PCF (see Pathfinder Framework Section 3.2.2).
    The value MUST be one of the following:

    - AR6: for the Sixth Assessment Report of the Intergovernmental Panel on Climate Change (IPCC)
    - AR5: for the Fifth Assessment Report of the IPCC.

    The set of characterization factor identifiers will likely change in future revisions.
    It is recommended to account for this when implementing the validation of this property.

    For more information, please refer to the official documentation:
        https://wbcsd.github.io/tr/2023/data-exchange-protocol-20231207/#element-attrdef-carbonfootprint-characterizationfactors
    """

    AR5 = "AR5"
    AR6 = "AR6"
