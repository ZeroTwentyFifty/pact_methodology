import pytest

from pact_methodology.carbon_footprint.product_or_sector_specific_rule import (
    ProductOrSectorSpecificRule,
)
from pact_methodology.carbon_footprint.product_or_sector_specific_rule_operator import (
    ProductOrSectorSpecificRuleOperator,
)


@pytest.fixture
def valid_product_or_sector_specific_rule():
    return {
        "operator": ProductOrSectorSpecificRuleOperator.OTHER,
        "rule_names": ["Rule1"],
        "other_operator_name": "Custom Operator",
    }


def test_product_or_sector_specific_rule_init_valid(valid_product_or_sector_specific_rule):
    rule = ProductOrSectorSpecificRule(**valid_product_or_sector_specific_rule)
    assert rule.operator == ProductOrSectorSpecificRuleOperator.OTHER
    assert rule.rule_names == ["Rule1"]
    assert rule.other_operator_name == "Custom Operator"


def test_product_or_sector_specific_rule_init_invalid_operator(valid_product_or_sector_specific_rule):
    invalid_rule = {
        **valid_product_or_sector_specific_rule,
        "operator": "Invalid Operator",
    }
    with pytest.raises(ValueError, match="operator must be an instance of ProductOrSectorSpecificRuleOperator"):
        ProductOrSectorSpecificRule(**invalid_rule)


def test_product_or_sector_specific_rule_init_invalid_rule_names(valid_product_or_sector_specific_rule):
    invalid_rule = {
        **valid_product_or_sector_specific_rule,
        "rule_names": "Invalid Rule Names"
    }
    with pytest.raises(ValueError, match="rule_names must be a list of strings"):
        ProductOrSectorSpecificRule(**invalid_rule)


def test_product_or_sector_specific_rule_init_missing_operator():
    invalid_rule = {"rule_names": ["Rule1"]}
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'operator'"):
        ProductOrSectorSpecificRule(**invalid_rule)


def test_product_or_sector_specific_rule_init_missing_rule_names():
    invalid_rule = {"operator": ProductOrSectorSpecificRuleOperator.OTHER}
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'rule_names'"):
        ProductOrSectorSpecificRule(**invalid_rule)


def test_product_or_sector_specific_rule_init_other_operator_name_when_operator_not_other(valid_product_or_sector_specific_rule):
    invalid_rule = {
        **valid_product_or_sector_specific_rule,
        "operator": ProductOrSectorSpecificRuleOperator.PEF,
        "other_operator_name": "Should not be set"
    }
    with pytest.raises(ValueError, match="other_operator_name must not be provided if operator is not 'Other'"):
        ProductOrSectorSpecificRule(**invalid_rule)


def test_product_or_sector_specific_rule_init_valid_rule_names():
    rule = {
        "operator": ProductOrSectorSpecificRuleOperator.OTHER,
        "rule_names": ["Rule1", "Rule2"],
        "other_operator_name": "Custom Operator",
    }
    ProductOrSectorSpecificRule(**rule)


def test_product_or_sector_specific_rule_to_dict(valid_product_or_sector_specific_rule):
    rule = ProductOrSectorSpecificRule(**valid_product_or_sector_specific_rule)
    assert rule.to_dict() == {
        "operator": ProductOrSectorSpecificRuleOperator.OTHER,
        "ruleNames": ["Rule1"],
        "otherOperatorName": "Custom Operator",
    }


def test_product_or_sector_specific_rule_str(valid_product_or_sector_specific_rule):
    rule = ProductOrSectorSpecificRule(**valid_product_or_sector_specific_rule)
    expected_str = "operator=Other, rule_names=['Rule1'], other_operator_name=Custom Operator"
    assert str(rule) == expected_str


def test_product_or_sector_specific_rule_repr(valid_product_or_sector_specific_rule):
    rule = ProductOrSectorSpecificRule(**valid_product_or_sector_specific_rule)
    expected_repr = "ProductOrSectorSpecificRule(operator=ProductOrSectorSpecificRuleOperator.OTHER, rule_names=['Rule1'], other_operator_name='Custom Operator')"
    assert repr(rule) == expected_repr

