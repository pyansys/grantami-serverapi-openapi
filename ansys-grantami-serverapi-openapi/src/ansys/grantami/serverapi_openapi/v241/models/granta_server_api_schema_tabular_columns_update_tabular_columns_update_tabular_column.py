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


class GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn(ModelBase):
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
    swagger_types = {
        "guid": "str",
        "name": "str",
        "roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "show_as_link": "bool",
        "summary_row_enabled": "bool",
        "summary_row_roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "summary_row_text": "str",
    }

    attribute_map = {
        "guid": "guid",
        "name": "name",
        "roll_up_type": "rollUpType",
        "show_as_link": "showAsLink",
        "summary_row_enabled": "summaryRowEnabled",
        "summary_row_roll_up_type": "summaryRowRollUpType",
        "summary_row_text": "summaryRowText",
    }

    subtype_mapping = {
        "rollUpType": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "summaryRowRollUpType": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
    }

    discriminator_value_class_map = {
        "linkedAttribute".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLinkedAttributeTabularColumn",
        "linkedColumn".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLinkedColumnTabularColumn",
        "linkedRecord".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLinkedRecordTabularColumn",
        "localPoint".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLocalPointTabularColumn",
        "localRange".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLocalRangeTabularColumn",
        "localInteger".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLocalIntegerTabularColumn",
        "localLogical".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLocalLogicalTabularColumn",
        "localShortText".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLocalShortTextTabularColumn",
        "localLongText".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLocalLongTextTabularColumn",
        "localDateTime".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLocalDateTimeTabularColumn",
        "localDiscrete".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLocalDiscreteTabularColumn",
        "localHyperlink".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLocalHyperlinkTabularColumn",
        "localFile".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLocalFileTabularColumn",
        "localPicture".lower(): "#/components/schemas/GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateLocalPictureTabularColumn",
    }

    discriminator = "column_type"

    def __init__(
        self,
        *,
        guid: "Optional[str]" = None,
        name: "Optional[str]" = None,
        roll_up_type: "Optional[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType]" = None,
        show_as_link: "Optional[bool]" = None,
        summary_row_enabled: "Optional[bool]" = None,
        summary_row_roll_up_type: "Optional[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType]" = None,
        summary_row_text: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn - a model defined in Swagger

        Parameters
        ----------
            guid: str, optional
            name: str, optional
            roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, optional
            show_as_link: bool, optional
            summary_row_enabled: bool, optional
            summary_row_roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, optional
            summary_row_text: str, optional
        """
        self._show_as_link = None
        self._summary_row_enabled = None
        self._summary_row_text = None
        self._roll_up_type = None
        self._summary_row_roll_up_type = None
        self._name = None
        self._guid = None

        if show_as_link is not None:
            self.show_as_link = show_as_link
        if summary_row_enabled is not None:
            self.summary_row_enabled = summary_row_enabled
        if summary_row_text is not None:
            self.summary_row_text = summary_row_text
        if roll_up_type is not None:
            self.roll_up_type = roll_up_type
        if summary_row_roll_up_type is not None:
            self.summary_row_roll_up_type = summary_row_roll_up_type
        if name is not None:
            self.name = name
        if guid is not None:
            self.guid = guid

    @property
    def show_as_link(self) -> "bool":
        """Gets the show_as_link of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.

        Returns
        -------
        bool
            The show_as_link of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.
        """
        return self._show_as_link

    @show_as_link.setter
    def show_as_link(self, show_as_link: "bool") -> None:
        """Sets the show_as_link of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.

        Parameters
        ----------
        show_as_link: bool
            The show_as_link of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.
        """
        self._show_as_link = show_as_link

    @property
    def summary_row_enabled(self) -> "bool":
        """Gets the summary_row_enabled of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.

        Returns
        -------
        bool
            The summary_row_enabled of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.
        """
        return self._summary_row_enabled

    @summary_row_enabled.setter
    def summary_row_enabled(self, summary_row_enabled: "bool") -> None:
        """Sets the summary_row_enabled of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.

        Parameters
        ----------
        summary_row_enabled: bool
            The summary_row_enabled of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.
        """
        self._summary_row_enabled = summary_row_enabled

    @property
    def summary_row_text(self) -> "str":
        """Gets the summary_row_text of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.

        Returns
        -------
        str
            The summary_row_text of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.
        """
        return self._summary_row_text

    @summary_row_text.setter
    def summary_row_text(self, summary_row_text: "str") -> None:
        """Sets the summary_row_text of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.

        Parameters
        ----------
        summary_row_text: str
            The summary_row_text of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.
        """
        self._summary_row_text = summary_row_text

    @property
    def roll_up_type(
        self,
    ) -> "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType":
        """Gets the roll_up_type of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.

        Returns
        -------
        GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
            The roll_up_type of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.
        """
        return self._roll_up_type

    @roll_up_type.setter
    def roll_up_type(
        self, roll_up_type: "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType"
    ) -> None:
        """Sets the roll_up_type of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.

        Parameters
        ----------
        roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
            The roll_up_type of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.
        """
        self._roll_up_type = roll_up_type

    @property
    def summary_row_roll_up_type(
        self,
    ) -> "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType":
        """Gets the summary_row_roll_up_type of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.

        Returns
        -------
        GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
            The summary_row_roll_up_type of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.
        """
        return self._summary_row_roll_up_type

    @summary_row_roll_up_type.setter
    def summary_row_roll_up_type(
        self,
        summary_row_roll_up_type: "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
    ) -> None:
        """Sets the summary_row_roll_up_type of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.

        Parameters
        ----------
        summary_row_roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
            The summary_row_roll_up_type of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.
        """
        self._summary_row_roll_up_type = summary_row_roll_up_type

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.
        """
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn.
        """
        self._guid = guid

    @classmethod
    def get_real_child_model(cls, data: ModelBase) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[cls._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen,
        # so we have to extract it from the JSON reference
        return cls.discriminator_value_class_map.get(discriminator_value).rsplit("/", 1)[-1]

    @classmethod
    def _get_discriminator_field_name(cls) -> str:
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
            GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
