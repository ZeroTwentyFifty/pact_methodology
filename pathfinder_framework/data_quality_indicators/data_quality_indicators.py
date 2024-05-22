from __future__ import annotations  # For forward references within the module


from pathfinder_framework.carbon_footprint.reference_period import ReferencePeriod


class DataQualityIndicators:

    def __init__(self, reference_period: ReferencePeriod, coverage_percent: float | None = None,
                 technological_dqr: float | None = None, temporal_dqr: float | None = None,
                 geographical_dqr: float | None = None, completeness_dqr: float | None = None,
                 reliability_dqr: float | None = None):
        """Represents quantitative data quality indicators.

        Attributes:
            coverage_percent: Percentage of PCF included in the assessment (>5% emissions threshold).
            technological_dqr: Data quality rating for technological representativeness (1-3).
            temporal_dqr: Data quality rating for temporal representativeness (1-3).
            geographical_dqr: Data quality rating for geographical representativeness (1-3).
            completeness_dqr: Data quality rating for data completeness (1-3).
            reliability_dqr: Data quality rating for data reliability (1-3).

        Args:
            reference_period (ReferencePeriod): The reference period for the data quality assessment.
            coverage_percent (float, optional): defaults to None if before 2025.
            technological_dqr (float, optional): defaults to None if before 2025.
            temporal_dqr (float, optional): defaults to None if before 2025.
            geographical_dqr (float, optional): defaults to None if before 2025.
            completeness_dqr (float, optional): defaults to None if before 2025.
            reliability_dqr (float, optional): defaults to None if before 2025.

        Raises:
            ValueError: If any DQR value is not between 1 and 3, or if a required attribute
                        is missing or None for reporting periods including 2025 or later.
        """
        self.coverage_percent = coverage_percent
        self.technological_dqr = technological_dqr
        self.temporal_dqr = temporal_dqr
        self.geographical_dqr = geographical_dqr
        self.completeness_dqr = completeness_dqr
        self.reliability_dqr = reliability_dqr

        required_attributes_after_2025 = ["coverage_percent", "technological_dqr", "temporal_dqr",
                                          "geographical_dqr", "completeness_dqr", "reliability_dqr"]

        if reference_period is not None and reference_period.includes_2025_or_later():
            for attr in required_attributes_after_2025:
                if not hasattr(self, attr) or getattr(self, attr) is None:
                    raise ValueError(
                        f"Attribute '{attr}' must be defined and not None for reporting periods including 2025 or later")

        # Validate DQR values (should be between 1 and 3)
        for attr in required_attributes_after_2025[1:]:
            if getattr(self, attr) is not None and not 1 <= getattr(self, attr) <= 3:
                raise ValueError(f"Attribute '{attr}' must be between 1 and 3")
