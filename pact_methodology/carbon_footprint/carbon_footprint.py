from pact_methodology.assurance.assurance import Assurance
from pact_methodology.carbon_footprint.characterization_factors import (
    CharacterizationFactors,
)
from pact_methodology.carbon_footprint.cross_sectoral_standard_set import CrossSectoralStandardSet
from pact_methodology.carbon_footprint.declared_unit import DeclaredUnit
from pact_methodology.carbon_footprint.geographical_scope import (
    CarbonFootprintGeographicalScope,
)
from pact_methodology.carbon_footprint.reference_period import ReferencePeriod
from pact_methodology.data_quality_indicators.data_quality_indicators import (
    DataQualityIndicators,
)
from pact_methodology.carbon_footprint.biogenic_accounting_methodology import BiogenicAccountingMethodology
from pact_methodology.carbon_footprint.product_or_sector_specific_rule_set import ProductOrSectorSpecificRuleSet
from pact_methodology.carbon_footprint.emission_factor_ds_set import EmissionFactorDSSet

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
        cross_sectoral_standards_used (CrossSectoralStandardSet): The cross-sectoral standards applied for calculating or allocating GHG emissions.
        boundary_processes_description (str): Description of boundary processes.
        exempted_emissions_percent (float): The Percentage of emissions excluded from PCF, expressed as a decimal number between 0.0 and 5 including.
        exempted_emissions_description (str): Rationale behind exclusion of specific PCF emissions, can be the empty string if no emissions were excluded.
        reference_period (ReferencePeriod): The period over which the data was recorded for the Carbon Footprint.
        packaging_emissions_included (bool): A boolean flag indicating whether packaging emissions are included in the PCF (pCfExcludingBiogenic, pCfIncludingBiogenic).
        geographical_scope (CarbonFootprintGeographicalScope): The geographical scope of the carbon footprint.
        p_cf_including_biogenic (float | None): Carbon footprint including all biogenic emissions, expressed per declared unit.
           Can be negative, representing a net removal of CO2. Defaults to None.
        primary_data_share (float): The share of primary data in percent. See the Pathfinder Framework Sections 4.2.1, 4.2.2, Appendix B.
        dqi (DataQualityIndicators): The data quality indicators for the carbon footprint.
        secondary_emission_factor_sources (EmissionFactorDSSet | None): The secondary emission factor sources used in the calculation of the PCF.
        d_luc_ghg_emissions (float | None): Emissions resulting from recent (i.e., previous 20 years) carbon stock loss due to land conversion directly on the area of land under consideration, expressed as a decimal equal to or greater than zero, per declared unit with unit kg of CO2 equivalent per declared unit (kgCO2e / declaredUnit). Defaults to None.
        land_management_ghg_emissions (float | None): If present, GHG emissions and removals associated with land-management-related changes, including non-CO2 sources. The value MUST be calculated per declared unit with unit kg of CO2 equivalent per declared unit (kgCO2e / declaredUnit), expressed as a decimal. Defaults to None.
        other_biogenic_ghg_emissions (float | None): If present, all other biogenic GHG emissions associated with product manufacturing and transport that are not included in dLUC (dLucGhgEmissions), iLUC (iLucGhgEmissions), and land management (landManagementGhgEmissions). The value MUST be calculated per declared unit with unit kg of CO2 equivalent per declared unit (kgCO2e / declaredUnit), expressed as a decimal equal to or greater than zero.
        biogenic_carbon_withdrawal (float | None): If present, the Biogenic Carbon contained in the product converted to kilogram of CO2e. The value MUST be calculated per declared unit with unit kgCO2e / declaredUnit expressed as a decimal equal to or less than zero.
        iluc_ghg_emissions (float | None): If present, emissions resulting from recent (i.e., previous 20 years) carbon stock loss due to land conversion on land not owned or controlled by the company or in its supply chain, induced by change in demand for products produced or sourced by the company. The value MUST be calculated per declared unit with unit kg of CO2 equivalent per declared unit (kgCO2e / declaredUnit), expressed as a decimal equal to or greater than zero. See Pathfinder Framework (Appendix B) for details. Defaults to None.
        aircraft_ghg_emissions (float | None): If present, the GHG emissions resulting from aircraft engine usage for the transport of the product, excluding radiative forcing. The value MUST be calculated per declared unit with unit kg of CO2 equivalent per declared unit (kgCO2e / declaredUnit), expressed as a decimal equal to or greater than zero.
        packaging_ghg_emissions (float | None): Emissions resulting from the packaging of the product. If present, the value MUST be calculated per declared unit with unit kg of CO2 equivalent per kilogram (kgCO2e / declared unit), expressed as a decimal equal to or greater than zero. The value MUST NOT be defined if packagingEmissionsIncluded is false.
        allocation_rules_description (str | None): If present, a description of any allocation rules applied and the rationale explaining how the selected approach aligns with Pathfinder Framework rules (see Section 3.3.1.4).
        uncertainty_assessment_description (str | None): If present, the results, key drivers, and a short qualitative description of the uncertainty assessment.
        assurance (Assurance | None): If present, the Assurance information in accordance with the Pathfinder Framework.
        biogenic_accounting_methodology (BiogenicAccountingMethodology | None): The methodology used for biogenic carbon accounting.
        product_or_sector_specific_rules (ProductOrSectorSpecificRuleSet | None): If present, refers to a set of product or sector specific rules published by a specific operator and applied during product carbon footprint calculation.
    """

    def __init__(
        self,
        declared_unit,
        unitary_product_amount,
        p_cf_excluding_biogenic,
        fossil_ghg_emissions,
        fossil_carbon_content,
        biogenic_carbon_content,
        characterization_factors,
        ipcc_characterization_factors_sources,
        cross_sectoral_standards_used,
        boundary_processes_description,
        exempted_emissions_percent,
        exempted_emissions_description,
        reference_period,
        packaging_emissions_included,
        geographical_scope,
        p_cf_including_biogenic=None,
        primary_data_share=None,
        dqi=None,
        secondary_emission_factor_sources=None,
        d_luc_ghg_emissions=None,
        land_management_ghg_emissions=None,
        other_biogenic_ghg_emissions=None,
        biogenic_carbon_withdrawal=None,
        iluc_ghg_emissions=None,
        aircraft_ghg_emissions=None,
        packaging_ghg_emissions=None,
        allocation_rules_description=None,
        uncertainty_assessment_description=None,
        assurance=None,
        biogenic_accounting_methodology=None,
        product_or_sector_specific_rules=None
    ):
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
        self.exempted_emissions_description = exempted_emissions_description
        self.reference_period = reference_period
        self.packaging_emissions_included = packaging_emissions_included
        self.geographical_scope = geographical_scope
        self.p_cf_including_biogenic = p_cf_including_biogenic
        self.primary_data_share = primary_data_share
        self.dqi = dqi
        self.secondary_emission_factor_sources = secondary_emission_factor_sources
        self.d_luc_ghg_emissions = d_luc_ghg_emissions
        self.land_management_ghg_emissions = land_management_ghg_emissions
        self.other_biogenic_ghg_emissions = other_biogenic_ghg_emissions
        self.biogenic_carbon_withdrawal = biogenic_carbon_withdrawal
        self.iluc_ghg_emissions = iluc_ghg_emissions
        self.aircraft_ghg_emissions = aircraft_ghg_emissions
        self.packaging_ghg_emissions = packaging_ghg_emissions
        self.allocation_rules_description = allocation_rules_description
        self.uncertainty_assessment_description = uncertainty_assessment_description
        self.assurance = assurance
        self.biogenic_accounting_methodology = biogenic_accounting_methodology
        self.product_or_sector_specific_rules = product_or_sector_specific_rules

        required_attributes_before_2025 = ["primary_data_share", "dqi"]
        required_attributes_after_2025 = [
            "primary_data_share",
            "dqi",
            "p_cf_including_biogenic",
            "d_luc_ghg_emissions",
            "land_management_ghg_emissions",
            "other_biogenic_ghg_emissions",
            "biogenic_carbon_withdrawal",
            "biogenic_accounting_methodology",
        ]

        if reference_period.includes_2025_or_later():
            for attr in required_attributes_after_2025:
                if not hasattr(self, attr) or getattr(self, attr) is None:
                    raise ValueError(
                        f"Attribute '{attr}' must be defined and not None for reporting periods including 2025 or later"
                    )
        else:
            if not any(
                hasattr(self, attr) and getattr(self, attr) is not None
                for attr in required_attributes_before_2025
            ):
                raise ValueError(
                    "At least one of 'primary_data_share' or 'dqi' must be defined for reporting periods before 2025"
                )

    @property
    def declared_unit(self):
        """Gets the declared unit of analysis for the product.

        Returns:
            DeclaredUnit: The declared unit of analysis for the product.
        """
        return self._declared_unit

    @declared_unit.setter
    def declared_unit(self, value):
        """Sets the declared unit of analysis for the product.

        Args:
            value (DeclaredUnit): The declared unit to set.

        Raises:
            ValueError: If value is not an instance of DeclaredUnit.
        """
        if not isinstance(value, DeclaredUnit):
            raise ValueError(
                f"declared_unit '{value}' is not valid. It must be one of the following: {', '.join([unit.value for unit in DeclaredUnit])}"
            )
        self._declared_unit = value

    @property
    def unitary_product_amount(self):
        """Gets the amount of Declared Units contained within the product.

        Returns:
            float: The unitary product amount.
        """
        return self._unitary_product_amount

    @unitary_product_amount.setter
    def unitary_product_amount(self, value):
        """Sets the amount of Declared Units contained within the product.

        Args:
            value (float): The unitary product amount to set.

        Raises:
            ValueError: If value is not greater than 0.
        """
        if value <= 0:
            raise ValueError("unitary_product_amount must be strictly greater than 0")
        self._unitary_product_amount = value

    @property
    def p_cf_excluding_biogenic(self):
        """Gets the product carbon footprint excluding biogenic CO2 emissions.

        Returns:
            float: The product carbon footprint excluding biogenic CO2 emissions.
        """
        return self._p_cf_excluding_biogenic

    @p_cf_excluding_biogenic.setter
    def p_cf_excluding_biogenic(self, value):
        """Sets the product carbon footprint excluding biogenic CO2 emissions.

        Args:
            value (float): The carbon footprint to set.

        Raises:
            ValueError: If value is negative.
        """
        if value < 0:
            raise ValueError("p_cf_excluding_biogenic must be equal to or greater than 0")
        self._p_cf_excluding_biogenic = value

    @property
    def fossil_ghg_emissions(self):
        """Gets the emissions from fossil sources.

        Returns:
            float: The fossil GHG emissions.
        """
        return self._fossil_ghg_emissions

    @fossil_ghg_emissions.setter
    def fossil_ghg_emissions(self, value):
        """Sets the emissions from fossil sources.

        Args:
            value (float): The emissions to set.

        Raises:
            ValueError: If value is negative.
        """
        if value < 0:
            raise ValueError("fossil_ghg_emissions must be equal to or greater than 0")
        self._fossil_ghg_emissions = value

    @property
    def fossil_carbon_content(self):
        """Gets the fossil carbon content of the product.

        Returns:
            float: The fossil carbon content.
        """
        return self._fossil_carbon_content

    @fossil_carbon_content.setter
    def fossil_carbon_content(self, value):
        """Sets the fossil carbon content of the product.

        Args:
            value (float): The carbon content to set.

        Raises:
            ValueError: If value is negative.
        """
        if value < 0:
            raise ValueError("fossil_carbon_content must be equal to or greater than 0")
        self._fossil_carbon_content = value

    @property
    def biogenic_carbon_content(self):
        """Gets the biogenic carbon content of the product.

        Returns:
            float: The biogenic carbon content.
        """
        return self._biogenic_carbon_content

    @biogenic_carbon_content.setter
    def biogenic_carbon_content(self, value):
        """Sets the biogenic carbon content of the product.

        Args:
            value (float): The carbon content to set.

        Raises:
            ValueError: If value is negative.
        """
        if value < 0:
            raise ValueError("biogenic_carbon_content must be equal to or greater than 0")
        self._biogenic_carbon_content = value

    @property
    def characterization_factors(self):
        """Gets the characterization factors used in the PCF calculation.

        Returns:
            CharacterizationFactors: The characterization factors.
        """
        return self._characterization_factors

    @characterization_factors.setter
    def characterization_factors(self, value):
        """Sets the characterization factors used in the PCF calculation.

        Args:
            value (CharacterizationFactors): The factors to set.

        Raises:
            ValueError: If value is not an instance of CharacterizationFactors.
        """
        if not isinstance(value, CharacterizationFactors):
            raise ValueError("characterization_factors must be an instance of CharacterizationFactors")
        self._characterization_factors = value

    @property
    def ipcc_characterization_factors_sources(self):
        """Gets the IPCC characterization factors sources.

        Returns:
            list[str]: The sources of the characterization factors.
        """
        return self._ipcc_characterization_factors_sources

    @ipcc_characterization_factors_sources.setter
    def ipcc_characterization_factors_sources(self, value):
        """Sets the IPCC characterization factors sources.

        Args:
            value (list[str]): The sources to set.

        Raises:
            ValueError: If value is empty.
        """
        if not value:
            raise ValueError("ipcc_characterization_factors_sources must not be empty")
        self._ipcc_characterization_factors_sources = value

    @property
    def cross_sectoral_standards_used(self) -> CrossSectoralStandardSet:
        """Gets the cross-sectoral standards used for GHG emissions.

        Returns:
            CrossSectoralStandardSet: The cross-sectoral standards.
        """
        return self._cross_sectoral_standards_used

    @cross_sectoral_standards_used.setter
    def cross_sectoral_standards_used(self, value: CrossSectoralStandardSet) -> None:
        """Sets the cross-sectoral standards used for GHG emissions.

        Args:
            value (CrossSectoralStandardSet): The standards to set.

        Raises:
            ValueError: If value is not an instance of CrossSectoralStandardSet.
        """
        if not isinstance(value, CrossSectoralStandardSet):
            raise ValueError("cross_sectoral_standards_used must be an instance of CrossSectoralStandardSet")
        self._cross_sectoral_standards_used = value

    @property
    def boundary_processes_description(self):
        """Gets the description of boundary processes.

        Returns:
            str: The description of boundary processes.
        """
        return self._boundary_processes_description

    @boundary_processes_description.setter
    def boundary_processes_description(self, value):
        """Sets the description of boundary processes.

        Args:
            value (str): The description to set.

        Raises:
            ValueError: If value is empty.
        """
        if not value:
            raise ValueError("boundary_processes_description must not be empty")
        self._boundary_processes_description = value

    @property
    def secondary_emission_factor_sources(self):
        """Gets the secondary emission factor sources.

        Returns:
            EmissionFactorDSSet | None: The secondary emission factor sources.
        """
        return self._secondary_emission_factor_sources

    @secondary_emission_factor_sources.setter
    def secondary_emission_factor_sources(self, value):
        """Sets the secondary emission factor sources.

        Args:
            value (EmissionFactorDSSet | None): The sources to set.

        Raises:
            ValueError: If value is not an instance of EmissionFactorDSSet.
        """
        if value is not None and not isinstance(value, EmissionFactorDSSet):
            raise ValueError("secondary_emission_factor_sources must be an instance of EmissionFactorDSSet")
        self._secondary_emission_factor_sources = value

    @property
    def exempted_emissions_percent(self):
        """Gets the percent of emissions excluded from the PCF.

        Returns:
            float: The percent of emissions excluded.
        """
        return self._exempted_emissions_percent

    @exempted_emissions_percent.setter
    def exempted_emissions_percent(self, value):
        """Sets the percent of emissions excluded from the PCF.

        Args:
            value (float): The percent to set.

        Raises:
            ValueError: If value is not between 0.0 and 5.0 inclusive.
        """
        if not 0.0 <= value <= 5.0:
            raise ValueError("exempted_emissions_percent must be between 0.0 and 5.0")
        self._exempted_emissions_percent = value

    @property
    def exempted_emissions_description(self):
        """Gets the description of exempted emissions.

        Returns:
            str: The description of exempted emissions.
        """
        return self._exempted_emissions_description

    @exempted_emissions_description.setter
    def exempted_emissions_description(self, value):
        """Sets the description of exempted emissions.

        Args:
            value (str): The description to set.

        Raises:
            ValueError: If value is not a string.
        """
        if not isinstance(value, str):
            raise ValueError("exempted_emissions_description must be a string")
        self._exempted_emissions_description = value

    @property
    def reference_period(self):
        """Gets the reference period for the carbon footprint.

        Returns:
            ReferencePeriod: The reference period.
        """
        return self._reference_period

    @reference_period.setter
    def reference_period(self, value):
        """Sets the reference period for the carbon footprint.

        Args:
            value (ReferencePeriod): The reference period to set.

        Raises:
            ValueError: If value is not an instance of ReferencePeriod.
        """
        if not isinstance(value, ReferencePeriod):
            raise ValueError("reference_period must be an instance of ReferencePeriod")
        self._reference_period = value

    @property
    def packaging_emissions_included(self):
        """Gets whether packaging emissions are included in the PCF.

        Returns:
            bool: True if packaging emissions are included, otherwise False.
        """
        return self._packaging_emissions_included

    @packaging_emissions_included.setter
    def packaging_emissions_included(self, value):
        """Sets whether packaging emissions are included in the PCF.

        Args:
            value (bool): True to include packaging emissions, otherwise False.

        Raises:
            ValueError: If value is not a boolean.
        """
        if not isinstance(value, bool):
            raise ValueError("packaging_emissions_included must be a boolean")
        self._packaging_emissions_included = value

    @property
    def geographical_scope(self):
        """Gets the geographical scope of the carbon footprint.

        Returns:
            CarbonFootprintGeographicalScope: The geographical scope.
        """
        return self._geographical_scope

    @geographical_scope.setter
    def geographical_scope(self, value):
        """Sets the geographical scope of the carbon footprint.

        Args:
            value (CarbonFootprintGeographicalScope): The geographical scope to set.

        Raises:
            ValueError: If value is not an instance of CarbonFootprintGeographicalScope.
        """
        if not isinstance(value, CarbonFootprintGeographicalScope):
            raise ValueError("geographical_scope must be an instance of CarbonFootprintGeographicalScope")
        self._geographical_scope = value

    @property
    def p_cf_including_biogenic(self):
        """Gets the carbon footprint including all biogenic emissions.

        Returns:
            float | None: The carbon footprint including biogenic emissions.
        """
        return self._p_cf_including_biogenic

    @p_cf_including_biogenic.setter
    def p_cf_including_biogenic(self, value):
        """Sets the carbon footprint including all biogenic emissions.

        Args:
            value (float | None): The carbon footprint to set.

        Raises:
            ValueError: If value is not a number or None.
        """
        if value is not None and not isinstance(value, (int, float)):
            raise ValueError("p_cf_including_biogenic must be a number")
        self._p_cf_including_biogenic = value

    @property
    def primary_data_share(self):
        """Gets the share of primary data in percent.

        Returns:
            float | None: The share of primary data.
        """
        return self._primary_data_share

    @primary_data_share.setter
    def primary_data_share(self, value):
        """Sets the share of primary data in percent.

        Args:
            value (float | None): The share to set.

        Raises:
            ValueError: If value is not a number or None.
        """
        if not isinstance(value, (int, float)) and value is not None:
            raise ValueError("primary_data_share must be a number")
        self._primary_data_share = value

    @property
    def dqi(self):
        """Gets the data quality indicators for the carbon footprint.

        Returns:
            DataQualityIndicators | None: The data quality indicators.
        """
        return self._dqi

    @dqi.setter
    def dqi(self, value):
        """Sets the data quality indicators for the carbon footprint.

        Args:
            value (DataQualityIndicators | None): The data quality indicators to set.

        Raises:
            ValueError: If value is not an instance of DataQualityIndicators or None.
        """
        if value is not None and not isinstance(value, DataQualityIndicators):
            raise ValueError("dqi must be an instance of DataQualityIndicators")
        self._dqi = value

    @property
    def d_luc_ghg_emissions(self):
        """Gets the emissions from direct land use change.

        Returns:
            float | None: The emissions from direct land use change.
        """
        return self._d_luc_ghg_emissions

    @d_luc_ghg_emissions.setter
    def d_luc_ghg_emissions(self, value):
        """Sets the emissions from direct land use change.

        Args:
            value (float | None): The emissions to set.

        Raises:
            ValueError: If value is not a non-negative number or None.
        """
        if value is not None and (not isinstance(value, (int, float)) or value < 0):
            raise ValueError("d_luc_ghg_emissions must be a non-negative number")
        self._d_luc_ghg_emissions = value

    @property
    def land_management_ghg_emissions(self):
        """Gets the emissions from land management activities.

        Returns:
            float | None: The emissions from land management activities.
        """
        return self._land_management_ghg_emissions

    @land_management_ghg_emissions.setter
    def land_management_ghg_emissions(self, value):
        """Sets the emissions from land management activities.

        Args:
            value (float | None): The emissions to set.

        Raises:
            ValueError: If value is not a number or None.
        """
        if value is not None and not isinstance(value, (int, float)):
            raise ValueError("land_management_ghg_emissions must be a number")
        self._land_management_ghg_emissions = value

    @property
    def other_biogenic_ghg_emissions(self):
        """Gets the other biogenic GHG emissions.

        Returns:
            float | None: The other biogenic GHG emissions.
        """
        return self._other_biogenic_ghg_emissions

    @other_biogenic_ghg_emissions.setter
    def other_biogenic_ghg_emissions(self, value):
        """Sets the other biogenic GHG emissions.

        Args:
            value (float | None): The emissions to set.

        Raises:
            ValueError: If value is not a non-negative number or None.
        """
        if value is not None and (not isinstance(value, (int, float)) or value < 0):
            raise ValueError("other_biogenic_ghg_emissions must be a non-negative number")
        self._other_biogenic_ghg_emissions = value

    @property
    def biogenic_carbon_withdrawal(self):
        """Gets the biogenic carbon withdrawal.

        Returns:
            float | None: The biogenic carbon withdrawal.
        """
        return self._biogenic_carbon_withdrawal

    @biogenic_carbon_withdrawal.setter
    def biogenic_carbon_withdrawal(self, value):
        """Sets the biogenic carbon withdrawal.

        Args:
            value (float | None): The withdrawal to set.

        Raises:
            ValueError: If value is not a non-positive number or None.
        """
        if value is not None and (not isinstance(value, (int, float)) or value > 0):
            raise ValueError("biogenic_carbon_withdrawal must be a non-positive number")
        self._biogenic_carbon_withdrawal = value

    @property
    def iluc_ghg_emissions(self):
        """Gets the emissions from indirect land use change.

        Returns:
            float | None: The emissions from indirect land use change.
        """
        return self._iluc_ghg_emissions

    @iluc_ghg_emissions.setter
    def iluc_ghg_emissions(self, value):
        """Sets the emissions from indirect land use change.

        Args:
            value (float | None): The emissions to set.

        Raises:
            ValueError: If value is not a non-negative number or None.
        """
        if value is not None and (not isinstance(value, (int, float)) or value < 0):
            raise ValueError("iluc_ghg_emissions must be a non-negative number")
        self._iluc_ghg_emissions = value

    @property
    def aircraft_ghg_emissions(self):
        """Gets the GHG emissions from aircraft transport.

        Returns:
            float | None: The GHG emissions from aircraft transport.
        """
        return self._aircraft_ghg_emissions

    @aircraft_ghg_emissions.setter
    def aircraft_ghg_emissions(self, value):
        """Sets the GHG emissions from aircraft transport.

        Args:
            value (float | None): The emissions to set.

        Raises:
            ValueError: If value is not a non-negative number or None.
        """
        if value is not None and (not isinstance(value, (int, float)) or value < 0):
            raise ValueError("aircraft_ghg_emissions must be a non-negative number")
        self._aircraft_ghg_emissions = value

    @property
    def packaging_ghg_emissions(self):
        """Gets the emissions from product packaging.

        Returns:
            float | None: The emissions from product packaging.
        """
        return self._packaging_ghg_emissions

    @packaging_ghg_emissions.setter
    def packaging_ghg_emissions(self, value):
        """Sets the emissions from product packaging.

        Args:
            value (float | None): The emissions to set.

        Raises:
            ValueError: If packaging emissions are not included and value is defined, or if value is not a non-negative number when packaging emissions are included.
        """
        if self.packaging_emissions_included and (value is None or not isinstance(value, (int, float)) or value < 0):
            raise ValueError("packaging_ghg_emissions must be a non-negative number if packaging_emissions_included is true")
        elif value is not None and not self.packaging_emissions_included:
            raise ValueError("packaging_ghg_emissions must not be defined if packaging_emissions_included is false")
        self._packaging_ghg_emissions = value

    @property
    def allocation_rules_description(self):
        """Gets the description of allocation rules applied.

        Returns:
            str | None: The description of allocation rules.
        """
        return self._allocation_rules_description

    @allocation_rules_description.setter
    def allocation_rules_description(self, value):
        """Sets the description of allocation rules applied.

        Args:
            value (str | None): The description to set.

        Raises:
            ValueError: If value is not a string or None.
        """
        if value is not None and not isinstance(value, str):
            raise ValueError("allocation_rules_description must be a string")
        self._allocation_rules_description = value

    @property
    def uncertainty_assessment_description(self):
        """Gets the description of the uncertainty assessment.

        Returns:
            str | None: The description of the uncertainty assessment.
        """
        return self._uncertainty_assessment_description

    @uncertainty_assessment_description.setter
    def uncertainty_assessment_description(self, value):
        """Sets the description of the uncertainty assessment.

        Args:
            value (str | None): The description to set.

        Raises:
            ValueError: If value is not a string or None.
        """
        if value is not None and not isinstance(value, str):
            raise ValueError("uncertainty_assessment_description must be a string")
        self._uncertainty_assessment_description = value

    @property
    def assurance(self):
        """Gets the assurance information.

        Returns:
            Assurance | None: The assurance information.
        """
        return self._assurance

    @assurance.setter
    def assurance(self, value):
        """Sets the assurance information.

        Args:
            value (Assurance | None): The assurance information to set.

        Raises:
            ValueError: If value is not an instance of Assurance or None.
        """
        if value is not None and not isinstance(value, Assurance):
            raise ValueError("assurance must be an instance of Assurance")
        self._assurance = value

    @property
    def biogenic_accounting_methodology(self):
        """Gets the biogenic carbon accounting methodology.

        Returns:
            BiogenicAccountingMethodology | None: The biogenic accounting methodology.
        """
        return self._biogenic_accounting_methodology

    @biogenic_accounting_methodology.setter
    def biogenic_accounting_methodology(self, value):
        """Sets the biogenic carbon accounting methodology.

        Args:
            value (BiogenicAccountingMethodology | None): The methodology to set.

        Raises:
            ValueError: If value is not an instance of BiogenicAccountingMethodology or None.
        """
        if value is not None and not isinstance(value, BiogenicAccountingMethodology):
            raise ValueError("biogenic_accounting_methodology must be an instance of BiogenicAccountingMethodology")
        self._biogenic_accounting_methodology = value

    @property
    def product_or_sector_specific_rules(self):
        """Gets the product or sector-specific rules.

        Returns:
            ProductOrSectorSpecificRuleSet | None: The specific rules applied.
        """
        return self._product_or_sector_specific_rules

    @product_or_sector_specific_rules.setter
    def product_or_sector_specific_rules(self, value):
        """Sets the product or sector-specific rules.

        Args:
            value (ProductOrSectorSpecificRuleSet | None): The specific rules to set.

        Raises:
            ValueError: If value is not an instance of ProductOrSectorSpecificRuleSet or None.
        """
        if value is not None and not isinstance(value, ProductOrSectorSpecificRuleSet):
            raise ValueError("product_or_sector_specific_rules must be an instance of ProductOrSectorSpecificRuleSet")
        self._product_or_sector_specific_rules = value

    def __str__(self):
        return (
            f"CarbonFootprint("
            f"declared_unit={self.declared_unit}, "
            f"unitary_product_amount={self.unitary_product_amount}, "
            f"p_cf_excluding_biogenic={self.p_cf_excluding_biogenic}, "
            f"p_cf_including_biogenic={self.p_cf_including_biogenic}, "
            f"fossil_ghg_emissions={self.fossil_ghg_emissions}, "
            f"fossil_carbon_content={self.fossil_carbon_content}, "
            f"biogenic_carbon_content={self.biogenic_carbon_content}, "
            f"characterization_factors={self.characterization_factors.value}, "
            f"ipcc_characterization_factors_sources={self.ipcc_characterization_factors_sources}, "
            f"cross_sectoral_standards_used={self.cross_sectoral_standards_used}, "
            f"boundary_processes_description='{self.boundary_processes_description}', "
            f"exempted_emissions_percent={self.exempted_emissions_percent}, "
            f"exempted_emissions_description='{self.exempted_emissions_description}', "
            f"reference_period={self.reference_period}, "
            f"packaging_emissions_included={self.packaging_emissions_included}, "
            f"geographical_scope={self.geographical_scope}, "
            f"primary_data_share={self.primary_data_share}, "
            f"dqi={self.dqi}, "
            f"secondary_emission_factor_sources={self.secondary_emission_factor_sources}, "
            f"d_luc_ghg_emissions={self.d_luc_ghg_emissions}, "
            f"land_management_ghg_emissions={self.land_management_ghg_emissions}, "
            f"other_biogenic_ghg_emissions={self.other_biogenic_ghg_emissions}, "
            f"biogenic_carbon_withdrawal={self.biogenic_carbon_withdrawal}, "
            f"iluc_ghg_emissions={self.iluc_ghg_emissions}, "
            f"aircraft_ghg_emissions={self.aircraft_ghg_emissions}, "
            f"packaging_ghg_emissions={self.packaging_ghg_emissions}, "
            f"allocation_rules_description='{self.allocation_rules_description}', "
            f"uncertainty_assessment_description='{self.uncertainty_assessment_description}', "
            f"assurance={self.assurance}, "
            f"biogenic_accounting_methodology={self.biogenic_accounting_methodology.value}, "
            f"product_or_sector_specific_rules={self.product_or_sector_specific_rules})"
        )

    def __repr__(self):
        return (
            f"CarbonFootprint("
            f"declared_unit={self.declared_unit!r}, "
            f"unitary_product_amount={self.unitary_product_amount!r}, "
            f"p_cf_excluding_biogenic={self.p_cf_excluding_biogenic!r}, "
            f"p_cf_including_biogenic={self.p_cf_including_biogenic!r}, "
            f"fossil_ghg_emissions={self.fossil_ghg_emissions!r}, "
            f"fossil_carbon_content={self.fossil_carbon_content!r}, "
            f"biogenic_carbon_content={self.biogenic_carbon_content!r}, "
            f"characterization_factors={self.characterization_factors!r}, "
            f"ipcc_characterization_factors_sources={self.ipcc_characterization_factors_sources!r}, "
            f"cross_sectoral_standards_used={self.cross_sectoral_standards_used!r}, "
            f"boundary_processes_description={self.boundary_processes_description!r}, "
            f"exempted_emissions_percent={self.exempted_emissions_percent!r}, "
            f"exempted_emissions_description={self.exempted_emissions_description!r}, "
            f"reference_period={self.reference_period!r}, "
            f"packaging_emissions_included={self.packaging_emissions_included!r}, "
            f"geographical_scope={self.geographical_scope!r}, "
            f"primary_data_share={self.primary_data_share!r}, "
            f"dqi={self.dqi!r}, "
            f"secondary_emission_factor_sources={self.secondary_emission_factor_sources!r}, "
            f"d_luc_ghg_emissions={self.d_luc_ghg_emissions!r}, "
            f"land_management_ghg_emissions={self.land_management_ghg_emissions!r}, "
            f"other_biogenic_ghg_emissions={self.other_biogenic_ghg_emissions!r}, "
            f"biogenic_carbon_withdrawal={self.biogenic_carbon_withdrawal!r}, "
            f"iluc_ghg_emissions={self.iluc_ghg_emissions!r}, "
            f"aircraft_ghg_emissions={self.aircraft_ghg_emissions!r}, "
            f"packaging_ghg_emissions={self.packaging_ghg_emissions!r}, "
            f"allocation_rules_description={self.allocation_rules_description!r}, "
            f"uncertainty_assessment_description={self.uncertainty_assessment_description!r}, "
            f"assurance={self.assurance!r}, "
            f"biogenic_accounting_methodology={self.biogenic_accounting_methodology!r}, "
            f"product_or_sector_specific_rules={self.product_or_sector_specific_rules!r})"
        )

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)