from datetime import timedelta, datetime

from pathfinder_framework.datetime import DateTime


class ValidityPeriod:
    def __init__(self, start: DateTime, end: DateTime):
        if not isinstance(start, DateTime):
            raise ValueError("Start date must be a DateTime object")
        if not isinstance(end, DateTime):
            raise ValueError("End date must be a DateTime object")
        if start >= end:
            raise ValueError("Start date must be before end date")
        self.start = start
        self.end = end

    def is_valid(self, reference_period_end: DateTime) -> bool:
        if not isinstance(reference_period_end, DateTime):
            raise ValueError("Reference period end date must be a DateTime object")
        dt = datetime.fromisoformat(reference_period_end.value.replace('Z', '+00:00'))
        # TODO: Absolute known bug, if this ever becomes a problem that actually needs
        #       to be fixed, then reading this will be a very happy moment.
        max_end_date = DateTime((dt + timedelta(days=3 * 366)).isoformat())
        return self.start >= reference_period_end and self.end <= max_end_date
