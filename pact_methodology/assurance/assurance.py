from enum import Enum

from pact_methodology.datetime import DateTime


class Coverage(str, Enum):
    PCF_SYSTEM = "PCF system"
    CORPORATE_LEVEL = "corporate level"
    PRODUCT_LINE = "product line"
    PRODUCT_LEVEL = "product level"


class Level(str, Enum):
    LIMITED = "limited"
    REASONABLE = "reasonable"


class Boundary(str, Enum):
    GATE_TO_GATE = "Gate-to-Gate"
    CRADLE_TO_GATE = "Cradle-to-Gate"


class Assurance:
    """
    Represents an assurance in conformance with Pathfinder Framework chapter 5 and appendix B.

    Args:
        assurance (bool): A boolean flag indicating whether the CarbonFootprint has been assured in line with Pathfinder Framework requirements (section 5).
        provider_name (str): The non-empty name of the independent third party engaged to undertake the assurance.
        coverage (Coverage | None): Level of granularity of the emissions data assured.
        level (Level | None): Level of assurance applicable to the PCF.
        boundary (Boundary | None): Boundary of the assurance.
        completed_at (DateTime | None): The date at which the assurance was completed.
        standard_name (str | None): Name of the standard against which the PCF was assured.
        comments (str | None): Any additional comments that will clarify the interpretation of the assurance.

    Attributes:
        assurance (bool): A boolean flag indicating whether the CarbonFootprint has been assured in line with Pathfinder Framework requirements (section 5).
        provider_name (str): The non-empty name of the independent third party engaged to undertake the assurance.
        coverage (Coverage | None): Level of granularity of the emissions data assured.
        level (Level | None): Level of assurance applicable to the PCF.
        boundary (Boundary | None): Boundary of the assurance.
        completed_at (DateTime | None): The date at which the assurance was completed.
        standard_name (str | None): Name of the standard against which the PCF was assured.
        comments (str | None): Any additional comments that will clarify the interpretation of the assurance.

    Raises:
        ValueError: If any of the arguments are of the wrong type.
    """

    def __init__(
        self,
        assurance: bool,
        provider_name: str,
        coverage: Coverage | None = None,
        level: Level | None = None,
        boundary: Boundary | None = None,
        completed_at: DateTime | None = None,
        standard_name: str | None = None,
        comments: str | None = None,
    ):
        if not isinstance(assurance, bool):
            raise ValueError("assurance must be a boolean")
        if not isinstance(provider_name, str):
            raise ValueError("provider_name must be a string")
        if coverage is not None and not isinstance(coverage, Coverage):
            raise ValueError("coverage must be an instance of Coverage")
        if level is not None and not isinstance(level, Level):
            raise ValueError("level must be an instance of Level")
        if boundary is not None and not isinstance(boundary, Boundary):
            raise ValueError("boundary must be an instance of Boundary")
        if completed_at is not None and not isinstance(completed_at, DateTime):
            raise ValueError("completed_at must be an instance of DateTime")
        if standard_name is not None and not isinstance(standard_name, str):
            raise ValueError("standard_name must be a string")
        if comments is not None and not isinstance(comments, str):
            raise ValueError("comments must be a string")

        self.assurance = assurance
        self.provider_name = provider_name
        self.coverage = coverage
        self.level = level
        self.boundary = boundary
        self.completed_at = completed_at
        self.standard_name = standard_name
        self.comments = comments

    def to_dict(self) -> dict:
        assurance_dict = {
            "assurance": self.assurance,
            "provider_name": self.provider_name,
        }

        if self.coverage is not None:
            assurance_dict["coverage"] = self.coverage.value

        if self.level is not None:
            assurance_dict["level"] = self.level.value

        if self.boundary is not None:
            assurance_dict["boundary"] = self.boundary.value

        if self.completed_at is not None:
            assurance_dict["completed_at"] = str(self.completed_at)

        if self.standard_name is not None:
            assurance_dict["standard_name"] = self.standard_name

        if self.comments is not None:
            assurance_dict["comments"] = self.comments

        return assurance_dict
