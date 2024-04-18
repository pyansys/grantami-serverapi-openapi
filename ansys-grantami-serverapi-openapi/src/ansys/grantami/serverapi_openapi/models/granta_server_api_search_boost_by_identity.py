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


class GrantaServerApiSearchBoostByIdentity(ModelBase):
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
        "boost_factor": "float",
        "identity": "int",
    }

    attribute_map: Dict[str, str] = {
        "boost_factor": "boostFactor",
        "identity": "identity",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        boost_factor: "Union[float, Unset_Type]" = Unset,
        identity: "Union[int, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSearchBoostByIdentity - a model defined in Swagger

        Parameters
        ----------
        boost_factor: float, optional
        identity: int, optional
        """
        self._identity: Union[int, Unset_Type] = Unset
        self._boost_factor: Union[float, Unset_Type] = Unset

        if identity is not Unset:
            self.identity = identity
        if boost_factor is not Unset:
            self.boost_factor = boost_factor

    @property
    def identity(self) -> "Union[int, Unset_Type]":
        """Gets the identity of this GrantaServerApiSearchBoostByIdentity.

        Returns
        -------
        Union[int, Unset_Type]
            The identity of this GrantaServerApiSearchBoostByIdentity.
        """
        return self._identity

    @identity.setter
    def identity(self, identity: "Union[int, Unset_Type]") -> None:
        """Sets the identity of this GrantaServerApiSearchBoostByIdentity.

        Parameters
        ----------
        identity: Union[int, Unset_Type]
            The identity of this GrantaServerApiSearchBoostByIdentity.
        """
        # Field is not nullable
        if identity is None:
            raise ValueError("Invalid value for 'identity', must not be 'None'")
        self._identity = identity

    @property
    def boost_factor(self) -> "Union[float, Unset_Type]":
        """Gets the boost_factor of this GrantaServerApiSearchBoostByIdentity.

        Returns
        -------
        Union[float, Unset_Type]
            The boost_factor of this GrantaServerApiSearchBoostByIdentity.
        """
        return self._boost_factor

    @boost_factor.setter
    def boost_factor(self, boost_factor: "Union[float, Unset_Type]") -> None:
        """Sets the boost_factor of this GrantaServerApiSearchBoostByIdentity.

        Parameters
        ----------
        boost_factor: Union[float, Unset_Type]
            The boost_factor of this GrantaServerApiSearchBoostByIdentity.
        """
        # Field is not nullable
        if boost_factor is None:
            raise ValueError("Invalid value for 'boost_factor', must not be 'None'")
        self._boost_factor = boost_factor

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
        if not isinstance(other, GrantaServerApiSearchBoostByIdentity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
