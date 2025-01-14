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


class GsaDeleteRecordListItems(ModelBase):
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
        "items": "list[GsaDeleteRecordListItem]",
    }

    attribute_map: dict[str, str] = {
        "items": "items",
    }

    subtype_mapping: dict[str, str] = {
        "items": "GsaDeleteRecordListItem",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, items: "list[GsaDeleteRecordListItem]",) -> None:
        """GsaDeleteRecordListItems - a model defined in Swagger

        Parameters
        ----------
        items: list[GsaDeleteRecordListItem]
        """
        self._items: list[GsaDeleteRecordListItem]

        self.items = items

    @property
    def items(self) -> "list[GsaDeleteRecordListItem]":
        """Gets the items of this GsaDeleteRecordListItems.

        Returns
        -------
        list[GsaDeleteRecordListItem]
            The items of this GsaDeleteRecordListItems.
        """
        return self._items

    @items.setter
    def items(self, items: "list[GsaDeleteRecordListItem]") -> None:
        """Sets the items of this GsaDeleteRecordListItems.

        Parameters
        ----------
        items: list[GsaDeleteRecordListItem]
            The items of this GsaDeleteRecordListItems.
        """
        # Field is not nullable
        if items is None:
            raise ValueError("Invalid value for 'items', must not be 'None'")
        # Field is required
        if items is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'items', must not be 'Unset'")
        self._items = items

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
        if not isinstance(other, GsaDeleteRecordListItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

