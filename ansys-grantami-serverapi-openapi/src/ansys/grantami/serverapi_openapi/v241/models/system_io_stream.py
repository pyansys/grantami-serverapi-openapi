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


class SystemIOStream(ModelBase):
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
        "can_read": "bool",
        "can_seek": "bool",
        "can_timeout": "bool",
        "can_write": "bool",
        "length": "int",
        "position": "int",
        "read_timeout": "int",
        "write_timeout": "int",
    }

    attribute_map = {
        "can_read": "canRead",
        "can_seek": "canSeek",
        "can_timeout": "canTimeout",
        "can_write": "canWrite",
        "length": "length",
        "position": "position",
        "read_timeout": "readTimeout",
        "write_timeout": "writeTimeout",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        can_read: "Optional[bool]" = None,
        can_seek: "Optional[bool]" = None,
        can_timeout: "Optional[bool]" = None,
        can_write: "Optional[bool]" = None,
        length: "Optional[int]" = None,
        position: "Optional[int]" = None,
        read_timeout: "Optional[int]" = None,
        write_timeout: "Optional[int]" = None,
    ) -> None:
        """SystemIOStream - a model defined in Swagger

        Parameters
        ----------
            can_read: bool, optional
            can_seek: bool, optional
            can_timeout: bool, optional
            can_write: bool, optional
            length: int, optional
            position: int, optional
            read_timeout: int, optional
            write_timeout: int, optional
        """
        self._can_read = None
        self._can_seek = None
        self._can_timeout = None
        self._can_write = None
        self._length = None
        self._position = None
        self._read_timeout = None
        self._write_timeout = None

        if can_read is not None:
            self.can_read = can_read
        if can_seek is not None:
            self.can_seek = can_seek
        if can_timeout is not None:
            self.can_timeout = can_timeout
        if can_write is not None:
            self.can_write = can_write
        if length is not None:
            self.length = length
        if position is not None:
            self.position = position
        if read_timeout is not None:
            self.read_timeout = read_timeout
        if write_timeout is not None:
            self.write_timeout = write_timeout

    @property
    def can_read(self) -> "bool":
        """Gets the can_read of this SystemIOStream.

        Returns
        -------
        bool
            The can_read of this SystemIOStream.
        """
        return self._can_read

    @can_read.setter
    def can_read(self, can_read: "bool") -> None:
        """Sets the can_read of this SystemIOStream.

        Parameters
        ----------
        can_read: bool
            The can_read of this SystemIOStream.
        """
        self._can_read = can_read

    @property
    def can_seek(self) -> "bool":
        """Gets the can_seek of this SystemIOStream.

        Returns
        -------
        bool
            The can_seek of this SystemIOStream.
        """
        return self._can_seek

    @can_seek.setter
    def can_seek(self, can_seek: "bool") -> None:
        """Sets the can_seek of this SystemIOStream.

        Parameters
        ----------
        can_seek: bool
            The can_seek of this SystemIOStream.
        """
        self._can_seek = can_seek

    @property
    def can_timeout(self) -> "bool":
        """Gets the can_timeout of this SystemIOStream.

        Returns
        -------
        bool
            The can_timeout of this SystemIOStream.
        """
        return self._can_timeout

    @can_timeout.setter
    def can_timeout(self, can_timeout: "bool") -> None:
        """Sets the can_timeout of this SystemIOStream.

        Parameters
        ----------
        can_timeout: bool
            The can_timeout of this SystemIOStream.
        """
        self._can_timeout = can_timeout

    @property
    def can_write(self) -> "bool":
        """Gets the can_write of this SystemIOStream.

        Returns
        -------
        bool
            The can_write of this SystemIOStream.
        """
        return self._can_write

    @can_write.setter
    def can_write(self, can_write: "bool") -> None:
        """Sets the can_write of this SystemIOStream.

        Parameters
        ----------
        can_write: bool
            The can_write of this SystemIOStream.
        """
        self._can_write = can_write

    @property
    def length(self) -> "int":
        """Gets the length of this SystemIOStream.

        Returns
        -------
        int
            The length of this SystemIOStream.
        """
        return self._length

    @length.setter
    def length(self, length: "int") -> None:
        """Sets the length of this SystemIOStream.

        Parameters
        ----------
        length: int
            The length of this SystemIOStream.
        """
        self._length = length

    @property
    def position(self) -> "int":
        """Gets the position of this SystemIOStream.

        Returns
        -------
        int
            The position of this SystemIOStream.
        """
        return self._position

    @position.setter
    def position(self, position: "int") -> None:
        """Sets the position of this SystemIOStream.

        Parameters
        ----------
        position: int
            The position of this SystemIOStream.
        """
        self._position = position

    @property
    def read_timeout(self) -> "int":
        """Gets the read_timeout of this SystemIOStream.

        Returns
        -------
        int
            The read_timeout of this SystemIOStream.
        """
        return self._read_timeout

    @read_timeout.setter
    def read_timeout(self, read_timeout: "int") -> None:
        """Sets the read_timeout of this SystemIOStream.

        Parameters
        ----------
        read_timeout: int
            The read_timeout of this SystemIOStream.
        """
        self._read_timeout = read_timeout

    @property
    def write_timeout(self) -> "int":
        """Gets the write_timeout of this SystemIOStream.

        Returns
        -------
        int
            The write_timeout of this SystemIOStream.
        """
        return self._write_timeout

    @write_timeout.setter
    def write_timeout(self, write_timeout: "int") -> None:
        """Sets the write_timeout of this SystemIOStream.

        Parameters
        ----------
        write_timeout: int
            The write_timeout of this SystemIOStream.
        """
        self._write_timeout = write_timeout

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
        if not isinstance(other, SystemIOStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
