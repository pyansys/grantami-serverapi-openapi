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

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSchemaTablesCreateTable(ModelBase):
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
        "name": "str",
        "guid": "str",
        "is_hidden_from_browse": "bool",
        "is_hidden_from_search": "bool",
    }

    attribute_map: Dict[str, str] = {
        "name": "name",
        "guid": "guid",
        "is_hidden_from_browse": "isHiddenFromBrowse",
        "is_hidden_from_search": "isHiddenFromSearch",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        name: "str",
        guid: "Union[str, Unset_Type]" = Unset,
        is_hidden_from_browse: "Union[bool, Unset_Type]" = Unset,
        is_hidden_from_search: "Union[bool, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaTablesCreateTable - a model defined in Swagger

        Parameters
        ----------
        name: str
        guid: str, optional
        is_hidden_from_browse: bool, optional
        is_hidden_from_search: bool, optional
        """
        self._is_hidden_from_browse: Union[bool, Unset_Type] = Unset
        self._is_hidden_from_search: Union[bool, Unset_Type] = Unset
        self._name: str
        self._guid: Union[str, Unset_Type] = Unset

        if is_hidden_from_browse is not Unset:
            self.is_hidden_from_browse = is_hidden_from_browse
        if is_hidden_from_search is not Unset:
            self.is_hidden_from_search = is_hidden_from_search
        self.name = name
        if guid is not Unset:
            self.guid = guid

    @property
    def is_hidden_from_browse(self) -> "Union[bool, Unset_Type]":
        """Gets the is_hidden_from_browse of this GrantaServerApiSchemaTablesCreateTable.

        Returns
        -------
        Union[bool, Unset_Type]
            The is_hidden_from_browse of this GrantaServerApiSchemaTablesCreateTable.
        """
        return self._is_hidden_from_browse

    @is_hidden_from_browse.setter
    def is_hidden_from_browse(self, is_hidden_from_browse: "Union[bool, Unset_Type]") -> None:
        """Sets the is_hidden_from_browse of this GrantaServerApiSchemaTablesCreateTable.

        Parameters
        ----------
        is_hidden_from_browse: Union[bool, Unset_Type]
            The is_hidden_from_browse of this GrantaServerApiSchemaTablesCreateTable.
        """
        # Field is not nullable
        if is_hidden_from_browse is None:
            raise ValueError("Invalid value for 'is_hidden_from_browse', must not be 'None'")
        self._is_hidden_from_browse = is_hidden_from_browse

    @property
    def is_hidden_from_search(self) -> "Union[bool, Unset_Type]":
        """Gets the is_hidden_from_search of this GrantaServerApiSchemaTablesCreateTable.

        Returns
        -------
        Union[bool, Unset_Type]
            The is_hidden_from_search of this GrantaServerApiSchemaTablesCreateTable.
        """
        return self._is_hidden_from_search

    @is_hidden_from_search.setter
    def is_hidden_from_search(self, is_hidden_from_search: "Union[bool, Unset_Type]") -> None:
        """Sets the is_hidden_from_search of this GrantaServerApiSchemaTablesCreateTable.

        Parameters
        ----------
        is_hidden_from_search: Union[bool, Unset_Type]
            The is_hidden_from_search of this GrantaServerApiSchemaTablesCreateTable.
        """
        # Field is not nullable
        if is_hidden_from_search is None:
            raise ValueError("Invalid value for 'is_hidden_from_search', must not be 'None'")
        self._is_hidden_from_search = is_hidden_from_search

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaTablesCreateTable.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaTablesCreateTable.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaTablesCreateTable.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaTablesCreateTable.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
        self._name = name

    @property
    def guid(self) -> "Union[str, Unset_Type]":
        """Gets the guid of this GrantaServerApiSchemaTablesCreateTable.

        Returns
        -------
        Union[str, Unset_Type]
            The guid of this GrantaServerApiSchemaTablesCreateTable.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, Unset_Type]") -> None:
        """Sets the guid of this GrantaServerApiSchemaTablesCreateTable.

        Parameters
        ----------
        guid: Union[str, Unset_Type]
            The guid of this GrantaServerApiSchemaTablesCreateTable.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        self._guid = guid

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
        if not isinstance(other, GrantaServerApiSchemaTablesCreateTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
