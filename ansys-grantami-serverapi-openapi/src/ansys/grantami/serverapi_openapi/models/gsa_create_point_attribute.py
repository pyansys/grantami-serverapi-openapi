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

from ansys.grantami.serverapi_openapi.models.gsa_attribute_type import GsaAttributeType
from ansys.grantami.serverapi_openapi.models.gsa_create_attribute import (  # noqa: F401
    GsaCreateAttribute,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaCreatePointAttribute(GsaCreateAttribute):
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
        "name": "str",
        "type": "GsaAttributeType",
        "attribute_parameters": "list[GsaSlimEntity]",
        "axis_name": "str",
        "default_threshold_type": "GsaAttributeThresholdType",
        "guid": "str",
        "help_path": "str",
        "is_hidden_from_search_criteria": "bool",
        "is_multi_valued": "bool",
        "unit": "GsaSlimEntity",
    }

    attribute_map: dict[str, str] = {
        "name": "name",
        "type": "type",
        "attribute_parameters": "attributeParameters",
        "axis_name": "axisName",
        "default_threshold_type": "defaultThresholdType",
        "guid": "guid",
        "help_path": "helpPath",
        "is_hidden_from_search_criteria": "isHiddenFromSearchCriteria",
        "is_multi_valued": "isMultiValued",
        "unit": "unit",
    }

    subtype_mapping: dict[str, str] = {
        "unit": "GsaSlimEntity",
        "attributeParameters": "GsaSlimEntity",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        name: "str",
        type: "GsaAttributeType" = GsaAttributeType.POINT,
        attribute_parameters: "Union[list[GsaSlimEntity], None, Unset_Type]" = Unset,
        axis_name: "Union[str, None, Unset_Type]" = Unset,
        default_threshold_type: "Union[GsaAttributeThresholdType, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
        help_path: "Union[str, None, Unset_Type]" = Unset,
        is_hidden_from_search_criteria: "Union[bool, None, Unset_Type]" = Unset,
        is_multi_valued: "Union[bool, Unset_Type]" = Unset,
        unit: "Union[GsaSlimEntity, Unset_Type]" = Unset,
    ) -> None:
        """GsaCreatePointAttribute - a model defined in Swagger

        Parameters
        ----------
        name: str
        type: GsaAttributeType
        attribute_parameters: list[GsaSlimEntity], optional
        axis_name: str, optional
        default_threshold_type: GsaAttributeThresholdType, optional
        guid: str, optional
        help_path: str, optional
        is_hidden_from_search_criteria: bool, optional
        is_multi_valued: bool, optional
        unit: GsaSlimEntity, optional
        """
        super().__init__(
            name=name,
            type=type,
            default_threshold_type=default_threshold_type,
            guid=guid,
            help_path=help_path,
            is_hidden_from_search_criteria=is_hidden_from_search_criteria,
        )
        self._is_multi_valued: Union[bool, Unset_Type] = Unset
        self._unit: Union[GsaSlimEntity, Unset_Type] = Unset
        self._axis_name: Union[str, None, Unset_Type] = Unset
        self._attribute_parameters: Union[list[GsaSlimEntity], None, Unset_Type] = Unset

        if is_multi_valued is not Unset:
            self.is_multi_valued = is_multi_valued
        if unit is not Unset:
            self.unit = unit
        if axis_name is not Unset:
            self.axis_name = axis_name
        if attribute_parameters is not Unset:
            self.attribute_parameters = attribute_parameters

    @property
    def is_multi_valued(self) -> "Union[bool, Unset_Type]":
        """Gets the is_multi_valued of this GsaCreatePointAttribute.

        Returns
        -------
        Union[bool, Unset_Type]
            The is_multi_valued of this GsaCreatePointAttribute.
        """
        return self._is_multi_valued

    @is_multi_valued.setter
    def is_multi_valued(self, is_multi_valued: "Union[bool, Unset_Type]") -> None:
        """Sets the is_multi_valued of this GsaCreatePointAttribute.

        Parameters
        ----------
        is_multi_valued: Union[bool, Unset_Type]
            The is_multi_valued of this GsaCreatePointAttribute.
        """
        # Field is not nullable
        if is_multi_valued is None:
            raise ValueError("Invalid value for 'is_multi_valued', must not be 'None'")
        self._is_multi_valued = is_multi_valued

    @property
    def unit(self) -> "Union[GsaSlimEntity, Unset_Type]":
        """Gets the unit of this GsaCreatePointAttribute.

        Returns
        -------
        Union[GsaSlimEntity, Unset_Type]
            The unit of this GsaCreatePointAttribute.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "Union[GsaSlimEntity, Unset_Type]") -> None:
        """Sets the unit of this GsaCreatePointAttribute.

        Parameters
        ----------
        unit: Union[GsaSlimEntity, Unset_Type]
            The unit of this GsaCreatePointAttribute.
        """
        # Field is not nullable
        if unit is None:
            raise ValueError("Invalid value for 'unit', must not be 'None'")
        self._unit = unit

    @property
    def axis_name(self) -> "Union[str, None, Unset_Type]":
        """Gets the axis_name of this GsaCreatePointAttribute.

        Returns
        -------
        Union[str, None, Unset_Type]
            The axis_name of this GsaCreatePointAttribute.
        """
        return self._axis_name

    @axis_name.setter
    def axis_name(self, axis_name: "Union[str, None, Unset_Type]") -> None:
        """Sets the axis_name of this GsaCreatePointAttribute.

        Parameters
        ----------
        axis_name: Union[str, None, Unset_Type]
            The axis_name of this GsaCreatePointAttribute.
        """
        self._axis_name = axis_name

    @property
    def attribute_parameters(self) -> "Union[list[GsaSlimEntity], None, Unset_Type]":
        """Gets the attribute_parameters of this GsaCreatePointAttribute.

        Returns
        -------
        Union[list[GsaSlimEntity], None, Unset_Type]
            The attribute_parameters of this GsaCreatePointAttribute.
        """
        return self._attribute_parameters

    @attribute_parameters.setter
    def attribute_parameters(
        self, attribute_parameters: "Union[list[GsaSlimEntity], None, Unset_Type]"
    ) -> None:
        """Sets the attribute_parameters of this GsaCreatePointAttribute.

        Parameters
        ----------
        attribute_parameters: Union[list[GsaSlimEntity], None, Unset_Type]
            The attribute_parameters of this GsaCreatePointAttribute.
        """
        self._attribute_parameters = attribute_parameters

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
        if not isinstance(other, GsaCreatePointAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
