"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.models.gsa_series_graph import GsaSeriesGraph  # noqa: F401
from ansys.grantami.serverapi_openapi.models.gsa_functional_type import GsaFunctionalType
from ansys.grantami.serverapi_openapi.models.gsa_graph_type import GsaGraphType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaFloatSeriesGraph(GsaSeriesGraph):
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
        "constraint_parameters": "list[GsaSlimParameter]",
        "functional_type": "GsaFunctionalType",
        "graph_type": "GsaGraphType",
        "number_of_points": "int",
        "series": "list[GsaFloatSeries]",
        "x_axis_parameter": "GsaSlimParameter",
    }

    attribute_map: dict[str, str] = {
        "constraint_parameters": "constraintParameters",
        "functional_type": "functionalType",
        "graph_type": "graphType",
        "number_of_points": "numberOfPoints",
        "series": "series",
        "x_axis_parameter": "xAxisParameter",
    }

    subtype_mapping: dict[str, str] = {
        "series": "GsaFloatSeries",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, constraint_parameters: "list[GsaSlimParameter]", functional_type: "GsaFunctionalType" = GsaFunctionalType.FLOAT, graph_type: "GsaGraphType" = GsaGraphType.SERIES, number_of_points: "int", series: "list[GsaFloatSeries]", x_axis_parameter: "GsaSlimParameter",) -> None:
        """GsaFloatSeriesGraph - a model defined in Swagger

        Parameters
        ----------
        constraint_parameters: list[GsaSlimParameter]
        functional_type: GsaFunctionalType
        graph_type: GsaGraphType
        number_of_points: int
        series: list[GsaFloatSeries]
        x_axis_parameter: GsaSlimParameter
        """
        super().__init__(constraint_parameters=constraint_parameters, functional_type=functional_type, graph_type=graph_type, number_of_points=number_of_points, x_axis_parameter=x_axis_parameter)
        self._series: list[GsaFloatSeries]

        self.series = series

    @property
    def series(self) -> "list[GsaFloatSeries]":
        """Gets the series of this GsaFloatSeriesGraph.

        Returns
        -------
        list[GsaFloatSeries]
            The series of this GsaFloatSeriesGraph.
        """
        return self._series

    @series.setter
    def series(self, series: "list[GsaFloatSeries]") -> None:
        """Sets the series of this GsaFloatSeriesGraph.

        Parameters
        ----------
        series: list[GsaFloatSeries]
            The series of this GsaFloatSeriesGraph.
        """
        # Field is not nullable
        if series is None:
            raise ValueError("Invalid value for 'series', must not be 'None'")
        # Field is required
        if series is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'series', must not be 'Unset'")
        self._series = series

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
        if not isinstance(other, GsaFloatSeriesGraph):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

