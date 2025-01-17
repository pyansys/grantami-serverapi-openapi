"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase
from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_layouts_new_layout_item import (
    GrantaServerApiSchemaLayoutsNewLayoutItem,
)  # noqa: F401


if TYPE_CHECKING:
    from . import *


class GrantaServerApiSchemaLayoutsNewLayoutAttributeItem(
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
    swagger_types = {
        "attribute_guid": "str",
        "guid": "str",
        "item_type": "str",
        "meta_attributes": "list[GrantaServerApiSchemaLayoutsNewLayoutAttributeItem]",
        "read_only": "bool",
        "required": "bool",
        "tabular_column_guids": "list[str]",
    }

    attribute_map = {
        "attribute_guid": "attributeGuid",
        "guid": "guid",
        "item_type": "itemType",
        "meta_attributes": "metaAttributes",
        "read_only": "readOnly",
        "required": "required",
        "tabular_column_guids": "tabularColumnGuids",
    }

    subtype_mapping = {
        "metaAttributes": "GrantaServerApiSchemaLayoutsNewLayoutAttributeItem",
    }

    discriminator = None

    def __init__(
        self,
        *,
        attribute_guid: "str",
        guid: "Optional[str]" = None,
        item_type: "str" = "attribute",
        meta_attributes: "Optional[List[GrantaServerApiSchemaLayoutsNewLayoutAttributeItem]]" = None,
        read_only: "Optional[bool]" = None,
        required: "Optional[bool]" = None,
        tabular_column_guids: "Optional[List[str]]" = None,
    ) -> None:
        """GrantaServerApiSchemaLayoutsNewLayoutAttributeItem - a model defined in Swagger

        Parameters
        ----------
            attribute_guid: str
            guid: str, optional
            item_type: str
            meta_attributes: List[GrantaServerApiSchemaLayoutsNewLayoutAttributeItem], optional
            read_only: bool, optional
            required: bool, optional
            tabular_column_guids: List[str], optional
        """
        super().__init__(guid=guid)
        self._item_type = None
        self._attribute_guid = None
        self._required = None
        self._read_only = None
        self._meta_attributes = None
        self._tabular_column_guids = None

        self.item_type = item_type
        self.attribute_guid = attribute_guid
        if required is not None:
            self.required = required
        if read_only is not None:
            self.read_only = read_only
        if meta_attributes is not None:
            self.meta_attributes = meta_attributes
        if tabular_column_guids is not None:
            self.tabular_column_guids = tabular_column_guids

    @property
    def item_type(self) -> "str":
        """Gets the item_type of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.

        Returns
        -------
        str
            The item_type of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type: "str") -> None:
        """Sets the item_type of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.

        Parameters
        ----------
        item_type: str
            The item_type of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.
        """
        if item_type is None:
            raise ValueError("Invalid value for 'item_type', must not be 'None'")
        self._item_type = item_type

    @property
    def attribute_guid(self) -> "str":
        """Gets the attribute_guid of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.

        Returns
        -------
        str
            The attribute_guid of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.
        """
        return self._attribute_guid

    @attribute_guid.setter
    def attribute_guid(self, attribute_guid: "str") -> None:
        """Sets the attribute_guid of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.

        Parameters
        ----------
        attribute_guid: str
            The attribute_guid of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.
        """
        if attribute_guid is None:
            raise ValueError("Invalid value for 'attribute_guid', must not be 'None'")
        self._attribute_guid = attribute_guid

    @property
    def required(self) -> "bool":
        """Gets the required of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.

        Returns
        -------
        bool
            The required of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.
        """
        return self._required

    @required.setter
    def required(self, required: "bool") -> None:
        """Sets the required of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.

        Parameters
        ----------
        required: bool
            The required of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.
        """
        self._required = required

    @property
    def read_only(self) -> "bool":
        """Gets the read_only of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.

        Returns
        -------
        bool
            The read_only of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only: "bool") -> None:
        """Sets the read_only of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.

        Parameters
        ----------
        read_only: bool
            The read_only of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.
        """
        self._read_only = read_only

    @property
    def meta_attributes(
        self,
    ) -> "list[GrantaServerApiSchemaLayoutsNewLayoutAttributeItem]":
        """Gets the meta_attributes of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.

        Returns
        -------
        list[GrantaServerApiSchemaLayoutsNewLayoutAttributeItem]
            The meta_attributes of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.
        """
        return self._meta_attributes

    @meta_attributes.setter
    def meta_attributes(
        self,
        meta_attributes: "list[GrantaServerApiSchemaLayoutsNewLayoutAttributeItem]",
    ) -> None:
        """Sets the meta_attributes of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.

        Parameters
        ----------
        meta_attributes: list[GrantaServerApiSchemaLayoutsNewLayoutAttributeItem]
            The meta_attributes of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.
        """
        self._meta_attributes = meta_attributes

    @property
    def tabular_column_guids(self) -> "list[str]":
        """Gets the tabular_column_guids of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.

        Returns
        -------
        list[str]
            The tabular_column_guids of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.
        """
        return self._tabular_column_guids

    @tabular_column_guids.setter
    def tabular_column_guids(self, tabular_column_guids: "list[str]") -> None:
        """Sets the tabular_column_guids of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.

        Parameters
        ----------
        tabular_column_guids: list[str]
            The tabular_column_guids of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.
        """
        self._tabular_column_guids = tabular_column_guids

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
        if not isinstance(other, GrantaServerApiSchemaLayoutsNewLayoutAttributeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
