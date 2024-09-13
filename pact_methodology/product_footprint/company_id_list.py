from pact_methodology.urn import CompanyId
from pact_methodology.exceptions import DuplicateIdError


class CompanyIdList:
    """
    A list of CompanyId objects.

    Attributes:
        company_ids (list): A list of CompanyId objects.

    Raises:
        ValueError: If company_ids is not a list of CompanyId objects.
        ValueError: If there are duplicate CompanyId objects in the list.
    """

    def __init__(self, company_ids):
        """
        Initializes a CompanyIdList object.

        Args:
            company_ids (list): A list of CompanyId objects.

        Raises:
            ValueError: If company_ids is not a list of CompanyId objects.
            ValueError: If there are duplicate CompanyId objects in the list.
        """
        if not isinstance(company_ids, list) or not all(
            isinstance(company_id, CompanyId) for company_id in company_ids
        ):
            raise ValueError("company_ids must be a list of CompanyId")
        if len(set(company_ids)) != len(company_ids):
            raise DuplicateIdError("Duplicate company_ids are not allowed")
        self.company_ids = company_ids

    def __iter__(self):
        """
        Returns an iterator over the CompanyId objects in the list.

        Returns:
            iterator: An iterator over the CompanyId objects in the list.
        """
        return iter(self.company_ids)

    def __len__(self):
        """
        Returns the number of CompanyId objects in the list.

        Returns:
            int: The number of CompanyId objects in the list.
        """
        return len(self.company_ids)

    def __getitem__(self, index):
        """
        Returns the CompanyId object at the specified index.

        Args:
            index (int): The index of the CompanyId object to return.

        Returns:
            CompanyId: The CompanyId object at the specified index.
        """
        return self.company_ids[index]

    def __setitem__(self, index, value):
        """
        Sets the CompanyId object at the specified index.

        Args:
            index (int): The index of the CompanyId object to set.
            value (CompanyId): The CompanyId object to set.

        Raises:
            ValueError: If value is not a CompanyId object.
        """
        if not isinstance(value, CompanyId):
            raise ValueError("company_id must be an instance of CompanyId")
        self.company_ids[index] = value

    def __delitem__(self, index):
        """
        Deletes the CompanyId object at the specified index.

        Args:
            index (int): The index of the CompanyId object to delete.
        """
        del self.company_ids[index]

    def append(self, company_id):
        """
        Appends a CompanyId object to the list.

        Args:
            company_id (CompanyId): The CompanyId object to append.

        Raises:
            ValueError: If company_id is not a CompanyId object.
            ValueError: If company_id is already in the list.
        """
        if not isinstance(company_id, CompanyId):
            raise ValueError("company_id must be an instance of CompanyId")
        if company_id in self.company_ids:
            raise DuplicateIdError("Duplicate company_ids are not allowed")
        self.company_ids.append(company_id)

    def insert(self, index, company_id):
        """
        Inserts a CompanyId object at the specified index.

        Args:
            index (int): The index at which to insert the CompanyId object.
            company_id (CompanyId): The CompanyId object to insert.

        Raises:
            ValueError: If company_id is not a CompanyId object.
            ValueError: If company_id is already in the list.
        """
        if not isinstance(company_id, CompanyId):
            raise ValueError("company_id must be an instance of CompanyId")
        if company_id in self.company_ids:
            raise DuplicateIdError("Duplicate company_ids are not allowed")
        self.company_ids.insert(index, company_id)

    def remove(self, company_id):
        """
        Removes a CompanyId object from the list.

        Args:
            company_id (CompanyId): The CompanyId object to remove.

        Raises:
            ValueError: If company_id is not in the list.
        """
        if company_id not in self.company_ids:
            raise ValueError("company_id is not in the list")
        self.company_ids.remove(company_id)
