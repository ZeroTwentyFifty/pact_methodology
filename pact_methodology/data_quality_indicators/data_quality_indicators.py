"""
Data Quality Indicators (DQIs) are used to assess the quality of data used in Pathfinder Framework calculations.
These indicators are applied to different aspects of data quality, such as technological representativeness,
temporal representativeness, geographical representativeness, completeness, and reliability.

Each DQI is represented as a set of attributes, including a reference period and various data quality ratings.

This module provides the `DataQualityIndicators` class to encapsulate and validate DQI values.
"""

from pact_methodology.carbon_footprint.reference_period import ReferencePeriod
from pact_methodology.data_quality_indicators.data_quality_rating import DataQualityRating
from pact_methodology.datetime import DateTime

class DataQualityIndicators:
    """
    Represents quantitative data quality indicators.

    Attributes:
        reference_period (ReferencePeriod): The reference period for the data quality assessment.
        coverage_percent (float | None): Percentage of PCF included in the assessment (>5% emissions threshold).
        technological_dqr (DataQualityRating | None): Data quality rating for technological representativeness.
        temporal_dqr (DataQualityRating | None): Data quality rating for temporal representativeness.
        geographical_dqr (DataQualityRating | None): Data quality rating for geographical representativeness.
        completeness_dqr (DataQualityRating | None): Data quality rating for data completeness.
        reliability_dqr (DataQualityRating | None): Data quality rating for data reliability.

    Examples:
        >>> from pact_methodology.datetime import DateTime
        >>> dqi = DataQualityIndicators(
        ...    reference_period=ReferencePeriod(start=DateTime.now(), end=DateTime.now()),
        ...    coverage_percent=50.0,
        ...    technological_dqr=DataQualityRating(3),
        ...    temporal_dqr=DataQualityRating(3),
        ...    geographical_dqr=DataQualityRating(3),
        ...    completeness_dqr=DataQualityRating(3),
        ...    reliability_dqr=DataQualityRating(3)
        ... )
        >>> dqi.reference_period
        ReferencePeriod(start=DateTime.now(), end=DateTime.now())
        >>> dqi.coverage_percent
        50.0
    """

    def __init__(
        self,
        *,
        reference_period: ReferencePeriod,
        coverage_percent: float | None = None,
        technological_dqr: DataQualityRating | None = None,
        temporal_dqr: DataQualityRating | None = None,
        geographical_dqr: DataQualityRating | None = None,
        completeness_dqr: DataQualityRating | None = None,
        reliability_dqr: DataQualityRating | None = None,
    ):
        """
        Initializes a new DataQualityIndicators instance.

        Args:
            reference_period (ReferencePeriod): The reference period for the data quality assessment.
            coverage_percent (float, optional): Defaults to None if before 2025.
            technological_dqr (DataQualityRating, optional): Defaults to None if before 2025.
            temporal_dqr (DataQualityRating, optional): Defaults to None if before 2025.
            geographical_dqr (DataQualityRating, optional): Defaults to None if before 2025.
            completeness_dqr (DataQualityRating, optional): Defaults to None if before 2025.
            reliability_dqr (DataQualityRating, optional): Defaults to None if before 2025.

        Raises:
            ValueError: If a required attribute is missing or None for reference periods
                        including 2025 or later.

        Examples:
            >>> from pact_methodology.datetime import DateTime
            >>> dqi = DataQualityIndicators(
            ...    reference_period=ReferencePeriod(start=DateTime.now(), end=DateTime.now()),
            ...    coverage_percent=50.0,
            ...    technological_dqr=DataQualityRating(3),
            ...    temporal_dqr=DataQualityRating(3),
            ...    geographical_dqr=DataQualityRating(3),
            ...    completeness_dqr=DataQualityRating(3),
            ...    reliability_dqr=DataQualityRating(3)
            ... )
        """
        self.reference_period = reference_period
        self.coverage_percent = coverage_percent
        self.technological_dqr = technological_dqr
        self.temporal_dqr = temporal_dqr
        self.geographical_dqr = geographical_dqr
        self.completeness_dqr = completeness_dqr
        self.reliability_dqr = reliability_dqr

        required_attributes_after_2025 = [
            "coverage_percent",
            "technological_dqr",
            "temporal_dqr",
            "geographical_dqr",
            "completeness_dqr",
            "reliability_dqr",
        ]

        if reference_period is not None and reference_period.includes_2025_or_later():
            for attr in required_attributes_after_2025:
                if not hasattr(self, attr) or getattr(self, attr) is None:
                    raise ValueError(
                        f"Attribute '{attr}' must be defined and not None for reference periods including 2025 or later"
                    )

    @property
    def reference_period(self):
        """
        Gets the reference period for the data quality assessment.

        Returns:
            ReferencePeriod: The reference period.
        """
        return self._reference_period

    @reference_period.setter
    def reference_period(self, value):
        """
        Sets the reference period for the data quality assessment.

        Args:
            value (ReferencePeriod): The reference period to set.

        Raises:
            ValueError: If value is not an instance of ReferencePeriod.

        Examples:
            >>> from pact_methodology.datetime import DateTime
            >>> dqi = DataQualityIndicators(
            ...     reference_period=ReferencePeriod(start=DateTime.now(), end=DateTime.now()),
            ...     coverage_percent=50.0,
            ...     technological_dqr=DataQualityRating(3),
            ...     temporal_dqr=DataQualityRating(3),
            ...     geographical_dqr=DataQualityRating(3),
            ...     completeness_dqr=DataQualityRating(3),
            ...     reliability_dqr=DataQualityRating(3)
            ... )
            >>> dqi.reference_period = ReferencePeriod(start=DateTime.now(), end=DateTime.now())
        """
        if not isinstance(value, ReferencePeriod):
            raise ValueError("reference_period must be an instance of ReferencePeriod")
        self._reference_period = value

    @property
    def coverage_percent(self):
        """
        Gets the coverage percentage of the PCF included in the assessment.

        Returns:
            float | None: The coverage percentage.
        """
        return self._coverage_percent

    @coverage_percent.setter
    def coverage_percent(self, value):
        """
        Sets the coverage percentage of the PCF included in the assessment.

        Args:
            value (float | None): The coverage percentage to set.

        Raises:
            ValueError: If value is not a number.

        Examples:
            >>> from pact_methodology.datetime import DateTime
            >>> dqi = DataQualityIndicators(
            ...     reference_period=ReferencePeriod(start=DateTime.now(), end=DateTime.now()),
            ...     coverage_percent=50.0,
            ...     technological_dqr=DataQualityRating(3),
            ...     temporal_dqr=DataQualityRating(3),
            ...     geographical_dqr=DataQualityRating(3),
            ...     completeness_dqr=DataQualityRating(3),
            ...     reliability_dqr=DataQualityRating(3)
            ... )
            >>> dqi.coverage_percent = 60.0
        """
        if value is not None and not isinstance(value, (int, float)):
            raise ValueError("coverage_percent must be a number")
        self._coverage_percent = value

    @property
    def technological_dqr(self):
        """
        Gets the data quality rating for technological representativeness.

        Returns:
            DataQualityRating | None: The technological data quality rating.
        """
        return self._technological_dqr

    @technological_dqr.setter
    def technological_dqr(self, value):
        """
        Sets the data quality rating for technological representativeness.

        Args:
            value (DataQualityRating | None): The technological data quality rating to set.

        Raises:
            TypeError: If value is not an instance of DataQualityRating.

        Examples:
            >>> from pact_methodology.datetime import DateTime
            >>> dqi = DataQualityIndicators(
            ...     reference_period=ReferencePeriod(start=DateTime.now(), end=DateTime.now()),
            ...     coverage_percent=50.0,
            ...     technological_dqr=DataQualityRating(3),
            ...     temporal_dqr=DataQualityRating(3),
            ...     geographical_dqr=DataQualityRating(3),
            ...     completeness_dqr=DataQualityRating(3),
            ...     reliability_dqr=DataQualityRating(3)
            ... )
            >>> dqi.technological_dqr = DataQualityRating(2)
        """
        if value is not None and not isinstance(value, DataQualityRating):
            raise TypeError("technological_dqr must be an instance of DataQualityRating")
        self._technological_dqr = value

    @property
    def temporal_dqr(self):
        """
        Gets the data quality rating for temporal representativeness.

        Returns:
            DataQualityRating | None: The temporal data quality rating.
        """
        return self._temporal_dqr

    @temporal_dqr.setter
    def temporal_dqr(self, value):
        """
        Sets the data quality rating for temporal representativeness.

        Args:
            value (DataQualityRating | None): The temporal data quality rating to set.

        Raises:
            TypeError: If value is not an instance of DataQualityRating.

        Examples:
            >>> from pact_methodology.datetime import DateTime
            >>> dqi = DataQualityIndicators(
            ...     reference_period=ReferencePeriod(start=DateTime.now(), end=DateTime.now()),
            ...     coverage_percent=50.0,
            ...     technological_dqr=DataQualityRating(3),
            ...     temporal_dqr=DataQualityRating(3),
            ...     geographical_dqr=DataQualityRating(3),
            ...     completeness_dqr=DataQualityRating(3),
            ...     reliability_dqr=DataQualityRating(3)
            ... )
            >>> dqi.temporal_dqr = DataQualityRating(2)
        """
        if value is not None and not isinstance(value, DataQualityRating):
            raise TypeError("temporal_dqr must be an instance of DataQualityRating")
        self._temporal_dqr = value

    @property
    def geographical_dqr(self):
        """
        Gets the data quality rating for geographical representativeness.

        Returns:
            DataQualityRating | None: The geographical data quality rating.
        """
        return self._geographical_dqr

    @geographical_dqr.setter
    def geographical_dqr(self, value):
        """
        Sets the data quality rating for geographical representativeness.

        Args:
            value (DataQualityRating | None): The geographical data quality rating to set.

        Raises:
            TypeError: If value is not an instance of DataQualityRating.

        Examples:
            >>> from pact_methodology.datetime import DateTime
            >>> dqi = DataQualityIndicators(
            ...     reference_period=ReferencePeriod(start=DateTime.now(), end=DateTime.now()),
            ...     coverage_percent=50.0,
            ...     technological_dqr=DataQualityRating(3),
            ...     temporal_dqr=DataQualityRating(3),
            ...     geographical_dqr=DataQualityRating(3),
            ...     completeness_dqr=DataQualityRating(3),
            ...     reliability_dqr=DataQualityRating(3)
            ... )
            >>> dqi.geographical_dqr = DataQualityRating(2)
        """
        if value is not None and not isinstance(value, DataQualityRating):
            raise TypeError("geographical_dqr must be an instance of DataQualityRating")
        self._geographical_dqr = value

    @property
    def completeness_dqr(self):
        """
        Gets the data quality rating for data completeness.

        Returns:
            DataQualityRating | None: The completeness data quality rating.
        """
        return self._completeness_dqr

    @completeness_dqr.setter
    def completeness_dqr(self, value):
        """
        Sets the data quality rating for data completeness.

        Args:
            value (DataQualityRating | None): The completeness data quality rating to set.

        Raises:
            TypeError: If value is not an instance of DataQualityRating.

        Examples:
            >>> from pact_methodology.datetime import DateTime
            >>> dqi = DataQualityIndicators(
            ...     reference_period=ReferencePeriod(start=DateTime.now(), end=DateTime.now()),
            ...     coverage_percent=50.0,
            ...     technological_dqr=DataQualityRating(3),
            ...     temporal_dqr=DataQualityRating(3),
            ...     geographical_dqr=DataQualityRating(3),
            ...     completeness_dqr=DataQualityRating(3),
            ...     reliability_dqr=DataQualityRating(3)
            ... )
            >>> dqi.completeness_dqr = DataQualityRating(2)
        """
        if value is not None and not isinstance(value, DataQualityRating):
            raise TypeError("completeness_dqr must be an instance of DataQualityRating")
        self._completeness_dqr = value

    @property
    def reliability_dqr(self):
        """
        Gets the data quality rating for data reliability.

        Returns:
            DataQualityRating | None: The reliability data quality rating.
        """
        return self._reliability_dqr

    @reliability_dqr.setter
    def reliability_dqr(self, value):
        """
        Sets the data quality rating for data reliability.

        Args:
            value (DataQualityRating | None): The reliability data quality rating to set.

        Raises:
            TypeError: If value is not an instance of DataQualityRating.

        Examples:
            >>> from pact_methodology.datetime import DateTime
            >>> dqi = DataQualityIndicators(
            ...     reference_period=ReferencePeriod(start=DateTime.now(), end=DateTime.now()),
            ...     coverage_percent=50.0,
            ...     technological_dqr=DataQualityRating(3),
            ...     temporal_dqr=DataQualityRating(3),
            ...     geographical_dqr=DataQualityRating(3),
            ...     completeness_dqr=DataQualityRating(3),
            ...     reliability_dqr=DataQualityRating(3)
            ... )
            >>> dqi.reliability_dqr = DataQualityRating(2)
        """
        if value is not None and not isinstance(value, DataQualityRating):
            raise TypeError("reliability_dqr must be an instance of DataQualityRating")
        self._reliability_dqr = value

    def __str__(self):
        """
        Returns the string representation of the data quality indicators.

        Returns:
            str: The string representation of the data quality indicators.

        Examples:
            >>> from pact_methodology.datetime import DateTime
            >>> dqi = DataQualityIndicators(
            ...     reference_period=ReferencePeriod(start=DateTime.now(), end=DateTime.now()),
            ...     coverage_percent=50.0,
            ...     technological_dqr=DataQualityRating(3),
            ...     temporal_dqr=DataQualityRating(3),
            ...     geographical_dqr=DataQualityRating(3),
            ...     completeness_dqr=DataQualityRating(3),
            ...     reliability_dqr=DataQualityRating(3)
            ... )
            >>> str(dqi)
            'DataQualityIndicators(reference_period=ReferencePeriod(start=DateTime.now(), end=DateTime.now()), coverage_percent=50.0, technological_dqr=DataQualityRating(3), temporal_dqr=DataQualityRating(3), geographical_dqr=DataQualityRating(3), completeness_dqr=DataQualityRating(3), reliability_dqr=DataQualityRating(3))'
        """
        return (
            f"DataQualityIndicators("
            f"reference_period={self.reference_period}, "
            f"coverage_percent={self.coverage_percent}, "
            f"technological_dqr={self.technological_dqr}, "
            f"temporal_dqr={self.temporal_dqr}, "
            f"geographical_dqr={self.geographical_dqr}, "
            f"completeness_dqr={self.completeness_dqr}, "
            f"reliability_dqr={self.reliability_dqr})"
        )

    def __repr__(self):
        """
        Returns the official string representation of the data quality indicators.

        Returns:
            str: The official string representation of the data quality indicators.

        Examples:
            >>> from pact_methodology.datetime import DateTime
            >>> dqi = DataQualityIndicators(
            ...     reference_period=ReferencePeriod(start=DateTime.now(), end=DateTime.now()),
            ...     coverage_percent=50.0,
            ...     technological_dqr=DataQualityRating(3),
            ...     temporal_dqr=DataQualityRating(3),
            ...     geographical_dqr=DataQualityRating(3),
            ...     completeness_dqr=DataQualityRating(3),
            ...     reliability_dqr=DataQualityRating(3)
            ... )
            >>> repr(dqi)
            'DataQualityIndicators(reference_period=ReferencePeriod(start=DateTime.now(), end=DateTime.now()), coverage_percent=50.0, technological_dqr=DataQualityRating(3), temporal_dqr=DataQualityRating(3), geographical_dqr=DataQualityRating(3), completeness_dqr=DataQualityRating(3), reliability_dqr=DataQualityRating(3))'
        """
        return (
            f"DataQualityIndicators("
            f"reference_period={repr(self.reference_period)}, "
            f"coverage_percent={repr(self.coverage_percent)}, "
            f"technological_dqr={repr(self.technological_dqr)}, "
            f"temporal_dqr={repr(self.temporal_dqr)}, "
            f"geographical_dqr={repr(self.geographical_dqr)}, "
            f"completeness_dqr={repr(self.completeness_dqr)}, "
            f"reliability_dqr={repr(self.reliability_dqr)})"
        )

    def __eq__(self, other):
        """
        Compares two DataQualityIndicators instances for equality.

        Args:
            other (DataQualityIndicators): The other DataQualityIndicators instance to compare.

        Returns:
            bool: True if the instances are equal, False otherwise.

        Examples:
            >>> from pact_methodology.datetime import DateTime
            >>> dqi1 = DataQualityIndicators(
            ...     reference_period=ReferencePeriod(start=DateTime.now(), end=DateTime.now()),
            ...     coverage_percent=50.0,
            ...     technological_dqr=DataQualityRating(3),
            ...     temporal_dqr=DataQualityRating(3),
            ...     geographical_dqr=DataQualityRating(3),
            ...     completeness_dqr=DataQualityRating(3),
            ...     reliability_dqr=DataQualityRating(3)
            ... )
            >>> dqi2 = DataQualityIndicators(
            ...     reference_period=ReferencePeriod(start=DateTime.now(), end=DateTime.now()),
            ...     coverage_percent=50.0,
            ...     technological_dqr=DataQualityRating(3),
            ...     temporal_dqr=DataQualityRating(3),
            ...     geographical_dqr=DataQualityRating(3),
            ...     completeness_dqr=DataQualityRating(3),
            ...     reliability_dqr=DataQualityRating(3)
            ... )
            >>> dqi1 == dqi2
            True
        """
        if not isinstance(other, DataQualityIndicators):
            return NotImplemented
        return (
            self.reference_period == other.reference_period
            and self.coverage_percent == other.coverage_percent
            and self.technological_dqr == other.technological_dqr
            and self.temporal_dqr == other.temporal_dqr
            and self.geographical_dqr == other.geographical_dqr
            and self.completeness_dqr == other.completeness_dqr
            and self.reliability_dqr == other.reliability_dqr
        )