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
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, Union  # noqa: F401

from ansys.grantami.serverapi_openapi.models.granta_server_api_aggregations_attribute_aggregation import (  # noqa: F401
    GrantaServerApiAggregationsAttributeAggregation,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiAggregationsAttributeValueAggregation(
    GrantaServerApiAggregationsAttributeAggregation
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
        "aggregation_datum": "GrantaServerApiAggregationsAggregationDatum",
        "attribute_aggregation_type": "str",
        "attribute_guid": "str",
        "attribute_identity": "int",
        "count": "int",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "aggregation_datum": "aggregationDatum",
        "attribute_aggregation_type": "attributeAggregationType",
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "count": "count",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {
        "aggregationDatum": "GrantaServerApiAggregationsAggregationDatum",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        aggregation_datum: "Union[GrantaServerApiAggregationsAggregationDatum, Unset_Type]" = Unset,
        attribute_aggregation_type: "str" = "value",
        attribute_guid: "Union[str, None, Unset_Type]" = Unset,
        attribute_identity: "Union[int, None, Unset_Type]" = Unset,
        count: "Union[int, Unset_Type]" = Unset,
        type: "str" = "attribute",
    ) -> None:
        """GrantaServerApiAggregationsAttributeValueAggregation - a model defined in Swagger

        Parameters
        ----------
        aggregation_datum: GrantaServerApiAggregationsAggregationDatum, optional
        attribute_aggregation_type: str
        attribute_guid: str, optional
        attribute_identity: int, optional
        count: int, optional
        type: str
        """
        super().__init__(
            attribute_guid=attribute_guid,
            attribute_identity=attribute_identity,
            count=count,
            type=type,
        )
        self._attribute_aggregation_type: str
        self._aggregation_datum: Union[GrantaServerApiAggregationsAggregationDatum, Unset_Type] = (
            Unset
        )

        self.attribute_aggregation_type = attribute_aggregation_type
        if aggregation_datum is not Unset:
            self.aggregation_datum = aggregation_datum

    @property
    def attribute_aggregation_type(self) -> "str":
        """Gets the attribute_aggregation_type of this GrantaServerApiAggregationsAttributeValueAggregation.

        Returns
        -------
        str
            The attribute_aggregation_type of this GrantaServerApiAggregationsAttributeValueAggregation.
        """
        return self._attribute_aggregation_type

    @attribute_aggregation_type.setter
    def attribute_aggregation_type(self, attribute_aggregation_type: "str") -> None:
        """Sets the attribute_aggregation_type of this GrantaServerApiAggregationsAttributeValueAggregation.

        Parameters
        ----------
        attribute_aggregation_type: str
            The attribute_aggregation_type of this GrantaServerApiAggregationsAttributeValueAggregation.
        """
        # Field is not nullable
        if attribute_aggregation_type is None:
            raise ValueError("Invalid value for 'attribute_aggregation_type', must not be 'None'")
        # Field is required
        if attribute_aggregation_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'attribute_aggregation_type', must not be 'Unset'")
        self._attribute_aggregation_type = attribute_aggregation_type

    @property
    def aggregation_datum(self) -> "Union[GrantaServerApiAggregationsAggregationDatum, Unset_Type]":
        """Gets the aggregation_datum of this GrantaServerApiAggregationsAttributeValueAggregation.

        Returns
        -------
        Union[GrantaServerApiAggregationsAggregationDatum, Unset_Type]
            The aggregation_datum of this GrantaServerApiAggregationsAttributeValueAggregation.
        """
        return self._aggregation_datum

    @aggregation_datum.setter
    def aggregation_datum(
        self, aggregation_datum: "Union[GrantaServerApiAggregationsAggregationDatum, Unset_Type]"
    ) -> None:
        """Sets the aggregation_datum of this GrantaServerApiAggregationsAttributeValueAggregation.

        Parameters
        ----------
        aggregation_datum: Union[GrantaServerApiAggregationsAggregationDatum, Unset_Type]
            The aggregation_datum of this GrantaServerApiAggregationsAttributeValueAggregation.
        """
        # Field is not nullable
        if aggregation_datum is None:
            raise ValueError("Invalid value for 'aggregation_datum', must not be 'None'")
        self._aggregation_datum = aggregation_datum

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
        if not isinstance(other, GrantaServerApiAggregationsAttributeValueAggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
