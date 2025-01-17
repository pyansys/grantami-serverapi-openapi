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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from ansys.grantami.serverapi_openapi.v252.models.gsa_functional_type import GsaFunctionalType
from ansys.grantami.serverapi_openapi.v252.models.gsa_graph_type import GsaGraphType
from ansys.grantami.serverapi_openapi.v252.models.gsa_grid_graph import GsaGridGraph  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaFloatGridGraph(GsaGridGraph):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes
    ----------
    swagger_types: dict[str, str]
        The key is attribute name and the value is attribute type.
    attribute_map: dict[str, str]
        The key is attribute name and the value is json key in definition.
    subtype_mapping: dict[str, str]
        The key is the unmangled property name and the value is the corresponding type.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "all_parameters": "list[GsaSlimParameter]",
        "default_x_axis_parameter": "GsaSlimParameter",
        "functional_type": "GsaFunctionalType",
        "graph_type": "GsaGraphType",
        "points": "list[GsaFloatGridPoint]",
    }

    attribute_map: dict[str, str] = {
        "all_parameters": "allParameters",
        "default_x_axis_parameter": "defaultXAxisParameter",
        "functional_type": "functionalType",
        "graph_type": "graphType",
        "points": "points",
    }

    subtype_mapping: dict[str, str] = {
        "points": "GsaFloatGridPoint",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        all_parameters: "list[GsaSlimParameter]",
        default_x_axis_parameter: "GsaSlimParameter",
        functional_type: "GsaFunctionalType" = GsaFunctionalType.FLOAT,
        graph_type: "GsaGraphType" = GsaGraphType.GRID,
        points: "list[GsaFloatGridPoint]",
    ) -> None:
        """GsaFloatGridGraph - a model defined in Swagger

        Parameters
        ----------
        all_parameters: list[GsaSlimParameter]
        default_x_axis_parameter: GsaSlimParameter
        functional_type: GsaFunctionalType
        graph_type: GsaGraphType
        points: list[GsaFloatGridPoint]
        """
        super().__init__(
            all_parameters=all_parameters,
            default_x_axis_parameter=default_x_axis_parameter,
            functional_type=functional_type,
            graph_type=graph_type,
        )
        self._points: list[GsaFloatGridPoint]

        self.points = points

    @property
    def points(self) -> "list[GsaFloatGridPoint]":
        """Gets the points of this GsaFloatGridGraph.

        Returns
        -------
        list[GsaFloatGridPoint]
            The points of this GsaFloatGridGraph.
        """
        return self._points

    @points.setter
    def points(self, points: "list[GsaFloatGridPoint]") -> None:
        """Sets the points of this GsaFloatGridGraph.

        Parameters
        ----------
        points: list[GsaFloatGridPoint]
            The points of this GsaFloatGridGraph.
        """
        # Field is not nullable
        if points is None:
            raise ValueError("Invalid value for 'points', must not be 'None'")
        # Field is required
        if points is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'points', must not be 'Unset'")
        self._points = points

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
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
        if not isinstance(other, GsaFloatGridGraph):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
