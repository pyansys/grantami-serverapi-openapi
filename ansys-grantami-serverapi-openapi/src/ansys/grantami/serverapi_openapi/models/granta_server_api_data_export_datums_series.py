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
    Dict,
    List,
    BinaryIO,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiDataExportDatumsSeries(ModelBase):  # type: ignore[misc]
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
        graph_decoration: "Optional[GrantaServerApiDataExportDatumsGraphDecoration]" = None,
        parameter_values: "Optional[List[GrantaServerApiDataExportDatumsParameterValue]]" = None,
        points: "Optional[List[GrantaServerApiDataExportDatumsSeriesPoint]]" = None,
    ) -> None:
        """GrantaServerApiDataExportDatumsSeries - a model defined in Swagger

        Parameters
        ----------
            graph_decoration: GrantaServerApiDataExportDatumsGraphDecoration, optional
            parameter_values: List[GrantaServerApiDataExportDatumsParameterValue], optional
            points: List[GrantaServerApiDataExportDatumsSeriesPoint], optional
        """
        self._parameter_values = None
        self._points = None
        self._graph_decoration = None

        if parameter_values is not None:
            self.parameter_values = parameter_values
        if points is not None:
            self.points = points
        if graph_decoration is not None:
            self.graph_decoration = graph_decoration

    @property
    def parameter_values(
        self,
    ) -> "Optional[List[GrantaServerApiDataExportDatumsParameterValue]]":
        """Gets the parameter_values of this GrantaServerApiDataExportDatumsSeries.

        Returns
        -------
        list[GrantaServerApiDataExportDatumsParameterValue]
            The parameter_values of this GrantaServerApiDataExportDatumsSeries.
        """
        return self._parameter_values

    @parameter_values.setter
    def parameter_values(
        self,
        parameter_values: "Optional[List[GrantaServerApiDataExportDatumsParameterValue]]",
    ) -> None:
        """Sets the parameter_values of this GrantaServerApiDataExportDatumsSeries.

        Parameters
        ----------
        parameter_values: List[GrantaServerApiDataExportDatumsParameterValue]
            The parameter_values of this GrantaServerApiDataExportDatumsSeries.
        """
        self._parameter_values = parameter_values

    @property
    def points(self) -> "Optional[List[GrantaServerApiDataExportDatumsSeriesPoint]]":
        """Gets the points of this GrantaServerApiDataExportDatumsSeries.

        Returns
        -------
        list[GrantaServerApiDataExportDatumsSeriesPoint]
            The points of this GrantaServerApiDataExportDatumsSeries.
        """
        return self._points

    @points.setter
    def points(
        self, points: "Optional[List[GrantaServerApiDataExportDatumsSeriesPoint]]"
    ) -> None:
        """Sets the points of this GrantaServerApiDataExportDatumsSeries.

        Parameters
        ----------
        points: List[GrantaServerApiDataExportDatumsSeriesPoint]
            The points of this GrantaServerApiDataExportDatumsSeries.
        """
        self._points = points

    @property
    def graph_decoration(
        self,
    ) -> "Optional[GrantaServerApiDataExportDatumsGraphDecoration]":
        """Gets the graph_decoration of this GrantaServerApiDataExportDatumsSeries.

        Returns
        -------
        GrantaServerApiDataExportDatumsGraphDecoration
            The graph_decoration of this GrantaServerApiDataExportDatumsSeries.
        """
        return self._graph_decoration

    @graph_decoration.setter
    def graph_decoration(
        self,
        graph_decoration: "Optional[GrantaServerApiDataExportDatumsGraphDecoration]",
    ) -> None:
        """Sets the graph_decoration of this GrantaServerApiDataExportDatumsSeries.

        Parameters
        ----------
        graph_decoration: GrantaServerApiDataExportDatumsGraphDecoration
            The graph_decoration of this GrantaServerApiDataExportDatumsSeries.
        """
        self._graph_decoration = graph_decoration

    @classmethod
    def get_real_child_model(cls, data: ModelBase) -> str:
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
        return self.to_str()  # type: ignore[no-any-return]

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiDataExportDatumsSeries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
