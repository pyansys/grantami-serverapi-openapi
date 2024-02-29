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


class GrantaServerApiAggregationsValueWithCountOfSystemInt32(ModelBase):
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
        "count": "int",
        "value": "int",
    }

    attribute_map: Dict[str, str] = {
        "count": "count",
        "value": "value",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        count: "Union[int, Unset_Type]" = Unset,
        value: "Union[int, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiAggregationsValueWithCountOfSystemInt32 - a model defined in Swagger

        Parameters
        ----------
        count: int, optional
        value: int, optional
        """
        self._value: Union[int, Unset_Type] = Unset
        self._count: Union[int, Unset_Type] = Unset

        if value is not Unset:
            self.value = value
        if count is not Unset:
            self.count = count

    @property
    def value(self) -> "Union[int, Unset_Type]":
        """Gets the value of this GrantaServerApiAggregationsValueWithCountOfSystemInt32.

        Returns
        -------
        Union[int, Unset_Type]
            The value of this GrantaServerApiAggregationsValueWithCountOfSystemInt32.
        """
        return self._value

    @value.setter
    def value(self, value: "Union[int, Unset_Type]") -> None:
        """Sets the value of this GrantaServerApiAggregationsValueWithCountOfSystemInt32.

        Parameters
        ----------
        value: Union[int, Unset_Type]
            The value of this GrantaServerApiAggregationsValueWithCountOfSystemInt32.
        """
        # Field is not nullable
        if value is None:
            raise ValueError("Invalid value for 'value', must not be 'None'")
        self._value = value

    @property
    def count(self) -> "Union[int, Unset_Type]":
        """Gets the count of this GrantaServerApiAggregationsValueWithCountOfSystemInt32.

        Returns
        -------
        Union[int, Unset_Type]
            The count of this GrantaServerApiAggregationsValueWithCountOfSystemInt32.
        """
        return self._count

    @count.setter
    def count(self, count: "Union[int, Unset_Type]") -> None:
        """Sets the count of this GrantaServerApiAggregationsValueWithCountOfSystemInt32.

        Parameters
        ----------
        count: Union[int, Unset_Type]
            The count of this GrantaServerApiAggregationsValueWithCountOfSystemInt32.
        """
        # Field is not nullable
        if count is None:
            raise ValueError("Invalid value for 'count', must not be 'None'")
        self._count = count

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
        if not isinstance(
            other, GrantaServerApiAggregationsValueWithCountOfSystemInt32
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
