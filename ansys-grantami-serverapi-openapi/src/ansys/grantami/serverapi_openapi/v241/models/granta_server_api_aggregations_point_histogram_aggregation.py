# Copyright (C) 2023 - 2025 ANSYS, Inc. and/or its affiliates.
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
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from ansys.grantami.serverapi_openapi.models.granta_server_api_aggregations_aggregation_datum import (  # noqa: F401
    GrantaServerApiAggregationsAggregationDatum,
)

from . import ModelBase

if TYPE_CHECKING:
    from . import *


class GrantaServerApiAggregationsPointHistogramAggregation(
    GrantaServerApiAggregationsAggregationDatum
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
        "datum_type": "str",
        "histogram": "GrantaServerApiAggregationsHistogram",
    }

    attribute_map = {
        "datum_type": "datumType",
        "histogram": "histogram",
    }

    subtype_mapping = {
        "histogram": "GrantaServerApiAggregationsHistogram",
    }

    discriminator = None

    def __init__(
        self,
        *,
        datum_type: "str" = "pointHistogram",
        histogram: "Optional[GrantaServerApiAggregationsHistogram]" = None,
    ) -> None:
        """GrantaServerApiAggregationsPointHistogramAggregation - a model defined in Swagger

        Parameters
        ----------
            datum_type: str
            histogram: GrantaServerApiAggregationsHistogram, optional
        """
        super().__init__()
        self._histogram = None
        self._datum_type = None

        if histogram is not None:
            self.histogram = histogram
        self.datum_type = datum_type

    @property
    def histogram(self) -> "GrantaServerApiAggregationsHistogram":
        """Gets the histogram of this GrantaServerApiAggregationsPointHistogramAggregation.

        Returns
        -------
        GrantaServerApiAggregationsHistogram
            The histogram of this GrantaServerApiAggregationsPointHistogramAggregation.
        """
        return self._histogram

    @histogram.setter
    def histogram(self, histogram: "GrantaServerApiAggregationsHistogram") -> None:
        """Sets the histogram of this GrantaServerApiAggregationsPointHistogramAggregation.

        Parameters
        ----------
        histogram: GrantaServerApiAggregationsHistogram
            The histogram of this GrantaServerApiAggregationsPointHistogramAggregation.
        """
        self._histogram = histogram

    @property
    def datum_type(self) -> "str":
        """Gets the datum_type of this GrantaServerApiAggregationsPointHistogramAggregation.

        Returns
        -------
        str
            The datum_type of this GrantaServerApiAggregationsPointHistogramAggregation.
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type: "str") -> None:
        """Sets the datum_type of this GrantaServerApiAggregationsPointHistogramAggregation.

        Parameters
        ----------
        datum_type: str
            The datum_type of this GrantaServerApiAggregationsPointHistogramAggregation.
        """
        if datum_type is None:
            raise ValueError("Invalid value for 'datum_type', must not be 'None'")
        self._datum_type = datum_type

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
        if not isinstance(other, GrantaServerApiAggregationsPointHistogramAggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
