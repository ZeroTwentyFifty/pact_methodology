from typing import Iterable, Set

from pact_methodology.carbon_footprint.cross_sectoral_standard import CrossSectoralStandard


class CrossSectoralStandardSet:
    """
    CrossSectoralStandardSet is a set of CrossSectoralStandard values.

    This class provides methods to add, remove, and check for the presence of standards within the set.

    Examples:
        Creating a set of standards:
        >>> standards_set = CrossSectoralStandardSet()
        >>> standards_set.add(CrossSectoralStandard.GHG_PROTOCOL)
        >>> standards_set.add(CrossSectoralStandard.ISO_14067)
        >>> print(standards_set)
        {'GHG Protocol Product standard', 'ISO Standard 14067'}

        Checking for the presence of a standard:
        >>> CrossSectoralStandard.ISO_14044 in standards_set
        False

        Removing a standard:
        >>> standards_set.remove(CrossSectoralStandard.GHG_PROTOCOL)
        >>> print(standards_set)
        {'ISO Standard 14067'}

        Adding multiple standards:
        >>> standards_set.add_multiple([CrossSectoralStandard.GHG_PROTOCOL, CrossSectoralStandard.ISO_14044])
        >>> print(standards_set)
        {'GHG Protocol Product standard', 'ISO Standard 14067', 'ISO Standard 14044'}

        String representation of the set:
        >>> str(standards_set)
        "{'GHG Protocol Product standard', 'ISO Standard 14067', 'ISO Standard 14044'}"

        Representation of the set:
        >>> repr(standards_set)
        "CrossSectoralStandardSet({CrossSectoralStandard.GHG_PROTOCOL, CrossSectoralStandard.ISO_14067, CrossSectoralStandard.ISO_14044})"
    """

    def __init__(self):
        self._standards: Set[CrossSectoralStandard] = set()

    def add(self, standard: CrossSectoralStandard):
        """Add a standard to the set."""
        self._standards.add(standard)

    def remove(self, standard: CrossSectoralStandard):
        """Remove a standard from the set."""
        self._standards.discard(standard)

    def add_multiple(self, standards: Iterable[CrossSectoralStandard]):
        """Add multiple standards to the set."""
        self._standards.update(standards)

    def __contains__(self, standard: CrossSectoralStandard) -> bool:
        """Check if a standard is in the set."""
        return standard in self._standards

    def __str__(self):
        return str({str(standard) for standard in self._standards})

    def __repr__(self):
        return f"CrossSectoralStandardSet({self._standards})"
