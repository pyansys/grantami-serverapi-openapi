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
    Dict,
    List,
    BinaryIO,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaProfileTablesCreateProfileTable(ModelBase):  # type: ignore[misc]
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
        "table_guid": "str",
        "guid": "str",
        "layout_guid": "str",
        "subset_guid": "str",
    }

    attribute_map: Dict[str, str] = {
        "database_guid": "databaseGuid",
        "table_guid": "tableGuid",
        "guid": "guid",
        "layout_guid": "layoutGuid",
        "subset_guid": "subsetGuid",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        database_guid: "str",
        table_guid: "str",
        guid: "Optional[str]" = None,
        layout_guid: "Optional[str]" = None,
        subset_guid: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiSchemaProfileTablesCreateProfileTable - a model defined in Swagger

        Parameters
        ----------
            database_guid: str
            table_guid: str
            guid: str, optional
            layout_guid: str, optional
            subset_guid: str, optional
        """
        self._database_guid: str = None  # type: ignore[assignment]
        self._table_guid: str = None  # type: ignore[assignment]
        self._subset_guid = None
        self._layout_guid = None
        self._guid = None

        self.database_guid = database_guid
        self.table_guid = table_guid
        if subset_guid is not None:
            self.subset_guid = subset_guid
        if layout_guid is not None:
            self.layout_guid = layout_guid
        if guid is not None:
            self.guid = guid

    @property
    def database_guid(self) -> "str":
        """Gets the database_guid of this GrantaServerApiSchemaProfileTablesCreateProfileTable.

        Returns
        -------
        str
            The database_guid of this GrantaServerApiSchemaProfileTablesCreateProfileTable.
        """
        return self._database_guid

    @database_guid.setter
    def database_guid(self, database_guid: "str") -> None:
        """Sets the database_guid of this GrantaServerApiSchemaProfileTablesCreateProfileTable.

        Parameters
        ----------
        database_guid: str
            The database_guid of this GrantaServerApiSchemaProfileTablesCreateProfileTable.
        """
        if database_guid is None:
            raise ValueError("Invalid value for 'database_guid', must not be 'None'")
        self._database_guid = database_guid

    @property
    def table_guid(self) -> "str":
        """Gets the table_guid of this GrantaServerApiSchemaProfileTablesCreateProfileTable.

        Returns
        -------
        str
            The table_guid of this GrantaServerApiSchemaProfileTablesCreateProfileTable.
        """
        return self._table_guid

    @table_guid.setter
    def table_guid(self, table_guid: "str") -> None:
        """Sets the table_guid of this GrantaServerApiSchemaProfileTablesCreateProfileTable.

        Parameters
        ----------
        table_guid: str
            The table_guid of this GrantaServerApiSchemaProfileTablesCreateProfileTable.
        """
        if table_guid is None:
            raise ValueError("Invalid value for 'table_guid', must not be 'None'")
        self._table_guid = table_guid

    @property
    def subset_guid(self) -> "Optional[str]":
        """Gets the subset_guid of this GrantaServerApiSchemaProfileTablesCreateProfileTable.

        Returns
        -------
        str
            The subset_guid of this GrantaServerApiSchemaProfileTablesCreateProfileTable.
        """
        return self._subset_guid

    @subset_guid.setter
    def subset_guid(self, subset_guid: "Optional[str]") -> None:
        """Sets the subset_guid of this GrantaServerApiSchemaProfileTablesCreateProfileTable.

        Parameters
        ----------
        subset_guid: str
            The subset_guid of this GrantaServerApiSchemaProfileTablesCreateProfileTable.
        """
        self._subset_guid = subset_guid

    @property
    def layout_guid(self) -> "Optional[str]":
        """Gets the layout_guid of this GrantaServerApiSchemaProfileTablesCreateProfileTable.

        Returns
        -------
        str
            The layout_guid of this GrantaServerApiSchemaProfileTablesCreateProfileTable.
        """
        return self._layout_guid

    @layout_guid.setter
    def layout_guid(self, layout_guid: "Optional[str]") -> None:
        """Sets the layout_guid of this GrantaServerApiSchemaProfileTablesCreateProfileTable.

        Parameters
        ----------
        layout_guid: str
            The layout_guid of this GrantaServerApiSchemaProfileTablesCreateProfileTable.
        """
        self._layout_guid = layout_guid

    @property
    def guid(self) -> "Optional[str]":
        """Gets the guid of this GrantaServerApiSchemaProfileTablesCreateProfileTable.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaProfileTablesCreateProfileTable.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Optional[str]") -> None:
        """Sets the guid of this GrantaServerApiSchemaProfileTablesCreateProfileTable.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaProfileTablesCreateProfileTable.
        """
        self._guid = guid

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
        return self.to_str()  # type: ignore[no-any-return]

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiSchemaProfileTablesCreateProfileTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
