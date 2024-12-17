import re
from typing import Any

import casregnum
from urnparse import URN8141, InvalidURNFormatError


import re
from typing import Any

import casregnum
from urnparse import URN8141, InvalidURNFormatError


class URN:
    """
    A class representing a generic URN (RFC8141).

    This class encapsulates the functionality to create, validate, and represent a URN.
    It ensures that the URN conforms to the RFC8141 standard.

    Examples:
        >>> urn = URN("urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6")
        >>> str(urn)
        'urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6'
        >>> repr(urn)
        "URN(value='urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6')"
        >>> hash(urn) == hash("urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6")
        True
        >>> urn == URN("urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6")
        True
        >>> urn == "urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6"
        False
    """

    def __init__(self, value: str):
        """
        Initialize a URN instance.

        Args:
            value (str): The URN string to be validated and stored.

        Raises:
            ValueError: If the provided value is not a valid URN according to RFC8141.

        Examples:
            >>> URN("urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6")
            URN(value='urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6')
            >>> URN("invalid-urn")
            Traceback (most recent call last):
                ...
            ValueError: Value must be a valid URN
        """
        try:
            URN8141.from_string(value)
        except InvalidURNFormatError:
            raise ValueError("Value must be a valid URN")
        self.value = value

    def __str__(self) -> str:
        """
        Return the string representation of the URN.

        Returns:
            str: The URN value.

        Examples:
            >>> urn = URN("urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6")
            >>> str(urn)
            'urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6'
        """
        return self.value

    def __repr__(self) -> str:
        """
        Return the representation of the URN instance.

        Returns:
            str: A string representation of the URN instance.

        Examples:
            >>> urn = URN("urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6")
            >>> repr(urn)
            "URN(value='urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6')"
        """
        return f"URN(value='{self.value}')"

    def __hash__(self) -> int:
        """
        Return the hash of the URN value.

        Returns:
            int: The hash value of the URN.

        Examples:
            >>> urn = URN("urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6")
            >>> hash(urn) == hash("urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6")
            True
        """
        return hash(self.value)

    def __eq__(self, other: Any) -> bool:
        """
        Check if this URN is equal to another object.

        Args:
            other (Any): The object to compare with.

        Returns:
            bool: True if the objects are equal, False otherwise.

        Examples:
            >>> urn1 = URN("urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6")
            >>> urn2 = URN("urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6")
            >>> urn1 == urn2
            True
            >>> urn1 == "urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6"
            False
        """
        if not isinstance(other, URN):
            return False
        return self.value == other.value


class CompanyId(URN):
    BUYER_ASSIGNED_PATTERN = re.compile(
        r"^urn:pathfinder:company:customcode:buyer-assigned:[a-zA-Z0-9-]+$"
    )
    VENDOR_ASSIGNED_PATTERN = re.compile(
        r"^urn:pathfinder:company:customcode:vendor-assigned:[a-zA-Z0-9-]+$"
    )

    def _validate(self):
        super()._validate()  # Inherit URN validation

        if not (
            self.BUYER_ASSIGNED_PATTERN.match(self.value)
            or self.VENDOR_ASSIGNED_PATTERN.match(self.value)
        ):
            raise ValueError("CompanyId does not conform to the required format")


class ProductId(URN):
    BUYER_ASSIGNED_PATTERN = re.compile(
        r"^urn:pathfinder:product:customcode:buyer-assigned:[a-zA-Z0-9-]+$"
    )
    VENDOR_ASSIGNED_PATTERN = re.compile(
        r"^urn:pathfinder:product:customcode:vendor-assigned:[a-zA-Z0-9-]+$"
    )
    CAS_PATTERN = re.compile(r"^urn:pathfinder:product:id:cas:\b\d{2,7}-\d{2}-\d\b$")
    IUPAC_INCHI_PATTERN = re.compile(r"^urn:pathfinder:product:id:iupac-inchi:.*$")

    def _validate(self):
        super()._validate()

        if not any(
            [
                self.BUYER_ASSIGNED_PATTERN.match(self.value),
                self.VENDOR_ASSIGNED_PATTERN.match(self.value),
                self._validate_cas_number(self.value),
                self.IUPAC_INCHI_PATTERN.match(self.value),
            ]
        ):
            raise ValueError("ProductId does not conform to the required format")

    def _validate_cas_number(self, value):
        print(value)
        if self.CAS_PATTERN.match(value):
            try:
                print(value.rsplit(":", 1)[-1])
                casregnum.CAS(value.rsplit(":", 1)[-1])
                return True
            except ValueError:
                return False
        return False
