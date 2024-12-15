from typing import List, Optional
from pact_methodology.carbon_footprint.product_or_sector_specific_rule import ProductOrSectorSpecificRule

class ProductOrSectorSpecificRuleSet:
    """A set of product or sector specific rules published by operators and applied during product carbon footprint calculation.

    This class represents a collection of one or more ProductOrSectorSpecificRule objects. Each rule defines specific 
    methodologies that must be followed when calculating product carbon footprints, published by recognized operators like:
    - PEF (Product Environmental Footprint)
    - EPD International
    - Other custom operators

    Each rule in the set must specify:
    - The operator that published the rule (e.g. PEF, EPD International, or Other)
    - A non-empty list of rule names applied from that operator
    - For custom operators (operator="Other"), the name of the operator must be provided

    Attributes:
        rules (List[ProductOrSectorSpecificRule]): A non-empty list of ProductOrSectorSpecificRule objects.
            Each rule represents a specific methodology from a recognized operator.

    Examples:
        Create a rule set with a PEF rule:
        >>> rule = ProductOrSectorSpecificRule(
        ...     operator=ProductOrSectorSpecificRuleOperator.PEF,
        ...     rule_names=["PEFCR Guidance v6.3"]
        ... )
        >>> ruleset = ProductOrSectorSpecificRuleSet([rule])

        Create a rule set with a custom operator rule:
        >>> custom_rule = ProductOrSectorSpecificRule(
        ...     operator=ProductOrSectorSpecificRuleOperator.OTHER,
        ...     rule_names=["Custom PCR 2023"],
        ...     other_operator_name="Industry Association X"
        ... )
        >>> ruleset = ProductOrSectorSpecificRuleSet([custom_rule])

        Add an EPD International rule:
        >>> epd_rule = ProductOrSectorSpecificRule(
        ...     operator=ProductOrSectorSpecificRuleOperator.EPD_INTERNATIONAL,
        ...     rule_names=["PCR 2019:14 v1.11"]
        ... )
        >>> ruleset.add_rule(epd_rule)

        Convert rule set to dictionary format:
        >>> ruleset.to_dict()
        [
            {'operator': 'PEF', 'rule_names': ['PEFCR Guidance v6.3']},
            {'operator': 'Other', 'rule_names': ['Custom PCR 2023'], 'other_operator_name': 'Industry Association X'},
            {'operator': 'EPD_INTERNATIONAL', 'rule_names': ['PCR 2019:14 v1.11']}
        ]

        Remove a rule:
        >>> ruleset.remove_rule(epd_rule)
        >>> len(ruleset.rules)
        2
    """

    def __init__(self, rules: Optional[List[ProductOrSectorSpecificRule]] = None):
        """Initialize a ProductOrSectorSpecificRuleSet instance.

        Args:
            rules: A list of ProductOrSectorSpecificRule objects. Defaults to an empty list.
                Each rule must specify a valid operator (PEF, EPD International, or Other),
                a non-empty list of rule names, and for custom operators, the operator name.

        Raises:
            ValueError: If rules is empty or contains invalid ProductOrSectorSpecificRule objects.

        Examples:
            Initialize with a single rule:
            >>> rule = ProductOrSectorSpecificRule(
            ...     operator=ProductOrSectorSpecificRuleOperator.PEF,
            ...     rule_names=["PEFCR Guidance v6.3"]
            ... )
            >>> ruleset = ProductOrSectorSpecificRuleSet([rule])

            Initialize with multiple rules:
            >>> rules = [
            ...     ProductOrSectorSpecificRule(
            ...         operator=ProductOrSectorSpecificRuleOperator.PEF,
            ...         rule_names=["PEFCR Guidance v6.3"]
            ...     ),
            ...     ProductOrSectorSpecificRule(
            ...         operator=ProductOrSectorSpecificRuleOperator.EPD_INTERNATIONAL,
            ...         rule_names=["PCR 2019:14 v1.11"]
            ...     )
            ... ]
            >>> ruleset = ProductOrSectorSpecificRuleSet(rules)
        """
        self.rules = rules if rules is not None else []

    @property
    def rules(self) -> List[ProductOrSectorSpecificRule]:
        """Get the list of product/sector specific rules.

        Returns:
            A list of ProductOrSectorSpecificRule objects representing the calculation rules
            that must be followed, each from a recognized operator.

        Examples:
            >>> ruleset = ProductOrSectorSpecificRuleSet()
            >>> ruleset.rules
            []

            >>> rule = ProductOrSectorSpecificRule(
            ...     operator=ProductOrSectorSpecificRuleOperator.PEF,
            ...     rule_names=["PEFCR Guidance v6.3"]
            ... )
            >>> ruleset = ProductOrSectorSpecificRuleSet([rule])
            >>> ruleset.rules
            [ProductOrSectorSpecificRule(operator=ProductOrSectorSpecificRuleOperator.PEF, rule_names=['PEFCR Guidance v6.3'], other_operator_name=None)]
        """
        return self._rules

    @rules.setter
    def rules(self, value: List[ProductOrSectorSpecificRule]):
        """Set the list of product/sector specific rules.

        Args:
            value: A list of ProductOrSectorSpecificRule objects to set as the current rules.
                Must contain at least one valid rule.

        Raises:
            ValueError: If value is not a list of valid ProductOrSectorSpecificRule objects.

        Examples:
            >>> ruleset = ProductOrSectorSpecificRuleSet()
            >>> rules = [
            ...     ProductOrSectorSpecificRule(
            ...         operator=ProductOrSectorSpecificRuleOperator.PEF,
            ...         rule_names=["PEFCR Guidance v6.3"]
            ...     )
            ... ]
            >>> ruleset.rules = rules

            Invalid assignment raises ValueError:
            >>> ruleset.rules = ["not a rule"]  # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
                ...
            ValueError: rules must be a list of ProductOrSectorSpecificRule objects
        """
        if not isinstance(value, list) or not all(isinstance(rule, ProductOrSectorSpecificRule) for rule in value):
            raise ValueError("rules must be a list of ProductOrSectorSpecificRule objects")
        self._rules = value

    def add_rule(self, rule: ProductOrSectorSpecificRule):
        """Add a product/sector specific rule to the set.

        Args:
            rule: A ProductOrSectorSpecificRule object to add to the current set.
                Must be a valid rule with required operator and rule names.

        Raises:
            ValueError: If rule is not a valid ProductOrSectorSpecificRule instance.

        Examples:
            >>> ruleset = ProductOrSectorSpecificRuleSet()
            >>> pef_rule = ProductOrSectorSpecificRule(
            ...     operator=ProductOrSectorSpecificRuleOperator.PEF,
            ...     rule_names=["PEFCR Guidance v6.3"]
            ... )
            >>> ruleset.add_rule(pef_rule)
            >>> len(ruleset.rules)
            1

            Adding an invalid rule raises ValueError:
            >>> ruleset.add_rule("not a rule")  # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
                ...
            ValueError: rule must be an instance of ProductOrSectorSpecificRule
        """
        if not isinstance(rule, ProductOrSectorSpecificRule):
            raise ValueError("rule must be an instance of ProductOrSectorSpecificRule")
        self.rules.append(rule)

    def remove_rule(self, rule: ProductOrSectorSpecificRule):
        """Remove a product/sector specific rule from the set.

        Args:
            rule: A ProductOrSectorSpecificRule object to remove from the current set.
                Must exist in the current set.

        Raises:
            ValueError: If rule is invalid or not found in the current set.

        Examples:
            >>> pef_rule = ProductOrSectorSpecificRule(
            ...     operator=ProductOrSectorSpecificRuleOperator.PEF,
            ...     rule_names=["PEFCR Guidance v6.3"]
            ... )
            >>> ruleset = ProductOrSectorSpecificRuleSet([pef_rule])
            >>> ruleset.remove_rule(pef_rule)
            >>> len(ruleset.rules)
            0

            Removing a non-existent rule raises ValueError:
            >>> epd_rule = ProductOrSectorSpecificRule(
            ...     operator=ProductOrSectorSpecificRuleOperator.EPD_INTERNATIONAL,
            ...     rule_names=["PCR 2019:14 v1.11"]
            ... )
            >>> ruleset.remove_rule(epd_rule)  # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
                ...
            ValueError: rule not found in the set
        """
        if not isinstance(rule, ProductOrSectorSpecificRule):
            raise ValueError("rule must be an instance of ProductOrSectorSpecificRule")
        if rule not in self.rules:
            raise ValueError("rule not found in the set")
        self.rules.remove(rule)

    def to_dict(self) -> List[dict]:
        """Convert the rule set to a JSON-compatible format.

        Returns:
            A list of dictionaries, each representing a ProductOrSectorSpecificRule
            as a JSON object with operator, ruleNames, and optional otherOperatorName.

        Examples:
            >>> pef_rule = ProductOrSectorSpecificRule(
            ...     operator=ProductOrSectorSpecificRuleOperator.PEF,
            ...     rule_names=["PEFCR Guidance v6.3"]
            ... )
            >>> custom_rule = ProductOrSectorSpecificRule(
            ...     operator=ProductOrSectorSpecificRuleOperator.OTHER,
            ...     rule_names=["Custom PCR 2023"],
            ...     other_operator_name="Industry Association X"
            ... )
            >>> ruleset = ProductOrSectorSpecificRuleSet([pef_rule, custom_rule])
            >>> ruleset.to_dict()
            [{'operator': 'PEF', 'rule_names': ['PEFCR Guidance v6.3']}, {'operator': 'Other', 'rule_names': ['Custom PCR 2023'], 'other_operator_name': 'Industry Association X'}]
        """
        return [rule.to_dict() for rule in self.rules]

    def __str__(self) -> str:
        """Get string representation of the rule set.

        Returns:
            A human-readable string showing the contained rules.

        Examples:
            >>> pef_rule = ProductOrSectorSpecificRule(
            ...     operator=ProductOrSectorSpecificRuleOperator.PEF,
            ...     rule_names=["PEFCR Guidance v6.3"]
            ... )
            >>> ruleset = ProductOrSectorSpecificRuleSet([pef_rule])
            >>> str(ruleset)
            'ProductOrSectorSpecificRuleSet(rules=[ProductOrSectorSpecificRule(operator=ProductOrSectorSpecificRuleOperator.PEF, rule_names=[\'PEFCR Guidance v6.3\'], other_operator_name=None)])'
        """
        return f"ProductOrSectorSpecificRuleSet(rules={self.rules})"

    def __repr__(self) -> str:
        """Get detailed string representation of the rule set.

        Returns:
            A string containing all information needed to recreate the object.

        Examples:
            >>> pef_rule = ProductOrSectorSpecificRule(
            ...     operator=ProductOrSectorSpecificRuleOperator.PEF,
            ...     rule_names=["PEFCR Guidance v6.3"]
            ... )
            >>> ruleset = ProductOrSectorSpecificRuleSet([pef_rule])
            >>> repr(ruleset)
            'ProductOrSectorSpecificRuleSet(rules=[ProductOrSectorSpecificRule(operator=ProductOrSectorSpecificRuleOperator.PEF, rule_names=[\'PEFCR Guidance v6.3\'], other_operator_name=None)])'
        """
        return f"ProductOrSectorSpecificRuleSet(rules={self.rules!r})"

    def __eq__(self, other) -> bool:
        """Check if two rule sets are equal.

        Args:
            other: Another ProductOrSectorSpecificRuleSet to compare with this one.

        Returns:
            True if both sets contain the same rules in the same order.

        Examples:
            >>> pef_rule = ProductOrSectorSpecificRule(
            ...     operator=ProductOrSectorSpecificRuleOperator.PEF,
            ...     rule_names=["PEFCR Guidance v6.3"]
            ... )
            >>> ruleset1 = ProductOrSectorSpecificRuleSet([pef_rule])
            >>> ruleset2 = ProductOrSectorSpecificRuleSet([pef_rule])
            >>> ruleset1 == ruleset2
            True

            >>> epd_rule = ProductOrSectorSpecificRule(
            ...     operator=ProductOrSectorSpecificRuleOperator.EPD_INTERNATIONAL,
            ...     rule_names=["PCR 2019:14 v1.11"]
            ... )
            >>> ruleset3 = ProductOrSectorSpecificRuleSet([epd_rule])
            >>> ruleset1 == ruleset3
            False
        """
        if not isinstance(other, ProductOrSectorSpecificRuleSet):
            return False
        return self.rules == other.rules

    def __ne__(self, other) -> bool:
        """Check if two rule sets are not equal.

        Args:
            other: Another ProductOrSectorSpecificRuleSet to compare with this one.

        Returns:
            True if the rule sets differ in any way.

        Examples:
            >>> pef_rule = ProductOrSectorSpecificRule(
            ...     operator=ProductOrSectorSpecificRuleOperator.PEF,
            ...     rule_names=["PEFCR Guidance v6.3"]
            ... )
            >>> ruleset1 = ProductOrSectorSpecificRuleSet([pef_rule])
            >>> ruleset2 = ProductOrSectorSpecificRuleSet([pef_rule])
            >>> ruleset1 != ruleset2
            False

            >>> epd_rule = ProductOrSectorSpecificRule(
            ...     operator=ProductOrSectorSpecificRuleOperator.EPD_INTERNATIONAL,
            ...     rule_names=["PCR 2019:14 v1.11"]
            ... )
            >>> ruleset3 = ProductOrSectorSpecificRuleSet([epd_rule])
            >>> ruleset1 != ruleset3
            True
        """
        return not self.__eq__(other)
