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
from typing import (
    TYPE_CHECKING,
    Any,
    BinaryIO,
    Dict,
    List,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_attributes_attribute import (
    GrantaServerApiSchemaAttributesAttribute,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaAttributesFloatFunctionalAttribute(
    GrantaServerApiSchemaAttributesAttribute
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
        "attribute_parameters": "list[GrantaServerApiSchemaAttributesFloatFunctionalAttributeParameter]",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "display_names": "dict(str, str)",
        "guid": "str",
        "info": "GrantaServerApiSchemaAttributesAttributeAttributeInfo",
        "is_range": "bool",
        "name": "str",
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "axis_name": "str",
        "help_path": "str",
        "type": "str",
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimUnit",
    }

    attribute_map: Dict[str, str] = {
        "attribute_parameters": "attributeParameters",
        "default_threshold_type": "defaultThresholdType",
        "display_names": "displayNames",
        "guid": "guid",
        "info": "info",
        "is_range": "isRange",
        "name": "name",
        "about_attribute": "aboutAttribute",
        "axis_name": "axisName",
        "help_path": "helpPath",
        "type": "type",
        "unit": "unit",
    }

    subtype_mapping: Dict[str, str] = {
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimUnit",
        "attributeParameters": "GrantaServerApiSchemaAttributesFloatFunctionalAttributeParameter",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_parameters: "List[GrantaServerApiSchemaAttributesFloatFunctionalAttributeParameter]",
        default_threshold_type: "GrantaServerApiSchemaAttributesAttributeThresholdType",
        display_names: "Dict[str, str]",
        guid: "str",
        info: "GrantaServerApiSchemaAttributesAttributeAttributeInfo",
        is_range: "bool",
        name: "str",
        about_attribute: "Union[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, Unset_Type]" = Unset,
        axis_name: "Union[str, None, Unset_Type]" = Unset,
        help_path: "Union[str, None, Unset_Type]" = Unset,
        type: "str" = "floatFunctional",
        unit: "Union[GrantaServerApiSchemaSlimEntitiesSlimUnit, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaAttributesFloatFunctionalAttribute - a model defined in Swagger

        Parameters
        ----------
        attribute_parameters: List[GrantaServerApiSchemaAttributesFloatFunctionalAttributeParameter]
        default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType
        display_names: Dict[str, str]
        guid: str
        info: GrantaServerApiSchemaAttributesAttributeAttributeInfo
        is_range: bool
        name: str
        about_attribute: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, optional
        axis_name: str, optional
        help_path: str, optional
        type: str
        unit: GrantaServerApiSchemaSlimEntitiesSlimUnit, optional
        """
        super().__init__(
            default_threshold_type=default_threshold_type,
            display_names=display_names,
            guid=guid,
            info=info,
            name=name,
            about_attribute=about_attribute,
            axis_name=axis_name,
            help_path=help_path,
        )
        self._type: str
        self._unit: Union[GrantaServerApiSchemaSlimEntitiesSlimUnit, Unset_Type] = Unset
        self._attribute_parameters: List[
            GrantaServerApiSchemaAttributesFloatFunctionalAttributeParameter
        ]
        self._is_range: bool

        self.type = type
        if unit is not Unset:
            self.unit = unit
        self.attribute_parameters = attribute_parameters
        self.is_range = is_range

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @property
    def unit(self) -> "Union[GrantaServerApiSchemaSlimEntitiesSlimUnit, Unset_Type]":
        """Gets the unit of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.

        Returns
        -------
        Union[GrantaServerApiSchemaSlimEntitiesSlimUnit, Unset_Type]
            The unit of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.
        """
        return self._unit

    @unit.setter
    def unit(
        self, unit: "Union[GrantaServerApiSchemaSlimEntitiesSlimUnit, Unset_Type]"
    ) -> None:
        """Sets the unit of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.

        Parameters
        ----------
        unit: Union[GrantaServerApiSchemaSlimEntitiesSlimUnit, Unset_Type]
            The unit of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.
        """
        # Field is not nullable
        if unit is None:
            raise ValueError("Invalid value for 'unit', must not be 'None'")
        self._unit = unit

    @property
    def attribute_parameters(
        self,
    ) -> "List[GrantaServerApiSchemaAttributesFloatFunctionalAttributeParameter]":
        """Gets the attribute_parameters of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.

        Returns
        -------
        List[GrantaServerApiSchemaAttributesFloatFunctionalAttributeParameter]
            The attribute_parameters of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.
        """
        return self._attribute_parameters

    @attribute_parameters.setter
    def attribute_parameters(
        self,
        attribute_parameters: "List[GrantaServerApiSchemaAttributesFloatFunctionalAttributeParameter]",
    ) -> None:
        """Sets the attribute_parameters of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.

        Parameters
        ----------
        attribute_parameters: List[GrantaServerApiSchemaAttributesFloatFunctionalAttributeParameter]
            The attribute_parameters of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.
        """
        # Field is not nullable
        if attribute_parameters is None:
            raise ValueError(
                "Invalid value for 'attribute_parameters', must not be 'None'"
            )
        # Field is required
        if attribute_parameters is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'attribute_parameters', must not be 'Unset'"
            )
        self._attribute_parameters = attribute_parameters

    @property
    def is_range(self) -> "bool":
        """Gets the is_range of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.

        Returns
        -------
        bool
            The is_range of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.
        """
        return self._is_range

    @is_range.setter
    def is_range(self, is_range: "bool") -> None:
        """Sets the is_range of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.

        Parameters
        ----------
        is_range: bool
            The is_range of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.
        """
        # Field is not nullable
        if is_range is None:
            raise ValueError("Invalid value for 'is_range', must not be 'None'")
        # Field is required
        if is_range is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'is_range', must not be 'Unset'")
        self._is_range = is_range

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
            other, GrantaServerApiSchemaAttributesFloatFunctionalAttribute
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
