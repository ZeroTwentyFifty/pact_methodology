from typing import Any

from pathfinder_framework.product_footprint.id import ProductFootprintId


class ProductFootprint:
    """
    Represents the carbon footprint of a product under a specific scope and with values calculated in accordance
    with the Pathfinder Framework.
    """

    def __init__(self, *, id: ProductFootprintId | None = None):
        """Initializes a new ProductFootprint instance.

        Args:
            id (ProductFootprintId | None): The ProductFootprintId for this instance. If not provided, a new one
                will be generated.
        """
        self.id = id if id else ProductFootprintId()

    def __repr__(self) -> str:
        """Returns a string representation of the ProductFootprint instance."""
        return f"ProductFootprint(id={self.id})"
