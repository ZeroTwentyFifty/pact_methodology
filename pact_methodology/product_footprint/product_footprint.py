from pact_methodology.carbon_footprint.carbon_footprint import CarbonFootprint
from pact_methodology.data_model_extension.data_model_extension import (
    DataModelExtension,
)
from pact_methodology.datetime import DateTime
from pact_methodology.product_footprint.id import ProductFootprintId
from pact_methodology.product_footprint.status import ProductFootprintStatus
from pact_methodology.product_footprint.cpc import CPC
from pact_methodology.product_footprint.version import Version
from pact_methodology.product_footprint.validity_period import ValidityPeriod
from pact_methodology.urn import CompanyId, ProductId
from pact_methodology.product_footprint.product_id_list import ProductIdList


class ProductFootprint:
    """
    Represents the carbon footprint of a product under a specific scope and with values calculated in accordance
    with the Pathfinder Framework.

    Attributes:
        id (ProductFootprintId): The unique identifier for this ProductFootprint.
        spec_version (str): The version of the ProductFootprint data specification.
        version (Version): The version of the ProductFootprint.
        created (DateTime): The date and time when the ProductFootprint was created.
        updated (DateTime | None): The date and time when the ProductFootprint was last updated.
        status (ProductFootprintStatus): The status of the ProductFootprint.
        status_comment (str | None): A comment describing the status of the ProductFootprint.
        validity_period (ValidityPeriod | None): The validity period for the ProductFootprint.
        company_name (str): The name of the company that owns the ProductFootprint.
        company_ids (list[CompanyId]): A list of CompanyIds for the company that owns the ProductFootprint.
        product_description (str): A description of the product.
        product_ids (list[ProductId]): A list of ProductIds for the product.
        product_category_cpc (CPC): The category of the product according to the CPC (Central Product Classification) system.
        product_name_company (str): The name of the product as used by the company.
        comment (str): A comment about the ProductFootprint.
        extensions (list[DataModelExtension] | None): A list of DataModelExtension objects.
        pcf (CarbonFootprint): The carbon footprint of the given product with value conforming to the data type CarbonFootprint.
        preceding_pf_ids (list[ProductFootprintId] | None): A list of preceding ProductFootprintIds.

    Examples:
        >>> pcf = CarbonFootprint(...)  # Assume CarbonFootprint is properly initialized
        >>> product_footprint = ProductFootprint(
        ...     version=Version(),
        ...     created=DateTime(),
        ...     status=ProductFootprintStatus(),
        ...     company_name="Example Company",
        ...     company_ids=[CompanyId()],
        ...     product_description="Example Product",
        ...     product_ids=[ProductId()],
        ...     product_category_cpc=CPC(),
        ...     product_name_company="Example Product Name",
        ...     comment="Example comment",
        ...     pcf=pcf
        ... )
        >>> print(product_footprint)
        ProductFootprint(id=<ProductFootprintId>, spec_version=2.2.0, version=<Version>, ...)
    """

    def __init__(
        self,
        *,
        id: ProductFootprintId | None = None,
        spec_version: str = "2.2.0",
        version: Version,
        created: DateTime,
        updated: DateTime | None = None,
        status_info: ProductFootprintStatus,
        validity_period: ValidityPeriod | None = None,
        company_name: str,
        company_ids: list[CompanyId],
        product_description: str,
        product_ids: ProductIdList,
        product_category_cpc: CPC,
        product_name_company: str,
        comment: str,
        extensions: list[DataModelExtension] | None = None,
        pcf: CarbonFootprint,
        preceding_pf_ids: list[ProductFootprintId] | None = None,
    ):
        """
        Initializes a new ProductFootprint instance.

        Args:
            id (ProductFootprintId | None): The ProductFootprintId for this instance. If not provided, a new one will be generated.
            spec_version (str): The version of the ProductFootprint data specification. Currently, hardcoded to "2.2.0", but may be updated in the future to support different versions.
            version (Version): The version of the ProductFootprint.
            created (DateTime): The date and time when the ProductFootprint was created.
            updated (DateTime | None): The date and time when the ProductFootprint was last updated.
            status (ProductFootprintStatus): The status of the ProductFootprint.
            status_comment (str | None): A comment describing the status of the ProductFootprint.
            validity_period (ValidityPeriod | None): The validity period for the ProductFootprint.
            company_name (str): The name of the company that owns the ProductFootprint.
            company_ids (list[CompanyId]): A list of CompanyIds for the company that owns the ProductFootprint.
            product_description (str): A description of the product.
            product_ids (list[ProductId]): A list of ProductIds for the product.
            product_category_cpc (CPC): The category of the product according to the CPC (Central Product Classification) system.
            product_name_company (str): The name of the product as used by the company.
            comment (str): A comment about the ProductFootprint.
            extensions (list[DataModelExtension] | None): A list of DataModelExtension objects.
            pcf (CarbonFootprint): The carbon footprint of the given product with value conforming to the data type CarbonFootprint.
            preceding_pf_ids (list[ProductFootprintId] | None): A list of preceding ProductFootprintIds.

        Examples:
            >>> pcf = CarbonFootprint(...)  # Assume CarbonFootprint is properly initialized
            >>> product_footprint = ProductFootprint(
            ...     version=Version(),
            ...     created=DateTime(),
            ...     status=ProductFootprintStatus(),
            ...     company_name="Example Company",
            ...     company_ids=[CompanyId()],
            ...     product_description="Example Product",
            ...     product_ids=[ProductId()],
            ...     product_category_cpc=CPC(),
            ...     product_name_company="Example Product Name",
            ...     comment="Example comment",
            ...     pcf=pcf
            ... )
            >>> print(product_footprint)
            ProductFootprint(id=<ProductFootprintId>, spec_version=2.2.0, version=<Version>, ...)
        """
        self.id = id if id else ProductFootprintId()
        self.spec_version = spec_version
        self.version = version
        self.created = created
        self.updated = updated
        self.status_info = status_info
        self.company_name = company_name
        self.company_ids = company_ids
        self.product_description = product_description
        self.product_ids = product_ids
        self.product_category_cpc = product_category_cpc
        self.product_name_company = product_name_company
        self.comment = comment
        self.extensions = extensions
        self.pcf = pcf
        self.preceding_pf_ids = preceding_pf_ids
        self.validity_period = validity_period if validity_period else ValidityPeriod(reference_period_end=self.pcf.reference_period.end)

    @property
    def id(self):
        """Gets the unique identifier for this ProductFootprint."""
        return self._id

    @id.setter
    def id(self, value):
        """Sets the unique identifier for this ProductFootprint.

        Args:
            value (ProductFootprintId | None): The identifier to set.

        Raises:
            ValueError: If value is not an instance of ProductFootprintId or None.
        """
        if not isinstance(value, (ProductFootprintId, type(None))):
            raise ValueError("id must be an instance of ProductFootprintId or None")
        self._id = value

    @property
    def spec_version(self):
        """Gets the version of the ProductFootprint data specification."""
        return self._spec_version

    @spec_version.setter
    def spec_version(self, value):
        """Sets the version of the ProductFootprint data specification.

        Args:
            value (str): The specification version to set.

        Raises:
            ValueError: If value is not "2.2.0".
        """
        if value != "2.2.0":
            raise ValueError("Invalid spec version")
        self._spec_version = value

    @property
    def version(self):
        """Gets the version of the ProductFootprint."""
        return self._version

    @version.setter
    def version(self, value):
        """Sets the version of the ProductFootprint.

        Args:
            value (Version): The version to set.

        Raises:
            ValueError: If value is not an instance of Version.
        """
        if not isinstance(value, Version):
            raise ValueError("version must be an instance of Version")
        self._version = value

    @property
    def created(self):
        """Gets the date and time when the ProductFootprint was created."""
        return self._created

    @created.setter
    def created(self, value):
        """Sets the date and time when the ProductFootprint was created.

        Args:
            value (DateTime): The creation date/time to set.

        Raises:
            ValueError: If value is not an instance of DateTime.
        """
        if not isinstance(value, DateTime):
            raise ValueError("created must be an instance of DateTime")
        self._created = value

    @property
    def updated(self):
        """Gets the date and time when the ProductFootprint was last updated."""
        return self._updated

    @updated.setter
    def updated(self, value):
        """Sets the date and time when the ProductFootprint was last updated.

        Args:
            value (DateTime | None): The update date/time to set.

        Raises:
            ValueError: If value is not an instance of DateTime or None.
        """
        if value is not None and not isinstance(value, DateTime):
            raise ValueError("updated must be an instance of DateTime or None")
        self._updated = value

    @property
    def status(self):
        """Gets the status of the ProductFootprint."""
        return self._status_info.status

    @status.setter
    def status(self, value):
        """Sets the status of the ProductFootprint.

        Args:
            value (Status): The status to set.

        Raises:
            ValueError: If value is not an instance of Status.
        """
        self._status_info.status = value

    @property
    def status_comment(self):
        """Gets the comment describing the status of the ProductFootprint."""
        return self._status_info.comment

    @status_comment.setter
    def status_comment(self, value):
        """Sets the comment describing the status of the ProductFootprint.

        Args:
            value (str | None): The status comment to set.

        Raises:
            ValueError: If value is not a string or None.
        """
        self._status_info.comment = value

    @property
    def status_info(self):
        """Gets the status information of the ProductFootprint."""
        return self._status_info

    @status_info.setter
    def status_info(self, value):
        """Sets the status information of the ProductFootprint.

        Args:
            value (ProductFootprintStatus): The status information to set.

        Raises:
            ValueError: If value is not an instance of ProductFootprintStatus.
        """
        if not isinstance(value, ProductFootprintStatus):
            raise ValueError("status_info must be an instance of ProductFootprintStatus")
        self._status_info = value

    @property
    def validity_period(self):
        """Gets the validity period for the ProductFootprint."""
        return self._validity_period

    @validity_period.setter
    def validity_period(self, value):
        """Sets the validity period for the ProductFootprint.

        Args:
            value (ValidityPeriod | None): The validity period to set.

        Raises:
            ValueError: If value is not an instance of ValidityPeriod or None.
        """
        if value is not None and not isinstance(value, ValidityPeriod):
            raise ValueError("validity_period must be an instance of ValidityPeriod or None")
        self._validity_period = value

    @property
    def company_name(self):
        """Gets the name of the company that owns the ProductFootprint."""
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        """Sets the name of the company that owns the ProductFootprint.

        Args:
            value (str): The company name to set.

        Raises:
            ValueError: If value is not a non-empty string.
        """
        if not isinstance(value, str) or not value:
            raise ValueError("company_name must be a non-empty string")
        self._company_name = value

    @property
    def company_ids(self):
        """Gets the list of CompanyIds for the company that owns the ProductFootprint."""
        return self._company_ids

    @company_ids.setter
    def company_ids(self, value):
        """Sets the list of CompanyIds for the company that owns the ProductFootprint.

        Args:
            value (list[CompanyId]): The list of company IDs to set.

        Raises:
            ValueError: If value is not a list of CompanyId instances.
        """
        if not isinstance(value, list) or not all(isinstance(company_id, CompanyId) for company_id in value):
            raise ValueError("company_ids must be a list of CompanyId")
        self._company_ids = value

    @property
    def product_description(self):
        """Gets the description of the product."""
        return self._product_description

    @product_description.setter
    def product_description(self, value):
        """Sets the description of the product.

        Args:
            value (str): The product description to set.

        Raises:
            ValueError: If value is not a non-empty string.
        """
        if not isinstance(value, str) or not value:
            raise ValueError("product_description must be a non-empty string")
        self._product_description = value

    @property
    def product_ids(self):
        """Gets the ProductIdList for the product."""
        return self._product_ids

    @product_ids.setter
    def product_ids(self, value):
        """Sets the ProductIdList for the product.

        Args:
            value (ProductIdList): The ProductIdList to set.

        Raises:
            ValueError: If value is not an instance of ProductIdList.
        """
        if not isinstance(value, ProductIdList):
            raise ValueError("product_ids must be an instance of ProductIdList")
        self._product_ids = value

    @property
    def product_category_cpc(self):
        """Gets the category of the product according to the CPC (Central Product Classification) system."""
        return self._product_category_cpc

    @product_category_cpc.setter
    def product_category_cpc(self, value):
        """Sets the category of the product according to the CPC system.

        Args:
            value (CPC): The CPC category to set.

        Raises:
            ValueError: If value is not an instance of CPC.
        """
        if not isinstance(value, CPC):
            raise ValueError("product_category_cpc must be an instance of CPC")
        self._product_category_cpc = value

    @property
    def product_name_company(self):
        """Gets the name of the product as used by the company."""
        return self._product_name_company

    @product_name_company.setter
    def product_name_company(self, value):
        """Sets the name of the product as used by the company.

        Args:
            value (str): The product name to set.

        Raises:
            ValueError: If value is not a non-empty string.
        """
        if not isinstance(value, str) or not value:
            raise ValueError("product_name_company must be a non-empty string")
        self._product_name_company = value

    @property
    def comment(self):
        """Gets the comment about the ProductFootprint."""
        return self._comment

    @comment.setter
    def comment(self, value):
        """Sets the comment about the ProductFootprint.

        Args:
            value (str): The comment to set.

        Raises:
            ValueError: If value is not a string.
        """
        if not isinstance(value, str):
            raise ValueError("comment must be a string")
        self._comment = value

    @property
    def extensions(self):
        """Gets the list of DataModelExtension objects."""
        return self._extensions

    @extensions.setter
    def extensions(self, value):
        """Sets the list of DataModelExtension objects.

        Args:
            value (list[DataModelExtension] | None): The list of extensions to set.

        Raises:
            ValueError: If value is not None and not a list of DataModelExtension instances.
        """
        if value is not None and (not isinstance(value, list) or not all(isinstance(ext, DataModelExtension) for ext in value)):
            raise ValueError("extensions must be a list of DataModelExtension objects or None")
        self._extensions = value

    @property
    def pcf(self):
        """Gets the carbon footprint of the given product with value conforming to the data type CarbonFootprint."""
        return self._pcf

    @pcf.setter
    def pcf(self, value):
        """Sets the carbon footprint of the given product.

        Args:
            value (CarbonFootprint): The carbon footprint to set.

        Raises:
            ValueError: If value is not an instance of CarbonFootprint.
        """
        if not isinstance(value, CarbonFootprint):
            raise ValueError("pcf must be an instance of CarbonFootprint")
        self._pcf = value

    @property
    def preceding_pf_ids(self):
        """Gets the list of preceding ProductFootprintIds."""
        return self._preceding_pf_ids

    @preceding_pf_ids.setter
    def preceding_pf_ids(self, value):
        """Sets the list of preceding ProductFootprintIds.

        Args:
            value (list[ProductFootprintId] | None): The list of preceding product footprint IDs to set.

        Raises:
            ValueError: If value is not None and not a list of unique ProductFootprintId instances.
        """
        if value is not None:
            if not isinstance(value, list) or not all(isinstance(pf_id, ProductFootprintId) for pf_id in value):
                raise ValueError("preceding_pf_ids must be a list of ProductFootprintId or None")
            if len(value) != len(set(value)):
                raise ValueError("preceding_pf_ids must not contain duplicates")
        self._preceding_pf_ids = value

    def __str__(self):
        """
        Returns a string representation of the ProductFootprint instance.

        Examples:
            >>> pcf = CarbonFootprint(...)  # Assume CarbonFootprint is properly initialized
            >>> product_footprint = ProductFootprint(
            ...     version=Version(),
            ...     created=DateTime(),
            ...     status=ProductFootprintStatus(),
            ...     company_name="Example Company",
            ...     company_ids=[CompanyId()],
            ...     product_description="Example Product",
            ...     product_ids=[ProductId()],
            ...     product_category_cpc=CPC(),
            ...     product_name_company="Example Product Name",
            ...     comment="Example comment",
            ...     pcf=pcf
            ... )
            >>> print(product_footprint)
            ProductFootprint(id=<ProductFootprintId>, spec_version=2.2.0, version=<Version>, ...)
        """
        return (
            f"ProductFootprint(id={self.id}, spec_version={self.spec_version}, version={self.version}, "
            f"created={self.created}, updated={self.updated}, status={self.status}, status_comment='{self.status_comment}', "
            f"validity_period={self.validity_period}, company_name='{self.company_name}', company_ids={self.company_ids}, "
            f"product_description='{self.product_description}', product_ids={self.product_ids}, "
            f"product_category_cpc={self.product_category_cpc}, product_name_company='{self.product_name_company}', "
            f"comment='{self.comment}', extensions={self.extensions}, pcf={self.pcf}, preceding_pf_ids={self.preceding_pf_ids})"
        )

    def __repr__(self):
        """
        Returns a detailed string representation of the ProductFootprint instance for debugging.

        Examples:
            >>> pcf = CarbonFootprint(
            >>> product_footprint = ProductFootprint(
            ...     version=Version(),
            ...     created=DateTime(),
            ...     status=ProductFootprintStatus(),
            ...     company_name="Example Company",
            ...     company_ids=[CompanyId()],
            ...     product_description="Example Product",
            ...     product_ids=[ProductId()],
            ...     product_category_cpc=CPC(),
            ...     product_name_company="Example Product Name",
            ...     comment="Example comment",
            ...     pcf=pcf
            ... )
            >>> repr(product_footprint)
            ProductFootprint(id=<ProductFootprintId>, spec_version='2.2.0', version=<Version>, ...)
        """
        return (
            f"ProductFootprint(id={self.id!r}, spec_version={self.spec_version!r}, version={self.version!r}, "
            f"created={self.created!r}, updated={self.updated!r}, status={self.status!r}, status_comment={self.status_comment!r}, "
            f"validity_period={self.validity_period!r}, company_name={self.company_name!r}, company_ids={self.company_ids!r}, "
            f"product_description={self.product_description!r}, product_ids={self.product_ids!r}, "
            f"product_category_cpc={self.product_category_cpc!r}, product_name_company={self.product_name_company!r}, "
            f"comment={self.comment!r}, extensions={self.extensions!r}, pcf={self.pcf!r}, preceding_pf_ids={self.preceding_pf_ids!r})"
        )

    def __eq__(self, other):
        """
        Compares two ProductFootprint instances for equality.

        Examples:
            >>> pcf = CarbonFootprint(...)  # Assume CarbonFootprint is properly initialized
            >>> product_footprint1 = ProductFootprint(
            ...     version=Version(),
            ...     created=DateTime(),
            ...     status=ProductFootprintStatus(),
            ...     company_name="Example Company",
            ...     company_ids=[CompanyId()],
            ...     product_description="Example Product",
            ...     product_ids=[ProductId()],
            ...     product_category_cpc=CPC(),
            ...     product_name_company="Example Product Name",
            ...     comment="Example comment",
            ...     pcf=pcf
            ... )
            >>> product_footprint2 = ProductFootprint(
            ...     version=Version(),
            ...     created=DateTime(),
            ...     status=ProductFootprintStatus(),
            ...     company_name="Example Company",
            ...     company_ids=[CompanyId()],
            ...     product_description="Example Product",
            ...     product_ids=[ProductId()],
            ...     product_category_cpc=CPC(),
            ...     product_name_company="Example Product Name",
            ...     comment="Example comment",
            ...     pcf=pcf
            ... )
            >>> product_footprint1 == product_footprint2
            True
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Compares two ProductFootprint instances for inequality.

        Examples:
            >>> pcf = CarbonFootprint(...)  # Assume CarbonFootprint is properly initialized
            >>> product_footprint1 = ProductFootprint(
            ...     version=Version(),
            ...     created=DateTime(),
            ...     status=ProductFootprintStatus(),
            ...     company_name="Example Company",
            ...     company_ids=[CompanyId()],
            ...     product_description="Example Product",
            ...     product_ids=[ProductId()],
            ...     product_category_cpc=CPC(),
            ...     product_name_company="Example Product Name",
            ...     comment="Example comment",
            ...     pcf=pcf
            ... )
            >>> product_footprint2 = ProductFootprint(
            ...     version=Version(),
            ...     created=DateTime(),
            ...     status=ProductFootprintStatus(),
            ...     company_name="Different Company",
            ...     company_ids=[CompanyId()],
            ...     product_description="Example Product",
            ...     product_ids=[ProductId()],
            ...     product_category_cpc=CPC(),
            ...     product_name_company="Example Product Name",
            ...     comment="Example comment",
            ...     pcf=pcf
            ... )
            >>> product_footprint1 != product_footprint2
            True
        """
        return not self.__eq__(other)