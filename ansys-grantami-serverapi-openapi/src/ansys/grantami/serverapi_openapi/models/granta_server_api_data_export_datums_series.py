# Copyright (C) 2023 - 2024 ANSYS, Inc. and/or its affiliates.
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


class GrantaServerApiDataExportDatumsSeries(ModelBase):
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
        "graph_decoration": "GrantaServerApiDataExportDatumsGraphDecoration",
        "parameter_values": "list[GrantaServerApiDataExportDatumsParameterValue]",
        "points": "list[GrantaServerApiDataExportDatumsSeriesPoint]",
    }

    attribute_map: Dict[str, str] = {
        "graph_decoration": "graphDecoration",
        "parameter_values": "parameterValues",
        "points": "points",
    }

    subtype_mapping: Dict[str, str] = {
        "parameterValues": "GrantaServerApiDataExportDatumsParameterValue",
        "points": "GrantaServerApiDataExportDatumsSeriesPoint",
        "graphDecoration": "GrantaServerApiDataExportDatumsGraphDecoration",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        graph_decoration: "Union[GrantaServerApiDataExportDatumsGraphDecoration, Unset_Type]" = Unset,
        parameter_values: "Union[List[GrantaServerApiDataExportDatumsParameterValue], None, Unset_Type]" = Unset,
        points: "Union[List[GrantaServerApiDataExportDatumsSeriesPoint], None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiDataExportDatumsSeries - a model defined in Swagger

        Parameters
        ----------
        graph_decoration: GrantaServerApiDataExportDatumsGraphDecoration, optional
        parameter_values: List[GrantaServerApiDataExportDatumsParameterValue], optional
        points: List[GrantaServerApiDataExportDatumsSeriesPoint], optional
        """
        self._parameter_values: Union[
            List[GrantaServerApiDataExportDatumsParameterValue], None, Unset_Type
        ] = Unset
        self._points: Union[
            List[GrantaServerApiDataExportDatumsSeriesPoint], None, Unset_Type
        ] = Unset
        self._graph_decoration: Union[
            GrantaServerApiDataExportDatumsGraphDecoration, Unset_Type
        ] = Unset

        if parameter_values is not Unset:
            self.parameter_values = parameter_values
        if points is not Unset:
            self.points = points
        if graph_decoration is not Unset:
            self.graph_decoration = graph_decoration

    @property
    def parameter_values(
        self,
    ) -> "Union[List[GrantaServerApiDataExportDatumsParameterValue], None, Unset_Type]":
        """Gets the parameter_values of this GrantaServerApiDataExportDatumsSeries.

        Returns
        -------
        Union[List[GrantaServerApiDataExportDatumsParameterValue], None, Unset_Type]
            The parameter_values of this GrantaServerApiDataExportDatumsSeries.
        """
        return self._parameter_values

    @parameter_values.setter
    def parameter_values(
        self,
        parameter_values: "Union[List[GrantaServerApiDataExportDatumsParameterValue], None, Unset_Type]",
    ) -> None:
        """Sets the parameter_values of this GrantaServerApiDataExportDatumsSeries.

        Parameters
        ----------
        parameter_values: Union[List[GrantaServerApiDataExportDatumsParameterValue], None, Unset_Type]
            The parameter_values of this GrantaServerApiDataExportDatumsSeries.
        """
        self._parameter_values = parameter_values

    @property
    def points(
        self,
    ) -> "Union[List[GrantaServerApiDataExportDatumsSeriesPoint], None, Unset_Type]":
        """Gets the points of this GrantaServerApiDataExportDatumsSeries.

        Returns
        -------
        Union[List[GrantaServerApiDataExportDatumsSeriesPoint], None, Unset_Type]
            The points of this GrantaServerApiDataExportDatumsSeries.
        """
        return self._points

    @points.setter
    def points(
        self,
        points: "Union[List[GrantaServerApiDataExportDatumsSeriesPoint], None, Unset_Type]",
    ) -> None:
        """Sets the points of this GrantaServerApiDataExportDatumsSeries.

        Parameters
        ----------
        points: Union[List[GrantaServerApiDataExportDatumsSeriesPoint], None, Unset_Type]
            The points of this GrantaServerApiDataExportDatumsSeries.
        """
        self._points = points

    @property
    def graph_decoration(
        self,
    ) -> "Union[GrantaServerApiDataExportDatumsGraphDecoration, Unset_Type]":
        """Gets the graph_decoration of this GrantaServerApiDataExportDatumsSeries.

        Returns
        -------
        Union[GrantaServerApiDataExportDatumsGraphDecoration, Unset_Type]
            The graph_decoration of this GrantaServerApiDataExportDatumsSeries.
        """
        return self._graph_decoration

    @graph_decoration.setter
    def graph_decoration(
        self,
        graph_decoration: "Union[GrantaServerApiDataExportDatumsGraphDecoration, Unset_Type]",
    ) -> None:
        """Sets the graph_decoration of this GrantaServerApiDataExportDatumsSeries.

        Parameters
        ----------
        graph_decoration: Union[GrantaServerApiDataExportDatumsGraphDecoration, Unset_Type]
            The graph_decoration of this GrantaServerApiDataExportDatumsSeries.
        """
        # Field is not nullable
        if graph_decoration is None:
            raise ValueError("Invalid value for 'graph_decoration', must not be 'None'")
        self._graph_decoration = graph_decoration

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
        if not isinstance(other, GrantaServerApiDataExportDatumsSeries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
