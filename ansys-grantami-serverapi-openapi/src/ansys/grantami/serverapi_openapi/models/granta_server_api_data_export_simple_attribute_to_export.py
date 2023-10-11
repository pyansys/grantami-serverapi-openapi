"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase

from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_attribute_to_export import GrantaServerApiDataExportAttributeToExport  # noqa: F401

if TYPE_CHECKING:
    from . import *

class GrantaServerApiDataExportSimpleAttributeToExport(GrantaServerApiDataExportAttributeToExport):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes
    ----------
    swagger_types: Dict[str, str]
        The key is attribute name and the value is attribute type.
    attribute_map: Dict[str, str]
        The key is attribute name and the value is json key in definition.
    subtype_mapping: Dict[str, str]
        The key is the unmangled property name and the value is the corresponding type.

    """
    swagger_types = {
        "attribute_type": "str",
        "guid": "str",
        "identity": "int",
    }

    attribute_map = {
        "attribute_type": "attributeType",
        "guid": "guid",
        "identity": "identity",
    }

    subtype_mapping = {
    }

    def __init__(self, *, attribute_type: "str" = 'simple', guid: "Optional[str]" = None, identity: "Optional[int]" = None,) -> None:
        """GrantaServerApiDataExportSimpleAttributeToExport - a model defined in Swagger

        Parameters
        ----------
            attribute_type: str
            guid: str, optional
            identity: int, optional
        """
        super().__init__(guid=guid, identity=identity)
        self._attribute_type = None
        self.discriminator = None
        self.attribute_type = attribute_type

    @property
    def attribute_type(self) -> "str":
        """Gets the attribute_type of this GrantaServerApiDataExportSimpleAttributeToExport.

        Returns
        -------
        str
            The attribute_type of this GrantaServerApiDataExportSimpleAttributeToExport.
        """
        return self._attribute_type

    @attribute_type.setter
    def attribute_type(self, attribute_type: "str") -> None:
        """Sets the attribute_type of this GrantaServerApiDataExportSimpleAttributeToExport.

        Parameters
        ----------
        attribute_type: str
            The attribute_type of this GrantaServerApiDataExportSimpleAttributeToExport.
        """
        if attribute_type is None:
            raise ValueError("Invalid value for 'attribute_type', must not be 'None'")
        self._attribute_type = attribute_type

    def get_real_child_model(self, data: ModelBase) -> str:
        """Raises a NotImplementedError for a type without a discriminator defined.

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class

        Raises
        ------
        NotImplementedError
            This class has no discriminator, and hence no subclasses
        """
        raise NotImplementedError()

    def to_dict(self) -> Dict:
        """Returns the model properties as a dict

        Returns
        -------
        Dict
            Dictionary indexed by property name containing all the model properties
        """
        result = {}

        for attr in self.swagger_types.keys():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GrantaServerApiDataExportSimpleAttributeToExport, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model

        Returns
        -------
        str
            String representation of the model as a dictionary
        """
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiDataExportSimpleAttributeToExport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
