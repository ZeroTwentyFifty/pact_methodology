import pytest

from pathfinder_framework.carbon_footprint import ProductOrSectorSpecificRule
from pathfinder_framework.carbon_footprint.product_or_sector_specific_rule_operator import ProductOrSectorSpecificRuleOperator


def test_product_or_sector_specific_rule_init():
    with pytest.raises(NotImplementedError):
        rule = ProductOrSectorSpecificRule(operator=ProductOrSectorSpecificRuleOperator.OTHER, rule_names=["Rule1"])


def test_product_or_sector_specific_rule_to_dict():
    with pytest.raises(NotImplementedError):
        rule = ProductOrSectorSpecificRule(operator=ProductOrSectorSpecificRuleOperator.OTHER, rule_names=["Rule1"])
        rule.to_dict()


def test_init_with_invalid_operator():
    with pytest.raises(ValueError):
        ProductOrSectorSpecificRule(operator="Invalid Operator", rule_names=["Rule1"])


def test_init_with_invalid_rule_names():
    with pytest.raises(ValueError):
        ProductOrSectorSpecificRule(operator=ProductOrSectorSpecificRuleOperator.OTHER, rule_names="Invalid Rule Names")


def test_init_with_valid_other_operator_name():
    with pytest.raises(NotImplementedError):
        ProductOrSectorSpecificRule(operator=ProductOrSectorSpecificRuleOperator.OTHER, rule_names=["Rule1"], other_operator_name="Other Operator")


def test_init_without_mandatory_operator():
    with pytest.raises(ValueError):
        ProductOrSectorSpecificRule(rule_names=["Rule1"])


def test_init_without_mandatory_rule_names():
    with pytest.raises(ValueError):
        ProductOrSectorSpecificRule(operator=ProductOrSectorSpecificRuleOperator.OTHER)


def test_other_operator_name_when_operator_not_other():
    with pytest.raises(ValueError):
        ProductOrSectorSpecificRule(operator=ProductOrSectorSpecificRuleOperator.PEF, rule_names=["Rule1"], other_operator_name="Should not be set")


@pytest.mark.parametrize("operator", [ProductOrSectorSpecificRuleOperator.OTHER, ProductOrSectorSpecificRuleOperator.EPD_INTERNATIONAL])
def test_init_with_valid_operator(operator):
    with pytest.raises(NotImplementedError):
        ProductOrSectorSpecificRule(operator=operator, rule_names=["Rule1"])


@pytest.mark.parametrize("rule_names", [["Rule1", "Rule2"], ["Rule1", "Rule2"]])
def test_init_with_valid_rule_names(rule_names):
    with pytest.raises(NotImplementedError):
        ProductOrSectorSpecificRule(operator=ProductOrSectorSpecificRuleOperator.OTHER, rule_names=rule_names)
