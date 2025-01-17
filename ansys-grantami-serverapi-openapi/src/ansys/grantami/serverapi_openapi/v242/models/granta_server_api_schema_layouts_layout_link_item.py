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

from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_layouts_layout_item import (  # noqa: F401
    GrantaServerApiSchemaLayoutsLayoutItem,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSchemaLayoutsLayoutLinkItem(GrantaServerApiSchemaLayoutsLayoutItem):
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
        "forwards": "bool",
        "guid": "str",
        "link_type": "GrantaServerApiSchemaLayoutsLayoutItemLinkType",
        "name": "str",
        "target_table": "str",
        "underlying_entity_guid": "str",
        "item_type": "str",
        "next_link": "GrantaServerApiSchemaLayoutsLayoutLinkItem",
        "target_database": "str",
        "target_database_version": "str",
    }

    attribute_map: Dict[str, str] = {
        "forwards": "forwards",
        "guid": "guid",
        "link_type": "linkType",
        "name": "name",
        "target_table": "targetTable",
        "underlying_entity_guid": "underlyingEntityGuid",
        "item_type": "itemType",
        "next_link": "nextLink",
        "target_database": "targetDatabase",
        "target_database_version": "targetDatabaseVersion",
    }

    subtype_mapping: Dict[str, str] = {
        "linkType": "GrantaServerApiSchemaLayoutsLayoutItemLinkType",
        "nextLink": "GrantaServerApiSchemaLayoutsLayoutLinkItem",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        forwards: "bool",
        guid: "str",
        link_type: "GrantaServerApiSchemaLayoutsLayoutItemLinkType",
        name: "str",
        target_table: "str",
        underlying_entity_guid: "str",
        item_type: "str" = "link",
        next_link: "Union[GrantaServerApiSchemaLayoutsLayoutLinkItem, Unset_Type]" = Unset,
        target_database: "Union[str, None, Unset_Type]" = Unset,
        target_database_version: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaLayoutsLayoutLinkItem - a model defined in Swagger

        Parameters
        ----------
        forwards: bool
        guid: str
        link_type: GrantaServerApiSchemaLayoutsLayoutItemLinkType
        name: str
        target_table: str
        underlying_entity_guid: str
        item_type: str
        next_link: GrantaServerApiSchemaLayoutsLayoutLinkItem, optional
        target_database: str, optional
        target_database_version: str, optional
        """
        super().__init__(guid=guid, name=name, underlying_entity_guid=underlying_entity_guid)
        self._item_type: str
        self._link_type: GrantaServerApiSchemaLayoutsLayoutItemLinkType
        self._target_database: Union[str, None, Unset_Type] = Unset
        self._target_database_version: Union[str, None, Unset_Type] = Unset
        self._target_table: str
        self._forwards: bool
        self._next_link: Union[GrantaServerApiSchemaLayoutsLayoutLinkItem, Unset_Type] = Unset

        self.item_type = item_type
        self.link_type = link_type
        if target_database is not Unset:
            self.target_database = target_database
        if target_database_version is not Unset:
            self.target_database_version = target_database_version
        self.target_table = target_table
        self.forwards = forwards
        if next_link is not Unset:
            self.next_link = next_link

    @property
    def item_type(self) -> "str":
        """Gets the item_type of this GrantaServerApiSchemaLayoutsLayoutLinkItem.

        Returns
        -------
        str
            The item_type of this GrantaServerApiSchemaLayoutsLayoutLinkItem.
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type: "str") -> None:
        """Sets the item_type of this GrantaServerApiSchemaLayoutsLayoutLinkItem.

        Parameters
        ----------
        item_type: str
            The item_type of this GrantaServerApiSchemaLayoutsLayoutLinkItem.
        """
        # Field is not nullable
        if item_type is None:
            raise ValueError("Invalid value for 'item_type', must not be 'None'")
        # Field is required
        if item_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'item_type', must not be 'Unset'")
        self._item_type = item_type

    @property
    def link_type(self) -> "GrantaServerApiSchemaLayoutsLayoutItemLinkType":
        """Gets the link_type of this GrantaServerApiSchemaLayoutsLayoutLinkItem.

        Returns
        -------
        GrantaServerApiSchemaLayoutsLayoutItemLinkType
            The link_type of this GrantaServerApiSchemaLayoutsLayoutLinkItem.
        """
        return self._link_type

    @link_type.setter
    def link_type(self, link_type: "GrantaServerApiSchemaLayoutsLayoutItemLinkType") -> None:
        """Sets the link_type of this GrantaServerApiSchemaLayoutsLayoutLinkItem.

        Parameters
        ----------
        link_type: GrantaServerApiSchemaLayoutsLayoutItemLinkType
            The link_type of this GrantaServerApiSchemaLayoutsLayoutLinkItem.
        """
        # Field is not nullable
        if link_type is None:
            raise ValueError("Invalid value for 'link_type', must not be 'None'")
        # Field is required
        if link_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'link_type', must not be 'Unset'")
        self._link_type = link_type

    @property
    def target_database(self) -> "Union[str, None, Unset_Type]":
        """Gets the target_database of this GrantaServerApiSchemaLayoutsLayoutLinkItem.

        Returns
        -------
        Union[str, None, Unset_Type]
            The target_database of this GrantaServerApiSchemaLayoutsLayoutLinkItem.
        """
        return self._target_database

    @target_database.setter
    def target_database(self, target_database: "Union[str, None, Unset_Type]") -> None:
        """Sets the target_database of this GrantaServerApiSchemaLayoutsLayoutLinkItem.

        Parameters
        ----------
        target_database: Union[str, None, Unset_Type]
            The target_database of this GrantaServerApiSchemaLayoutsLayoutLinkItem.
        """
        self._target_database = target_database

    @property
    def target_database_version(self) -> "Union[str, None, Unset_Type]":
        """Gets the target_database_version of this GrantaServerApiSchemaLayoutsLayoutLinkItem.

        Returns
        -------
        Union[str, None, Unset_Type]
            The target_database_version of this GrantaServerApiSchemaLayoutsLayoutLinkItem.
        """
        return self._target_database_version

    @target_database_version.setter
    def target_database_version(
        self, target_database_version: "Union[str, None, Unset_Type]"
    ) -> None:
        """Sets the target_database_version of this GrantaServerApiSchemaLayoutsLayoutLinkItem.

        Parameters
        ----------
        target_database_version: Union[str, None, Unset_Type]
            The target_database_version of this GrantaServerApiSchemaLayoutsLayoutLinkItem.
        """
        self._target_database_version = target_database_version

    @property
    def target_table(self) -> "str":
        """Gets the target_table of this GrantaServerApiSchemaLayoutsLayoutLinkItem.

        Returns
        -------
        str
            The target_table of this GrantaServerApiSchemaLayoutsLayoutLinkItem.
        """
        return self._target_table

    @target_table.setter
    def target_table(self, target_table: "str") -> None:
        """Sets the target_table of this GrantaServerApiSchemaLayoutsLayoutLinkItem.

        Parameters
        ----------
        target_table: str
            The target_table of this GrantaServerApiSchemaLayoutsLayoutLinkItem.
        """
        # Field is not nullable
        if target_table is None:
            raise ValueError("Invalid value for 'target_table', must not be 'None'")
        # Field is required
        if target_table is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'target_table', must not be 'Unset'")
        self._target_table = target_table

    @property
    def forwards(self) -> "bool":
        """Gets the forwards of this GrantaServerApiSchemaLayoutsLayoutLinkItem.

        Returns
        -------
        bool
            The forwards of this GrantaServerApiSchemaLayoutsLayoutLinkItem.
        """
        return self._forwards

    @forwards.setter
    def forwards(self, forwards: "bool") -> None:
        """Sets the forwards of this GrantaServerApiSchemaLayoutsLayoutLinkItem.

        Parameters
        ----------
        forwards: bool
            The forwards of this GrantaServerApiSchemaLayoutsLayoutLinkItem.
        """
        # Field is not nullable
        if forwards is None:
            raise ValueError("Invalid value for 'forwards', must not be 'None'")
        # Field is required
        if forwards is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'forwards', must not be 'Unset'")
        self._forwards = forwards

    @property
    def next_link(self) -> "Union[GrantaServerApiSchemaLayoutsLayoutLinkItem, Unset_Type]":
        """Gets the next_link of this GrantaServerApiSchemaLayoutsLayoutLinkItem.

        Returns
        -------
        Union[GrantaServerApiSchemaLayoutsLayoutLinkItem, Unset_Type]
            The next_link of this GrantaServerApiSchemaLayoutsLayoutLinkItem.
        """
        return self._next_link

    @next_link.setter
    def next_link(
        self, next_link: "Union[GrantaServerApiSchemaLayoutsLayoutLinkItem, Unset_Type]"
    ) -> None:
        """Sets the next_link of this GrantaServerApiSchemaLayoutsLayoutLinkItem.

        Parameters
        ----------
        next_link: Union[GrantaServerApiSchemaLayoutsLayoutLinkItem, Unset_Type]
            The next_link of this GrantaServerApiSchemaLayoutsLayoutLinkItem.
        """
        # Field is not nullable
        if next_link is None:
            raise ValueError("Invalid value for 'next_link', must not be 'None'")
        self._next_link = next_link

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
        if not isinstance(other, GrantaServerApiSchemaLayoutsLayoutLinkItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
