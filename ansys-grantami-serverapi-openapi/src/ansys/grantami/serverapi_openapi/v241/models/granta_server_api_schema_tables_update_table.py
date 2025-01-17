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

from . import ModelBase

if TYPE_CHECKING:
    from . import *


class GrantaServerApiSchemaTablesUpdateTable(ModelBase):
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
        "default_layout_guid": "str",
        "default_subset_guid": "str",
        "guid": "str",
        "is_hidden_from_browse": "bool",
        "is_hidden_from_search": "bool",
        "name": "str",
    }

    attribute_map = {
        "default_layout_guid": "defaultLayoutGuid",
        "default_subset_guid": "defaultSubsetGuid",
        "guid": "guid",
        "is_hidden_from_browse": "isHiddenFromBrowse",
        "is_hidden_from_search": "isHiddenFromSearch",
        "name": "name",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        default_layout_guid: "Optional[str]" = None,
        default_subset_guid: "Optional[str]" = None,
        guid: "Optional[str]" = None,
        is_hidden_from_browse: "Optional[bool]" = None,
        is_hidden_from_search: "Optional[bool]" = None,
        name: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiSchemaTablesUpdateTable - a model defined in Swagger

        Parameters
        ----------
            default_layout_guid: str, optional
            default_subset_guid: str, optional
            guid: str, optional
            is_hidden_from_browse: bool, optional
            is_hidden_from_search: bool, optional
            name: str, optional
        """
        self._is_hidden_from_browse = None
        self._is_hidden_from_search = None
        self._default_subset_guid = None
        self._default_layout_guid = None
        self._name = None
        self._guid = None

        if is_hidden_from_browse is not None:
            self.is_hidden_from_browse = is_hidden_from_browse
        if is_hidden_from_search is not None:
            self.is_hidden_from_search = is_hidden_from_search
        if default_subset_guid is not None:
            self.default_subset_guid = default_subset_guid
        if default_layout_guid is not None:
            self.default_layout_guid = default_layout_guid
        if name is not None:
            self.name = name
        if guid is not None:
            self.guid = guid

    @property
    def is_hidden_from_browse(self) -> "bool":
        """Gets the is_hidden_from_browse of this GrantaServerApiSchemaTablesUpdateTable.

        Returns
        -------
        bool
            The is_hidden_from_browse of this GrantaServerApiSchemaTablesUpdateTable.
        """
        return self._is_hidden_from_browse

    @is_hidden_from_browse.setter
    def is_hidden_from_browse(self, is_hidden_from_browse: "bool") -> None:
        """Sets the is_hidden_from_browse of this GrantaServerApiSchemaTablesUpdateTable.

        Parameters
        ----------
        is_hidden_from_browse: bool
            The is_hidden_from_browse of this GrantaServerApiSchemaTablesUpdateTable.
        """
        self._is_hidden_from_browse = is_hidden_from_browse

    @property
    def is_hidden_from_search(self) -> "bool":
        """Gets the is_hidden_from_search of this GrantaServerApiSchemaTablesUpdateTable.

        Returns
        -------
        bool
            The is_hidden_from_search of this GrantaServerApiSchemaTablesUpdateTable.
        """
        return self._is_hidden_from_search

    @is_hidden_from_search.setter
    def is_hidden_from_search(self, is_hidden_from_search: "bool") -> None:
        """Sets the is_hidden_from_search of this GrantaServerApiSchemaTablesUpdateTable.

        Parameters
        ----------
        is_hidden_from_search: bool
            The is_hidden_from_search of this GrantaServerApiSchemaTablesUpdateTable.
        """
        self._is_hidden_from_search = is_hidden_from_search

    @property
    def default_subset_guid(self) -> "str":
        """Gets the default_subset_guid of this GrantaServerApiSchemaTablesUpdateTable.

        Returns
        -------
        str
            The default_subset_guid of this GrantaServerApiSchemaTablesUpdateTable.
        """
        return self._default_subset_guid

    @default_subset_guid.setter
    def default_subset_guid(self, default_subset_guid: "str") -> None:
        """Sets the default_subset_guid of this GrantaServerApiSchemaTablesUpdateTable.

        Parameters
        ----------
        default_subset_guid: str
            The default_subset_guid of this GrantaServerApiSchemaTablesUpdateTable.
        """
        self._default_subset_guid = default_subset_guid

    @property
    def default_layout_guid(self) -> "str":
        """Gets the default_layout_guid of this GrantaServerApiSchemaTablesUpdateTable.

        Returns
        -------
        str
            The default_layout_guid of this GrantaServerApiSchemaTablesUpdateTable.
        """
        return self._default_layout_guid

    @default_layout_guid.setter
    def default_layout_guid(self, default_layout_guid: "str") -> None:
        """Sets the default_layout_guid of this GrantaServerApiSchemaTablesUpdateTable.

        Parameters
        ----------
        default_layout_guid: str
            The default_layout_guid of this GrantaServerApiSchemaTablesUpdateTable.
        """
        self._default_layout_guid = default_layout_guid

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaTablesUpdateTable.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaTablesUpdateTable.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaTablesUpdateTable.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaTablesUpdateTable.
        """
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaTablesUpdateTable.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaTablesUpdateTable.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaTablesUpdateTable.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaTablesUpdateTable.
        """
        self._guid = guid

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
        if not isinstance(other, GrantaServerApiSchemaTablesUpdateTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
