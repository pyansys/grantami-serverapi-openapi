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

class GrantaServerApiSchemaAttributesShortTextAttribute(GrantaServerApiSchemaAttributesAttribute):
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
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "axis_name": "str",
        "data_rule": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "display_names": "dict(str, str)",
        "guid": "str",
        "help_path": "str",
        "info": "GrantaServerApiSchemaAttributesAttributeAttributeInfo",
        "is_unique": "bool",
        "name": "str",
        "type": "str",
    }

    attribute_map = {
        "about_attribute": "aboutAttribute",
        "axis_name": "axisName",
        "data_rule": "dataRule",
        "default_threshold_type": "defaultThresholdType",
        "display_names": "displayNames",
        "guid": "guid",
        "help_path": "helpPath",
        "info": "info",
        "is_unique": "isUnique",
        "name": "name",
        "type": "type",
    }

    subtype_mapping = {
        "dataRule": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
    }

    def __init__(self, *, about_attribute: "Optional[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]" = None, axis_name: "Optional[str]" = None, data_rule: "Optional[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]" = None, default_threshold_type: "Optional[GrantaServerApiSchemaAttributesAttributeThresholdType]" = None, display_names: "Optional[Dict[str, str]]" = None, guid: "Optional[str]" = None, help_path: "Optional[str]" = None, info: "Optional[GrantaServerApiSchemaAttributesAttributeAttributeInfo]" = None, is_unique: "Optional[bool]" = None, name: "Optional[str]" = None, type: "str" = 'shortText',) -> None:
        """GrantaServerApiSchemaAttributesShortTextAttribute - a model defined in Swagger

        Parameters
        ----------
            about_attribute: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, optional
            axis_name: str, optional
            data_rule: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, optional
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
        self._data_rule = None
        self.discriminator = None
        self.type = type
        if is_unique is not None:
            self.is_unique = is_unique
        if data_rule is not None:
            self.data_rule = data_rule

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaAttributesShortTextAttribute.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaAttributesShortTextAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaAttributesShortTextAttribute.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaAttributesShortTextAttribute.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @property
    def is_unique(self) -> "bool":
        """Gets the is_unique of this GrantaServerApiSchemaAttributesShortTextAttribute.

        Returns
        -------
        bool
            The is_unique of this GrantaServerApiSchemaAttributesShortTextAttribute.
        """
        return self._is_unique

    @is_unique.setter
    def is_unique(self, is_unique: "bool") -> None:
        """Sets the is_unique of this GrantaServerApiSchemaAttributesShortTextAttribute.

        Parameters
        ----------
        is_unique: bool
            The is_unique of this GrantaServerApiSchemaAttributesShortTextAttribute.
        """
        self._is_unique = is_unique

    @property
    def data_rule(self) -> "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity":
        """Gets the data_rule of this GrantaServerApiSchemaAttributesShortTextAttribute.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
            The data_rule of this GrantaServerApiSchemaAttributesShortTextAttribute.
        """
        return self._data_rule

    @data_rule.setter
    def data_rule(self, data_rule: "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity") -> None:
        """Sets the data_rule of this GrantaServerApiSchemaAttributesShortTextAttribute.

        Parameters
        ----------
        data_rule: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
            The data_rule of this GrantaServerApiSchemaAttributesShortTextAttribute.
        """
        self._data_rule = data_rule

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
        if issubclass(GrantaServerApiSchemaAttributesShortTextAttribute, dict):
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
        if not isinstance(other, GrantaServerApiSchemaAttributesShortTextAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
