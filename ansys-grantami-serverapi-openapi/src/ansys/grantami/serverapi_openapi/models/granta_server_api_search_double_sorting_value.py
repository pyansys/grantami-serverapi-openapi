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
from ansys.grantami.serverapi_openapi.models.granta_server_api_search_sorting_value import (
    GrantaServerApiSearchSortingValue,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSearchDoubleSortingValue(GrantaServerApiSearchSortingValue):
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
        "type": "str",
        "value": "float",
    }

    attribute_map: Dict[str, str] = {
        "type": "type",
        "value": "value",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        type: "str" = "double",
        value: "Union[float, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSearchDoubleSortingValue - a model defined in Swagger

        Parameters
        ----------
        type: str
        value: float, optional
        """
        super().__init__()
        self._value: Union[float, Unset_Type] = Unset
        self._type: str

        if value is not Unset:
            self.value = value
        self.type = type

    @property
    def value(self) -> "Union[float, Unset_Type]":
        """Gets the value of this GrantaServerApiSearchDoubleSortingValue.

        Returns
        -------
        Union[float, Unset_Type]
            The value of this GrantaServerApiSearchDoubleSortingValue.
        """
        return self._value

    @value.setter
    def value(self, value: "Union[float, Unset_Type]") -> None:
        """Sets the value of this GrantaServerApiSearchDoubleSortingValue.

        Parameters
        ----------
        value: Union[float, Unset_Type]
            The value of this GrantaServerApiSearchDoubleSortingValue.
        """
        # Field is not nullable
        if value is None:
            raise ValueError("Invalid value for 'value', must not be 'None'")
        self._value = value

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchDoubleSortingValue.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchDoubleSortingValue.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchDoubleSortingValue.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchDoubleSortingValue.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

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
        if not isinstance(other, GrantaServerApiSearchDoubleSortingValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
