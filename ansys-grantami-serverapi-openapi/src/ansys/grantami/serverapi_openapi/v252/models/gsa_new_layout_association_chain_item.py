"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.v252.models.gsa_new_layout_item import GsaNewLayoutItem  # noqa: F401
from ansys.grantami.serverapi_openapi.v252.models.gsa_new_layout_item_type import GsaNewLayoutItemType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaNewLayoutAssociationChainItem(GsaNewLayoutItem):
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
        "association_chain_links": "list[GsaNewLayoutAssociationChainLink]",
        "association_chain_name": "str",
        "item_type": "GsaNewLayoutItemType",
        "guid": "str",
    }

    attribute_map: dict[str, str] = {
        "association_chain_links": "associationChainLinks",
        "association_chain_name": "associationChainName",
        "item_type": "itemType",
        "guid": "guid",
    }

    subtype_mapping: dict[str, str] = {
        "associationChainLinks": "GsaNewLayoutAssociationChainLink",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, association_chain_links: "list[GsaNewLayoutAssociationChainLink]", association_chain_name: "str", item_type: "GsaNewLayoutItemType" = GsaNewLayoutItemType.ASSOCIATIONCHAIN, guid: "Union[str, Unset_Type]" = Unset,) -> None:
        """GsaNewLayoutAssociationChainItem - a model defined in Swagger

        Parameters
        ----------
        association_chain_links: list[GsaNewLayoutAssociationChainLink]
        association_chain_name: str
        item_type: GsaNewLayoutItemType
        guid: str, optional
        """
        super().__init__(item_type=item_type, guid=guid)
        self._association_chain_name: str
        self._association_chain_links: list[GsaNewLayoutAssociationChainLink]

        self.association_chain_name = association_chain_name
        self.association_chain_links = association_chain_links

    @property
    def association_chain_name(self) -> "str":
        """Gets the association_chain_name of this GsaNewLayoutAssociationChainItem.

        Returns
        -------
        str
            The association_chain_name of this GsaNewLayoutAssociationChainItem.
        """
        return self._association_chain_name

    @association_chain_name.setter
    def association_chain_name(self, association_chain_name: "str") -> None:
        """Sets the association_chain_name of this GsaNewLayoutAssociationChainItem.

        Parameters
        ----------
        association_chain_name: str
            The association_chain_name of this GsaNewLayoutAssociationChainItem.
        """
        # Field is not nullable
        if association_chain_name is None:
            raise ValueError("Invalid value for 'association_chain_name', must not be 'None'")
        # Field is required
        if association_chain_name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'association_chain_name', must not be 'Unset'")
        self._association_chain_name = association_chain_name

    @property
    def association_chain_links(self) -> "list[GsaNewLayoutAssociationChainLink]":
        """Gets the association_chain_links of this GsaNewLayoutAssociationChainItem.

        Returns
        -------
        list[GsaNewLayoutAssociationChainLink]
            The association_chain_links of this GsaNewLayoutAssociationChainItem.
        """
        return self._association_chain_links

    @association_chain_links.setter
    def association_chain_links(self, association_chain_links: "list[GsaNewLayoutAssociationChainLink]") -> None:
        """Sets the association_chain_links of this GsaNewLayoutAssociationChainItem.

        Parameters
        ----------
        association_chain_links: list[GsaNewLayoutAssociationChainLink]
            The association_chain_links of this GsaNewLayoutAssociationChainItem.
        """
        # Field is not nullable
        if association_chain_links is None:
            raise ValueError("Invalid value for 'association_chain_links', must not be 'None'")
        # Field is required
        if association_chain_links is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'association_chain_links', must not be 'Unset'")
        self._association_chain_links = association_chain_links

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
        if not isinstance(other, GsaNewLayoutAssociationChainItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

