"""
Data Quality Ratings (DQRs) are used to assess the quality of data used in Pathfinder Framework calculations.
These ratings are applied to different aspects of data quality, such as technological representativeness,
temporal representativeness, geographical representativeness, completeness, and reliability.

Each DQR is represented as a decimal value between 1.0 and 3.0 (inclusive),
following the Pathfinder Framework guidelines. A higher DQR indicates higher data quality.

This module provides the `DataQualityRating` class to encapsulate and validate DQR values.
"""

from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class DataQualityRating:
    rating: int

    def __post_init__(self):
        if not isinstance(self.rating, int):
            raise TypeError("Data quality rating must be an integer")
        if self.rating < 1 or self.rating > 3:
            raise ValueError("Data quality rating must be between 1 and 3 (inclusive)")
