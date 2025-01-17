"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase
from ansys.grantami.serverapi_openapi.models.granta_server_api_search_criterion import (
    GrantaServerApiSearchCriterion,
)  # noqa: F401


if TYPE_CHECKING:
    from . import *


class GrantaServerApiSearchRecordReferenceCriterion(GrantaServerApiSearchCriterion):
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
        "database_key": "str",
        "record_guid": "str",
        "record_history_guid": "str",
        "record_history_identity": "int",
        "record_identity": "int",
        "type": "str",
    }

    attribute_map = {
        "database_key": "databaseKey",
        "record_guid": "recordGuid",
        "record_history_guid": "recordHistoryGuid",
        "record_history_identity": "recordHistoryIdentity",
        "record_identity": "recordIdentity",
        "type": "type",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        database_key: "Optional[str]" = None,
        record_guid: "Optional[str]" = None,
        record_history_guid: "Optional[str]" = None,
        record_history_identity: "Optional[int]" = None,
        record_identity: "Optional[int]" = None,
        type: "str" = "reference",
    ) -> None:
        """GrantaServerApiSearchRecordReferenceCriterion - a model defined in Swagger

        Parameters
        ----------
            database_key: str, optional
            record_guid: str, optional
            record_history_guid: str, optional
            record_history_identity: int, optional
            record_identity: int, optional
            type: str
        """
        super().__init__()
        self._database_key = None
        self._record_identity = None
        self._record_history_identity = None
        self._record_history_guid = None
        self._record_guid = None
        self._type = None

        if database_key is not None:
            self.database_key = database_key
        if record_identity is not None:
            self.record_identity = record_identity
        if record_history_identity is not None:
            self.record_history_identity = record_history_identity
        if record_history_guid is not None:
            self.record_history_guid = record_history_guid
        if record_guid is not None:
            self.record_guid = record_guid
        self.type = type

    @property
    def database_key(self) -> "str":
        """Gets the database_key of this GrantaServerApiSearchRecordReferenceCriterion.

        Returns
        -------
        str
            The database_key of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key: "str") -> None:
        """Sets the database_key of this GrantaServerApiSearchRecordReferenceCriterion.

        Parameters
        ----------
        database_key: str
            The database_key of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        self._database_key = database_key

    @property
    def record_identity(self) -> "int":
        """Gets the record_identity of this GrantaServerApiSearchRecordReferenceCriterion.

        Returns
        -------
        int
            The record_identity of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        return self._record_identity

    @record_identity.setter
    def record_identity(self, record_identity: "int") -> None:
        """Sets the record_identity of this GrantaServerApiSearchRecordReferenceCriterion.

        Parameters
        ----------
        record_identity: int
            The record_identity of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        self._record_identity = record_identity

    @property
    def record_history_identity(self) -> "int":
        """Gets the record_history_identity of this GrantaServerApiSearchRecordReferenceCriterion.

        Returns
        -------
        int
            The record_history_identity of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        return self._record_history_identity

    @record_history_identity.setter
    def record_history_identity(self, record_history_identity: "int") -> None:
        """Sets the record_history_identity of this GrantaServerApiSearchRecordReferenceCriterion.

        Parameters
        ----------
        record_history_identity: int
            The record_history_identity of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        self._record_history_identity = record_history_identity

    @property
    def record_history_guid(self) -> "str":
        """Gets the record_history_guid of this GrantaServerApiSearchRecordReferenceCriterion.

        Returns
        -------
        str
            The record_history_guid of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        return self._record_history_guid

    @record_history_guid.setter
    def record_history_guid(self, record_history_guid: "str") -> None:
        """Sets the record_history_guid of this GrantaServerApiSearchRecordReferenceCriterion.

        Parameters
        ----------
        record_history_guid: str
            The record_history_guid of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        self._record_history_guid = record_history_guid

    @property
    def record_guid(self) -> "str":
        """Gets the record_guid of this GrantaServerApiSearchRecordReferenceCriterion.

        Returns
        -------
        str
            The record_guid of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        return self._record_guid

    @record_guid.setter
    def record_guid(self, record_guid: "str") -> None:
        """Sets the record_guid of this GrantaServerApiSearchRecordReferenceCriterion.

        Parameters
        ----------
        record_guid: str
            The record_guid of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        self._record_guid = record_guid

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchRecordReferenceCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchRecordReferenceCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchRecordReferenceCriterion.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

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
        if not isinstance(other, GrantaServerApiSearchRecordReferenceCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
