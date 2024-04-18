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
from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_attributes_update_attributes_update_attribute import (
    GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute(
    GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute
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
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "allow_all_compatible_expressions": "bool",
        "allow_anonymous_expressions": "bool",
        "allow_extrapolation": "bool",
        "attribute_parameters": "list[GrantaServerApiSchemaSlimEntitiesSlimEntity]",
        "axis_name": "str",
        "default_content": "GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "expressions": "list[GrantaServerApiSchemaSlimEntitiesSlimEntity]",
        "guid": "str",
        "help_path": "str",
        "is_range": "bool",
        "name": "str",
        "type": "str",
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
    }

    attribute_map: Dict[str, str] = {
        "about_attribute": "aboutAttribute",
        "allow_all_compatible_expressions": "allowAllCompatibleExpressions",
        "allow_anonymous_expressions": "allowAnonymousExpressions",
        "allow_extrapolation": "allowExtrapolation",
        "attribute_parameters": "attributeParameters",
        "axis_name": "axisName",
        "default_content": "defaultContent",
        "default_threshold_type": "defaultThresholdType",
        "expressions": "expressions",
        "guid": "guid",
        "help_path": "helpPath",
        "is_range": "isRange",
        "name": "name",
        "type": "type",
        "unit": "unit",
    }

    subtype_mapping: Dict[str, str] = {
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "attributeParameters": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "expressions": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "defaultContent": "GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        about_attribute: "Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]" = Unset,
        allow_all_compatible_expressions: "Union[bool, Unset_Type]" = Unset,
        allow_anonymous_expressions: "Union[bool, Unset_Type]" = Unset,
        allow_extrapolation: "Union[bool, Unset_Type]" = Unset,
        attribute_parameters: "Union[List[GrantaServerApiSchemaSlimEntitiesSlimEntity], None, Unset_Type]" = Unset,
        axis_name: "Union[str, None, Unset_Type]" = Unset,
        default_content: "Union[GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent, Unset_Type]" = Unset,
        default_threshold_type: "Union[GrantaServerApiSchemaAttributesAttributeThresholdType, Unset_Type]" = Unset,
        expressions: "Union[List[GrantaServerApiSchemaSlimEntitiesSlimEntity], None, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
        help_path: "Union[str, None, Unset_Type]" = Unset,
        is_range: "Union[bool, Unset_Type]" = Unset,
        name: "Union[str, Unset_Type]" = Unset,
        type: "str" = "mathsFunctional",
        unit: "Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute - a model defined in Swagger

        Parameters
        ----------
        about_attribute: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
        allow_all_compatible_expressions: bool, optional
        allow_anonymous_expressions: bool, optional
        allow_extrapolation: bool, optional
        attribute_parameters: List[GrantaServerApiSchemaSlimEntitiesSlimEntity], optional
        axis_name: str, optional
        default_content: GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent, optional
        default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType, optional
        expressions: List[GrantaServerApiSchemaSlimEntitiesSlimEntity], optional
        guid: str, optional
        help_path: str, optional
        is_range: bool, optional
        name: str, optional
        type: str
        unit: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
        """
        super().__init__(
            about_attribute=about_attribute,
            axis_name=axis_name,
            default_threshold_type=default_threshold_type,
            guid=guid,
            help_path=help_path,
            name=name,
        )
        self._type: str
        self._unit: Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type] = (
            Unset
        )
        self._attribute_parameters: Union[
            List[GrantaServerApiSchemaSlimEntitiesSlimEntity], None, Unset_Type
        ] = Unset
        self._expressions: Union[
            List[GrantaServerApiSchemaSlimEntitiesSlimEntity], None, Unset_Type
        ] = Unset
        self._allow_extrapolation: Union[bool, Unset_Type] = Unset
        self._is_range: Union[bool, Unset_Type] = Unset
        self._default_content: Union[
            GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent,
            Unset_Type,
        ] = Unset
        self._allow_all_compatible_expressions: Union[bool, Unset_Type] = Unset
        self._allow_anonymous_expressions: Union[bool, Unset_Type] = Unset

        self.type = type
        if unit is not Unset:
            self.unit = unit
        if attribute_parameters is not Unset:
            self.attribute_parameters = attribute_parameters
        if expressions is not Unset:
            self.expressions = expressions
        if allow_extrapolation is not Unset:
            self.allow_extrapolation = allow_extrapolation
        if is_range is not Unset:
            self.is_range = is_range
        if default_content is not Unset:
            self.default_content = default_content
        if allow_all_compatible_expressions is not Unset:
            self.allow_all_compatible_expressions = allow_all_compatible_expressions
        if allow_anonymous_expressions is not Unset:
            self.allow_anonymous_expressions = allow_anonymous_expressions

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @property
    def unit(self) -> "Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]":
        """Gets the unit of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Returns
        -------
        Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]
            The unit of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        return self._unit

    @unit.setter
    def unit(
        self, unit: "Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]"
    ) -> None:
        """Sets the unit of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Parameters
        ----------
        unit: Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]
            The unit of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        # Field is not nullable
        if unit is None:
            raise ValueError("Invalid value for 'unit', must not be 'None'")
        self._unit = unit

    @property
    def attribute_parameters(
        self,
    ) -> "Union[List[GrantaServerApiSchemaSlimEntitiesSlimEntity], None, Unset_Type]":
        """Gets the attribute_parameters of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Returns
        -------
        Union[List[GrantaServerApiSchemaSlimEntitiesSlimEntity], None, Unset_Type]
            The attribute_parameters of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        return self._attribute_parameters

    @attribute_parameters.setter
    def attribute_parameters(
        self,
        attribute_parameters: "Union[List[GrantaServerApiSchemaSlimEntitiesSlimEntity], None, Unset_Type]",
    ) -> None:
        """Sets the attribute_parameters of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Parameters
        ----------
        attribute_parameters: Union[List[GrantaServerApiSchemaSlimEntitiesSlimEntity], None, Unset_Type]
            The attribute_parameters of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        self._attribute_parameters = attribute_parameters

    @property
    def expressions(
        self,
    ) -> "Union[List[GrantaServerApiSchemaSlimEntitiesSlimEntity], None, Unset_Type]":
        """Gets the expressions of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Returns
        -------
        Union[List[GrantaServerApiSchemaSlimEntitiesSlimEntity], None, Unset_Type]
            The expressions of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        return self._expressions

    @expressions.setter
    def expressions(
        self,
        expressions: "Union[List[GrantaServerApiSchemaSlimEntitiesSlimEntity], None, Unset_Type]",
    ) -> None:
        """Sets the expressions of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Parameters
        ----------
        expressions: Union[List[GrantaServerApiSchemaSlimEntitiesSlimEntity], None, Unset_Type]
            The expressions of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        self._expressions = expressions

    @property
    def allow_extrapolation(self) -> "Union[bool, Unset_Type]":
        """Gets the allow_extrapolation of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Returns
        -------
        Union[bool, Unset_Type]
            The allow_extrapolation of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        return self._allow_extrapolation

    @allow_extrapolation.setter
    def allow_extrapolation(
        self, allow_extrapolation: "Union[bool, Unset_Type]"
    ) -> None:
        """Sets the allow_extrapolation of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Parameters
        ----------
        allow_extrapolation: Union[bool, Unset_Type]
            The allow_extrapolation of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        # Field is not nullable
        if allow_extrapolation is None:
            raise ValueError(
                "Invalid value for 'allow_extrapolation', must not be 'None'"
            )
        self._allow_extrapolation = allow_extrapolation

    @property
    def is_range(self) -> "Union[bool, Unset_Type]":
        """Gets the is_range of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Returns
        -------
        Union[bool, Unset_Type]
            The is_range of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        return self._is_range

    @is_range.setter
    def is_range(self, is_range: "Union[bool, Unset_Type]") -> None:
        """Sets the is_range of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Parameters
        ----------
        is_range: Union[bool, Unset_Type]
            The is_range of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        # Field is not nullable
        if is_range is None:
            raise ValueError("Invalid value for 'is_range', must not be 'None'")
        self._is_range = is_range

    @property
    def default_content(
        self,
    ) -> "Union[GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent, Unset_Type]":
        """Gets the default_content of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Returns
        -------
        Union[GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent, Unset_Type]
            The default_content of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        return self._default_content

    @default_content.setter
    def default_content(
        self,
        default_content: "Union[GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent, Unset_Type]",
    ) -> None:
        """Sets the default_content of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Parameters
        ----------
        default_content: Union[GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsContent, Unset_Type]
            The default_content of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        # Field is not nullable
        if default_content is None:
            raise ValueError("Invalid value for 'default_content', must not be 'None'")
        self._default_content = default_content

    @property
    def allow_all_compatible_expressions(self) -> "Union[bool, Unset_Type]":
        """Gets the allow_all_compatible_expressions of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Returns
        -------
        Union[bool, Unset_Type]
            The allow_all_compatible_expressions of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        return self._allow_all_compatible_expressions

    @allow_all_compatible_expressions.setter
    def allow_all_compatible_expressions(
        self, allow_all_compatible_expressions: "Union[bool, Unset_Type]"
    ) -> None:
        """Sets the allow_all_compatible_expressions of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Parameters
        ----------
        allow_all_compatible_expressions: Union[bool, Unset_Type]
            The allow_all_compatible_expressions of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        # Field is not nullable
        if allow_all_compatible_expressions is None:
            raise ValueError(
                "Invalid value for 'allow_all_compatible_expressions', must not be 'None'"
            )
        self._allow_all_compatible_expressions = allow_all_compatible_expressions

    @property
    def allow_anonymous_expressions(self) -> "Union[bool, Unset_Type]":
        """Gets the allow_anonymous_expressions of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Returns
        -------
        Union[bool, Unset_Type]
            The allow_anonymous_expressions of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        return self._allow_anonymous_expressions

    @allow_anonymous_expressions.setter
    def allow_anonymous_expressions(
        self, allow_anonymous_expressions: "Union[bool, Unset_Type]"
    ) -> None:
        """Sets the allow_anonymous_expressions of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.

        Parameters
        ----------
        allow_anonymous_expressions: Union[bool, Unset_Type]
            The allow_anonymous_expressions of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute.
        """
        # Field is not nullable
        if allow_anonymous_expressions is None:
            raise ValueError(
                "Invalid value for 'allow_anonymous_expressions', must not be 'None'"
            )
        self._allow_anonymous_expressions = allow_anonymous_expressions

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
            other,
            GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
