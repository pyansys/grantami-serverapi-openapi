"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
    from . import *

class GrantaServerApiListsDtoRecordListSearchResult(ModelBase):
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

    """
    swagger_types = {
        "header": "GrantaServerApiListsDtoRecordListHeader",
        "items": "list[GrantaServerApiListsDtoListItem]",
    }

    attribute_map = {
        "header": "header",
        "items": "items",
    }

    subtype_mapping = {
        "header": "GrantaServerApiListsDtoRecordListHeader",
        "items": "GrantaServerApiListsDtoListItem",
    }

    def __init__(self, *, header: "Optional[GrantaServerApiListsDtoRecordListHeader]" = None, items: "Optional[List[GrantaServerApiListsDtoListItem]]" = None) -> None:
        """GrantaServerApiListsDtoRecordListSearchResult - a model defined in Swagger

        Parameters
        ----------
            header: GrantaServerApiListsDtoRecordListHeader, optional
            items: List[GrantaServerApiListsDtoListItem], optional
        """
        self._header = None
        self._items = None
        self.discriminator = None
        if header is not None:
            self.header = header
        if items is not None:
            self.items = items

    @property
    def header(self) -> "GrantaServerApiListsDtoRecordListHeader":
        """Gets the header of this GrantaServerApiListsDtoRecordListSearchResult.

        Returns
        -------
        GrantaServerApiListsDtoRecordListHeader
            The header of this GrantaServerApiListsDtoRecordListSearchResult.
        """
        return self._header

    @header.setter
    def header(self, header: "GrantaServerApiListsDtoRecordListHeader") -> None:
        """Sets the header of this GrantaServerApiListsDtoRecordListSearchResult.

        Parameters
        ----------
        header: GrantaServerApiListsDtoRecordListHeader
            The header of this GrantaServerApiListsDtoRecordListSearchResult.
        """
        self._header = header

    @property
    def items(self) -> "list[GrantaServerApiListsDtoListItem]":
        """Gets the items of this GrantaServerApiListsDtoRecordListSearchResult.

        Returns
        -------
        list[GrantaServerApiListsDtoListItem]
            The items of this GrantaServerApiListsDtoRecordListSearchResult.
        """
        return self._items

    @items.setter
    def items(self, items: "list[GrantaServerApiListsDtoListItem]") -> None:
        """Sets the items of this GrantaServerApiListsDtoRecordListSearchResult.

        Parameters
        ----------
        items: list[GrantaServerApiListsDtoListItem]
            The items of this GrantaServerApiListsDtoRecordListSearchResult.
        """
        self._items = items

    def get_real_child_model(self, data: ModelBase) -> str:
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

    def to_dict(self) -> Dict:
        """Returns the model properties as a dict

        Returns
        -------
        Dict
            Dictionary indexed by property name containing all the model properties
        """
        result = {}

        for attr in self.swagger_types.keys():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GrantaServerApiListsDtoRecordListSearchResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model

        Returns
        -------
        str
            String representation of the model as a dictionary
        """
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiListsDtoRecordListSearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
