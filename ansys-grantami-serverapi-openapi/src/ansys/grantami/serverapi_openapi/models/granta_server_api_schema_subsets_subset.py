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


class GrantaServerApiSchemaSubsetsSubset(ModelBase):  # type: ignore[misc]
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
        "display_names": "dict(str, str)",
        "guid": "str",
        "name": "str",
        "associated_layout": "GrantaServerApiSchemaSlimEntitiesSlimLayout",
    }

    attribute_map: Dict[str, str] = {
        "display_names": "displayNames",
        "guid": "guid",
        "name": "name",
        "associated_layout": "associatedLayout",
    }

    subtype_mapping: Dict[str, str] = {
        "associatedLayout": "GrantaServerApiSchemaSlimEntitiesSlimLayout",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        display_names: "Dict[str, str]",
        guid: "str",
        name: "str",
        associated_layout: "Optional[GrantaServerApiSchemaSlimEntitiesSlimLayout]" = None,
    ) -> None:
        """GrantaServerApiSchemaSubsetsSubset - a model defined in Swagger

        Parameters
        ----------
            display_names: Dict[str, str]
            guid: str
            name: str
            associated_layout: GrantaServerApiSchemaSlimEntitiesSlimLayout, optional
        """
        self._associated_layout = None
        self._display_names: Dict[str, str] = None  # type: ignore[assignment]
        self._name: str = None  # type: ignore[assignment]
        self._guid: str = None  # type: ignore[assignment]

        if associated_layout is not None:
            self.associated_layout = associated_layout
        self.display_names = display_names
        self.name = name
        self.guid = guid

    @property
    def associated_layout(
        self,
    ) -> "Optional[GrantaServerApiSchemaSlimEntitiesSlimLayout]":
        """Gets the associated_layout of this GrantaServerApiSchemaSubsetsSubset.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimLayout
            The associated_layout of this GrantaServerApiSchemaSubsetsSubset.
        """
        return self._associated_layout

    @associated_layout.setter
    def associated_layout(
        self, associated_layout: "Optional[GrantaServerApiSchemaSlimEntitiesSlimLayout]"
    ) -> None:
        """Sets the associated_layout of this GrantaServerApiSchemaSubsetsSubset.

        Parameters
        ----------
        associated_layout: GrantaServerApiSchemaSlimEntitiesSlimLayout
            The associated_layout of this GrantaServerApiSchemaSubsetsSubset.
        """
        self._associated_layout = associated_layout

    @property
    def display_names(self) -> "Dict[str, str]":
        """Gets the display_names of this GrantaServerApiSchemaSubsetsSubset.

        Returns
        -------
        dict(str, str)
            The display_names of this GrantaServerApiSchemaSubsetsSubset.
        """
        return self._display_names

    @display_names.setter
    def display_names(self, display_names: "Dict[str, str]") -> None:
        """Sets the display_names of this GrantaServerApiSchemaSubsetsSubset.

        Parameters
        ----------
        display_names: Dict[str, str]
            The display_names of this GrantaServerApiSchemaSubsetsSubset.
        """
        if display_names is None:
            raise ValueError("Invalid value for 'display_names', must not be 'None'")
        self._display_names = display_names

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaSubsetsSubset.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaSubsetsSubset.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaSubsetsSubset.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaSubsetsSubset.
        """
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaSubsetsSubset.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaSubsetsSubset.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaSubsetsSubset.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaSubsetsSubset.
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
        if not isinstance(other, GrantaServerApiSchemaSubsetsSubset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
