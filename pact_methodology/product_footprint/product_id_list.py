from pact_methodology.exceptions import DuplicateIdError
from pact_methodology.urn import ProductId


class ProductIdList:
    """
    A list of ProductId objects.

    Attributes:
        product_ids (list): A list of ProductId objects.

    Raises:
        ValueError: If product_ids is not a list of ProductId objects.
        ValueError: If there are duplicate ProductId objects in the list.
    """

    def __init__(self, product_ids):
        """
        Initializes a ProductIdList object.

        Args:
            product_ids (list): A list of ProductId objects.

        Raises:
            ValueError: If product_ids is not a list of ProductId objects.
            ValueError: If there are duplicate ProductId objects in the list.
        """
        if not isinstance(product_ids, list) or not all(
            isinstance(product_id, ProductId) for product_id in product_ids
        ):
            raise ValueError("product_ids must be a list of ProductId")
        if len(set(product_ids)) != len(product_ids):
            raise DuplicateIdError("Duplicate product_ids are not allowed")
        self.product_ids = product_ids

    def __iter__(self):
        """
        Returns an iterator over the ProductId objects in the list.

        Returns:
            iterator: An iterator over the ProductId objects in the list.
        """
        return iter(self.product_ids)

    def __len__(self):
        """
        Returns the number of ProductId objects in the list.

        Returns:
            int: The number of ProductId objects in the list.
        """
        return len(self.product_ids)

    def __getitem__(self, index):
        """
        Returns the ProductId object at the specified index.

        Args:
            index (int): The index of the ProductId object to return.

        Returns:
            ProductId: The ProductId object at the specified index.
        """
        return self.product_ids[index]

    def __setitem__(self, index, value):
        """
        Sets the ProductId object at the specified index.

        Args:
            index (int): The index of the ProductId object to set.
            value (ProductId): The ProductId object to set.

        Raises:
            ValueError: If value is not a ProductId object.
        """
        if not isinstance(value, ProductId):
            raise ValueError("product_id must be an instance of ProductId")
        self.product_ids[index] = value

    def __delitem__(self, index):
        """
        Deletes the ProductId object at the specified index.

        Args:
            index (int): The index of the ProductId object to delete.
        """
        del self.product_ids[index]

    def append(self, product_id):
        """
        Appends a ProductId object to the list.

        Args:
            product_id (ProductId): The ProductId object to append.

        Raises:
            ValueError: If product_id is not a ProductId object.
            ValueError: If product_id is already in the list.
        """
        if not isinstance(product_id, ProductId):
            raise ValueError("product_id must be an instance of ProductId")
        if product_id in self.product_ids:
            raise DuplicateIdError("Duplicate product_ids are not allowed")
        self.product_ids.append(product_id)

    def insert(self, index, product_id):
        """
        Inserts a ProductId object at the specified index.

        Args:
            index (int): The index at which to insert the ProductId object.
            product_id (ProductId): The ProductId object to insert.

        Raises:
            ValueError: If product_id is not a ProductId object.
            ValueError: If product_id is already in the list.
        """
        if not isinstance(product_id, ProductId):
            raise ValueError("product_id must be an instance of ProductId")
        if product_id in self.product_ids:
            raise DuplicateIdError("Duplicate product_ids are not allowed")
        self.product_ids.insert(index, product_id)

    def remove(self, product_id):
        """
        Removes a ProductId object from the list.

        Args:
            product_id (ProductId): The ProductId object to remove.

        Raises:
            ValueError: If product_id is not in the list.
        """
        if product_id not in self.product_ids:
            raise ValueError("product_id is not in the list")
        self.product_ids.remove(product_id)
