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

from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_attributes_create_attributes_create_attribute import (  # noqa: F401
    GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute,
)

from . import ModelBase

if TYPE_CHECKING:
    from . import *


class GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute(
    GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute
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
    swagger_types = {
        "name": "str",
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "data_rule": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "guid": "str",
        "help_path": "str",
        "is_unique": "bool",
        "type": "str",
    }

    attribute_map = {
        "name": "name",
        "about_attribute": "aboutAttribute",
        "data_rule": "dataRule",
        "default_threshold_type": "defaultThresholdType",
        "guid": "guid",
        "help_path": "helpPath",
        "is_unique": "isUnique",
        "type": "type",
    }

    subtype_mapping = {
        "dataRule": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
    }

    discriminator = None

    def __init__(
        self,
        *,
        name: "str",
        about_attribute: "Optional[GrantaServerApiSchemaSlimEntitiesSlimEntity]" = None,
        data_rule: "Optional[GrantaServerApiSchemaSlimEntitiesSlimEntity]" = None,
        default_threshold_type: "Optional[GrantaServerApiSchemaAttributesAttributeThresholdType]" = None,
        guid: "Optional[str]" = None,
        help_path: "Optional[str]" = None,
        is_unique: "Optional[bool]" = None,
        type: "str" = "shortText",
    ) -> None:
        """GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute - a model defined in Swagger

        Parameters
        ----------
            name: str
            about_attribute: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
            data_rule: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
            default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType, optional
            guid: str, optional
            help_path: str, optional
            is_unique: bool, optional
            type: str
        """
        super().__init__(
            name=name,
            about_attribute=about_attribute,
            default_threshold_type=default_threshold_type,
            guid=guid,
            help_path=help_path,
        )
        self._type = None
        self._is_unique = None
        self._data_rule = None

        self.type = type
        if is_unique is not None:
            self.is_unique = is_unique
        if data_rule is not None:
            self.data_rule = data_rule

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @property
    def is_unique(self) -> "bool":
        """Gets the is_unique of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.
        Whether or not the attribute is constrained to contain a unique value

        Returns
        -------
        bool
            The is_unique of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.
        """
        return self._is_unique

    @is_unique.setter
    def is_unique(self, is_unique: "bool") -> None:
        """Sets the is_unique of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.
        Whether or not the attribute is constrained to contain a unique value

        Parameters
        ----------
        is_unique: bool
            The is_unique of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.
        """
        self._is_unique = is_unique

    @property
    def data_rule(self) -> "GrantaServerApiSchemaSlimEntitiesSlimEntity":
        """Gets the data_rule of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimEntity
            The data_rule of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.
        """
        return self._data_rule

    @data_rule.setter
    def data_rule(self, data_rule: "GrantaServerApiSchemaSlimEntitiesSlimEntity") -> None:
        """Sets the data_rule of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.

        Parameters
        ----------
        data_rule: GrantaServerApiSchemaSlimEntitiesSlimEntity
            The data_rule of this GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute.
        """
        self._data_rule = data_rule

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
        if not isinstance(
            other,
            GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
