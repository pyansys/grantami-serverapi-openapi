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


class GrantaServerApiListsDtoUserOrGroup(ModelBase):
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
        "display_name": "str",
        "identifier": "str",
        "name": "str",
    }

    attribute_map: Dict[str, str] = {
        "display_name": "displayName",
        "identifier": "identifier",
        "name": "name",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        display_name: "str",
        identifier: "str",
        name: "str",
    ) -> None:
        """GrantaServerApiListsDtoUserOrGroup - a model defined in Swagger

        Parameters
        ----------
        display_name: str
        identifier: str
        name: str
        """
        self._identifier: str
        self._display_name: str
        self._name: str

        self.identifier = identifier
        self.display_name = display_name
        self.name = name

    @property
    def identifier(self) -> "str":
        """Gets the identifier of this GrantaServerApiListsDtoUserOrGroup.

        Returns
        -------
        str
            The identifier of this GrantaServerApiListsDtoUserOrGroup.
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier: "str") -> None:
        """Sets the identifier of this GrantaServerApiListsDtoUserOrGroup.

        Parameters
        ----------
        identifier: str
            The identifier of this GrantaServerApiListsDtoUserOrGroup.
        """
        # Field is not nullable
        if identifier is None:
            raise ValueError("Invalid value for 'identifier', must not be 'None'")
        # Field is required
        if identifier is Unset:  # type: ignore[comparison-overlap]
            raise ValueError("Invalid value for 'identifier', must not be 'Unset'")
        self._identifier = identifier

    @property
    def display_name(self) -> "str":
        """Gets the display_name of this GrantaServerApiListsDtoUserOrGroup.

        Returns
        -------
        str
            The display_name of this GrantaServerApiListsDtoUserOrGroup.
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: "str") -> None:
        """Sets the display_name of this GrantaServerApiListsDtoUserOrGroup.

        Parameters
        ----------
        display_name: str
            The display_name of this GrantaServerApiListsDtoUserOrGroup.
        """
        # Field is not nullable
        if display_name is None:
            raise ValueError("Invalid value for 'display_name', must not be 'None'")
        # Field is required
        if display_name is Unset:  # type: ignore[comparison-overlap]
            raise ValueError("Invalid value for 'display_name', must not be 'Unset'")
        self._display_name = display_name

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiListsDtoUserOrGroup.

        Returns
        -------
        str
            The name of this GrantaServerApiListsDtoUserOrGroup.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiListsDtoUserOrGroup.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiListsDtoUserOrGroup.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
        self._name = name

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
        if not isinstance(other, GrantaServerApiListsDtoUserOrGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
