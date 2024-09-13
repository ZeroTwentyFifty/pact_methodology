import pytest

from pact_methodology.assurance.assurance import (
    Assurance,
    Coverage,
    Level,
    Boundary,
)
from pact_methodology.datetime import DateTime


def test_assurance_init():
    assurance = Assurance(True, "My Auditor")
    assert assurance.assurance == True
    assert assurance.provider_name == "My Auditor"


def test_assurance_to_dict():
    assurance = Assurance(
        True,
        "My Auditor",
        Coverage.PCF_SYSTEM,
        Level.LIMITED,
        Boundary.CRADLE_TO_GATE,
        DateTime("2022-12-08T14:47:32Z"),
        "ISO 14044",
    )
    expected_dict = {
        "assurance": True,
        "provider_name": "My Auditor",
        "coverage": "PCF system",
        "level": "limited",
        "boundary": "Cradle-to-Gate",
        "completed_at": "2022-12-08T14:47:32Z",
        "standard_name": "ISO 14044",
    }
    assert assurance.to_dict() == expected_dict


def test_coverage_enum():
    assert Coverage.CORPORATE_LEVEL.value == "corporate level"
    assert Coverage.PRODUCT_LINE.value == "product line"
    assert Coverage.PCF_SYSTEM.value == "PCF system"
    assert Coverage.PRODUCT_LEVEL.value == "product level"


def test_level_enum():
    assert Level.LIMITED.value == "limited"
    assert Level.REASONABLE.value == "reasonable"


def test_boundary_enum():
    assert Boundary.GATE_TO_GATE.value == "Gate-to-Gate"
    assert Boundary.CRADLE_TO_GATE.value == "Cradle-to-Gate"


def test_assurance_init_with_invalid_coverage():
    with pytest.raises(ValueError) as excinfo:
        Assurance(True, "My Auditor", "Invalid coverage")
    assert str(excinfo.value) == "coverage must be an instance of Coverage"


def test_assurance_init_with_invalid_level():
    with pytest.raises(ValueError) as excinfo:
        Assurance(True, "My Auditor", level="Invalid level")
    assert str(excinfo.value) == "level must be an instance of Level"


def test_assurance_init_with_invalid_boundary():
    with pytest.raises(ValueError) as excinfo:
        Assurance(True, "My Auditor", boundary="Invalid boundary")
    assert str(excinfo.value) == "boundary must be an instance of Boundary"


def test_assurance_init_with_valid_enum_values():
    assurance = Assurance(
        True,
        "My Auditor",
        coverage=Coverage.PCF_SYSTEM,
        level=Level.LIMITED,
        boundary=Boundary.GATE_TO_GATE,
    )
    assert assurance.coverage == Coverage.PCF_SYSTEM
    assert assurance.level == Level.LIMITED
    assert assurance.boundary == Boundary.GATE_TO_GATE


@pytest.mark.parametrize("assurance", [True, False])
def test_assurance_init_with_valid_assurance(assurance):
    Assurance(assurance, "My Auditor")


@pytest.mark.parametrize("assurance", ["True", 1, None])
def test_assurance_init_with_invalid_assurance(assurance):
    with pytest.raises(ValueError) as excinfo:
        Assurance(assurance, "My Auditor")
    assert str(excinfo.value) == "assurance must be a boolean"


@pytest.mark.parametrize("provider_name", ["My Auditor", "Your Auditor"])
def test_assurance_init_with_valid_provider_name(provider_name):
    Assurance(True, provider_name)


@pytest.mark.parametrize("provider_name", [True, 1, None])
def test_assurance_init_with_invalid_provider_name(provider_name):
    with pytest.raises(ValueError) as excinfo:
        Assurance(True, provider_name)
    assert str(excinfo.value) == "provider_name must be a string"


@pytest.mark.parametrize(
    "completed_at",
    [DateTime("2022-12-08T14:47:32Z"), DateTime("2023-01-01T00:00:00Z"), None],
)
def test_assurance_init_with_valid_completed_at(completed_at):
    Assurance(True, "My Auditor", completed_at=completed_at)


@pytest.mark.parametrize("completed_at", [True, 1])
def test_assurance_init_with_invalid_completed_at(completed_at):
    with pytest.raises(ValueError) as excinfo:
        Assurance(True, "My Auditor", completed_at=completed_at)
    assert str(excinfo.value) == "completed_at must be an instance of DateTime"


@pytest.mark.parametrize("standard_name", ["ISO 14044", "Another Standard", None])
def test_assurance_init_with_valid_standard_name(standard_name):
    Assurance(True, "My Auditor", standard_name=standard_name)


@pytest.mark.parametrize("standard_name", [True, 1])
def test_assurance_init_with_invalid_standard_name(standard_name):
    with pytest.raises(ValueError) as excinfo:
        Assurance(True, "My Auditor", standard_name=standard_name)
    assert str(excinfo.value) == "standard_name must be a string"


@pytest.mark.parametrize("comments", ["Some comments", "More comments", None])
def test_assurance_init_with_valid_comments(comments):
    Assurance(True, "My Auditor", comments=comments)


@pytest.mark.parametrize("comments", [True, 1])
def test_assurance_init_with_invalid_comments(comments):
    with pytest.raises(ValueError) as excinfo:
        Assurance(True, "My Auditor", comments=comments)
    assert str(excinfo.value) == "comments must be a string"
