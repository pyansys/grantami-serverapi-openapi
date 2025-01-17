"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase
from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_datums_discrete_functional_datum import (
    GrantaServerApiDataExportDatumsDiscreteFunctionalDatum,
)  # noqa: F401


if TYPE_CHECKING:
    from . import *


class GrantaServerApiDataExportDatumsDiscreteFunctionalSeriesDatum(
    GrantaServerApiDataExportDatumsDiscreteFunctionalDatum
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
        "meta_datums": "list[GrantaServerApiDataExportDatumsDatum]",
        "not_applicable": "str",
        "parameters": "list[GrantaServerApiFunctionalDatumParameterInfo]",
        "series": "list[GrantaServerApiDataExportDatumsDiscreteSeries]",
        "x_axis_parameter": "GrantaServerApiFunctionalDatumParameterInfo",
    }

    attribute_map = {
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "datum_type": "datumType",
        "graph_type": "graphType",
        "meta_datums": "metaDatums",
        "not_applicable": "notApplicable",
        "parameters": "parameters",
        "series": "series",
        "x_axis_parameter": "xAxisParameter",
    }

    subtype_mapping = {
        "series": "GrantaServerApiDataExportDatumsDiscreteSeries",
    }

    discriminator = None

    def __init__(
        self,
        *,
        attribute_guid: "Optional[str]" = None,
        attribute_identity: "Optional[int]" = None,
        datum_type: "str" = "discreteFunctional",
        graph_type: "str" = "series",
        meta_datums: "Optional[List[GrantaServerApiDataExportDatumsDatum]]" = None,
        not_applicable: "str" = "applicable",
        parameters: "Optional[List[GrantaServerApiFunctionalDatumParameterInfo]]" = None,
        series: "Optional[List[GrantaServerApiDataExportDatumsDiscreteSeries]]" = None,
        x_axis_parameter: "Optional[GrantaServerApiFunctionalDatumParameterInfo]" = None,
    ) -> None:
        """GrantaServerApiDataExportDatumsDiscreteFunctionalSeriesDatum - a model defined in Swagger

        Parameters
        ----------
            attribute_guid: str, optional
            attribute_identity: int, optional
            datum_type: str
            graph_type: str
            meta_datums: List[GrantaServerApiDataExportDatumsDatum], optional
            not_applicable: str
            parameters: List[GrantaServerApiFunctionalDatumParameterInfo], optional
            series: List[GrantaServerApiDataExportDatumsDiscreteSeries], optional
            x_axis_parameter: GrantaServerApiFunctionalDatumParameterInfo, optional
        """
        super().__init__(
            attribute_guid=attribute_guid,
            attribute_identity=attribute_identity,
            datum_type=datum_type,
            meta_datums=meta_datums,
            not_applicable=not_applicable,
            parameters=parameters,
            x_axis_parameter=x_axis_parameter,
        )
        self._graph_type = None
        self._series = None

        self.graph_type = graph_type
        if series is not None:
            self.series = series

    @property
    def graph_type(self) -> "str":
        """Gets the graph_type of this GrantaServerApiDataExportDatumsDiscreteFunctionalSeriesDatum.

        Returns
        -------
        str
            The graph_type of this GrantaServerApiDataExportDatumsDiscreteFunctionalSeriesDatum.
        """
        return self._graph_type

    @graph_type.setter
    def graph_type(self, graph_type: "str") -> None:
        """Sets the graph_type of this GrantaServerApiDataExportDatumsDiscreteFunctionalSeriesDatum.

        Parameters
        ----------
        graph_type: str
            The graph_type of this GrantaServerApiDataExportDatumsDiscreteFunctionalSeriesDatum.
        """
        if graph_type is None:
            raise ValueError("Invalid value for 'graph_type', must not be 'None'")
        self._graph_type = graph_type

    @property
    def series(self) -> "list[GrantaServerApiDataExportDatumsDiscreteSeries]":
        """Gets the series of this GrantaServerApiDataExportDatumsDiscreteFunctionalSeriesDatum.

        Returns
        -------
        list[GrantaServerApiDataExportDatumsDiscreteSeries]
            The series of this GrantaServerApiDataExportDatumsDiscreteFunctionalSeriesDatum.
        """
        return self._series

    @series.setter
    def series(
        self, series: "list[GrantaServerApiDataExportDatumsDiscreteSeries]"
    ) -> None:
        """Sets the series of this GrantaServerApiDataExportDatumsDiscreteFunctionalSeriesDatum.

        Parameters
        ----------
        series: list[GrantaServerApiDataExportDatumsDiscreteSeries]
            The series of this GrantaServerApiDataExportDatumsDiscreteFunctionalSeriesDatum.
        """
        self._series = series

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
        if not isinstance(
            other, GrantaServerApiDataExportDatumsDiscreteFunctionalSeriesDatum
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
