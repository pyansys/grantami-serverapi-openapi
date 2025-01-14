"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.models.gsa_discrete_functional_datum import GsaDiscreteFunctionalDatum  # noqa: F401
from ansys.grantami.serverapi_openapi.models.gsa_graph_type import GsaGraphType
from ansys.grantami.serverapi_openapi.models.gsa_datum_type import GsaDatumType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaDiscreteFunctionalGridDatum(GsaDiscreteFunctionalDatum):
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
        "datum_type": "GsaDatumType",
        "graph": "GsaDiscreteGridGraph",
        "graph_type": "GsaGraphType",
        "not_applicable": "str",
        "parameter_settings": "list[GsaFunctionalParameterSetting]",
    }

    attribute_map: dict[str, str] = {
        "datum_type": "datumType",
        "graph": "graph",
        "graph_type": "graphType",
        "not_applicable": "notApplicable",
        "parameter_settings": "parameterSettings",
    }

    subtype_mapping: dict[str, str] = {
        "graph": "GsaDiscreteGridGraph",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, datum_type: "GsaDatumType" = GsaDatumType.DISCRETEFUNCTIONAL, graph: "GsaDiscreteGridGraph", graph_type: "GsaGraphType" = GsaGraphType.GRID, not_applicable: "str" = "applicable", parameter_settings: "list[GsaFunctionalParameterSetting]",) -> None:
        """GsaDiscreteFunctionalGridDatum - a model defined in Swagger

        Parameters
        ----------
        datum_type: GsaDatumType
        graph: GsaDiscreteGridGraph
        graph_type: GsaGraphType
        not_applicable: str
        parameter_settings: list[GsaFunctionalParameterSetting]
        """
        super().__init__(datum_type=datum_type, graph_type=graph_type, not_applicable=not_applicable, parameter_settings=parameter_settings)
        self._graph: GsaDiscreteGridGraph

        self.graph = graph

    @property
    def graph(self) -> "GsaDiscreteGridGraph":
        """Gets the graph of this GsaDiscreteFunctionalGridDatum.

        Returns
        -------
        GsaDiscreteGridGraph
            The graph of this GsaDiscreteFunctionalGridDatum.
        """
        return self._graph

    @graph.setter
    def graph(self, graph: "GsaDiscreteGridGraph") -> None:
        """Sets the graph of this GsaDiscreteFunctionalGridDatum.

        Parameters
        ----------
        graph: GsaDiscreteGridGraph
            The graph of this GsaDiscreteFunctionalGridDatum.
        """
        # Field is not nullable
        if graph is None:
            raise ValueError("Invalid value for 'graph', must not be 'None'")
        # Field is required
        if graph is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'graph', must not be 'Unset'")
        self._graph = graph

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
        if not isinstance(other, GsaDiscreteFunctionalGridDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

