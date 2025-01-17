"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase
from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_datums_float_functional_datum import (
    GrantaServerApiDataExportDatumsFloatFunctionalDatum,
)  # noqa: F401


if TYPE_CHECKING:
    from . import *


class GrantaServerApiDataExportDatumsFunctionalSeriesDatum(
    GrantaServerApiDataExportDatumsFloatFunctionalDatum
):
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
    swagger_types = {
        "attribute_guid": "str",
        "attribute_identity": "int",
        "datum_type": "str",
        "graph_type": "str",
        "is_estimated": "bool",
        "is_logarithmic": "bool",
        "is_range": "bool",
        "meta_datums": "list[GrantaServerApiDataExportDatumsDatum]",
        "not_applicable": "str",
        "parameters": "list[GrantaServerApiFunctionalDatumParameterInfo]",
        "series": "list[GrantaServerApiDataExportDatumsSeries]",
        "show_as_table": "bool",
        "unit_symbol": "str",
        "x_axis_parameter": "GrantaServerApiFunctionalDatumParameterInfo",
    }

    attribute_map = {
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "datum_type": "datumType",
        "graph_type": "graphType",
        "is_estimated": "isEstimated",
        "is_logarithmic": "isLogarithmic",
        "is_range": "isRange",
        "meta_datums": "metaDatums",
        "not_applicable": "notApplicable",
        "parameters": "parameters",
        "series": "series",
        "show_as_table": "showAsTable",
        "unit_symbol": "unitSymbol",
        "x_axis_parameter": "xAxisParameter",
    }

    subtype_mapping = {
        "series": "GrantaServerApiDataExportDatumsSeries",
    }

    discriminator = None

    def __init__(
        self,
        *,
        attribute_guid: "Optional[str]" = None,
        attribute_identity: "Optional[int]" = None,
        datum_type: "str" = "floatFunctional",
        graph_type: "str" = "series",
        is_estimated: "Optional[bool]" = None,
        is_logarithmic: "Optional[bool]" = None,
        is_range: "Optional[bool]" = None,
        meta_datums: "Optional[List[GrantaServerApiDataExportDatumsDatum]]" = None,
        not_applicable: "str" = "applicable",
        parameters: "Optional[List[GrantaServerApiFunctionalDatumParameterInfo]]" = None,
        series: "Optional[List[GrantaServerApiDataExportDatumsSeries]]" = None,
        show_as_table: "Optional[bool]" = None,
        unit_symbol: "Optional[str]" = None,
        x_axis_parameter: "Optional[GrantaServerApiFunctionalDatumParameterInfo]" = None,
    ) -> None:
        """GrantaServerApiDataExportDatumsFunctionalSeriesDatum - a model defined in Swagger

        Parameters
        ----------
            attribute_guid: str, optional
            attribute_identity: int, optional
            datum_type: str
            graph_type: str
            is_estimated: bool, optional
            is_logarithmic: bool, optional
            is_range: bool, optional
            meta_datums: List[GrantaServerApiDataExportDatumsDatum], optional
            not_applicable: str
            parameters: List[GrantaServerApiFunctionalDatumParameterInfo], optional
            series: List[GrantaServerApiDataExportDatumsSeries], optional
            show_as_table: bool, optional
            unit_symbol: str, optional
            x_axis_parameter: GrantaServerApiFunctionalDatumParameterInfo, optional
        """
        super().__init__(
            attribute_guid=attribute_guid,
            attribute_identity=attribute_identity,
            datum_type=datum_type,
            is_estimated=is_estimated,
            meta_datums=meta_datums,
            not_applicable=not_applicable,
            parameters=parameters,
            unit_symbol=unit_symbol,
            x_axis_parameter=x_axis_parameter,
        )
        self._graph_type = None
        self._series = None
        self._is_logarithmic = None
        self._is_range = None
        self._show_as_table = None

        self.graph_type = graph_type
        if series is not None:
            self.series = series
        if is_logarithmic is not None:
            self.is_logarithmic = is_logarithmic
        if is_range is not None:
            self.is_range = is_range
        if show_as_table is not None:
            self.show_as_table = show_as_table

    @property
    def graph_type(self) -> "str":
        """Gets the graph_type of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.

        Returns
        -------
        str
            The graph_type of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.
        """
        return self._graph_type

    @graph_type.setter
    def graph_type(self, graph_type: "str") -> None:
        """Sets the graph_type of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.

        Parameters
        ----------
        graph_type: str
            The graph_type of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.
        """
        if graph_type is None:
            raise ValueError("Invalid value for 'graph_type', must not be 'None'")
        self._graph_type = graph_type

    @property
    def series(self) -> "list[GrantaServerApiDataExportDatumsSeries]":
        """Gets the series of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.

        Returns
        -------
        list[GrantaServerApiDataExportDatumsSeries]
            The series of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.
        """
        return self._series

    @series.setter
    def series(self, series: "list[GrantaServerApiDataExportDatumsSeries]") -> None:
        """Sets the series of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.

        Parameters
        ----------
        series: list[GrantaServerApiDataExportDatumsSeries]
            The series of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.
        """
        self._series = series

    @property
    def is_logarithmic(self) -> "bool":
        """Gets the is_logarithmic of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.

        Returns
        -------
        bool
            The is_logarithmic of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.
        """
        return self._is_logarithmic

    @is_logarithmic.setter
    def is_logarithmic(self, is_logarithmic: "bool") -> None:
        """Sets the is_logarithmic of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.

        Parameters
        ----------
        is_logarithmic: bool
            The is_logarithmic of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.
        """
        self._is_logarithmic = is_logarithmic

    @property
    def is_range(self) -> "bool":
        """Gets the is_range of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.

        Returns
        -------
        bool
            The is_range of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.
        """
        return self._is_range

    @is_range.setter
    def is_range(self, is_range: "bool") -> None:
        """Sets the is_range of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.

        Parameters
        ----------
        is_range: bool
            The is_range of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.
        """
        self._is_range = is_range

    @property
    def show_as_table(self) -> "bool":
        """Gets the show_as_table of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.

        Returns
        -------
        bool
            The show_as_table of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.
        """
        return self._show_as_table

    @show_as_table.setter
    def show_as_table(self, show_as_table: "bool") -> None:
        """Sets the show_as_table of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.

        Parameters
        ----------
        show_as_table: bool
            The show_as_table of this GrantaServerApiDataExportDatumsFunctionalSeriesDatum.
        """
        self._show_as_table = show_as_table

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
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiDataExportDatumsFunctionalSeriesDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
