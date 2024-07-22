from datetime import datetime, timedelta

from pathfinder_framework.datetime import DateTime


class ValidityPeriod:
    """
    Represents a validity period with a start and end date.

    Ultimately, because the ValidityPeriod is modelled as an entity in this library
    it changes the ProductFootprint entity slightly. The nature of the change in
    v2.2 effectively means that whilst the validity period is optional, as they have
    stated, you then use the reference period end, and that assigns a validity period
    now no longer making the validity period optional, the docs would indicate that
    a PF can have an undefined period of validity, but the max is 3 years.
    """

    def __init__(self, *, start=None, end=None, reference_period_end=None) -> None:
        """
        Represents a validity period with a start and end date.

        Args:
            start: The start date of the validity period. Defaults to None.
            end: The end date of the validity period. Defaults to None.
            reference_period_end: The reference date to calculate default start and end if not provided. Defaults to None.

        Raises:
            ValueError: If start and end dates are not provided and reference_period_end is also not provided.
            ValueError: If start or end is not a DateTime object.
            ValueError: If start date is not before end date.

        Attributes:
            start (DateTime): The start date of the validity period.
            end (DateTime): The end date of the validity period.
        """
        if start is None or end is None:
            if reference_period_end is None:
                raise ValueError("Reference period end date must be provided when start or end dates are not specified.")
            if not isinstance(reference_period_end, DateTime):
                raise ValueError("Reference period end must be a DateTime object")
            self.start = reference_period_end
            self.end = DateTime((datetime.fromisoformat(reference_period_end.value.replace("Z", "+00:00")) + timedelta(days=3 * 366)).isoformat())
        else:
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
        dt = datetime.fromisoformat(reference_period_end.value.replace("Z", "+00:00"))
        max_end_date = DateTime((dt + timedelta(days=3 * 366)).isoformat())
        return self.start >= reference_period_end and self.end <= max_end_date
