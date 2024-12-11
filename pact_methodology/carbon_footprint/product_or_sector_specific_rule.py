from pact_methodology.carbon_footprint.product_or_sector_specific_rule_operator import (
    ProductOrSectorSpecificRuleOperator
)


class ProductOrSectorSpecificRule:
    """Represents a product or sector specific rule for calculating carbon footprints.

    This class represents rules and methodologies published by specific operators that must be followed
    when calculating product carbon footprints. These rules can come from various sources like PEF
    (Product Environmental Footprint) or custom operators.

    Attributes:
        operator (ProductOrSectorSpecificRuleOperator): The operator that published the specific rule.
            Must be a valid ProductOrSectorSpecificRuleOperator enum value.
        rule_names (list[str]): A list of names of the rules applied from the specified operator.
            Each rule name must be a string.
        other_operator_name (str | None): The name of the operator if the operator is 'Other'.
            Required when operator is ProductOrSectorSpecificRuleOperator.OTHER, must be None otherwise.

    Examples:
        Create a rule for PEF methodology:
        >>> rule = ProductOrSectorSpecificRule(
        ...     operator=ProductOrSectorSpecificRuleOperator.PEF,
        ...     rule_names=["PEFCR Guidance v6.3"]
        ... )

        Create a rule with a custom operator:
        >>> custom_rule = ProductOrSectorSpecificRule(
        ...     operator=ProductOrSectorSpecificRuleOperator.OTHER,
        ...     rule_names=["Custom Rule 1", "Custom Rule 2"],
        ...     other_operator_name="My Organization"
        ... )

        Convert rule to dictionary format:
        >>> rule.to_dict()
        {
            'operator': 'PEF',
            'ruleNames': ['PEFCR Guidance v6.3']
        }

    Raises:
        ValueError: If operator is not a valid ProductOrSectorSpecificRuleOperator,
            if rule_names is not a list of strings, or if other_operator_name is provided
            incorrectly based on the operator value.
        TypeError: If required arguments are missing during initialization.

    Note:
        The other_operator_name is only valid and required when operator is set to
        ProductOrSectorSpecificRuleOperator.OTHER. For all other operators, it must be None.
    """

    def __init__(
        self,
        operator: ProductOrSectorSpecificRuleOperator,
        rule_names: list[str],
        other_operator_name: str | None = None
    ):
        """Initialize a ProductOrSectorSpecificRule instance.

        Args:
            operator: The operator publishing the rule (e.g. PEF, GHG Protocol)
            rule_names: List of specific rule names from the operator
            other_operator_name: Name of custom operator if operator is "Other"

        Raises:
            ValueError: If arguments are invalid
            TypeError: If required arguments are missing
        """
        self.operator = operator
        self.rule_names = rule_names
        self.other_operator_name = other_operator_name

    @property
    def operator(self) -> ProductOrSectorSpecificRuleOperator:
        """Get the rule operator.

        Returns:
            The ProductOrSectorSpecificRuleOperator enum value
        """
        return self._operator

    @operator.setter
    def operator(self, value: ProductOrSectorSpecificRuleOperator):
        """Set the rule operator.

        Args:
            value: The operator enum value to set

        Raises:
            ValueError: If value is not a ProductOrSectorSpecificRuleOperator
        """
        if not isinstance(value, ProductOrSectorSpecificRuleOperator):
            raise ValueError("operator must be an instance of ProductOrSectorSpecificRuleOperator")
        self._operator = value

    @property
    def rule_names(self) -> list[str]:
        """Get the list of rule names.

        Returns:
            List of rule name strings
        """
        return self._rule_names

    @rule_names.setter
    def rule_names(self, value: list[str]):
        """Set the list of rule names.

        Args:
            value: List of rule name strings

        Raises:
            ValueError: If value is not a list of strings
        """
        if not isinstance(value, list) or not all(isinstance(rule, str) for rule in value):
            raise ValueError("rule_names must be a list of strings")
        self._rule_names = value

    @property
    def other_operator_name(self) -> str | None:
        """Get the custom operator name if operator is "Other".

        Returns:
            The custom operator name string or None
        """
        return self._other_operator_name

    @other_operator_name.setter
    def other_operator_name(self, value: str | None):
        """Set the custom operator name.

        Args:
            value: The custom operator name string or None

        Raises:
            ValueError: If value is provided incorrectly based on operator
        """
        if self.operator == ProductOrSectorSpecificRuleOperator.OTHER and not value:
            raise ValueError("other_operator_name must be provided if operator is 'Other'")
        if self.operator != ProductOrSectorSpecificRuleOperator.OTHER and value:
            raise ValueError("other_operator_name must not be provided if operator is not 'Other'")
        self._other_operator_name = value

    def to_dict(self) -> dict:
        """Convert the rule to a dictionary representation.

        Returns:
            A dictionary with the following structure:
            {
                "operator": str,  # The operator value
                "ruleNames": list[str],  # List of rule names
                "otherOperatorName": str | None  # Custom operator name if applicable
            }
        """
        rule_dict = {
            "operator": self.operator.value,
            "ruleNames": self.rule_names,
        }

        if self.operator == ProductOrSectorSpecificRuleOperator.OTHER:
            rule_dict["otherOperatorName"] = self.other_operator_name

        return rule_dict

    def __str__(self) -> str:
        """Get string representation of the rule.

        Returns:
            A human-readable string showing the rule's attributes
        """
        return (
            f"operator={self.operator}, rule_names={self.rule_names}, other_operator_name={self.other_operator_name}"
        )
    
    def __repr__(self) -> str:
        """Get detailed string representation of the rule.

        Returns:
            A string that could be used to recreate the object
        """
        return (
            f"ProductOrSectorSpecificRule(operator={self.operator!r}, "
            f"rule_names={self.rule_names!r}, other_operator_name={self.other_operator_name!r})"
        )
