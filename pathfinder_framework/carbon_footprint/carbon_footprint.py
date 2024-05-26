from pathfinder_framework.carbon_footprint.characterization_factors import CharacterizationFactors
from pathfinder_framework.carbon_footprint.cross_sectoral_standard import CrossSectoralStandard
from pathfinder_framework.carbon_footprint.declared_unit import DeclaredUnit
from pathfinder_framework.datetime import DateTime
from pathfinder_framework.carbon_footprint.geographical_scope import CarbonFootprintGeographicalScope
from pathfinder_framework.carbon_footprint.reference_period import ReferencePeriod
from pathfinder_framework.data_quality_indicators.data_quality_indicators import DataQualityIndicators


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
        reference_period (ReferencePeriod): The period over which the data was recorded for the Carbon Footprint_
        packaging_emissions_included (bool): A boolean flag indicating whether packaging emissions are included in the PCF (pCfExcludingBiogenic, pCfIncludingBiogenic).
        geographical_scope (CarbonFootprintGeographicalScope): The geographical scope of the carbon footprint.
        p_cf_including_biogenic (float | None): Carbon footprint including all biogenic emissions, expressed per declared unit.
           Can be negative, representing a net removal of CO2. Defaults to None.
        primary_data_share (float): The share of primary data in percent. See the Pathfinder Framework Sections 4.2.1, 4.2.2, Appendix B.
        dqi (DataQualityIndicators): The data quality indicators for the carbon footprint.
        d_luc_ghg_emissions (float | None): Emissions resulting from recent (i.e., previous 20 years) carbon stock loss due to land conversion directly on the area of land under consideration, expressed as a decimal equal to or greater than zero, per declared unit with unit kg of CO2 equivalent per declared unit (kgCO2e / declaredUnit). Defaults to None.
        land_management_ghg_emissions (float | None): If present, GHG emissions and removals associated with land-management-related changes, including non-CO2 sources. The value MUST be calculated per declared unit with unit kg of CO2 equivalent per declared unit (kgCO2e / declaredUnit), expressed as a decimal. Defaults to None.
        other_biogenic_ghg_emissions (float | None): If present, all other biogenic GHG emissions associated with product manufacturing and transport that are not included in dLUC (dLucGhgEmissions), iLUC (iLucGhgEmissions), and land management (landManagementGhgEmissions). The value MUST be calculated per declared unit with unit kg of CO2 equivalent per declared unit (kgCO2e / declaredUnit), expressed as a decimal equal to or greater than zero.
        biogenic_carbon_withdrawal (float | None): If present, the Biogenic Carbon contained in the product converted to kilogram of CO2e. The value MUST be calculated per declared unit with unit kgCO2e / declaredUnit expressed as a decimal equal to or less than zero.

    Note: The following attributes are not currently defined but will be affected by the 2025 check:
        - biogenicAccountingMethodology
    """

    def __init__(self, declared_unit, unitary_product_amount, p_cf_excluding_biogenic, fossil_ghg_emissions,
                 fossil_carbon_content, biogenic_carbon_content, characterization_factors,
                 ipcc_characterization_factors_sources, cross_sectoral_standards_used, boundary_processes_description,
                 exempted_emissions_percent, reference_period, packaging_emissions_included, geographical_scope,
                 p_cf_including_biogenic=None, primary_data_share=None, dqi=None, d_luc_ghg_emissions=None,
                 land_management_ghg_emissions=None, other_biogenic_ghg_emissions=None, biogenic_carbon_withdrawal=None):
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
        if not isinstance(reference_period, ReferencePeriod):
            raise ValueError("reference_period must be an instance of ReferencePeriod")
        if not isinstance(packaging_emissions_included, bool):
            raise ValueError("packaging_emissions_included must be a boolean")
        if not isinstance(geographical_scope, CarbonFootprintGeographicalScope):
            raise ValueError("geographical_scope must be an instance of CarbonFootprintGeographicalScope")
        if p_cf_including_biogenic is not None and not isinstance(p_cf_including_biogenic, (int, float)):
            raise ValueError("p_cf_including_biogenic must be a number")
        if not isinstance(primary_data_share, (int, float)) and primary_data_share is not None:
            raise ValueError("primaryDataShare must be a number")
        if dqi is not None and not isinstance(dqi, DataQualityIndicators):
            raise ValueError("dqi must be an instance of DataQualityIndicators")
        if d_luc_ghg_emissions is not None and (
                not isinstance(d_luc_ghg_emissions, (int, float)) or d_luc_ghg_emissions < 0):
            raise ValueError("d_luc_ghg_emissions must be a non-negative number")
        if land_management_ghg_emissions is not None and (
                not isinstance(land_management_ghg_emissions, (int, float))):
            raise ValueError("land_management_ghg_emissions must be a number")
        if other_biogenic_ghg_emissions is not None and (
                not isinstance(other_biogenic_ghg_emissions, (int, float)) or other_biogenic_ghg_emissions < 0):
            raise ValueError("other_biogenic_ghg_emissions must be a non-negative number")
        if biogenic_carbon_withdrawal is not None and (
                not isinstance(biogenic_carbon_withdrawal, (int, float)) or biogenic_carbon_withdrawal > 0):
            raise ValueError("biogenic_carbon_withdrawal must be a non-positive number")

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
        self.reference_period = reference_period
        self.packaging_emissions_included = packaging_emissions_included
        self.geographical_scope = geographical_scope
        self.p_cf_including_biogenic = p_cf_including_biogenic
        self.primary_data_share = primary_data_share
        self.dqi = dqi
        self.d_luc_ghg_emissions = d_luc_ghg_emissions
        self.land_management_ghg_emissions = land_management_ghg_emissions
        self.other_biogenic_ghg_emissions = other_biogenic_ghg_emissions
        self.biogenic_carbon_withdrawal = biogenic_carbon_withdrawal

        required_attributes_before_2025 = ["primary_data_share", "dqi"]
        required_attributes_after_2025 = ["primary_data_share", "dqi", "p_cf_including_biogenic", "d_luc_ghg_emissions", "land_management_ghg_emissions", "other_biogenic_ghg_emissions", "biogenic_carbon_withdrawal"]

        if reference_period.includes_2025_or_later():
            for attr in required_attributes_after_2025:
                if not hasattr(self, attr) or getattr(self, attr) is None:
                    raise ValueError(
                        f"Attribute '{attr}' must be defined and not None for reporting periods including 2025 or later"
                    )
        else:
            if not any(hasattr(self, attr) and getattr(self, attr) is not None for attr in
                       required_attributes_before_2025):
                raise ValueError(
                    "At least one of 'primary_data_share' or 'dqi' must be defined for reporting periods before 2025"
                )