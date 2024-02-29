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
from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_record_link_groups_record_link_group import (
    GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaRecordLinkGroupsCrossDatabaseRecordLinkGroup(
    GrantaServerApiSchemaRecordLinkGroupsRecordLinkGroup
):
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
        "include_indirect_links": "bool",
        "link_info": "GrantaServerApiSchemaRecordLinkGroupsLinkInfo",
        "name": "str",
        "reverse_name": "str",
        "identity": "int",
        "reverse_display_names": "dict(str, str)",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "display_names": "displayNames",
        "guid": "guid",
        "include_indirect_links": "includeIndirectLinks",
        "link_info": "linkInfo",
        "name": "name",
        "reverse_name": "reverseName",
        "identity": "identity",
        "reverse_display_names": "reverseDisplayNames",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        display_names: "Dict[str, str]",
        guid: "str",
        include_indirect_links: "bool",
        link_info: "GrantaServerApiSchemaRecordLinkGroupsLinkInfo",
        name: "str",
        reverse_name: "str",
        identity: "Union[int, None, Unset_Type]" = Unset,
        reverse_display_names: "Union[Dict[str, str], None, Unset_Type]" = Unset,
        type: "str" = "crossDatabase",
    ) -> None:
        """GrantaServerApiSchemaRecordLinkGroupsCrossDatabaseRecordLinkGroup - a model defined in Swagger

        Parameters
        ----------
        display_names: Dict[str, str]
        guid: str
        include_indirect_links: bool
        link_info: GrantaServerApiSchemaRecordLinkGroupsLinkInfo
        name: str
        reverse_name: str
        identity: int, optional
        reverse_display_names: Dict[str, str], optional
        type: str
        """
        super().__init__(
            display_names=display_names,
            guid=guid,
            link_info=link_info,
            name=name,
            reverse_name=reverse_name,
            identity=identity,
            reverse_display_names=reverse_display_names,
        )
        self._type: str
        self._include_indirect_links: bool

        self.type = type
        self.include_indirect_links = include_indirect_links

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaRecordLinkGroupsCrossDatabaseRecordLinkGroup.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaRecordLinkGroupsCrossDatabaseRecordLinkGroup.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaRecordLinkGroupsCrossDatabaseRecordLinkGroup.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaRecordLinkGroupsCrossDatabaseRecordLinkGroup.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @property
    def include_indirect_links(self) -> "bool":
        """Gets the include_indirect_links of this GrantaServerApiSchemaRecordLinkGroupsCrossDatabaseRecordLinkGroup.

        Returns
        -------
        bool
            The include_indirect_links of this GrantaServerApiSchemaRecordLinkGroupsCrossDatabaseRecordLinkGroup.
        """
        return self._include_indirect_links

    @include_indirect_links.setter
    def include_indirect_links(self, include_indirect_links: "bool") -> None:
        """Sets the include_indirect_links of this GrantaServerApiSchemaRecordLinkGroupsCrossDatabaseRecordLinkGroup.

        Parameters
        ----------
        include_indirect_links: bool
            The include_indirect_links of this GrantaServerApiSchemaRecordLinkGroupsCrossDatabaseRecordLinkGroup.
        """
        # Field is not nullable
        if include_indirect_links is None:
            raise ValueError(
                "Invalid value for 'include_indirect_links', must not be 'None'"
            )
        # Field is required
        if include_indirect_links is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'include_indirect_links', must not be 'Unset'"
            )
        self._include_indirect_links = include_indirect_links

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
        if not isinstance(
            other, GrantaServerApiSchemaRecordLinkGroupsCrossDatabaseRecordLinkGroup
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
