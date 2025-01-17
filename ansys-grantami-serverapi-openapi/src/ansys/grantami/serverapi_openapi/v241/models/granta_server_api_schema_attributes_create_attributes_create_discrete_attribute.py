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


class GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteAttribute(
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
        "discrete_type": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "name": "str",
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "guid": "str",
        "help_path": "str",
        "is_multi_valued": "bool",
        "type": "str",
    }

    attribute_map = {
        "discrete_type": "discreteType",
        "name": "name",
        "about_attribute": "aboutAttribute",
        "default_threshold_type": "defaultThresholdType",
        "guid": "guid",
        "help_path": "helpPath",
        "is_multi_valued": "isMultiValued",
        "type": "type",
    }

    subtype_mapping = {
        "discreteType": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
    }

    discriminator = None

    def __init__(
        self,
        *,
        discrete_type: "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        name: "str",
        about_attribute: "Optional[GrantaServerApiSchemaSlimEntitiesSlimEntity]" = None,
        default_threshold_type: "Optional[GrantaServerApiSchemaAttributesAttributeThresholdType]" = None,
        guid: "Optional[str]" = None,
        help_path: "Optional[str]" = None,
        is_multi_valued: "Optional[bool]" = None,
        type: "str" = "discrete",
    ) -> None:
        """GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteAttribute - a model defined in Swagger

        Parameters
        ----------
            discrete_type: GrantaServerApiSchemaSlimEntitiesSlimEntity
            name: str
            about_attribute: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
            default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType, optional
            guid: str, optional
            help_path: str, optional
            is_multi_valued: bool, optional
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
        self._discrete_type = None
        self._is_multi_valued = None

        self.type = type
        self.discrete_type = discrete_type
        if is_multi_valued is not None:
            self.is_multi_valued = is_multi_valued

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteAttribute.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteAttribute.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteAttribute.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @property
    def discrete_type(self) -> "GrantaServerApiSchemaSlimEntitiesSlimEntity":
        """Gets the discrete_type of this GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteAttribute.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimEntity
            The discrete_type of this GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteAttribute.
        """
        return self._discrete_type

    @discrete_type.setter
    def discrete_type(self, discrete_type: "GrantaServerApiSchemaSlimEntitiesSlimEntity") -> None:
        """Sets the discrete_type of this GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteAttribute.

        Parameters
        ----------
        discrete_type: GrantaServerApiSchemaSlimEntitiesSlimEntity
            The discrete_type of this GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteAttribute.
        """
        if discrete_type is None:
            raise ValueError("Invalid value for 'discrete_type', must not be 'None'")
        self._discrete_type = discrete_type

    @property
    def is_multi_valued(self) -> "bool":
        """Gets the is_multi_valued of this GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteAttribute.

        Returns
        -------
        bool
            The is_multi_valued of this GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteAttribute.
        """
        return self._is_multi_valued

    @is_multi_valued.setter
    def is_multi_valued(self, is_multi_valued: "bool") -> None:
        """Sets the is_multi_valued of this GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteAttribute.

        Parameters
        ----------
        is_multi_valued: bool
            The is_multi_valued of this GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteAttribute.
        """
        self._is_multi_valued = is_multi_valued

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
            GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteAttribute,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
