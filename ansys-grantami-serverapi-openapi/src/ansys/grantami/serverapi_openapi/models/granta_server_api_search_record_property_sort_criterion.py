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
from ansys.grantami.serverapi_openapi.models.granta_server_api_search_sort_criterion import (
    GrantaServerApiSearchSortCriterion,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSearchRecordPropertySortCriterion(
    GrantaServerApiSearchSortCriterion
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
        "_property": "GrantaServerApiSearchSearchableRecordProperty",
        "sort_direction": "GrantaServerApiSearchSortDirection",
        "sort_type": "GrantaServerApiSearchSortType",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "_property": "property",
        "sort_direction": "sortDirection",
        "sort_type": "sortType",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {
        "property": "GrantaServerApiSearchSearchableRecordProperty",
        "sortType": "GrantaServerApiSearchSortType",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        _property: "Union[GrantaServerApiSearchSearchableRecordProperty, Unset_Type]" = Unset,
        sort_direction: "Union[GrantaServerApiSearchSortDirection, Unset_Type]" = Unset,
        sort_type: "Union[GrantaServerApiSearchSortType, Unset_Type]" = Unset,
        type: "str" = "recordProperty",
    ) -> None:
        """GrantaServerApiSearchRecordPropertySortCriterion - a model defined in Swagger

        Parameters
        ----------
        _property: GrantaServerApiSearchSearchableRecordProperty, optional
        sort_direction: GrantaServerApiSearchSortDirection, optional
        sort_type: GrantaServerApiSearchSortType, optional
        type: str
        """
        super().__init__(sort_direction=sort_direction)
        self.__property: Union[
            GrantaServerApiSearchSearchableRecordProperty, Unset_Type
        ] = Unset
        self._sort_type: Union[GrantaServerApiSearchSortType, Unset_Type] = Unset
        self._type: str

        if _property is not Unset:
            self._property = _property
        if sort_type is not Unset:
            self.sort_type = sort_type
        self.type = type

    @property
    def _property(
        self,
    ) -> "Union[GrantaServerApiSearchSearchableRecordProperty, Unset_Type]":
        """Gets the _property of this GrantaServerApiSearchRecordPropertySortCriterion.

        Returns
        -------
        Union[GrantaServerApiSearchSearchableRecordProperty, Unset_Type]
            The _property of this GrantaServerApiSearchRecordPropertySortCriterion.
        """
        return self.__property

    @_property.setter
    def _property(
        self,
        _property: "Union[GrantaServerApiSearchSearchableRecordProperty, Unset_Type]",
    ) -> None:
        """Sets the _property of this GrantaServerApiSearchRecordPropertySortCriterion.

        Parameters
        ----------
        _property: Union[GrantaServerApiSearchSearchableRecordProperty, Unset_Type]
            The _property of this GrantaServerApiSearchRecordPropertySortCriterion.
        """
        # Field is not nullable
        if _property is None:
            raise ValueError("Invalid value for '_property', must not be 'None'")
        self.__property = _property

    @property
    def sort_type(self) -> "Union[GrantaServerApiSearchSortType, Unset_Type]":
        """Gets the sort_type of this GrantaServerApiSearchRecordPropertySortCriterion.

        Returns
        -------
        Union[GrantaServerApiSearchSortType, Unset_Type]
            The sort_type of this GrantaServerApiSearchRecordPropertySortCriterion.
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(
        self, sort_type: "Union[GrantaServerApiSearchSortType, Unset_Type]"
    ) -> None:
        """Sets the sort_type of this GrantaServerApiSearchRecordPropertySortCriterion.

        Parameters
        ----------
        sort_type: Union[GrantaServerApiSearchSortType, Unset_Type]
            The sort_type of this GrantaServerApiSearchRecordPropertySortCriterion.
        """
        # Field is not nullable
        if sort_type is None:
            raise ValueError("Invalid value for 'sort_type', must not be 'None'")
        self._sort_type = sort_type

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchRecordPropertySortCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchRecordPropertySortCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchRecordPropertySortCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchRecordPropertySortCriterion.
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
        if not isinstance(other, GrantaServerApiSearchRecordPropertySortCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
