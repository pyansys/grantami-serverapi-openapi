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

class GrantaServerApiDataExportDatumsParameterValue(ModelBase):
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
        "parameter": "GrantaServerApiParameterInfo",
        "value": "float",
        "value_name": "str",
    }

    attribute_map = {
        "parameter": "parameter",
        "value": "value",
        "value_name": "valueName",
    }

    subtype_mapping = {
        "parameter": "GrantaServerApiParameterInfo",
    }

    def __init__(self, *, parameter: "Optional[GrantaServerApiParameterInfo]" = None, value: "Optional[float]" = None, value_name: "Optional[str]" = None,) -> None:
        """GrantaServerApiDataExportDatumsParameterValue - a model defined in Swagger

        Parameters
        ----------
            parameter: GrantaServerApiParameterInfo, optional
            value: float, optional
            value_name: str, optional
        """
        self._parameter = None
        self._value_name = None
        self._value = None
        self.discriminator = None
        if parameter is not None:
            self.parameter = parameter
        if value_name is not None:
            self.value_name = value_name
        if value is not None:
            self.value = value

    @property
    def parameter(self) -> "GrantaServerApiParameterInfo":
        """Gets the parameter of this GrantaServerApiDataExportDatumsParameterValue.

        Returns
        -------
        GrantaServerApiParameterInfo
            The parameter of this GrantaServerApiDataExportDatumsParameterValue.
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter: "GrantaServerApiParameterInfo") -> None:
        """Sets the parameter of this GrantaServerApiDataExportDatumsParameterValue.

        Parameters
        ----------
        parameter: GrantaServerApiParameterInfo
            The parameter of this GrantaServerApiDataExportDatumsParameterValue.
        """
        self._parameter = parameter

    @property
    def value_name(self) -> "str":
        """Gets the value_name of this GrantaServerApiDataExportDatumsParameterValue.

        Returns
        -------
        str
            The value_name of this GrantaServerApiDataExportDatumsParameterValue.
        """
        return self._value_name

    @value_name.setter
    def value_name(self, value_name: "str") -> None:
        """Sets the value_name of this GrantaServerApiDataExportDatumsParameterValue.

        Parameters
        ----------
        value_name: str
            The value_name of this GrantaServerApiDataExportDatumsParameterValue.
        """
        self._value_name = value_name

    @property
    def value(self) -> "float":
        """Gets the value of this GrantaServerApiDataExportDatumsParameterValue.

        Returns
        -------
        float
            The value of this GrantaServerApiDataExportDatumsParameterValue.
        """
        return self._value

    @value.setter
    def value(self, value: "float") -> None:
        """Sets the value of this GrantaServerApiDataExportDatumsParameterValue.

        Parameters
        ----------
        value: float
            The value of this GrantaServerApiDataExportDatumsParameterValue.
        """
        self._value = value

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
        if issubclass(GrantaServerApiDataExportDatumsParameterValue, dict):
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
        if not isinstance(other, GrantaServerApiDataExportDatumsParameterValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
