from pathfinder_framework.carbon_footprint.characterization_factors import CharacterizationFactors
from pathfinder_framework.carbon_footprint.cross_sectoral_standard import CrossSectoralStandard
from pathfinder_framework.carbon_footprint.declared_unit import DeclaredUnit
from pathfinder_framework.datetime import DateTime


class CarbonFootprint:
    """
    A CarbonFootprint represents the carbon footprint of a product and related data in accordance with the Pathfinder Framework.

    Attributes:
        declared_unit (DeclaredUnit): The unit of analysis of the product.
        unitary_product_amount (float): The amount of Declared Units contained within the product to which the PCF is referring to.
        p_cf_excluding_biogenic (float): The product carbon footprint of the product excluding biogenic CO2 emissions.
        fossil_ghg_emissions (float): The emissions from fossil sources as a result of fuel combustion, from fugitive emissions, and from process emissions.
        fossil_carbon_content (float): The fossil carbon content of the product (mass of carbon).
        biogenic_carbon_content (float): The biogenic carbon content of the product (mass of carbon).
        characterization_factors (CharacterizationFactors): The IPCC version of the GWP characterization factors used in the calculation of the PCF.
        ipcc_characterization_factors_sources (list[str]): The characterization factors from one or more IPCC Assessment Reports used in the calculation of the PCF.
        cross_sectoral_standards_used (list[CrossSectoralStandard]): The cross-sectoral standards applied for calculating or allocating GHG emissions.
        exempted_emissions_percent (float): The Percentage of emissions excluded from PCF, expressed as a decimal number between 0.0 and 5 including.
        reference_period_start (DateTime): The start (including) of the time boundary for which the PCF value is considered to be representative.
        reference_period_end (DateTime): The end (excluding) of the time boundary for which the PCF value is considered to be representative.
        packaging_emissions_included (bool): A boolean flag indicating whether packaging emissions are included in the PCF (pCfExcludingBiogenic, pCfIncludingBiogenic).
    """
    def __init__(self, declared_unit, unitary_product_amount, p_cf_excluding_biogenic, fossil_ghg_emissions, fossil_carbon_content, biogenic_carbon_content, characterization_factors, ipcc_characterization_factors_sources, cross_sectoral_standards_used, boundary_processes_description, exempted_emissions_percent, reference_period_start, reference_period_end, packaging_emissions_included):
        if not isinstance(declared_unit, DeclaredUnit):
            raise ValueError(
                f"declared_unit '{declared_unit}' is not valid. It must be one of the following: {', '.join([unit.value for unit in DeclaredUnit])}")
        if unitary_product_amount <= 0:
            raise ValueError("unitary_product_amount must be strictly greater than 0")
        if p_cf_excluding_biogenic < 0:
            raise ValueError("p_cf_excluding_biogenic must be equal to or greater than 0")
        if fossil_ghg_emissions < 0:
            raise ValueError("fossil_ghg_emissions must be equal to or greater than 0")
        if fossil_carbon_content < 0:
            raise ValueError("fossil_carbon_content must be equal to or greater than 0")
        if biogenic_carbon_content < 0:
            raise ValueError("biogenic_carbon_content must be equal to or greater than 0")
        if not isinstance(characterization_factors, CharacterizationFactors):
            raise ValueError("characterization_factors must be an instance of CharacterizationFactors")
        if not ipcc_characterization_factors_sources:
            raise ValueError("ipcc_characterization_factors_sources must not be empty")
        if not all(isinstance(standard, CrossSectoralStandard) for standard in cross_sectoral_standards_used):
            raise ValueError("cross_sectoral_standards_used must be a list of CrossSectoralStandard")
        if not boundary_processes_description:
            raise ValueError("boundary_processes_description must not be empty")
        if not 0.0 <= exempted_emissions_percent <= 5.0:
            raise ValueError("exempted_emissions_percent must be between 0.0 and 5.0")
        if not isinstance(reference_period_start, DateTime):
            raise ValueError("reference_period_start must be an instance of DateTime")
        if not isinstance(reference_period_end, DateTime):
            raise ValueError("reference_period_end must be an instance of DateTime")
        if not isinstance(packaging_emissions_included, bool):
            raise ValueError("packaging_emissions_included must be a boolean")

        self.declared_unit = declared_unit
        self.unitary_product_amount = unitary_product_amount
        self.p_cf_excluding_biogenic = p_cf_excluding_biogenic
        self.fossil_ghg_emissions = fossil_ghg_emissions
        self.fossil_carbon_content = fossil_carbon_content
        self.biogenic_carbon_content = biogenic_carbon_content
        self.characterization_factors = characterization_factors
        self.ipcc_characterization_factors_sources = ipcc_characterization_factors_sources
        self.cross_sectoral_standards_used = cross_sectoral_standards_used
        self.boundary_processes_description = boundary_processes_description
        self.exempted_emissions_percent = exempted_emissions_percent
        self.reference_period_start = reference_period_start
        self.reference_period_end = reference_period_end
        self.packaging_emissions_included = packaging_emissions_included
