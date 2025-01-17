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


class GrantaServerApiSchemaFilesUpdateFile(ModelBase):
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
        "description": "str",
        "guid": "str",
        "name": "str",
    }

    attribute_map = {
        "description": "description",
        "guid": "guid",
        "name": "name",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        description: "Optional[str]" = None,
        guid: "Optional[str]" = None,
        name: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiSchemaFilesUpdateFile - a model defined in Swagger

        Parameters
        ----------
            description: str, optional
            guid: str, optional
            name: str, optional
        """
        self._description = None
        self._name = None
        self._guid = None

        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if guid is not None:
            self.guid = guid

    @property
    def description(self) -> "str":
        """Gets the description of this GrantaServerApiSchemaFilesUpdateFile.

        Returns
        -------
        str
            The description of this GrantaServerApiSchemaFilesUpdateFile.
        """
        return self._description

    @description.setter
    def description(self, description: "str") -> None:
        """Sets the description of this GrantaServerApiSchemaFilesUpdateFile.

        Parameters
        ----------
        description: str
            The description of this GrantaServerApiSchemaFilesUpdateFile.
        """
        self._description = description

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaFilesUpdateFile.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaFilesUpdateFile.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaFilesUpdateFile.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaFilesUpdateFile.
        """
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaFilesUpdateFile.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaFilesUpdateFile.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaFilesUpdateFile.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaFilesUpdateFile.
        """
        self._guid = guid

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
        if not isinstance(other, GrantaServerApiSchemaFilesUpdateFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
