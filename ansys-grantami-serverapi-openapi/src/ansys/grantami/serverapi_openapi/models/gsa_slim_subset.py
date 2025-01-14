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


class GsaSlimSubset(ModelBase):
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
        "display_names": "dict(str, str)",
        "guid": "str",
        "name": "str",
    }

    attribute_map: dict[str, str] = {
        "display_names": "displayNames",
        "guid": "guid",
        "name": "name",
    }

    subtype_mapping: dict[str, str] = {
    }

    discriminator: Optional[str] = None

    def __init__(self, *, display_names: "dict[str, str]", guid: "str", name: "str",) -> None:
        """GsaSlimSubset - a model defined in Swagger

        Parameters
        ----------
        display_names: dict[str, str]
        guid: str
        name: str
        """
        self._display_names: dict[str, str]
        self._name: str
        self._guid: str

        self.display_names = display_names
        self.name = name
        self.guid = guid

    @property
    def display_names(self) -> "dict[str, str]":
        """Gets the display_names of this GsaSlimSubset.

        Returns
        -------
        dict[str, str]
            The display_names of this GsaSlimSubset.
        """
        return self._display_names

    @display_names.setter
    def display_names(self, display_names: "dict[str, str]") -> None:
        """Sets the display_names of this GsaSlimSubset.

        Parameters
        ----------
        display_names: dict[str, str]
            The display_names of this GsaSlimSubset.
        """
        # Field is not nullable
        if display_names is None:
            raise ValueError("Invalid value for 'display_names', must not be 'None'")
        # Field is required
        if display_names is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'display_names', must not be 'Unset'")
        self._display_names = display_names

    @property
    def name(self) -> "str":
        """Gets the name of this GsaSlimSubset.

        Returns
        -------
        str
            The name of this GsaSlimSubset.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GsaSlimSubset.

        Parameters
        ----------
        name: str
            The name of this GsaSlimSubset.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GsaSlimSubset.

        Returns
        -------
        str
            The guid of this GsaSlimSubset.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GsaSlimSubset.

        Parameters
        ----------
        guid: str
            The guid of this GsaSlimSubset.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        # Field is required
        if guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'guid', must not be 'Unset'")
        self._guid = guid

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
        if not isinstance(other, GsaSlimSubset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

