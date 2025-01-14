"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.models.gsa_sorting_value import GsaSortingValue  # noqa: F401
from ansys.grantami.serverapi_openapi.models.gsa_sorting_value_type import GsaSortingValueType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaDoubleSortingValue(GsaSortingValue):
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
        "type": "GsaSortingValueType",
        "value": "float",
    }

    attribute_map: dict[str, str] = {
        "type": "type",
        "value": "value",
    }

    subtype_mapping: dict[str, str] = {
    }

    discriminator: Optional[str] = None

    def __init__(self, *, type: "GsaSortingValueType" = GsaSortingValueType.DOUBLE, value: "Union[float, Unset_Type]" = Unset,) -> None:
        """GsaDoubleSortingValue - a model defined in Swagger

        Parameters
        ----------
        type: GsaSortingValueType
        value: float, optional
        """
        super().__init__(type=type)
        self._value: Union[float, Unset_Type] = Unset

        if value is not Unset:
            self.value = value

    @property
    def value(self) -> "Union[float, Unset_Type]":
        """Gets the value of this GsaDoubleSortingValue.

        Returns
        -------
        Union[float, Unset_Type]
            The value of this GsaDoubleSortingValue.
        """
        return self._value

    @value.setter
    def value(self, value: "Union[float, Unset_Type]") -> None:
        """Sets the value of this GsaDoubleSortingValue.

        Parameters
        ----------
        value: Union[float, Unset_Type]
            The value of this GsaDoubleSortingValue.
        """
        # Field is not nullable
        if value is None:
            raise ValueError("Invalid value for 'value', must not be 'None'")
        self._value = value

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
        if not isinstance(other, GsaDoubleSortingValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

