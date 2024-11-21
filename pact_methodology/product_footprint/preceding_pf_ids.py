from typing import List, Set
from .id import ProductFootprintId

class PrecedingPfIds:
    def __init__(self, pf_ids: List[ProductFootprintId] = None):
        """
        A collection of preceding product footprint identifiers.

        Attributes:
            pf_ids (Set[ProductFootprintId]): The set of preceding product footprint identifiers.

        Raises:
            ValueError: If the provided list contains non-unique or invalid ProductFootprintId objects.
        """
        if pf_ids is None:
            self.pf_ids = set()
        else:
            if not all(isinstance(pf_id, ProductFootprintId) for pf_id in pf_ids):
                raise ValueError("All elements in pf_ids must be instances of ProductFootprintId")
            if len(pf_ids) != len(set(pf_ids)):
                raise ValueError("pf_ids must not contain duplicates")
            self.pf_ids = set(pf_ids)

    def add(self, pf_id: ProductFootprintId):
        """
        Add a new product footprint identifier to the collection.

        Args:
            pf_id (ProductFootprintId): The product footprint identifier to add.

        Raises:
            ValueError: If the provided product footprint identifier is not unique.
        """
        if pf_id in self.pf_ids:
            raise ValueError("pf_id already exists in the collection")
        self.pf_ids.add(pf_id)

    def __iter__(self):
        return iter(self.pf_ids)

    def __len__(self):
        return len(self.pf_ids)

    def __repr__(self):
        return f"PrecedingPfIds({list(self.pf_ids)})"