from pact_methodology.carbon_footprint.product_or_sector_specific_rule_operator import (
    ProductOrSectorSpecificRuleOperator,
)


def test_product_or_sector_specific_rule_operator_values():
    assert ProductOrSectorSpecificRuleOperator.PEF == "PEF"
    assert ProductOrSectorSpecificRuleOperator.EPD_INTERNATIONAL == "EPD International"
    assert ProductOrSectorSpecificRuleOperator.OTHER == "Other"


def test_product_or_sector_specific_rule_operator_str():
    assert str(ProductOrSectorSpecificRuleOperator.PEF) == "PEF"
    assert str(ProductOrSectorSpecificRuleOperator.EPD_INTERNATIONAL) == "EPD International"
    assert str(ProductOrSectorSpecificRuleOperator.OTHER) == "Other"

def test_product_or_sector_specific_rule_operator_repr():
    assert repr(ProductOrSectorSpecificRuleOperator.PEF) == "ProductOrSectorSpecificRuleOperator.PEF"
    assert repr(ProductOrSectorSpecificRuleOperator.EPD_INTERNATIONAL) == "ProductOrSectorSpecificRuleOperator.EPD_INTERNATIONAL"
    assert repr(ProductOrSectorSpecificRuleOperator.OTHER) == "ProductOrSectorSpecificRuleOperator.OTHER"
