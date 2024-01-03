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


class GrantaServerApiListsDtoUserPermissionDto(ModelBase):
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
        "flags": "GrantaServerApiListsDtoRecordListPermissionFlagsDto",
        "user_or_group_identifier": "str",
        "user_or_group_name": "str",
    }

    attribute_map = {
        "flags": "flags",
        "user_or_group_identifier": "userOrGroupIdentifier",
        "user_or_group_name": "userOrGroupName",
    }

    subtype_mapping = {
        "flags": "GrantaServerApiListsDtoRecordListPermissionFlagsDto",
    }

    discriminator = None

    def __init__(
        self,
        *,
        flags: "Optional[GrantaServerApiListsDtoRecordListPermissionFlagsDto]" = None,
        user_or_group_identifier: "Optional[str]" = None,
        user_or_group_name: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiListsDtoUserPermissionDto - a model defined in Swagger

        Parameters
        ----------
            flags: GrantaServerApiListsDtoRecordListPermissionFlagsDto, optional
            user_or_group_identifier: str, optional
            user_or_group_name: str, optional
        """
        self._user_or_group_name = None
        self._user_or_group_identifier = None
        self._flags = None

        if user_or_group_name is not None:
            self.user_or_group_name = user_or_group_name
        if user_or_group_identifier is not None:
            self.user_or_group_identifier = user_or_group_identifier
        if flags is not None:
            self.flags = flags

    @property
    def user_or_group_name(self) -> "str":
        """Gets the user_or_group_name of this GrantaServerApiListsDtoUserPermissionDto.
        The user or group name.

        Returns
        -------
        str
            The user_or_group_name of this GrantaServerApiListsDtoUserPermissionDto.
        """
        return self._user_or_group_name

    @user_or_group_name.setter
    def user_or_group_name(self, user_or_group_name: "str") -> None:
        """Sets the user_or_group_name of this GrantaServerApiListsDtoUserPermissionDto.
        The user or group name.

        Parameters
        ----------
        user_or_group_name: str
            The user_or_group_name of this GrantaServerApiListsDtoUserPermissionDto.
        """
        self._user_or_group_name = user_or_group_name

    @property
    def user_or_group_identifier(self) -> "str":
        """Gets the user_or_group_identifier of this GrantaServerApiListsDtoUserPermissionDto.
        The user or group identifier

        Returns
        -------
        str
            The user_or_group_identifier of this GrantaServerApiListsDtoUserPermissionDto.
        """
        return self._user_or_group_identifier

    @user_or_group_identifier.setter
    def user_or_group_identifier(self, user_or_group_identifier: "str") -> None:
        """Sets the user_or_group_identifier of this GrantaServerApiListsDtoUserPermissionDto.
        The user or group identifier

        Parameters
        ----------
        user_or_group_identifier: str
            The user_or_group_identifier of this GrantaServerApiListsDtoUserPermissionDto.
        """
        self._user_or_group_identifier = user_or_group_identifier

    @property
    def flags(self) -> "GrantaServerApiListsDtoRecordListPermissionFlagsDto":
        """Gets the flags of this GrantaServerApiListsDtoUserPermissionDto.

        Returns
        -------
        GrantaServerApiListsDtoRecordListPermissionFlagsDto
            The flags of this GrantaServerApiListsDtoUserPermissionDto.
        """
        return self._flags

    @flags.setter
    def flags(
        self, flags: "GrantaServerApiListsDtoRecordListPermissionFlagsDto"
    ) -> None:
        """Sets the flags of this GrantaServerApiListsDtoUserPermissionDto.

        Parameters
        ----------
        flags: GrantaServerApiListsDtoRecordListPermissionFlagsDto
            The flags of this GrantaServerApiListsDtoUserPermissionDto.
        """
        self._flags = flags

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
        if not isinstance(other, GrantaServerApiListsDtoUserPermissionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
