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


class GrantaServerApiSchemaSlimEntitiesSlimProfileTable(ModelBase):
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
        "database_guid": "str",
        "table_guid": "str",
        "database_fallback_hint": "str",
        "guid": "str",
        "table_fallback_hint": "str",
    }

    attribute_map = {
        "database_guid": "databaseGuid",
        "table_guid": "tableGuid",
        "database_fallback_hint": "databaseFallbackHint",
        "guid": "guid",
        "table_fallback_hint": "tableFallbackHint",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        database_guid: "str",
        table_guid: "str",
        database_fallback_hint: "Optional[str]" = None,
        guid: "Optional[str]" = None,
        table_fallback_hint: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiSchemaSlimEntitiesSlimProfileTable - a model defined in Swagger

        Parameters
        ----------
            database_guid: str
            table_guid: str
            database_fallback_hint: str, optional
            guid: str, optional
            table_fallback_hint: str, optional
        """
        self._guid = None
        self._database_guid = None
        self._database_fallback_hint = None
        self._table_guid = None
        self._table_fallback_hint = None

        if guid is not None:
            self.guid = guid
        self.database_guid = database_guid
        if database_fallback_hint is not None:
            self.database_fallback_hint = database_fallback_hint
        self.table_guid = table_guid
        if table_fallback_hint is not None:
            self.table_fallback_hint = table_fallback_hint

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaSlimEntitiesSlimProfileTable.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaSlimEntitiesSlimProfileTable.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaSlimEntitiesSlimProfileTable.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaSlimEntitiesSlimProfileTable.
        """
        self._guid = guid

    @property
    def database_guid(self) -> "str":
        """Gets the database_guid of this GrantaServerApiSchemaSlimEntitiesSlimProfileTable.

        Returns
        -------
        str
            The database_guid of this GrantaServerApiSchemaSlimEntitiesSlimProfileTable.
        """
        return self._database_guid

    @database_guid.setter
    def database_guid(self, database_guid: "str") -> None:
        """Sets the database_guid of this GrantaServerApiSchemaSlimEntitiesSlimProfileTable.

        Parameters
        ----------
        database_guid: str
            The database_guid of this GrantaServerApiSchemaSlimEntitiesSlimProfileTable.
        """
        if database_guid is None:
            raise ValueError("Invalid value for 'database_guid', must not be 'None'")
        self._database_guid = database_guid

    @property
    def database_fallback_hint(self) -> "str":
        """Gets the database_fallback_hint of this GrantaServerApiSchemaSlimEntitiesSlimProfileTable.

        Returns
        -------
        str
            The database_fallback_hint of this GrantaServerApiSchemaSlimEntitiesSlimProfileTable.
        """
        return self._database_fallback_hint

    @database_fallback_hint.setter
    def database_fallback_hint(self, database_fallback_hint: "str") -> None:
        """Sets the database_fallback_hint of this GrantaServerApiSchemaSlimEntitiesSlimProfileTable.

        Parameters
        ----------
        database_fallback_hint: str
            The database_fallback_hint of this GrantaServerApiSchemaSlimEntitiesSlimProfileTable.
        """
        self._database_fallback_hint = database_fallback_hint

    @property
    def table_guid(self) -> "str":
        """Gets the table_guid of this GrantaServerApiSchemaSlimEntitiesSlimProfileTable.

        Returns
        -------
        str
            The table_guid of this GrantaServerApiSchemaSlimEntitiesSlimProfileTable.
        """
        return self._table_guid

    @table_guid.setter
    def table_guid(self, table_guid: "str") -> None:
        """Sets the table_guid of this GrantaServerApiSchemaSlimEntitiesSlimProfileTable.

        Parameters
        ----------
        table_guid: str
            The table_guid of this GrantaServerApiSchemaSlimEntitiesSlimProfileTable.
        """
        if table_guid is None:
            raise ValueError("Invalid value for 'table_guid', must not be 'None'")
        self._table_guid = table_guid

    @property
    def table_fallback_hint(self) -> "str":
        """Gets the table_fallback_hint of this GrantaServerApiSchemaSlimEntitiesSlimProfileTable.

        Returns
        -------
        str
            The table_fallback_hint of this GrantaServerApiSchemaSlimEntitiesSlimProfileTable.
        """
        return self._table_fallback_hint

    @table_fallback_hint.setter
    def table_fallback_hint(self, table_fallback_hint: "str") -> None:
        """Sets the table_fallback_hint of this GrantaServerApiSchemaSlimEntitiesSlimProfileTable.

        Parameters
        ----------
        table_fallback_hint: str
            The table_fallback_hint of this GrantaServerApiSchemaSlimEntitiesSlimProfileTable.
        """
        self._table_fallback_hint = table_fallback_hint

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
        if not isinstance(other, GrantaServerApiSchemaSlimEntitiesSlimProfileTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
