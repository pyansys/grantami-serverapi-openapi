"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase

from ansys.grantami.serverapi_openapi.models.granta_server_api_search_datum_criterion import GrantaServerApiSearchDatumCriterion  # noqa: F401

if TYPE_CHECKING:
    from . import *

class GrantaServerApiSearchFloatFunctionalGraphDatumCriterion(GrantaServerApiSearchDatumCriterion):
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

    """
    swagger_types = {
        "number_of_series_gte": "int",
        "number_of_series_lte": "int",
        "show_as_table": "bool",
        "type": "str",
        "x_axis_parameter_guid": "str",
        "x_axis_parameter_identity": "int",
    }

    attribute_map = {
        "number_of_series_gte": "numberOfSeriesGte",
        "number_of_series_lte": "numberOfSeriesLte",
        "show_as_table": "showAsTable",
        "type": "type",
        "x_axis_parameter_guid": "xAxisParameterGuid",
        "x_axis_parameter_identity": "xAxisParameterIdentity",
    }

    subtype_mapping = {
    }

    def __init__(self, *, number_of_series_gte: "Optional[int]" = None, number_of_series_lte: "Optional[int]" = None, show_as_table: "Optional[bool]" = None, type: "str" = 'floatFunctionalGraph', x_axis_parameter_guid: "Optional[str]" = None, x_axis_parameter_identity: "Optional[int]" = None,) -> None:
        """GrantaServerApiSearchFloatFunctionalGraphDatumCriterion - a model defined in Swagger

        Parameters
        ----------
            number_of_series_gte: int, optional
            number_of_series_lte: int, optional
            show_as_table: bool, optional
            type: str
            x_axis_parameter_guid: str, optional
            x_axis_parameter_identity: int, optional
        """
        super().__init__()
        self._type = None
        self._x_axis_parameter_identity = None
        self._x_axis_parameter_guid = None
        self._number_of_series_lte = None
        self._number_of_series_gte = None
        self._show_as_table = None
        self.discriminator = None
        self.type = type
        if x_axis_parameter_identity is not None:
            self.x_axis_parameter_identity = x_axis_parameter_identity
        if x_axis_parameter_guid is not None:
            self.x_axis_parameter_guid = x_axis_parameter_guid
        if number_of_series_lte is not None:
            self.number_of_series_lte = number_of_series_lte
        if number_of_series_gte is not None:
            self.number_of_series_gte = number_of_series_gte
        if show_as_table is not None:
            self.show_as_table = show_as_table

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
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @property
    def x_axis_parameter_identity(self) -> "int":
        """Gets the x_axis_parameter_identity of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional x axis parameter filter.

        Returns
        -------
        int
            The x_axis_parameter_identity of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        return self._x_axis_parameter_identity

    @x_axis_parameter_identity.setter
    def x_axis_parameter_identity(self, x_axis_parameter_identity: "int") -> None:
        """Sets the x_axis_parameter_identity of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional x axis parameter filter.

        Parameters
        ----------
        x_axis_parameter_identity: int
            The x_axis_parameter_identity of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        self._x_axis_parameter_identity = x_axis_parameter_identity

    @property
    def x_axis_parameter_guid(self) -> "str":
        """Gets the x_axis_parameter_guid of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional x axis parameter filter.

        Returns
        -------
        str
            The x_axis_parameter_guid of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        return self._x_axis_parameter_guid

    @x_axis_parameter_guid.setter
    def x_axis_parameter_guid(self, x_axis_parameter_guid: "str") -> None:
        """Sets the x_axis_parameter_guid of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional x axis parameter filter.

        Parameters
        ----------
        x_axis_parameter_guid: str
            The x_axis_parameter_guid of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        self._x_axis_parameter_guid = x_axis_parameter_guid

    @property
    def number_of_series_lte(self) -> "int":
        """Gets the number_of_series_lte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional filter for the number of series.

        Returns
        -------
        int
            The number_of_series_lte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        return self._number_of_series_lte

    @number_of_series_lte.setter
    def number_of_series_lte(self, number_of_series_lte: "int") -> None:
        """Sets the number_of_series_lte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional filter for the number of series.

        Parameters
        ----------
        number_of_series_lte: int
            The number_of_series_lte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        self._number_of_series_lte = number_of_series_lte

    @property
    def number_of_series_gte(self) -> "int":
        """Gets the number_of_series_gte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional filter for the number of series.

        Returns
        -------
        int
            The number_of_series_gte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        return self._number_of_series_gte

    @number_of_series_gte.setter
    def number_of_series_gte(self, number_of_series_gte: "int") -> None:
        """Sets the number_of_series_gte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional filter for the number of series.

        Parameters
        ----------
        number_of_series_gte: int
            The number_of_series_gte of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        self._number_of_series_gte = number_of_series_gte

    @property
    def show_as_table(self) -> "bool":
        """Gets the show_as_table of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional filter for data on the \"Show as table\" property

        Returns
        -------
        bool
            The show_as_table of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        return self._show_as_table

    @show_as_table.setter
    def show_as_table(self, show_as_table: "bool") -> None:
        """Sets the show_as_table of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        Optional filter for data on the \"Show as table\" property

        Parameters
        ----------
        show_as_table: bool
            The show_as_table of this GrantaServerApiSearchFloatFunctionalGraphDatumCriterion.
        """
        self._show_as_table = show_as_table

    def get_real_child_model(self, data: ModelBase) -> str:
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

    def to_dict(self) -> Dict:
        """Returns the model properties as a dict

        Returns
        -------
        Dict
            Dictionary indexed by property name containing all the model properties
        """
        result = {}

        for attr in self.swagger_types.keys():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GrantaServerApiSearchFloatFunctionalGraphDatumCriterion, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model

        Returns
        -------
        str
            String representation of the model as a dictionary
        """
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiSearchFloatFunctionalGraphDatumCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
