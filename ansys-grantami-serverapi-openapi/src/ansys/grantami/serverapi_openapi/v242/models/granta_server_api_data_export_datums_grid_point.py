# Copyright (C) 2023 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiDataExportDatumsGridPoint(ModelBase):
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
        "high": "float",
        "low": "float",
        "parameter_values": "list[GrantaServerApiDataExportDatumsParameterValue]",
    }

    attribute_map: Dict[str, str] = {
        "high": "high",
        "low": "low",
        "parameter_values": "parameterValues",
    }

    subtype_mapping: Dict[str, str] = {
        "parameterValues": "GrantaServerApiDataExportDatumsParameterValue",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        high: "Union[float, Unset_Type]" = Unset,
        low: "Union[float, Unset_Type]" = Unset,
        parameter_values: "Union[List[GrantaServerApiDataExportDatumsParameterValue], None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiDataExportDatumsGridPoint - a model defined in Swagger

        Parameters
        ----------
        high: float, optional
        low: float, optional
        parameter_values: List[GrantaServerApiDataExportDatumsParameterValue], optional
        """
        self._parameter_values: Union[
            List[GrantaServerApiDataExportDatumsParameterValue], None, Unset_Type
        ] = Unset
        self._low: Union[float, Unset_Type] = Unset
        self._high: Union[float, Unset_Type] = Unset

        if parameter_values is not Unset:
            self.parameter_values = parameter_values
        if low is not Unset:
            self.low = low
        if high is not Unset:
            self.high = high

    @property
    def parameter_values(
        self,
    ) -> "Union[List[GrantaServerApiDataExportDatumsParameterValue], None, Unset_Type]":
        """Gets the parameter_values of this GrantaServerApiDataExportDatumsGridPoint.

        Returns
        -------
        Union[List[GrantaServerApiDataExportDatumsParameterValue], None, Unset_Type]
            The parameter_values of this GrantaServerApiDataExportDatumsGridPoint.
        """
        return self._parameter_values

    @parameter_values.setter
    def parameter_values(
        self,
        parameter_values: "Union[List[GrantaServerApiDataExportDatumsParameterValue], None, Unset_Type]",
    ) -> None:
        """Sets the parameter_values of this GrantaServerApiDataExportDatumsGridPoint.

        Parameters
        ----------
        parameter_values: Union[List[GrantaServerApiDataExportDatumsParameterValue], None, Unset_Type]
            The parameter_values of this GrantaServerApiDataExportDatumsGridPoint.
        """
        self._parameter_values = parameter_values

    @property
    def low(self) -> "Union[float, Unset_Type]":
        """Gets the low of this GrantaServerApiDataExportDatumsGridPoint.

        Returns
        -------
        Union[float, Unset_Type]
            The low of this GrantaServerApiDataExportDatumsGridPoint.
        """
        return self._low

    @low.setter
    def low(self, low: "Union[float, Unset_Type]") -> None:
        """Sets the low of this GrantaServerApiDataExportDatumsGridPoint.

        Parameters
        ----------
        low: Union[float, Unset_Type]
            The low of this GrantaServerApiDataExportDatumsGridPoint.
        """
        # Field is not nullable
        if low is None:
            raise ValueError("Invalid value for 'low', must not be 'None'")
        self._low = low

    @property
    def high(self) -> "Union[float, Unset_Type]":
        """Gets the high of this GrantaServerApiDataExportDatumsGridPoint.

        Returns
        -------
        Union[float, Unset_Type]
            The high of this GrantaServerApiDataExportDatumsGridPoint.
        """
        return self._high

    @high.setter
    def high(self, high: "Union[float, Unset_Type]") -> None:
        """Sets the high of this GrantaServerApiDataExportDatumsGridPoint.

        Parameters
        ----------
        high: Union[float, Unset_Type]
            The high of this GrantaServerApiDataExportDatumsGridPoint.
        """
        # Field is not nullable
        if high is None:
            raise ValueError("Invalid value for 'high', must not be 'None'")
        self._high = high

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
        if not isinstance(other, GrantaServerApiDataExportDatumsGridPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
