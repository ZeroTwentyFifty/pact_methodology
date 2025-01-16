"""
Data Quality Ratings (DQRs) are used to assess the quality of data used in Pathfinder Framework calculations.
These ratings are applied to different aspects of data quality, such as technological representativeness,
temporal representativeness, geographical representativeness, completeness, and reliability.

Each DQR is represented as an integer value between 1 and 3 (inclusive),
following the Pathfinder Framework guidelines. A higher DQR indicates higher data quality.

This module provides the `DataQualityRating` class to encapsulate and validate DQR values.
"""

from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class DataQualityRating:
    """
    Represents a data quality rating for a specific aspect of data quality.

    Attributes:
        rating (int): The data quality rating, an integer between 1 and 3 (inclusive).

    Examples:
        >>> dqr = DataQualityRating(3)
        >>> dqr.rating
        3
        >>> str(dqr)
        '3'
    """

    rating: int

    def __post_init__(self):
        """
        Validates the data quality rating upon initialization.

        Raises:
            TypeError: If the rating is not an integer.
            ValueError: If the rating is not between 1 and 3 (inclusive).

        Examples:
            >>> DataQualityRating(2)
            DataQualityRating(2)
            >>> DataQualityRating(4)
            Traceback (most recent call last):
            ...
            ValueError: Data quality rating must be between 1 and 3 (inclusive)
        """
        if not isinstance(self.rating, int):
            raise TypeError("Data quality rating must be an integer")
        if self.rating < 1 or self.rating > 3:
            raise ValueError("Data quality rating must be between 1 and 3 (inclusive)")

    def __str__(self):
        """
        Returns the string representation of the data quality rating.

        Returns:
            str: The string representation of the rating.

        Examples:
            >>> dqr = DataQualityRating(1)
            >>> str(dqr)
            '1'
        """
        return f"{self.rating}"

    def __repr__(self):
        """
        Returns the official string representation of the data quality rating.

        Returns:
            str: The official string representation of the rating.

        Examples:
            >>> dqr = DataQualityRating(2)
            >>> repr(dqr)
            'DataQualityRating(2)'
        """
        return f"DataQualityRating({self.rating})"
