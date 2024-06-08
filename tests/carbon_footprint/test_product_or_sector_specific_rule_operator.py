from pathfinder_framework.carbon_footprint.product_or_sector_specific_rule_operator import (
    ProductOrSectorSpecificRuleOperator,
)


def test_product_or_sector_specific_rule_operator_values():
    assert ProductOrSectorSpecificRuleOperator.PEF == "PEF"
    assert ProductOrSectorSpecificRuleOperator.EPD_INTERNATIONAL == "EPD International"
    assert ProductOrSectorSpecificRuleOperator.OTHER == "Other"
