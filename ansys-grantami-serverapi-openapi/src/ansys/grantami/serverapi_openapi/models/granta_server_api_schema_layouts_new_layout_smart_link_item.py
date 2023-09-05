"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase

from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_layouts_new_layout_item import GrantaServerApiSchemaLayoutsNewLayoutItem  # noqa: F401

if TYPE_CHECKING:
    from . import *

class GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem(GrantaServerApiSchemaLayoutsNewLayoutItem):
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

    """
    swagger_types = {
        "item_type": "str",
        "forwards": "bool",
        "link_group_guid": "str",
    }

    attribute_map = {
        "item_type": "itemType",
        "forwards": "forwards",
        "link_group_guid": "linkGroupGuid",
    }

    subtype_mapping = {
    }

    def __init__(self, *, forwards: "Optional[bool]" = None, guid: "Optional[str]" = None, item_type: "str" = 'smartLink', link_group_guid: "Optional[str]" = None) -> None:
        """GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem - a model defined in Swagger

        Parameters
        ----------
            forwards: bool, optional
            guid: str, optional
            item_type: str
            link_group_guid: str, optional
        """
        super().__init__(guid=guid)
        self._item_type = None
        self._forwards = None
        self._link_group_guid = None
        self.discriminator = None
        self.item_type = item_type
        if forwards is not None:
            self.forwards = forwards
        if link_group_guid is not None:
            self.link_group_guid = link_group_guid

    @property
    def item_type(self) -> "str":
        """Gets the item_type of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.

        Returns
        -------
        str
            The item_type of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type: "str") -> None:
        """Sets the item_type of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.

        Parameters
        ----------
        item_type: str
            The item_type of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.
        """
        if item_type is None:
            raise ValueError("Invalid value for 'item_type', must not be 'None'")
        self._item_type = item_type

    @property
    def forwards(self) -> "bool":
        """Gets the forwards of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.

        Returns
        -------
        bool
            The forwards of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.
        """
        return self._forwards

    @forwards.setter
    def forwards(self, forwards: "bool") -> None:
        """Sets the forwards of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.

        Parameters
        ----------
        forwards: bool
            The forwards of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.
        """
        self._forwards = forwards

    @property
    def link_group_guid(self) -> "str":
        """Gets the link_group_guid of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.

        Returns
        -------
        str
            The link_group_guid of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.
        """
        return self._link_group_guid

    @link_group_guid.setter
    def link_group_guid(self, link_group_guid: "str") -> None:
        """Sets the link_group_guid of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.

        Parameters
        ----------
        link_group_guid: str
            The link_group_guid of this GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem.
        """
        self._link_group_guid = link_group_guid

    def get_real_child_model(self, data: ModelBase) -> str:
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

    def to_dict(self) -> Dict:
        """Returns the model properties as a dict

        Returns
        -------
        Dict
            Dictionary indexed by property name containing all the model properties
        """
        result = {}

        for attr in self.swagger_types.keys():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model

        Returns
        -------
        str
            String representation of the model as a dictionary
        """
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiSchemaLayoutsNewLayoutSmartLinkItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
