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

class GrantaServerApiSchemaDatabase(ModelBase):
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

    """
    swagger_types = {
        "author": "str",
        "company": "str",
        "currency_code": "str",
        "guid": "str",
        "index_in_sync": "bool",
        "is_access_controlled": "bool",
        "is_locked": "bool",
        "is_read_only": "bool",
        "key": "str",
        "name": "str",
        "notes": "str",
        "schema_version": "str",
        "status": "GrantaServerApiSchemaDatabaseStatus",
        "version_guid": "str",
    }

    attribute_map = {
        "author": "author",
        "company": "company",
        "currency_code": "currencyCode",
        "guid": "guid",
        "index_in_sync": "indexInSync",
        "is_access_controlled": "isAccessControlled",
        "is_locked": "isLocked",
        "is_read_only": "isReadOnly",
        "key": "key",
        "name": "name",
        "notes": "notes",
        "schema_version": "schemaVersion",
        "status": "status",
        "version_guid": "versionGuid",
    }

    subtype_mapping = {
        "status": "GrantaServerApiSchemaDatabaseStatus",
    }

    def __init__(self, *, author: "Optional[str]" = None, company: "Optional[str]" = None, currency_code: "Optional[str]" = None, guid: "Optional[str]" = None, index_in_sync: "Optional[bool]" = None, is_access_controlled: "Optional[bool]" = None, is_locked: "Optional[bool]" = None, is_read_only: "Optional[bool]" = None, key: "Optional[str]" = None, name: "Optional[str]" = None, notes: "Optional[str]" = None, schema_version: "Optional[str]" = None, status: "Optional[GrantaServerApiSchemaDatabaseStatus]" = None, version_guid: "Optional[str]" = None,) -> None:
        """GrantaServerApiSchemaDatabase - a model defined in Swagger

        Parameters
        ----------
            author: str, optional
            company: str, optional
            currency_code: str, optional
            guid: str, optional
            index_in_sync: bool, optional
            is_access_controlled: bool, optional
            is_locked: bool, optional
            is_read_only: bool, optional
            key: str, optional
            name: str, optional
            notes: str, optional
            schema_version: str, optional
            status: GrantaServerApiSchemaDatabaseStatus, optional
            version_guid: str, optional
        """
        self._author = None
        self._company = None
        self._notes = None
        self._currency_code = None
        self._is_access_controlled = None
        self._key = None
        self._version_guid = None
        self._status = None
        self._is_read_only = None
        self._is_locked = None
        self._index_in_sync = None
        self._schema_version = None
        self._name = None
        self._guid = None
        self.discriminator = None
        if author is not None:
            self.author = author
        if company is not None:
            self.company = company
        if notes is not None:
            self.notes = notes
        if currency_code is not None:
            self.currency_code = currency_code
        if is_access_controlled is not None:
            self.is_access_controlled = is_access_controlled
        if key is not None:
            self.key = key
        if version_guid is not None:
            self.version_guid = version_guid
        if status is not None:
            self.status = status
        if is_read_only is not None:
            self.is_read_only = is_read_only
        if is_locked is not None:
            self.is_locked = is_locked
        if index_in_sync is not None:
            self.index_in_sync = index_in_sync
        if schema_version is not None:
            self.schema_version = schema_version
        if name is not None:
            self.name = name
        if guid is not None:
            self.guid = guid

    @property
    def author(self) -> "str":
        """Gets the author of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        str
            The author of this GrantaServerApiSchemaDatabase.
        """
        return self._author

    @author.setter
    def author(self, author: "str") -> None:
        """Sets the author of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        author: str
            The author of this GrantaServerApiSchemaDatabase.
        """
        self._author = author

    @property
    def company(self) -> "str":
        """Gets the company of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        str
            The company of this GrantaServerApiSchemaDatabase.
        """
        return self._company

    @company.setter
    def company(self, company: "str") -> None:
        """Sets the company of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        company: str
            The company of this GrantaServerApiSchemaDatabase.
        """
        self._company = company

    @property
    def notes(self) -> "str":
        """Gets the notes of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        str
            The notes of this GrantaServerApiSchemaDatabase.
        """
        return self._notes

    @notes.setter
    def notes(self, notes: "str") -> None:
        """Sets the notes of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        notes: str
            The notes of this GrantaServerApiSchemaDatabase.
        """
        self._notes = notes

    @property
    def currency_code(self) -> "str":
        """Gets the currency_code of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        str
            The currency_code of this GrantaServerApiSchemaDatabase.
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code: "str") -> None:
        """Sets the currency_code of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        currency_code: str
            The currency_code of this GrantaServerApiSchemaDatabase.
        """
        self._currency_code = currency_code

    @property
    def is_access_controlled(self) -> "bool":
        """Gets the is_access_controlled of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        bool
            The is_access_controlled of this GrantaServerApiSchemaDatabase.
        """
        return self._is_access_controlled

    @is_access_controlled.setter
    def is_access_controlled(self, is_access_controlled: "bool") -> None:
        """Sets the is_access_controlled of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        is_access_controlled: bool
            The is_access_controlled of this GrantaServerApiSchemaDatabase.
        """
        self._is_access_controlled = is_access_controlled

    @property
    def key(self) -> "str":
        """Gets the key of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        str
            The key of this GrantaServerApiSchemaDatabase.
        """
        return self._key

    @key.setter
    def key(self, key: "str") -> None:
        """Sets the key of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        key: str
            The key of this GrantaServerApiSchemaDatabase.
        """
        self._key = key

    @property
    def version_guid(self) -> "str":
        """Gets the version_guid of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        str
            The version_guid of this GrantaServerApiSchemaDatabase.
        """
        return self._version_guid

    @version_guid.setter
    def version_guid(self, version_guid: "str") -> None:
        """Sets the version_guid of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        version_guid: str
            The version_guid of this GrantaServerApiSchemaDatabase.
        """
        self._version_guid = version_guid

    @property
    def status(self) -> "GrantaServerApiSchemaDatabaseStatus":
        """Gets the status of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        GrantaServerApiSchemaDatabaseStatus
            The status of this GrantaServerApiSchemaDatabase.
        """
        return self._status

    @status.setter
    def status(self, status: "GrantaServerApiSchemaDatabaseStatus") -> None:
        """Sets the status of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        status: GrantaServerApiSchemaDatabaseStatus
            The status of this GrantaServerApiSchemaDatabase.
        """
        self._status = status

    @property
    def is_read_only(self) -> "bool":
        """Gets the is_read_only of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        bool
            The is_read_only of this GrantaServerApiSchemaDatabase.
        """
        return self._is_read_only

    @is_read_only.setter
    def is_read_only(self, is_read_only: "bool") -> None:
        """Sets the is_read_only of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        is_read_only: bool
            The is_read_only of this GrantaServerApiSchemaDatabase.
        """
        self._is_read_only = is_read_only

    @property
    def is_locked(self) -> "bool":
        """Gets the is_locked of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        bool
            The is_locked of this GrantaServerApiSchemaDatabase.
        """
        return self._is_locked

    @is_locked.setter
    def is_locked(self, is_locked: "bool") -> None:
        """Sets the is_locked of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        is_locked: bool
            The is_locked of this GrantaServerApiSchemaDatabase.
        """
        self._is_locked = is_locked

    @property
    def index_in_sync(self) -> "bool":
        """Gets the index_in_sync of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        bool
            The index_in_sync of this GrantaServerApiSchemaDatabase.
        """
        return self._index_in_sync

    @index_in_sync.setter
    def index_in_sync(self, index_in_sync: "bool") -> None:
        """Sets the index_in_sync of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        index_in_sync: bool
            The index_in_sync of this GrantaServerApiSchemaDatabase.
        """
        self._index_in_sync = index_in_sync

    @property
    def schema_version(self) -> "str":
        """Gets the schema_version of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        str
            The schema_version of this GrantaServerApiSchemaDatabase.
        """
        return self._schema_version

    @schema_version.setter
    def schema_version(self, schema_version: "str") -> None:
        """Sets the schema_version of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        schema_version: str
            The schema_version of this GrantaServerApiSchemaDatabase.
        """
        self._schema_version = schema_version

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaDatabase.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaDatabase.
        """
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaDatabase.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaDatabase.
        """
        self._guid = guid

    def get_real_child_model(self, data: ModelBase) -> str:
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
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GrantaServerApiSchemaDatabase, dict):
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
        if not isinstance(other, GrantaServerApiSchemaDatabase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
