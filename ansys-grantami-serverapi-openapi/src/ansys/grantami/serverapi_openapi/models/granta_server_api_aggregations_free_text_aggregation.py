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

from ansys.grantami.serverapi_openapi.models.granta_server_api_aggregations_aggregation import (  # noqa: F401
    GrantaServerApiAggregationsAggregation,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiAggregationsFreeTextAggregation(
    GrantaServerApiAggregationsAggregation
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
        "guid": "str",
        "terms": "list[str]",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "guid": "guid",
        "terms": "terms",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        guid: "Union[str, Unset_Type]" = Unset,
        terms: "Union[List[str], None, Unset_Type]" = Unset,
        type: "str" = "text",
    ) -> None:
        """GrantaServerApiAggregationsFreeTextAggregation - a model defined in Swagger

        Parameters
        ----------
        guid: str, optional
        terms: List[str], optional
        type: str
        """
        super().__init__()
        self._guid: Union[str, Unset_Type] = Unset
        self._terms: Union[List[str], None, Unset_Type] = Unset
        self._type: str

        if guid is not Unset:
            self.guid = guid
        if terms is not Unset:
            self.terms = terms
        self.type = type

    @property
    def guid(self) -> "Union[str, Unset_Type]":
        """Gets the guid of this GrantaServerApiAggregationsFreeTextAggregation.
        The GUID of the input aggregation criterion.

        Returns
        -------
        Union[str, Unset_Type]
            The guid of this GrantaServerApiAggregationsFreeTextAggregation.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, Unset_Type]") -> None:
        """Sets the guid of this GrantaServerApiAggregationsFreeTextAggregation.
        The GUID of the input aggregation criterion.

        Parameters
        ----------
        guid: Union[str, Unset_Type]
            The guid of this GrantaServerApiAggregationsFreeTextAggregation.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        self._guid = guid

    @property
    def terms(self) -> "Union[List[str], None, Unset_Type]":
        """Gets the terms of this GrantaServerApiAggregationsFreeTextAggregation.
        The topmost terms in the specified attributes, across all relevant records. Due to how  matches in multiple attributes are reconciled, we cannot easily provide a document count,  nor can we guarantee that the terms are perfectly correctly ordered.

        Returns
        -------
        Union[List[str], None, Unset_Type]
            The terms of this GrantaServerApiAggregationsFreeTextAggregation.
        """
        return self._terms

    @terms.setter
    def terms(self, terms: "Union[List[str], None, Unset_Type]") -> None:
        """Sets the terms of this GrantaServerApiAggregationsFreeTextAggregation.
        The topmost terms in the specified attributes, across all relevant records. Due to how  matches in multiple attributes are reconciled, we cannot easily provide a document count,  nor can we guarantee that the terms are perfectly correctly ordered.

        Parameters
        ----------
        terms: Union[List[str], None, Unset_Type]
            The terms of this GrantaServerApiAggregationsFreeTextAggregation.
        """
        self._terms = terms

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiAggregationsFreeTextAggregation.

        Returns
        -------
        str
            The type of this GrantaServerApiAggregationsFreeTextAggregation.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiAggregationsFreeTextAggregation.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiAggregationsFreeTextAggregation.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

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
        if not isinstance(other, GrantaServerApiAggregationsFreeTextAggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
