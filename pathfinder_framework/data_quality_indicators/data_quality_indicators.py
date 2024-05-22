class DataQualityIndicators:
    """
    Represents quantitative data quality indicators in accordance with Pathfinder Framework Section 4.2.3 and Appendix B.

    Attributes:
        coverage_percent (float, optional): Percentage of PCF included in the data quality assessment based on the >5% emissions threshold.
        technological_dqr (float, optional): Quantitative data quality rating for technological representativeness (1-3).
        temporal_dqr (float, optional): Quantitative data quality rating for temporal representativeness (1-3).
        geographical_dqr (float, optional): Quantitative data quality rating for geographical representativeness (1-3).
        completeness_dqr (float, optional): Quantitative data quality rating for data completeness (1-3).
        reliability_dqr (float, optional): Quantitative data quality rating for data reliability (1-3).
    """

    def __init__(self, reference_period, coverage_percent=None, technological_dqr=None, temporal_dqr=None,
                 geographical_dqr=None, completeness_dqr=None, reliability_dqr=None):

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