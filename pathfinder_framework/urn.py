import re

import casregnum
from urnparse import URN8141, InvalidURNFormatError


class URN:
    """
    A class representing a generic URN (RFC8141).
    """

    def __init__(self, value: str):
        self.value = value
        self._validate()

    def _validate(self):
        try:
            URN8141.from_string(self.value)
        except InvalidURNFormatError:
            raise ValueError("Value must be a valid URN")

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"URN(value='{self.value}')"

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
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
