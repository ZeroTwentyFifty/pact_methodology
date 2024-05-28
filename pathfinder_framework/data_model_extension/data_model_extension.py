from packaging.version import Version, InvalidVersion
from urllib.parse import urlparse
import json


class DataModelExtension:
    """
    Data Model Extension class.

    Attributes:
        spec_version (str): The version of the Data Model Extension specification.
            Must be a string in the format major.minor.patch as defined in Semantic Versioning 2.0.0.
            Must be 2.0.0 when referencing this specification.
        data_schema (str): The URL to the publicly accessible Extension Schema File.
            Must be a string representing a URL with the HTTPS schema.
        data (dict): A JSON Object that conforms to the extension schema file referenced by the dataSchema property.
        documentation (str): The URL to the publicly accessible Extension Documentation.
            Must be a string representing a URL with the HTTPS schema.

    """
    def __init__(self, spec_version: str, data_schema: str, data: dict, documentation: str = None):
        """
        Initializes a DataModelExtension object.

        Args:
            spec_version (str): The version of the Data Model Extension specification.
            data_schema (str): The URL to the publicly accessible Extension Schema File.
            data (dict): A JSON Object that conforms to the extension schema file referenced by the dataSchema property.
            documentation (str, optional): The URL to the publicly accessible Extension Documentation.

        Raises:
            ValueError: If the spec_version is not in the format major.minor.patch or is not 2.0.0.
            ValueError: If the data_schema is not a string representing a URL with the HTTPS schema.
            ValueError: If the data is not a dictionary or cannot be serialized to a JSON object.
            ValueError: If the documentation is not a string representing a URL with the HTTPS schema.

        """
        try:
            semvar_version = Version(spec_version)
            if semvar_version.major != 2 or semvar_version.minor != 0 or semvar_version.micro != 0:
                raise ValueError("Invalid spec version")
        except InvalidVersion:
            raise ValueError("Invalid spec version")

        parsed_url = urlparse(data_schema)
        if parsed_url.scheme != "https":
            raise ValueError("Invalid data schema URL scheme")
        if not parsed_url.netloc:
            raise ValueError("Invalid data schema URL")

        if not isinstance(data, dict):
            raise ValueError("Invalid data type")
        try:
            json.dumps(data)
        except TypeError:
            raise ValueError("Invalid data format")

        if documentation is not None:
            parsed_url = urlparse(documentation)
            if parsed_url.scheme != "https":
                raise ValueError("Invalid documentation URL scheme")
            if not parsed_url.netloc:
                raise ValueError("Invalid documentation URL")

        self.spec_version = spec_version
        self.data_schema = data_schema
        self.data = data
        self.documentation = documentation
