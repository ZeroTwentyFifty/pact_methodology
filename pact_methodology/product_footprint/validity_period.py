from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from pact_methodology.datetime import DateTime


class ValidityPeriod:
    """
    Represents a validity period with a start and end date.

    Attributes:
        start (DateTime): The start date of the validity period.
        end (DateTime): The end date of the validity period.
    """


    def __init__(
        self,
        *,
        start: DateTime = None,
        end: DateTime = None,
        reference_period_end: DateTime = None
    ) -> None:
        """
        Represents a validity period with a start and end date.

        Args:
            start (DateTime, optional): The start date of the validity period. Defaults to None.
            end (DateTime, optional): The end date of the validity period. Defaults to None.
            reference_period_end (DateTime, optional): The reference date to calculate default start and end if not provided. Defaults to None.

        Raises:
            ValueError: If start or end dates are not provided and reference period end date is not provided.
            ValueError: If start or end dates are not DateTime objects.
            ValueError: If start date is not before end date.
        """
        if not (start and end):
            if reference_period_end is None:
                raise ValueError("Reference period end date must be provided when start or end dates are not specified.")
            if not isinstance(reference_period_end, DateTime):
                raise ValueError("Reference period end must be a DateTime object")

            self.start = reference_period_end
            self.end = self.three_years_from_end(reference_period_end)
        else:
            if not isinstance(start, DateTime):
                raise ValueError("Start date must be a DateTime object")
            if not isinstance(end, DateTime):
                raise ValueError("End date must be a DateTime object")
            if start >= end:
                raise ValueError("Start date must be before end date")
            self.start = start
            self.end = end

    @classmethod
    def three_years_from_end(cls, end_date: DateTime) -> DateTime:
        """
        Calculate the date that is 3 years from the given end date.

        Args:
            end_date (DateTime): The end date to calculate from.

        Returns:
            DateTime: The date that is 3 years from the given end date.
        """
        dt = datetime.fromisoformat(end_date.iso_string.replace("Z", "+00:00"))
        return DateTime((dt + relativedelta(years=3)).isoformat())

    def is_valid(self, reference_period_end: DateTime) -> bool:
        """
        Checks if the validity period is valid with respect to the reference period end date.

        Args:
            reference_period_end (DateTime): The reference period end date.

        Returns:
            bool: True if the validity period is valid, False otherwise.

        Raises:
            ValueError: If reference period end date is not a DateTime object.
        """
        if not isinstance(reference_period_end, DateTime):
            raise ValueError("Reference period end date must be a DateTime object")

        max_end_date = self.three_years_from_end(reference_period_end)
        return self.start >= reference_period_end and self.end <= max_end_date
