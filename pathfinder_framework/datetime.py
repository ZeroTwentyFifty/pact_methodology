from datetime import datetime, timedelta


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

    def __repr__(self) -> str:
        """
        Returns a string representation of the DateTime object.

        Returns:
            str: A string representation of the DateTime object.
        """
        return f"DateTime({self.value})"
