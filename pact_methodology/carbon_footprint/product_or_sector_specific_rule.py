from pact_methodology.carbon_footprint.product_or_sector_specific_rule_operator import (
    ProductOrSectorSpecificRuleOperator
)


class ProductOrSectorSpecificRule:
    """
    Represents a product or sector specific rule for calculating carbon footprints.

    Attributes:
        operator (ProductOrSectorSpecificRuleOperator): The operator that published the specific rule.
        rule_names (list[str]): A list of names of the rules applied from the specified operator.
        other_operator_name (str | None): The name of the operator if the operator is 'Other'.

    Args:
        operator (ProductOrSectorSpecificRuleOperator): The operator that published the specific rule.
        rule_names (list[str]): A list of names of the rules applied from the specified operator.
        other_operator_name (str | None): The name of the operator if the operator is 'Other'.

    Raises:
        ValueError: If the operator is 'Other' and other_operator_name is not provided, or if the operator is not
                    'Other' and other_operator_name is provided.
    """

    def __init__(self,
                 operator: ProductOrSectorSpecificRuleOperator,
                 rule_names: list[str],
                 other_operator_name: str | None = None):
        if not isinstance(operator, ProductOrSectorSpecificRuleOperator):
            raise ValueError("operator must be an instance of ProductOrSectorSpecificRuleOperator")

        if not isinstance(rule_names, list) or not all(isinstance(rule, str) for rule in rule_names):
            raise ValueError("rule_names must be a list of strings")

        if operator == ProductOrSectorSpecificRuleOperator.OTHER and not other_operator_name:
            raise ValueError("other_operator_name must be provided if operator is 'Other'")

        if operator != ProductOrSectorSpecificRuleOperator.OTHER and other_operator_name:
            raise ValueError("other_operator_name must not be provided if operator is not 'Other'")

        self.operator = operator
        self.rule_names = rule_names
        self.other_operator_name = other_operator_name

    def to_dict(self) -> dict:
        """
        Converts the ProductOrSectorSpecificRule instance to a dictionary representation.

        Returns:
            dict: A dictionary containing the operator, rule names, and other operator name if applicable.
        """
        rule_dict = {
            "operator": self.operator.value,
            "ruleNames": self.rule_names,
        }

        if self.operator == ProductOrSectorSpecificRuleOperator.OTHER:
            rule_dict["otherOperatorName"] = self.other_operator_name

        return rule_dict
