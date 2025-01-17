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


class GrantaServerApiSchemaConstantsUpdateConstant(ModelBase):
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
        "guid": "str",
        "name": "str",
        "unit_guid": "str",
        "value": "float",
    }

    attribute_map = {
        "guid": "guid",
        "name": "name",
        "unit_guid": "unitGuid",
        "value": "value",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        guid: "Optional[str]" = None,
        name: "Optional[str]" = None,
        unit_guid: "Optional[str]" = None,
        value: "Optional[float]" = None,
    ) -> None:
        """GrantaServerApiSchemaConstantsUpdateConstant - a model defined in Swagger

        Parameters
        ----------
            guid: str, optional
            name: str, optional
            unit_guid: str, optional
            value: float, optional
        """
        self._unit_guid = None
        self._value = None
        self._name = None
        self._guid = None

        if unit_guid is not None:
            self.unit_guid = unit_guid
        if value is not None:
            self.value = value
        if name is not None:
            self.name = name
        if guid is not None:
            self.guid = guid

    @property
    def unit_guid(self) -> "str":
        """Gets the unit_guid of this GrantaServerApiSchemaConstantsUpdateConstant.

        Returns
        -------
        str
            The unit_guid of this GrantaServerApiSchemaConstantsUpdateConstant.
        """
        return self._unit_guid

    @unit_guid.setter
    def unit_guid(self, unit_guid: "str") -> None:
        """Sets the unit_guid of this GrantaServerApiSchemaConstantsUpdateConstant.

        Parameters
        ----------
        unit_guid: str
            The unit_guid of this GrantaServerApiSchemaConstantsUpdateConstant.
        """
        self._unit_guid = unit_guid

    @property
    def value(self) -> "float":
        """Gets the value of this GrantaServerApiSchemaConstantsUpdateConstant.

        Returns
        -------
        float
            The value of this GrantaServerApiSchemaConstantsUpdateConstant.
        """
        return self._value

    @value.setter
    def value(self, value: "float") -> None:
        """Sets the value of this GrantaServerApiSchemaConstantsUpdateConstant.

        Parameters
        ----------
        value: float
            The value of this GrantaServerApiSchemaConstantsUpdateConstant.
        """
        self._value = value

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaConstantsUpdateConstant.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaConstantsUpdateConstant.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaConstantsUpdateConstant.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaConstantsUpdateConstant.
        """
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaConstantsUpdateConstant.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaConstantsUpdateConstant.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaConstantsUpdateConstant.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaConstantsUpdateConstant.
        """
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
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiSchemaConstantsUpdateConstant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
