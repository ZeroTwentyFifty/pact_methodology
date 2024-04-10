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

        Attributes:
            id (ProductFootprintId): The unique identifier for this ProductFootprint.
            spec_version (str): The version of the ProductFootprint data specification. Currently, hardcoded to "2.0.0",
                but may be updated in the future to support different versions. There is a little confusion between
                the definition in the technical documentation and the framework documentation, and the steering council
                will be looking to implement this in a more SemVer friendly way, which it currently is not. So just
                introduce it hard-coded for now, and revise it later.
        """
        self.id = id if id else ProductFootprintId()
        self.spec_version = "2.0.0"

    def __repr__(self) -> str:
        """Returns a string representation of the ProductFootprint instance."""
        return f"ProductFootprint(id={self.id})"
