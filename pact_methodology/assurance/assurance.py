from enum import Enum

from pact_methodology.datetime import DateTime


class Coverage(str, Enum):
    PCF_SYSTEM = "PCF system"
    CORPORATE_LEVEL = "corporate level"
    PRODUCT_LINE = "product line"
    PRODUCT_LEVEL = "product level"

    def __str__(self):
        return self.value


class Level(str, Enum):
    LIMITED = "limited"
    REASONABLE = "reasonable"

    def __str__(self):
        return self.value


class Boundary(str, Enum):
    GATE_TO_GATE = "Gate-to-Gate"
    CRADLE_TO_GATE = "Cradle-to-Gate"

    def __str__(self):
        return self.value


class Assurance:
    """Represents an assurance in conformance with PACT Methodology chapter 5 and appendix B.

    This class represents the assurance information for a product carbon footprint calculation,
    including details about the assurance provider, coverage, level, and other relevant metadata.

    Attributes:
        assurance (bool): A boolean flag indicating whether the CarbonFootprint has been assured in line 
            with PACT Methodology requirements (section 5).
        provider_name (str): The non-empty name of the independent third party engaged to undertake 
            the assurance.
        coverage (Coverage | None): Level of granularity of the emissions data assured.
        level (Level | None): Level of assurance applicable to the PCF.
        boundary (Boundary | None): Boundary of the assurance.
        completed_at (DateTime | None): The date at which the assurance was completed.
        standard_name (str | None): Name of the standard against which the PCF was assured.
        comments (str | None): Any additional comments that will clarify the interpretation of the assurance.

    Examples:
        Create a basic assurance record:
        >>> assurance = Assurance(
        ...     assurance=True,
        ...     provider_name="Assurance Corp"
        ... )

        Create a detailed assurance record:
        >>> from pact_methodology.datetime import DateTime
        >>> detailed = Assurance(
        ...     assurance=True,
        ...     provider_name="Assurance Corp",
        ...     coverage=Coverage.PRODUCT_LEVEL,
        ...     level=Level.REASONABLE,
        ...     boundary=Boundary.CRADLE_TO_GATE,
        ...     completed_at=DateTime(2023, 1, 1),
        ...     standard_name="ISO 14064-3:2019",
        ...     comments="Full product lifecycle assessment"
        ... )

        Convert assurance to dictionary format:
        >>> assurance.to_dict()
        {
            'assurance': True,
            'provider_name': 'Assurance Corp'
        }

    Raises:
        ValueError: If assurance is not a boolean, if provider_name is not a string,
            if coverage is not None and not an instance of Coverage,
            if level is not None and not an instance of Level,
            if boundary is not None and not an instance of Boundary,
            if completed_at is not None and not an instance of DateTime,
            if standard_name is not None and not a string,
            if comments is not None and not a string.
        TypeError: If required arguments are missing during initialization.

    Note:
        Only assurance and provider_name are required fields. All other attributes are optional
        but must conform to their specified types when provided.
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
        """Initialize an Assurance instance.

        Args:
            assurance: Boolean indicating if CarbonFootprint is assured
            provider_name: Name of the assurance provider
            coverage: Level of granularity of assured emissions data
            level: Level of assurance for the PCF
            boundary: Boundary of the assurance
            completed_at: Date of assurance completion
            standard_name: Name of assurance standard used
            comments: Additional clarifying comments

        Raises:
            ValueError: If arguments are invalid
            TypeError: If required arguments are missing
        """
        self.assurance = assurance
        self.provider_name = provider_name
        self.coverage = coverage
        self.level = level
        self.boundary = boundary
        self.completed_at = completed_at
        self.standard_name = standard_name
        self.comments = comments

    @property
    def assurance(self) -> bool:
        """Get the assurance flag.

        Returns:
            The boolean assurance status
        """
        return self._assurance

    @assurance.setter
    def assurance(self, value: bool):
        """Set the assurance flag.

        Args:
            value: The boolean assurance status to set

        Raises:
            ValueError: If value is not a boolean
        """
        if not isinstance(value, bool):
            raise ValueError("assurance must be a boolean")
        self._assurance = value

    @property
    def provider_name(self) -> str:
        """Get the assurance provider name.

        Returns:
            The provider name string
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, value: str):
        """Set the assurance provider name.

        Args:
            value: The provider name string to set

        Raises:
            ValueError: If value is not a string
        """
        if not isinstance(value, str):
            raise ValueError("provider_name must be a string")
        self._provider_name = value

    @property
    def coverage(self) -> Coverage | None:
        """Get the assurance coverage level.

        Returns:
            The Coverage enum value or None
        """
        return self._coverage

    @coverage.setter
    def coverage(self, value: Coverage | None):
        """Set the assurance coverage level.

        Args:
            value: The Coverage enum value to set or None

        Raises:
            ValueError: If value is not None and not a Coverage enum
        """
        if value is not None and not isinstance(value, Coverage):
            raise ValueError("coverage must be an instance of Coverage")
        self._coverage = value

    @property
    def level(self) -> Level | None:
        """Get the assurance level.

        Returns:
            The Level enum value or None
        """
        return self._level

    @level.setter
    def level(self, value: Level | None):
        """Set the assurance level.

        Args:
            value: The Level enum value to set or None

        Raises:
            ValueError: If value is not None and not a Level enum
        """
        if value is not None and not isinstance(value, Level):
            raise ValueError("level must be an instance of Level")
        self._level = value

    @property
    def boundary(self) -> Boundary | None:
        """Get the assurance boundary.

        Returns:
            The Boundary enum value or None
        """
        return self._boundary

    @boundary.setter
    def boundary(self, value: Boundary | None):
        """Set the assurance boundary.

        Args:
            value: The Boundary enum value to set or None

        Raises:
            ValueError: If value is not None and not a Boundary enum
        """
        if value is not None and not isinstance(value, Boundary):
            raise ValueError("boundary must be an instance of Boundary")
        self._boundary = value

    @property
    def completed_at(self) -> DateTime | None:
        """Get the assurance completion date.

        Returns:
            The DateTime instance or None
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, value: DateTime | None):
        """Set the assurance completion date.

        Args:
            value: The DateTime instance to set or None

        Raises:
            ValueError: If value is not None and not a DateTime instance
        """
        if value is not None and not isinstance(value, DateTime):
            raise ValueError("completed_at must be an instance of DateTime")
        self._completed_at = value

    @property
    def standard_name(self) -> str | None:
        """Get the assurance standard name.

        Returns:
            The standard name string or None
        """
        return self._standard_name

    @standard_name.setter
    def standard_name(self, value: str | None):
        """Set the assurance standard name.

        Args:
            value: The standard name string to set or None

        Raises:
            ValueError: If value is not None and not a string
        """
        if value is not None and not isinstance(value, str):
            raise ValueError("standard_name must be a string")
        self._standard_name = value

    @property
    def comments(self) -> str | None:
        """Get the assurance comments.

        Returns:
            The comments string or None
        """
        return self._comments

    @comments.setter
    def comments(self, value: str | None):
        """Set the assurance comments.

        Args:
            value: The comments string to set or None

        Raises:
            ValueError: If value is not None and not a string
        """
        if value is not None and not isinstance(value, str):
            raise ValueError("comments must be a string")
        self._comments = value

    def to_dict(self) -> dict:
        """Convert the assurance to a dictionary representation.

        Returns:
            A dictionary with the following structure:
            {
                "assurance": bool,  # The assurance status
                "provider_name": str,  # Name of assurance provider
                "coverage": str | None,  # Coverage level if set
                "level": str | None,  # Assurance level if set
                "boundary": str | None,  # Assurance boundary if set
                "completed_at": str | None,  # Completion date if set
                "standard_name": str | None,  # Standard name if set
                "comments": str | None  # Comments if set
            }
        """
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

    def __str__(self):
        return (
            f"Assurance("
            f"assurance={self.assurance}, "
            f"provider_name='{self.provider_name}', "
            f"coverage={self.coverage}, "
            f"level={self.level}, "
            f"boundary={self.boundary}, "
            f"completed_at={self.completed_at}, "
            f"standard_name='{self.standard_name}', "
            f"comments='{self.comments}')"
        )