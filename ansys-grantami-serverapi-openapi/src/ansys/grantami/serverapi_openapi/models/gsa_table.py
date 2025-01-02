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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaTable(ModelBase):
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
        "layouts": "list[GsaSlimLayout]",
        "name": "str",
        "subsets": "list[GsaSlimSubset]",
        "table_types": "list[str]",
        "version_state": "GsaVersionState",
        "default_layout": "GsaSlimLayout",
        "default_subset": "GsaSlimSubset",
    }

    attribute_map: dict[str, str] = {
        "display_names": "displayNames",
        "guid": "guid",
        "is_hidden_from_browse": "isHiddenFromBrowse",
        "is_hidden_from_search": "isHiddenFromSearch",
        "is_versioned": "isVersioned",
        "layouts": "layouts",
        "name": "name",
        "subsets": "subsets",
        "table_types": "tableTypes",
        "version_state": "versionState",
        "default_layout": "defaultLayout",
        "default_subset": "defaultSubset",
    }

    subtype_mapping: dict[str, str] = {
        "defaultSubset": "GsaSlimSubset",
        "subsets": "GsaSlimSubset",
        "defaultLayout": "GsaSlimLayout",
        "layouts": "GsaSlimLayout",
        "versionState": "GsaVersionState",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        display_names: "dict[str, str]",
        guid: "str",
        is_hidden_from_browse: "bool",
        is_hidden_from_search: "bool",
        is_versioned: "bool",
        layouts: "list[GsaSlimLayout]",
        name: "str",
        subsets: "list[GsaSlimSubset]",
        table_types: "list[str]",
        version_state: "GsaVersionState",
        default_layout: "Union[GsaSlimLayout, Unset_Type]" = Unset,
        default_subset: "Union[GsaSlimSubset, Unset_Type]" = Unset,
    ) -> None:
        """GsaTable - a model defined in Swagger

        Parameters
        ----------
        display_names: dict[str, str]
        guid: str
        is_hidden_from_browse: bool
        is_hidden_from_search: bool
        is_versioned: bool
        layouts: list[GsaSlimLayout]
        name: str
        subsets: list[GsaSlimSubset]
        table_types: list[str]
        version_state: GsaVersionState
        default_layout: GsaSlimLayout, optional
        default_subset: GsaSlimSubset, optional
        """
        self._default_subset: Union[GsaSlimSubset, Unset_Type] = Unset
        self._subsets: list[GsaSlimSubset]
        self._default_layout: Union[GsaSlimLayout, Unset_Type] = Unset
        self._layouts: list[GsaSlimLayout]
        self._version_state: GsaVersionState
        self._is_hidden_from_browse: bool
        self._is_hidden_from_search: bool
        self._is_versioned: bool
        self._table_types: list[str]
        self._display_names: dict[str, str]
        self._name: str
        self._guid: str

        if default_subset is not Unset:
            self.default_subset = default_subset
        self.subsets = subsets
        if default_layout is not Unset:
            self.default_layout = default_layout
        self.layouts = layouts
        self.version_state = version_state
        self.is_hidden_from_browse = is_hidden_from_browse
        self.is_hidden_from_search = is_hidden_from_search
        self.is_versioned = is_versioned
        self.table_types = table_types
        self.display_names = display_names
        self.name = name
        self.guid = guid

    @property
    def default_subset(self) -> "Union[GsaSlimSubset, Unset_Type]":
        """Gets the default_subset of this GsaTable.

        Returns
        -------
        Union[GsaSlimSubset, Unset_Type]
            The default_subset of this GsaTable.
        """
        return self._default_subset

    @default_subset.setter
    def default_subset(self, default_subset: "Union[GsaSlimSubset, Unset_Type]") -> None:
        """Sets the default_subset of this GsaTable.

        Parameters
        ----------
        default_subset: Union[GsaSlimSubset, Unset_Type]
            The default_subset of this GsaTable.
        """
        # Field is not nullable
        if default_subset is None:
            raise ValueError("Invalid value for 'default_subset', must not be 'None'")
        self._default_subset = default_subset

    @property
    def subsets(self) -> "list[GsaSlimSubset]":
        """Gets the subsets of this GsaTable.

        Returns
        -------
        list[GsaSlimSubset]
            The subsets of this GsaTable.
        """
        return self._subsets

    @subsets.setter
    def subsets(self, subsets: "list[GsaSlimSubset]") -> None:
        """Sets the subsets of this GsaTable.

        Parameters
        ----------
        subsets: list[GsaSlimSubset]
            The subsets of this GsaTable.
        """
        # Field is not nullable
        if subsets is None:
            raise ValueError("Invalid value for 'subsets', must not be 'None'")
        # Field is required
        if subsets is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'subsets', must not be 'Unset'")
        self._subsets = subsets

    @property
    def default_layout(self) -> "Union[GsaSlimLayout, Unset_Type]":
        """Gets the default_layout of this GsaTable.

        Returns
        -------
        Union[GsaSlimLayout, Unset_Type]
            The default_layout of this GsaTable.
        """
        return self._default_layout

    @default_layout.setter
    def default_layout(self, default_layout: "Union[GsaSlimLayout, Unset_Type]") -> None:
        """Sets the default_layout of this GsaTable.

        Parameters
        ----------
        default_layout: Union[GsaSlimLayout, Unset_Type]
            The default_layout of this GsaTable.
        """
        # Field is not nullable
        if default_layout is None:
            raise ValueError("Invalid value for 'default_layout', must not be 'None'")
        self._default_layout = default_layout

    @property
    def layouts(self) -> "list[GsaSlimLayout]":
        """Gets the layouts of this GsaTable.

        Returns
        -------
        list[GsaSlimLayout]
            The layouts of this GsaTable.
        """
        return self._layouts

    @layouts.setter
    def layouts(self, layouts: "list[GsaSlimLayout]") -> None:
        """Sets the layouts of this GsaTable.

        Parameters
        ----------
        layouts: list[GsaSlimLayout]
            The layouts of this GsaTable.
        """
        # Field is not nullable
        if layouts is None:
            raise ValueError("Invalid value for 'layouts', must not be 'None'")
        # Field is required
        if layouts is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'layouts', must not be 'Unset'")
        self._layouts = layouts

    @property
    def version_state(self) -> "GsaVersionState":
        """Gets the version_state of this GsaTable.

        Returns
        -------
        GsaVersionState
            The version_state of this GsaTable.
        """
        return self._version_state

    @version_state.setter
    def version_state(self, version_state: "GsaVersionState") -> None:
        """Sets the version_state of this GsaTable.

        Parameters
        ----------
        version_state: GsaVersionState
            The version_state of this GsaTable.
        """
        # Field is not nullable
        if version_state is None:
            raise ValueError("Invalid value for 'version_state', must not be 'None'")
        # Field is required
        if version_state is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'version_state', must not be 'Unset'")
        self._version_state = version_state

    @property
    def is_hidden_from_browse(self) -> "bool":
        """Gets the is_hidden_from_browse of this GsaTable.

        Returns
        -------
        bool
            The is_hidden_from_browse of this GsaTable.
        """
        return self._is_hidden_from_browse

    @is_hidden_from_browse.setter
    def is_hidden_from_browse(self, is_hidden_from_browse: "bool") -> None:
        """Sets the is_hidden_from_browse of this GsaTable.

        Parameters
        ----------
        is_hidden_from_browse: bool
            The is_hidden_from_browse of this GsaTable.
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
        """Gets the is_hidden_from_search of this GsaTable.

        Returns
        -------
        bool
            The is_hidden_from_search of this GsaTable.
        """
        return self._is_hidden_from_search

    @is_hidden_from_search.setter
    def is_hidden_from_search(self, is_hidden_from_search: "bool") -> None:
        """Sets the is_hidden_from_search of this GsaTable.

        Parameters
        ----------
        is_hidden_from_search: bool
            The is_hidden_from_search of this GsaTable.
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
        """Gets the is_versioned of this GsaTable.

        Returns
        -------
        bool
            The is_versioned of this GsaTable.
        """
        return self._is_versioned

    @is_versioned.setter
    def is_versioned(self, is_versioned: "bool") -> None:
        """Sets the is_versioned of this GsaTable.

        Parameters
        ----------
        is_versioned: bool
            The is_versioned of this GsaTable.
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
        """Gets the table_types of this GsaTable.

        Returns
        -------
        list[str]
            The table_types of this GsaTable.
        """
        return self._table_types

    @table_types.setter
    def table_types(self, table_types: "list[str]") -> None:
        """Sets the table_types of this GsaTable.

        Parameters
        ----------
        table_types: list[str]
            The table_types of this GsaTable.
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
        """Gets the display_names of this GsaTable.

        Returns
        -------
        dict[str, str]
            The display_names of this GsaTable.
        """
        return self._display_names

    @display_names.setter
    def display_names(self, display_names: "dict[str, str]") -> None:
        """Sets the display_names of this GsaTable.

        Parameters
        ----------
        display_names: dict[str, str]
            The display_names of this GsaTable.
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
        """Gets the name of this GsaTable.

        Returns
        -------
        str
            The name of this GsaTable.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GsaTable.

        Parameters
        ----------
        name: str
            The name of this GsaTable.
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
        """Gets the guid of this GsaTable.

        Returns
        -------
        str
            The guid of this GsaTable.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GsaTable.

        Parameters
        ----------
        guid: str
            The guid of this GsaTable.
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
        if not isinstance(other, GsaTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
