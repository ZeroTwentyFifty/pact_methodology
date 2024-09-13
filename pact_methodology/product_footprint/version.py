class Version:
    """
    Represents a version of a product footprint.

    Attributes:
        version (int): The version number, which must be an integer in the range 0 to 2^31-1.

    Raises:
        ValueError: If the version number is not an integer or is out of range.
    """

    def __init__(self, version: int) -> None:
        """
        Initializes a new Version object.

        Args:
            version (int): The version number.

        Raises:
            ValueError: If the version number is not an integer or is out of range.
        """
        if not isinstance(version, int):
            raise ValueError("Version must be an integer")
        if version < 0 or version > 2**31 - 1:
            raise ValueError("Version must be in the range of 0 to 2^31-1")
        self.version = version

    def __eq__(self, other: object) -> bool:
        """
        Compares two Version objects for equality.

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        if not isinstance(other, Version):
            return False
        return self.version == other.version

    def __repr__(self) -> str:
        """
        Returns a string representation of the Version object.

        Returns:
            str: A string representation of the Version object.
        """
        return f"Version({self.version})"

    @classmethod
    def get_latest_version(cls, *versions: "Version") -> "Version":
        """
        Returns the latest version from a list of versions.

        Args:
            *versions (Version): The versions to compare.

        Returns:
            Version: The latest version.

        Raises:
            ValueError: If any of the arguments are not instances of Version.
        """
        if not all(isinstance(version, cls) for version in versions):
            raise ValueError("All arguments must be instances of Version")
        return max(versions, key=lambda version: version.version)
