# Copyright (C) 2023 - 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, Union  # noqa: F401

from ansys.grantami.serverapi_openapi.models.gsa_aggregation_datum_criterion import (  # noqa: F401
    GsaAggregationDatumCriterion,
)
from ansys.grantami.serverapi_openapi.models.gsa_aggregation_datum_criterion_type import (
    GsaAggregationDatumCriterionType,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaDateTimeFixedWidthHistogramAggregationDatumCriterion(GsaAggregationDatumCriterion):
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
        "type": "GsaAggregationDatumCriterionType",
        "interval": "str",
        "offset": "str",
    }

    attribute_map: Dict[str, str] = {
        "type": "type",
        "interval": "interval",
        "offset": "offset",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        type: "GsaAggregationDatumCriterionType" = GsaAggregationDatumCriterionType.DATETIMEFIXEDWIDTHHISTOGRAM,
        interval: "Union[str, None, Unset_Type]" = Unset,
        offset: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaDateTimeFixedWidthHistogramAggregationDatumCriterion - a model defined in Swagger

        Parameters
        ----------
        type: GsaAggregationDatumCriterionType
        interval: str, optional
        offset: str, optional
        """
        super().__init__(type=type)
        self._interval: Union[str, None, Unset_Type] = Unset
        self._offset: Union[str, None, Unset_Type] = Unset

        if interval is not Unset:
            self.interval = interval
        if offset is not Unset:
            self.offset = offset

    @property
    def interval(self) -> "Union[str, None, Unset_Type]":
        """Gets the interval of this GsaDateTimeFixedWidthHistogramAggregationDatumCriterion.
        Fixed size of the resulting histogram buckets, in SI time units. Must be an integer followed by one of the following units: ms (milliseconds), s (seconds), m (minutes), h (hours), d (days)

        Returns
        -------
        Union[str, None, Unset_Type]
            The interval of this GsaDateTimeFixedWidthHistogramAggregationDatumCriterion.
        """
        return self._interval

    @interval.setter
    def interval(self, interval: "Union[str, None, Unset_Type]") -> None:
        """Sets the interval of this GsaDateTimeFixedWidthHistogramAggregationDatumCriterion.
        Fixed size of the resulting histogram buckets, in SI time units. Must be an integer followed by one of the following units: ms (milliseconds), s (seconds), m (minutes), h (hours), d (days)

        Parameters
        ----------
        interval: Union[str, None, Unset_Type]
            The interval of this GsaDateTimeFixedWidthHistogramAggregationDatumCriterion.
        """
        self._interval = interval

    @property
    def offset(self) -> "Union[str, None, Unset_Type]":
        """Gets the offset of this GsaDateTimeFixedWidthHistogramAggregationDatumCriterion.
        Optional offset of the lowest bucket boundary, in SI time units. Must be an integer followed by one of the following units: ms (milliseconds), s (seconds), m (minutes), h (hours), d (days). Defaults to 0. Must be less than the interval. Negative offsets (e.g. \"-6h\") are supported

        Returns
        -------
        Union[str, None, Unset_Type]
            The offset of this GsaDateTimeFixedWidthHistogramAggregationDatumCriterion.
        """
        return self._offset

    @offset.setter
    def offset(self, offset: "Union[str, None, Unset_Type]") -> None:
        """Sets the offset of this GsaDateTimeFixedWidthHistogramAggregationDatumCriterion.
        Optional offset of the lowest bucket boundary, in SI time units. Must be an integer followed by one of the following units: ms (milliseconds), s (seconds), m (minutes), h (hours), d (days). Defaults to 0. Must be less than the interval. Negative offsets (e.g. \"-6h\") are supported

        Parameters
        ----------
        offset: Union[str, None, Unset_Type]
            The offset of this GsaDateTimeFixedWidthHistogramAggregationDatumCriterion.
        """
        self._offset = offset

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
        if not isinstance(other, GsaDateTimeFixedWidthHistogramAggregationDatumCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
