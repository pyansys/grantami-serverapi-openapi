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
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, Union  # noqa: F401

from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_tabular_columns_tabular_column import (  # noqa: F401
    GrantaServerApiSchemaTabularColumnsTabularColumn,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSchemaTabularColumnsLinkedColumnTabularColumn(
    GrantaServerApiSchemaTabularColumnsTabularColumn
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
        "display_names": "dict(str, str)",
        "guid": "str",
        "linked_attribute": "GrantaServerApiSchemaSlimEntitiesSlimAttribute",
        "linked_column": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "name": "str",
        "roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "show_as_link": "bool",
        "summary_row_enabled": "bool",
        "summary_row_roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "summary_row_text": "str",
        "column_type": "str",
    }

    attribute_map: Dict[str, str] = {
        "display_names": "displayNames",
        "guid": "guid",
        "linked_attribute": "linkedAttribute",
        "linked_column": "linkedColumn",
        "name": "name",
        "roll_up_type": "rollUpType",
        "show_as_link": "showAsLink",
        "summary_row_enabled": "summaryRowEnabled",
        "summary_row_roll_up_type": "summaryRowRollUpType",
        "summary_row_text": "summaryRowText",
        "column_type": "columnType",
    }

    subtype_mapping: Dict[str, str] = {
        "linkedAttribute": "GrantaServerApiSchemaSlimEntitiesSlimAttribute",
        "linkedColumn": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        display_names: "Dict[str, str]",
        guid: "str",
        linked_attribute: "GrantaServerApiSchemaSlimEntitiesSlimAttribute",
        linked_column: "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        name: "str",
        roll_up_type: "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        show_as_link: "bool",
        summary_row_enabled: "bool",
        summary_row_roll_up_type: "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        summary_row_text: "str",
        column_type: "str" = "linkedColumn",
    ) -> None:
        """GrantaServerApiSchemaTabularColumnsLinkedColumnTabularColumn - a model defined in Swagger

        Parameters
        ----------
        display_names: Dict[str, str]
        guid: str
        linked_attribute: GrantaServerApiSchemaSlimEntitiesSlimAttribute
        linked_column: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
        name: str
        roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
        show_as_link: bool
        summary_row_enabled: bool
        summary_row_roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
        summary_row_text: str
        column_type: str
        """
        super().__init__(
            display_names=display_names,
            guid=guid,
            name=name,
            roll_up_type=roll_up_type,
            show_as_link=show_as_link,
            summary_row_enabled=summary_row_enabled,
            summary_row_roll_up_type=summary_row_roll_up_type,
            summary_row_text=summary_row_text,
        )
        self._column_type: str
        self._linked_attribute: GrantaServerApiSchemaSlimEntitiesSlimAttribute
        self._linked_column: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity

        self.column_type = column_type
        self.linked_attribute = linked_attribute
        self.linked_column = linked_column

    @property
    def column_type(self) -> "str":
        """Gets the column_type of this GrantaServerApiSchemaTabularColumnsLinkedColumnTabularColumn.

        Returns
        -------
        str
            The column_type of this GrantaServerApiSchemaTabularColumnsLinkedColumnTabularColumn.
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type: "str") -> None:
        """Sets the column_type of this GrantaServerApiSchemaTabularColumnsLinkedColumnTabularColumn.

        Parameters
        ----------
        column_type: str
            The column_type of this GrantaServerApiSchemaTabularColumnsLinkedColumnTabularColumn.
        """
        # Field is not nullable
        if column_type is None:
            raise ValueError("Invalid value for 'column_type', must not be 'None'")
        # Field is required
        if column_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'column_type', must not be 'Unset'")
        self._column_type = column_type

    @property
    def linked_attribute(self) -> "GrantaServerApiSchemaSlimEntitiesSlimAttribute":
        """Gets the linked_attribute of this GrantaServerApiSchemaTabularColumnsLinkedColumnTabularColumn.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimAttribute
            The linked_attribute of this GrantaServerApiSchemaTabularColumnsLinkedColumnTabularColumn.
        """
        return self._linked_attribute

    @linked_attribute.setter
    def linked_attribute(
        self, linked_attribute: "GrantaServerApiSchemaSlimEntitiesSlimAttribute"
    ) -> None:
        """Sets the linked_attribute of this GrantaServerApiSchemaTabularColumnsLinkedColumnTabularColumn.

        Parameters
        ----------
        linked_attribute: GrantaServerApiSchemaSlimEntitiesSlimAttribute
            The linked_attribute of this GrantaServerApiSchemaTabularColumnsLinkedColumnTabularColumn.
        """
        # Field is not nullable
        if linked_attribute is None:
            raise ValueError("Invalid value for 'linked_attribute', must not be 'None'")
        # Field is required
        if linked_attribute is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'linked_attribute', must not be 'Unset'"
            )
        self._linked_attribute = linked_attribute

    @property
    def linked_column(self) -> "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity":
        """Gets the linked_column of this GrantaServerApiSchemaTabularColumnsLinkedColumnTabularColumn.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
            The linked_column of this GrantaServerApiSchemaTabularColumnsLinkedColumnTabularColumn.
        """
        return self._linked_column

    @linked_column.setter
    def linked_column(
        self, linked_column: "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity"
    ) -> None:
        """Sets the linked_column of this GrantaServerApiSchemaTabularColumnsLinkedColumnTabularColumn.

        Parameters
        ----------
        linked_column: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
            The linked_column of this GrantaServerApiSchemaTabularColumnsLinkedColumnTabularColumn.
        """
        # Field is not nullable
        if linked_column is None:
            raise ValueError("Invalid value for 'linked_column', must not be 'None'")
        # Field is required
        if linked_column is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'linked_column', must not be 'Unset'")
        self._linked_column = linked_column

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
        if not isinstance(
            other, GrantaServerApiSchemaTabularColumnsLinkedColumnTabularColumn
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
