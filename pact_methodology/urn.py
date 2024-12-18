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
    """
    A class representing a Company ID URN, extending the generic URN class.

    This class encapsulates the functionality to create, validate, and represent a Company ID URN.
    It ensures that the URN conforms to specific Company ID formats.

    Examples:
        >>> company_id = CompanyId("urn:pathfinder:company:customcode:buyer-assigned:acme-corp")
        >>> str(company_id)
        'urn:pathfinder:company:customcode:buyer-assigned:acme-corp'
        >>> repr(company_id)
        "CompanyId(value='urn:pathfinder:company:customcode:buyer-assigned:acme-corp')"
        >>> hash(company_id) == hash("urn:pathfinder:company:customcode:buyer-assigned:acme-corp")
        True
        >>> company_id == CompanyId("urn:pathfinder:company:customcode:buyer-assigned:acme-corp")
        True
        >>> company_id == "urn:pathfinder:company:customcode:buyer-assigned:acme-corp"
        False
    """

    BUYER_ASSIGNED_PATTERN: re.Pattern = re.compile(
        r"^urn:pathfinder:company:customcode:buyer-assigned:[a-zA-Z0-9-]+$"
    )
    VENDOR_ASSIGNED_PATTERN: re.Pattern = re.compile(
        r"^urn:pathfinder:company:customcode:vendor-assigned:[a-zA-Z0-9-]+$"
    )

    def __init__(self, value: str):
        """
        Initialize a CompanyId instance.

        Args:
            value (str): The Company ID string to be validated and stored.

        Raises:
            ValueError: If the provided value is not a valid URN or does not conform to the Company ID format.

        Examples:
            >>> CompanyId("urn:pathfinder:company:customcode:buyer-assigned:acme-corp")
            CompanyId(value='urn:pathfinder:company:customcode:buyer-assigned:acme-corp')
            >>> CompanyId("invalid-urn")
            Traceback (most recent call last):
                ...
            ValueError: Value must be a valid URN
            >>> CompanyId("urn:pathfinder:company:customcode:invalid-type:12345")
            Traceback (most recent call last):
                ...
            ValueError: CompanyId does not conform to the required format
        """
        super().__init__(value)
        self._validate_company_id()

    def _validate_company_id(self) -> None:
        """
        Validate the Company ID format beyond the URN standard.

        Raises:
            ValueError: If the URN does not match the required Company ID format.
        """
        if not (
            self.BUYER_ASSIGNED_PATTERN.match(self.value)
            or self.VENDOR_ASSIGNED_PATTERN.match(self.value)
        ):
            raise ValueError("CompanyId does not conform to the required format")

    def __str__(self) -> str:
        """
        Return the string representation of the CompanyId.

        Returns:
            str: The CompanyId value.

        Examples:
            >>> company_id = CompanyId("urn:pathfinder:company:customcode:buyer-assigned:acme-corp")
            >>> str(company_id)
            'urn:pathfinder:company:customcode:buyer-assigned:acme-corp'
        """
        return self.value

    def __repr__(self) -> str:
        """
        Return the representation of the CompanyId instance.

        Returns:
            str: A string representation of the CompanyId instance.

        Examples:
            >>> company_id = CompanyId("urn:pathfinder:company:customcode:buyer-assigned:acme-corp")
            >>> repr(company_id)
            "CompanyId(value='urn:pathfinder:company:customcode:buyer-assigned:acme-corp')"
        """
        return f"CompanyId(value='{self.value}')"

    def __hash__(self) -> int:
        """
        Return the hash of the CompanyId value.

        Returns:
            int: The hash value of the CompanyId.

        Examples:
            >>> company_id = CompanyId("urn:pathfinder:company:customcode:buyer-assigned:acme-corp")
            >>> hash(company_id) == hash("urn:pathfinder:company:customcode:buyer-assigned:acme-corp")
            True
        """
        return hash(self.value)

    def __eq__(self, other: Any) -> bool:
        """
        Check if this CompanyId is equal to another object.

        Args:
            other (Any): The object to compare with.

        Returns:
            bool: True if the objects are equal, False otherwise.

        Examples:
            >>> company_id1 = CompanyId("urn:pathfinder:company:customcode:buyer-assigned:acme-corp")
            >>> company_id2 = CompanyId("urn:pathfinder:company:customcode:buyer-assigned:acme-corp")
            >>> company_id1 == company_id2
            True
            >>> company_id1 == "urn:pathfinder:company:customcode:buyer-assigned:acme-corp"
            False
        """
        if not isinstance(other, CompanyId):
            return False
        return self.value == other.value


