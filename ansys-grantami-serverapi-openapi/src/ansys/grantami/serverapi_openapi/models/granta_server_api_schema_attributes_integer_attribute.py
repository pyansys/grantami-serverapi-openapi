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

from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_attributes_attribute import GrantaServerApiSchemaAttributesAttribute  # noqa: F401

if TYPE_CHECKING:
    from . import *

class GrantaServerApiSchemaAttributesIntegerAttribute(GrantaServerApiSchemaAttributesAttribute):
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
        "type": "str",
        "is_unique": "bool",
    }

    attribute_map = {
        "type": "type",
        "is_unique": "isUnique",
    }

    subtype_mapping = {
    }

    def __init__(self, *, about_attribute: "Optional[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]" = None, axis_name: "Optional[str]" = None, default_threshold_type: "Optional[GrantaServerApiSchemaAttributesAttributeThresholdType]" = None, display_names: "Optional[Dict[str, str]]" = None, guid: "Optional[str]" = None, help_path: "Optional[str]" = None, info: "Optional[GrantaServerApiSchemaAttributesAttributeAttributeInfo]" = None, is_unique: "Optional[bool]" = None, name: "Optional[str]" = None, type: "str" = 'integer') -> None:
        """GrantaServerApiSchemaAttributesIntegerAttribute - a model defined in Swagger

        Parameters
        ----------
            about_attribute: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, optional
            axis_name: str, optional
            default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType, optional
            display_names: Dict[str, str], optional
            guid: str, optional
            help_path: str, optional
            info: GrantaServerApiSchemaAttributesAttributeAttributeInfo, optional
            is_unique: bool, optional
            name: str, optional
            type: str
        """
        super().__init__(about_attribute=about_attribute, axis_name=axis_name, default_threshold_type=default_threshold_type, display_names=display_names, guid=guid, help_path=help_path, info=info, name=name)
        self._type = None
        self._is_unique = None
        self.discriminator = None
        self.type = type
        if is_unique is not None:
            self.is_unique = is_unique

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaAttributesIntegerAttribute.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaAttributesIntegerAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaAttributesIntegerAttribute.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaAttributesIntegerAttribute.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @property
    def is_unique(self) -> "bool":
        """Gets the is_unique of this GrantaServerApiSchemaAttributesIntegerAttribute.

        Returns
        -------
        bool
            The is_unique of this GrantaServerApiSchemaAttributesIntegerAttribute.
        """
        return self._is_unique

    @is_unique.setter
    def is_unique(self, is_unique: "bool") -> None:
        """Sets the is_unique of this GrantaServerApiSchemaAttributesIntegerAttribute.

        Parameters
        ----------
        is_unique: bool
            The is_unique of this GrantaServerApiSchemaAttributesIntegerAttribute.
        """
        self._is_unique = is_unique

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
        if issubclass(GrantaServerApiSchemaAttributesIntegerAttribute, dict):
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
        if not isinstance(other, GrantaServerApiSchemaAttributesIntegerAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
