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

class GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter(ModelBase):
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
        "default_value": "float",
        "parameter": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
    }

    attribute_map = {
        "default_value": "defaultValue",
        "parameter": "parameter",
    }

    subtype_mapping = {
        "parameter": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
    }

    def __init__(self, *, default_value: "Optional[float]" = None, parameter: "Optional[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]" = None,) -> None:
        """GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter - a model defined in Swagger

        Parameters
        ----------
            default_value: float, optional
            parameter: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, optional
        """
        self._parameter = None
        self._default_value = None
        self.discriminator = None
        if parameter is not None:
            self.parameter = parameter
        if default_value is not None:
            self.default_value = default_value

    @property
    def parameter(self) -> "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity":
        """Gets the parameter of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
            The parameter of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter.
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter: "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity") -> None:
        """Sets the parameter of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter.

        Parameters
        ----------
        parameter: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
            The parameter of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter.
        """
        self._parameter = parameter

    @property
    def default_value(self) -> "float":
        """Gets the default_value of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter.

        Returns
        -------
        float
            The default_value of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter.
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value: "float") -> None:
        """Sets the default_value of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter.

        Parameters
        ----------
        default_value: float
            The default_value of this GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter.
        """
        self._default_value = default_value

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
        if issubclass(GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter, dict):
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
        if not isinstance(other, GrantaServerApiSchemaAttributesDiscreteFunctionalAttributeParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
