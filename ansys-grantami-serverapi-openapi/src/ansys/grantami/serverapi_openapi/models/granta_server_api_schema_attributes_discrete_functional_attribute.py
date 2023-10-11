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

class GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute(GrantaServerApiSchemaAttributesAttribute):
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
        "attribute_parameters": "list[GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter]",
        "axis_name": "str",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "discrete_type": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "display_names": "dict(str, str)",
        "guid": "str",
        "help_path": "str",
        "info": "GrantaServerApiSchemaAttributesAttributeAttributeInfo",
        "name": "str",
        "type": "str",
    }

    attribute_map = {
        "about_attribute": "aboutAttribute",
        "attribute_parameters": "attributeParameters",
        "axis_name": "axisName",
        "default_threshold_type": "defaultThresholdType",
        "discrete_type": "discreteType",
        "display_names": "displayNames",
        "guid": "guid",
        "help_path": "helpPath",
        "info": "info",
        "name": "name",
        "type": "type",
    }

    subtype_mapping = {
        "discreteType": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "attributeParameters": "GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter",
    }

    def __init__(self, *, about_attribute: "Optional[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]" = None, attribute_parameters: "Optional[List[GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter]]" = None, axis_name: "Optional[str]" = None, default_threshold_type: "Optional[GrantaServerApiSchemaAttributesAttributeThresholdType]" = None, discrete_type: "Optional[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]" = None, display_names: "Optional[Dict[str, str]]" = None, guid: "Optional[str]" = None, help_path: "Optional[str]" = None, info: "Optional[GrantaServerApiSchemaAttributesAttributeAttributeInfo]" = None, name: "Optional[str]" = None, type: "str" = 'discreteFunctional',) -> None:
        """GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute - a model defined in Swagger

        Parameters
        ----------
            about_attribute: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, optional
            attribute_parameters: List[GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter], optional
            axis_name: str, optional
            default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType, optional
            discrete_type: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, optional
            display_names: Dict[str, str], optional
            guid: str, optional
            help_path: str, optional
            info: GrantaServerApiSchemaAttributesAttributeAttributeInfo, optional
            name: str, optional
            type: str
        """
        super().__init__(about_attribute=about_attribute, axis_name=axis_name, default_threshold_type=default_threshold_type, display_names=display_names, guid=guid, help_path=help_path, info=info, name=name)
        self._type = None
        self._discrete_type = None
        self._attribute_parameters = None
        self.discriminator = None
        self.type = type
        if discrete_type is not None:
            self.discrete_type = discrete_type
        if attribute_parameters is not None:
            self.attribute_parameters = attribute_parameters

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @property
    def discrete_type(self) -> "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity":
        """Gets the discrete_type of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
            The discrete_type of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.
        """
        return self._discrete_type

    @discrete_type.setter
    def discrete_type(self, discrete_type: "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity") -> None:
        """Sets the discrete_type of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.

        Parameters
        ----------
        discrete_type: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
            The discrete_type of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.
        """
        self._discrete_type = discrete_type

    @property
    def attribute_parameters(self) -> "list[GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter]":
        """Gets the attribute_parameters of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.

        Returns
        -------
        list[GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter]
            The attribute_parameters of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.
        """
        return self._attribute_parameters

    @attribute_parameters.setter
    def attribute_parameters(self, attribute_parameters: "list[GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter]") -> None:
        """Sets the attribute_parameters of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.

        Parameters
        ----------
        attribute_parameters: list[GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter]
            The attribute_parameters of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute.
        """
        self._attribute_parameters = attribute_parameters

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
        if issubclass(GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute, dict):
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
        if not isinstance(other, GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
