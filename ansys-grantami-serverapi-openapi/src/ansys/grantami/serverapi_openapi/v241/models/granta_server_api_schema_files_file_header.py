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


class GrantaServerApiSchemaFilesFileHeader(ModelBase):
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
        "data_length": "int",
        "description": "str",
        "extension": "str",
        "folder_guid": "str",
        "guid": "str",
        "name": "str",
        "path": "str",
    }

    attribute_map = {
        "data_length": "dataLength",
        "description": "description",
        "extension": "extension",
        "folder_guid": "folderGuid",
        "guid": "guid",
        "name": "name",
        "path": "path",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        data_length: "int",
        description: "str",
        extension: "str",
        folder_guid: "str",
        guid: "str",
        name: "str",
        path: "str",
    ) -> None:
        """GrantaServerApiSchemaFilesFileHeader - a model defined in Swagger

        Parameters
        ----------
            data_length: int
            description: str
            extension: str
            folder_guid: str
            guid: str
            name: str
            path: str
        """
        self._folder_guid = None
        self._description = None
        self._extension = None
        self._data_length = None
        self._path = None
        self._name = None
        self._guid = None

        self.folder_guid = folder_guid
        self.description = description
        self.extension = extension
        self.data_length = data_length
        self.path = path
        self.name = name
        self.guid = guid

    @property
    def folder_guid(self) -> "str":
        """Gets the folder_guid of this GrantaServerApiSchemaFilesFileHeader.

        Returns
        -------
        str
            The folder_guid of this GrantaServerApiSchemaFilesFileHeader.
        """
        return self._folder_guid

    @folder_guid.setter
    def folder_guid(self, folder_guid: "str") -> None:
        """Sets the folder_guid of this GrantaServerApiSchemaFilesFileHeader.

        Parameters
        ----------
        folder_guid: str
            The folder_guid of this GrantaServerApiSchemaFilesFileHeader.
        """
        if folder_guid is None:
            raise ValueError("Invalid value for 'folder_guid', must not be 'None'")
        self._folder_guid = folder_guid

    @property
    def description(self) -> "str":
        """Gets the description of this GrantaServerApiSchemaFilesFileHeader.

        Returns
        -------
        str
            The description of this GrantaServerApiSchemaFilesFileHeader.
        """
        return self._description

    @description.setter
    def description(self, description: "str") -> None:
        """Sets the description of this GrantaServerApiSchemaFilesFileHeader.

        Parameters
        ----------
        description: str
            The description of this GrantaServerApiSchemaFilesFileHeader.
        """
        if description is None:
            raise ValueError("Invalid value for 'description', must not be 'None'")
        self._description = description

    @property
    def extension(self) -> "str":
        """Gets the extension of this GrantaServerApiSchemaFilesFileHeader.

        Returns
        -------
        str
            The extension of this GrantaServerApiSchemaFilesFileHeader.
        """
        return self._extension

    @extension.setter
    def extension(self, extension: "str") -> None:
        """Sets the extension of this GrantaServerApiSchemaFilesFileHeader.

        Parameters
        ----------
        extension: str
            The extension of this GrantaServerApiSchemaFilesFileHeader.
        """
        if extension is None:
            raise ValueError("Invalid value for 'extension', must not be 'None'")
        self._extension = extension

    @property
    def data_length(self) -> "int":
        """Gets the data_length of this GrantaServerApiSchemaFilesFileHeader.

        Returns
        -------
        int
            The data_length of this GrantaServerApiSchemaFilesFileHeader.
        """
        return self._data_length

    @data_length.setter
    def data_length(self, data_length: "int") -> None:
        """Sets the data_length of this GrantaServerApiSchemaFilesFileHeader.

        Parameters
        ----------
        data_length: int
            The data_length of this GrantaServerApiSchemaFilesFileHeader.
        """
        if data_length is None:
            raise ValueError("Invalid value for 'data_length', must not be 'None'")
        self._data_length = data_length

    @property
    def path(self) -> "str":
        """Gets the path of this GrantaServerApiSchemaFilesFileHeader.

        Returns
        -------
        str
            The path of this GrantaServerApiSchemaFilesFileHeader.
        """
        return self._path

    @path.setter
    def path(self, path: "str") -> None:
        """Sets the path of this GrantaServerApiSchemaFilesFileHeader.

        Parameters
        ----------
        path: str
            The path of this GrantaServerApiSchemaFilesFileHeader.
        """
        if path is None:
            raise ValueError("Invalid value for 'path', must not be 'None'")
        self._path = path

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaFilesFileHeader.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaFilesFileHeader.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaFilesFileHeader.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaFilesFileHeader.
        """
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaFilesFileHeader.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaFilesFileHeader.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaFilesFileHeader.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaFilesFileHeader.
        """
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
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
        if not isinstance(other, GrantaServerApiSchemaFilesFileHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
