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


class GrantaServerApiSchemaSlimEntitiesSlimConstant(ModelBase):
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
    }

    attribute_map = {
        "guid": "guid",
        "name": "name",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        guid: "str",
        name: "str",
    ) -> None:
        """GrantaServerApiSchemaSlimEntitiesSlimConstant - a model defined in Swagger

        Parameters
        ----------
            guid: str
            name: str
        """
        self._name = None
        self._guid = None

        self.name = name
        self.guid = guid

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaSlimEntitiesSlimConstant.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaSlimEntitiesSlimConstant.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaSlimEntitiesSlimConstant.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaSlimEntitiesSlimConstant.
        """
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaSlimEntitiesSlimConstant.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaSlimEntitiesSlimConstant.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaSlimEntitiesSlimConstant.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaSlimEntitiesSlimConstant.
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
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiSchemaSlimEntitiesSlimConstant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
