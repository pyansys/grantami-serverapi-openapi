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
    BinaryIO,
    Dict,
    List,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase, Unset, Unset_Type


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiListsDtoRecordListSearchInfo(ModelBase):
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
        "search_result_identifier": "str",
    }

    attribute_map: Dict[str, str] = {
        "search_result_identifier": "searchResultIdentifier",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        search_result_identifier: "str",
    ) -> None:
        """GrantaServerApiListsDtoRecordListSearchInfo - a model defined in Swagger

        Parameters
        ----------
        search_result_identifier: str
        """
        self._search_result_identifier: str

        self.search_result_identifier = search_result_identifier

    @property
    def search_result_identifier(self) -> "str":
        """Gets the search_result_identifier of this GrantaServerApiListsDtoRecordListSearchInfo.

        Returns
        -------
        str
            The search_result_identifier of this GrantaServerApiListsDtoRecordListSearchInfo.
        """
        return self._search_result_identifier

    @search_result_identifier.setter
    def search_result_identifier(self, search_result_identifier: "str") -> None:
        """Sets the search_result_identifier of this GrantaServerApiListsDtoRecordListSearchInfo.

        Parameters
        ----------
        search_result_identifier: str
            The search_result_identifier of this GrantaServerApiListsDtoRecordListSearchInfo.
        """
        # Field is not nullable
        if search_result_identifier is None:
            raise ValueError(
                "Invalid value for 'search_result_identifier', must not be 'None'"
            )
        # Field is required
        if search_result_identifier is Unset:  # type: ignore[comparison-overlap]
            raise ValueError(
                "Invalid value for 'search_result_identifier', must not be 'Unset'"
            )
        self._search_result_identifier = search_result_identifier

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
        if not isinstance(other, GrantaServerApiListsDtoRecordListSearchInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
