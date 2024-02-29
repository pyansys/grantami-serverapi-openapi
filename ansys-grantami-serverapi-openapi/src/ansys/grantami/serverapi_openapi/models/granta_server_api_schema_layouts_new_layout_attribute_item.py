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
    swagger_types: Dict[str, str] = {
        "attribute_guid": "str",
        "guid": "str",
        "item_type": "str",
        "meta_attributes": "list[GrantaServerApiSchemaLayoutsNewLayoutAttributeItem]",
        "read_only": "bool",
        "required": "bool",
        "tabular_column_guids": "list[str]",
    }

    attribute_map: Dict[str, str] = {
        "attribute_guid": "attributeGuid",
        "guid": "guid",
        "item_type": "itemType",
        "meta_attributes": "metaAttributes",
        "read_only": "readOnly",
        "required": "required",
        "tabular_column_guids": "tabularColumnGuids",
    }

    subtype_mapping: Dict[str, str] = {
        "metaAttributes": "GrantaServerApiSchemaLayoutsNewLayoutAttributeItem",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_guid: "str",
        guid: "Union[str, Unset_Type]" = Unset,
        item_type: "str" = "attribute",
        meta_attributes: "Union[List[GrantaServerApiSchemaLayoutsNewLayoutAttributeItem], None, Unset_Type]" = Unset,
        read_only: "Union[bool, Unset_Type]" = Unset,
        required: "Union[bool, Unset_Type]" = Unset,
        tabular_column_guids: "Union[List[str], None, Unset_Type]" = Unset,
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
        self._item_type: str
        self._attribute_guid: str
        self._required: Union[bool, Unset_Type] = Unset
        self._read_only: Union[bool, Unset_Type] = Unset
        self._meta_attributes: Union[
            List[GrantaServerApiSchemaLayoutsNewLayoutAttributeItem], None, Unset_Type
        ] = Unset
        self._tabular_column_guids: Union[List[str], None, Unset_Type] = Unset

        self.item_type = item_type
        self.attribute_guid = attribute_guid
        if required is not Unset:
            self.required = required
        if read_only is not Unset:
            self.read_only = read_only
        if meta_attributes is not Unset:
            self.meta_attributes = meta_attributes
        if tabular_column_guids is not Unset:
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
        # Field is not nullable
        if item_type is None:
            raise ValueError("Invalid value for 'item_type', must not be 'None'")
        # Field is required
        if item_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'item_type', must not be 'Unset'")
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
        # Field is not nullable
        if attribute_guid is None:
            raise ValueError("Invalid value for 'attribute_guid', must not be 'None'")
        # Field is required
        if attribute_guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'attribute_guid', must not be 'Unset'")
        self._attribute_guid = attribute_guid

    @property
    def required(self) -> "Union[bool, Unset_Type]":
        """Gets the required of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.

        Returns
        -------
        Union[bool, Unset_Type]
            The required of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.
        """
        return self._required

    @required.setter
    def required(self, required: "Union[bool, Unset_Type]") -> None:
        """Sets the required of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.

        Parameters
        ----------
        required: Union[bool, Unset_Type]
            The required of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.
        """
        # Field is not nullable
        if required is None:
            raise ValueError("Invalid value for 'required', must not be 'None'")
        self._required = required

    @property
    def read_only(self) -> "Union[bool, Unset_Type]":
        """Gets the read_only of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.

        Returns
        -------
        Union[bool, Unset_Type]
            The read_only of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only: "Union[bool, Unset_Type]") -> None:
        """Sets the read_only of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.

        Parameters
        ----------
        read_only: Union[bool, Unset_Type]
            The read_only of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.
        """
        # Field is not nullable
        if read_only is None:
            raise ValueError("Invalid value for 'read_only', must not be 'None'")
        self._read_only = read_only

    @property
    def meta_attributes(
        self,
    ) -> "Union[List[GrantaServerApiSchemaLayoutsNewLayoutAttributeItem], None, Unset_Type]":
        """Gets the meta_attributes of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.

        Returns
        -------
        Union[List[GrantaServerApiSchemaLayoutsNewLayoutAttributeItem], None, Unset_Type]
            The meta_attributes of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.
        """
        return self._meta_attributes

    @meta_attributes.setter
    def meta_attributes(
        self,
        meta_attributes: "Union[List[GrantaServerApiSchemaLayoutsNewLayoutAttributeItem], None, Unset_Type]",
    ) -> None:
        """Sets the meta_attributes of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.

        Parameters
        ----------
        meta_attributes: Union[List[GrantaServerApiSchemaLayoutsNewLayoutAttributeItem], None, Unset_Type]
            The meta_attributes of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.
        """
        self._meta_attributes = meta_attributes

    @property
    def tabular_column_guids(self) -> "Union[List[str], None, Unset_Type]":
        """Gets the tabular_column_guids of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.

        Returns
        -------
        Union[List[str], None, Unset_Type]
            The tabular_column_guids of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.
        """
        return self._tabular_column_guids

    @tabular_column_guids.setter
    def tabular_column_guids(
        self, tabular_column_guids: "Union[List[str], None, Unset_Type]"
    ) -> None:
        """Sets the tabular_column_guids of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.

        Parameters
        ----------
        tabular_column_guids: Union[List[str], None, Unset_Type]
            The tabular_column_guids of this GrantaServerApiSchemaLayoutsNewLayoutAttributeItem.
        """
        self._tabular_column_guids = tabular_column_guids

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
        if not isinstance(other, GrantaServerApiSchemaLayoutsNewLayoutAttributeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
