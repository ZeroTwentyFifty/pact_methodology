import pytest
from pact_methodology.carbon_footprint.product_or_sector_specific_rule import ProductOrSectorSpecificRule
from pact_methodology.carbon_footprint.product_or_sector_specific_rule_operator import ProductOrSectorSpecificRuleOperator
from pact_methodology.carbon_footprint.product_or_sector_specific_rule_set import ProductOrSectorSpecificRuleSet

@pytest.fixture
def valid_rule():
    return ProductOrSectorSpecificRule(
        operator=ProductOrSectorSpecificRuleOperator.PEF,
        rule_names=["PEFCR Guidance v6.3"]
    )

@pytest.fixture
def valid_custom_rule():
    return ProductOrSectorSpecificRule(
        operator=ProductOrSectorSpecificRuleOperator.OTHER,
        rule_names=["Custom PCR 2023"],
        other_operator_name="Industry Association X"
    )

@pytest.fixture
def valid_epd_rule():
    return ProductOrSectorSpecificRule(
        operator=ProductOrSectorSpecificRuleOperator.EPD_INTERNATIONAL,
        rule_names=["PCR 2019:14 v1.11"]
    )

def test_product_or_sector_specific_rule_set_exists():
    assert ProductOrSectorSpecificRuleSet is not None

def test_empty_initialization():
    rule_set = ProductOrSectorSpecificRuleSet()
    assert rule_set.rules == []

def test_initialization_with_rules(valid_rule):
    rule_set = ProductOrSectorSpecificRuleSet([valid_rule])
    assert len(rule_set.rules) == 1
    assert rule_set.rules[0] == valid_rule

def test_initialization_with_invalid_rules():
    with pytest.raises(ValueError) as excinfo:
        ProductOrSectorSpecificRuleSet([1, 2, 3])
    assert str(excinfo.value) == "rules must be a list of ProductOrSectorSpecificRule objects"

def test_add_rule(valid_rule, valid_custom_rule):
    rule_set = ProductOrSectorSpecificRuleSet([valid_rule])
    rule_set.add_rule(valid_custom_rule)
    assert len(rule_set.rules) == 2
    assert rule_set.rules[1] == valid_custom_rule

def test_add_invalid_rule(valid_rule):
    rule_set = ProductOrSectorSpecificRuleSet([valid_rule])
    with pytest.raises(ValueError) as excinfo:
        rule_set.add_rule("invalid")
    assert str(excinfo.value) == "rule must be an instance of ProductOrSectorSpecificRule"

def test_remove_rule(valid_rule, valid_custom_rule):
    rule_set = ProductOrSectorSpecificRuleSet([valid_rule, valid_custom_rule])
    rule_set.remove_rule(valid_rule)
    assert len(rule_set.rules) == 1
    assert rule_set.rules[0] == valid_custom_rule

def test_remove_nonexistent_rule(valid_rule, valid_custom_rule):
    rule_set = ProductOrSectorSpecificRuleSet([valid_rule])
    with pytest.raises(ValueError) as excinfo:
        rule_set.remove_rule(valid_custom_rule)
    assert str(excinfo.value) == "rule not found in the set"

def test_remove_invalid_rule(valid_rule):
    rule_set = ProductOrSectorSpecificRuleSet([valid_rule])
    with pytest.raises(ValueError) as excinfo:
        rule_set.remove_rule("invalid")
    assert str(excinfo.value) == "rule must be an instance of ProductOrSectorSpecificRule"

def test_to_dict(valid_rule, valid_custom_rule):
    rule_set = ProductOrSectorSpecificRuleSet([valid_rule, valid_custom_rule])
    dict_output = rule_set.to_dict()
    assert len(dict_output) == 2
    expected_dict_0 = {
        'operator': 'PEF',
        'rule_names': ['PEFCR Guidance v6.3']
    }
    expected_dict_1 = {
        'operator': 'Other',
        'rule_names': ['Custom PCR 2023'],
        'other_operator_name': 'Industry Association X'
    }
    assert dict_output[0] == expected_dict_0
    assert dict_output[1] == expected_dict_1

def test_str_representation(valid_rule):
    rule_set = ProductOrSectorSpecificRuleSet([valid_rule])
    expected_str = "ProductOrSectorSpecificRuleSet(rules=[ProductOrSectorSpecificRule(operator=ProductOrSectorSpecificRuleOperator.PEF, rule_names=['PEFCR Guidance v6.3'], other_operator_name=None)])"
    assert str(rule_set) == expected_str

def test_repr_representation(valid_rule):
    rule_set = ProductOrSectorSpecificRuleSet([valid_rule])
    expected_repr = "ProductOrSectorSpecificRuleSet(rules=[ProductOrSectorSpecificRule(operator=ProductOrSectorSpecificRuleOperator.PEF, rule_names=['PEFCR Guidance v6.3'], other_operator_name=None)])"
    assert repr(rule_set) == expected_repr

def test_equality(valid_rule, valid_custom_rule):
    rule_set1 = ProductOrSectorSpecificRuleSet([valid_rule, valid_custom_rule])
    rule_set2 = ProductOrSectorSpecificRuleSet([valid_rule, valid_custom_rule])
    assert rule_set1 == rule_set2

def test_inequality(valid_rule, valid_custom_rule):
    rule_set1 = ProductOrSectorSpecificRuleSet([valid_rule])
    rule_set2 = ProductOrSectorSpecificRuleSet([valid_custom_rule])
    assert rule_set1 != rule_set2

def test_inequality_with_different_type(valid_rule):
    rule_set = ProductOrSectorSpecificRuleSet([valid_rule])
    assert rule_set != "not a rule set"

def test_multiple_rule_types(valid_rule, valid_custom_rule, valid_epd_rule):
    rule_set = ProductOrSectorSpecificRuleSet([valid_rule])
    rule_set.add_rule(valid_custom_rule)
    rule_set.add_rule(valid_epd_rule)
    assert len(rule_set.rules) == 3
    assert rule_set.rules[0].operator == ProductOrSectorSpecificRuleOperator.PEF
    assert rule_set.rules[0].rule_names == ["PEFCR Guidance v6.3"]
    assert rule_set.rules[1].operator == ProductOrSectorSpecificRuleOperator.OTHER
    assert rule_set.rules[1].rule_names == ["Custom PCR 2023"]
    assert rule_set.rules[2].operator == ProductOrSectorSpecificRuleOperator.EPD_INTERNATIONAL
    assert rule_set.rules[2].rule_names == ["PCR 2019:14 v1.11"]
