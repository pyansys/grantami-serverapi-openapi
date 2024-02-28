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


class GrantaServerApiSchemaRecordLinkGroupsLinkInfo(ModelBase):
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
        "link_source": "GrantaServerApiSchemaRecordLinkGroupsLinkTarget",
        "link_target": "GrantaServerApiSchemaRecordLinkGroupsLinkTarget",
    }

    attribute_map: Dict[str, str] = {
        "link_source": "linkSource",
        "link_target": "linkTarget",
    }

    subtype_mapping: Dict[str, str] = {
        "linkSource": "GrantaServerApiSchemaRecordLinkGroupsLinkTarget",
        "linkTarget": "GrantaServerApiSchemaRecordLinkGroupsLinkTarget",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        link_source: "GrantaServerApiSchemaRecordLinkGroupsLinkTarget",
        link_target: "GrantaServerApiSchemaRecordLinkGroupsLinkTarget",
    ) -> None:
        """GrantaServerApiSchemaRecordLinkGroupsLinkInfo - a model defined in Swagger

        Parameters
        ----------
        link_source: GrantaServerApiSchemaRecordLinkGroupsLinkTarget
        link_target: GrantaServerApiSchemaRecordLinkGroupsLinkTarget
        """
        self._link_source: GrantaServerApiSchemaRecordLinkGroupsLinkTarget
        self._link_target: GrantaServerApiSchemaRecordLinkGroupsLinkTarget

        self.link_source = link_source
        self.link_target = link_target

    @property
    def link_source(self) -> "GrantaServerApiSchemaRecordLinkGroupsLinkTarget":
        """Gets the link_source of this GrantaServerApiSchemaRecordLinkGroupsLinkInfo.

        Returns
        -------
        GrantaServerApiSchemaRecordLinkGroupsLinkTarget
            The link_source of this GrantaServerApiSchemaRecordLinkGroupsLinkInfo.
        """
        return self._link_source

    @link_source.setter
    def link_source(
        self, link_source: "GrantaServerApiSchemaRecordLinkGroupsLinkTarget"
    ) -> None:
        """Sets the link_source of this GrantaServerApiSchemaRecordLinkGroupsLinkInfo.

        Parameters
        ----------
        link_source: GrantaServerApiSchemaRecordLinkGroupsLinkTarget
            The link_source of this GrantaServerApiSchemaRecordLinkGroupsLinkInfo.
        """
        # Field is not nullable
        if link_source is None:
            raise ValueError("Invalid value for 'link_source', must not be 'None'")
        # Field is required
        if link_source is Unset:  # type: ignore[comparison-overlap]
            raise ValueError("Invalid value for 'link_source', must not be 'Unset'")
        self._link_source = link_source

    @property
    def link_target(self) -> "GrantaServerApiSchemaRecordLinkGroupsLinkTarget":
        """Gets the link_target of this GrantaServerApiSchemaRecordLinkGroupsLinkInfo.

        Returns
        -------
        GrantaServerApiSchemaRecordLinkGroupsLinkTarget
            The link_target of this GrantaServerApiSchemaRecordLinkGroupsLinkInfo.
        """
        return self._link_target

    @link_target.setter
    def link_target(
        self, link_target: "GrantaServerApiSchemaRecordLinkGroupsLinkTarget"
    ) -> None:
        """Sets the link_target of this GrantaServerApiSchemaRecordLinkGroupsLinkInfo.

        Parameters
        ----------
        link_target: GrantaServerApiSchemaRecordLinkGroupsLinkTarget
            The link_target of this GrantaServerApiSchemaRecordLinkGroupsLinkInfo.
        """
        # Field is not nullable
        if link_target is None:
            raise ValueError("Invalid value for 'link_target', must not be 'None'")
        # Field is required
        if link_target is Unset:  # type: ignore[comparison-overlap]
            raise ValueError("Invalid value for 'link_target', must not be 'Unset'")
        self._link_target = link_target

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
        if not isinstance(other, GrantaServerApiSchemaRecordLinkGroupsLinkInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
