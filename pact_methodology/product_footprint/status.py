from enum import Enum

class Status(Enum):
    """
    Enumeration of possible statuses for a product footprint.

    Attributes:
        ACTIVE (str): The product footprint is active and can be used by data recipients.
        DEPRECATED (str): The product footprint is deprecated and should not be used.

    Examples:
        >>> Status.ACTIVE.value
        'Active'
        >>> Status.DEPRECATED.value
        'Deprecated'
    """
    ACTIVE = "Active"
    DEPRECATED = "Deprecated"

class ProductFootprintStatus:
    """
    Represents the status information of a product footprint, including the status and an optional comment.

    Attributes:
        status (Status): The status of the product footprint.
        comment (str | None): An optional comment describing the status.

    Examples:
        >>> status_info = ProductFootprintStatus(status=Status.ACTIVE, comment="Active comment")
        >>> status_info.status
        <Status.ACTIVE: 'Active'>
        >>> status_info.comment
        'Active comment'
    """

    def __init__(self, status: Status, comment: str | None = None):
        """
        Initializes a new ProductFootprintStatus instance.

        Args:
            status (Status): The status of the product footprint.
            comment (str | None): An optional comment describing the status.

        Raises:
            ValueError: If status is not an instance of Status or comment is not a string or None.
        """
        self.status = status
        self.comment = comment

    @property
    def status(self):
        """Gets the status of the product footprint."""
        return self._status

    @status.setter
    def status(self, value):
        """Sets the status of the product footprint.

        Args:
            value (Status): The status to set.

        Raises:
            ValueError: If value is not an instance of Status.

        Examples:
            >>> status_info = ProductFootprintStatus(status=Status.ACTIVE)
            >>> status_info.status = Status.DEPRECATED
            >>> status_info.status
            <Status.DEPRECATED: 'Deprecated'>
        """
        if not isinstance(value, Status):
            raise ValueError("status must be an instance of Status")
        self._status = value

    @property
    def comment(self):
        """Gets the comment describing the status of the product footprint."""
        return self._comment

    @comment.setter
    def comment(self, value):
        """Sets the comment describing the status of the product footprint.

        Args:
            value (str | None): The status comment to set.

        Raises:
            ValueError: If value is not a string or None.

        Examples:
            >>> status_info = ProductFootprintStatus(status=Status.ACTIVE)
            >>> status_info.comment = "New comment"
            >>> status_info.comment
            'New comment'
        """
        if value is not None and not isinstance(value, str):
            raise ValueError("comment must be a string or None")
        self._comment = value
