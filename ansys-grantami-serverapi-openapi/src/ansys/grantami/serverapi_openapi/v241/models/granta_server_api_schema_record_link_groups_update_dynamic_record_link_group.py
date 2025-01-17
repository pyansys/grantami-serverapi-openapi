"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase
from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_record_link_groups_update_record_link_group import (
    GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup,
)  # noqa: F401


if TYPE_CHECKING:
    from . import *


class GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup(
    GrantaServerApiSchemaRecordLinkGroupsUpdateRecordLinkGroup
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
    swagger_types = {
        "attribute_pairs": "list[GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair]",
        "forbid_orphans": "bool",
        "guid": "str",
        "name": "str",
        "referential_integrity_model": "GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel",
        "reverse_name": "str",
        "type": "str",
    }

    attribute_map = {
        "attribute_pairs": "attributePairs",
        "forbid_orphans": "forbidOrphans",
        "guid": "guid",
        "name": "name",
        "referential_integrity_model": "referentialIntegrityModel",
        "reverse_name": "reverseName",
        "type": "type",
    }

    subtype_mapping = {
        "referentialIntegrityModel": "GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel",
        "attributePairs": "GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair",
    }

    discriminator = None

    def __init__(
        self,
        *,
        attribute_pairs: "Optional[List[GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair]]" = None,
        forbid_orphans: "Optional[bool]" = None,
        guid: "Optional[str]" = None,
        name: "Optional[str]" = None,
        referential_integrity_model: "Optional[GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel]" = None,
        reverse_name: "Optional[str]" = None,
        type: "str" = "dynamic",
    ) -> None:
        """GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup - a model defined in Swagger

        Parameters
        ----------
            attribute_pairs: List[GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair], optional
            forbid_orphans: bool, optional
            guid: str, optional
            name: str, optional
            referential_integrity_model: GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel, optional
            reverse_name: str, optional
            type: str
        """
        super().__init__(guid=guid, name=name, reverse_name=reverse_name)
        self._forbid_orphans = None
        self._referential_integrity_model = None
        self._attribute_pairs = None
        self._type = None

        if forbid_orphans is not None:
            self.forbid_orphans = forbid_orphans
        if referential_integrity_model is not None:
            self.referential_integrity_model = referential_integrity_model
        if attribute_pairs is not None:
            self.attribute_pairs = attribute_pairs
        self.type = type

    @property
    def forbid_orphans(self) -> "bool":
        """Gets the forbid_orphans of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.

        Returns
        -------
        bool
            The forbid_orphans of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.
        """
        return self._forbid_orphans

    @forbid_orphans.setter
    def forbid_orphans(self, forbid_orphans: "bool") -> None:
        """Sets the forbid_orphans of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.

        Parameters
        ----------
        forbid_orphans: bool
            The forbid_orphans of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.
        """
        self._forbid_orphans = forbid_orphans

    @property
    def referential_integrity_model(
        self,
    ) -> "GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel":
        """Gets the referential_integrity_model of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.

        Returns
        -------
        GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel
            The referential_integrity_model of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.
        """
        return self._referential_integrity_model

    @referential_integrity_model.setter
    def referential_integrity_model(
        self,
        referential_integrity_model: "GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel",
    ) -> None:
        """Sets the referential_integrity_model of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.

        Parameters
        ----------
        referential_integrity_model: GrantaServerApiSchemaRecordLinkGroupsReferentialIntegrityModel
            The referential_integrity_model of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.
        """
        self._referential_integrity_model = referential_integrity_model

    @property
    def attribute_pairs(
        self,
    ) -> "list[GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair]":
        """Gets the attribute_pairs of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.

        Returns
        -------
        list[GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair]
            The attribute_pairs of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.
        """
        return self._attribute_pairs

    @attribute_pairs.setter
    def attribute_pairs(
        self,
        attribute_pairs: "list[GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair]",
    ) -> None:
        """Sets the attribute_pairs of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.

        Parameters
        ----------
        attribute_pairs: list[GrantaServerApiSchemaRecordLinkGroupsCreateAttributeLinkPair]
            The attribute_pairs of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.
        """
        self._attribute_pairs = attribute_pairs

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

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
        if not isinstance(
            other, GrantaServerApiSchemaRecordLinkGroupsUpdateDynamicRecordLinkGroup
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
