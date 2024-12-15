class EmissionFactorDS:
    """Represents an emission factor database reference.

    This class represents references to emission factor databases as defined in
    Section 4.1.3.2 of the PACT Methodology.

    Args:
        name (str): The name of the emission factor database.
        version (str): The version of the emission factor database.

    Raises:
        ValueError: If name or version is empty or not a string.

    Examples:
        Create an emission factor database reference:
            >>> ef_db = EmissionFactorDS(name="ecoinvent", version="3.9.1")

        Convert to dictionary format:
            >>> ef_db.to_dict()
            {'name': 'ecoinvent', 'version': '3.9.1'}
    """

    def __init__(self, name: str, version: str):
        """Initialize an EmissionFactorDS instance.

        Args:
            name: The name of the emission factor database
            version: The version of the emission factor database

        Raises:
            ValueError: If name or version is empty or not a string
        """
        self.name = name
        self.version = version

    @property
    def name(self) -> str:
        """Get the database name.

        Returns:
            str: The database name string
        """
        return self._name

    @name.setter
    def name(self, value: str):
        """Set the database name.

        Args:
            value: The database name string

        Raises:
            ValueError: If value is empty or not a string
        """
        if not isinstance(value, str) or not value:
            raise ValueError("name must be a non-empty string")
        self._name = value

    @property
    def version(self) -> str:
        """Get the database version.

        Returns:
            str: The database version string
        """
        return self._version

    @version.setter
    def version(self, value: str):
        """Set the database version.

        Args:
            value: The database version string

        Raises:
            ValueError: If value is empty or not a string
        """
        if not isinstance(value, str) or not value:
            raise ValueError("version must be a non-empty string")
        self._version = value

    def to_dict(self) -> dict:
        """Convert to a dictionary representation.

        Returns:
            dict: A dictionary with the following structure:
                {
                    "name": str,  # The database name
                    "version": str  # The database version
                }

        Example:
            >>> ef_ds = EmissionFactorDS(name="ecoinvent", version="3.9.1")
            >>> ef_ds.to_dict()
            {'name': 'ecoinvent', 'version': '3.9.1'}
        """
        return {
            "name": self.name,
            "version": self.version
        }

    def __str__(self) -> str:
        """Get string representation.

        Returns:
            str: A human-readable string showing the attributes
        """
        return f"name={self.name}, version={self.version}"

    def __repr__(self) -> str:
        """Get detailed string representation.

        Returns:
            str: A string that could be used to recreate the object
        """
        return f"EmissionFactorDS(name='{self.name}', version='{self.version}')"

    def __eq__(self, other) -> bool:
        """Check equality with another instance.

        Args:
            other: The other instance to compare with

        Returns:
            bool: True if equal, False otherwise
        """
        if not isinstance(other, EmissionFactorDS):
            return False
        return self.name == other.name and self.version == other.version
