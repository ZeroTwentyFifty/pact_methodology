import uuid


class ProductFootprintId(uuid.UUID):
    def __init__(self, value: str | None = None) -> None:
        """
        A unique identifier for a Product Footprint.

        The Product Footprint ID is a UUID v4 as specified in RFC 4122.

        Attributes:
            value (str): The UUID value of the Product Footprint ID.

        References:
            - https://www.rfc-editor.org/rfc/rfc4122
            - Pathfinder Framework - Guidance for the Accounting and Exchange of Product Life Cycle Emissions Version 2.0
        """
        if value is None:
            super().__init__(uuid.uuid4().hex, version=4)
        else:
            super().__init__(value, version=4)
