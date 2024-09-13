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

        if technological_dqr is not None and not isinstance(
            technological_dqr, DataQualityRating
        ):
            raise TypeError(
                "technological_dqr must be an instance of DataQualityRating"
            )
        if temporal_dqr is not None and not isinstance(temporal_dqr, DataQualityRating):
            raise TypeError("temporal_dqr must be an instance of DataQualityRating")
        if geographical_dqr is not None and not isinstance(
            geographical_dqr, DataQualityRating
        ):
            raise TypeError("geographical_dqr must be an instance of DataQualityRating")
        if completeness_dqr is not None and not isinstance(
            completeness_dqr, DataQualityRating
        ):
            raise TypeError("completeness_dqr must be an instance of DataQualityRating")
        if reliability_dqr is not None and not isinstance(
            reliability_dqr, DataQualityRating
        ):
            raise TypeError("reliability_dqr must be an instance of DataQualityRating")

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
