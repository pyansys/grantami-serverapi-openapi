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


class GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup(ModelBase):
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
        "display_names": "dict(str, str)",
        "guid": "str",
        "link_info": "GrantaServerApiSchemaRecordLinkGroupsLinkInfo",
        "name": "str",
        "reverse_name": "str",
        "identity": "int",
        "reverse_display_names": "dict(str, str)",
    }

    attribute_map = {
        "display_names": "displayNames",
        "guid": "guid",
        "link_info": "linkInfo",
        "name": "name",
        "reverse_name": "reverseName",
        "identity": "identity",
        "reverse_display_names": "reverseDisplayNames",
    }

    subtype_mapping = {
        "linkInfo": "GrantaServerApiSchemaRecordLinkGroupsLinkInfo",
    }

    discriminator_value_class_map = {
        "static".lower(): "#/components/schemas/GrantaServerApiSchemaRecordLinkGroupsStaticRecordLinkGroup",
        "dynamic".lower(): "#/components/schemas/GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup",
        "crossDatabase".lower(): "#/components/schemas/GrantaServerApiSchemaRecordLinkGroupsCrossDatabaseRecordLinkGroup",
    }

    discriminator = "type"

    def __init__(
        self,
        *,
        display_names: "Dict[str, str]",
        guid: "str",
        link_info: "GrantaServerApiSchemaRecordLinkGroupsLinkInfo",
        name: "str",
        reverse_name: "str",
        identity: "Optional[int]" = None,
        reverse_display_names: "Optional[Dict[str, str]]" = None,
    ) -> None:
        """GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup - a model defined in Swagger

        Parameters
        ----------
            display_names: Dict[str, str]
            guid: str
            link_info: GrantaServerApiSchemaRecordLinkGroupsLinkInfo
            name: str
            reverse_name: str
            identity: int, optional
            reverse_display_names: Dict[str, str], optional
        """
        self._link_info = None
        self._identity = None
        self._reverse_name = None
        self._reverse_display_names = None
        self._display_names = None
        self._name = None
        self._guid = None

        self.link_info = link_info
        if identity is not None:
            self.identity = identity
        self.reverse_name = reverse_name
        if reverse_display_names is not None:
            self.reverse_display_names = reverse_display_names
        self.display_names = display_names
        self.name = name
        self.guid = guid

    @property
    def link_info(self) -> "GrantaServerApiSchemaRecordLinkGroupsLinkInfo":
        """Gets the link_info of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.

        Returns
        -------
        GrantaServerApiSchemaRecordLinkGroupsLinkInfo
            The link_info of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.
        """
        return self._link_info

    @link_info.setter
    def link_info(self, link_info: "GrantaServerApiSchemaRecordLinkGroupsLinkInfo") -> None:
        """Sets the link_info of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.

        Parameters
        ----------
        link_info: GrantaServerApiSchemaRecordLinkGroupsLinkInfo
            The link_info of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.
        """
        if link_info is None:
            raise ValueError("Invalid value for 'link_info', must not be 'None'")
        self._link_info = link_info

    @property
    def identity(self) -> "int":
        """Gets the identity of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.

        Returns
        -------
        int
            The identity of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.
        """
        return self._identity

    @identity.setter
    def identity(self, identity: "int") -> None:
        """Sets the identity of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.

        Parameters
        ----------
        identity: int
            The identity of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.
        """
        self._identity = identity

    @property
    def reverse_name(self) -> "str":
        """Gets the reverse_name of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.

        Returns
        -------
        str
            The reverse_name of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.
        """
        return self._reverse_name

    @reverse_name.setter
    def reverse_name(self, reverse_name: "str") -> None:
        """Sets the reverse_name of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.

        Parameters
        ----------
        reverse_name: str
            The reverse_name of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.
        """
        if reverse_name is None:
            raise ValueError("Invalid value for 'reverse_name', must not be 'None'")
        self._reverse_name = reverse_name

    @property
    def reverse_display_names(self) -> "dict(str, str)":
        """Gets the reverse_display_names of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.

        Returns
        -------
        dict(str, str)
            The reverse_display_names of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.
        """
        return self._reverse_display_names

    @reverse_display_names.setter
    def reverse_display_names(self, reverse_display_names: "dict(str, str)") -> None:
        """Sets the reverse_display_names of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.

        Parameters
        ----------
        reverse_display_names: dict(str, str)
            The reverse_display_names of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.
        """
        self._reverse_display_names = reverse_display_names

    @property
    def display_names(self) -> "dict(str, str)":
        """Gets the display_names of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.

        Returns
        -------
        dict(str, str)
            The display_names of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.
        """
        return self._display_names

    @display_names.setter
    def display_names(self, display_names: "dict(str, str)") -> None:
        """Sets the display_names of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.

        Parameters
        ----------
        display_names: dict(str, str)
            The display_names of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.
        """
        if display_names is None:
            raise ValueError("Invalid value for 'display_names', must not be 'None'")
        self._display_names = display_names

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.
        """
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup.
        """
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
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
        if not isinstance(other, GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
