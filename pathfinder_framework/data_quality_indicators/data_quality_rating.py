"""
Data Quality Ratings (DQRs) are used to assess the quality of data used in Pathfinder Framework calculations.
These ratings are applied to different aspects of data quality, such as technological representativeness,
temporal representativeness, geographical representativeness, completeness, and reliability.

Each DQR is represented as a decimal value between 1.0 and 3.0 (inclusive),
following the Pathfinder Framework guidelines. A higher DQR indicates higher data quality.

This module provides the `DataQualityRating` class to encapsulate and validate DQR values.
"""


class DataQualityRating:

    def __init__(self, rating: int):
        """Data Quality Rating (DQR)

        Args:
            rating (int): The numerical value of the data quality rating.

        Raises:
            ValueError: If the provided value is not between 1 and 3 (inclusive).
        """
        if not 1 <= rating <= 3:
            raise ValueError("Data quality rating must be between 1 and 3 (inclusive)")
        self.rating = rating
