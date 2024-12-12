import pytest
from pact_methodology.carbon_footprint.cross_sectoral_standard import CrossSectoralStandard
from pact_methodology.carbon_footprint.cross_sectoral_standard_set import CrossSectoralStandardSet

def test_add_standard():
    standards_set = CrossSectoralStandardSet()
    standards_set.add(CrossSectoralStandard.GHG_PROTOCOL)
    assert CrossSectoralStandard.GHG_PROTOCOL in standards_set

def test_remove_standard():
    standards_set = CrossSectoralStandardSet()
    standards_set.add(CrossSectoralStandard.GHG_PROTOCOL)
    standards_set.remove(CrossSectoralStandard.GHG_PROTOCOL)
    assert CrossSectoralStandard.GHG_PROTOCOL not in standards_set

def test_add_multiple_standards():
    standards_set = CrossSectoralStandardSet()
    standards_set.add_multiple([CrossSectoralStandard.GHG_PROTOCOL, CrossSectoralStandard.ISO_14067])
    assert CrossSectoralStandard.GHG_PROTOCOL in standards_set
    assert CrossSectoralStandard.ISO_14067 in standards_set

def test_check_presence_of_standard():
    standards_set = CrossSectoralStandardSet()
    standards_set.add(CrossSectoralStandard.GHG_PROTOCOL)
    assert CrossSectoralStandard.GHG_PROTOCOL in standards_set
    assert CrossSectoralStandard.ISO_14044 not in standards_set

def test_str_representation():
    standards_set = CrossSectoralStandardSet()
    standards_set.add(CrossSectoralStandard.GHG_PROTOCOL)
    standards_set.add(CrossSectoralStandard.ISO_14067)
    expected_elements = {CrossSectoralStandard.GHG_PROTOCOL.value, CrossSectoralStandard.ISO_14067.value}
    actual_elements = {str(standard) for standard in standards_set._standards}
    assert actual_elements == expected_elements

def test_repr_representation():
    standards_set = CrossSectoralStandardSet()
    standards_set.add(CrossSectoralStandard.GHG_PROTOCOL)
    standards_set.add(CrossSectoralStandard.ISO_14067)
    expected_elements = {CrossSectoralStandard.GHG_PROTOCOL, CrossSectoralStandard.ISO_14067}
    actual_elements = standards_set._standards
    assert actual_elements == expected_elements