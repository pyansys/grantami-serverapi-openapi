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


class GrantaServerApiSchemaSubsetsCreateSubset(ModelBase):  # type: ignore[misc]
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
        "name": "str",
        "associated_layout": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "guid": "str",
    }

    attribute_map: Dict[str, str] = {
        "name": "name",
        "associated_layout": "associatedLayout",
        "guid": "guid",
    }

    subtype_mapping: Dict[str, str] = {
        "associatedLayout": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        name: "str",
        associated_layout: "Optional[GrantaServerApiSchemaSlimEntitiesSlimEntity]" = None,
        guid: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiSchemaSubsetsCreateSubset - a model defined in Swagger

        Parameters
        ----------
            name: str
            associated_layout: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
            guid: str, optional
        """
        self._associated_layout = None
        self._name: str = None  # type: ignore[assignment]
        self._guid = None

        if associated_layout is not None:
            self.associated_layout = associated_layout
        self.name = name
        if guid is not None:
            self.guid = guid

    @property
    def associated_layout(
        self,
    ) -> "Optional[GrantaServerApiSchemaSlimEntitiesSlimEntity]":
        """Gets the associated_layout of this GrantaServerApiSchemaSubsetsCreateSubset.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimEntity
            The associated_layout of this GrantaServerApiSchemaSubsetsCreateSubset.
        """
        return self._associated_layout

    @associated_layout.setter
    def associated_layout(
        self, associated_layout: "Optional[GrantaServerApiSchemaSlimEntitiesSlimEntity]"
    ) -> None:
        """Sets the associated_layout of this GrantaServerApiSchemaSubsetsCreateSubset.

        Parameters
        ----------
        associated_layout: GrantaServerApiSchemaSlimEntitiesSlimEntity
            The associated_layout of this GrantaServerApiSchemaSubsetsCreateSubset.
        """
        self._associated_layout = associated_layout

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaSubsetsCreateSubset.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaSubsetsCreateSubset.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaSubsetsCreateSubset.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaSubsetsCreateSubset.
        """
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def guid(self) -> "Optional[str]":
        """Gets the guid of this GrantaServerApiSchemaSubsetsCreateSubset.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaSubsetsCreateSubset.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Optional[str]") -> None:
        """Sets the guid of this GrantaServerApiSchemaSubsetsCreateSubset.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaSubsetsCreateSubset.
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
        return self.to_str()  # type: ignore[no-any-return]

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiSchemaSubsetsCreateSubset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
