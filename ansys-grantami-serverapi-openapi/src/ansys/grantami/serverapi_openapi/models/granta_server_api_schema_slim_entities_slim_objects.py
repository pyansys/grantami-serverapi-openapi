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


class GrantaServerApiSchemaSlimEntitiesSlimObjects(ModelBase):  # type: ignore[misc]
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
        "attributes": "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
    }

    attribute_map: Dict[str, str] = {
        "attributes": "attributes",
    }

    subtype_mapping: Dict[str, str] = {
        "attributes": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attributes: "Optional[List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]]" = None,
    ) -> None:
        """GrantaServerApiSchemaSlimEntitiesSlimObjects - a model defined in Swagger

        Parameters
        ----------
            attributes: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity], optional
        """
        self._attributes = None

        if attributes is not None:
            self.attributes = attributes

    @property
    def attributes(
        self,
    ) -> "Optional[List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]]":
        """Gets the attributes of this GrantaServerApiSchemaSlimEntitiesSlimObjects.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The attributes of this GrantaServerApiSchemaSlimEntitiesSlimObjects.
        """
        return self._attributes

    @attributes.setter
    def attributes(
        self,
        attributes: "Optional[List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]]",
    ) -> None:
        """Sets the attributes of this GrantaServerApiSchemaSlimEntitiesSlimObjects.

        Parameters
        ----------
        attributes: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The attributes of this GrantaServerApiSchemaSlimEntitiesSlimObjects.
        """
        self._attributes = attributes

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
        if not isinstance(other, GrantaServerApiSchemaSlimEntitiesSlimObjects):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
