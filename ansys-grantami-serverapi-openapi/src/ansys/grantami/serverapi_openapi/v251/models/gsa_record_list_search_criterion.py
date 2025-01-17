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

from ansys.grantami.serverapi_openapi.models.gsa_list_criterion import (  # noqa: F401
    GsaListCriterion,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaRecordListSearchCriterion(GsaListCriterion):
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
        "type": "str",
        "contains_records": "list[str]",
        "contains_records_in_databases": "list[str]",
        "contains_records_in_integration_schemas": "list[str]",
        "contains_records_in_tables": "list[str]",
        "is_awaiting_approval": "bool",
        "is_internal_use": "bool",
        "is_published": "bool",
        "is_revision": "bool",
        "name_contains": "str",
        "user_can_add_or_remove_items": "bool",
        "user_role": "GsaUserRole",
    }

    attribute_map: dict[str, str] = {
        "type": "type",
        "contains_records": "containsRecords",
        "contains_records_in_databases": "containsRecordsInDatabases",
        "contains_records_in_integration_schemas": "containsRecordsInIntegrationSchemas",
        "contains_records_in_tables": "containsRecordsInTables",
        "is_awaiting_approval": "isAwaitingApproval",
        "is_internal_use": "isInternalUse",
        "is_published": "isPublished",
        "is_revision": "isRevision",
        "name_contains": "nameContains",
        "user_can_add_or_remove_items": "userCanAddOrRemoveItems",
        "user_role": "userRole",
    }

    subtype_mapping: dict[str, str] = {
        "userRole": "GsaUserRole",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        type: "str" = "recordList",
        contains_records: "Union[list[str], None, Unset_Type]" = Unset,
        contains_records_in_databases: "Union[list[str], None, Unset_Type]" = Unset,
        contains_records_in_integration_schemas: "Union[list[str], None, Unset_Type]" = Unset,
        contains_records_in_tables: "Union[list[str], None, Unset_Type]" = Unset,
        is_awaiting_approval: "Union[bool, None, Unset_Type]" = Unset,
        is_internal_use: "Union[bool, None, Unset_Type]" = Unset,
        is_published: "Union[bool, None, Unset_Type]" = Unset,
        is_revision: "Union[bool, None, Unset_Type]" = Unset,
        name_contains: "Union[str, None, Unset_Type]" = Unset,
        user_can_add_or_remove_items: "Union[bool, None, Unset_Type]" = Unset,
        user_role: "Union[GsaUserRole, Unset_Type]" = Unset,
    ) -> None:
        """GsaRecordListSearchCriterion - a model defined in Swagger

        Parameters
        ----------
        type: str
        contains_records: list[str], optional
        contains_records_in_databases: list[str], optional
        contains_records_in_integration_schemas: list[str], optional
        contains_records_in_tables: list[str], optional
        is_awaiting_approval: bool, optional
        is_internal_use: bool, optional
        is_published: bool, optional
        is_revision: bool, optional
        name_contains: str, optional
        user_can_add_or_remove_items: bool, optional
        user_role: GsaUserRole, optional
        """
        super().__init__(type=type)
        self._name_contains: Union[str, None, Unset_Type] = Unset
        self._user_role: Union[GsaUserRole, Unset_Type] = Unset
        self._is_published: Union[bool, None, Unset_Type] = Unset
        self._is_awaiting_approval: Union[bool, None, Unset_Type] = Unset
        self._is_internal_use: Union[bool, None, Unset_Type] = Unset
        self._is_revision: Union[bool, None, Unset_Type] = Unset
        self._contains_records_in_databases: Union[list[str], None, Unset_Type] = Unset
        self._contains_records_in_integration_schemas: Union[list[str], None, Unset_Type] = Unset
        self._contains_records_in_tables: Union[list[str], None, Unset_Type] = Unset
        self._contains_records: Union[list[str], None, Unset_Type] = Unset
        self._user_can_add_or_remove_items: Union[bool, None, Unset_Type] = Unset

        if name_contains is not Unset:
            self.name_contains = name_contains
        if user_role is not Unset:
            self.user_role = user_role
        if is_published is not Unset:
            self.is_published = is_published
        if is_awaiting_approval is not Unset:
            self.is_awaiting_approval = is_awaiting_approval
        if is_internal_use is not Unset:
            self.is_internal_use = is_internal_use
        if is_revision is not Unset:
            self.is_revision = is_revision
        if contains_records_in_databases is not Unset:
            self.contains_records_in_databases = contains_records_in_databases
        if contains_records_in_integration_schemas is not Unset:
            self.contains_records_in_integration_schemas = contains_records_in_integration_schemas
        if contains_records_in_tables is not Unset:
            self.contains_records_in_tables = contains_records_in_tables
        if contains_records is not Unset:
            self.contains_records = contains_records
        if user_can_add_or_remove_items is not Unset:
            self.user_can_add_or_remove_items = user_can_add_or_remove_items

    @property
    def name_contains(self) -> "Union[str, None, Unset_Type]":
        """Gets the name_contains of this GsaRecordListSearchCriterion.

        Returns
        -------
        Union[str, None, Unset_Type]
            The name_contains of this GsaRecordListSearchCriterion.
        """
        return self._name_contains

    @name_contains.setter
    def name_contains(self, name_contains: "Union[str, None, Unset_Type]") -> None:
        """Sets the name_contains of this GsaRecordListSearchCriterion.

        Parameters
        ----------
        name_contains: Union[str, None, Unset_Type]
            The name_contains of this GsaRecordListSearchCriterion.
        """
        self._name_contains = name_contains

    @property
    def user_role(self) -> "Union[GsaUserRole, Unset_Type]":
        """Gets the user_role of this GsaRecordListSearchCriterion.

        Returns
        -------
        Union[GsaUserRole, Unset_Type]
            The user_role of this GsaRecordListSearchCriterion.
        """
        return self._user_role

    @user_role.setter
    def user_role(self, user_role: "Union[GsaUserRole, Unset_Type]") -> None:
        """Sets the user_role of this GsaRecordListSearchCriterion.

        Parameters
        ----------
        user_role: Union[GsaUserRole, Unset_Type]
            The user_role of this GsaRecordListSearchCriterion.
        """
        # Field is not nullable
        if user_role is None:
            raise ValueError("Invalid value for 'user_role', must not be 'None'")
        self._user_role = user_role

    @property
    def is_published(self) -> "Union[bool, None, Unset_Type]":
        """Gets the is_published of this GsaRecordListSearchCriterion.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The is_published of this GsaRecordListSearchCriterion.
        """
        return self._is_published

    @is_published.setter
    def is_published(self, is_published: "Union[bool, None, Unset_Type]") -> None:
        """Sets the is_published of this GsaRecordListSearchCriterion.

        Parameters
        ----------
        is_published: Union[bool, None, Unset_Type]
            The is_published of this GsaRecordListSearchCriterion.
        """
        self._is_published = is_published

    @property
    def is_awaiting_approval(self) -> "Union[bool, None, Unset_Type]":
        """Gets the is_awaiting_approval of this GsaRecordListSearchCriterion.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The is_awaiting_approval of this GsaRecordListSearchCriterion.
        """
        return self._is_awaiting_approval

    @is_awaiting_approval.setter
    def is_awaiting_approval(self, is_awaiting_approval: "Union[bool, None, Unset_Type]") -> None:
        """Sets the is_awaiting_approval of this GsaRecordListSearchCriterion.

        Parameters
        ----------
        is_awaiting_approval: Union[bool, None, Unset_Type]
            The is_awaiting_approval of this GsaRecordListSearchCriterion.
        """
        self._is_awaiting_approval = is_awaiting_approval

    @property
    def is_internal_use(self) -> "Union[bool, None, Unset_Type]":
        """Gets the is_internal_use of this GsaRecordListSearchCriterion.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The is_internal_use of this GsaRecordListSearchCriterion.
        """
        return self._is_internal_use

    @is_internal_use.setter
    def is_internal_use(self, is_internal_use: "Union[bool, None, Unset_Type]") -> None:
        """Sets the is_internal_use of this GsaRecordListSearchCriterion.

        Parameters
        ----------
        is_internal_use: Union[bool, None, Unset_Type]
            The is_internal_use of this GsaRecordListSearchCriterion.
        """
        self._is_internal_use = is_internal_use

    @property
    def is_revision(self) -> "Union[bool, None, Unset_Type]":
        """Gets the is_revision of this GsaRecordListSearchCriterion.
        Restrict to record lists that are (non discarded) revisions.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The is_revision of this GsaRecordListSearchCriterion.
        """
        return self._is_revision

    @is_revision.setter
    def is_revision(self, is_revision: "Union[bool, None, Unset_Type]") -> None:
        """Sets the is_revision of this GsaRecordListSearchCriterion.
        Restrict to record lists that are (non discarded) revisions.

        Parameters
        ----------
        is_revision: Union[bool, None, Unset_Type]
            The is_revision of this GsaRecordListSearchCriterion.
        """
        self._is_revision = is_revision

    @property
    def contains_records_in_databases(self) -> "Union[list[str], None, Unset_Type]":
        """Gets the contains_records_in_databases of this GsaRecordListSearchCriterion.
        Limits results to lists containing records in any of of the specified databases

        Returns
        -------
        Union[list[str], None, Unset_Type]
            The contains_records_in_databases of this GsaRecordListSearchCriterion.
        """
        return self._contains_records_in_databases

    @contains_records_in_databases.setter
    def contains_records_in_databases(
        self, contains_records_in_databases: "Union[list[str], None, Unset_Type]"
    ) -> None:
        """Sets the contains_records_in_databases of this GsaRecordListSearchCriterion.
        Limits results to lists containing records in any of of the specified databases

        Parameters
        ----------
        contains_records_in_databases: Union[list[str], None, Unset_Type]
            The contains_records_in_databases of this GsaRecordListSearchCriterion.
        """
        self._contains_records_in_databases = contains_records_in_databases

    @property
    def contains_records_in_integration_schemas(self) -> "Union[list[str], None, Unset_Type]":
        """Gets the contains_records_in_integration_schemas of this GsaRecordListSearchCriterion.
        Limits results to lists containing records in any of the specified integration schemas

        Returns
        -------
        Union[list[str], None, Unset_Type]
            The contains_records_in_integration_schemas of this GsaRecordListSearchCriterion.
        """
        return self._contains_records_in_integration_schemas

    @contains_records_in_integration_schemas.setter
    def contains_records_in_integration_schemas(
        self, contains_records_in_integration_schemas: "Union[list[str], None, Unset_Type]"
    ) -> None:
        """Sets the contains_records_in_integration_schemas of this GsaRecordListSearchCriterion.
        Limits results to lists containing records in any of the specified integration schemas

        Parameters
        ----------
        contains_records_in_integration_schemas: Union[list[str], None, Unset_Type]
            The contains_records_in_integration_schemas of this GsaRecordListSearchCriterion.
        """
        self._contains_records_in_integration_schemas = contains_records_in_integration_schemas

    @property
    def contains_records_in_tables(self) -> "Union[list[str], None, Unset_Type]":
        """Gets the contains_records_in_tables of this GsaRecordListSearchCriterion.
        Limits results to lists containing records in any of the specified tables

        Returns
        -------
        Union[list[str], None, Unset_Type]
            The contains_records_in_tables of this GsaRecordListSearchCriterion.
        """
        return self._contains_records_in_tables

    @contains_records_in_tables.setter
    def contains_records_in_tables(
        self, contains_records_in_tables: "Union[list[str], None, Unset_Type]"
    ) -> None:
        """Sets the contains_records_in_tables of this GsaRecordListSearchCriterion.
        Limits results to lists containing records in any of the specified tables

        Parameters
        ----------
        contains_records_in_tables: Union[list[str], None, Unset_Type]
            The contains_records_in_tables of this GsaRecordListSearchCriterion.
        """
        self._contains_records_in_tables = contains_records_in_tables

    @property
    def contains_records(self) -> "Union[list[str], None, Unset_Type]":
        """Gets the contains_records of this GsaRecordListSearchCriterion.
        Limits results to lists containing any of the given records

        Returns
        -------
        Union[list[str], None, Unset_Type]
            The contains_records of this GsaRecordListSearchCriterion.
        """
        return self._contains_records

    @contains_records.setter
    def contains_records(self, contains_records: "Union[list[str], None, Unset_Type]") -> None:
        """Sets the contains_records of this GsaRecordListSearchCriterion.
        Limits results to lists containing any of the given records

        Parameters
        ----------
        contains_records: Union[list[str], None, Unset_Type]
            The contains_records of this GsaRecordListSearchCriterion.
        """
        self._contains_records = contains_records

    @property
    def user_can_add_or_remove_items(self) -> "Union[bool, None, Unset_Type]":
        """Gets the user_can_add_or_remove_items of this GsaRecordListSearchCriterion.
        Limits results to lists where the current user can add or remove items.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The user_can_add_or_remove_items of this GsaRecordListSearchCriterion.
        """
        return self._user_can_add_or_remove_items

    @user_can_add_or_remove_items.setter
    def user_can_add_or_remove_items(
        self, user_can_add_or_remove_items: "Union[bool, None, Unset_Type]"
    ) -> None:
        """Sets the user_can_add_or_remove_items of this GsaRecordListSearchCriterion.
        Limits results to lists where the current user can add or remove items.

        Parameters
        ----------
        user_can_add_or_remove_items: Union[bool, None, Unset_Type]
            The user_can_add_or_remove_items of this GsaRecordListSearchCriterion.
        """
        self._user_can_add_or_remove_items = user_can_add_or_remove_items

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
        if not isinstance(other, GsaRecordListSearchCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
