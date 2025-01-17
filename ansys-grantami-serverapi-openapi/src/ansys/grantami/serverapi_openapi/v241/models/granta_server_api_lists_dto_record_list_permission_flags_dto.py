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


class GrantaServerApiListsDtoRecordListPermissionFlagsDto(ModelBase):
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
        "is_administrator": "bool",
        "is_curator": "bool",
        "is_owner": "bool",
        "is_publisher": "bool",
        "is_subscribed": "bool",
    }

    attribute_map = {
        "is_administrator": "isAdministrator",
        "is_curator": "isCurator",
        "is_owner": "isOwner",
        "is_publisher": "isPublisher",
        "is_subscribed": "isSubscribed",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        is_administrator: "Optional[bool]" = None,
        is_curator: "Optional[bool]" = None,
        is_owner: "Optional[bool]" = None,
        is_publisher: "Optional[bool]" = None,
        is_subscribed: "Optional[bool]" = None,
    ) -> None:
        """GrantaServerApiListsDtoRecordListPermissionFlagsDto - a model defined in Swagger

        Parameters
        ----------
            is_administrator: bool, optional
            is_curator: bool, optional
            is_owner: bool, optional
            is_publisher: bool, optional
            is_subscribed: bool, optional
        """
        self._is_owner = None
        self._is_subscribed = None
        self._is_curator = None
        self._is_administrator = None
        self._is_publisher = None

        if is_owner is not None:
            self.is_owner = is_owner
        if is_subscribed is not None:
            self.is_subscribed = is_subscribed
        if is_curator is not None:
            self.is_curator = is_curator
        if is_administrator is not None:
            self.is_administrator = is_administrator
        if is_publisher is not None:
            self.is_publisher = is_publisher

    @property
    def is_owner(self) -> "bool":
        """Gets the is_owner of this GrantaServerApiListsDtoRecordListPermissionFlagsDto.
        Flag indicating if the user or group is an owner of this list.  Null means: do not change this flag's value when inserting into database.

        Returns
        -------
        bool
            The is_owner of this GrantaServerApiListsDtoRecordListPermissionFlagsDto.
        """
        return self._is_owner

    @is_owner.setter
    def is_owner(self, is_owner: "bool") -> None:
        """Sets the is_owner of this GrantaServerApiListsDtoRecordListPermissionFlagsDto.
        Flag indicating if the user or group is an owner of this list.  Null means: do not change this flag's value when inserting into database.

        Parameters
        ----------
        is_owner: bool
            The is_owner of this GrantaServerApiListsDtoRecordListPermissionFlagsDto.
        """
        self._is_owner = is_owner

    @property
    def is_subscribed(self) -> "bool":
        """Gets the is_subscribed of this GrantaServerApiListsDtoRecordListPermissionFlagsDto.
        Flag indicating if the user or group is subscribed to this list.  Null means: do not change this flag's value when inserting into database.

        Returns
        -------
        bool
            The is_subscribed of this GrantaServerApiListsDtoRecordListPermissionFlagsDto.
        """
        return self._is_subscribed

    @is_subscribed.setter
    def is_subscribed(self, is_subscribed: "bool") -> None:
        """Sets the is_subscribed of this GrantaServerApiListsDtoRecordListPermissionFlagsDto.
        Flag indicating if the user or group is subscribed to this list.  Null means: do not change this flag's value when inserting into database.

        Parameters
        ----------
        is_subscribed: bool
            The is_subscribed of this GrantaServerApiListsDtoRecordListPermissionFlagsDto.
        """
        self._is_subscribed = is_subscribed

    @property
    def is_curator(self) -> "bool":
        """Gets the is_curator of this GrantaServerApiListsDtoRecordListPermissionFlagsDto.
        Flag indicating if the user or group is a curator of this list.  Null means: do not change this flag's value when inserting into database.

        Returns
        -------
        bool
            The is_curator of this GrantaServerApiListsDtoRecordListPermissionFlagsDto.
        """
        return self._is_curator

    @is_curator.setter
    def is_curator(self, is_curator: "bool") -> None:
        """Sets the is_curator of this GrantaServerApiListsDtoRecordListPermissionFlagsDto.
        Flag indicating if the user or group is a curator of this list.  Null means: do not change this flag's value when inserting into database.

        Parameters
        ----------
        is_curator: bool
            The is_curator of this GrantaServerApiListsDtoRecordListPermissionFlagsDto.
        """
        self._is_curator = is_curator

    @property
    def is_administrator(self) -> "bool":
        """Gets the is_administrator of this GrantaServerApiListsDtoRecordListPermissionFlagsDto.
        Flag indicating if the user or group is an administrator of this list.  Null means: do not change this flag's value when inserting into database.

        Returns
        -------
        bool
            The is_administrator of this GrantaServerApiListsDtoRecordListPermissionFlagsDto.
        """
        return self._is_administrator

    @is_administrator.setter
    def is_administrator(self, is_administrator: "bool") -> None:
        """Sets the is_administrator of this GrantaServerApiListsDtoRecordListPermissionFlagsDto.
        Flag indicating if the user or group is an administrator of this list.  Null means: do not change this flag's value when inserting into database.

        Parameters
        ----------
        is_administrator: bool
            The is_administrator of this GrantaServerApiListsDtoRecordListPermissionFlagsDto.
        """
        self._is_administrator = is_administrator

    @property
    def is_publisher(self) -> "bool":
        """Gets the is_publisher of this GrantaServerApiListsDtoRecordListPermissionFlagsDto.
        Flag indicating if this user or group is a publisher of this list.  Null means: do not change this flag's value when inserting into database.

        Returns
        -------
        bool
            The is_publisher of this GrantaServerApiListsDtoRecordListPermissionFlagsDto.
        """
        return self._is_publisher

    @is_publisher.setter
    def is_publisher(self, is_publisher: "bool") -> None:
        """Sets the is_publisher of this GrantaServerApiListsDtoRecordListPermissionFlagsDto.
        Flag indicating if this user or group is a publisher of this list.  Null means: do not change this flag's value when inserting into database.

        Parameters
        ----------
        is_publisher: bool
            The is_publisher of this GrantaServerApiListsDtoRecordListPermissionFlagsDto.
        """
        self._is_publisher = is_publisher

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
        if not isinstance(other, GrantaServerApiListsDtoRecordListPermissionFlagsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
