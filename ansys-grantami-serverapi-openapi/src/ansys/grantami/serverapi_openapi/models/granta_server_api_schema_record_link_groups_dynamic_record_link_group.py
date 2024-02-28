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


class GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup(
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
        "attribute_pairs": "list[GrantaServerApiSchemaRecordLinkGroupsAttributeLinkPair]",
        "display_names": "dict(str, str)",
        "forbid_orphans": "bool",
        "guid": "str",
        "link_info": "GrantaServerApiSchemaRecordLinkGroupsLinkInfo",
        "name": "str",
        "referential_integrity_model": "GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel",
        "reverse_name": "str",
        "identity": "int",
        "reverse_display_names": "dict(str, str)",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "attribute_pairs": "attributePairs",
        "display_names": "displayNames",
        "forbid_orphans": "forbidOrphans",
        "guid": "guid",
        "link_info": "linkInfo",
        "name": "name",
        "referential_integrity_model": "referentialIntegrityModel",
        "reverse_name": "reverseName",
        "identity": "identity",
        "reverse_display_names": "reverseDisplayNames",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {
        "referentialIntegrityModel": "GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel",
        "attributePairs": "GrantaServerApiSchemaRecordLinkGroupsAttributeLinkPair",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_pairs: "List[GrantaServerApiSchemaRecordLinkGroupsAttributeLinkPair]",
        display_names: "Dict[str, str]",
        forbid_orphans: "bool",
        guid: "str",
        link_info: "GrantaServerApiSchemaRecordLinkGroupsLinkInfo",
        name: "str",
        referential_integrity_model: "GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel",
        reverse_name: "str",
        identity: "Union[int, None, Unset_Type]" = Unset,
        reverse_display_names: "Union[Dict[str, str], None, Unset_Type]" = Unset,
        type: "str" = "dynamic",
    ) -> None:
        """GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup - a model defined in Swagger

        Parameters
        ----------
        attribute_pairs: List[GrantaServerApiSchemaRecordLinkGroupsAttributeLinkPair]
        display_names: Dict[str, str]
        forbid_orphans: bool
        guid: str
        link_info: GrantaServerApiSchemaRecordLinkGroupsLinkInfo
        name: str
        referential_integrity_model: GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel
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
        self._forbid_orphans: bool
        self._referential_integrity_model: (
            GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel
        )
        self._attribute_pairs: List[
            GrantaServerApiSchemaRecordLinkGroupsAttributeLinkPair
        ]

        self.type = type
        self.forbid_orphans = forbid_orphans
        self.referential_integrity_model = referential_integrity_model
        self.attribute_pairs = attribute_pairs

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @property
    def forbid_orphans(self) -> "bool":
        """Gets the forbid_orphans of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.

        Returns
        -------
        bool
            The forbid_orphans of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.
        """
        return self._forbid_orphans

    @forbid_orphans.setter
    def forbid_orphans(self, forbid_orphans: "bool") -> None:
        """Sets the forbid_orphans of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.

        Parameters
        ----------
        forbid_orphans: bool
            The forbid_orphans of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.
        """
        # Field is not nullable
        if forbid_orphans is None:
            raise ValueError("Invalid value for 'forbid_orphans', must not be 'None'")
        # Field is required
        if forbid_orphans is Unset:  # type: ignore[comparison-overlap]
            raise ValueError("Invalid value for 'forbid_orphans', must not be 'Unset'")
        self._forbid_orphans = forbid_orphans

    @property
    def referential_integrity_model(
        self,
    ) -> "GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel":
        """Gets the referential_integrity_model of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.

        Returns
        -------
        GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel
            The referential_integrity_model of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.
        """
        return self._referential_integrity_model

    @referential_integrity_model.setter
    def referential_integrity_model(
        self,
        referential_integrity_model: "GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel",
    ) -> None:
        """Sets the referential_integrity_model of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.

        Parameters
        ----------
        referential_integrity_model: GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel
            The referential_integrity_model of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.
        """
        # Field is not nullable
        if referential_integrity_model is None:
            raise ValueError(
                "Invalid value for 'referential_integrity_model', must not be 'None'"
            )
        # Field is required
        if referential_integrity_model is Unset:  # type: ignore[comparison-overlap]
            raise ValueError(
                "Invalid value for 'referential_integrity_model', must not be 'Unset'"
            )
        self._referential_integrity_model = referential_integrity_model

    @property
    def attribute_pairs(
        self,
    ) -> "List[GrantaServerApiSchemaRecordLinkGroupsAttributeLinkPair]":
        """Gets the attribute_pairs of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.

        Returns
        -------
        List[GrantaServerApiSchemaRecordLinkGroupsAttributeLinkPair]
            The attribute_pairs of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.
        """
        return self._attribute_pairs

    @attribute_pairs.setter
    def attribute_pairs(
        self,
        attribute_pairs: "List[GrantaServerApiSchemaRecordLinkGroupsAttributeLinkPair]",
    ) -> None:
        """Sets the attribute_pairs of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.

        Parameters
        ----------
        attribute_pairs: List[GrantaServerApiSchemaRecordLinkGroupsAttributeLinkPair]
            The attribute_pairs of this GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup.
        """
        # Field is not nullable
        if attribute_pairs is None:
            raise ValueError("Invalid value for 'attribute_pairs', must not be 'None'")
        # Field is required
        if attribute_pairs is Unset:  # type: ignore[comparison-overlap]
            raise ValueError("Invalid value for 'attribute_pairs', must not be 'Unset'")
        self._attribute_pairs = attribute_pairs

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
            other, GrantaServerApiSchemaRecordLinkGroupsDynamicRecordLinkGroup
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
