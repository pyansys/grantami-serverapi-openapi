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
from ansys.grantami.serverapi_openapi.models.granta_server_api_search_datum_criterion import (
    GrantaServerApiSearchDatumCriterion,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSearchFloatFunctionalGraphDatumCriterion(
    GrantaServerApiSearchDatumCriterion
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
        "default_x_axis_parameter_guid": "str",
        "default_x_axis_parameter_identity": "int",
        "is_series_graph": "bool",
        "number_of_points_gte": "int",
        "number_of_points_lte": "int",
        "number_of_series_gte": "int",
        "number_of_series_lte": "int",
        "show_as_table": "bool",
        "type": "str",
        "x_axis_parameter_guid": "str",
        "x_axis_parameter_identity": "int",
    }

    attribute_map: Dict[str, str] = {
        "default_x_axis_parameter_guid": "defaultXAxisParameterGuid",
        "default_x_axis_parameter_identity": "defaultXAxisParameterIdentity",
        "is_series_graph": "isSeriesGraph",
        "number_of_points_gte": "numberOfPointsGte",
        "number_of_points_lte": "numberOfPointsLte",
        "number_of_series_gte": "numberOfSeriesGte",
        "number_of_series_lte": "numberOfSeriesLte",
        "show_as_table": "showAsTable",
        "type": "type",
        "x_axis_parameter_guid": "xAxisParameterGuid",
        "x_axis_parameter_identity": "xAxisParameterIdentity",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        default_x_axis_parameter_guid: "Union[str, None, Unset_Type]" = Unset,
        default_x_axis_parameter_identity: "Union[int, None, Unset_Type]" = Unset,
        is_series_graph: "Union[bool, None, Unset_Type]" = Unset,
        number_of_points_gte: "Union[int, None, Unset_Type]" = Unset,
        number_of_points_lte: "Union[int, None, Unset_Type]" = Unset,
        number_of_series_gte: "Union[int, None, Unset_Type]" = Unset,
        number_of_series_lte: "Union[int, None, Unset_Type]" = Unset,
        show_as_table: "Union[bool, None, Unset_Type]" = Unset,
        type: "str" = "floatFunctionalGraph",
        x_axis_parameter_guid: "Union[str, None, Unset_Type]" = Unset,
        x_axis_parameter_identity: "Union[int, None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSearchFloatFunctionalGraphDatumCriterion - a model defined in Swagger

        Parameters
        ----------
        default_x_axis_parameter_guid: str, optional
        default_x_axis_parameter_identity: int, optional
        is_series_graph: bool, optional
        number_of_points_gte: int, optional
        number_of_points_lte: int, optional
        number_of_series_gte: int, optional
        number_of_series_lte: int, optional
        show_as_table: bool, optional
        type: str
        x_axis_parameter_guid: str, optional
        x_axis_parameter_identity: int, optional
        """
        super().__init__()
        self._type: str
        self._x_axis_parameter_identity: Union[int, None, Unset_Type] = Unset
        self._x_axis_parameter_guid: Union[str, None, Unset_Type] = Unset
        self._number_of_series_lte: Union[int, None, Unset_Type] = Unset
        self._number_of_series_gte: Union[int, None, Unset_Type] = Unset
        self._show_as_table: Union[bool, None, Unset_Type] = Unset
        self._default_x_axis_parameter_identity: Union[int, None, Unset_Type] = Unset
        self._default_x_axis_parameter_guid: Union[str, None, Unset_Type] = Unset
        self._number_of_points_lte: Union[int, None, Unset_Type] = Unset
        self._number_of_points_gte: Union[int, None, Unset_Type] = Unset
        self._is_series_graph: Union[bool, None, Unset_Type] = Unset

        self.type = type
        if x_axis_parameter_identity is not Unset:
            self.x_axis_parameter_identity = x_axis_parameter_identity
        if x_axis_parameter_guid is not Unset:
            self.x_axis_parameter_guid = x_axis_parameter_guid
        if number_of_series_lte is not Unset:
            self.number_of_series_lte = number_of_series_lte
        if number_of_series_gte is not Unset:
            self.number_of_series_gte = number_of_series_gte
        if show_as_table is not Unset:
            self.show_as_table = show_as_table
        if default_x_axis_parameter_identity is not Unset:
            self.default_x_axis_parameter_identity = default_x_axis_parameter_identity
        if default_x_axis_parameter_guid is not Unset:
            self.default_x_axis_parameter_guid = default_x_axis_parameter_guid
        if number_of_points_lte is not Unset:
            self.number_of_points_lte = number_of_points_lte
        if number_of_points_gte is not Unset:
            self.number_of_points_gte = number_of_points_gte
        if is_series_graph is not Unset:
            self.is_series_graph = is_series_graph

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @property
    def x_axis_parameter_identity(self) -> "Union[int, None, Unset_Type]":
        """Gets the x_axis_parameter_identity of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional x axis parameter filter. Only series graphs have an x axis.

        Returns
        -------
        Union[int, None, Unset_Type]
            The x_axis_parameter_identity of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        return self._x_axis_parameter_identity

    @x_axis_parameter_identity.setter
    def x_axis_parameter_identity(
        self, x_axis_parameter_identity: "Union[int, None, Unset_Type]"
    ) -> None:
        """Sets the x_axis_parameter_identity of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional x axis parameter filter. Only series graphs have an x axis.

        Parameters
        ----------
        x_axis_parameter_identity: Union[int, None, Unset_Type]
            The x_axis_parameter_identity of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        self._x_axis_parameter_identity = x_axis_parameter_identity

    @property
    def x_axis_parameter_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the x_axis_parameter_guid of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional x axis parameter filter. Only series graphs have an x axis.

        Returns
        -------
        Union[str, None, Unset_Type]
            The x_axis_parameter_guid of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        return self._x_axis_parameter_guid

    @x_axis_parameter_guid.setter
    def x_axis_parameter_guid(
        self, x_axis_parameter_guid: "Union[str, None, Unset_Type]"
    ) -> None:
        """Sets the x_axis_parameter_guid of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional x axis parameter filter. Only series graphs have an x axis.

        Parameters
        ----------
        x_axis_parameter_guid: Union[str, None, Unset_Type]
            The x_axis_parameter_guid of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        self._x_axis_parameter_guid = x_axis_parameter_guid

    @property
    def number_of_series_lte(self) -> "Union[int, None, Unset_Type]":
        """Gets the number_of_series_lte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional filter for the number of series.

        Returns
        -------
        Union[int, None, Unset_Type]
            The number_of_series_lte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        return self._number_of_series_lte

    @number_of_series_lte.setter
    def number_of_series_lte(
        self, number_of_series_lte: "Union[int, None, Unset_Type]"
    ) -> None:
        """Sets the number_of_series_lte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional filter for the number of series.

        Parameters
        ----------
        number_of_series_lte: Union[int, None, Unset_Type]
            The number_of_series_lte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        self._number_of_series_lte = number_of_series_lte

    @property
    def number_of_series_gte(self) -> "Union[int, None, Unset_Type]":
        """Gets the number_of_series_gte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional filter for the number of series.

        Returns
        -------
        Union[int, None, Unset_Type]
            The number_of_series_gte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        return self._number_of_series_gte

    @number_of_series_gte.setter
    def number_of_series_gte(
        self, number_of_series_gte: "Union[int, None, Unset_Type]"
    ) -> None:
        """Sets the number_of_series_gte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional filter for the number of series.

        Parameters
        ----------
        number_of_series_gte: Union[int, None, Unset_Type]
            The number_of_series_gte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        self._number_of_series_gte = number_of_series_gte

    @property
    def show_as_table(self) -> "Union[bool, None, Unset_Type]":
        """Gets the show_as_table of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional filter for data on the \"Show as table\" property

        Returns
        -------
        Union[bool, None, Unset_Type]
            The show_as_table of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        return self._show_as_table

    @show_as_table.setter
    def show_as_table(self, show_as_table: "Union[bool, None, Unset_Type]") -> None:
        """Sets the show_as_table of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional filter for data on the \"Show as table\" property

        Parameters
        ----------
        show_as_table: Union[bool, None, Unset_Type]
            The show_as_table of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        self._show_as_table = show_as_table

    @property
    def default_x_axis_parameter_identity(self) -> "Union[int, None, Unset_Type]":
        """Gets the default_x_axis_parameter_identity of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional default x axis parameter filter. Only grid graphs have a default x axis.

        Returns
        -------
        Union[int, None, Unset_Type]
            The default_x_axis_parameter_identity of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        return self._default_x_axis_parameter_identity

    @default_x_axis_parameter_identity.setter
    def default_x_axis_parameter_identity(
        self, default_x_axis_parameter_identity: "Union[int, None, Unset_Type]"
    ) -> None:
        """Sets the default_x_axis_parameter_identity of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional default x axis parameter filter. Only grid graphs have a default x axis.

        Parameters
        ----------
        default_x_axis_parameter_identity: Union[int, None, Unset_Type]
            The default_x_axis_parameter_identity of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        self._default_x_axis_parameter_identity = default_x_axis_parameter_identity

    @property
    def default_x_axis_parameter_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the default_x_axis_parameter_guid of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional x axis parameter filter. Only grid graphs have a default x axis..

        Returns
        -------
        Union[str, None, Unset_Type]
            The default_x_axis_parameter_guid of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        return self._default_x_axis_parameter_guid

    @default_x_axis_parameter_guid.setter
    def default_x_axis_parameter_guid(
        self, default_x_axis_parameter_guid: "Union[str, None, Unset_Type]"
    ) -> None:
        """Sets the default_x_axis_parameter_guid of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional x axis parameter filter. Only grid graphs have a default x axis..

        Parameters
        ----------
        default_x_axis_parameter_guid: Union[str, None, Unset_Type]
            The default_x_axis_parameter_guid of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        self._default_x_axis_parameter_guid = default_x_axis_parameter_guid

    @property
    def number_of_points_lte(self) -> "Union[int, None, Unset_Type]":
        """Gets the number_of_points_lte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional filter for the number of points in a grid graph.

        Returns
        -------
        Union[int, None, Unset_Type]
            The number_of_points_lte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        return self._number_of_points_lte

    @number_of_points_lte.setter
    def number_of_points_lte(
        self, number_of_points_lte: "Union[int, None, Unset_Type]"
    ) -> None:
        """Sets the number_of_points_lte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional filter for the number of points in a grid graph.

        Parameters
        ----------
        number_of_points_lte: Union[int, None, Unset_Type]
            The number_of_points_lte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        self._number_of_points_lte = number_of_points_lte

    @property
    def number_of_points_gte(self) -> "Union[int, None, Unset_Type]":
        """Gets the number_of_points_gte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional filter for the number of points in a grid graph.

        Returns
        -------
        Union[int, None, Unset_Type]
            The number_of_points_gte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        return self._number_of_points_gte

    @number_of_points_gte.setter
    def number_of_points_gte(
        self, number_of_points_gte: "Union[int, None, Unset_Type]"
    ) -> None:
        """Sets the number_of_points_gte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional filter for the number of points in a grid graph.

        Parameters
        ----------
        number_of_points_gte: Union[int, None, Unset_Type]
            The number_of_points_gte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        self._number_of_points_gte = number_of_points_gte

    @property
    def is_series_graph(self) -> "Union[bool, None, Unset_Type]":
        """Gets the is_series_graph of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional filter for data on the type of graph

        Returns
        -------
        Union[bool, None, Unset_Type]
            The is_series_graph of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        return self._is_series_graph

    @is_series_graph.setter
    def is_series_graph(self, is_series_graph: "Union[bool, None, Unset_Type]") -> None:
        """Sets the is_series_graph of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional filter for data on the type of graph

        Parameters
        ----------
        is_series_graph: Union[bool, None, Unset_Type]
            The is_series_graph of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        self._is_series_graph = is_series_graph

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
            other, GrantaServerApiSearchFloatFunctionalGraphDatumCriterion
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
