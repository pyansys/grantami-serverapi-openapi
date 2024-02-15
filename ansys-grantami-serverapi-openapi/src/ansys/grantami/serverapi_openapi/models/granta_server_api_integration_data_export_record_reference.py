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


class GrantaServerApiIntegrationDataExportRecordReference(ModelBase):  # type: ignore[misc]
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
        "database_key": "str",
        "record_history_identity": "int",
    }

    attribute_map: Dict[str, str] = {
        "database_key": "databaseKey",
        "record_history_identity": "recordHistoryIdentity",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        database_key: "Optional[str]" = None,
        record_history_identity: "Optional[int]" = None,
    ) -> None:
        """GrantaServerApiIntegrationDataExportRecordReference - a model defined in Swagger

        Parameters
        ----------
            database_key: str, optional
            record_history_identity: int, optional
        """
        self._record_history_identity = None
        self._database_key = None

        if record_history_identity is not None:
            self.record_history_identity = record_history_identity
        if database_key is not None:
            self.database_key = database_key

    @property
    def record_history_identity(self) -> "Optional[int]":
        """Gets the record_history_identity of this GrantaServerApiIntegrationDataExportRecordReference.

        Returns
        -------
        int
            The record_history_identity of this GrantaServerApiIntegrationDataExportRecordReference.
        """
        return self._record_history_identity

    @record_history_identity.setter
    def record_history_identity(self, record_history_identity: "Optional[int]") -> None:
        """Sets the record_history_identity of this GrantaServerApiIntegrationDataExportRecordReference.

        Parameters
        ----------
        record_history_identity: int
            The record_history_identity of this GrantaServerApiIntegrationDataExportRecordReference.
        """
        self._record_history_identity = record_history_identity

    @property
    def database_key(self) -> "Optional[str]":
        """Gets the database_key of this GrantaServerApiIntegrationDataExportRecordReference.

        Returns
        -------
        str
            The database_key of this GrantaServerApiIntegrationDataExportRecordReference.
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key: "Optional[str]") -> None:
        """Sets the database_key of this GrantaServerApiIntegrationDataExportRecordReference.

        Parameters
        ----------
        database_key: str
            The database_key of this GrantaServerApiIntegrationDataExportRecordReference.
        """
        self._database_key = database_key

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
        if not isinstance(other, GrantaServerApiIntegrationDataExportRecordReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
