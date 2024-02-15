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


class GrantaServerApiListsDtoPagingOptions(ModelBase):  # type: ignore[misc]
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
        "page_size": "int",
        "start_index": "int",
    }

    attribute_map: Dict[str, str] = {
        "page_size": "pageSize",
        "start_index": "startIndex",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        page_size: "Optional[int]" = None,
        start_index: "Optional[int]" = None,
    ) -> None:
        """GrantaServerApiListsDtoPagingOptions - a model defined in Swagger

        Parameters
        ----------
            page_size: int, optional
            start_index: int, optional
        """
        self._start_index = None
        self._page_size = None

        if start_index is not None:
            self.start_index = start_index
        if page_size is not None:
            self.page_size = page_size

    @property
    def start_index(self) -> "Optional[int]":
        """Gets the start_index of this GrantaServerApiListsDtoPagingOptions.
        The index of the first list in the collection to be returned. If not provided it will start at index 0.

        Returns
        -------
        int
            The start_index of this GrantaServerApiListsDtoPagingOptions.
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index: "Optional[int]") -> None:
        """Sets the start_index of this GrantaServerApiListsDtoPagingOptions.
        The index of the first list in the collection to be returned. If not provided it will start at index 0.

        Parameters
        ----------
        start_index: int
            The start_index of this GrantaServerApiListsDtoPagingOptions.
        """
        self._start_index = start_index

    @property
    def page_size(self) -> "Optional[int]":
        """Gets the page_size of this GrantaServerApiListsDtoPagingOptions.
        The number of lists to be returned per page. If not provided the number of returned lists will be unlimited.

        Returns
        -------
        int
            The page_size of this GrantaServerApiListsDtoPagingOptions.
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size: "Optional[int]") -> None:
        """Sets the page_size of this GrantaServerApiListsDtoPagingOptions.
        The number of lists to be returned per page. If not provided the number of returned lists will be unlimited.

        Parameters
        ----------
        page_size: int
            The page_size of this GrantaServerApiListsDtoPagingOptions.
        """
        self._page_size = page_size

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
        if not isinstance(other, GrantaServerApiListsDtoPagingOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
