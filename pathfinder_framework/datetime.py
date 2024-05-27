from datetime import datetime, timedelta, timezone


class DateTime:
    """
    Represents a date and time string conforming to ISO 8601 with UTC timezone.

    Attributes:
        value (str): The date and time string in ISO 8601 format with UTC timezone, always represented with 'Z'
                    instead of '+00:00'.
    """

    def __init__(self, value: str) -> None:
        """
        Initializes a new DateTime object.

        Args:
            value (str): The date and time string in ISO 8601 format with UTC timezone.

        Raises:
            ValueError: If the value is not a valid ISO 8601 date and time string with UTC timezone.
        """
        try:
            dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
            if dt.tzinfo is None or dt.tzinfo.utcoffset(dt) != timedelta(0):
                raise ValueError("Invalid ISO 8601 date and time string, timezone must be UTC")
            self.value = dt.isoformat().replace('+00:00', 'Z')
        except ValueError:
            raise ValueError("Invalid ISO 8601 date and time string")

    @classmethod
    def now(cls) -> 'DateTime':
        """
        Creates a new DateTime object representing the current date and time in UTC.

        Returns:
            DateTime: A new DateTime object representing the current date and time in UTC.
        """
        return cls(datetime.now(timezone.utc).isoformat())

    def __eq__(self, other: object) -> bool:
        """
        Compares two DateTime objects for equality.

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        if not isinstance(other, DateTime):
            return False
        return self.value == other.value

    def __lt__(self, other: 'DateTime') -> bool:
        """
        Compares this DateTime object with another DateTime object for less than.

        Args:
            other (DateTime): The object to compare with.

        Returns:
            bool: True if this object is less than the other object, False otherwise.
        """
        if not isinstance(other, DateTime):
            raise TypeError("Other object must be a DateTime instance")
        return datetime.fromisoformat(self.value.replace('Z', '+00:00')) < datetime.fromisoformat(other.value.replace('Z', '+00:00'))

    def __le__(self, other: 'DateTime') -> bool:
        """
        Compares this DateTime object with another DateTime object for less than or equal.

        Args:
            other (DateTime): The object to compare with.

        Returns:
            bool: True if this object is less than or equal to the other object, False otherwise.
        """
        if not isinstance(other, DateTime):
            raise TypeError("Other object must be a DateTime instance")
        return datetime.fromisoformat(self.value.replace('Z', '+00:00')) <= datetime.fromisoformat(other.value.replace('Z', '+00:00'))

    def __gt__(self, other: 'DateTime') -> bool:
        """
        Compares this DateTime object with another DateTime object for greater than.

        Args:
            other (DateTime): The object to compare with.

        Returns:
            bool: True if this object is greater than the other object, False otherwise.
        """
        if not isinstance(other, DateTime):
            raise TypeError("Other object must be a DateTime instance")
        return datetime.fromisoformat(self.value.replace('Z', '+00:00')) > datetime.fromisoformat(other.value.replace('Z', '+00:00'))

    def __ge__(self, other: 'DateTime') -> bool:
        """
        Compares this DateTime object with another DateTime object for greater than or equal.

        Args:
            other (DateTime): The object to compare with.

        Returns:
            bool: True if this object is greater than or equal to the other object, False otherwise.
        """
        if not isinstance(other, DateTime):
            raise TypeError("Other object must be a DateTime instance")
        return datetime.fromisoformat(self.value.replace('Z', '+00:00')) >= datetime.fromisoformat(other.value.replace('Z', '+00:00'))

    def __repr__(self) -> str:
        """
        Returns a string representation of the DateTime object that can be used to recreate the object.

        Returns:
            str: A string representation of the DateTime object.
        """
        return f"DateTime('{self.value}')"

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the DateTime object.

        Returns:
            str: A human-readable string representation of the DateTime object.
        """
        return self.value

    @property
    def year(self) -> int:
        """
        The year of the date and time.

        Returns:
            int: The year.
        """
        return datetime.fromisoformat(self.value.replace('Z', '+00:00')).year

    @property
    def month(self) -> int:
        """
        The month of the date and time.

        Returns:
            int: The month.
        """
        return datetime.fromisoformat(self.value.replace('Z', '+00:00')).month

    @property
    def day(self) -> int:
        """
        The day of the date and time.

        Returns:
            int: The day.
        """
        return datetime.fromisoformat(self.value.replace('Z', '+00:00')).day

    @property
    def time(self) -> str:
        """
        The time of the date and time in ISO 8601 format (HH:MM:SS).

        Returns:
            str: The time.
        """
        return datetime.fromisoformat(self.value.replace('Z', '+00:00')).strftime('%H:%M:%S')