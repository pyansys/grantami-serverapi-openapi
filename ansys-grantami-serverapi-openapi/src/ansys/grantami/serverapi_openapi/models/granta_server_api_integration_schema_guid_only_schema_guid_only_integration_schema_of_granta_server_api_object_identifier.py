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


class GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier(
    ModelBase
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
        "access_control_category_values": "dict(str, list[str])",
        "attributes": "list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute]",
        "discrete_types": "list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyDiscreteType]",
        "key": "str",
        "layouts": "list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyLayout]",
        "security_groups": "GrantaServerApiIntegrationSchemaSecurityGroups",
        "sources": "list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier]",
        "unit_system": "str",
        "version": "int",
    }

    attribute_map = {
        "access_control_category_values": "accessControlCategoryValues",
        "attributes": "attributes",
        "discrete_types": "discreteTypes",
        "key": "key",
        "layouts": "layouts",
        "security_groups": "securityGroups",
        "sources": "sources",
        "unit_system": "unitSystem",
        "version": "version",
    }

    subtype_mapping = {
        "attributes": "GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute",
        "layouts": "GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyLayout",
        "discreteTypes": "GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyDiscreteType",
        "sources": "GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier",
        "securityGroups": "GrantaServerApiIntegrationSchemaSecurityGroups",
    }

    discriminator = None

    def __init__(
        self,
        *,
        access_control_category_values: "Optional[Dict[str, List[str]]]" = None,
        attributes: "Optional[List[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute]]" = None,
        discrete_types: "Optional[List[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyDiscreteType]]" = None,
        key: "Optional[str]" = None,
        layouts: "Optional[List[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyLayout]]" = None,
        security_groups: "Optional[GrantaServerApiIntegrationSchemaSecurityGroups]" = None,
        sources: "Optional[List[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier]]" = None,
        unit_system: "Optional[str]" = None,
        version: "Optional[int]" = None,
    ) -> None:
        """GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier - a model defined in Swagger

        Parameters
        ----------
            access_control_category_values: Dict[str, List[str]], optional
            attributes: List[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute], optional
            discrete_types: List[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyDiscreteType], optional
            key: str, optional
            layouts: List[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyLayout], optional
            security_groups: GrantaServerApiIntegrationSchemaSecurityGroups, optional
            sources: List[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier], optional
            unit_system: str, optional
            version: int, optional
        """
        self._key = None
        self._version = None
        self._attributes = None
        self._layouts = None
        self._unit_system = None
        self._discrete_types = None
        self._sources = None
        self._access_control_category_values = None
        self._security_groups = None

        if key is not None:
            self.key = key
        if version is not None:
            self.version = version
        if attributes is not None:
            self.attributes = attributes
        if layouts is not None:
            self.layouts = layouts
        if unit_system is not None:
            self.unit_system = unit_system
        if discrete_types is not None:
            self.discrete_types = discrete_types
        if sources is not None:
            self.sources = sources
        if access_control_category_values is not None:
            self.access_control_category_values = access_control_category_values
        if security_groups is not None:
            self.security_groups = security_groups

    @property
    def key(self) -> "str":
        """Gets the key of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        str
            The key of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        return self._key

    @key.setter
    def key(self, key: "str") -> None:
        """Sets the key of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        key: str
            The key of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        self._key = key

    @property
    def version(self) -> "int":
        """Gets the version of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        int
            The version of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        return self._version

    @version.setter
    def version(self, version: "int") -> None:
        """Sets the version of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        version: int
            The version of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        self._version = version

    @property
    def attributes(
        self,
    ) -> "list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute]":
        """Gets the attributes of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute]
            The attributes of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        return self._attributes

    @attributes.setter
    def attributes(
        self,
        attributes: "list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute]",
    ) -> None:
        """Sets the attributes of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        attributes: list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyAttribute]
            The attributes of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        self._attributes = attributes

    @property
    def layouts(
        self,
    ) -> "list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyLayout]":
        """Gets the layouts of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyLayout]
            The layouts of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        return self._layouts

    @layouts.setter
    def layouts(
        self,
        layouts: "list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyLayout]",
    ) -> None:
        """Sets the layouts of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        layouts: list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyLayout]
            The layouts of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        self._layouts = layouts

    @property
    def unit_system(self) -> "str":
        """Gets the unit_system of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        str
            The unit_system of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        return self._unit_system

    @unit_system.setter
    def unit_system(self, unit_system: "str") -> None:
        """Sets the unit_system of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        unit_system: str
            The unit_system of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        self._unit_system = unit_system

    @property
    def discrete_types(
        self,
    ) -> "list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyDiscreteType]":
        """Gets the discrete_types of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyDiscreteType]
            The discrete_types of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        return self._discrete_types

    @discrete_types.setter
    def discrete_types(
        self,
        discrete_types: "list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyDiscreteType]",
    ) -> None:
        """Sets the discrete_types of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        discrete_types: list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyDiscreteType]
            The discrete_types of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        self._discrete_types = discrete_types

    @property
    def sources(
        self,
    ) -> "list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier]":
        """Gets the sources of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier]
            The sources of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        return self._sources

    @sources.setter
    def sources(
        self,
        sources: "list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier]",
    ) -> None:
        """Sets the sources of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        sources: list[GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlySourceOfGrantaServerApiObjectIdentifier]
            The sources of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        self._sources = sources

    @property
    def access_control_category_values(self) -> "dict(str, list[str])":
        """Gets the access_control_category_values of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        dict(str, list[str])
            The access_control_category_values of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        return self._access_control_category_values

    @access_control_category_values.setter
    def access_control_category_values(
        self, access_control_category_values: "dict(str, list[str])"
    ) -> None:
        """Sets the access_control_category_values of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        access_control_category_values: dict(str, list[str])
            The access_control_category_values of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        self._access_control_category_values = access_control_category_values

    @property
    def security_groups(self) -> "GrantaServerApiIntegrationSchemaSecurityGroups":
        """Gets the security_groups of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        GrantaServerApiIntegrationSchemaSecurityGroups
            The security_groups of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(
        self, security_groups: "GrantaServerApiIntegrationSchemaSecurityGroups"
    ) -> None:
        """Sets the security_groups of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        security_groups: GrantaServerApiIntegrationSchemaSecurityGroups
            The security_groups of this GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier.
        """
        self._security_groups = security_groups

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
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(
            GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier,
            dict,
        ):
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
        if not isinstance(
            other,
            GrantaServerApiIntegrationSchemaGuidOnlySchemaGuidOnlyIntegrationSchemaOfGrantaServerApiObjectIdentifier,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
