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


if TYPE_CHECKING:
    from . import *

class GrantaServerApiDataExportAttributeToExport(ModelBase):
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
    discriminator_class_map: Dict[str, str]
        They key is discriminator value and the value is associated subtype.
    """
    swagger_types = {
        "identity": "int",
        "guid": "str",
    }

    attribute_map = {
        "identity": "identity",
        "guid": "guid",
    }

    subtype_mapping = {
    }

    discriminator_value_class_map = {
        "link".lower(): "#/components/schemas/GrantaServerApiDataExportLinkAttributeToExport",
        "simple".lower(): "#/components/schemas/GrantaServerApiDataExportSimpleAttributeToExport",
    }

    def __init__(self, *, guid: "Optional[str]" = None, identity: "Optional[int]" = None) -> None:
        """GrantaServerApiDataExportAttributeToExport - a model defined in Swagger

        Parameters
        ----------
            guid: str, optional
            identity: int, optional
        """
        self._identity = None
        self._guid = None
        self.discriminator = "attributeType"
        if identity is not None:
            self.identity = identity
        if guid is not None:
            self.guid = guid

    @property
    def identity(self) -> "int":
        """Gets the identity of this GrantaServerApiDataExportAttributeToExport.

        Returns
        -------
        int
            The identity of this GrantaServerApiDataExportAttributeToExport.
        """
        return self._identity

    @identity.setter
    def identity(self, identity: "int") -> None:
        """Sets the identity of this GrantaServerApiDataExportAttributeToExport.

        Parameters
        ----------
        identity: int
            The identity of this GrantaServerApiDataExportAttributeToExport.
        """
        self._identity = identity

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiDataExportAttributeToExport.

        Returns
        -------
        str
            The guid of this GrantaServerApiDataExportAttributeToExport.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiDataExportAttributeToExport.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiDataExportAttributeToExport.
        """
        self._guid = guid

    def get_real_child_model(self, data: ModelBase) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[self._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen, 
        # so we have to extract it from the JSON reference
        return self.discriminator_value_class_map.get(discriminator_value).rsplit("/", 1)[-1]

    def _get_discriminator_field_name(self) -> str:
        name_tokens = self.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

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
        if issubclass(GrantaServerApiDataExportAttributeToExport, dict):
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
        if not isinstance(other, GrantaServerApiDataExportAttributeToExport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
