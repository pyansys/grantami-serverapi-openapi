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


class GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute(
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
        "attribute_parameters": "list[GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter]",
        "name": "str",
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "axis_name": "str",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "guid": "str",
        "help_path": "str",
        "is_range": "bool",
        "type": "str",
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
    }

    attribute_map = {
        "attribute_parameters": "attributeParameters",
        "name": "name",
        "about_attribute": "aboutAttribute",
        "axis_name": "axisName",
        "default_threshold_type": "defaultThresholdType",
        "guid": "guid",
        "help_path": "helpPath",
        "is_range": "isRange",
        "type": "type",
        "unit": "unit",
    }

    subtype_mapping = {
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "attributeParameters": "GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter",
    }

    discriminator = None

    def __init__(
        self,
        *,
        attribute_parameters: "List[GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter]",
        name: "str",
        about_attribute: "Optional[GrantaServerApiSchemaSlimEntitiesSlimEntity]" = None,
        axis_name: "Optional[str]" = None,
        default_threshold_type: "Optional[GrantaServerApiSchemaAttributesAttributeThresholdType]" = None,
        guid: "Optional[str]" = None,
        help_path: "Optional[str]" = None,
        is_range: "Optional[bool]" = None,
        type: "str" = "floatFunctional",
        unit: "Optional[GrantaServerApiSchemaSlimEntitiesSlimEntity]" = None,
    ) -> None:
        """GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute - a model defined in Swagger

        Parameters
        ----------
            attribute_parameters: List[GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter]
            name: str
            about_attribute: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
            axis_name: str, optional
            default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType, optional
            guid: str, optional
            help_path: str, optional
            is_range: bool, optional
            type: str
            unit: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
        """
        super().__init__(
            name=name,
            about_attribute=about_attribute,
            default_threshold_type=default_threshold_type,
            guid=guid,
            help_path=help_path,
        )
        self._type = None
        self._unit = None
        self._axis_name = None
        self._attribute_parameters = None
        self._is_range = None

        self.type = type
        if unit is not None:
            self.unit = unit
        if axis_name is not None:
            self.axis_name = axis_name
        self.attribute_parameters = attribute_parameters
        if is_range is not None:
            self.is_range = is_range

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @property
    def unit(self) -> "GrantaServerApiSchemaSlimEntitiesSlimEntity":
        """Gets the unit of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimEntity
            The unit of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "GrantaServerApiSchemaSlimEntitiesSlimEntity") -> None:
        """Sets the unit of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute.

        Parameters
        ----------
        unit: GrantaServerApiSchemaSlimEntitiesSlimEntity
            The unit of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute.
        """
        self._unit = unit

    @property
    def axis_name(self) -> "str":
        """Gets the axis_name of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute.

        Returns
        -------
        str
            The axis_name of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute.
        """
        return self._axis_name

    @axis_name.setter
    def axis_name(self, axis_name: "str") -> None:
        """Sets the axis_name of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute.

        Parameters
        ----------
        axis_name: str
            The axis_name of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute.
        """
        self._axis_name = axis_name

    @property
    def attribute_parameters(
        self,
    ) -> "list[GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter]":
        """Gets the attribute_parameters of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute.

        Returns
        -------
        list[GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter]
            The attribute_parameters of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute.
        """
        return self._attribute_parameters

    @attribute_parameters.setter
    def attribute_parameters(
        self,
        attribute_parameters: "list[GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter]",
    ) -> None:
        """Sets the attribute_parameters of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute.

        Parameters
        ----------
        attribute_parameters: list[GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttributeParameter]
            The attribute_parameters of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute.
        """
        if attribute_parameters is None:
            raise ValueError("Invalid value for 'attribute_parameters', must not be 'None'")
        self._attribute_parameters = attribute_parameters

    @property
    def is_range(self) -> "bool":
        """Gets the is_range of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute.

        Returns
        -------
        bool
            The is_range of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute.
        """
        return self._is_range

    @is_range.setter
    def is_range(self, is_range: "bool") -> None:
        """Sets the is_range of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute.

        Parameters
        ----------
        is_range: bool
            The is_range of this GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute.
        """
        self._is_range = is_range

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
            GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
