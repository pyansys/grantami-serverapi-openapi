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


class GsaDiscreteGridPoint(ModelBase):
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
        "constraints": "list[GsaParameterWithDataValue]",
        "estimated": "bool",
        "value": "GsaDiscreteValuesDiscreteValue",
    }

    attribute_map: dict[str, str] = {
        "constraints": "constraints",
        "estimated": "estimated",
        "value": "value",
    }

    subtype_mapping: dict[str, str] = {
        "constraints": "GsaParameterWithDataValue",
        "value": "GsaDiscreteValuesDiscreteValue",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        constraints: "list[GsaParameterWithDataValue]",
        estimated: "bool",
        value: "GsaDiscreteValuesDiscreteValue",
    ) -> None:
        """GsaDiscreteGridPoint - a model defined in Swagger

        Parameters
        ----------
        constraints: list[GsaParameterWithDataValue]
        estimated: bool
        value: GsaDiscreteValuesDiscreteValue
        """
        self._constraints: list[GsaParameterWithDataValue]
        self._value: GsaDiscreteValuesDiscreteValue
        self._estimated: bool

        self.constraints = constraints
        self.value = value
        self.estimated = estimated

    @property
    def constraints(self) -> "list[GsaParameterWithDataValue]":
        """Gets the constraints of this GsaDiscreteGridPoint.

        Returns
        -------
        list[GsaParameterWithDataValue]
            The constraints of this GsaDiscreteGridPoint.
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints: "list[GsaParameterWithDataValue]") -> None:
        """Sets the constraints of this GsaDiscreteGridPoint.

        Parameters
        ----------
        constraints: list[GsaParameterWithDataValue]
            The constraints of this GsaDiscreteGridPoint.
        """
        # Field is not nullable
        if constraints is None:
            raise ValueError("Invalid value for 'constraints', must not be 'None'")
        # Field is required
        if constraints is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'constraints', must not be 'Unset'")
        self._constraints = constraints

    @property
    def value(self) -> "GsaDiscreteValuesDiscreteValue":
        """Gets the value of this GsaDiscreteGridPoint.

        Returns
        -------
        GsaDiscreteValuesDiscreteValue
            The value of this GsaDiscreteGridPoint.
        """
        return self._value

    @value.setter
    def value(self, value: "GsaDiscreteValuesDiscreteValue") -> None:
        """Sets the value of this GsaDiscreteGridPoint.

        Parameters
        ----------
        value: GsaDiscreteValuesDiscreteValue
            The value of this GsaDiscreteGridPoint.
        """
        # Field is not nullable
        if value is None:
            raise ValueError("Invalid value for 'value', must not be 'None'")
        # Field is required
        if value is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'value', must not be 'Unset'")
        self._value = value

    @property
    def estimated(self) -> "bool":
        """Gets the estimated of this GsaDiscreteGridPoint.

        Returns
        -------
        bool
            The estimated of this GsaDiscreteGridPoint.
        """
        return self._estimated

    @estimated.setter
    def estimated(self, estimated: "bool") -> None:
        """Sets the estimated of this GsaDiscreteGridPoint.

        Parameters
        ----------
        estimated: bool
            The estimated of this GsaDiscreteGridPoint.
        """
        # Field is not nullable
        if estimated is None:
            raise ValueError("Invalid value for 'estimated', must not be 'None'")
        # Field is required
        if estimated is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'estimated', must not be 'Unset'")
        self._estimated = estimated

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
        if not isinstance(other, GsaDiscreteGridPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
