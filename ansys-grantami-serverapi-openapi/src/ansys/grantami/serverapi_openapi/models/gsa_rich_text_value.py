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


class GsaRichTextValue(ModelBase):
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
        "text": "str",
        "type": "GsaRichTextType",
    }

    attribute_map: dict[str, str] = {
        "text": "text",
        "type": "type",
    }

    subtype_mapping: dict[str, str] = {
        "type": "GsaRichTextType",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        text: "str",
        type: "GsaRichTextType",
    ) -> None:
        """GsaRichTextValue - a model defined in Swagger

        Parameters
        ----------
        text: str
        type: GsaRichTextType
        """
        self._text: str
        self._type: GsaRichTextType

        self.text = text
        self.type = type

    @property
    def text(self) -> "str":
        """Gets the text of this GsaRichTextValue.

        Returns
        -------
        str
            The text of this GsaRichTextValue.
        """
        return self._text

    @text.setter
    def text(self, text: "str") -> None:
        """Sets the text of this GsaRichTextValue.

        Parameters
        ----------
        text: str
            The text of this GsaRichTextValue.
        """
        # Field is not nullable
        if text is None:
            raise ValueError("Invalid value for 'text', must not be 'None'")
        # Field is required
        if text is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'text', must not be 'Unset'")
        self._text = text

    @property
    def type(self) -> "GsaRichTextType":
        """Gets the type of this GsaRichTextValue.

        Returns
        -------
        GsaRichTextType
            The type of this GsaRichTextValue.
        """
        return self._type

    @type.setter
    def type(self, type: "GsaRichTextType") -> None:
        """Sets the type of this GsaRichTextValue.

        Parameters
        ----------
        type: GsaRichTextType
            The type of this GsaRichTextValue.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

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
        if not isinstance(other, GsaRichTextValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
