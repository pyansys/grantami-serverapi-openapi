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


class GrantaServerApiExceptionsErrorDetail(ModelBase):
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
        "message": "str",
        "reason": "str",
    }

    attribute_map = {
        "message": "message",
        "reason": "reason",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        message: "Optional[str]" = None,
        reason: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiExceptionsErrorDetail - a model defined in Swagger

        Parameters
        ----------
            message: str, optional
            reason: str, optional
        """
        self._message = None
        self._reason = None

        if message is not None:
            self.message = message
        if reason is not None:
            self.reason = reason

    @property
    def message(self) -> "str":
        """Gets the message of this GrantaServerApiExceptionsErrorDetail.

        Returns
        -------
        str
            The message of this GrantaServerApiExceptionsErrorDetail.
        """
        return self._message

    @message.setter
    def message(self, message: "str") -> None:
        """Sets the message of this GrantaServerApiExceptionsErrorDetail.

        Parameters
        ----------
        message: str
            The message of this GrantaServerApiExceptionsErrorDetail.
        """
        self._message = message

    @property
    def reason(self) -> "str":
        """Gets the reason of this GrantaServerApiExceptionsErrorDetail.

        Returns
        -------
        str
            The reason of this GrantaServerApiExceptionsErrorDetail.
        """
        return self._reason

    @reason.setter
    def reason(self, reason: "str") -> None:
        """Sets the reason of this GrantaServerApiExceptionsErrorDetail.

        Parameters
        ----------
        reason: str
            The reason of this GrantaServerApiExceptionsErrorDetail.
        """
        self._reason = reason

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
        if not isinstance(other, GrantaServerApiExceptionsErrorDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
