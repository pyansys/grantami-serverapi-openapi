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
from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_layouts_new_layout_item import (
    GrantaServerApiSchemaLayoutsNewLayoutItem,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaLayoutsNewLayoutCrossDatabaseLinkItem(
    GrantaServerApiSchemaLayoutsNewLayoutItem
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
        "link_group_guid": "str",
        "source_database_guid": "str",
        "source_table_guid": "str",
        "guid": "str",
        "item_type": "str",
    }

    attribute_map: Dict[str, str] = {
        "link_group_guid": "linkGroupGuid",
        "source_database_guid": "sourceDatabaseGuid",
        "source_table_guid": "sourceTableGuid",
        "guid": "guid",
        "item_type": "itemType",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        link_group_guid: "str",
        source_database_guid: "str",
        source_table_guid: "str",
        guid: "Union[str, Unset_Type]" = Unset,
        item_type: "str" = "crossDatabaseLink",
    ) -> None:
        """GrantaServerApiSchemaLayoutsNewLayoutCrossDatabaseLinkItem - a model defined in Swagger

        Parameters
        ----------
        link_group_guid: str
        source_database_guid: str
        source_table_guid: str
        guid: str, optional
        item_type: str
        """
        super().__init__(guid=guid)
        self._item_type: str
        self._source_database_guid: str
        self._source_table_guid: str
        self._link_group_guid: str

        self.item_type = item_type
        self.source_database_guid = source_database_guid
        self.source_table_guid = source_table_guid
        self.link_group_guid = link_group_guid

    @property
    def item_type(self) -> "str":
        """Gets the item_type of this GrantaServerApiSchemaLayoutsNewLayoutCrossDatabaseLinkItem.

        Returns
        -------
        str
            The item_type of this GrantaServerApiSchemaLayoutsNewLayoutCrossDatabaseLinkItem.
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type: "str") -> None:
        """Sets the item_type of this GrantaServerApiSchemaLayoutsNewLayoutCrossDatabaseLinkItem.

        Parameters
        ----------
        item_type: str
            The item_type of this GrantaServerApiSchemaLayoutsNewLayoutCrossDatabaseLinkItem.
        """
        # Field is not nullable
        if item_type is None:
            raise ValueError("Invalid value for 'item_type', must not be 'None'")
        # Field is required
        if item_type is Unset:  # type: ignore[comparison-overlap]
            raise ValueError("Invalid value for 'item_type', must not be 'Unset'")
        self._item_type = item_type

    @property
    def source_database_guid(self) -> "str":
        """Gets the source_database_guid of this GrantaServerApiSchemaLayoutsNewLayoutCrossDatabaseLinkItem.

        Returns
        -------
        str
            The source_database_guid of this GrantaServerApiSchemaLayoutsNewLayoutCrossDatabaseLinkItem.
        """
        return self._source_database_guid

    @source_database_guid.setter
    def source_database_guid(self, source_database_guid: "str") -> None:
        """Sets the source_database_guid of this GrantaServerApiSchemaLayoutsNewLayoutCrossDatabaseLinkItem.

        Parameters
        ----------
        source_database_guid: str
            The source_database_guid of this GrantaServerApiSchemaLayoutsNewLayoutCrossDatabaseLinkItem.
        """
        # Field is not nullable
        if source_database_guid is None:
            raise ValueError(
                "Invalid value for 'source_database_guid', must not be 'None'"
            )
        # Field is required
        if source_database_guid is Unset:  # type: ignore[comparison-overlap]
            raise ValueError(
                "Invalid value for 'source_database_guid', must not be 'Unset'"
            )
        self._source_database_guid = source_database_guid

    @property
    def source_table_guid(self) -> "str":
        """Gets the source_table_guid of this GrantaServerApiSchemaLayoutsNewLayoutCrossDatabaseLinkItem.

        Returns
        -------
        str
            The source_table_guid of this GrantaServerApiSchemaLayoutsNewLayoutCrossDatabaseLinkItem.
        """
        return self._source_table_guid

    @source_table_guid.setter
    def source_table_guid(self, source_table_guid: "str") -> None:
        """Sets the source_table_guid of this GrantaServerApiSchemaLayoutsNewLayoutCrossDatabaseLinkItem.

        Parameters
        ----------
        source_table_guid: str
            The source_table_guid of this GrantaServerApiSchemaLayoutsNewLayoutCrossDatabaseLinkItem.
        """
        # Field is not nullable
        if source_table_guid is None:
            raise ValueError(
                "Invalid value for 'source_table_guid', must not be 'None'"
            )
        # Field is required
        if source_table_guid is Unset:  # type: ignore[comparison-overlap]
            raise ValueError(
                "Invalid value for 'source_table_guid', must not be 'Unset'"
            )
        self._source_table_guid = source_table_guid

    @property
    def link_group_guid(self) -> "str":
        """Gets the link_group_guid of this GrantaServerApiSchemaLayoutsNewLayoutCrossDatabaseLinkItem.

        Returns
        -------
        str
            The link_group_guid of this GrantaServerApiSchemaLayoutsNewLayoutCrossDatabaseLinkItem.
        """
        return self._link_group_guid

    @link_group_guid.setter
    def link_group_guid(self, link_group_guid: "str") -> None:
        """Sets the link_group_guid of this GrantaServerApiSchemaLayoutsNewLayoutCrossDatabaseLinkItem.

        Parameters
        ----------
        link_group_guid: str
            The link_group_guid of this GrantaServerApiSchemaLayoutsNewLayoutCrossDatabaseLinkItem.
        """
        # Field is not nullable
        if link_group_guid is None:
            raise ValueError("Invalid value for 'link_group_guid', must not be 'None'")
        # Field is required
        if link_group_guid is Unset:  # type: ignore[comparison-overlap]
            raise ValueError("Invalid value for 'link_group_guid', must not be 'Unset'")
        self._link_group_guid = link_group_guid

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
            other, GrantaServerApiSchemaLayoutsNewLayoutCrossDatabaseLinkItem
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
