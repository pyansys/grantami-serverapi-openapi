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

from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_attributes_attribute import (
    GrantaServerApiSchemaAttributesAttribute,
)  # noqa: F401

if TYPE_CHECKING:
    from . import *


class GrantaServerApiSchemaAttributesLongTextAttribute(
    GrantaServerApiSchemaAttributesAttribute
):
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

    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types = {
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "display_names": "dict(str, str)",
        "guid": "str",
        "info": "GrantaServerApiSchemaAttributesAttributeAttributeInfo",
        "name": "str",
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "axis_name": "str",
        "help_path": "str",
        "type": "str",
    }

    attribute_map = {
        "default_threshold_type": "defaultThresholdType",
        "display_names": "displayNames",
        "guid": "guid",
        "info": "info",
        "name": "name",
        "about_attribute": "aboutAttribute",
        "axis_name": "axisName",
        "help_path": "helpPath",
        "type": "type",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        default_threshold_type: "GrantaServerApiSchemaAttributesAttributeThresholdType",
        display_names: "Dict[str, str]",
        guid: "str",
        info: "GrantaServerApiSchemaAttributesAttributeAttributeInfo",
        name: "str",
        about_attribute: "Optional[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]" = None,
        axis_name: "Optional[str]" = None,
        help_path: "Optional[str]" = None,
        type: "str" = "longText",
    ) -> None:
        """GrantaServerApiSchemaAttributesLongTextAttribute - a model defined in Swagger

        Parameters
        ----------
            default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType
            display_names: Dict[str, str]
            guid: str
            info: GrantaServerApiSchemaAttributesAttributeAttributeInfo
            name: str
            about_attribute: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, optional
            axis_name: str, optional
            help_path: str, optional
            type: str
        """
        super().__init__(
            default_threshold_type=default_threshold_type,
            display_names=display_names,
            guid=guid,
            info=info,
            name=name,
            about_attribute=about_attribute,
            axis_name=axis_name,
            help_path=help_path,
        )
        self._type = None

        self.type = type

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaAttributesLongTextAttribute.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaAttributesLongTextAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaAttributesLongTextAttribute.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaAttributesLongTextAttribute.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @classmethod
    def get_real_child_model(cls, data: ModelBase) -> str:
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
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(GrantaServerApiSchemaAttributesLongTextAttribute, dict):
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
        if not isinstance(other, GrantaServerApiSchemaAttributesLongTextAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
