from pact_methodology.carbon_footprint.reference_period import ReferencePeriod
from pact_methodology.data_quality_indicators.data_quality_rating import (
    DataQualityRating,
)


class DataQualityIndicators:

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
        """Represents quantitative data quality indicators.

        Attributes:
            coverage_percent (float): Percentage of PCF included in the assessment (>5% emissions threshold).
            technological_dqr (DataQualityRating): Data quality rating for technological representativeness.
            temporal_dqr (DataQualityRating): Data quality rating for temporal representativeness.
            geographical_dqr (DataQualityRating): Data quality rating for geographical representativeness.
            completeness_dqr (DataQualityRating): Data quality rating for data completeness.
            reliability_dqr (DataQualityRating): Data quality rating for data reliability.

        Args:
            reference_period (ReferencePeriod): The reference period for the data quality assessment.
            coverage_percent (float, optional): Defaults to None if before 2025.
            technological_dqr (DataQualityRating, optional): Defaults to None if before 2025.
            temporal_dqr (DataQualityRating, optional): Defaults to None if before 2025.
            geographical_dqr (DataQualityRating, optional): Defaults to None if before 2025.
            completeness_dqr (DataQualityRating, optional): Defaults to None if before 2025.
            reliability_dqr (DataQualityRating, optional): Defaults to None if before 2025.

        Raises:
            ValueError: If a required attribute is missing or None for reporting periods
                        including 2025 or later.
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
                        f"Attribute '{attr}' must be defined and not None for reporting periods including 2025 or later"
                    )

    @property
    def reference_period(self):
        return self._reference_period

    @reference_period.setter
    def reference_period(self, value):
        if not isinstance(value, ReferencePeriod):
            raise ValueError("reference_period must be an instance of ReferencePeriod")
        self._reference_period = value

    @property
    def coverage_percent(self):
        return self._coverage_percent

    @coverage_percent.setter
    def coverage_percent(self, value):
        if value is not None and not isinstance(value, (int, float)):
            raise ValueError("coverage_percent must be a number")
        self._coverage_percent = value

    @property
    def technological_dqr(self):
        return self._technological_dqr

    @technological_dqr.setter
    def technological_dqr(self, value):
        if value is not None and not isinstance(value, DataQualityRating):
            raise TypeError("technological_dqr must be an instance of DataQualityRating")
        self._technological_dqr = value

    @property
    def temporal_dqr(self):
        return self._temporal_dqr

    @temporal_dqr.setter
    def temporal_dqr(self, value):
        if value is not None and not isinstance(value, DataQualityRating):
            raise TypeError("temporal_dqr must be an instance of DataQualityRating")
        self._temporal_dqr = value

    @property
    def geographical_dqr(self):
        return self._geographical_dqr

    @geographical_dqr.setter
    def geographical_dqr(self, value):
        if value is not None and not isinstance(value, DataQualityRating):
            raise TypeError("geographical_dqr must be an instance of DataQualityRating")
        self._geographical_dqr = value

    @property
    def completeness_dqr(self):
        return self._completeness_dqr

    @completeness_dqr.setter
    def completeness_dqr(self, value):
        if value is not None and not isinstance(value, DataQualityRating):
            raise TypeError("completeness_dqr must be an instance of DataQualityRating")
        self._completeness_dqr = value

    @property
    def reliability_dqr(self):
        return self._reliability_dqr

    @reliability_dqr.setter
    def reliability_dqr(self, value):
        if value is not None and not isinstance(value, DataQualityRating):
            raise TypeError("reliability_dqr must be an instance of DataQualityRating")
        self._reliability_dqr = value

    def __str__(self):
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
