"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import (
    TYPE_CHECKING,
    Any,
    BinaryIO,
    Dict,
    List,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase, Unset, Unset_Type


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiDataExportDatumsSeriesPoint(ModelBase):
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
    swagger_types: Dict[str, str] = {
        "x": "float",
        "x_name": "str",
        "y_high": "float",
        "y_low": "float",
    }

    attribute_map: Dict[str, str] = {
        "x": "x",
        "x_name": "xName",
        "y_high": "yHigh",
        "y_low": "yLow",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        x: "Union[float, Unset_Type]" = Unset,
        x_name: "Union[str, None, Unset_Type]" = Unset,
        y_high: "Union[float, Unset_Type]" = Unset,
        y_low: "Union[float, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiDataExportDatumsSeriesPoint - a model defined in Swagger

        Parameters
        ----------
        x: float, optional
        x_name: str, optional
        y_high: float, optional
        y_low: float, optional
        """
        self._x: Union[float, Unset_Type] = Unset
        self._x_name: Union[str, None, Unset_Type] = Unset
        self._y_low: Union[float, Unset_Type] = Unset
        self._y_high: Union[float, Unset_Type] = Unset

        if x is not Unset:
            self.x = x
        if x_name is not Unset:
            self.x_name = x_name
        if y_low is not Unset:
            self.y_low = y_low
        if y_high is not Unset:
            self.y_high = y_high

    @property
    def x(self) -> "Union[float, Unset_Type]":
        """Gets the x of this GrantaServerApiDataExportDatumsSeriesPoint.

        Returns
        -------
        Union[float, Unset_Type]
            The x of this GrantaServerApiDataExportDatumsSeriesPoint.
        """
        return self._x

    @x.setter
    def x(self, x: "Union[float, Unset_Type]") -> None:
        """Sets the x of this GrantaServerApiDataExportDatumsSeriesPoint.

        Parameters
        ----------
        x: Union[float, Unset_Type]
            The x of this GrantaServerApiDataExportDatumsSeriesPoint.
        """
        # Field is not nullable
        if x is None:
            raise ValueError("Invalid value for 'x', must not be 'None'")
        self._x = x

    @property
    def x_name(self) -> "Union[str, None, Unset_Type]":
        """Gets the x_name of this GrantaServerApiDataExportDatumsSeriesPoint.

        Returns
        -------
        Union[str, None, Unset_Type]
            The x_name of this GrantaServerApiDataExportDatumsSeriesPoint.
        """
        return self._x_name

    @x_name.setter
    def x_name(self, x_name: "Union[str, None, Unset_Type]") -> None:
        """Sets the x_name of this GrantaServerApiDataExportDatumsSeriesPoint.

        Parameters
        ----------
        x_name: Union[str, None, Unset_Type]
            The x_name of this GrantaServerApiDataExportDatumsSeriesPoint.
        """
        self._x_name = x_name

    @property
    def y_low(self) -> "Union[float, Unset_Type]":
        """Gets the y_low of this GrantaServerApiDataExportDatumsSeriesPoint.

        Returns
        -------
        Union[float, Unset_Type]
            The y_low of this GrantaServerApiDataExportDatumsSeriesPoint.
        """
        return self._y_low

    @y_low.setter
    def y_low(self, y_low: "Union[float, Unset_Type]") -> None:
        """Sets the y_low of this GrantaServerApiDataExportDatumsSeriesPoint.

        Parameters
        ----------
        y_low: Union[float, Unset_Type]
            The y_low of this GrantaServerApiDataExportDatumsSeriesPoint.
        """
        # Field is not nullable
        if y_low is None:
            raise ValueError("Invalid value for 'y_low', must not be 'None'")
        self._y_low = y_low

    @property
    def y_high(self) -> "Union[float, Unset_Type]":
        """Gets the y_high of this GrantaServerApiDataExportDatumsSeriesPoint.

        Returns
        -------
        Union[float, Unset_Type]
            The y_high of this GrantaServerApiDataExportDatumsSeriesPoint.
        """
        return self._y_high

    @y_high.setter
    def y_high(self, y_high: "Union[float, Unset_Type]") -> None:
        """Sets the y_high of this GrantaServerApiDataExportDatumsSeriesPoint.

        Parameters
        ----------
        y_high: Union[float, Unset_Type]
            The y_high of this GrantaServerApiDataExportDatumsSeriesPoint.
        """
        # Field is not nullable
        if y_high is None:
            raise ValueError("Invalid value for 'y_high', must not be 'None'")
        self._y_high = y_high

    @classmethod
    def get_real_child_model(cls, data: Dict[str, str]) -> str:
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

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiDataExportDatumsSeriesPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
