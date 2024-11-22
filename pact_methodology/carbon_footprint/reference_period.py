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
        self.start = start
        self.end = end

    @property
    def start(self) -> DateTime:
        return self._start

    @start.setter
    def start(self, value: DateTime):
        if not isinstance(value, DateTime):
            raise ValueError("Start date must be a DateTime object")
        self._start = value

    @property
    def end(self) -> DateTime:
        return self._end

    @end.setter
    def end(self, value: DateTime):
        if not isinstance(value, DateTime):
            raise ValueError("End date must be a DateTime object")
        if self.start is not None and value <= self.start:
            raise ValueError("End date must be after start date")
        self._end = value

    def includes_2025_or_later(self) -> bool:
        """Checks if the reference period includes 2025 or later.

        Returns:
            bool: True if the end date of the reference period is in 2025 or later, False otherwise.
        """
        return self.end.year >= 2025

    def __repr__(self):
        return f"ReferencePeriod(start={self.start}, end={self.end})"
