import pytest

from pathfinder_framework.carbon_footprint.product_or_sector_specific_rule import ProductOrSectorSpecificRule
from pathfinder_framework.carbon_footprint.product_or_sector_specific_rule_operator import ProductOrSectorSpecificRuleOperator


def test_product_or_sector_specific_rule_init():
    rule = ProductOrSectorSpecificRule(operator=ProductOrSectorSpecificRuleOperator.OTHER, rule_names=["Rule1"], other_operator_name="Custom Operator")


def test_product_or_sector_specific_rule_to_dict():
    rule = ProductOrSectorSpecificRule(operator=ProductOrSectorSpecificRuleOperator.OTHER, rule_names=["Rule1"], other_operator_name="Custom Operator")
    assert rule.to_dict() == {
        "operator": "Other",
        "ruleNames": ["Rule1"],
        "otherOperatorName": "Custom Operator",
    }


def test_init_with_invalid_operator():
    with pytest.raises(ValueError):
        ProductOrSectorSpecificRule(operator="Invalid Operator", rule_names=["Rule1"])


def test_init_with_invalid_rule_names():
    with pytest.raises(ValueError):
        ProductOrSectorSpecificRule(operator=ProductOrSectorSpecificRuleOperator.OTHER, rule_names="Invalid Rule Names")


def test_init_without_mandatory_operator():
    with pytest.raises(TypeError):
        ProductOrSectorSpecificRule(rule_names=["Rule1"])


def test_init_without_mandatory_rule_names():
    with pytest.raises(TypeError):
        ProductOrSectorSpecificRule(operator=ProductOrSectorSpecificRuleOperator.OTHER)


def test_other_operator_name_when_operator_not_other():
    with pytest.raises(ValueError):
        ProductOrSectorSpecificRule(operator=ProductOrSectorSpecificRuleOperator.PEF, rule_names=["Rule1"], other_operator_name="Should not be set")


def test_init_with_valid_operator():
    with pytest.raises(ValueError):
        ProductOrSectorSpecificRule(operator=ProductOrSectorSpecificRuleOperator.OTHER, rule_names=["Rule1"])


def test_init_with_valid_rule_names():
    with pytest.raises(ValueError):
        ProductOrSectorSpecificRule(operator=ProductOrSectorSpecificRuleOperator.OTHER, rule_names=["Rule1", "Rule2"])
