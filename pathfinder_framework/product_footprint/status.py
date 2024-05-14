from enum import Enum


class ProductFootprintStatus(Enum):
    """
    Status of a product footprint.

    Attributes:
        ACTIVE: The default status of a product footprint. A product footprint with
                status Active can be used by data recipients, e.g., for product
                footprint calculations.
        DEPRECATED: The product footprint is deprecated and should not be used for
                    e.g., product footprint calculations by data recipients.
    """

    ACTIVE = "Active"
    DEPRECATED = "Deprecated"
