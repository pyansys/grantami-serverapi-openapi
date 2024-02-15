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
    Dict,
    List,
    BinaryIO,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiDataExportDatumsBinaryData(ModelBase):  # type: ignore[misc]
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
        "content_type": "str",
        "data": "str",
        "description": "str",
        "name": "str",
    }

    attribute_map: Dict[str, str] = {
        "content_type": "contentType",
        "data": "data",
        "description": "description",
        "name": "name",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        content_type: "Optional[str]" = None,
        data: "Optional[str]" = None,
        description: "Optional[str]" = None,
        name: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiDataExportDatumsBinaryData - a model defined in Swagger

        Parameters
        ----------
            content_type: str, optional
            data: str, optional
            description: str, optional
            name: str, optional
        """
        self._name = None
        self._description = None
        self._content_type = None
        self._data = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if content_type is not None:
            self.content_type = content_type
        if data is not None:
            self.data = data

    @property
    def name(self) -> "Optional[str]":
        """Gets the name of this GrantaServerApiDataExportDatumsBinaryData.

        Returns
        -------
        str
            The name of this GrantaServerApiDataExportDatumsBinaryData.
        """
        return self._name

    @name.setter
    def name(self, name: "Optional[str]") -> None:
        """Sets the name of this GrantaServerApiDataExportDatumsBinaryData.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiDataExportDatumsBinaryData.
        """
        self._name = name

    @property
    def description(self) -> "Optional[str]":
        """Gets the description of this GrantaServerApiDataExportDatumsBinaryData.

        Returns
        -------
        str
            The description of this GrantaServerApiDataExportDatumsBinaryData.
        """
        return self._description

    @description.setter
    def description(self, description: "Optional[str]") -> None:
        """Sets the description of this GrantaServerApiDataExportDatumsBinaryData.

        Parameters
        ----------
        description: str
            The description of this GrantaServerApiDataExportDatumsBinaryData.
        """
        self._description = description

    @property
    def content_type(self) -> "Optional[str]":
        """Gets the content_type of this GrantaServerApiDataExportDatumsBinaryData.

        Returns
        -------
        str
            The content_type of this GrantaServerApiDataExportDatumsBinaryData.
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type: "Optional[str]") -> None:
        """Sets the content_type of this GrantaServerApiDataExportDatumsBinaryData.

        Parameters
        ----------
        content_type: str
            The content_type of this GrantaServerApiDataExportDatumsBinaryData.
        """
        self._content_type = content_type

    @property
    def data(self) -> "Optional[str]":
        """Gets the data of this GrantaServerApiDataExportDatumsBinaryData.

        Returns
        -------
        str
            The data of this GrantaServerApiDataExportDatumsBinaryData.
        """
        return self._data

    @data.setter
    def data(self, data: "Optional[str]") -> None:
        """Sets the data of this GrantaServerApiDataExportDatumsBinaryData.

        Parameters
        ----------
        data: str
            The data of this GrantaServerApiDataExportDatumsBinaryData.
        """
        self._data = data

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
        return self.to_str()  # type: ignore[no-any-return]

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiDataExportDatumsBinaryData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
