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


class GsaIntegrationDiscreteType(ModelBase):
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
        "guid": "str",
        "identity": "int",
        "name": "str",
        "values": "list[str]",
    }

    attribute_map: dict[str, str] = {
        "guid": "guid",
        "identity": "identity",
        "name": "name",
        "values": "values",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        guid: "Union[str, None, Unset_Type]" = Unset,
        identity: "Union[int, Unset_Type]" = Unset,
        name: "Union[str, None, Unset_Type]" = Unset,
        values: "Union[list[str], None, Unset_Type]" = Unset,
    ) -> None:
        """GsaIntegrationDiscreteType - a model defined in Swagger

        Parameters
        ----------
        guid: str, optional
        identity: int, optional
        name: str, optional
        values: list[str], optional
        """
        self._identity: Union[int, Unset_Type] = Unset
        self._guid: Union[str, None, Unset_Type] = Unset
        self._name: Union[str, None, Unset_Type] = Unset
        self._values: Union[list[str], None, Unset_Type] = Unset

        if identity is not Unset:
            self.identity = identity
        if guid is not Unset:
            self.guid = guid
        if name is not Unset:
            self.name = name
        if values is not Unset:
            self.values = values

    @property
    def identity(self) -> "Union[int, Unset_Type]":
        """Gets the identity of this GsaIntegrationDiscreteType.

        Returns
        -------
        Union[int, Unset_Type]
            The identity of this GsaIntegrationDiscreteType.
        """
        return self._identity

    @identity.setter
    def identity(self, identity: "Union[int, Unset_Type]") -> None:
        """Sets the identity of this GsaIntegrationDiscreteType.

        Parameters
        ----------
        identity: Union[int, Unset_Type]
            The identity of this GsaIntegrationDiscreteType.
        """
        # Field is not nullable
        if identity is None:
            raise ValueError("Invalid value for 'identity', must not be 'None'")
        self._identity = identity

    @property
    def guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the guid of this GsaIntegrationDiscreteType.

        Returns
        -------
        Union[str, None, Unset_Type]
            The guid of this GsaIntegrationDiscreteType.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the guid of this GsaIntegrationDiscreteType.

        Parameters
        ----------
        guid: Union[str, None, Unset_Type]
            The guid of this GsaIntegrationDiscreteType.
        """
        self._guid = guid

    @property
    def name(self) -> "Union[str, None, Unset_Type]":
        """Gets the name of this GsaIntegrationDiscreteType.

        Returns
        -------
        Union[str, None, Unset_Type]
            The name of this GsaIntegrationDiscreteType.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, None, Unset_Type]") -> None:
        """Sets the name of this GsaIntegrationDiscreteType.

        Parameters
        ----------
        name: Union[str, None, Unset_Type]
            The name of this GsaIntegrationDiscreteType.
        """
        self._name = name

    @property
    def values(self) -> "Union[list[str], None, Unset_Type]":
        """Gets the values of this GsaIntegrationDiscreteType.

        Returns
        -------
        Union[list[str], None, Unset_Type]
            The values of this GsaIntegrationDiscreteType.
        """
        return self._values

    @values.setter
    def values(self, values: "Union[list[str], None, Unset_Type]") -> None:
        """Sets the values of this GsaIntegrationDiscreteType.

        Parameters
        ----------
        values: Union[list[str], None, Unset_Type]
            The values of this GsaIntegrationDiscreteType.
        """
        self._values = values

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
        if not isinstance(other, GsaIntegrationDiscreteType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
