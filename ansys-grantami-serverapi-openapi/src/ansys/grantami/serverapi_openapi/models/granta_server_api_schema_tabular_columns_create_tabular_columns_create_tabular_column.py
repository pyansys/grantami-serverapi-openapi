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

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn(
    ModelBase
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
    discriminator_class_map: Dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: Dict[str, str] = {
        "name": "str",
        "guid": "str",
        "roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "show_as_link": "bool",
        "summary_row_enabled": "bool",
        "summary_row_roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "summary_row_text": "str",
    }

    attribute_map: Dict[str, str] = {
        "name": "name",
        "guid": "guid",
        "roll_up_type": "rollUpType",
        "show_as_link": "showAsLink",
        "summary_row_enabled": "summaryRowEnabled",
        "summary_row_roll_up_type": "summaryRowRollUpType",
        "summary_row_text": "summaryRowText",
    }

    subtype_mapping: Dict[str, str] = {
        "rollUpType": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "summaryRowRollUpType": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
    }

    discriminator_value_class_map = {
        "linkedAttribute".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLinkedAttributeTabularColumn",
        "linkedColumn".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLinkedColumnTabularColumn",
        "linkedRecord".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLinkedRecordTabularColumn",
        "localPoint".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalPointTabularColumn",
        "localRange".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalRangeTabularColumn",
        "localInteger".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalIntegerTabularColumn",
        "localLogical".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalLogicalTabularColumn",
        "localShortText".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalShortTextTabularColumn",
        "localLongText".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalLongTextTabularColumn",
        "localDateTime".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalDateTimeTabularColumn",
        "localDiscrete".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalDiscreteTabularColumn",
        "localHyperlink".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalHyperlinkTabularColumn",
        "localFile".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalFileTabularColumn",
        "localPicture".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateLocalPictureTabularColumn",
    }

    discriminator: Optional[str] = "column_type"

    def __init__(
        self,
        *,
        name: "str",
        guid: "Union[str, Unset_Type]" = Unset,
        roll_up_type: "Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]" = Unset,
        show_as_link: "Union[bool, Unset_Type]" = Unset,
        summary_row_enabled: "Union[bool, Unset_Type]" = Unset,
        summary_row_roll_up_type: "Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]" = Unset,
        summary_row_text: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn - a model defined in Swagger

        Parameters
        ----------
        name: str
        guid: str, optional
        roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, optional
        show_as_link: bool, optional
        summary_row_enabled: bool, optional
        summary_row_roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, optional
        summary_row_text: str, optional
        """
        self._show_as_link: Union[bool, Unset_Type] = Unset
        self._summary_row_enabled: Union[bool, Unset_Type] = Unset
        self._summary_row_text: Union[str, None, Unset_Type] = Unset
        self._roll_up_type: Union[
            GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type
        ] = Unset
        self._summary_row_roll_up_type: Union[
            GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type
        ] = Unset
        self._name: str
        self._guid: Union[str, Unset_Type] = Unset

        if show_as_link is not Unset:
            self.show_as_link = show_as_link
        if summary_row_enabled is not Unset:
            self.summary_row_enabled = summary_row_enabled
        if summary_row_text is not Unset:
            self.summary_row_text = summary_row_text
        if roll_up_type is not Unset:
            self.roll_up_type = roll_up_type
        if summary_row_roll_up_type is not Unset:
            self.summary_row_roll_up_type = summary_row_roll_up_type
        self.name = name
        if guid is not Unset:
            self.guid = guid

    @property
    def show_as_link(self) -> "Union[bool, Unset_Type]":
        """Gets the show_as_link of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Returns
        -------
        Union[bool, Unset_Type]
            The show_as_link of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        return self._show_as_link

    @show_as_link.setter
    def show_as_link(self, show_as_link: "Union[bool, Unset_Type]") -> None:
        """Sets the show_as_link of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Parameters
        ----------
        show_as_link: Union[bool, Unset_Type]
            The show_as_link of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        # Field is not nullable
        if show_as_link is None:
            raise ValueError("Invalid value for 'show_as_link', must not be 'None'")
        self._show_as_link = show_as_link

    @property
    def summary_row_enabled(self) -> "Union[bool, Unset_Type]":
        """Gets the summary_row_enabled of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Returns
        -------
        Union[bool, Unset_Type]
            The summary_row_enabled of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        return self._summary_row_enabled

    @summary_row_enabled.setter
    def summary_row_enabled(
        self, summary_row_enabled: "Union[bool, Unset_Type]"
    ) -> None:
        """Sets the summary_row_enabled of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Parameters
        ----------
        summary_row_enabled: Union[bool, Unset_Type]
            The summary_row_enabled of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        # Field is not nullable
        if summary_row_enabled is None:
            raise ValueError(
                "Invalid value for 'summary_row_enabled', must not be 'None'"
            )
        self._summary_row_enabled = summary_row_enabled

    @property
    def summary_row_text(self) -> "Union[str, None, Unset_Type]":
        """Gets the summary_row_text of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Returns
        -------
        Union[str, None, Unset_Type]
            The summary_row_text of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        return self._summary_row_text

    @summary_row_text.setter
    def summary_row_text(
        self, summary_row_text: "Union[str, None, Unset_Type]"
    ) -> None:
        """Sets the summary_row_text of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Parameters
        ----------
        summary_row_text: Union[str, None, Unset_Type]
            The summary_row_text of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        self._summary_row_text = summary_row_text

    @property
    def roll_up_type(
        self,
    ) -> (
        "Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]"
    ):
        """Gets the roll_up_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Returns
        -------
        Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]
            The roll_up_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        return self._roll_up_type

    @roll_up_type.setter
    def roll_up_type(
        self,
        roll_up_type: "Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]",
    ) -> None:
        """Sets the roll_up_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Parameters
        ----------
        roll_up_type: Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]
            The roll_up_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        # Field is not nullable
        if roll_up_type is None:
            raise ValueError("Invalid value for 'roll_up_type', must not be 'None'")
        self._roll_up_type = roll_up_type

    @property
    def summary_row_roll_up_type(
        self,
    ) -> (
        "Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]"
    ):
        """Gets the summary_row_roll_up_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Returns
        -------
        Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]
            The summary_row_roll_up_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        return self._summary_row_roll_up_type

    @summary_row_roll_up_type.setter
    def summary_row_roll_up_type(
        self,
        summary_row_roll_up_type: "Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]",
    ) -> None:
        """Sets the summary_row_roll_up_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Parameters
        ----------
        summary_row_roll_up_type: Union[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, Unset_Type]
            The summary_row_roll_up_type of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        # Field is not nullable
        if summary_row_roll_up_type is None:
            raise ValueError(
                "Invalid value for 'summary_row_roll_up_type', must not be 'None'"
            )
        self._summary_row_roll_up_type = summary_row_roll_up_type

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
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
        """Gets the guid of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Returns
        -------
        Union[str, Unset_Type]
            The guid of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, Unset_Type]") -> None:
        """Sets the guid of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.

        Parameters
        ----------
        guid: Union[str, Unset_Type]
            The guid of this GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        self._guid = guid

    @classmethod
    def get_real_child_model(cls, data: Dict[str, str]) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[cls._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen,
        # so we have to extract it from the JSON reference
        return cls.discriminator_value_class_map[discriminator_value].rsplit("/", 1)[-1]

    @classmethod
    def _get_discriminator_field_name(cls) -> str:
        assert cls.discriminator
        name_tokens = cls.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(
            other,
            GrantaServerApiSchemaTabularColumnsCreateTabularColumnsCreateTabularColumn,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
