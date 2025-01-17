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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaAttributeLinkPair(ModelBase):
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
        "attribute_source": "GsaSlimAttribute",
        "attribute_target": "GsaSlimAttribute",
    }

    attribute_map: dict[str, str] = {
        "attribute_source": "attributeSource",
        "attribute_target": "attributeTarget",
    }

    subtype_mapping: dict[str, str] = {
        "attributeSource": "GsaSlimAttribute",
        "attributeTarget": "GsaSlimAttribute",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_source: "Union[GsaSlimAttribute, Unset_Type]" = Unset,
        attribute_target: "Union[GsaSlimAttribute, Unset_Type]" = Unset,
    ) -> None:
        """GsaAttributeLinkPair - a model defined in Swagger

        Parameters
        ----------
        attribute_source: GsaSlimAttribute, optional
        attribute_target: GsaSlimAttribute, optional
        """
        self._attribute_source: Union[GsaSlimAttribute, Unset_Type] = Unset
        self._attribute_target: Union[GsaSlimAttribute, Unset_Type] = Unset

        if attribute_source is not Unset:
            self.attribute_source = attribute_source
        if attribute_target is not Unset:
            self.attribute_target = attribute_target

    @property
    def attribute_source(self) -> "Union[GsaSlimAttribute, Unset_Type]":
        """Gets the attribute_source of this GsaAttributeLinkPair.

        Returns
        -------
        Union[GsaSlimAttribute, Unset_Type]
            The attribute_source of this GsaAttributeLinkPair.
        """
        return self._attribute_source

    @attribute_source.setter
    def attribute_source(self, attribute_source: "Union[GsaSlimAttribute, Unset_Type]") -> None:
        """Sets the attribute_source of this GsaAttributeLinkPair.

        Parameters
        ----------
        attribute_source: Union[GsaSlimAttribute, Unset_Type]
            The attribute_source of this GsaAttributeLinkPair.
        """
        # Field is not nullable
        if attribute_source is None:
            raise ValueError("Invalid value for 'attribute_source', must not be 'None'")
        self._attribute_source = attribute_source

    @property
    def attribute_target(self) -> "Union[GsaSlimAttribute, Unset_Type]":
        """Gets the attribute_target of this GsaAttributeLinkPair.

        Returns
        -------
        Union[GsaSlimAttribute, Unset_Type]
            The attribute_target of this GsaAttributeLinkPair.
        """
        return self._attribute_target

    @attribute_target.setter
    def attribute_target(self, attribute_target: "Union[GsaSlimAttribute, Unset_Type]") -> None:
        """Sets the attribute_target of this GsaAttributeLinkPair.

        Parameters
        ----------
        attribute_target: Union[GsaSlimAttribute, Unset_Type]
            The attribute_target of this GsaAttributeLinkPair.
        """
        # Field is not nullable
        if attribute_target is None:
            raise ValueError("Invalid value for 'attribute_target', must not be 'None'")
        self._attribute_target = attribute_target

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
        if not isinstance(other, GsaAttributeLinkPair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
