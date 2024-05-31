from datetime import datetime, timedelta

from pathfinder_framework.datetime import DateTime


class ValidityPeriod:
    """
    Represents a validity period with a start and end date.

    Attributes:
        start (DateTime): The start date of the validity period.
        end (DateTime): The end date of the validity period.
    """

    def __init__(self, start: DateTime, end: DateTime) -> None:
        """
        Initializes a new ValidityPeriod instance.

        Args:
            start (DateTime): The start date of the validity period.
            end (DateTime): The end date of the validity period.

        Raises:
            ValueError: If start date is not before end date.
        """
        if not isinstance(start, DateTime):
            raise ValueError("Start date must be a DateTime object")
        if not isinstance(end, DateTime):
            raise ValueError("End date must be a DateTime object")
        if start >= end:
            raise ValueError("Start date must be before end date")
        self.start = start
        self.end = end

    def is_valid(self, reference_period_end: DateTime) -> bool:
        """
        Checks if the validity period is valid with respect to the reference period end date.

        Args:
            reference_period_end (DateTime): The reference period end date.

        Returns:
            bool: True if the validity period is valid, False otherwise.

        Raises:
            ValueError: If reference_period_end is not a DateTime object.
        """
        if not isinstance(reference_period_end, DateTime):
            raise ValueError("Reference period end date must be a DateTime object")
        dt = datetime.fromisoformat(reference_period_end.value.replace('Z', '+00:00'))
        max_end_date = DateTime((dt + timedelta(days=3 * 366)).isoformat())
        return self.start >= reference_period_end and self.end <= max_end_date
