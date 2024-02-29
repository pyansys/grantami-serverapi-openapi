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


class GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup(ModelBase):
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
    discriminator_class_map: Dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: Dict[str, str] = {
        "link_target": "GrantaServerApiSchemaRecordLinkGroupsLinkTarget",
        "name": "str",
        "reverse_name": "str",
        "guid": "str",
    }

    attribute_map: Dict[str, str] = {
        "link_target": "linkTarget",
        "name": "name",
        "reverse_name": "reverseName",
        "guid": "guid",
    }

    subtype_mapping: Dict[str, str] = {
        "linkTarget": "GrantaServerApiSchemaRecordLinkGroupsLinkTarget",
    }

    discriminator_value_class_map = {
        "static".lower(): "#/components/schemas/GrantaServerApiSchemaRecordLinkGroupsCreateStaticRecordLinkGroup",
        "dynamic".lower(): "#/components/schemas/GrantaServerApiSchemaRecordLinkGroupsCreateDynamicRecordLinkGroup",
        "crossDatabase".lower(): "#/components/schemas/GrantaServerApiSchemaRecordLinkGroupsCreateCrossDatabaseRecordLinkGroup",
    }

    discriminator: Optional[str] = "type"

    def __init__(
        self,
        *,
        link_target: "GrantaServerApiSchemaRecordLinkGroupsLinkTarget",
        name: "str",
        reverse_name: "str",
        guid: "Union[str, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup - a model defined in Swagger

        Parameters
        ----------
        link_target: GrantaServerApiSchemaRecordLinkGroupsLinkTarget
        name: str
        reverse_name: str
        guid: str, optional
        """
        self._link_target: GrantaServerApiSchemaRecordLinkGroupsLinkTarget
        self._reverse_name: str
        self._name: str
        self._guid: Union[str, Unset_Type] = Unset

        self.link_target = link_target
        self.reverse_name = reverse_name
        self.name = name
        if guid is not Unset:
            self.guid = guid

    @property
    def link_target(self) -> "GrantaServerApiSchemaRecordLinkGroupsLinkTarget":
        """Gets the link_target of this GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup.

        Returns
        -------
        GrantaServerApiSchemaRecordLinkGroupsLinkTarget
            The link_target of this GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup.
        """
        return self._link_target

    @link_target.setter
    def link_target(
        self, link_target: "GrantaServerApiSchemaRecordLinkGroupsLinkTarget"
    ) -> None:
        """Sets the link_target of this GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup.

        Parameters
        ----------
        link_target: GrantaServerApiSchemaRecordLinkGroupsLinkTarget
            The link_target of this GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup.
        """
        # Field is not nullable
        if link_target is None:
            raise ValueError("Invalid value for 'link_target', must not be 'None'")
        # Field is required
        if link_target is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'link_target', must not be 'Unset'")
        self._link_target = link_target

    @property
    def reverse_name(self) -> "str":
        """Gets the reverse_name of this GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup.

        Returns
        -------
        str
            The reverse_name of this GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup.
        """
        return self._reverse_name

    @reverse_name.setter
    def reverse_name(self, reverse_name: "str") -> None:
        """Sets the reverse_name of this GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup.

        Parameters
        ----------
        reverse_name: str
            The reverse_name of this GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup.
        """
        # Field is not nullable
        if reverse_name is None:
            raise ValueError("Invalid value for 'reverse_name', must not be 'None'")
        # Field is required
        if reverse_name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'reverse_name', must not be 'Unset'")
        self._reverse_name = reverse_name

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
        self._name = name

    @property
    def guid(self) -> "Union[str, Unset_Type]":
        """Gets the guid of this GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup.

        Returns
        -------
        Union[str, Unset_Type]
            The guid of this GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, Unset_Type]") -> None:
        """Sets the guid of this GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup.

        Parameters
        ----------
        guid: Union[str, Unset_Type]
            The guid of this GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        self._guid = guid

    @classmethod
    def get_real_child_model(cls, data: Dict[str, str]) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[cls._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen,
        # so we have to extract it from the JSON reference
        return cls.discriminator_value_class_map[discriminator_value].rsplit("/", 1)[-1]

    @classmethod
    def _get_discriminator_field_name(cls) -> str:
        assert cls.discriminator
        name_tokens = cls.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(
            other, GrantaServerApiSchemaRecordLinkGroupsCreateRecordLinkGroup
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
