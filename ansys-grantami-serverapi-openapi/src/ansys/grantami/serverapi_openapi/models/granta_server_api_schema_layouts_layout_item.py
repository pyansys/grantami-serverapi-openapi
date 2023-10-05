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


if TYPE_CHECKING:
    from . import *

class GrantaServerApiSchemaLayoutsLayoutItem(ModelBase):
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
    """
    swagger_types = {
        "underlying_entity_guid": "str",
        "name": "str",
        "guid": "str",
    }

    attribute_map = {
        "underlying_entity_guid": "underlyingEntityGuid",
        "name": "name",
        "guid": "guid",
    }

    subtype_mapping = {
    }

    discriminator_value_class_map = {
        "attribute".lower(): "#/components/schemas/GrantaServerApiSchemaLayoutsLayoutAttributeItem",
        "link".lower(): "#/components/schemas/GrantaServerApiSchemaLayoutsLayoutLinkItem",
    }

    def __init__(self, *, guid: "Optional[str]" = None, name: "Optional[str]" = None, underlying_entity_guid: "Optional[str]" = None) -> None:
        """GrantaServerApiSchemaLayoutsLayoutItem - a model defined in Swagger

        Parameters
        ----------
            guid: str, optional
            name: str, optional
            underlying_entity_guid: str, optional
        """
        self._underlying_entity_guid = None
        self._name = None
        self._guid = None
        self.discriminator = "itemType"
        if underlying_entity_guid is not None:
            self.underlying_entity_guid = underlying_entity_guid
        if name is not None:
            self.name = name
        if guid is not None:
            self.guid = guid

    @property
    def underlying_entity_guid(self) -> "str":
        """Gets the underlying_entity_guid of this GrantaServerApiSchemaLayoutsLayoutItem.

        Returns
        -------
        str
            The underlying_entity_guid of this GrantaServerApiSchemaLayoutsLayoutItem.
        """
        return self._underlying_entity_guid

    @underlying_entity_guid.setter
    def underlying_entity_guid(self, underlying_entity_guid: "str") -> None:
        """Sets the underlying_entity_guid of this GrantaServerApiSchemaLayoutsLayoutItem.

        Parameters
        ----------
        underlying_entity_guid: str
            The underlying_entity_guid of this GrantaServerApiSchemaLayoutsLayoutItem.
        """
        self._underlying_entity_guid = underlying_entity_guid

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaLayoutsLayoutItem.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaLayoutsLayoutItem.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaLayoutsLayoutItem.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaLayoutsLayoutItem.
        """
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaLayoutsLayoutItem.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaLayoutsLayoutItem.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaLayoutsLayoutItem.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaLayoutsLayoutItem.
        """
        self._guid = guid

    def get_real_child_model(self, data: ModelBase) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[self._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen, 
        # so we have to extract it from the JSON reference
        return self.discriminator_value_class_map.get(discriminator_value).rsplit("/", 1)[-1]

    def _get_discriminator_field_name(self) -> str:
        name_tokens = self.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

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
        if issubclass(GrantaServerApiSchemaLayoutsLayoutItem, dict):
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
        if not isinstance(other, GrantaServerApiSchemaLayoutsLayoutItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
