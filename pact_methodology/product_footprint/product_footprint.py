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
        updated (DateTime): The date and time when the ProductFootprint was last updated.
        status (ProductFootprintStatus): The status of the ProductFootprint.
        status_comment (str): A comment describing the status of the ProductFootprint.
        validity_period (ValidityPeriod): The validity period for the ProductFootprint.
        company_name (str): The name of the company that owns the ProductFootprint.
        company_ids (list[CompanyId]): A list of CompanyIds for the company that owns the ProductFootprint.
        product_description (str): A description of the product.
        product_ids (list[ProductId]): A list of ProductIds for the product.
        product_category_cpc (str): The category of the product according to the CPC (Central Product Classification) system.
        product_name_company (str): The name of the product as used by the company.
        comment (str): A comment about the ProductFootprint.
        extensions (list[DataModelExtension]): A list of DataModelExtension objects.
        pcf (CarbonFootprint): The carbon footprint of the given product with value conforming to the data type CarbonFootprint.
        preceding_pf_ids (list[ProductFootprintId]): A list of preceding ProductFootprintIds.
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
            spec_version (str): The version of the ProductFootprint data specification. Currently, hardcoded to "2.0.0", but may be updated in the future to support different versions.
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
            product_category_cpc (str): The category of the product according to the CPC (Central Product Classification) system.
            product_name_company (str): The name of the product as used by the company.
            comment (str): A comment about the ProductFootprint.
            extensions (list[DataModelExtension] | None): A list of DataModelExtension objects.
            pcf (CarbonFootprint): The carbon footprint of the given product with value conforming to the data type CarbonFootprint.
            preceding_pf_ids (list[ProductFootprintId] | None): A list of preceding ProductFootprintIds.
        """

        if not isinstance(pcf, CarbonFootprint):
            raise ValueError("pcf must be an instance of CarbonFootprint")
        if not isinstance(id, (ProductFootprintId, type(None))):
            raise ValueError("id must be an instance of ProductFootprintId or None")
        if spec_version != "2.2.0":
            raise ValueError("Invalid spec version")
        if not isinstance(version, Version):
            raise ValueError("version must be an instance of Version")
        if not isinstance(created, DateTime):
            raise ValueError("created must be an instance of DateTime")
        if updated is not None:
            if not isinstance(updated, DateTime):
                raise ValueError("updated must be an instance of DateTime")
        if not isinstance(status, ProductFootprintStatus):
            raise ValueError("status must be an instance of ProductFootprintStatus")
        if status_comment is not None and not isinstance(status_comment, str):
            raise ValueError("status_comment must be a string")
        if validity_period is not None:
            if not isinstance(validity_period, ValidityPeriod):
                raise ValueError("validity_period must be an instance of ValidityPeriod")
        if not isinstance(company_name, str) or not company_name:
            raise ValueError("company_name must be a non-empty string")
        if not isinstance(company_ids, list) or not all(
            isinstance(company_id, CompanyId) for company_id in company_ids
        ):
            raise ValueError("company_ids must be a list of CompanyId")
        if not isinstance(product_ids, list) or not all(
            isinstance(product_id, ProductId) for product_id in product_ids
        ):
            raise ValueError("product_ids must be a list of ProductId")
        if not isinstance(product_description, str) or not product_description:
            raise ValueError("product_description must be a non-empty string")
        if not isinstance(product_category_cpc, CPC):
            raise ValueError("product_category_cpc must be an instance of CPC")
        if not isinstance(product_name_company, str) or not product_name_company:
            raise ValueError("product_name_company must be a non-empty string")
        if not isinstance(comment, str):
            raise ValueError("comment must be a string")
        if extensions is not None:
            if not isinstance(extensions, list) or not all(
                isinstance(ext, DataModelExtension) for ext in extensions
            ):
                raise ValueError("extensions must be a list of DataModelExtension objects")
        if not isinstance(pcf, CarbonFootprint):
            raise ValueError("pcf must be an instance of CarbonFootprint")

        if preceding_pf_ids is not None:
            if not isinstance(preceding_pf_ids, list) or not all(
                isinstance(pf_id, ProductFootprintId) for pf_id in preceding_pf_ids
            ):
                raise ValueError("preceding_pf_ids must be a list of ProductFootprintId")
            if len(preceding_pf_ids) != len(set(preceding_pf_ids)):
                raise ValueError("preceding_pf_ids must not contain duplicates")

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

    def __repr__(self) -> str:
        """Returns a string representation of the ProductFootprint instance."""
        return f"ProductFootprint(id={self.id})"
