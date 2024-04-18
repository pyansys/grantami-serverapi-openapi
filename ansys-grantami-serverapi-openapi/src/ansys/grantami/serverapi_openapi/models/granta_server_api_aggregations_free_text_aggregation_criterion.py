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

from ansys.grantami.serverapi_openapi.models.granta_server_api_aggregations_aggregation_criterion import (  # noqa: F401
    GrantaServerApiAggregationsAggregationCriterion,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiAggregationsFreeTextAggregationCriterion(
    GrantaServerApiAggregationsAggregationCriterion
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
        "attributes": "GrantaServerApiValueSpecifier",
        "criterion_guid": "str",
        "local_columns": "GrantaServerApiValueSpecifier",
        "number_of_terms": "int",
        "prefix": "str",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "attributes": "attributes",
        "criterion_guid": "criterionGuid",
        "local_columns": "localColumns",
        "number_of_terms": "numberOfTerms",
        "prefix": "prefix",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {
        "attributes": "GrantaServerApiValueSpecifier",
        "localColumns": "GrantaServerApiValueSpecifier",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attributes: "Union[GrantaServerApiValueSpecifier, Unset_Type]" = Unset,
        criterion_guid: "Union[str, Unset_Type]" = Unset,
        local_columns: "Union[GrantaServerApiValueSpecifier, Unset_Type]" = Unset,
        number_of_terms: "Union[int, Unset_Type]" = Unset,
        prefix: "Union[str, None, Unset_Type]" = Unset,
        type: "str" = "text",
    ) -> None:
        """GrantaServerApiAggregationsFreeTextAggregationCriterion - a model defined in Swagger

        Parameters
        ----------
        attributes: GrantaServerApiValueSpecifier, optional
        criterion_guid: str, optional
        local_columns: GrantaServerApiValueSpecifier, optional
        number_of_terms: int, optional
        prefix: str, optional
        type: str
        """
        super().__init__()
        self._criterion_guid: Union[str, Unset_Type] = Unset
        self._number_of_terms: Union[int, Unset_Type] = Unset
        self._prefix: Union[str, None, Unset_Type] = Unset
        self._attributes: Union[GrantaServerApiValueSpecifier, Unset_Type] = Unset
        self._local_columns: Union[GrantaServerApiValueSpecifier, Unset_Type] = Unset
        self._type: str

        if criterion_guid is not Unset:
            self.criterion_guid = criterion_guid
        if number_of_terms is not Unset:
            self.number_of_terms = number_of_terms
        if prefix is not Unset:
            self.prefix = prefix
        if attributes is not Unset:
            self.attributes = attributes
        if local_columns is not Unset:
            self.local_columns = local_columns
        self.type = type

    @property
    def criterion_guid(self) -> "Union[str, Unset_Type]":
        """Gets the criterion_guid of this GrantaServerApiAggregationsFreeTextAggregationCriterion.
        A GUID to identify this free-text criterion, so that its results can be determined in the output.  For each input free-text aggregation criterion, there will be a free-text aggregation in the output  with a matching GUID.

        Returns
        -------
        Union[str, Unset_Type]
            The criterion_guid of this GrantaServerApiAggregationsFreeTextAggregationCriterion.
        """
        return self._criterion_guid

    @criterion_guid.setter
    def criterion_guid(self, criterion_guid: "Union[str, Unset_Type]") -> None:
        """Sets the criterion_guid of this GrantaServerApiAggregationsFreeTextAggregationCriterion.
        A GUID to identify this free-text criterion, so that its results can be determined in the output.  For each input free-text aggregation criterion, there will be a free-text aggregation in the output  with a matching GUID.

        Parameters
        ----------
        criterion_guid: Union[str, Unset_Type]
            The criterion_guid of this GrantaServerApiAggregationsFreeTextAggregationCriterion.
        """
        # Field is not nullable
        if criterion_guid is None:
            raise ValueError("Invalid value for 'criterion_guid', must not be 'None'")
        self._criterion_guid = criterion_guid

    @property
    def number_of_terms(self) -> "Union[int, Unset_Type]":
        """Gets the number_of_terms of this GrantaServerApiAggregationsFreeTextAggregationCriterion.
        The number of terms that should be returned

        Returns
        -------
        Union[int, Unset_Type]
            The number_of_terms of this GrantaServerApiAggregationsFreeTextAggregationCriterion.
        """
        return self._number_of_terms

    @number_of_terms.setter
    def number_of_terms(self, number_of_terms: "Union[int, Unset_Type]") -> None:
        """Sets the number_of_terms of this GrantaServerApiAggregationsFreeTextAggregationCriterion.
        The number of terms that should be returned

        Parameters
        ----------
        number_of_terms: Union[int, Unset_Type]
            The number_of_terms of this GrantaServerApiAggregationsFreeTextAggregationCriterion.
        """
        # Field is not nullable
        if number_of_terms is None:
            raise ValueError("Invalid value for 'number_of_terms', must not be 'None'")
        self._number_of_terms = number_of_terms

    @property
    def prefix(self) -> "Union[str, None, Unset_Type]":
        """Gets the prefix of this GrantaServerApiAggregationsFreeTextAggregationCriterion.

        Returns
        -------
        Union[str, None, Unset_Type]
            The prefix of this GrantaServerApiAggregationsFreeTextAggregationCriterion.
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix: "Union[str, None, Unset_Type]") -> None:
        """Sets the prefix of this GrantaServerApiAggregationsFreeTextAggregationCriterion.

        Parameters
        ----------
        prefix: Union[str, None, Unset_Type]
            The prefix of this GrantaServerApiAggregationsFreeTextAggregationCriterion.
        """
        self._prefix = prefix

    @property
    def attributes(self) -> "Union[GrantaServerApiValueSpecifier, Unset_Type]":
        """Gets the attributes of this GrantaServerApiAggregationsFreeTextAggregationCriterion.

        Returns
        -------
        Union[GrantaServerApiValueSpecifier, Unset_Type]
            The attributes of this GrantaServerApiAggregationsFreeTextAggregationCriterion.
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes: "Union[GrantaServerApiValueSpecifier, Unset_Type]") -> None:
        """Sets the attributes of this GrantaServerApiAggregationsFreeTextAggregationCriterion.

        Parameters
        ----------
        attributes: Union[GrantaServerApiValueSpecifier, Unset_Type]
            The attributes of this GrantaServerApiAggregationsFreeTextAggregationCriterion.
        """
        # Field is not nullable
        if attributes is None:
            raise ValueError("Invalid value for 'attributes', must not be 'None'")
        self._attributes = attributes

    @property
    def local_columns(self) -> "Union[GrantaServerApiValueSpecifier, Unset_Type]":
        """Gets the local_columns of this GrantaServerApiAggregationsFreeTextAggregationCriterion.

        Returns
        -------
        Union[GrantaServerApiValueSpecifier, Unset_Type]
            The local_columns of this GrantaServerApiAggregationsFreeTextAggregationCriterion.
        """
        return self._local_columns

    @local_columns.setter
    def local_columns(
        self, local_columns: "Union[GrantaServerApiValueSpecifier, Unset_Type]"
    ) -> None:
        """Sets the local_columns of this GrantaServerApiAggregationsFreeTextAggregationCriterion.

        Parameters
        ----------
        local_columns: Union[GrantaServerApiValueSpecifier, Unset_Type]
            The local_columns of this GrantaServerApiAggregationsFreeTextAggregationCriterion.
        """
        # Field is not nullable
        if local_columns is None:
            raise ValueError("Invalid value for 'local_columns', must not be 'None'")
        self._local_columns = local_columns

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiAggregationsFreeTextAggregationCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiAggregationsFreeTextAggregationCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiAggregationsFreeTextAggregationCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiAggregationsFreeTextAggregationCriterion.
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
        if not isinstance(other, GrantaServerApiAggregationsFreeTextAggregationCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
