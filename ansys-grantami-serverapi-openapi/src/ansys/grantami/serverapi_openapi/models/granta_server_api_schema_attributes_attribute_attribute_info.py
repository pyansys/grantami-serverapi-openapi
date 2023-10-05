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

class GrantaServerApiSchemaAttributesAttributeAttributeInfo(ModelBase):
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
        "type_code": "str",
        "chartable": "bool",
        "expressionable": "bool",
        "linkable": "bool",
        "extended_name": "str",
        "is_meta_attribute": "bool",
        "ordered_meta_attributes": "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
        "standard_names": "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
        "primary_data_link_groups": "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
        "foreign_data_link_groups": "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
        "primary_dynamic_link_groups": "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
        "foreign_dynamic_link_groups": "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]",
    }

    attribute_map = {
        "type_code": "typeCode",
        "chartable": "chartable",
        "expressionable": "expressionable",
        "linkable": "linkable",
        "extended_name": "extendedName",
        "is_meta_attribute": "isMetaAttribute",
        "ordered_meta_attributes": "orderedMetaAttributes",
        "standard_names": "standardNames",
        "primary_data_link_groups": "primaryDataLinkGroups",
        "foreign_data_link_groups": "foreignDataLinkGroups",
        "primary_dynamic_link_groups": "primaryDynamicLinkGroups",
        "foreign_dynamic_link_groups": "foreignDynamicLinkGroups",
    }

    subtype_mapping = {
        "orderedMetaAttributes": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "standardNames": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "primaryDataLinkGroups": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "foreignDataLinkGroups": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "primaryDynamicLinkGroups": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "foreignDynamicLinkGroups": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
    }

    def __init__(self, *, chartable: "Optional[bool]" = None, expressionable: "Optional[bool]" = None, extended_name: "Optional[str]" = None, foreign_data_link_groups: "Optional[List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]]" = None, foreign_dynamic_link_groups: "Optional[List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]]" = None, is_meta_attribute: "Optional[bool]" = None, linkable: "Optional[bool]" = None, ordered_meta_attributes: "Optional[List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]]" = None, primary_data_link_groups: "Optional[List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]]" = None, primary_dynamic_link_groups: "Optional[List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]]" = None, standard_names: "Optional[List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]]" = None, type_code: "Optional[str]" = None) -> None:
        """GrantaServerApiSchemaAttributesAttributeAttributeInfo - a model defined in Swagger

        Parameters
        ----------
            chartable: bool, optional
            expressionable: bool, optional
            extended_name: str, optional
            foreign_data_link_groups: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity], optional
            foreign_dynamic_link_groups: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity], optional
            is_meta_attribute: bool, optional
            linkable: bool, optional
            ordered_meta_attributes: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity], optional
            primary_data_link_groups: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity], optional
            primary_dynamic_link_groups: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity], optional
            standard_names: List[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity], optional
            type_code: str, optional
        """
        self._type_code = None
        self._chartable = None
        self._expressionable = None
        self._linkable = None
        self._extended_name = None
        self._is_meta_attribute = None
        self._ordered_meta_attributes = None
        self._standard_names = None
        self._primary_data_link_groups = None
        self._foreign_data_link_groups = None
        self._primary_dynamic_link_groups = None
        self._foreign_dynamic_link_groups = None
        self.discriminator = None
        if type_code is not None:
            self.type_code = type_code
        if chartable is not None:
            self.chartable = chartable
        if expressionable is not None:
            self.expressionable = expressionable
        if linkable is not None:
            self.linkable = linkable
        if extended_name is not None:
            self.extended_name = extended_name
        if is_meta_attribute is not None:
            self.is_meta_attribute = is_meta_attribute
        if ordered_meta_attributes is not None:
            self.ordered_meta_attributes = ordered_meta_attributes
        if standard_names is not None:
            self.standard_names = standard_names
        if primary_data_link_groups is not None:
            self.primary_data_link_groups = primary_data_link_groups
        if foreign_data_link_groups is not None:
            self.foreign_data_link_groups = foreign_data_link_groups
        if primary_dynamic_link_groups is not None:
            self.primary_dynamic_link_groups = primary_dynamic_link_groups
        if foreign_dynamic_link_groups is not None:
            self.foreign_dynamic_link_groups = foreign_dynamic_link_groups

    @property
    def type_code(self) -> "str":
        """Gets the type_code of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        str
            The type_code of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._type_code

    @type_code.setter
    def type_code(self, type_code: "str") -> None:
        """Sets the type_code of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        type_code: str
            The type_code of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        self._type_code = type_code

    @property
    def chartable(self) -> "bool":
        """Gets the chartable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        bool
            The chartable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._chartable

    @chartable.setter
    def chartable(self, chartable: "bool") -> None:
        """Sets the chartable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        chartable: bool
            The chartable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        self._chartable = chartable

    @property
    def expressionable(self) -> "bool":
        """Gets the expressionable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        bool
            The expressionable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._expressionable

    @expressionable.setter
    def expressionable(self, expressionable: "bool") -> None:
        """Sets the expressionable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        expressionable: bool
            The expressionable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        self._expressionable = expressionable

    @property
    def linkable(self) -> "bool":
        """Gets the linkable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        bool
            The linkable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._linkable

    @linkable.setter
    def linkable(self, linkable: "bool") -> None:
        """Sets the linkable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        linkable: bool
            The linkable of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        self._linkable = linkable

    @property
    def extended_name(self) -> "str":
        """Gets the extended_name of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        str
            The extended_name of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._extended_name

    @extended_name.setter
    def extended_name(self, extended_name: "str") -> None:
        """Sets the extended_name of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        extended_name: str
            The extended_name of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        self._extended_name = extended_name

    @property
    def is_meta_attribute(self) -> "bool":
        """Gets the is_meta_attribute of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        bool
            The is_meta_attribute of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._is_meta_attribute

    @is_meta_attribute.setter
    def is_meta_attribute(self, is_meta_attribute: "bool") -> None:
        """Sets the is_meta_attribute of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        is_meta_attribute: bool
            The is_meta_attribute of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        self._is_meta_attribute = is_meta_attribute

    @property
    def ordered_meta_attributes(self) -> "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]":
        """Gets the ordered_meta_attributes of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The ordered_meta_attributes of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._ordered_meta_attributes

    @ordered_meta_attributes.setter
    def ordered_meta_attributes(self, ordered_meta_attributes: "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]") -> None:
        """Sets the ordered_meta_attributes of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        ordered_meta_attributes: list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The ordered_meta_attributes of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        self._ordered_meta_attributes = ordered_meta_attributes

    @property
    def standard_names(self) -> "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]":
        """Gets the standard_names of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The standard_names of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._standard_names

    @standard_names.setter
    def standard_names(self, standard_names: "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]") -> None:
        """Sets the standard_names of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        standard_names: list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The standard_names of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        self._standard_names = standard_names

    @property
    def primary_data_link_groups(self) -> "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]":
        """Gets the primary_data_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The primary_data_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._primary_data_link_groups

    @primary_data_link_groups.setter
    def primary_data_link_groups(self, primary_data_link_groups: "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]") -> None:
        """Sets the primary_data_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        primary_data_link_groups: list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The primary_data_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        self._primary_data_link_groups = primary_data_link_groups

    @property
    def foreign_data_link_groups(self) -> "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]":
        """Gets the foreign_data_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The foreign_data_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._foreign_data_link_groups

    @foreign_data_link_groups.setter
    def foreign_data_link_groups(self, foreign_data_link_groups: "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]") -> None:
        """Sets the foreign_data_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        foreign_data_link_groups: list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The foreign_data_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        self._foreign_data_link_groups = foreign_data_link_groups

    @property
    def primary_dynamic_link_groups(self) -> "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]":
        """Gets the primary_dynamic_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The primary_dynamic_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._primary_dynamic_link_groups

    @primary_dynamic_link_groups.setter
    def primary_dynamic_link_groups(self, primary_dynamic_link_groups: "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]") -> None:
        """Sets the primary_dynamic_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        primary_dynamic_link_groups: list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The primary_dynamic_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        self._primary_dynamic_link_groups = primary_dynamic_link_groups

    @property
    def foreign_dynamic_link_groups(self) -> "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]":
        """Gets the foreign_dynamic_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The foreign_dynamic_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        return self._foreign_dynamic_link_groups

    @foreign_dynamic_link_groups.setter
    def foreign_dynamic_link_groups(self, foreign_dynamic_link_groups: "list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]") -> None:
        """Sets the foreign_dynamic_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.

        Parameters
        ----------
        foreign_dynamic_link_groups: list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
            The foreign_dynamic_link_groups of this GrantaServerApiSchemaAttributesAttributeAttributeInfo.
        """
        self._foreign_dynamic_link_groups = foreign_dynamic_link_groups

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
        if issubclass(GrantaServerApiSchemaAttributesAttributeAttributeInfo, dict):
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
        if not isinstance(other, GrantaServerApiSchemaAttributesAttributeAttributeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
