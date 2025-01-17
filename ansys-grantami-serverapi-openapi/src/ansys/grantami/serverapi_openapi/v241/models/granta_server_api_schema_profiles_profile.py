"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
    from . import *


class GrantaServerApiSchemaProfilesProfile(ModelBase):
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
        "is_implicit": "bool",
        "key": "str",
        "name": "str",
        "profile_tables": "list[GrantaServerApiSchemaSlimEntitiesSlimProfileTable]",
        "description": "str",
        "group_name": "str",
        "guid": "str",
        "homepage_url": "str",
    }

    attribute_map = {
        "is_implicit": "isImplicit",
        "key": "key",
        "name": "name",
        "profile_tables": "profileTables",
        "description": "description",
        "group_name": "groupName",
        "guid": "guid",
        "homepage_url": "homepageUrl",
    }

    subtype_mapping = {
        "profileTables": "GrantaServerApiSchemaSlimEntitiesSlimProfileTable",
    }

    discriminator = None

    def __init__(
        self,
        *,
        is_implicit: "bool",
        key: "str",
        name: "str",
        profile_tables: "List[GrantaServerApiSchemaSlimEntitiesSlimProfileTable]",
        description: "Optional[str]" = None,
        group_name: "Optional[str]" = None,
        guid: "Optional[str]" = None,
        homepage_url: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiSchemaProfilesProfile - a model defined in Swagger

        Parameters
        ----------
            is_implicit: bool
            key: str
            name: str
            profile_tables: List[GrantaServerApiSchemaSlimEntitiesSlimProfileTable]
            description: str, optional
            group_name: str, optional
            guid: str, optional
            homepage_url: str, optional
        """
        self._description = None
        self._homepage_url = None
        self._profile_tables = None
        self._key = None
        self._guid = None
        self._group_name = None
        self._is_implicit = None
        self._name = None

        if description is not None:
            self.description = description
        if homepage_url is not None:
            self.homepage_url = homepage_url
        self.profile_tables = profile_tables
        self.key = key
        if guid is not None:
            self.guid = guid
        if group_name is not None:
            self.group_name = group_name
        self.is_implicit = is_implicit
        self.name = name

    @property
    def description(self) -> "str":
        """Gets the description of this GrantaServerApiSchemaProfilesProfile.

        Returns
        -------
        str
            The description of this GrantaServerApiSchemaProfilesProfile.
        """
        return self._description

    @description.setter
    def description(self, description: "str") -> None:
        """Sets the description of this GrantaServerApiSchemaProfilesProfile.

        Parameters
        ----------
        description: str
            The description of this GrantaServerApiSchemaProfilesProfile.
        """
        self._description = description

    @property
    def homepage_url(self) -> "str":
        """Gets the homepage_url of this GrantaServerApiSchemaProfilesProfile.

        Returns
        -------
        str
            The homepage_url of this GrantaServerApiSchemaProfilesProfile.
        """
        return self._homepage_url

    @homepage_url.setter
    def homepage_url(self, homepage_url: "str") -> None:
        """Sets the homepage_url of this GrantaServerApiSchemaProfilesProfile.

        Parameters
        ----------
        homepage_url: str
            The homepage_url of this GrantaServerApiSchemaProfilesProfile.
        """
        self._homepage_url = homepage_url

    @property
    def profile_tables(
        self,
    ) -> "list[GrantaServerApiSchemaSlimEntitiesSlimProfileTable]":
        """Gets the profile_tables of this GrantaServerApiSchemaProfilesProfile.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimProfileTable]
            The profile_tables of this GrantaServerApiSchemaProfilesProfile.
        """
        return self._profile_tables

    @profile_tables.setter
    def profile_tables(
        self, profile_tables: "list[GrantaServerApiSchemaSlimEntitiesSlimProfileTable]"
    ) -> None:
        """Sets the profile_tables of this GrantaServerApiSchemaProfilesProfile.

        Parameters
        ----------
        profile_tables: list[GrantaServerApiSchemaSlimEntitiesSlimProfileTable]
            The profile_tables of this GrantaServerApiSchemaProfilesProfile.
        """
        if profile_tables is None:
            raise ValueError("Invalid value for 'profile_tables', must not be 'None'")
        self._profile_tables = profile_tables

    @property
    def key(self) -> "str":
        """Gets the key of this GrantaServerApiSchemaProfilesProfile.
        Key is a unique identifier of a profile. Separate from guid.

        Returns
        -------
        str
            The key of this GrantaServerApiSchemaProfilesProfile.
        """
        return self._key

    @key.setter
    def key(self, key: "str") -> None:
        """Sets the key of this GrantaServerApiSchemaProfilesProfile.
        Key is a unique identifier of a profile. Separate from guid.

        Parameters
        ----------
        key: str
            The key of this GrantaServerApiSchemaProfilesProfile.
        """
        if key is None:
            raise ValueError("Invalid value for 'key', must not be 'None'")
        self._key = key

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaProfilesProfile.
        Guid is a unique identifier of a profile. Separate from key.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaProfilesProfile.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaProfilesProfile.
        Guid is a unique identifier of a profile. Separate from key.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaProfilesProfile.
        """
        self._guid = guid

    @property
    def group_name(self) -> "str":
        """Gets the group_name of this GrantaServerApiSchemaProfilesProfile.

        Returns
        -------
        str
            The group_name of this GrantaServerApiSchemaProfilesProfile.
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name: "str") -> None:
        """Sets the group_name of this GrantaServerApiSchemaProfilesProfile.

        Parameters
        ----------
        group_name: str
            The group_name of this GrantaServerApiSchemaProfilesProfile.
        """
        self._group_name = group_name

    @property
    def is_implicit(self) -> "bool":
        """Gets the is_implicit of this GrantaServerApiSchemaProfilesProfile.

        Returns
        -------
        bool
            The is_implicit of this GrantaServerApiSchemaProfilesProfile.
        """
        return self._is_implicit

    @is_implicit.setter
    def is_implicit(self, is_implicit: "bool") -> None:
        """Sets the is_implicit of this GrantaServerApiSchemaProfilesProfile.

        Parameters
        ----------
        is_implicit: bool
            The is_implicit of this GrantaServerApiSchemaProfilesProfile.
        """
        if is_implicit is None:
            raise ValueError("Invalid value for 'is_implicit', must not be 'None'")
        self._is_implicit = is_implicit

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaProfilesProfile.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaProfilesProfile.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaProfilesProfile.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaProfilesProfile.
        """
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

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
        if not isinstance(other, GrantaServerApiSchemaProfilesProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
