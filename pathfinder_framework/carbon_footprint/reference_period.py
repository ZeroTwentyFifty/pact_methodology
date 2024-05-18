from pathfinder_framework.datetime import DateTime


class ReferencePeriod:
    def __init__(self, start: DateTime, end: DateTime):
        if not isinstance(start, DateTime):
            raise ValueError("Start date must be a DateTime object")
        if not isinstance(end, DateTime):
            raise ValueError("End date must be a DateTime object")
        if start >= end:
            raise ValueError("Start date must be before end date")
        self.start = start
        self.end = end

    def includes_2025_or_later(self) -> bool:
        return self.end.year >= 2025
