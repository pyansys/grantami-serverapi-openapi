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

class GrantaServerApiSchemaConstantsCreateConstant(ModelBase):
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
        "unit_guid": "str",
        "value": "float",
        "name": "str",
        "guid": "str",
    }

    attribute_map = {
        "unit_guid": "unitGuid",
        "value": "value",
        "name": "name",
        "guid": "guid",
    }

    subtype_mapping = {
    }

    def __init__(self, *, guid: "Optional[str]" = None, name: "Optional[str]" = None, unit_guid: "Optional[str]" = None, value: "Optional[float]" = None) -> None:
        """GrantaServerApiSchemaConstantsCreateConstant - a model defined in Swagger

        Parameters
        ----------
            guid: str, optional
            name: str, optional
            unit_guid: str, optional
            value: float, optional
        """
        self._unit_guid = None
        self._value = None
        self._name = None
        self._guid = None
        self.discriminator = None
        if unit_guid is not None:
            self.unit_guid = unit_guid
        if value is not None:
            self.value = value
        if name is not None:
            self.name = name
        if guid is not None:
            self.guid = guid

    @property
    def unit_guid(self) -> "str":
        """Gets the unit_guid of this GrantaServerApiSchemaConstantsCreateConstant.

        Returns
        -------
        str
            The unit_guid of this GrantaServerApiSchemaConstantsCreateConstant.
        """
        return self._unit_guid

    @unit_guid.setter
    def unit_guid(self, unit_guid: "str") -> None:
        """Sets the unit_guid of this GrantaServerApiSchemaConstantsCreateConstant.

        Parameters
        ----------
        unit_guid: str
            The unit_guid of this GrantaServerApiSchemaConstantsCreateConstant.
        """
        self._unit_guid = unit_guid

    @property
    def value(self) -> "float":
        """Gets the value of this GrantaServerApiSchemaConstantsCreateConstant.

        Returns
        -------
        float
            The value of this GrantaServerApiSchemaConstantsCreateConstant.
        """
        return self._value

    @value.setter
    def value(self, value: "float") -> None:
        """Sets the value of this GrantaServerApiSchemaConstantsCreateConstant.

        Parameters
        ----------
        value: float
            The value of this GrantaServerApiSchemaConstantsCreateConstant.
        """
        self._value = value

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaConstantsCreateConstant.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaConstantsCreateConstant.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaConstantsCreateConstant.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaConstantsCreateConstant.
        """
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaConstantsCreateConstant.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaConstantsCreateConstant.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaConstantsCreateConstant.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaConstantsCreateConstant.
        """
        self._guid = guid

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
        if issubclass(GrantaServerApiSchemaConstantsCreateConstant, dict):
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
        if not isinstance(other, GrantaServerApiSchemaConstantsCreateConstant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
