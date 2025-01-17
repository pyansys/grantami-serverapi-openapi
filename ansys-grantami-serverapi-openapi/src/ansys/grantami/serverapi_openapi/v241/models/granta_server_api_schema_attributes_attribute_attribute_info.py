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


class GrantaServerApiSchemaAttributesAttributeAttributeInfo(ModelBase):
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
        "chartable": "bool",
        "expressionable": "bool",
        "extended_name": "str",
        "foreign_data_link_groups": "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
        "is_meta_attribute": "bool",
        "linkable": "bool",
        "primary_data_link_groups": "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
        "standard_names": "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
        "type_code": "str",
        "foreign_dynamic_link_groups": "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
        "ordered_meta_attributes": "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
        "primary_dynamic_link_groups": "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
    }

    attribute_map = {
        "chartable": "chartable",
        "expressionable": "expressionable",
        "extended_name": "extendedName",
        "foreign_data_link_groups": "foreignDataLinkGroups",
        "is_meta_attribute": "isMetaAttribute",
        "linkable": "linkable",
        "primary_data_link_groups": "primaryDataLinkGroups",
        "standard_names": "standardNames",
        "type_code": "typeCode",
        "foreign_dynamic_link_groups": "foreignDynamicLinkGroups",
        "ordered_meta_attributes": "orderedMetaAttributes",
        "primary_dynamic_link_groups": "primaryDynamicLinkGroups",
    }

    subtype_mapping = {
        "orderedMetaAttributes": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "standardNames": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "primaryDataLinkGroups": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "foreignDataLinkGroups": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "primaryDynamicLinkGroups": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "foreignDynamicLinkGroups": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
    }

    discriminator = None

    def __init__(
        self,
        *,
        chartable: "bool",
        expressionable: "bool",
        extended_name: "str",
        foreign_data_link_groups: "List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
        is_meta_attribute: "bool",
        linkable: "bool",
        primary_data_link_groups: "List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
        standard_names: "List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
        type_code: "str",
        foreign_dynamic_link_groups: "Optional[List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]]" = None,
        ordered_meta_attributes: "Optional[List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]]" = None,
        primary_dynamic_link_groups: "Optional[List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]]" = None,
    ) -> None:
        """GrantaServerApiSchemaAttributesAttributeAttributeInfo - a model defined in Swagger

        Parameters
        ----------
            chartable: bool
            expressionable: bool
            extended_name: str
            foreign_data_link_groups: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            is_meta_attribute: bool
            linkable: bool
            primary_data_link_groups: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            standard_names: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            type_code: str
            foreign_dynamic_link_groups: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity], optional
            ordered_meta_attributes: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity], optional
            primary_dynamic_link_groups: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity], optional
        """
        self._type_code = None
        self._chartable = None
        self._expressionable = None
        self._linkable = None
        self._extended_name = None
        self._is_meta_attribute = None
        self._ordered_meta_attributes = None
        self._standard_names = None
        self._primary_data_link_groups = None
        self._foreign_data_link_groups = None
        self._primary_dynamic_link_groups = None
        self._foreign_dynamic_link_groups = None

        self.type_code = type_code
        self.chartable = chartable
        self.expressionable = expressionable
        self.linkable = linkable
        self.extended_name = extended_name
        self.is_meta_attribute = is_meta_attribute
        if ordered_meta_attributes is not None:
            self.ordered_meta_attributes = ordered_meta_attributes
        self.standard_names = standard_names
        self.primary_data_link_groups = primary_data_link_groups
        self.foreign_data_link_groups = foreign_data_link_groups
        if primary_dynamic_link_groups is not None:
            self.primary_dynamic_link_groups = primary_dynamic_link_groups
        if foreign_dynamic_link_groups is not None:
            self.foreign_dynamic_link_groups = foreign_dynamic_link_groups

    @property
    def type_code(self) -> "str":
        """Gets the type_code of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        str
            The type_code of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._type_code

    @type_code.setter
    def type_code(self, type_code: "str") -> None:
        """Sets the type_code of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        type_code: str
            The type_code of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        if type_code is None:
            raise ValueError("Invalid value for 'type_code', must not be 'None'")
        self._type_code = type_code

    @property
    def chartable(self) -> "bool":
        """Gets the chartable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        bool
            The chartable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._chartable

    @chartable.setter
    def chartable(self, chartable: "bool") -> None:
        """Sets the chartable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        chartable: bool
            The chartable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        if chartable is None:
            raise ValueError("Invalid value for 'chartable', must not be 'None'")
        self._chartable = chartable

    @property
    def expressionable(self) -> "bool":
        """Gets the expressionable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        bool
            The expressionable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._expressionable

    @expressionable.setter
    def expressionable(self, expressionable: "bool") -> None:
        """Sets the expressionable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        expressionable: bool
            The expressionable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        if expressionable is None:
            raise ValueError("Invalid value for 'expressionable', must not be 'None'")
        self._expressionable = expressionable

    @property
    def linkable(self) -> "bool":
        """Gets the linkable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        bool
            The linkable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._linkable

    @linkable.setter
    def linkable(self, linkable: "bool") -> None:
        """Sets the linkable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        linkable: bool
            The linkable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        if linkable is None:
            raise ValueError("Invalid value for 'linkable', must not be 'None'")
        self._linkable = linkable

    @property
    def extended_name(self) -> "str":
        """Gets the extended_name of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        str
            The extended_name of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._extended_name

    @extended_name.setter
    def extended_name(self, extended_name: "str") -> None:
        """Sets the extended_name of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        extended_name: str
            The extended_name of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        if extended_name is None:
            raise ValueError("Invalid value for 'extended_name', must not be 'None'")
        self._extended_name = extended_name

    @property
    def is_meta_attribute(self) -> "bool":
        """Gets the is_meta_attribute of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        bool
            The is_meta_attribute of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._is_meta_attribute

    @is_meta_attribute.setter
    def is_meta_attribute(self, is_meta_attribute: "bool") -> None:
        """Sets the is_meta_attribute of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        is_meta_attribute: bool
            The is_meta_attribute of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        if is_meta_attribute is None:
            raise ValueError("Invalid value for 'is_meta_attribute', must not be 'None'")
        self._is_meta_attribute = is_meta_attribute

    @property
    def ordered_meta_attributes(
        self,
    ) -> "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]":
        """Gets the ordered_meta_attributes of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The ordered_meta_attributes of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._ordered_meta_attributes

    @ordered_meta_attributes.setter
    def ordered_meta_attributes(
        self,
        ordered_meta_attributes: "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
    ) -> None:
        """Sets the ordered_meta_attributes of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        ordered_meta_attributes: list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The ordered_meta_attributes of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        self._ordered_meta_attributes = ordered_meta_attributes

    @property
    def standard_names(
        self,
    ) -> "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]":
        """Gets the standard_names of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The standard_names of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._standard_names

    @standard_names.setter
    def standard_names(
        self, standard_names: "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]"
    ) -> None:
        """Sets the standard_names of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        standard_names: list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The standard_names of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        if standard_names is None:
            raise ValueError("Invalid value for 'standard_names', must not be 'None'")
        self._standard_names = standard_names

    @property
    def primary_data_link_groups(
        self,
    ) -> "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]":
        """Gets the primary_data_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The primary_data_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._primary_data_link_groups

    @primary_data_link_groups.setter
    def primary_data_link_groups(
        self,
        primary_data_link_groups: "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
    ) -> None:
        """Sets the primary_data_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        primary_data_link_groups: list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The primary_data_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        if primary_data_link_groups is None:
            raise ValueError("Invalid value for 'primary_data_link_groups', must not be 'None'")
        self._primary_data_link_groups = primary_data_link_groups

    @property
    def foreign_data_link_groups(
        self,
    ) -> "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]":
        """Gets the foreign_data_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The foreign_data_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._foreign_data_link_groups

    @foreign_data_link_groups.setter
    def foreign_data_link_groups(
        self,
        foreign_data_link_groups: "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
    ) -> None:
        """Sets the foreign_data_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        foreign_data_link_groups: list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The foreign_data_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        if foreign_data_link_groups is None:
            raise ValueError("Invalid value for 'foreign_data_link_groups', must not be 'None'")
        self._foreign_data_link_groups = foreign_data_link_groups

    @property
    def primary_dynamic_link_groups(
        self,
    ) -> "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]":
        """Gets the primary_dynamic_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The primary_dynamic_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._primary_dynamic_link_groups

    @primary_dynamic_link_groups.setter
    def primary_dynamic_link_groups(
        self,
        primary_dynamic_link_groups: "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
    ) -> None:
        """Sets the primary_dynamic_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        primary_dynamic_link_groups: list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The primary_dynamic_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        self._primary_dynamic_link_groups = primary_dynamic_link_groups

    @property
    def foreign_dynamic_link_groups(
        self,
    ) -> "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]":
        """Gets the foreign_dynamic_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The foreign_dynamic_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._foreign_dynamic_link_groups

    @foreign_dynamic_link_groups.setter
    def foreign_dynamic_link_groups(
        self,
        foreign_dynamic_link_groups: "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
    ) -> None:
        """Sets the foreign_dynamic_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        foreign_dynamic_link_groups: list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The foreign_dynamic_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        self._foreign_dynamic_link_groups = foreign_dynamic_link_groups

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
        if not isinstance(other, GrantaServerApiSchemaAttributesAttributeAttributeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
