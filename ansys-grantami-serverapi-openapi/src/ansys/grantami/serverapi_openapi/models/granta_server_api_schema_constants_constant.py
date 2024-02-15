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


class GrantaServerApiSchemaConstantsConstant(ModelBase):  # type: ignore[misc]
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
        "guid": "str",
        "name": "str",
        "value": "float",
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimUnit",
    }

    attribute_map: Dict[str, str] = {
        "guid": "guid",
        "name": "name",
        "value": "value",
        "unit": "unit",
    }

    subtype_mapping: Dict[str, str] = {
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimUnit",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        guid: "str",
        name: "str",
        value: "float",
        unit: "Optional[GrantaServerApiSchemaSlimEntitiesSlimUnit]" = None,
    ) -> None:
        """GrantaServerApiSchemaConstantsConstant - a model defined in Swagger

        Parameters
        ----------
            guid: str
            name: str
            value: float
            unit: GrantaServerApiSchemaSlimEntitiesSlimUnit, optional
        """
        self._unit = None
        self._value: float = None  # type: ignore[assignment]
        self._name: str = None  # type: ignore[assignment]
        self._guid: str = None  # type: ignore[assignment]

        if unit is not None:
            self.unit = unit
        self.value = value
        self.name = name
        self.guid = guid

    @property
    def unit(self) -> "Optional[GrantaServerApiSchemaSlimEntitiesSlimUnit]":
        """Gets the unit of this GrantaServerApiSchemaConstantsConstant.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimUnit
            The unit of this GrantaServerApiSchemaConstantsConstant.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "Optional[GrantaServerApiSchemaSlimEntitiesSlimUnit]") -> None:
        """Sets the unit of this GrantaServerApiSchemaConstantsConstant.

        Parameters
        ----------
        unit: GrantaServerApiSchemaSlimEntitiesSlimUnit
            The unit of this GrantaServerApiSchemaConstantsConstant.
        """
        self._unit = unit

    @property
    def value(self) -> "float":
        """Gets the value of this GrantaServerApiSchemaConstantsConstant.

        Returns
        -------
        float
            The value of this GrantaServerApiSchemaConstantsConstant.
        """
        return self._value

    @value.setter
    def value(self, value: "float") -> None:
        """Sets the value of this GrantaServerApiSchemaConstantsConstant.

        Parameters
        ----------
        value: float
            The value of this GrantaServerApiSchemaConstantsConstant.
        """
        if value is None:
            raise ValueError("Invalid value for 'value', must not be 'None'")
        self._value = value

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaConstantsConstant.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaConstantsConstant.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaConstantsConstant.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaConstantsConstant.
        """
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaConstantsConstant.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaConstantsConstant.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaConstantsConstant.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaConstantsConstant.
        """
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        self._guid = guid

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
        if not isinstance(other, GrantaServerApiSchemaConstantsConstant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
