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

class GrantaServerApiDataExportDatumsRange(ModelBase):
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
        "high_value": "float",
        "low_value": "float",
        "high_value_is_inclusive": "bool",
        "low_value_is_inclusive": "bool",
    }

    attribute_map = {
        "high_value": "highValue",
        "low_value": "lowValue",
        "high_value_is_inclusive": "highValueIsInclusive",
        "low_value_is_inclusive": "lowValueIsInclusive",
    }

    subtype_mapping = {
    }

    def __init__(self, *, high_value: "Optional[float]" = None, high_value_is_inclusive: "Optional[bool]" = None, low_value: "Optional[float]" = None, low_value_is_inclusive: "Optional[bool]" = None) -> None:
        """GrantaServerApiDataExportDatumsRange - a model defined in Swagger

        Parameters
        ----------
            high_value: float, optional
            high_value_is_inclusive: bool, optional
            low_value: float, optional
            low_value_is_inclusive: bool, optional
        """
        self._high_value = None
        self._low_value = None
        self._high_value_is_inclusive = None
        self._low_value_is_inclusive = None
        self.discriminator = None
        if high_value is not None:
            self.high_value = high_value
        if low_value is not None:
            self.low_value = low_value
        if high_value_is_inclusive is not None:
            self.high_value_is_inclusive = high_value_is_inclusive
        if low_value_is_inclusive is not None:
            self.low_value_is_inclusive = low_value_is_inclusive

    @property
    def high_value(self) -> "float":
        """Gets the high_value of this GrantaServerApiDataExportDatumsRange.

        Returns
        -------
        float
            The high_value of this GrantaServerApiDataExportDatumsRange.
        """
        return self._high_value

    @high_value.setter
    def high_value(self, high_value: "float") -> None:
        """Sets the high_value of this GrantaServerApiDataExportDatumsRange.

        Parameters
        ----------
        high_value: float
            The high_value of this GrantaServerApiDataExportDatumsRange.
        """
        self._high_value = high_value

    @property
    def low_value(self) -> "float":
        """Gets the low_value of this GrantaServerApiDataExportDatumsRange.

        Returns
        -------
        float
            The low_value of this GrantaServerApiDataExportDatumsRange.
        """
        return self._low_value

    @low_value.setter
    def low_value(self, low_value: "float") -> None:
        """Sets the low_value of this GrantaServerApiDataExportDatumsRange.

        Parameters
        ----------
        low_value: float
            The low_value of this GrantaServerApiDataExportDatumsRange.
        """
        self._low_value = low_value

    @property
    def high_value_is_inclusive(self) -> "bool":
        """Gets the high_value_is_inclusive of this GrantaServerApiDataExportDatumsRange.

        Returns
        -------
        bool
            The high_value_is_inclusive of this GrantaServerApiDataExportDatumsRange.
        """
        return self._high_value_is_inclusive

    @high_value_is_inclusive.setter
    def high_value_is_inclusive(self, high_value_is_inclusive: "bool") -> None:
        """Sets the high_value_is_inclusive of this GrantaServerApiDataExportDatumsRange.

        Parameters
        ----------
        high_value_is_inclusive: bool
            The high_value_is_inclusive of this GrantaServerApiDataExportDatumsRange.
        """
        self._high_value_is_inclusive = high_value_is_inclusive

    @property
    def low_value_is_inclusive(self) -> "bool":
        """Gets the low_value_is_inclusive of this GrantaServerApiDataExportDatumsRange.

        Returns
        -------
        bool
            The low_value_is_inclusive of this GrantaServerApiDataExportDatumsRange.
        """
        return self._low_value_is_inclusive

    @low_value_is_inclusive.setter
    def low_value_is_inclusive(self, low_value_is_inclusive: "bool") -> None:
        """Sets the low_value_is_inclusive of this GrantaServerApiDataExportDatumsRange.

        Parameters
        ----------
        low_value_is_inclusive: bool
            The low_value_is_inclusive of this GrantaServerApiDataExportDatumsRange.
        """
        self._low_value_is_inclusive = low_value_is_inclusive

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
        if issubclass(GrantaServerApiDataExportDatumsRange, dict):
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
        if not isinstance(other, GrantaServerApiDataExportDatumsRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
