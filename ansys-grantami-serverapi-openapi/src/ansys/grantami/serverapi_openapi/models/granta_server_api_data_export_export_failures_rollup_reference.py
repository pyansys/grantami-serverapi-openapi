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


class GrantaServerApiDataExportExportFailuresRollupReference(ModelBase):  # type: ignore[misc]
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
        "rollup_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "attribute_guid": "str",
        "attribute_identity": "int",
    }

    attribute_map: Dict[str, str] = {
        "database_key": "databaseKey",
        "rollup_type": "rollupType",
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
    }

    subtype_mapping: Dict[str, str] = {
        "rollupType": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        database_key: "str",
        rollup_type: "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        attribute_guid: "Optional[str]" = None,
        attribute_identity: "Optional[int]" = None,
    ) -> None:
        """GrantaServerApiDataExportExportFailuresRollupReference - a model defined in Swagger

        Parameters
        ----------
            database_key: str
            rollup_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
            attribute_guid: str, optional
            attribute_identity: int, optional
        """
        self._database_key: str = None  # type: ignore[assignment]
        self._attribute_identity = None
        self._attribute_guid = None
        self._rollup_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType = None  # type: ignore[assignment]

        self.database_key = database_key
        if attribute_identity is not None:
            self.attribute_identity = attribute_identity
        if attribute_guid is not None:
            self.attribute_guid = attribute_guid
        self.rollup_type = rollup_type

    @property
    def database_key(self) -> "str":
        """Gets the database_key of this GrantaServerApiDataExportExportFailuresRollupReference.

        Returns
        -------
        str
            The database_key of this GrantaServerApiDataExportExportFailuresRollupReference.
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key: "str") -> None:
        """Sets the database_key of this GrantaServerApiDataExportExportFailuresRollupReference.

        Parameters
        ----------
        database_key: str
            The database_key of this GrantaServerApiDataExportExportFailuresRollupReference.
        """
        if database_key is None:
            raise ValueError("Invalid value for 'database_key', must not be 'None'")
        self._database_key = database_key

    @property
    def attribute_identity(self) -> "Optional[int]":
        """Gets the attribute_identity of this GrantaServerApiDataExportExportFailuresRollupReference.

        Returns
        -------
        int
            The attribute_identity of this GrantaServerApiDataExportExportFailuresRollupReference.
        """
        return self._attribute_identity

    @attribute_identity.setter
    def attribute_identity(self, attribute_identity: "Optional[int]") -> None:
        """Sets the attribute_identity of this GrantaServerApiDataExportExportFailuresRollupReference.

        Parameters
        ----------
        attribute_identity: int
            The attribute_identity of this GrantaServerApiDataExportExportFailuresRollupReference.
        """
        self._attribute_identity = attribute_identity

    @property
    def attribute_guid(self) -> "Optional[str]":
        """Gets the attribute_guid of this GrantaServerApiDataExportExportFailuresRollupReference.

        Returns
        -------
        str
            The attribute_guid of this GrantaServerApiDataExportExportFailuresRollupReference.
        """
        return self._attribute_guid

    @attribute_guid.setter
    def attribute_guid(self, attribute_guid: "Optional[str]") -> None:
        """Sets the attribute_guid of this GrantaServerApiDataExportExportFailuresRollupReference.

        Parameters
        ----------
        attribute_guid: str
            The attribute_guid of this GrantaServerApiDataExportExportFailuresRollupReference.
        """
        self._attribute_guid = attribute_guid

    @property
    def rollup_type(
        self,
    ) -> "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType":
        """Gets the rollup_type of this GrantaServerApiDataExportExportFailuresRollupReference.

        Returns
        -------
        GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
            The rollup_type of this GrantaServerApiDataExportExportFailuresRollupReference.
        """
        return self._rollup_type

    @rollup_type.setter
    def rollup_type(
        self, rollup_type: "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType"
    ) -> None:
        """Sets the rollup_type of this GrantaServerApiDataExportExportFailuresRollupReference.

        Parameters
        ----------
        rollup_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
            The rollup_type of this GrantaServerApiDataExportExportFailuresRollupReference.
        """
        if rollup_type is None:
            raise ValueError("Invalid value for 'rollup_type', must not be 'None'")
        self._rollup_type = rollup_type

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
        if not isinstance(
            other, GrantaServerApiDataExportExportFailuresRollupReference
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
