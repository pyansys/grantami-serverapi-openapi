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
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: Dict[str, str] = {
        "guid": "str",
        "is_locked": "bool",
        "is_read_only": "bool",
        "key": "str",
        "name": "str",
        "status": "GrantaServerApiDatabaseStatus",
        "author": "str",
        "company": "str",
        "currency_code": "str",
        "index_in_sync": "bool",
        "index_out_of_date_duration": "str",
        "index_up_to_date": "bool",
        "is_access_controlled": "bool",
        "notes": "str",
        "schema_version": "str",
        "version_guid": "str",
    }

    attribute_map: Dict[str, str] = {
        "guid": "guid",
        "is_locked": "isLocked",
        "is_read_only": "isReadOnly",
        "key": "key",
        "name": "name",
        "status": "status",
        "author": "author",
        "company": "company",
        "currency_code": "currencyCode",
        "index_in_sync": "indexInSync",
        "index_out_of_date_duration": "indexOutOfDateDuration",
        "index_up_to_date": "indexUpToDate",
        "is_access_controlled": "isAccessControlled",
        "notes": "notes",
        "schema_version": "schemaVersion",
        "version_guid": "versionGuid",
    }

    subtype_mapping: Dict[str, str] = {
        "status": "GrantaServerApiDatabaseStatus",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        guid: "str",
        is_locked: "bool",
        is_read_only: "bool",
        key: "str",
        name: "str",
        status: "GrantaServerApiDatabaseStatus",
        author: "Union[str, None, Unset_Type]" = Unset,
        company: "Union[str, None, Unset_Type]" = Unset,
        currency_code: "Union[str, None, Unset_Type]" = Unset,
        index_in_sync: "Union[bool, None, Unset_Type]" = Unset,
        index_out_of_date_duration: "Union[str, None, Unset_Type]" = Unset,
        index_up_to_date: "Union[bool, None, Unset_Type]" = Unset,
        is_access_controlled: "Union[bool, None, Unset_Type]" = Unset,
        notes: "Union[str, None, Unset_Type]" = Unset,
        schema_version: "Union[str, None, Unset_Type]" = Unset,
        version_guid: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaDatabase - a model defined in Swagger

        Parameters
        ----------
        guid: str
        is_locked: bool
        is_read_only: bool
        key: str
        name: str
        status: GrantaServerApiDatabaseStatus
        author: str, optional
        company: str, optional
        currency_code: str, optional
        index_in_sync: bool, optional
        index_out_of_date_duration: str, optional
        index_up_to_date: bool, optional
        is_access_controlled: bool, optional
        notes: str, optional
        schema_version: str, optional
        version_guid: str, optional
        """
        self._author: Union[str, None, Unset_Type] = Unset
        self._company: Union[str, None, Unset_Type] = Unset
        self._notes: Union[str, None, Unset_Type] = Unset
        self._currency_code: Union[str, None, Unset_Type] = Unset
        self._is_access_controlled: Union[bool, None, Unset_Type] = Unset
        self._key: str
        self._version_guid: Union[str, None, Unset_Type] = Unset
        self._status: GrantaServerApiDatabaseStatus
        self._is_read_only: bool
        self._is_locked: bool
        self._index_in_sync: Union[bool, None, Unset_Type] = Unset
        self._index_up_to_date: Union[bool, None, Unset_Type] = Unset
        self._index_out_of_date_duration: Union[str, None, Unset_Type] = Unset
        self._schema_version: Union[str, None, Unset_Type] = Unset
        self._name: str
        self._guid: str

        if author is not Unset:
            self.author = author
        if company is not Unset:
            self.company = company
        if notes is not Unset:
            self.notes = notes
        if currency_code is not Unset:
            self.currency_code = currency_code
        if is_access_controlled is not Unset:
            self.is_access_controlled = is_access_controlled
        self.key = key
        if version_guid is not Unset:
            self.version_guid = version_guid
        self.status = status
        self.is_read_only = is_read_only
        self.is_locked = is_locked
        if index_in_sync is not Unset:
            self.index_in_sync = index_in_sync
        if index_up_to_date is not Unset:
            self.index_up_to_date = index_up_to_date
        if index_out_of_date_duration is not Unset:
            self.index_out_of_date_duration = index_out_of_date_duration
        if schema_version is not Unset:
            self.schema_version = schema_version
        self.name = name
        self.guid = guid

    @property
    def author(self) -> "Union[str, None, Unset_Type]":
        """Gets the author of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        Union[str, None, Unset_Type]
            The author of this GrantaServerApiSchemaDatabase.
        """
        return self._author

    @author.setter
    def author(self, author: "Union[str, None, Unset_Type]") -> None:
        """Sets the author of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        author: Union[str, None, Unset_Type]
            The author of this GrantaServerApiSchemaDatabase.
        """
        self._author = author

    @property
    def company(self) -> "Union[str, None, Unset_Type]":
        """Gets the company of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        Union[str, None, Unset_Type]
            The company of this GrantaServerApiSchemaDatabase.
        """
        return self._company

    @company.setter
    def company(self, company: "Union[str, None, Unset_Type]") -> None:
        """Sets the company of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        company: Union[str, None, Unset_Type]
            The company of this GrantaServerApiSchemaDatabase.
        """
        self._company = company

    @property
    def notes(self) -> "Union[str, None, Unset_Type]":
        """Gets the notes of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        Union[str, None, Unset_Type]
            The notes of this GrantaServerApiSchemaDatabase.
        """
        return self._notes

    @notes.setter
    def notes(self, notes: "Union[str, None, Unset_Type]") -> None:
        """Sets the notes of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        notes: Union[str, None, Unset_Type]
            The notes of this GrantaServerApiSchemaDatabase.
        """
        self._notes = notes

    @property
    def currency_code(self) -> "Union[str, None, Unset_Type]":
        """Gets the currency_code of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        Union[str, None, Unset_Type]
            The currency_code of this GrantaServerApiSchemaDatabase.
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code: "Union[str, None, Unset_Type]") -> None:
        """Sets the currency_code of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        currency_code: Union[str, None, Unset_Type]
            The currency_code of this GrantaServerApiSchemaDatabase.
        """
        self._currency_code = currency_code

    @property
    def is_access_controlled(self) -> "Union[bool, None, Unset_Type]":
        """Gets the is_access_controlled of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The is_access_controlled of this GrantaServerApiSchemaDatabase.
        """
        return self._is_access_controlled

    @is_access_controlled.setter
    def is_access_controlled(
        self, is_access_controlled: "Union[bool, None, Unset_Type]"
    ) -> None:
        """Sets the is_access_controlled of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        is_access_controlled: Union[bool, None, Unset_Type]
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
        # Field is not nullable
        if key is None:
            raise ValueError("Invalid value for 'key', must not be 'None'")
        # Field is required
        if key is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'key', must not be 'Unset'")
        self._key = key

    @property
    def version_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the version_guid of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        Union[str, None, Unset_Type]
            The version_guid of this GrantaServerApiSchemaDatabase.
        """
        return self._version_guid

    @version_guid.setter
    def version_guid(self, version_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the version_guid of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        version_guid: Union[str, None, Unset_Type]
            The version_guid of this GrantaServerApiSchemaDatabase.
        """
        self._version_guid = version_guid

    @property
    def status(self) -> "GrantaServerApiDatabaseStatus":
        """Gets the status of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        GrantaServerApiDatabaseStatus
            The status of this GrantaServerApiSchemaDatabase.
        """
        return self._status

    @status.setter
    def status(self, status: "GrantaServerApiDatabaseStatus") -> None:
        """Sets the status of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        status: GrantaServerApiDatabaseStatus
            The status of this GrantaServerApiSchemaDatabase.
        """
        # Field is not nullable
        if status is None:
            raise ValueError("Invalid value for 'status', must not be 'None'")
        # Field is required
        if status is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'status', must not be 'Unset'")
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
        # Field is not nullable
        if is_read_only is None:
            raise ValueError("Invalid value for 'is_read_only', must not be 'None'")
        # Field is required
        if is_read_only is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'is_read_only', must not be 'Unset'")
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
        # Field is not nullable
        if is_locked is None:
            raise ValueError("Invalid value for 'is_locked', must not be 'None'")
        # Field is required
        if is_locked is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'is_locked', must not be 'Unset'")
        self._is_locked = is_locked

    @property
    def index_in_sync(self) -> "Union[bool, None, Unset_Type]":
        """Gets the index_in_sync of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The index_in_sync of this GrantaServerApiSchemaDatabase.
        """
        return self._index_in_sync

    @index_in_sync.setter
    def index_in_sync(self, index_in_sync: "Union[bool, None, Unset_Type]") -> None:
        """Sets the index_in_sync of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        index_in_sync: Union[bool, None, Unset_Type]
            The index_in_sync of this GrantaServerApiSchemaDatabase.
        """
        self._index_in_sync = index_in_sync

    @property
    def index_up_to_date(self) -> "Union[bool, None, Unset_Type]":
        """Gets the index_up_to_date of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The index_up_to_date of this GrantaServerApiSchemaDatabase.
        """
        return self._index_up_to_date

    @index_up_to_date.setter
    def index_up_to_date(
        self, index_up_to_date: "Union[bool, None, Unset_Type]"
    ) -> None:
        """Sets the index_up_to_date of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        index_up_to_date: Union[bool, None, Unset_Type]
            The index_up_to_date of this GrantaServerApiSchemaDatabase.
        """
        self._index_up_to_date = index_up_to_date

    @property
    def index_out_of_date_duration(self) -> "Union[str, None, Unset_Type]":
        """Gets the index_out_of_date_duration of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        Union[str, None, Unset_Type]
            The index_out_of_date_duration of this GrantaServerApiSchemaDatabase.
        """
        return self._index_out_of_date_duration

    @index_out_of_date_duration.setter
    def index_out_of_date_duration(
        self, index_out_of_date_duration: "Union[str, None, Unset_Type]"
    ) -> None:
        """Sets the index_out_of_date_duration of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        index_out_of_date_duration: Union[str, None, Unset_Type]
            The index_out_of_date_duration of this GrantaServerApiSchemaDatabase.
        """
        self._index_out_of_date_duration = index_out_of_date_duration

    @property
    def schema_version(self) -> "Union[str, None, Unset_Type]":
        """Gets the schema_version of this GrantaServerApiSchemaDatabase.

        Returns
        -------
        Union[str, None, Unset_Type]
            The schema_version of this GrantaServerApiSchemaDatabase.
        """
        return self._schema_version

    @schema_version.setter
    def schema_version(self, schema_version: "Union[str, None, Unset_Type]") -> None:
        """Sets the schema_version of this GrantaServerApiSchemaDatabase.

        Parameters
        ----------
        schema_version: Union[str, None, Unset_Type]
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
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
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
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        # Field is required
        if guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'guid', must not be 'Unset'")
        self._guid = guid

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
        if not isinstance(other, GrantaServerApiSchemaDatabase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
