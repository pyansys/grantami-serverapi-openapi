"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.v252.models.gsa_create_parameter_value import GsaCreateParameterValue  # noqa: F401
from ansys.grantami.serverapi_openapi.v252.models.gsa_parameter_value_type import GsaParameterValueType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaCreateNumericParameterValue(GsaCreateParameterValue):
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
        "type": "GsaParameterValueType",
        "value": "float",
        "guid": "str",
        "name": "str",
    }

    attribute_map: dict[str, str] = {
        "type": "type",
        "value": "value",
        "guid": "guid",
        "name": "name",
    }

    subtype_mapping: dict[str, str] = {
    }

    discriminator: Optional[str] = None

    def __init__(self, *, type: "GsaParameterValueType" = GsaParameterValueType.NUMERIC, value: "float", guid: "Union[str, Unset_Type]" = Unset, name: "Union[str, None, Unset_Type]" = Unset,) -> None:
        """GsaCreateNumericParameterValue - a model defined in Swagger

        Parameters
        ----------
        type: GsaParameterValueType
        value: float
        guid: str, optional
        name: str, optional
        """
        super().__init__(type=type, guid=guid)
        self._value: float
        self._name: Union[str, None, Unset_Type] = Unset

        self.value = value
        if name is not Unset:
            self.name = name

    @property
    def value(self) -> "float":
        """Gets the value of this GsaCreateNumericParameterValue.

        Returns
        -------
        float
            The value of this GsaCreateNumericParameterValue.
        """
        return self._value

    @value.setter
    def value(self, value: "float") -> None:
        """Sets the value of this GsaCreateNumericParameterValue.

        Parameters
        ----------
        value: float
            The value of this GsaCreateNumericParameterValue.
        """
        # Field is not nullable
        if value is None:
            raise ValueError("Invalid value for 'value', must not be 'None'")
        # Field is required
        if value is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'value', must not be 'Unset'")
        self._value = value

    @property
    def name(self) -> "Union[str, None, Unset_Type]":
        """Gets the name of this GsaCreateNumericParameterValue.

        Returns
        -------
        Union[str, None, Unset_Type]
            The name of this GsaCreateNumericParameterValue.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, None, Unset_Type]") -> None:
        """Sets the name of this GsaCreateNumericParameterValue.

        Parameters
        ----------
        name: Union[str, None, Unset_Type]
            The name of this GsaCreateNumericParameterValue.
        """
        self._name = name

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
        if not isinstance(other, GsaCreateNumericParameterValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

