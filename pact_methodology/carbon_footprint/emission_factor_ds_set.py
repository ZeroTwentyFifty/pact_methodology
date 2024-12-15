from typing import List, Optional
from pact_methodology.carbon_footprint.emission_factor_ds import EmissionFactorDS
from pact_methodology.exceptions import DuplicateIdError


class EmissionFactorDSSet:
    """A set of emission factor database references.

    This class represents a collection of one or more emission factor database references
    as defined in Section 5.7 of the PACT Methodology.

    Attributes:
        emission_factor_ds_list (List[EmissionFactorDS]): A list of EmissionFactorDS objects.
            Each reference specifies a database name and version.

    Examples:
        Create a set with a single database reference:
        >>> ef_ds = EmissionFactorDS(name="ecoinvent", version="3.9.1")
        >>> ef_ds_set = EmissionFactorDSSet([ef_ds])

        Create a set with multiple references:
        >>> ef_ds_list = [
        ...     EmissionFactorDS(name="ecoinvent", version="3.9.1"),
        ...     EmissionFactorDS(name="gabi", version="2023.1")
        ... ]
        >>> ef_ds_set = EmissionFactorDSSet(ef_ds_list)

        Convert to dictionary format:
        >>> ef_ds_set.to_dict()
        [
            {'name': 'ecoinvent', 'version': '3.9.1'},
            {'name': 'gabi', 'version': '2023.1'}
        ]

        Remove a reference:
        >>> ef_ds_set.remove_ds(ef_ds)
        >>> len(ef_ds_set.emission_factor_ds_list)
        1
    """

    def __init__(self, emission_factor_ds_list: Optional[List[EmissionFactorDS]] = None):
        """Initialize an EmissionFactorDSSet instance.

        Args:
            emission_factor_ds_list: A list of EmissionFactorDS objects. Defaults to an empty list.
                Each reference must specify a valid database name and version.

        Raises:
            ValueError: If list contains invalid EmissionFactorDS objects.
            DuplicateIdError: If there are duplicate database references.

        Examples:
            Initialize with a single reference:
            >>> ef_ds = EmissionFactorDS(name="ecoinvent", version="3.9.1")
            >>> ef_ds_set = EmissionFactorDSSet([ef_ds])

            Initialize with multiple references:
            >>> ef_ds_list = [
            ...     EmissionFactorDS(name="ecoinvent", version="3.9.1"),
            ...     EmissionFactorDS(name="gabi", version="2023.1")
            ... ]
            >>> ef_ds_set = EmissionFactorDSSet(ef_ds_list)
        """
        self.emission_factor_ds_list = emission_factor_ds_list if emission_factor_ds_list is not None else []

    @property
    def emission_factor_ds_list(self) -> List[EmissionFactorDS]:
        """Get the list of emission factor database references.

        Returns:
            A list of EmissionFactorDS objects representing the database references.

        Examples:
            >>> ef_ds_set = EmissionFactorDSSet()
            >>> ef_ds_set.emission_factor_ds_list
            []

            >>> ef_ds = EmissionFactorDS(name="ecoinvent", version="3.9.1")
            >>> ef_ds_set = EmissionFactorDSSet([ef_ds])
            >>> ef_ds_set.emission_factor_ds_list
            [EmissionFactorDS(name='ecoinvent', version='3.9.1')]
        """
        return self._emission_factor_ds_list

    @emission_factor_ds_list.setter
    def emission_factor_ds_list(self, value: List[EmissionFactorDS]):
        """Set the list of emission factor database references.

        Args:
            value: A list of EmissionFactorDS objects to set as the current references.

        Raises:
            ValueError: If value is not a list of valid EmissionFactorDS objects.
            DuplicateIdError: If there are duplicate references.

        Examples:
            >>> ef_ds_set = EmissionFactorDSSet()
            >>> ef_ds_list = [
            ...     EmissionFactorDS(name="ecoinvent", version="3.9.1")
            ... ]
            >>> ef_ds_set.emission_factor_ds_list = ef_ds_list

            Invalid assignment raises ValueError:
            >>> ef_ds_set.emission_factor_ds_list = ["not a reference"]  # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
                ...
            ValueError: emission_factor_ds_list must be a list of EmissionFactorDS objects
        """
        if not isinstance(value, list) or not all(isinstance(ds, EmissionFactorDS) for ds in value):
            raise ValueError("emission_factor_ds_list must be a list of EmissionFactorDS objects")

        # Check for duplicates
        seen = set()
        for ds in value:
            key = (ds.name, ds.version)
            if key in seen:
                raise DuplicateIdError("duplicate emission factor database references found")
            seen.add(key)

        self._emission_factor_ds_list = value

    def add_ds(self, ds: EmissionFactorDS):
        """Add an emission factor database reference to the set.

        Args:
            ds: An EmissionFactorDS object to add to the current set.

        Raises:
            ValueError: If ds is not a valid EmissionFactorDS instance.
            DuplicateIdError: If the reference already exists in the set.

        Examples:
            >>> ef_ds_set = EmissionFactorDSSet()
            >>> ef_ds = EmissionFactorDS(name="ecoinvent", version="3.9.1")
            >>> ef_ds_set.add_ds(ef_ds)
            >>> len(ef_ds_set.emission_factor_ds_list)
            1

            Adding an invalid reference raises ValueError:
            >>> ef_ds_set.add_ds("not a reference")  # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
                ...
            ValueError: ds must be an instance of EmissionFactorDS
        """
        if not isinstance(ds, EmissionFactorDS):
            raise ValueError("ds must be an instance of EmissionFactorDS")

        # Check for duplicates
        key = (ds.name, ds.version)
        if any(key == (existing_ds.name, existing_ds.version) for existing_ds in self._emission_factor_ds_list):
            raise DuplicateIdError("duplicate emission factor database reference")

        self._emission_factor_ds_list.append(ds)

    def remove_ds(self, ds: EmissionFactorDS):
        """Remove an emission factor database reference from the set.

        Args:
            ds: An EmissionFactorDS object to remove from the current set.

        Raises:
            ValueError: If ds is invalid or not found in the current set.

        Examples:
            >>> ef_ds = EmissionFactorDS(name="ecoinvent", version="3.9.1")
            >>> ef_ds_set = EmissionFactorDSSet([ef_ds])
            >>> ef_ds_set.remove_ds(ef_ds)
            >>> len(ef_ds_set.emission_factor_ds_list)
            0

            Removing a non-existent reference raises ValueError:
            >>> other_ds = EmissionFactorDS(name="gabi", version="2023.1")
            >>> ef_ds_set.remove_ds(other_ds)  # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
                ...
            ValueError: reference not found in the set
        """
        if not isinstance(ds, EmissionFactorDS):
            raise ValueError("ds must be an instance of EmissionFactorDS")
        if ds not in self._emission_factor_ds_list:
            raise ValueError("reference not found in the set")
        self._emission_factor_ds_list.remove(ds)

    def to_dict(self) -> List[dict]:
        """Convert the set to a JSON-compatible format.

        Returns:
            A list of dictionaries, each representing an EmissionFactorDS
            as a JSON object with name and version.

        Examples:
            >>> ef_ds1 = EmissionFactorDS(name="ecoinvent", version="3.9.1")
            >>> ef_ds2 = EmissionFactorDS(name="gabi", version="2023.1")
            >>> ef_ds_set = EmissionFactorDSSet([ef_ds1, ef_ds2])
            >>> ef_ds_set.to_dict()
            [{'name': 'ecoinvent', 'version': '3.9.1'}, {'name': 'gabi', 'version': '2023.1'}]
        """
        return [ds.to_dict() for ds in self._emission_factor_ds_list]

    def __str__(self) -> str:
        """Get string representation of the set.

        Returns:
            A human-readable string showing the contained references.

        Examples:
            >>> ef_ds = EmissionFactorDS(name="ecoinvent", version="3.9.1")
            >>> ef_ds_set = EmissionFactorDSSet([ef_ds])
            >>> str(ef_ds_set)
            'EmissionFactorDSSet(emission_factor_ds_list=[EmissionFactorDS(name=\'ecoinvent\', version=\'3.9.1\')])'
        """
        return f"EmissionFactorDSSet(emission_factor_ds_list={self._emission_factor_ds_list})"

    def __repr__(self) -> str:
        """Get detailed string representation of the set.

        Returns:
            A string containing all information needed to recreate the object.

        Examples:
            >>> ef_ds = EmissionFactorDS(name="ecoinvent", version="3.9.1")
            >>> ef_ds_set = EmissionFactorDSSet([ef_ds])
            >>> repr(ef_ds_set)
            'EmissionFactorDSSet(emission_factor_ds_list=[EmissionFactorDS(name=\'ecoinvent\', version=\'3.9.1\')])'
        """
        return f"EmissionFactorDSSet(emission_factor_ds_list={self._emission_factor_ds_list!r})"

    def __eq__(self, other) -> bool:
        """Check if two sets are equal.

        Args:
            other: Another EmissionFactorDSSet to compare with this one.

        Returns:
            True if both sets contain the same references in the same order.

        Examples:
            >>> ef_ds = EmissionFactorDS(name="ecoinvent", version="3.9.1")
            >>> set1 = EmissionFactorDSSet([ef_ds])
            >>> set2 = EmissionFactorDSSet([ef_ds])
            >>> set1 == set2
            True

            >>> other_ds = EmissionFactorDS(name="gabi", version="2023.1")
            >>> set3 = EmissionFactorDSSet([other_ds])
            >>> set1 == set3
            False
        """
        if not isinstance(other, EmissionFactorDSSet):
            return False
        return self._emission_factor_ds_list == other._emission_factor_ds_list

    def __ne__(self, other) -> bool:
        """Check if two sets are not equal.

        Args:
            other: Another EmissionFactorDSSet to compare with this one.

        Returns:
            True if the sets differ in any way.

        Examples:
            >>> ef_ds = EmissionFactorDS(name="ecoinvent", version="3.9.1")
            >>> set1 = EmissionFactorDSSet([ef_ds])
            >>> set2 = EmissionFactorDSSet([ef_ds])
            >>> set1 != set2
            False

            >>> other_ds = EmissionFactorDS(name="gabi", version="2023.1")
            >>> set3 = EmissionFactorDSSet([other_ds])
            >>> set1 != set3
            True
        """
        return not self.__eq__(other)
