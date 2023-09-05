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

from ansys.grantami.serverapi_openapi.models.granta_server_api_aggregations_attribute_value_aggregation import GrantaServerApiAggregationsAttributeValueAggregation  # noqa: F401

if TYPE_CHECKING:
    from . import *

class GrantaServerApiAggregationsFloatFunctionalAttributeAggregation(GrantaServerApiAggregationsAttributeValueAggregation):
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
        "x_axis_parameter_identity_values": "list[GrantaServerApiAggregationsValueWithCountOfSystemInt32]",
        "x_axis_parameter_guid_values": "list[GrantaServerApiAggregationsValueWithCountOfSystemGuid]",
        "show_as_table_values": "list[GrantaServerApiAggregationsValueWithCountOfSystemBoolean]",
        "minimum_number_of_series": "int",
        "maximum_number_of_series": "int",
        "datum_type": "str",
    }

    attribute_map = {
        "x_axis_parameter_identity_values": "xAxisParameterIdentityValues",
        "x_axis_parameter_guid_values": "xAxisParameterGuidValues",
        "show_as_table_values": "showAsTableValues",
        "minimum_number_of_series": "minimumNumberOfSeries",
        "maximum_number_of_series": "maximumNumberOfSeries",
        "datum_type": "datumType",
    }

    subtype_mapping = {
        "xAxisParameterIdentityValues": "GrantaServerApiAggregationsValueWithCountOfSystemInt32",
        "xAxisParameterGuidValues": "GrantaServerApiAggregationsValueWithCountOfSystemGuid",
        "showAsTableValues": "GrantaServerApiAggregationsValueWithCountOfSystemBoolean",
    }

    def __init__(self, *, attribute_aggregation_type: "str" = 'value', attribute_guid: "Optional[str]" = None, attribute_identity: "Optional[int]" = None, count: "Optional[int]" = None, datum_type: "str" = 'floatFunctionalGraph', maximum_number_of_series: "Optional[int]" = None, minimum_number_of_series: "Optional[int]" = None, show_as_table_values: "Optional[List[GrantaServerApiAggregationsValueWithCountOfSystemBoolean]]" = None, type: "str" = 'attribute', x_axis_parameter_guid_values: "Optional[List[GrantaServerApiAggregationsValueWithCountOfSystemGuid]]" = None, x_axis_parameter_identity_values: "Optional[List[GrantaServerApiAggregationsValueWithCountOfSystemInt32]]" = None) -> None:
        """GrantaServerApiAggregationsFloatFunctionalAttributeAggregation - a model defined in Swagger

        Parameters
        ----------
            attribute_aggregation_type: str
            attribute_guid: str, optional
            attribute_identity: int, optional
            count: int, optional
            datum_type: str
            maximum_number_of_series: int, optional
            minimum_number_of_series: int, optional
            show_as_table_values: List[GrantaServerApiAggregationsValueWithCountOfSystemBoolean], optional
            type: str
            x_axis_parameter_guid_values: List[GrantaServerApiAggregationsValueWithCountOfSystemGuid], optional
            x_axis_parameter_identity_values: List[GrantaServerApiAggregationsValueWithCountOfSystemInt32], optional
        """
        super().__init__(attribute_aggregation_type=attribute_aggregation_type, attribute_guid=attribute_guid, attribute_identity=attribute_identity, count=count, type=type)
        self._x_axis_parameter_identity_values = None
        self._x_axis_parameter_guid_values = None
        self._show_as_table_values = None
        self._minimum_number_of_series = None
        self._maximum_number_of_series = None
        self._datum_type = None
        self.discriminator = None
        if x_axis_parameter_identity_values is not None:
            self.x_axis_parameter_identity_values = x_axis_parameter_identity_values
        if x_axis_parameter_guid_values is not None:
            self.x_axis_parameter_guid_values = x_axis_parameter_guid_values
        if show_as_table_values is not None:
            self.show_as_table_values = show_as_table_values
        if minimum_number_of_series is not None:
            self.minimum_number_of_series = minimum_number_of_series
        if maximum_number_of_series is not None:
            self.maximum_number_of_series = maximum_number_of_series
        self.datum_type = datum_type

    @property
    def x_axis_parameter_identity_values(self) -> "list[GrantaServerApiAggregationsValueWithCountOfSystemInt32]":
        """Gets the x_axis_parameter_identity_values of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.

        Returns
        -------
        list[GrantaServerApiAggregationsValueWithCountOfSystemInt32]
            The x_axis_parameter_identity_values of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.
        """
        return self._x_axis_parameter_identity_values

    @x_axis_parameter_identity_values.setter
    def x_axis_parameter_identity_values(self, x_axis_parameter_identity_values: "list[GrantaServerApiAggregationsValueWithCountOfSystemInt32]") -> None:
        """Sets the x_axis_parameter_identity_values of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.

        Parameters
        ----------
        x_axis_parameter_identity_values: list[GrantaServerApiAggregationsValueWithCountOfSystemInt32]
            The x_axis_parameter_identity_values of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.
        """
        self._x_axis_parameter_identity_values = x_axis_parameter_identity_values

    @property
    def x_axis_parameter_guid_values(self) -> "list[GrantaServerApiAggregationsValueWithCountOfSystemGuid]":
        """Gets the x_axis_parameter_guid_values of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.

        Returns
        -------
        list[GrantaServerApiAggregationsValueWithCountOfSystemGuid]
            The x_axis_parameter_guid_values of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.
        """
        return self._x_axis_parameter_guid_values

    @x_axis_parameter_guid_values.setter
    def x_axis_parameter_guid_values(self, x_axis_parameter_guid_values: "list[GrantaServerApiAggregationsValueWithCountOfSystemGuid]") -> None:
        """Sets the x_axis_parameter_guid_values of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.

        Parameters
        ----------
        x_axis_parameter_guid_values: list[GrantaServerApiAggregationsValueWithCountOfSystemGuid]
            The x_axis_parameter_guid_values of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.
        """
        self._x_axis_parameter_guid_values = x_axis_parameter_guid_values

    @property
    def show_as_table_values(self) -> "list[GrantaServerApiAggregationsValueWithCountOfSystemBoolean]":
        """Gets the show_as_table_values of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.

        Returns
        -------
        list[GrantaServerApiAggregationsValueWithCountOfSystemBoolean]
            The show_as_table_values of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.
        """
        return self._show_as_table_values

    @show_as_table_values.setter
    def show_as_table_values(self, show_as_table_values: "list[GrantaServerApiAggregationsValueWithCountOfSystemBoolean]") -> None:
        """Sets the show_as_table_values of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.

        Parameters
        ----------
        show_as_table_values: list[GrantaServerApiAggregationsValueWithCountOfSystemBoolean]
            The show_as_table_values of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.
        """
        self._show_as_table_values = show_as_table_values

    @property
    def minimum_number_of_series(self) -> "int":
        """Gets the minimum_number_of_series of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.

        Returns
        -------
        int
            The minimum_number_of_series of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.
        """
        return self._minimum_number_of_series

    @minimum_number_of_series.setter
    def minimum_number_of_series(self, minimum_number_of_series: "int") -> None:
        """Sets the minimum_number_of_series of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.

        Parameters
        ----------
        minimum_number_of_series: int
            The minimum_number_of_series of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.
        """
        self._minimum_number_of_series = minimum_number_of_series

    @property
    def maximum_number_of_series(self) -> "int":
        """Gets the maximum_number_of_series of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.

        Returns
        -------
        int
            The maximum_number_of_series of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.
        """
        return self._maximum_number_of_series

    @maximum_number_of_series.setter
    def maximum_number_of_series(self, maximum_number_of_series: "int") -> None:
        """Sets the maximum_number_of_series of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.

        Parameters
        ----------
        maximum_number_of_series: int
            The maximum_number_of_series of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.
        """
        self._maximum_number_of_series = maximum_number_of_series

    @property
    def datum_type(self) -> "str":
        """Gets the datum_type of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.

        Returns
        -------
        str
            The datum_type of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type: "str") -> None:
        """Sets the datum_type of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.

        Parameters
        ----------
        datum_type: str
            The datum_type of this GrantaServerApiAggregationsFloatFunctionalAttributeAggregation.
        """
        if datum_type is None:
            raise ValueError("Invalid value for 'datum_type', must not be 'None'")
        self._datum_type = datum_type

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
        if issubclass(GrantaServerApiAggregationsFloatFunctionalAttributeAggregation, dict):
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
        if not isinstance(other, GrantaServerApiAggregationsFloatFunctionalAttributeAggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
