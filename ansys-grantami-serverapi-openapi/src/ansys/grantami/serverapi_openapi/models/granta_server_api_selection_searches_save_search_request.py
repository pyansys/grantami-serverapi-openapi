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


class GrantaServerApiSelectionSearchesSaveSearchRequest(ModelBase):  # type: ignore[misc]
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
        "detail": "GrantaServerApiSelectionSearchesSearchDetail",
        "search_config": "str",
    }

    attribute_map: Dict[str, str] = {
        "detail": "detail",
        "search_config": "searchConfig",
    }

    subtype_mapping: Dict[str, str] = {
        "detail": "GrantaServerApiSelectionSearchesSearchDetail",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        detail: "Optional[GrantaServerApiSelectionSearchesSearchDetail]" = None,
        search_config: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiSelectionSearchesSaveSearchRequest - a model defined in Swagger

        Parameters
        ----------
            detail: GrantaServerApiSelectionSearchesSearchDetail, optional
            search_config: str, optional
        """
        self._search_config = None
        self._detail = None

        if search_config is not None:
            self.search_config = search_config
        if detail is not None:
            self.detail = detail

    @property
    def search_config(self) -> "Optional[str]":
        """Gets the search_config of this GrantaServerApiSelectionSearchesSaveSearchRequest.

        Returns
        -------
        str
            The search_config of this GrantaServerApiSelectionSearchesSaveSearchRequest.
        """
        return self._search_config

    @search_config.setter
    def search_config(self, search_config: "Optional[str]") -> None:
        """Sets the search_config of this GrantaServerApiSelectionSearchesSaveSearchRequest.

        Parameters
        ----------
        search_config: str
            The search_config of this GrantaServerApiSelectionSearchesSaveSearchRequest.
        """
        self._search_config = search_config

    @property
    def detail(self) -> "Optional[GrantaServerApiSelectionSearchesSearchDetail]":
        """Gets the detail of this GrantaServerApiSelectionSearchesSaveSearchRequest.

        Returns
        -------
        GrantaServerApiSelectionSearchesSearchDetail
            The detail of this GrantaServerApiSelectionSearchesSaveSearchRequest.
        """
        return self._detail

    @detail.setter
    def detail(
        self, detail: "Optional[GrantaServerApiSelectionSearchesSearchDetail]"
    ) -> None:
        """Sets the detail of this GrantaServerApiSelectionSearchesSaveSearchRequest.

        Parameters
        ----------
        detail: GrantaServerApiSelectionSearchesSearchDetail
            The detail of this GrantaServerApiSelectionSearchesSaveSearchRequest.
        """
        self._detail = detail

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
        if not isinstance(other, GrantaServerApiSelectionSearchesSaveSearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
