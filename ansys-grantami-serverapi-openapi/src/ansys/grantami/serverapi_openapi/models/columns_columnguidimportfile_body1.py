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
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class ColumnsColumnguidimportfileBody1(ModelBase):
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
        "allow_index": "bool",
        "description": "str",
        "file": "str",
        "target": "str",
    }

    attribute_map: Dict[str, str] = {
        "allow_index": "AllowIndex",
        "description": "Description",
        "file": "File",
        "target": "Target",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        allow_index: "Union[bool, Unset_Type]" = Unset,
        description: "Union[str, Unset_Type]" = Unset,
        file: "Union[Union[BinaryIO, pathlib.Path], Unset_Type]" = Unset,
        target: "Union[str, Unset_Type]" = Unset,
    ) -> None:
        """ColumnsColumnguidimportfileBody1 - a model defined in Swagger

        Parameters
        ----------
        allow_index: bool, optional
        description: str, optional
        file: Union[BinaryIO, pathlib.Path], optional
        target: str, optional
        """
        self._file: Union[Union[BinaryIO, pathlib.Path], Unset_Type] = Unset
        self._description: Union[str, Unset_Type] = Unset
        self._target: Union[str, Unset_Type] = Unset
        self._allow_index: Union[bool, Unset_Type] = Unset

        if file is not Unset:
            self.file = file
        if description is not Unset:
            self.description = description
        if target is not Unset:
            self.target = target
        if allow_index is not Unset:
            self.allow_index = allow_index

    @property
    def file(self) -> "Union[Union[BinaryIO, pathlib.Path], Unset_Type]":
        """Gets the file of this ColumnsColumnguidimportfileBody1.
        File to import.

        Returns
        -------
        Union[Union[BinaryIO, pathlib.Path], Unset_Type]
            The file of this ColumnsColumnguidimportfileBody1.
        """
        return self._file

    @file.setter
    def file(self, file: "Union[Union[BinaryIO, pathlib.Path], Unset_Type]") -> None:
        """Sets the file of this ColumnsColumnguidimportfileBody1.
        File to import.

        Parameters
        ----------
        file: Union[Union[BinaryIO, pathlib.Path], Unset_Type]
            The file of this ColumnsColumnguidimportfileBody1.
        """
        # Field is not nullable
        if file is None:
            raise ValueError("Invalid value for 'file', must not be 'None'")
        self._file = file

    @property
    def description(self) -> "Union[str, Unset_Type]":
        """Gets the description of this ColumnsColumnguidimportfileBody1.
        File description.

        Returns
        -------
        Union[str, Unset_Type]
            The description of this ColumnsColumnguidimportfileBody1.
        """
        return self._description

    @description.setter
    def description(self, description: "Union[str, Unset_Type]") -> None:
        """Sets the description of this ColumnsColumnguidimportfileBody1.
        File description.

        Parameters
        ----------
        description: Union[str, Unset_Type]
            The description of this ColumnsColumnguidimportfileBody1.
        """
        # Field is not nullable
        if description is None:
            raise ValueError("Invalid value for 'description', must not be 'None'")
        self._description = description

    @property
    def target(self) -> "Union[str, Unset_Type]":
        """Gets the target of this ColumnsColumnguidimportfileBody1.
        Sets the hyperlink target for the datum. Possible values are: 'NewWindow', 'Top', 'Parent', 'Tree', 'Content', 'CurrentFrame'. Defaults to 'NewWindow'.

        Returns
        -------
        Union[str, Unset_Type]
            The target of this ColumnsColumnguidimportfileBody1.
        """
        return self._target

    @target.setter
    def target(self, target: "Union[str, Unset_Type]") -> None:
        """Sets the target of this ColumnsColumnguidimportfileBody1.
        Sets the hyperlink target for the datum. Possible values are: 'NewWindow', 'Top', 'Parent', 'Tree', 'Content', 'CurrentFrame'. Defaults to 'NewWindow'.

        Parameters
        ----------
        target: Union[str, Unset_Type]
            The target of this ColumnsColumnguidimportfileBody1.
        """
        # Field is not nullable
        if target is None:
            raise ValueError("Invalid value for 'target', must not be 'None'")
        self._target = target

    @property
    def allow_index(self) -> "Union[bool, Unset_Type]":
        """Gets the allow_index of this ColumnsColumnguidimportfileBody1.
        Sets whether the datum will be available in the search index. Defaults to 'False'.

        Returns
        -------
        Union[bool, Unset_Type]
            The allow_index of this ColumnsColumnguidimportfileBody1.
        """
        return self._allow_index

    @allow_index.setter
    def allow_index(self, allow_index: "Union[bool, Unset_Type]") -> None:
        """Sets the allow_index of this ColumnsColumnguidimportfileBody1.
        Sets whether the datum will be available in the search index. Defaults to 'False'.

        Parameters
        ----------
        allow_index: Union[bool, Unset_Type]
            The allow_index of this ColumnsColumnguidimportfileBody1.
        """
        # Field is not nullable
        if allow_index is None:
            raise ValueError("Invalid value for 'allow_index', must not be 'None'")
        self._allow_index = allow_index

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
        if not isinstance(other, ColumnsColumnguidimportfileBody1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
