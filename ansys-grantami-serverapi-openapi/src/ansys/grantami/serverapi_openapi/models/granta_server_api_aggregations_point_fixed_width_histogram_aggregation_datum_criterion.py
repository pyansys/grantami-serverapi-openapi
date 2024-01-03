"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase
from ansys.grantami.serverapi_openapi.models.granta_server_api_aggregations_aggregation_datum_criterion import (
    GrantaServerApiAggregationsAggregationDatumCriterion,
)  # noqa: F401


if TYPE_CHECKING:
    from . import *


class GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion(
    GrantaServerApiAggregationsAggregationDatumCriterion
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
        "interval": "float",
        "offset": "float",
        "type": "str",
    }

    attribute_map = {
        "interval": "interval",
        "offset": "offset",
        "type": "type",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        interval: "Optional[float]" = None,
        offset: "Optional[float]" = None,
        type: "str" = "pointFixedWidthHistogram",
    ) -> None:
        """GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion - a model defined in Swagger

        Parameters
        ----------
            interval: float, optional
            offset: float, optional
            type: str
        """
        super().__init__()
        self._interval = None
        self._offset = None
        self._type = None

        if interval is not None:
            self.interval = interval
        if offset is not None:
            self.offset = offset
        self.type = type

    @property
    def interval(self) -> "float":
        """Gets the interval of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.
        Fixed size of the resulting histogram buckets

        Returns
        -------
        float
            The interval of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.
        """
        return self._interval

    @interval.setter
    def interval(self, interval: "float") -> None:
        """Sets the interval of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.
        Fixed size of the resulting histogram buckets

        Parameters
        ----------
        interval: float
            The interval of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.
        """
        self._interval = interval

    @property
    def offset(self) -> "float":
        """Gets the offset of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.
        Offset of the lowest bucket boundary. Defaults to 0. Must be less than the interval.

        Returns
        -------
        float
            The offset of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.
        """
        return self._offset

    @offset.setter
    def offset(self, offset: "float") -> None:
        """Sets the offset of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.
        Offset of the lowest bucket boundary. Defaults to 0. Must be less than the interval.

        Parameters
        ----------
        offset: float
            The offset of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.
        """
        self._offset = offset

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

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
            other,
            GrantaServerApiAggregationsPointFixedWidthHistogramAggregationDatumCriterion,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
