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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaSlimTable(ModelBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes
    ----------
    swagger_types: dict[str, str]
        The key is attribute name and the value is attribute type.
    attribute_map: dict[str, str]
        The key is attribute name and the value is json key in definition.
    subtype_mapping: dict[str, str]
        The key is the unmangled property name and the value is the corresponding type.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "display_names": "dict(str, str)",
        "guid": "str",
        "is_hidden_from_browse": "bool",
        "is_hidden_from_search": "bool",
        "is_versioned": "bool",
        "name": "str",
        "table_types": "list[str]",
    }

    attribute_map: dict[str, str] = {
        "display_names": "displayNames",
        "guid": "guid",
        "is_hidden_from_browse": "isHiddenFromBrowse",
        "is_hidden_from_search": "isHiddenFromSearch",
        "is_versioned": "isVersioned",
        "name": "name",
        "table_types": "tableTypes",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        display_names: "dict[str, str]",
        guid: "str",
        is_hidden_from_browse: "bool",
        is_hidden_from_search: "bool",
        is_versioned: "bool",
        name: "str",
        table_types: "list[str]",
    ) -> None:
        """GsaSlimTable - a model defined in Swagger

        Parameters
        ----------
        display_names: dict[str, str]
        guid: str
        is_hidden_from_browse: bool
        is_hidden_from_search: bool
        is_versioned: bool
        name: str
        table_types: list[str]
        """
        self._is_hidden_from_browse: bool
        self._is_hidden_from_search: bool
        self._is_versioned: bool
        self._table_types: list[str]
        self._display_names: dict[str, str]
        self._name: str
        self._guid: str

        self.is_hidden_from_browse = is_hidden_from_browse
        self.is_hidden_from_search = is_hidden_from_search
        self.is_versioned = is_versioned
        self.table_types = table_types
        self.display_names = display_names
        self.name = name
        self.guid = guid

    @property
    def is_hidden_from_browse(self) -> "bool":
        """Gets the is_hidden_from_browse of this GsaSlimTable.

        Returns
        -------
        bool
            The is_hidden_from_browse of this GsaSlimTable.
        """
        return self._is_hidden_from_browse

    @is_hidden_from_browse.setter
    def is_hidden_from_browse(self, is_hidden_from_browse: "bool") -> None:
        """Sets the is_hidden_from_browse of this GsaSlimTable.

        Parameters
        ----------
        is_hidden_from_browse: bool
            The is_hidden_from_browse of this GsaSlimTable.
        """
        # Field is not nullable
        if is_hidden_from_browse is None:
            raise ValueError("Invalid value for 'is_hidden_from_browse', must not be 'None'")
        # Field is required
        if is_hidden_from_browse is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'is_hidden_from_browse', must not be 'Unset'")
        self._is_hidden_from_browse = is_hidden_from_browse

    @property
    def is_hidden_from_search(self) -> "bool":
        """Gets the is_hidden_from_search of this GsaSlimTable.

        Returns
        -------
        bool
            The is_hidden_from_search of this GsaSlimTable.
        """
        return self._is_hidden_from_search

    @is_hidden_from_search.setter
    def is_hidden_from_search(self, is_hidden_from_search: "bool") -> None:
        """Sets the is_hidden_from_search of this GsaSlimTable.

        Parameters
        ----------
        is_hidden_from_search: bool
            The is_hidden_from_search of this GsaSlimTable.
        """
        # Field is not nullable
        if is_hidden_from_search is None:
            raise ValueError("Invalid value for 'is_hidden_from_search', must not be 'None'")
        # Field is required
        if is_hidden_from_search is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'is_hidden_from_search', must not be 'Unset'")
        self._is_hidden_from_search = is_hidden_from_search

    @property
    def is_versioned(self) -> "bool":
        """Gets the is_versioned of this GsaSlimTable.

        Returns
        -------
        bool
            The is_versioned of this GsaSlimTable.
        """
        return self._is_versioned

    @is_versioned.setter
    def is_versioned(self, is_versioned: "bool") -> None:
        """Sets the is_versioned of this GsaSlimTable.

        Parameters
        ----------
        is_versioned: bool
            The is_versioned of this GsaSlimTable.
        """
        # Field is not nullable
        if is_versioned is None:
            raise ValueError("Invalid value for 'is_versioned', must not be 'None'")
        # Field is required
        if is_versioned is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'is_versioned', must not be 'Unset'")
        self._is_versioned = is_versioned

    @property
    def table_types(self) -> "list[str]":
        """Gets the table_types of this GsaSlimTable.

        Returns
        -------
        list[str]
            The table_types of this GsaSlimTable.
        """
        return self._table_types

    @table_types.setter
    def table_types(self, table_types: "list[str]") -> None:
        """Sets the table_types of this GsaSlimTable.

        Parameters
        ----------
        table_types: list[str]
            The table_types of this GsaSlimTable.
        """
        # Field is not nullable
        if table_types is None:
            raise ValueError("Invalid value for 'table_types', must not be 'None'")
        # Field is required
        if table_types is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'table_types', must not be 'Unset'")
        self._table_types = table_types

    @property
    def display_names(self) -> "dict[str, str]":
        """Gets the display_names of this GsaSlimTable.

        Returns
        -------
        dict[str, str]
            The display_names of this GsaSlimTable.
        """
        return self._display_names

    @display_names.setter
    def display_names(self, display_names: "dict[str, str]") -> None:
        """Sets the display_names of this GsaSlimTable.

        Parameters
        ----------
        display_names: dict[str, str]
            The display_names of this GsaSlimTable.
        """
        # Field is not nullable
        if display_names is None:
            raise ValueError("Invalid value for 'display_names', must not be 'None'")
        # Field is required
        if display_names is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'display_names', must not be 'Unset'")
        self._display_names = display_names

    @property
    def name(self) -> "str":
        """Gets the name of this GsaSlimTable.

        Returns
        -------
        str
            The name of this GsaSlimTable.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GsaSlimTable.

        Parameters
        ----------
        name: str
            The name of this GsaSlimTable.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GsaSlimTable.

        Returns
        -------
        str
            The guid of this GsaSlimTable.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GsaSlimTable.

        Parameters
        ----------
        guid: str
            The guid of this GsaSlimTable.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        # Field is required
        if guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'guid', must not be 'Unset'")
        self._guid = guid

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
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
        if not isinstance(other, GsaSlimTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
