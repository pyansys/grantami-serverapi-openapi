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


class GrantaServerApiSchemaUnitsUnit(ModelBase):
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
        "guid": "str",
        "name": "str",
        "symbol": "str",
        "equation": "str",
    }

    attribute_map: Dict[str, str] = {
        "guid": "guid",
        "name": "name",
        "symbol": "symbol",
        "equation": "equation",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        guid: "str",
        name: "str",
        symbol: "str",
        equation: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaUnitsUnit - a model defined in Swagger

        Parameters
        ----------
        guid: str
        name: str
        symbol: str
        equation: str, optional
        """
        self._name: str
        self._equation: Union[str, None, Unset_Type] = Unset
        self._symbol: str
        self._guid: str

        self.name = name
        if equation is not Unset:
            self.equation = equation
        self.symbol = symbol
        self.guid = guid

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaUnitsUnit.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaUnitsUnit.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaUnitsUnit.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaUnitsUnit.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
        self._name = name

    @property
    def equation(self) -> "Union[str, None, Unset_Type]":
        """Gets the equation of this GrantaServerApiSchemaUnitsUnit.

        Returns
        -------
        Union[str, None, Unset_Type]
            The equation of this GrantaServerApiSchemaUnitsUnit.
        """
        return self._equation

    @equation.setter
    def equation(self, equation: "Union[str, None, Unset_Type]") -> None:
        """Sets the equation of this GrantaServerApiSchemaUnitsUnit.

        Parameters
        ----------
        equation: Union[str, None, Unset_Type]
            The equation of this GrantaServerApiSchemaUnitsUnit.
        """
        self._equation = equation

    @property
    def symbol(self) -> "str":
        """Gets the symbol of this GrantaServerApiSchemaUnitsUnit.

        Returns
        -------
        str
            The symbol of this GrantaServerApiSchemaUnitsUnit.
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol: "str") -> None:
        """Sets the symbol of this GrantaServerApiSchemaUnitsUnit.

        Parameters
        ----------
        symbol: str
            The symbol of this GrantaServerApiSchemaUnitsUnit.
        """
        # Field is not nullable
        if symbol is None:
            raise ValueError("Invalid value for 'symbol', must not be 'None'")
        # Field is required
        if symbol is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'symbol', must not be 'Unset'")
        self._symbol = symbol

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaUnitsUnit.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaUnitsUnit.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaUnitsUnit.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaUnitsUnit.
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
        if not isinstance(other, GrantaServerApiSchemaUnitsUnit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
