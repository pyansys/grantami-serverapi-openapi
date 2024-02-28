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


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaRecordLinkGroupsLinkTarget(ModelBase):
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
        "database_guid": "str",
        "database_version_guid": "str",
        "table_guid": "str",
    }

    attribute_map: Dict[str, str] = {
        "database_guid": "databaseGuid",
        "database_version_guid": "databaseVersionGuid",
        "table_guid": "tableGuid",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        database_guid: "Union[str, None, Unset_Type]" = Unset,
        database_version_guid: "Union[str, None, Unset_Type]" = Unset,
        table_guid: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaRecordLinkGroupsLinkTarget - a model defined in Swagger

        Parameters
        ----------
        database_guid: str, optional
        database_version_guid: str, optional
        table_guid: str, optional
        """
        self._database_guid: Union[str, None, Unset_Type] = Unset
        self._database_version_guid: Union[str, None, Unset_Type] = Unset
        self._table_guid: Union[str, None, Unset_Type] = Unset

        if database_guid is not Unset:
            self.database_guid = database_guid
        if database_version_guid is not Unset:
            self.database_version_guid = database_version_guid
        if table_guid is not Unset:
            self.table_guid = table_guid

    @property
    def database_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the database_guid of this GrantaServerApiSchemaRecordLinkGroupsLinkTarget.

        Returns
        -------
        Union[str, None, Unset_Type]
            The database_guid of this GrantaServerApiSchemaRecordLinkGroupsLinkTarget.
        """
        return self._database_guid

    @database_guid.setter
    def database_guid(self, database_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the database_guid of this GrantaServerApiSchemaRecordLinkGroupsLinkTarget.

        Parameters
        ----------
        database_guid: Union[str, None, Unset_Type]
            The database_guid of this GrantaServerApiSchemaRecordLinkGroupsLinkTarget.
        """
        self._database_guid = database_guid

    @property
    def database_version_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the database_version_guid of this GrantaServerApiSchemaRecordLinkGroupsLinkTarget.

        Returns
        -------
        Union[str, None, Unset_Type]
            The database_version_guid of this GrantaServerApiSchemaRecordLinkGroupsLinkTarget.
        """
        return self._database_version_guid

    @database_version_guid.setter
    def database_version_guid(
        self, database_version_guid: "Union[str, None, Unset_Type]"
    ) -> None:
        """Sets the database_version_guid of this GrantaServerApiSchemaRecordLinkGroupsLinkTarget.

        Parameters
        ----------
        database_version_guid: Union[str, None, Unset_Type]
            The database_version_guid of this GrantaServerApiSchemaRecordLinkGroupsLinkTarget.
        """
        self._database_version_guid = database_version_guid

    @property
    def table_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the table_guid of this GrantaServerApiSchemaRecordLinkGroupsLinkTarget.

        Returns
        -------
        Union[str, None, Unset_Type]
            The table_guid of this GrantaServerApiSchemaRecordLinkGroupsLinkTarget.
        """
        return self._table_guid

    @table_guid.setter
    def table_guid(self, table_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the table_guid of this GrantaServerApiSchemaRecordLinkGroupsLinkTarget.

        Parameters
        ----------
        table_guid: Union[str, None, Unset_Type]
            The table_guid of this GrantaServerApiSchemaRecordLinkGroupsLinkTarget.
        """
        self._table_guid = table_guid

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
        if not isinstance(other, GrantaServerApiSchemaRecordLinkGroupsLinkTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
