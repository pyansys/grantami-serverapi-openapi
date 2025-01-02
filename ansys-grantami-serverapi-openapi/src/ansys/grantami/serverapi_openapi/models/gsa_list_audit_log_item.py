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


class GsaListAuditLogItem(ModelBase):
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
        "action": "GsaListAction",
        "initiating_user": "GsaListsUserOrGroup",
        "list_identifier": "str",
        "list_item_affected": "GsaListItem",
        "timestamp": "datetime",
        "user_or_group_affected": "GsaListsUserOrGroup",
    }

    attribute_map: dict[str, str] = {
        "action": "action",
        "initiating_user": "initiatingUser",
        "list_identifier": "listIdentifier",
        "list_item_affected": "listItemAffected",
        "timestamp": "timestamp",
        "user_or_group_affected": "userOrGroupAffected",
    }

    subtype_mapping: dict[str, str] = {
        "initiatingUser": "GsaListsUserOrGroup",
        "userOrGroupAffected": "GsaListsUserOrGroup",
        "listItemAffected": "GsaListItem",
        "action": "GsaListAction",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        action: "Union[GsaListAction, Unset_Type]" = Unset,
        initiating_user: "Union[GsaListsUserOrGroup, Unset_Type]" = Unset,
        list_identifier: "Union[str, Unset_Type]" = Unset,
        list_item_affected: "Union[GsaListItem, Unset_Type]" = Unset,
        timestamp: "Union[datetime, Unset_Type]" = Unset,
        user_or_group_affected: "Union[GsaListsUserOrGroup, Unset_Type]" = Unset,
    ) -> None:
        """GsaListAuditLogItem - a model defined in Swagger

        Parameters
        ----------
        action: GsaListAction, optional
        initiating_user: GsaListsUserOrGroup, optional
        list_identifier: str, optional
        list_item_affected: GsaListItem, optional
        timestamp: datetime, optional
        user_or_group_affected: GsaListsUserOrGroup, optional
        """
        self._list_identifier: Union[str, Unset_Type] = Unset
        self._initiating_user: Union[GsaListsUserOrGroup, Unset_Type] = Unset
        self._user_or_group_affected: Union[GsaListsUserOrGroup, Unset_Type] = Unset
        self._list_item_affected: Union[GsaListItem, Unset_Type] = Unset
        self._action: Union[GsaListAction, Unset_Type] = Unset
        self._timestamp: Union[datetime, Unset_Type] = Unset

        if list_identifier is not Unset:
            self.list_identifier = list_identifier
        if initiating_user is not Unset:
            self.initiating_user = initiating_user
        if user_or_group_affected is not Unset:
            self.user_or_group_affected = user_or_group_affected
        if list_item_affected is not Unset:
            self.list_item_affected = list_item_affected
        if action is not Unset:
            self.action = action
        if timestamp is not Unset:
            self.timestamp = timestamp

    @property
    def list_identifier(self) -> "Union[str, Unset_Type]":
        """Gets the list_identifier of this GsaListAuditLogItem.
        The identifier of the list that the action was performed on

        Returns
        -------
        Union[str, Unset_Type]
            The list_identifier of this GsaListAuditLogItem.
        """
        return self._list_identifier

    @list_identifier.setter
    def list_identifier(self, list_identifier: "Union[str, Unset_Type]") -> None:
        """Sets the list_identifier of this GsaListAuditLogItem.
        The identifier of the list that the action was performed on

        Parameters
        ----------
        list_identifier: Union[str, Unset_Type]
            The list_identifier of this GsaListAuditLogItem.
        """
        # Field is not nullable
        if list_identifier is None:
            raise ValueError("Invalid value for 'list_identifier', must not be 'None'")
        self._list_identifier = list_identifier

    @property
    def initiating_user(self) -> "Union[GsaListsUserOrGroup, Unset_Type]":
        """Gets the initiating_user of this GsaListAuditLogItem.

        Returns
        -------
        Union[GsaListsUserOrGroup, Unset_Type]
            The initiating_user of this GsaListAuditLogItem.
        """
        return self._initiating_user

    @initiating_user.setter
    def initiating_user(self, initiating_user: "Union[GsaListsUserOrGroup, Unset_Type]") -> None:
        """Sets the initiating_user of this GsaListAuditLogItem.

        Parameters
        ----------
        initiating_user: Union[GsaListsUserOrGroup, Unset_Type]
            The initiating_user of this GsaListAuditLogItem.
        """
        # Field is not nullable
        if initiating_user is None:
            raise ValueError("Invalid value for 'initiating_user', must not be 'None'")
        self._initiating_user = initiating_user

    @property
    def user_or_group_affected(self) -> "Union[GsaListsUserOrGroup, Unset_Type]":
        """Gets the user_or_group_affected of this GsaListAuditLogItem.

        Returns
        -------
        Union[GsaListsUserOrGroup, Unset_Type]
            The user_or_group_affected of this GsaListAuditLogItem.
        """
        return self._user_or_group_affected

    @user_or_group_affected.setter
    def user_or_group_affected(
        self, user_or_group_affected: "Union[GsaListsUserOrGroup, Unset_Type]"
    ) -> None:
        """Sets the user_or_group_affected of this GsaListAuditLogItem.

        Parameters
        ----------
        user_or_group_affected: Union[GsaListsUserOrGroup, Unset_Type]
            The user_or_group_affected of this GsaListAuditLogItem.
        """
        # Field is not nullable
        if user_or_group_affected is None:
            raise ValueError("Invalid value for 'user_or_group_affected', must not be 'None'")
        self._user_or_group_affected = user_or_group_affected

    @property
    def list_item_affected(self) -> "Union[GsaListItem, Unset_Type]":
        """Gets the list_item_affected of this GsaListAuditLogItem.

        Returns
        -------
        Union[GsaListItem, Unset_Type]
            The list_item_affected of this GsaListAuditLogItem.
        """
        return self._list_item_affected

    @list_item_affected.setter
    def list_item_affected(self, list_item_affected: "Union[GsaListItem, Unset_Type]") -> None:
        """Sets the list_item_affected of this GsaListAuditLogItem.

        Parameters
        ----------
        list_item_affected: Union[GsaListItem, Unset_Type]
            The list_item_affected of this GsaListAuditLogItem.
        """
        # Field is not nullable
        if list_item_affected is None:
            raise ValueError("Invalid value for 'list_item_affected', must not be 'None'")
        self._list_item_affected = list_item_affected

    @property
    def action(self) -> "Union[GsaListAction, Unset_Type]":
        """Gets the action of this GsaListAuditLogItem.

        Returns
        -------
        Union[GsaListAction, Unset_Type]
            The action of this GsaListAuditLogItem.
        """
        return self._action

    @action.setter
    def action(self, action: "Union[GsaListAction, Unset_Type]") -> None:
        """Sets the action of this GsaListAuditLogItem.

        Parameters
        ----------
        action: Union[GsaListAction, Unset_Type]
            The action of this GsaListAuditLogItem.
        """
        # Field is not nullable
        if action is None:
            raise ValueError("Invalid value for 'action', must not be 'None'")
        self._action = action

    @property
    def timestamp(self) -> "Union[datetime, Unset_Type]":
        """Gets the timestamp of this GsaListAuditLogItem.
        The date/time that the action occurred.

        Returns
        -------
        Union[datetime, Unset_Type]
            The timestamp of this GsaListAuditLogItem.
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: "Union[datetime, Unset_Type]") -> None:
        """Sets the timestamp of this GsaListAuditLogItem.
        The date/time that the action occurred.

        Parameters
        ----------
        timestamp: Union[datetime, Unset_Type]
            The timestamp of this GsaListAuditLogItem.
        """
        # Field is not nullable
        if timestamp is None:
            raise ValueError("Invalid value for 'timestamp', must not be 'None'")
        self._timestamp = timestamp

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
        if not isinstance(other, GsaListAuditLogItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
