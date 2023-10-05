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

class GrantaServerApiListsDtoResponseOptions(ModelBase):
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
        "include_user_actions": "bool",
        "include_user_permissions": "bool",
        "include_record_list_items": "bool",
    }

    attribute_map = {
        "include_user_actions": "includeUserActions",
        "include_user_permissions": "includeUserPermissions",
        "include_record_list_items": "includeRecordListItems",
    }

    subtype_mapping = {
    }

    def __init__(self, *, include_record_list_items: "Optional[bool]" = None, include_user_actions: "Optional[bool]" = None, include_user_permissions: "Optional[bool]" = None) -> None:
        """GrantaServerApiListsDtoResponseOptions - a model defined in Swagger

        Parameters
        ----------
            include_record_list_items: bool, optional
            include_user_actions: bool, optional
            include_user_permissions: bool, optional
        """
        self._include_user_actions = None
        self._include_user_permissions = None
        self._include_record_list_items = None
        self.discriminator = None
        if include_user_actions is not None:
            self.include_user_actions = include_user_actions
        if include_user_permissions is not None:
            self.include_user_permissions = include_user_permissions
        if include_record_list_items is not None:
            self.include_record_list_items = include_record_list_items

    @property
    def include_user_actions(self) -> "bool":
        """Gets the include_user_actions of this GrantaServerApiListsDtoResponseOptions.

        Returns
        -------
        bool
            The include_user_actions of this GrantaServerApiListsDtoResponseOptions.
        """
        return self._include_user_actions

    @include_user_actions.setter
    def include_user_actions(self, include_user_actions: "bool") -> None:
        """Sets the include_user_actions of this GrantaServerApiListsDtoResponseOptions.

        Parameters
        ----------
        include_user_actions: bool
            The include_user_actions of this GrantaServerApiListsDtoResponseOptions.
        """
        self._include_user_actions = include_user_actions

    @property
    def include_user_permissions(self) -> "bool":
        """Gets the include_user_permissions of this GrantaServerApiListsDtoResponseOptions.

        Returns
        -------
        bool
            The include_user_permissions of this GrantaServerApiListsDtoResponseOptions.
        """
        return self._include_user_permissions

    @include_user_permissions.setter
    def include_user_permissions(self, include_user_permissions: "bool") -> None:
        """Sets the include_user_permissions of this GrantaServerApiListsDtoResponseOptions.

        Parameters
        ----------
        include_user_permissions: bool
            The include_user_permissions of this GrantaServerApiListsDtoResponseOptions.
        """
        self._include_user_permissions = include_user_permissions

    @property
    def include_record_list_items(self) -> "bool":
        """Gets the include_record_list_items of this GrantaServerApiListsDtoResponseOptions.

        Returns
        -------
        bool
            The include_record_list_items of this GrantaServerApiListsDtoResponseOptions.
        """
        return self._include_record_list_items

    @include_record_list_items.setter
    def include_record_list_items(self, include_record_list_items: "bool") -> None:
        """Sets the include_record_list_items of this GrantaServerApiListsDtoResponseOptions.

        Parameters
        ----------
        include_record_list_items: bool
            The include_record_list_items of this GrantaServerApiListsDtoResponseOptions.
        """
        self._include_record_list_items = include_record_list_items

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
        if issubclass(GrantaServerApiListsDtoResponseOptions, dict):
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
        if not isinstance(other, GrantaServerApiListsDtoResponseOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
