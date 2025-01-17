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


class GrantaServerApiSchemaDataRulesUpdateDataRule(ModelBase):
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
        "description": "str",
        "guid": "str",
        "name": "str",
        "regular_expression": "str",
    }

    attribute_map = {
        "description": "description",
        "guid": "guid",
        "name": "name",
        "regular_expression": "regularExpression",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        description: "Optional[str]" = None,
        guid: "Optional[str]" = None,
        name: "Optional[str]" = None,
        regular_expression: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiSchemaDataRulesUpdateDataRule - a model defined in Swagger

        Parameters
        ----------
            description: str, optional
            guid: str, optional
            name: str, optional
            regular_expression: str, optional
        """
        self._description = None
        self._regular_expression = None
        self._name = None
        self._guid = None

        if description is not None:
            self.description = description
        if regular_expression is not None:
            self.regular_expression = regular_expression
        if name is not None:
            self.name = name
        if guid is not None:
            self.guid = guid

    @property
    def description(self) -> "str":
        """Gets the description of this GrantaServerApiSchemaDataRulesUpdateDataRule.

        Returns
        -------
        str
            The description of this GrantaServerApiSchemaDataRulesUpdateDataRule.
        """
        return self._description

    @description.setter
    def description(self, description: "str") -> None:
        """Sets the description of this GrantaServerApiSchemaDataRulesUpdateDataRule.

        Parameters
        ----------
        description: str
            The description of this GrantaServerApiSchemaDataRulesUpdateDataRule.
        """
        self._description = description

    @property
    def regular_expression(self) -> "str":
        """Gets the regular_expression of this GrantaServerApiSchemaDataRulesUpdateDataRule.

        Returns
        -------
        str
            The regular_expression of this GrantaServerApiSchemaDataRulesUpdateDataRule.
        """
        return self._regular_expression

    @regular_expression.setter
    def regular_expression(self, regular_expression: "str") -> None:
        """Sets the regular_expression of this GrantaServerApiSchemaDataRulesUpdateDataRule.

        Parameters
        ----------
        regular_expression: str
            The regular_expression of this GrantaServerApiSchemaDataRulesUpdateDataRule.
        """
        self._regular_expression = regular_expression

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaDataRulesUpdateDataRule.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaDataRulesUpdateDataRule.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaDataRulesUpdateDataRule.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaDataRulesUpdateDataRule.
        """
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaDataRulesUpdateDataRule.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaDataRulesUpdateDataRule.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaDataRulesUpdateDataRule.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaDataRulesUpdateDataRule.
        """
        self._guid = guid

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
        if not isinstance(other, GrantaServerApiSchemaDataRulesUpdateDataRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
