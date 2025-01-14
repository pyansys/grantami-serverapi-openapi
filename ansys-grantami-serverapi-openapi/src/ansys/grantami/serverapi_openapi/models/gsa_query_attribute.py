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

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaQueryAttribute(ModelBase):
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
        "about_attribute": "GsaQuerySlimTypedAttribute",
        "attribute_parameters": "list[GsaQuerySlimNamedEntity]",
        "axis_name": "GsaQueryAxisName",
        "data_rule": "GsaQueryDataRule",
        "default_threshold_type": "GsaAttributeThresholdType",
        "discrete_type": "GsaQuerySlimDiscreteType",
        "display_names": "dict(str, str)",
        "expressions": "list[GsaQuerySlimNamedEntity]",
        "guid": "str",
        "info": "GsaQueryAttributeInfo",
        "is_functional_range": "bool",
        "is_hidden_from_search_criteria": "bool",
        "is_multi_valued": "bool",
        "name": "str",
        "tabular_columns": "list[GsaQuerySlimNamedEntity]",
        "target": "GsaQueryTabularAttributeTarget",
        "type": "GsaAttributeType",
        "unit": "GsaQueryUnit",
    }

    attribute_map: dict[str, str] = {
        "about_attribute": "aboutAttribute",
        "attribute_parameters": "attributeParameters",
        "axis_name": "axisName",
        "data_rule": "dataRule",
        "default_threshold_type": "defaultThresholdType",
        "discrete_type": "discreteType",
        "display_names": "displayNames",
        "expressions": "expressions",
        "guid": "guid",
        "info": "info",
        "is_functional_range": "isFunctionalRange",
        "is_hidden_from_search_criteria": "isHiddenFromSearchCriteria",
        "is_multi_valued": "isMultiValued",
        "name": "name",
        "tabular_columns": "tabularColumns",
        "target": "target",
        "type": "type",
        "unit": "unit",
    }

    subtype_mapping: dict[str, str] = {
        "type": "GsaAttributeType",
        "defaultThresholdType": "GsaAttributeThresholdType",
        "axisName": "GsaQueryAxisName",
        "info": "GsaQueryAttributeInfo",
        "unit": "GsaQueryUnit",
        "discreteType": "GsaQuerySlimDiscreteType",
        "dataRule": "GsaQueryDataRule",
        "target": "GsaQueryTabularAttributeTarget",
        "aboutAttribute": "GsaQuerySlimTypedAttribute",
        "tabularColumns": "GsaQuerySlimNamedEntity",
        "attributeParameters": "GsaQuerySlimNamedEntity",
        "expressions": "GsaQuerySlimNamedEntity",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        about_attribute: "Union[GsaQuerySlimTypedAttribute, Unset_Type]" = Unset,
        attribute_parameters: "Union[list[GsaQuerySlimNamedEntity], None, Unset_Type]" = Unset,
        axis_name: "Union[GsaQueryAxisName, Unset_Type]" = Unset,
        data_rule: "Union[GsaQueryDataRule, Unset_Type]" = Unset,
        default_threshold_type: "Union[GsaAttributeThresholdType, Unset_Type]" = Unset,
        discrete_type: "Union[GsaQuerySlimDiscreteType, Unset_Type]" = Unset,
        display_names: "Union[dict[str, str], None, Unset_Type]" = Unset,
        expressions: "Union[list[GsaQuerySlimNamedEntity], None, Unset_Type]" = Unset,
        guid: "Union[str, None, Unset_Type]" = Unset,
        info: "Union[GsaQueryAttributeInfo, Unset_Type]" = Unset,
        is_functional_range: "Union[bool, None, Unset_Type]" = Unset,
        is_hidden_from_search_criteria: "Union[bool, None, Unset_Type]" = Unset,
        is_multi_valued: "Union[bool, None, Unset_Type]" = Unset,
        name: "Union[str, None, Unset_Type]" = Unset,
        tabular_columns: "Union[list[GsaQuerySlimNamedEntity], None, Unset_Type]" = Unset,
        target: "Union[GsaQueryTabularAttributeTarget, Unset_Type]" = Unset,
        type: "Union[GsaAttributeType, Unset_Type]" = Unset,
        unit: "Union[GsaQueryUnit, Unset_Type]" = Unset,
    ) -> None:
        """GsaQueryAttribute - a model defined in Swagger

        Parameters
        ----------
        about_attribute: GsaQuerySlimTypedAttribute, optional
        attribute_parameters: list[GsaQuerySlimNamedEntity], optional
        axis_name: GsaQueryAxisName, optional
        data_rule: GsaQueryDataRule, optional
        default_threshold_type: GsaAttributeThresholdType, optional
        discrete_type: GsaQuerySlimDiscreteType, optional
        display_names: dict[str, str], optional
        expressions: list[GsaQuerySlimNamedEntity], optional
        guid: str, optional
        info: GsaQueryAttributeInfo, optional
        is_functional_range: bool, optional
        is_hidden_from_search_criteria: bool, optional
        is_multi_valued: bool, optional
        name: str, optional
        tabular_columns: list[GsaQuerySlimNamedEntity], optional
        target: GsaQueryTabularAttributeTarget, optional
        type: GsaAttributeType, optional
        unit: GsaQueryUnit, optional
        """
        self._type: Union[GsaAttributeType, Unset_Type] = Unset
        self._default_threshold_type: Union[GsaAttributeThresholdType, Unset_Type] = Unset
        self._is_hidden_from_search_criteria: Union[bool, None, Unset_Type] = Unset
        self._is_multi_valued: Union[bool, None, Unset_Type] = Unset
        self._is_functional_range: Union[bool, None, Unset_Type] = Unset
        self._axis_name: Union[GsaQueryAxisName, Unset_Type] = Unset
        self._info: Union[GsaQueryAttributeInfo, Unset_Type] = Unset
        self._unit: Union[GsaQueryUnit, Unset_Type] = Unset
        self._discrete_type: Union[GsaQuerySlimDiscreteType, Unset_Type] = Unset
        self._data_rule: Union[GsaQueryDataRule, Unset_Type] = Unset
        self._target: Union[GsaQueryTabularAttributeTarget, Unset_Type] = Unset
        self._about_attribute: Union[GsaQuerySlimTypedAttribute, Unset_Type] = Unset
        self._tabular_columns: Union[list[GsaQuerySlimNamedEntity], None, Unset_Type] = Unset
        self._attribute_parameters: Union[list[GsaQuerySlimNamedEntity], None, Unset_Type] = Unset
        self._expressions: Union[list[GsaQuerySlimNamedEntity], None, Unset_Type] = Unset
        self._display_names: Union[dict[str, str], None, Unset_Type] = Unset
        self._name: Union[str, None, Unset_Type] = Unset
        self._guid: Union[str, None, Unset_Type] = Unset

        if type is not Unset:
            self.type = type
        if default_threshold_type is not Unset:
            self.default_threshold_type = default_threshold_type
        if is_hidden_from_search_criteria is not Unset:
            self.is_hidden_from_search_criteria = is_hidden_from_search_criteria
        if is_multi_valued is not Unset:
            self.is_multi_valued = is_multi_valued
        if is_functional_range is not Unset:
            self.is_functional_range = is_functional_range
        if axis_name is not Unset:
            self.axis_name = axis_name
        if info is not Unset:
            self.info = info
        if unit is not Unset:
            self.unit = unit
        if discrete_type is not Unset:
            self.discrete_type = discrete_type
        if data_rule is not Unset:
            self.data_rule = data_rule
        if target is not Unset:
            self.target = target
        if about_attribute is not Unset:
            self.about_attribute = about_attribute
        if tabular_columns is not Unset:
            self.tabular_columns = tabular_columns
        if attribute_parameters is not Unset:
            self.attribute_parameters = attribute_parameters
        if expressions is not Unset:
            self.expressions = expressions
        if display_names is not Unset:
            self.display_names = display_names
        if name is not Unset:
            self.name = name
        if guid is not Unset:
            self.guid = guid

    @property
    def type(self) -> "Union[GsaAttributeType, Unset_Type]":
        """Gets the type of this GsaQueryAttribute.

        Returns
        -------
        Union[GsaAttributeType, Unset_Type]
            The type of this GsaQueryAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "Union[GsaAttributeType, Unset_Type]") -> None:
        """Sets the type of this GsaQueryAttribute.

        Parameters
        ----------
        type: Union[GsaAttributeType, Unset_Type]
            The type of this GsaQueryAttribute.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @property
    def default_threshold_type(self) -> "Union[GsaAttributeThresholdType, Unset_Type]":
        """Gets the default_threshold_type of this GsaQueryAttribute.

        Returns
        -------
        Union[GsaAttributeThresholdType, Unset_Type]
            The default_threshold_type of this GsaQueryAttribute.
        """
        return self._default_threshold_type

    @default_threshold_type.setter
    def default_threshold_type(
        self, default_threshold_type: "Union[GsaAttributeThresholdType, Unset_Type]"
    ) -> None:
        """Sets the default_threshold_type of this GsaQueryAttribute.

        Parameters
        ----------
        default_threshold_type: Union[GsaAttributeThresholdType, Unset_Type]
            The default_threshold_type of this GsaQueryAttribute.
        """
        # Field is not nullable
        if default_threshold_type is None:
            raise ValueError("Invalid value for 'default_threshold_type', must not be 'None'")
        self._default_threshold_type = default_threshold_type

    @property
    def is_hidden_from_search_criteria(self) -> "Union[bool, None, Unset_Type]":
        """Gets the is_hidden_from_search_criteria of this GsaQueryAttribute.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The is_hidden_from_search_criteria of this GsaQueryAttribute.
        """
        return self._is_hidden_from_search_criteria

    @is_hidden_from_search_criteria.setter
    def is_hidden_from_search_criteria(
        self, is_hidden_from_search_criteria: "Union[bool, None, Unset_Type]"
    ) -> None:
        """Sets the is_hidden_from_search_criteria of this GsaQueryAttribute.

        Parameters
        ----------
        is_hidden_from_search_criteria: Union[bool, None, Unset_Type]
            The is_hidden_from_search_criteria of this GsaQueryAttribute.
        """
        self._is_hidden_from_search_criteria = is_hidden_from_search_criteria

    @property
    def is_multi_valued(self) -> "Union[bool, None, Unset_Type]":
        """Gets the is_multi_valued of this GsaQueryAttribute.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The is_multi_valued of this GsaQueryAttribute.
        """
        return self._is_multi_valued

    @is_multi_valued.setter
    def is_multi_valued(self, is_multi_valued: "Union[bool, None, Unset_Type]") -> None:
        """Sets the is_multi_valued of this GsaQueryAttribute.

        Parameters
        ----------
        is_multi_valued: Union[bool, None, Unset_Type]
            The is_multi_valued of this GsaQueryAttribute.
        """
        self._is_multi_valued = is_multi_valued

    @property
    def is_functional_range(self) -> "Union[bool, None, Unset_Type]":
        """Gets the is_functional_range of this GsaQueryAttribute.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The is_functional_range of this GsaQueryAttribute.
        """
        return self._is_functional_range

    @is_functional_range.setter
    def is_functional_range(self, is_functional_range: "Union[bool, None, Unset_Type]") -> None:
        """Sets the is_functional_range of this GsaQueryAttribute.

        Parameters
        ----------
        is_functional_range: Union[bool, None, Unset_Type]
            The is_functional_range of this GsaQueryAttribute.
        """
        self._is_functional_range = is_functional_range

    @property
    def axis_name(self) -> "Union[GsaQueryAxisName, Unset_Type]":
        """Gets the axis_name of this GsaQueryAttribute.

        Returns
        -------
        Union[GsaQueryAxisName, Unset_Type]
            The axis_name of this GsaQueryAttribute.
        """
        return self._axis_name

    @axis_name.setter
    def axis_name(self, axis_name: "Union[GsaQueryAxisName, Unset_Type]") -> None:
        """Sets the axis_name of this GsaQueryAttribute.

        Parameters
        ----------
        axis_name: Union[GsaQueryAxisName, Unset_Type]
            The axis_name of this GsaQueryAttribute.
        """
        # Field is not nullable
        if axis_name is None:
            raise ValueError("Invalid value for 'axis_name', must not be 'None'")
        self._axis_name = axis_name

    @property
    def info(self) -> "Union[GsaQueryAttributeInfo, Unset_Type]":
        """Gets the info of this GsaQueryAttribute.

        Returns
        -------
        Union[GsaQueryAttributeInfo, Unset_Type]
            The info of this GsaQueryAttribute.
        """
        return self._info

    @info.setter
    def info(self, info: "Union[GsaQueryAttributeInfo, Unset_Type]") -> None:
        """Sets the info of this GsaQueryAttribute.

        Parameters
        ----------
        info: Union[GsaQueryAttributeInfo, Unset_Type]
            The info of this GsaQueryAttribute.
        """
        # Field is not nullable
        if info is None:
            raise ValueError("Invalid value for 'info', must not be 'None'")
        self._info = info

    @property
    def unit(self) -> "Union[GsaQueryUnit, Unset_Type]":
        """Gets the unit of this GsaQueryAttribute.

        Returns
        -------
        Union[GsaQueryUnit, Unset_Type]
            The unit of this GsaQueryAttribute.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "Union[GsaQueryUnit, Unset_Type]") -> None:
        """Sets the unit of this GsaQueryAttribute.

        Parameters
        ----------
        unit: Union[GsaQueryUnit, Unset_Type]
            The unit of this GsaQueryAttribute.
        """
        # Field is not nullable
        if unit is None:
            raise ValueError("Invalid value for 'unit', must not be 'None'")
        self._unit = unit

    @property
    def discrete_type(self) -> "Union[GsaQuerySlimDiscreteType, Unset_Type]":
        """Gets the discrete_type of this GsaQueryAttribute.

        Returns
        -------
        Union[GsaQuerySlimDiscreteType, Unset_Type]
            The discrete_type of this GsaQueryAttribute.
        """
        return self._discrete_type

    @discrete_type.setter
    def discrete_type(self, discrete_type: "Union[GsaQuerySlimDiscreteType, Unset_Type]") -> None:
        """Sets the discrete_type of this GsaQueryAttribute.

        Parameters
        ----------
        discrete_type: Union[GsaQuerySlimDiscreteType, Unset_Type]
            The discrete_type of this GsaQueryAttribute.
        """
        # Field is not nullable
        if discrete_type is None:
            raise ValueError("Invalid value for 'discrete_type', must not be 'None'")
        self._discrete_type = discrete_type

    @property
    def data_rule(self) -> "Union[GsaQueryDataRule, Unset_Type]":
        """Gets the data_rule of this GsaQueryAttribute.

        Returns
        -------
        Union[GsaQueryDataRule, Unset_Type]
            The data_rule of this GsaQueryAttribute.
        """
        return self._data_rule

    @data_rule.setter
    def data_rule(self, data_rule: "Union[GsaQueryDataRule, Unset_Type]") -> None:
        """Sets the data_rule of this GsaQueryAttribute.

        Parameters
        ----------
        data_rule: Union[GsaQueryDataRule, Unset_Type]
            The data_rule of this GsaQueryAttribute.
        """
        # Field is not nullable
        if data_rule is None:
            raise ValueError("Invalid value for 'data_rule', must not be 'None'")
        self._data_rule = data_rule

    @property
    def target(self) -> "Union[GsaQueryTabularAttributeTarget, Unset_Type]":
        """Gets the target of this GsaQueryAttribute.

        Returns
        -------
        Union[GsaQueryTabularAttributeTarget, Unset_Type]
            The target of this GsaQueryAttribute.
        """
        return self._target

    @target.setter
    def target(self, target: "Union[GsaQueryTabularAttributeTarget, Unset_Type]") -> None:
        """Sets the target of this GsaQueryAttribute.

        Parameters
        ----------
        target: Union[GsaQueryTabularAttributeTarget, Unset_Type]
            The target of this GsaQueryAttribute.
        """
        # Field is not nullable
        if target is None:
            raise ValueError("Invalid value for 'target', must not be 'None'")
        self._target = target

    @property
    def about_attribute(self) -> "Union[GsaQuerySlimTypedAttribute, Unset_Type]":
        """Gets the about_attribute of this GsaQueryAttribute.

        Returns
        -------
        Union[GsaQuerySlimTypedAttribute, Unset_Type]
            The about_attribute of this GsaQueryAttribute.
        """
        return self._about_attribute

    @about_attribute.setter
    def about_attribute(
        self, about_attribute: "Union[GsaQuerySlimTypedAttribute, Unset_Type]"
    ) -> None:
        """Sets the about_attribute of this GsaQueryAttribute.

        Parameters
        ----------
        about_attribute: Union[GsaQuerySlimTypedAttribute, Unset_Type]
            The about_attribute of this GsaQueryAttribute.
        """
        # Field is not nullable
        if about_attribute is None:
            raise ValueError("Invalid value for 'about_attribute', must not be 'None'")
        self._about_attribute = about_attribute

    @property
    def tabular_columns(self) -> "Union[list[GsaQuerySlimNamedEntity], None, Unset_Type]":
        """Gets the tabular_columns of this GsaQueryAttribute.

        Returns
        -------
        Union[list[GsaQuerySlimNamedEntity], None, Unset_Type]
            The tabular_columns of this GsaQueryAttribute.
        """
        return self._tabular_columns

    @tabular_columns.setter
    def tabular_columns(
        self, tabular_columns: "Union[list[GsaQuerySlimNamedEntity], None, Unset_Type]"
    ) -> None:
        """Sets the tabular_columns of this GsaQueryAttribute.

        Parameters
        ----------
        tabular_columns: Union[list[GsaQuerySlimNamedEntity], None, Unset_Type]
            The tabular_columns of this GsaQueryAttribute.
        """
        self._tabular_columns = tabular_columns

    @property
    def attribute_parameters(self) -> "Union[list[GsaQuerySlimNamedEntity], None, Unset_Type]":
        """Gets the attribute_parameters of this GsaQueryAttribute.

        Returns
        -------
        Union[list[GsaQuerySlimNamedEntity], None, Unset_Type]
            The attribute_parameters of this GsaQueryAttribute.
        """
        return self._attribute_parameters

    @attribute_parameters.setter
    def attribute_parameters(
        self, attribute_parameters: "Union[list[GsaQuerySlimNamedEntity], None, Unset_Type]"
    ) -> None:
        """Sets the attribute_parameters of this GsaQueryAttribute.

        Parameters
        ----------
        attribute_parameters: Union[list[GsaQuerySlimNamedEntity], None, Unset_Type]
            The attribute_parameters of this GsaQueryAttribute.
        """
        self._attribute_parameters = attribute_parameters

    @property
    def expressions(self) -> "Union[list[GsaQuerySlimNamedEntity], None, Unset_Type]":
        """Gets the expressions of this GsaQueryAttribute.

        Returns
        -------
        Union[list[GsaQuerySlimNamedEntity], None, Unset_Type]
            The expressions of this GsaQueryAttribute.
        """
        return self._expressions

    @expressions.setter
    def expressions(
        self, expressions: "Union[list[GsaQuerySlimNamedEntity], None, Unset_Type]"
    ) -> None:
        """Sets the expressions of this GsaQueryAttribute.

        Parameters
        ----------
        expressions: Union[list[GsaQuerySlimNamedEntity], None, Unset_Type]
            The expressions of this GsaQueryAttribute.
        """
        self._expressions = expressions

    @property
    def display_names(self) -> "Union[dict[str, str], None, Unset_Type]":
        """Gets the display_names of this GsaQueryAttribute.

        Returns
        -------
        Union[dict[str, str], None, Unset_Type]
            The display_names of this GsaQueryAttribute.
        """
        return self._display_names

    @display_names.setter
    def display_names(self, display_names: "Union[dict[str, str], None, Unset_Type]") -> None:
        """Sets the display_names of this GsaQueryAttribute.

        Parameters
        ----------
        display_names: Union[dict[str, str], None, Unset_Type]
            The display_names of this GsaQueryAttribute.
        """
        self._display_names = display_names

    @property
    def name(self) -> "Union[str, None, Unset_Type]":
        """Gets the name of this GsaQueryAttribute.

        Returns
        -------
        Union[str, None, Unset_Type]
            The name of this GsaQueryAttribute.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, None, Unset_Type]") -> None:
        """Sets the name of this GsaQueryAttribute.

        Parameters
        ----------
        name: Union[str, None, Unset_Type]
            The name of this GsaQueryAttribute.
        """
        self._name = name

    @property
    def guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the guid of this GsaQueryAttribute.

        Returns
        -------
        Union[str, None, Unset_Type]
            The guid of this GsaQueryAttribute.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the guid of this GsaQueryAttribute.

        Parameters
        ----------
        guid: Union[str, None, Unset_Type]
            The guid of this GsaQueryAttribute.
        """
        self._guid = guid

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
        if not isinstance(other, GsaQueryAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
