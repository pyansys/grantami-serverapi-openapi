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
from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_datums_discrete_functional_datum import (
    GrantaServerApiDataExportDatumsDiscreteFunctionalDatum,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiDataExportDatumsDiscreteFunctionalGridDatum(
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
    swagger_types: Dict[str, str] = {
        "attribute_guid": "str",
        "attribute_identity": "int",
        "datum_type": "str",
        "graph_type": "str",
        "meta_datums": "list[GrantaServerApiDataExportDatumsDatum]",
        "not_applicable": "str",
        "parameters": "list[GrantaServerApiFunctionalDatumParameterInfo]",
        "values": "list[GrantaServerApiDataExportDatumsDiscreteGridPoint]",
        "x_axis_parameter": "GrantaServerApiFunctionalDatumParameterInfo",
    }

    attribute_map: Dict[str, str] = {
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "datum_type": "datumType",
        "graph_type": "graphType",
        "meta_datums": "metaDatums",
        "not_applicable": "notApplicable",
        "parameters": "parameters",
        "values": "values",
        "x_axis_parameter": "xAxisParameter",
    }

    subtype_mapping: Dict[str, str] = {
        "values": "GrantaServerApiDataExportDatumsDiscreteGridPoint",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_guid: "Union[str, Unset_Type]" = Unset,
        attribute_identity: "Union[int, Unset_Type]" = Unset,
        datum_type: "str" = "discreteFunctional",
        graph_type: "str" = "grid",
        meta_datums: "Union[List[GrantaServerApiDataExportDatumsDatum], None, Unset_Type]" = Unset,
        not_applicable: "str" = "applicable",
        parameters: "Union[List[GrantaServerApiFunctionalDatumParameterInfo], None, Unset_Type]" = Unset,
        values: "Union[List[GrantaServerApiDataExportDatumsDiscreteGridPoint], None, Unset_Type]" = Unset,
        x_axis_parameter: "Union[GrantaServerApiFunctionalDatumParameterInfo, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiDataExportDatumsDiscreteFunctionalGridDatum - a model defined in Swagger

        Parameters
        ----------
        attribute_guid: str, optional
        attribute_identity: int, optional
        datum_type: str
        graph_type: str
        meta_datums: List[GrantaServerApiDataExportDatumsDatum], optional
        not_applicable: str
        parameters: List[GrantaServerApiFunctionalDatumParameterInfo], optional
        values: List[GrantaServerApiDataExportDatumsDiscreteGridPoint], optional
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
        self._graph_type: str
        self._values: Union[
            List[GrantaServerApiDataExportDatumsDiscreteGridPoint], None, Unset_Type
        ] = Unset

        self.graph_type = graph_type
        if values is not Unset:
            self.values = values

    @property
    def graph_type(self) -> "str":
        """Gets the graph_type of this GrantaServerApiDataExportDatumsDiscreteFunctionalGridDatum.

        Returns
        -------
        str
            The graph_type of this GrantaServerApiDataExportDatumsDiscreteFunctionalGridDatum.
        """
        return self._graph_type

    @graph_type.setter
    def graph_type(self, graph_type: "str") -> None:
        """Sets the graph_type of this GrantaServerApiDataExportDatumsDiscreteFunctionalGridDatum.

        Parameters
        ----------
        graph_type: str
            The graph_type of this GrantaServerApiDataExportDatumsDiscreteFunctionalGridDatum.
        """
        # Field is not nullable
        if graph_type is None:
            raise ValueError("Invalid value for 'graph_type', must not be 'None'")
        # Field is required
        if graph_type is Unset:  # type: ignore[comparison-overlap]
            raise ValueError("Invalid value for 'graph_type', must not be 'Unset'")
        self._graph_type = graph_type

    @property
    def values(
        self,
    ) -> "Union[List[GrantaServerApiDataExportDatumsDiscreteGridPoint], None, Unset_Type]":
        """Gets the values of this GrantaServerApiDataExportDatumsDiscreteFunctionalGridDatum.

        Returns
        -------
        Union[List[GrantaServerApiDataExportDatumsDiscreteGridPoint], None, Unset_Type]
            The values of this GrantaServerApiDataExportDatumsDiscreteFunctionalGridDatum.
        """
        return self._values

    @values.setter
    def values(
        self,
        values: "Union[List[GrantaServerApiDataExportDatumsDiscreteGridPoint], None, Unset_Type]",
    ) -> None:
        """Sets the values of this GrantaServerApiDataExportDatumsDiscreteFunctionalGridDatum.

        Parameters
        ----------
        values: Union[List[GrantaServerApiDataExportDatumsDiscreteGridPoint], None, Unset_Type]
            The values of this GrantaServerApiDataExportDatumsDiscreteFunctionalGridDatum.
        """
        self._values = values

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
        if not isinstance(
            other, GrantaServerApiDataExportDatumsDiscreteFunctionalGridDatum
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
