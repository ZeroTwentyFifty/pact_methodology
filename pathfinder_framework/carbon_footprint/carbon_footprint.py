from pathfinder_framework.carbon_footprint.characterization_factors import CharacterizationFactors
from pathfinder_framework.carbon_footprint.declared_unit import DeclaredUnit


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
        cross_sectoral_standards_used (list[str]): The cross-sectoral standards applied for calculating or allocating GHG emissions.
        exempted_emissions_percent (float): The Percentage of emissions excluded from PCF, expressed as a decimal number between 0.0 and 5 including.
    """
    def __init__(self, declared_unit, unitary_product_amount, p_cf_excluding_biogenic, fossil_ghg_emissions, fossil_carbon_content, biogenic_carbon_content, characterization_factors, ipcc_characterization_factors_sources, cross_sectoral_standards_used, boundary_processes_description, exempted_emissions_percent):
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
        if not cross_sectoral_standards_used:
            raise ValueError("cross_sectoral_standards_used must not be empty")
        if not boundary_processes_description:
            raise ValueError("boundary_processes_description must not be empty")
        if not 0.0 <= exempted_emissions_percent <= 5.0:
            raise ValueError("exempted_emissions_percent must be between 0.0 and 5.0")

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