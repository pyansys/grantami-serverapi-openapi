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


class GrantaServerApiListsDtoCreateListItem(ModelBase):
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
        "record_history_guid": "str",
        "record_version": "int",
        "table_guid": "str",
    }

    attribute_map = {
        "database_guid": "databaseGuid",
        "record_history_guid": "recordHistoryGuid",
        "record_version": "recordVersion",
        "table_guid": "tableGuid",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        database_guid: "str",
        record_history_guid: "str",
        record_version: "Optional[int]" = None,
        table_guid: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiListsDtoCreateListItem - a model defined in Swagger

        Parameters
        ----------
            database_guid: str
            record_history_guid: str
            record_version: int, optional
            table_guid: str, optional
        """
        self._database_guid = None
        self._record_history_guid = None
        self._record_version = None
        self._table_guid = None

        self.database_guid = database_guid
        self.record_history_guid = record_history_guid
        if record_version is not None:
            self.record_version = record_version
        if table_guid is not None:
            self.table_guid = table_guid

    @property
    def database_guid(self) -> "str":
        """Gets the database_guid of this GrantaServerApiListsDtoCreateListItem.

        Returns
        -------
        str
            The database_guid of this GrantaServerApiListsDtoCreateListItem.
        """
        return self._database_guid

    @database_guid.setter
    def database_guid(self, database_guid: "str") -> None:
        """Sets the database_guid of this GrantaServerApiListsDtoCreateListItem.

        Parameters
        ----------
        database_guid: str
            The database_guid of this GrantaServerApiListsDtoCreateListItem.
        """
        if database_guid is None:
            raise ValueError("Invalid value for 'database_guid', must not be 'None'")
        self._database_guid = database_guid

    @property
    def record_history_guid(self) -> "str":
        """Gets the record_history_guid of this GrantaServerApiListsDtoCreateListItem.

        Returns
        -------
        str
            The record_history_guid of this GrantaServerApiListsDtoCreateListItem.
        """
        return self._record_history_guid

    @record_history_guid.setter
    def record_history_guid(self, record_history_guid: "str") -> None:
        """Sets the record_history_guid of this GrantaServerApiListsDtoCreateListItem.

        Parameters
        ----------
        record_history_guid: str
            The record_history_guid of this GrantaServerApiListsDtoCreateListItem.
        """
        if record_history_guid is None:
            raise ValueError(
                "Invalid value for 'record_history_guid', must not be 'None'"
            )
        self._record_history_guid = record_history_guid

    @property
    def record_version(self) -> "int":
        """Gets the record_version of this GrantaServerApiListsDtoCreateListItem.

        Returns
        -------
        int
            The record_version of this GrantaServerApiListsDtoCreateListItem.
        """
        return self._record_version

    @record_version.setter
    def record_version(self, record_version: "int") -> None:
        """Sets the record_version of this GrantaServerApiListsDtoCreateListItem.

        Parameters
        ----------
        record_version: int
            The record_version of this GrantaServerApiListsDtoCreateListItem.
        """
        self._record_version = record_version

    @property
    def table_guid(self) -> "str":
        """Gets the table_guid of this GrantaServerApiListsDtoCreateListItem.

        Returns
        -------
        str
            The table_guid of this GrantaServerApiListsDtoCreateListItem.
        """
        return self._table_guid

    @table_guid.setter
    def table_guid(self, table_guid: "str") -> None:
        """Sets the table_guid of this GrantaServerApiListsDtoCreateListItem.

        Parameters
        ----------
        table_guid: str
            The table_guid of this GrantaServerApiListsDtoCreateListItem.
        """
        self._table_guid = table_guid

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
        if not isinstance(other, GrantaServerApiListsDtoCreateListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