class ProductId(URN):
    """
    A class representing a ProductId URN, extending the generic URN class.

    This class encapsulates the functionality to create, validate, and represent a ProductId URN.
    It ensures that the URN conforms to specific ProductId formats.

    Examples:
        >>> product_id = ProductId("urn:pathfinder:product:customcode:buyer-assigned:ABC-123")
        >>> str(product_id)
        'urn:pathfinder:product:customcode:buyer-assigned:ABC-123'
        >>> repr(product_id)
        "ProductId(value='urn:pathfinder:product:customcode:buyer-assigned:ABC-123')"
        >>> hash(product_id) == hash("urn:pathfinder:product:customcode:buyer-assigned:ABC-123")
        True
        >>> product_id == ProductId("urn:pathfinder:product:customcode:buyer-assigned:ABC-123")
        True
        >>> product_id == "urn:pathfinder:product:customcode:buyer-assigned:ABC-123"
        False
    """

    BUYER_ASSIGNED_PATTERN: re.Pattern = re.compile(
        r"^urn:pathfinder:product:customcode:buyer-assigned:[a-zA-Z0-9-]+$"
    )
    VENDOR_ASSIGNED_PATTERN: re.Pattern = re.compile(
        r"^urn:pathfinder:product:customcode:vendor-assigned:[a-zA-Z0-9-]+$"
    )
    CAS_PATTERN: re.Pattern = re.compile(r"^urn:pathfinder:product:id:cas:\b\d{2,7}-\d{2}-\d\b$")
    IUPAC_INCHI_PATTERN: re.Pattern = re.compile(r"^urn:pathfinder:product:id:iupac-inchi:.*$")

    def __init__(self, value: str):
        """
        Initialize a ProductId instance.

        Args:
            value (str): The ProductId string to be validated and stored.

        Raises:
            ValueError: If the provided value is not a valid URN or does not conform to the ProductId format.

        Examples:
            >>> ProductId("urn:pathfinder:product:customcode:buyer-assigned:ABC-123")
            ProductId(value='urn:pathfinder:product:customcode:buyer-assigned:ABC-123')
            >>> ProductId("invalid-urn")
            Traceback (most recent call last):
                ...
            ValueError: Value must be a valid URN
            >>> ProductId("urn:pathfinder:product:customcode:invalid:ABC-123")
            Traceback (most recent call last):
                ...
            ValueError: ProductId does not conform to the required format
        """
        super().__init__(value)
        self._validate()

    def _validate(self) -> None:
        """
        Validate the ProductId format.

        Raises:
            ValueError: If the ProductId does not conform to any of the required formats.
        """
        if not any(
            [
                self.BUYER_ASSIGNED_PATTERN.match(self.value),
                self.VENDOR_ASSIGNED_PATTERN.match(self.value),
                self._validate_cas_number(self.value),
                self.IUPAC_INCHI_PATTERN.match(self.value),
            ]
        ):
            raise ValueError("ProductId does not conform to the required format")

    def _validate_cas_number(self, value: str) -> bool:
        """
        Validate the CAS number format.

        Args:
            value (str): The URN string to validate.

        Returns:
            bool: True if the CAS number is valid, False otherwise.
        """
        if self.CAS_PATTERN.match(value):
            try:
                cas_value = value.rsplit(":", 1)[-1]
                casregnum.CAS(cas_value)
                return True
            except ValueError:
                return False
        return False

    def __str__(self) -> str:
        """
        Return the string representation of the ProductId.

        Returns:
            str: The ProductId value.

        Examples:
            >>> product_id = ProductId("urn:pathfinder:product:customcode:buyer-assigned:ABC-123")
            >>> str(product_id)
            'urn:pathfinder:product:customcode:buyer-assigned:ABC-123'
        """
        return self.value

    def __repr__(self) -> str:
        """
        Return the representation of the ProductId instance.

        Returns:
            str: A string representation of the ProductId instance.

        Examples:
            >>> product_id = ProductId("urn:pathfinder:product:customcode:buyer-assigned:ABC-123")
            >>> repr(product_id)
            "ProductId(value='urn:pathfinder:product:customcode:buyer-assigned:ABC-123')"
        """
        return f"ProductId(value='{self.value}')"

    def __hash__(self) -> int:
        """
        Return the hash of the ProductId value.

        Returns:
            int: The hash value of the ProductId.

        Examples:
            >>> product_id = ProductId("urn:pathfinder:product:customcode:buyer-assigned:ABC-123")
            >>> hash(product_id) == hash("urn:pathfinder:product:customcode:buyer-assigned:ABC-123")
            True
        """
        return hash(self.value)

    def __eq__(self, other: Any) -> bool:
        """
        Check if this ProductId is equal to another object.

        Args:
            other (Any): The object to compare with.

        Returns:
            bool: True if the objects are equal, False otherwise.

        Examples:
            >>> product_id1 = ProductId("urn:pathfinder:product:customcode:buyer-assigned:ABC-123")
            >>> product_id2 = ProductId("urn:pathfinder:product:customcode:buyer-assigned:ABC-123")
            >>> product_id1 == product_id2
            True
            >>> product_id1 == "urn:pathfinder:product:customcode:buyer-assigned:ABC-123"
            False
        """
        if not isinstance(other, ProductId):
            return False
        return self.value == other.value
