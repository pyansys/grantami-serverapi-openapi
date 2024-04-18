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


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiListsDtoUpdateRecordListProperties(ModelBase):
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
        "awaiting_approval": "bool",
        "description": "str",
        "internal_use": "bool",
        "name": "str",
        "notes": "str",
        "published": "bool",
    }

    attribute_map: Dict[str, str] = {
        "awaiting_approval": "awaitingApproval",
        "description": "description",
        "internal_use": "internalUse",
        "name": "name",
        "notes": "notes",
        "published": "published",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        awaiting_approval: "Union[bool, Unset_Type]" = Unset,
        description: "Union[str, None, Unset_Type]" = Unset,
        internal_use: "Union[bool, Unset_Type]" = Unset,
        name: "Union[str, None, Unset_Type]" = Unset,
        notes: "Union[str, None, Unset_Type]" = Unset,
        published: "Union[bool, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiListsDtoUpdateRecordListProperties - a model defined in Swagger

        Parameters
        ----------
        awaiting_approval: bool, optional
        description: str, optional
        internal_use: bool, optional
        name: str, optional
        notes: str, optional
        published: bool, optional
        """
        self._name: Union[str, None, Unset_Type] = Unset
        self._description: Union[str, None, Unset_Type] = Unset
        self._notes: Union[str, None, Unset_Type] = Unset
        self._published: Union[bool, Unset_Type] = Unset
        self._awaiting_approval: Union[bool, Unset_Type] = Unset
        self._internal_use: Union[bool, Unset_Type] = Unset

        if name is not Unset:
            self.name = name
        if description is not Unset:
            self.description = description
        if notes is not Unset:
            self.notes = notes
        if published is not Unset:
            self.published = published
        if awaiting_approval is not Unset:
            self.awaiting_approval = awaiting_approval
        if internal_use is not Unset:
            self.internal_use = internal_use

    @property
    def name(self) -> "Union[str, None, Unset_Type]":
        """Gets the name of this GrantaServerApiListsDtoUpdateRecordListProperties.

        Returns
        -------
        Union[str, None, Unset_Type]
            The name of this GrantaServerApiListsDtoUpdateRecordListProperties.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, None, Unset_Type]") -> None:
        """Sets the name of this GrantaServerApiListsDtoUpdateRecordListProperties.

        Parameters
        ----------
        name: Union[str, None, Unset_Type]
            The name of this GrantaServerApiListsDtoUpdateRecordListProperties.
        """
        self._name = name

    @property
    def description(self) -> "Union[str, None, Unset_Type]":
        """Gets the description of this GrantaServerApiListsDtoUpdateRecordListProperties.

        Returns
        -------
        Union[str, None, Unset_Type]
            The description of this GrantaServerApiListsDtoUpdateRecordListProperties.
        """
        return self._description

    @description.setter
    def description(self, description: "Union[str, None, Unset_Type]") -> None:
        """Sets the description of this GrantaServerApiListsDtoUpdateRecordListProperties.

        Parameters
        ----------
        description: Union[str, None, Unset_Type]
            The description of this GrantaServerApiListsDtoUpdateRecordListProperties.
        """
        self._description = description

    @property
    def notes(self) -> "Union[str, None, Unset_Type]":
        """Gets the notes of this GrantaServerApiListsDtoUpdateRecordListProperties.

        Returns
        -------
        Union[str, None, Unset_Type]
            The notes of this GrantaServerApiListsDtoUpdateRecordListProperties.
        """
        return self._notes

    @notes.setter
    def notes(self, notes: "Union[str, None, Unset_Type]") -> None:
        """Sets the notes of this GrantaServerApiListsDtoUpdateRecordListProperties.

        Parameters
        ----------
        notes: Union[str, None, Unset_Type]
            The notes of this GrantaServerApiListsDtoUpdateRecordListProperties.
        """
        self._notes = notes

    @property
    def published(self) -> "Union[bool, Unset_Type]":
        """Gets the published of this GrantaServerApiListsDtoUpdateRecordListProperties.

        Returns
        -------
        Union[bool, Unset_Type]
            The published of this GrantaServerApiListsDtoUpdateRecordListProperties.
        """
        return self._published

    @published.setter
    def published(self, published: "Union[bool, Unset_Type]") -> None:
        """Sets the published of this GrantaServerApiListsDtoUpdateRecordListProperties.

        Parameters
        ----------
        published: Union[bool, Unset_Type]
            The published of this GrantaServerApiListsDtoUpdateRecordListProperties.
        """
        # Field is not nullable
        if published is None:
            raise ValueError("Invalid value for 'published', must not be 'None'")
        self._published = published

    @property
    def awaiting_approval(self) -> "Union[bool, Unset_Type]":
        """Gets the awaiting_approval of this GrantaServerApiListsDtoUpdateRecordListProperties.

        Returns
        -------
        Union[bool, Unset_Type]
            The awaiting_approval of this GrantaServerApiListsDtoUpdateRecordListProperties.
        """
        return self._awaiting_approval

    @awaiting_approval.setter
    def awaiting_approval(self, awaiting_approval: "Union[bool, Unset_Type]") -> None:
        """Sets the awaiting_approval of this GrantaServerApiListsDtoUpdateRecordListProperties.

        Parameters
        ----------
        awaiting_approval: Union[bool, Unset_Type]
            The awaiting_approval of this GrantaServerApiListsDtoUpdateRecordListProperties.
        """
        # Field is not nullable
        if awaiting_approval is None:
            raise ValueError(
                "Invalid value for 'awaiting_approval', must not be 'None'"
            )
        self._awaiting_approval = awaiting_approval

    @property
    def internal_use(self) -> "Union[bool, Unset_Type]":
        """Gets the internal_use of this GrantaServerApiListsDtoUpdateRecordListProperties.

        Returns
        -------
        Union[bool, Unset_Type]
            The internal_use of this GrantaServerApiListsDtoUpdateRecordListProperties.
        """
        return self._internal_use

    @internal_use.setter
    def internal_use(self, internal_use: "Union[bool, Unset_Type]") -> None:
        """Sets the internal_use of this GrantaServerApiListsDtoUpdateRecordListProperties.

        Parameters
        ----------
        internal_use: Union[bool, Unset_Type]
            The internal_use of this GrantaServerApiListsDtoUpdateRecordListProperties.
        """
        # Field is not nullable
        if internal_use is None:
            raise ValueError("Invalid value for 'internal_use', must not be 'None'")
        self._internal_use = internal_use

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
        if not isinstance(other, GrantaServerApiListsDtoUpdateRecordListProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
