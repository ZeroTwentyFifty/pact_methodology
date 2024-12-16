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
    """

    def __init__(
        self,
        *,
        id: ProductFootprintId | None = None,
        spec_version: str = "2.2.0",
        version: Version,
        created: DateTime,
        updated: DateTime | None = None,
        status: ProductFootprintStatus,
        status_comment: str | None = None,
        validity_period: ValidityPeriod | None = None,
        company_name: str,
        company_ids: list[CompanyId],
        product_description: str,
        product_ids: list[ProductId],
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
        """
        self.id = id if id else ProductFootprintId()
        self.spec_version = spec_version
        self.version = version
        self.created = created
        self.updated = updated
        self.status = status
        self.status_comment = status_comment
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
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, (ProductFootprintId, type(None))):
            raise ValueError("id must be an instance of ProductFootprintId or None")
        self._id = value

    @property
    def spec_version(self):
        return self._spec_version

    @spec_version.setter
    def spec_version(self, value):
        if value != "2.2.0":
            raise ValueError("Invalid spec version")
        self._spec_version = value

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        if not isinstance(value, Version):
            raise ValueError("version must be an instance of Version")
        self._version = value

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, value):
        if not isinstance(value, DateTime):
            raise ValueError("created must be an instance of DateTime")
        self._created = value

    @property
    def updated(self):
        return self._updated

    @updated.setter
    def updated(self, value):
        if value is not None and not isinstance(value, DateTime):
            raise ValueError("updated must be an instance of DateTime or None")
        self._updated = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if not isinstance(value, ProductFootprintStatus):
            raise ValueError("status must be an instance of ProductFootprintStatus")
        self._status = value

    @property
    def status_comment(self):
        return self._status_comment

    @status_comment.setter
    def status_comment(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("status_comment must be a string or None")
        self._status_comment = value

    @property
    def validity_period(self):
        return self._validity_period

    @validity_period.setter
    def validity_period(self, value):
        if value is not None and not isinstance(value, ValidityPeriod):
            raise ValueError("validity_period must be an instance of ValidityPeriod or None")
        self._validity_period = value

    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("company_name must be a non-empty string")
        self._company_name = value

    @property
    def company_ids(self):
        return self._company_ids

    @company_ids.setter
    def company_ids(self, value):
        if not isinstance(value, list) or not all(isinstance(company_id, CompanyId) for company_id in value):
            raise ValueError("company_ids must be a list of CompanyId")
        self._company_ids = value

    @property
    def product_description(self):
        return self._product_description

    @product_description.setter
    def product_description(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("product_description must be a non-empty string")
        self._product_description = value

    @property
    def product_ids(self):
        return self._product_ids

    @product_ids.setter
    def product_ids(self, value):
        if not isinstance(value, list) or not all(isinstance(product_id, ProductId) for product_id in value):
            raise ValueError("product_ids must be a list of ProductId")
        self._product_ids = value

    @property
    def product_category_cpc(self):
        return self._product_category_cpc

    @product_category_cpc.setter
    def product_category_cpc(self, value):
        if not isinstance(value, CPC):
            raise ValueError("product_category_cpc must be an instance of CPC")
        self._product_category_cpc = value

    @property
    def product_name_company(self):
        return self._product_name_company

    @product_name_company.setter
    def product_name_company(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("product_name_company must be a non-empty string")
        self._product_name_company = value

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        if not isinstance(value, str):
            raise ValueError("comment must be a string")
        self._comment = value

    @property
    def extensions(self):
        return self._extensions

    @extensions.setter
    def extensions(self, value):
        if value is not None and (not isinstance(value, list) or not all(isinstance(ext, DataModelExtension) for ext in value)):
            raise ValueError("extensions must be a list of DataModelExtension objects or None")
        self._extensions = value

    @property
    def pcf(self):
        return self._pcf

    @pcf.setter
    def pcf(self, value):
        if not isinstance(value, CarbonFootprint):
            raise ValueError("pcf must be an instance of CarbonFootprint")
        self._pcf = value

    @property
    def preceding_pf_ids(self):
        return self._preceding_pf_ids

    @preceding_pf_ids.setter
    def preceding_pf_ids(self, value):
        if value is not None:
            if not isinstance(value, list) or not all(isinstance(pf_id, ProductFootprintId) for pf_id in value):
                raise ValueError("preceding_pf_ids must be a list of ProductFootprintId or None")
            if len(value) != len(set(value)):
                raise ValueError("preceding_pf_ids must not contain duplicates")
        self._preceding_pf_ids = value

    def __str__(self):
        return (
            f"ProductFootprint(id={self.id}, spec_version={self.spec_version}, version={self.version}, "
            f"created={self.created}, updated={self.updated}, status={self.status}, status_comment='{self.status_comment}', "
            f"validity_period={self.validity_period}, company_name='{self.company_name}', company_ids={self.company_ids}, "
            f"product_description='{self.product_description}', product_ids={self.product_ids}, "
            f"product_category_cpc={self.product_category_cpc}, product_name_company='{self.product_name_company}', "
            f"comment='{self.comment}', extensions={self.extensions}, pcf={self.pcf}, preceding_pf_ids={self.preceding_pf_ids})"
        )

    def __repr__(self):
        return (
            f"ProductFootprint(id={self.id!r}, spec_version={self.spec_version!r}, version={self.version!r}, "
            f"created={self.created!r}, updated={self.updated!r}, status={self.status!r}, status_comment={self.status_comment!r}, "
            f"validity_period={self.validity_period!r}, company_name={self.company_name!r}, company_ids={self.company_ids!r}, "
            f"product_description={self.product_description!r}, product_ids={self.product_ids!r}, "
            f"product_category_cpc={self.product_category_cpc!r}, product_name_company={self.product_name_company!r}, "
            f"comment={self.comment!r}, extensions={self.extensions!r}, pcf={self.pcf!r}, preceding_pf_ids={self.preceding_pf_ids!r})"
        )

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)