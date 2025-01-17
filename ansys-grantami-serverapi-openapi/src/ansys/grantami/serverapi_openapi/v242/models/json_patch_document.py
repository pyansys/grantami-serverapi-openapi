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
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class JsonPatchDocument(ModelBase):
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
        "op": "str",
        "path": "str",
        "value": "str",
    }

    attribute_map: Dict[str, str] = {
        "op": "op",
        "path": "path",
        "value": "value",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        op: "Union[str, Unset_Type]" = Unset,
        path: "Union[str, Unset_Type]" = Unset,
        value: "Union[str, Unset_Type]" = Unset,
    ) -> None:
        """JsonPatchDocument - a model defined in Swagger

        Parameters
        ----------
        op: str, optional
        path: str, optional
        value: str, optional
        """
        self._op: Union[str, Unset_Type] = Unset
        self._path: Union[str, Unset_Type] = Unset
        self._value: Union[str, Unset_Type] = Unset

        if op is not Unset:
            self.op = op
        if path is not Unset:
            self.path = path
        if value is not Unset:
            self.value = value

    @property
    def op(self) -> "Union[str, Unset_Type]":
        """Gets the op of this JsonPatchDocument.

        Returns
        -------
        Union[str, Unset_Type]
            The op of this JsonPatchDocument.
        """
        return self._op

    @op.setter
    def op(self, op: "Union[str, Unset_Type]") -> None:
        """Sets the op of this JsonPatchDocument.

        Parameters
        ----------
        op: Union[str, Unset_Type]
            The op of this JsonPatchDocument.
        """
        # Field is not nullable
        if op is None:
            raise ValueError("Invalid value for 'op', must not be 'None'")
        self._op = op

    @property
    def path(self) -> "Union[str, Unset_Type]":
        """Gets the path of this JsonPatchDocument.

        Returns
        -------
        Union[str, Unset_Type]
            The path of this JsonPatchDocument.
        """
        return self._path

    @path.setter
    def path(self, path: "Union[str, Unset_Type]") -> None:
        """Sets the path of this JsonPatchDocument.

        Parameters
        ----------
        path: Union[str, Unset_Type]
            The path of this JsonPatchDocument.
        """
        # Field is not nullable
        if path is None:
            raise ValueError("Invalid value for 'path', must not be 'None'")
        self._path = path

    @property
    def value(self) -> "Union[str, Unset_Type]":
        """Gets the value of this JsonPatchDocument.

        Returns
        -------
        Union[str, Unset_Type]
            The value of this JsonPatchDocument.
        """
        return self._value

    @value.setter
    def value(self, value: "Union[str, Unset_Type]") -> None:
        """Sets the value of this JsonPatchDocument.

        Parameters
        ----------
        value: Union[str, Unset_Type]
            The value of this JsonPatchDocument.
        """
        # Field is not nullable
        if value is None:
            raise ValueError("Invalid value for 'value', must not be 'None'")
        self._value = value

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
        if not isinstance(other, JsonPatchDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
