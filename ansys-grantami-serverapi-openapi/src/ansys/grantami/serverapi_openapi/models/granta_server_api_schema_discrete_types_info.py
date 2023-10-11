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

class GrantaServerApiSchemaDiscreteTypesInfo(ModelBase):
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
        "discrete_types": "list[GrantaServerApiSchemaDiscreteType]",
    }

    attribute_map = {
        "discrete_types": "discreteTypes",
    }

    subtype_mapping = {
        "discreteTypes": "GrantaServerApiSchemaDiscreteType",
    }

    def __init__(self, *, discrete_types: "Optional[List[GrantaServerApiSchemaDiscreteType]]" = None,) -> None:
        """GrantaServerApiSchemaDiscreteTypesInfo - a model defined in Swagger

        Parameters
        ----------
            discrete_types: List[GrantaServerApiSchemaDiscreteType], optional
        """
        self._discrete_types = None
        self.discriminator = None
        if discrete_types is not None:
            self.discrete_types = discrete_types

    @property
    def discrete_types(self) -> "list[GrantaServerApiSchemaDiscreteType]":
        """Gets the discrete_types of this GrantaServerApiSchemaDiscreteTypesInfo.

        Returns
        -------
        list[GrantaServerApiSchemaDiscreteType]
            The discrete_types of this GrantaServerApiSchemaDiscreteTypesInfo.
        """
        return self._discrete_types

    @discrete_types.setter
    def discrete_types(self, discrete_types: "list[GrantaServerApiSchemaDiscreteType]") -> None:
        """Sets the discrete_types of this GrantaServerApiSchemaDiscreteTypesInfo.

        Parameters
        ----------
        discrete_types: list[GrantaServerApiSchemaDiscreteType]
            The discrete_types of this GrantaServerApiSchemaDiscreteTypesInfo.
        """
        self._discrete_types = discrete_types

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
        if issubclass(GrantaServerApiSchemaDiscreteTypesInfo, dict):
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
        if not isinstance(other, GrantaServerApiSchemaDiscreteTypesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
