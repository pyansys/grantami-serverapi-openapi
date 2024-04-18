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


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaDataRulesDataRule(ModelBase):
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
        "description": "str",
        "guid": "str",
        "name": "str",
        "regular_expression": "str",
        "used_by_attributes": "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
    }

    attribute_map: Dict[str, str] = {
        "description": "description",
        "guid": "guid",
        "name": "name",
        "regular_expression": "regularExpression",
        "used_by_attributes": "usedByAttributes",
    }

    subtype_mapping: Dict[str, str] = {
        "usedByAttributes": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        description: "str",
        guid: "str",
        name: "str",
        regular_expression: "str",
        used_by_attributes: "List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
    ) -> None:
        """GrantaServerApiSchemaDataRulesDataRule - a model defined in Swagger

        Parameters
        ----------
        description: str
        guid: str
        name: str
        regular_expression: str
        used_by_attributes: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
        """
        self._description: str
        self._regular_expression: str
        self._used_by_attributes: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
        self._name: str
        self._guid: str

        self.description = description
        self.regular_expression = regular_expression
        self.used_by_attributes = used_by_attributes
        self.name = name
        self.guid = guid

    @property
    def description(self) -> "str":
        """Gets the description of this GrantaServerApiSchemaDataRulesDataRule.

        Returns
        -------
        str
            The description of this GrantaServerApiSchemaDataRulesDataRule.
        """
        return self._description

    @description.setter
    def description(self, description: "str") -> None:
        """Sets the description of this GrantaServerApiSchemaDataRulesDataRule.

        Parameters
        ----------
        description: str
            The description of this GrantaServerApiSchemaDataRulesDataRule.
        """
        # Field is not nullable
        if description is None:
            raise ValueError("Invalid value for 'description', must not be 'None'")
        # Field is required
        if description is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'description', must not be 'Unset'")
        self._description = description

    @property
    def regular_expression(self) -> "str":
        """Gets the regular_expression of this GrantaServerApiSchemaDataRulesDataRule.

        Returns
        -------
        str
            The regular_expression of this GrantaServerApiSchemaDataRulesDataRule.
        """
        return self._regular_expression

    @regular_expression.setter
    def regular_expression(self, regular_expression: "str") -> None:
        """Sets the regular_expression of this GrantaServerApiSchemaDataRulesDataRule.

        Parameters
        ----------
        regular_expression: str
            The regular_expression of this GrantaServerApiSchemaDataRulesDataRule.
        """
        # Field is not nullable
        if regular_expression is None:
            raise ValueError(
                "Invalid value for 'regular_expression', must not be 'None'"
            )
        # Field is required
        if regular_expression is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'regular_expression', must not be 'Unset'"
            )
        self._regular_expression = regular_expression

    @property
    def used_by_attributes(
        self,
    ) -> "List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]":
        """Gets the used_by_attributes of this GrantaServerApiSchemaDataRulesDataRule.

        Returns
        -------
        List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The used_by_attributes of this GrantaServerApiSchemaDataRulesDataRule.
        """
        return self._used_by_attributes

    @used_by_attributes.setter
    def used_by_attributes(
        self,
        used_by_attributes: "List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
    ) -> None:
        """Sets the used_by_attributes of this GrantaServerApiSchemaDataRulesDataRule.

        Parameters
        ----------
        used_by_attributes: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The used_by_attributes of this GrantaServerApiSchemaDataRulesDataRule.
        """
        # Field is not nullable
        if used_by_attributes is None:
            raise ValueError(
                "Invalid value for 'used_by_attributes', must not be 'None'"
            )
        # Field is required
        if used_by_attributes is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'used_by_attributes', must not be 'Unset'"
            )
        self._used_by_attributes = used_by_attributes

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaDataRulesDataRule.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaDataRulesDataRule.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaDataRulesDataRule.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaDataRulesDataRule.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaDataRulesDataRule.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaDataRulesDataRule.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaDataRulesDataRule.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaDataRulesDataRule.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        # Field is required
        if guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'guid', must not be 'Unset'")
        self._guid = guid

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
        if not isinstance(other, GrantaServerApiSchemaDataRulesDataRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
