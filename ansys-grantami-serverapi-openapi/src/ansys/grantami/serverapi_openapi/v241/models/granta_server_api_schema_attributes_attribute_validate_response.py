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


class GrantaServerApiSchemaAttributesAttributeValidateResponse(ModelBase):
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
        "has_validation_rules": "bool",
        "is_valid": "bool",
        "value_changed": "bool",
    }

    attribute_map = {
        "has_validation_rules": "hasValidationRules",
        "is_valid": "isValid",
        "value_changed": "valueChanged",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        has_validation_rules: "Optional[bool]" = None,
        is_valid: "Optional[bool]" = None,
        value_changed: "Optional[bool]" = None,
    ) -> None:
        """GrantaServerApiSchemaAttributesAttributeValidateResponse - a model defined in Swagger

        Parameters
        ----------
            has_validation_rules: bool, optional
            is_valid: bool, optional
            value_changed: bool, optional
        """
        self._is_valid = None
        self._has_validation_rules = None
        self._value_changed = None

        if is_valid is not None:
            self.is_valid = is_valid
        if has_validation_rules is not None:
            self.has_validation_rules = has_validation_rules
        if value_changed is not None:
            self.value_changed = value_changed

    @property
    def is_valid(self) -> "bool":
        """Gets the is_valid of this GrantaServerApiSchemaAttributesAttributeValidateResponse.
        Gets whether the provided value was valid based on the attributes data rules.

        Returns
        -------
        bool
            The is_valid of this GrantaServerApiSchemaAttributesAttributeValidateResponse.
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid: "bool") -> None:
        """Sets the is_valid of this GrantaServerApiSchemaAttributesAttributeValidateResponse.
        Gets whether the provided value was valid based on the attributes data rules.

        Parameters
        ----------
        is_valid: bool
            The is_valid of this GrantaServerApiSchemaAttributesAttributeValidateResponse.
        """
        self._is_valid = is_valid

    @property
    def has_validation_rules(self) -> "bool":
        """Gets the has_validation_rules of this GrantaServerApiSchemaAttributesAttributeValidateResponse.
        Gets whether the attribute has any validation rules that were checked.

        Returns
        -------
        bool
            The has_validation_rules of this GrantaServerApiSchemaAttributesAttributeValidateResponse.
        """
        return self._has_validation_rules

    @has_validation_rules.setter
    def has_validation_rules(self, has_validation_rules: "bool") -> None:
        """Sets the has_validation_rules of this GrantaServerApiSchemaAttributesAttributeValidateResponse.
        Gets whether the attribute has any validation rules that were checked.

        Parameters
        ----------
        has_validation_rules: bool
            The has_validation_rules of this GrantaServerApiSchemaAttributesAttributeValidateResponse.
        """
        self._has_validation_rules = has_validation_rules

    @property
    def value_changed(self) -> "bool":
        """Gets the value_changed of this GrantaServerApiSchemaAttributesAttributeValidateResponse.
        Gets whether the provided value was a new value compared to the existing value. Null if no record was provided.

        Returns
        -------
        bool
            The value_changed of this GrantaServerApiSchemaAttributesAttributeValidateResponse.
        """
        return self._value_changed

    @value_changed.setter
    def value_changed(self, value_changed: "bool") -> None:
        """Sets the value_changed of this GrantaServerApiSchemaAttributesAttributeValidateResponse.
        Gets whether the provided value was a new value compared to the existing value. Null if no record was provided.

        Parameters
        ----------
        value_changed: bool
            The value_changed of this GrantaServerApiSchemaAttributesAttributeValidateResponse.
        """
        self._value_changed = value_changed

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
        if not isinstance(other, GrantaServerApiSchemaAttributesAttributeValidateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
