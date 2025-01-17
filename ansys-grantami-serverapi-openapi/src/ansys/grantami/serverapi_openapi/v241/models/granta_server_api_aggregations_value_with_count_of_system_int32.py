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


class GrantaServerApiAggregationsValueWithCountOfSystemInt32(ModelBase):
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
        "count": "int",
        "value": "int",
    }

    attribute_map = {
        "count": "count",
        "value": "value",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        count: "Optional[int]" = None,
        value: "Optional[int]" = None,
    ) -> None:
        """GrantaServerApiAggregationsValueWithCountOfSystemInt32 - a model defined in Swagger

        Parameters
        ----------
            count: int, optional
            value: int, optional
        """
        self._value = None
        self._count = None

        if value is not None:
            self.value = value
        if count is not None:
            self.count = count

    @property
    def value(self) -> "int":
        """Gets the value of this GrantaServerApiAggregationsValueWithCountOfSystemInt32.

        Returns
        -------
        int
            The value of this GrantaServerApiAggregationsValueWithCountOfSystemInt32.
        """
        return self._value

    @value.setter
    def value(self, value: "int") -> None:
        """Sets the value of this GrantaServerApiAggregationsValueWithCountOfSystemInt32.

        Parameters
        ----------
        value: int
            The value of this GrantaServerApiAggregationsValueWithCountOfSystemInt32.
        """
        self._value = value

    @property
    def count(self) -> "int":
        """Gets the count of this GrantaServerApiAggregationsValueWithCountOfSystemInt32.

        Returns
        -------
        int
            The count of this GrantaServerApiAggregationsValueWithCountOfSystemInt32.
        """
        return self._count

    @count.setter
    def count(self, count: "int") -> None:
        """Sets the count of this GrantaServerApiAggregationsValueWithCountOfSystemInt32.

        Parameters
        ----------
        count: int
            The count of this GrantaServerApiAggregationsValueWithCountOfSystemInt32.
        """
        self._count = count

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
        if not isinstance(other, GrantaServerApiAggregationsValueWithCountOfSystemInt32):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
