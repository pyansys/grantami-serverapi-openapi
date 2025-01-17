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


class GrantaServerApiAggregationsValueWithCountOfSystemGuid(ModelBase):
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
        "count": "int",
        "value": "str",
    }

    attribute_map = {
        "count": "count",
        "value": "value",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        count: "Optional[int]" = None,
        value: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiAggregationsValueWithCountOfSystemGuid - a model defined in Swagger

        Parameters
        ----------
            count: int, optional
            value: str, optional
        """
        self._value = None
        self._count = None

        if value is not None:
            self.value = value
        if count is not None:
            self.count = count

    @property
    def value(self) -> "str":
        """Gets the value of this GrantaServerApiAggregationsValueWithCountOfSystemGuid.

        Returns
        -------
        str
            The value of this GrantaServerApiAggregationsValueWithCountOfSystemGuid.
        """
        return self._value

    @value.setter
    def value(self, value: "str") -> None:
        """Sets the value of this GrantaServerApiAggregationsValueWithCountOfSystemGuid.

        Parameters
        ----------
        value: str
            The value of this GrantaServerApiAggregationsValueWithCountOfSystemGuid.
        """
        self._value = value

    @property
    def count(self) -> "int":
        """Gets the count of this GrantaServerApiAggregationsValueWithCountOfSystemGuid.

        Returns
        -------
        int
            The count of this GrantaServerApiAggregationsValueWithCountOfSystemGuid.
        """
        return self._count

    @count.setter
    def count(self, count: "int") -> None:
        """Sets the count of this GrantaServerApiAggregationsValueWithCountOfSystemGuid.

        Parameters
        ----------
        count: int
            The count of this GrantaServerApiAggregationsValueWithCountOfSystemGuid.
        """
        self._count = count

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
        if not isinstance(other, GrantaServerApiAggregationsValueWithCountOfSystemGuid):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
