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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from ansys.grantami.serverapi_openapi.models.gsa_attribute_type import GsaAttributeType
from ansys.grantami.serverapi_openapi.models.gsa_update_attribute import (  # noqa: F401
    GsaUpdateAttribute,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaUpdateFloatFunctionalAttribute(GsaUpdateAttribute):
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
        "type": "GsaAttributeType",
        "about_attribute": "GsaSlimEntity",
        "attribute_parameters": "list[GsaUpdateFloatFunctionalAttributeParameter]",
        "axis_name": "str",
        "default_threshold_type": "GsaAttributeThresholdType",
        "guid": "str",
        "help_path": "str",
        "is_hidden_from_search_criteria": "bool",
        "is_range": "bool",
        "name": "str",
        "unit": "GsaSlimEntity",
    }

    attribute_map: dict[str, str] = {
        "type": "type",
        "about_attribute": "aboutAttribute",
        "attribute_parameters": "attributeParameters",
        "axis_name": "axisName",
        "default_threshold_type": "defaultThresholdType",
        "guid": "guid",
        "help_path": "helpPath",
        "is_hidden_from_search_criteria": "isHiddenFromSearchCriteria",
        "is_range": "isRange",
        "name": "name",
        "unit": "unit",
    }

    subtype_mapping: dict[str, str] = {
        "unit": "GsaSlimEntity",
        "attributeParameters": "GsaUpdateFloatFunctionalAttributeParameter",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        type: "GsaAttributeType" = GsaAttributeType.FLOATFUNCTIONAL,
        about_attribute: "Union[GsaSlimEntity, Unset_Type]" = Unset,
        attribute_parameters: "Union[list[GsaUpdateFloatFunctionalAttributeParameter], Unset_Type]" = Unset,
        axis_name: "Union[str, None, Unset_Type]" = Unset,
        default_threshold_type: "Union[GsaAttributeThresholdType, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
        help_path: "Union[str, None, Unset_Type]" = Unset,
        is_hidden_from_search_criteria: "Union[bool, None, Unset_Type]" = Unset,
        is_range: "Union[bool, Unset_Type]" = Unset,
        name: "Union[str, Unset_Type]" = Unset,
        unit: "Union[GsaSlimEntity, Unset_Type]" = Unset,
    ) -> None:
        """GsaUpdateFloatFunctionalAttribute - a model defined in Swagger

        Parameters
        ----------
        type: GsaAttributeType
        about_attribute: GsaSlimEntity, optional
        attribute_parameters: list[GsaUpdateFloatFunctionalAttributeParameter], optional
        axis_name: str, optional
        default_threshold_type: GsaAttributeThresholdType, optional
        guid: str, optional
        help_path: str, optional
        is_hidden_from_search_criteria: bool, optional
        is_range: bool, optional
        name: str, optional
        unit: GsaSlimEntity, optional
        """
        super().__init__(
            type=type,
            about_attribute=about_attribute,
            axis_name=axis_name,
            default_threshold_type=default_threshold_type,
            guid=guid,
            help_path=help_path,
            is_hidden_from_search_criteria=is_hidden_from_search_criteria,
            name=name,
        )
        self._unit: Union[GsaSlimEntity, Unset_Type] = Unset
        self._attribute_parameters: Union[
            list[GsaUpdateFloatFunctionalAttributeParameter], Unset_Type
        ] = Unset
        self._is_range: Union[bool, Unset_Type] = Unset

        if unit is not Unset:
            self.unit = unit
        if attribute_parameters is not Unset:
            self.attribute_parameters = attribute_parameters
        if is_range is not Unset:
            self.is_range = is_range

    @property
    def unit(self) -> "Union[GsaSlimEntity, Unset_Type]":
        """Gets the unit of this GsaUpdateFloatFunctionalAttribute.

        Returns
        -------
        Union[GsaSlimEntity, Unset_Type]
            The unit of this GsaUpdateFloatFunctionalAttribute.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "Union[GsaSlimEntity, Unset_Type]") -> None:
        """Sets the unit of this GsaUpdateFloatFunctionalAttribute.

        Parameters
        ----------
        unit: Union[GsaSlimEntity, Unset_Type]
            The unit of this GsaUpdateFloatFunctionalAttribute.
        """
        # Field is not nullable
        if unit is None:
            raise ValueError("Invalid value for 'unit', must not be 'None'")
        self._unit = unit

    @property
    def attribute_parameters(
        self,
    ) -> "Union[list[GsaUpdateFloatFunctionalAttributeParameter], Unset_Type]":
        """Gets the attribute_parameters of this GsaUpdateFloatFunctionalAttribute.

        Returns
        -------
        Union[list[GsaUpdateFloatFunctionalAttributeParameter], Unset_Type]
            The attribute_parameters of this GsaUpdateFloatFunctionalAttribute.
        """
        return self._attribute_parameters

    @attribute_parameters.setter
    def attribute_parameters(
        self,
        attribute_parameters: "Union[list[GsaUpdateFloatFunctionalAttributeParameter], Unset_Type]",
    ) -> None:
        """Sets the attribute_parameters of this GsaUpdateFloatFunctionalAttribute.

        Parameters
        ----------
        attribute_parameters: Union[list[GsaUpdateFloatFunctionalAttributeParameter], Unset_Type]
            The attribute_parameters of this GsaUpdateFloatFunctionalAttribute.
        """
        # Field is not nullable
        if attribute_parameters is None:
            raise ValueError("Invalid value for 'attribute_parameters', must not be 'None'")
        self._attribute_parameters = attribute_parameters

    @property
    def is_range(self) -> "Union[bool, Unset_Type]":
        """Gets the is_range of this GsaUpdateFloatFunctionalAttribute.

        Returns
        -------
        Union[bool, Unset_Type]
            The is_range of this GsaUpdateFloatFunctionalAttribute.
        """
        return self._is_range

    @is_range.setter
    def is_range(self, is_range: "Union[bool, Unset_Type]") -> None:
        """Sets the is_range of this GsaUpdateFloatFunctionalAttribute.

        Parameters
        ----------
        is_range: Union[bool, Unset_Type]
            The is_range of this GsaUpdateFloatFunctionalAttribute.
        """
        # Field is not nullable
        if is_range is None:
            raise ValueError("Invalid value for 'is_range', must not be 'None'")
        self._is_range = is_range

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
        if not isinstance(other, GsaUpdateFloatFunctionalAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
