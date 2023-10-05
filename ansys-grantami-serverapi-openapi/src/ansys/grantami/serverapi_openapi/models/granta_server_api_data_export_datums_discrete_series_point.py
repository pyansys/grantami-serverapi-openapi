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

class GrantaServerApiDataExportDatumsDiscreteSeriesPoint(ModelBase):
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
        "x": "float",
        "x_name": "str",
        "y": "GrantaServerApiDiscreteValue",
    }

    attribute_map = {
        "x": "x",
        "x_name": "xName",
        "y": "y",
    }

    subtype_mapping = {
        "y": "GrantaServerApiDiscreteValue",
    }

    def __init__(self, *, x: "Optional[float]" = None, x_name: "Optional[str]" = None, y: "Optional[GrantaServerApiDiscreteValue]" = None) -> None:
        """GrantaServerApiDataExportDatumsDiscreteSeriesPoint - a model defined in Swagger

        Parameters
        ----------
            x: float, optional
            x_name: str, optional
            y: GrantaServerApiDiscreteValue, optional
        """
        self._x = None
        self._x_name = None
        self._y = None
        self.discriminator = None
        if x is not None:
            self.x = x
        if x_name is not None:
            self.x_name = x_name
        if y is not None:
            self.y = y

    @property
    def x(self) -> "float":
        """Gets the x of this GrantaServerApiDataExportDatumsDiscreteSeriesPoint.

        Returns
        -------
        float
            The x of this GrantaServerApiDataExportDatumsDiscreteSeriesPoint.
        """
        return self._x

    @x.setter
    def x(self, x: "float") -> None:
        """Sets the x of this GrantaServerApiDataExportDatumsDiscreteSeriesPoint.

        Parameters
        ----------
        x: float
            The x of this GrantaServerApiDataExportDatumsDiscreteSeriesPoint.
        """
        self._x = x

    @property
    def x_name(self) -> "str":
        """Gets the x_name of this GrantaServerApiDataExportDatumsDiscreteSeriesPoint.

        Returns
        -------
        str
            The x_name of this GrantaServerApiDataExportDatumsDiscreteSeriesPoint.
        """
        return self._x_name

    @x_name.setter
    def x_name(self, x_name: "str") -> None:
        """Sets the x_name of this GrantaServerApiDataExportDatumsDiscreteSeriesPoint.

        Parameters
        ----------
        x_name: str
            The x_name of this GrantaServerApiDataExportDatumsDiscreteSeriesPoint.
        """
        self._x_name = x_name

    @property
    def y(self) -> "GrantaServerApiDiscreteValue":
        """Gets the y of this GrantaServerApiDataExportDatumsDiscreteSeriesPoint.

        Returns
        -------
        GrantaServerApiDiscreteValue
            The y of this GrantaServerApiDataExportDatumsDiscreteSeriesPoint.
        """
        return self._y

    @y.setter
    def y(self, y: "GrantaServerApiDiscreteValue") -> None:
        """Sets the y of this GrantaServerApiDataExportDatumsDiscreteSeriesPoint.

        Parameters
        ----------
        y: GrantaServerApiDiscreteValue
            The y of this GrantaServerApiDataExportDatumsDiscreteSeriesPoint.
        """
        self._y = y

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
        if issubclass(GrantaServerApiDataExportDatumsDiscreteSeriesPoint, dict):
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
        if not isinstance(other, GrantaServerApiDataExportDatumsDiscreteSeriesPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
