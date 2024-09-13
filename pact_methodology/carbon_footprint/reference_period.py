from __future__ import annotations  # For forward references within the module

from pact_methodology.datetime import DateTime


class ReferencePeriod:

    def __init__(self, start: DateTime, end: DateTime):
        """Represents a reference period with a start and end date.

        Args:
            start: The start date of the reference period.
            end: The end date of the reference period.

        Raises:
            ValueError: If start date is not before end date, or if either date is not a DateTime object.
        """
        if not isinstance(start, DateTime):
            raise ValueError("Start date must be a DateTime object")
        if not isinstance(end, DateTime):
            raise ValueError("End date must be a DateTime object")
        if start >= end:
            raise ValueError("Start date must be before end date")

        self.start = start
        self.end = end

    def includes_2025_or_later(self) -> bool:
        """Checks if the reference period includes 2025 or later.

        Returns:
            bool: True if the end date of the reference period is in 2025 or later, False otherwise.
        """
        return self.end.year >= 2025
