# Copyright (C) 2023 - 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaIntegrationSchemaStatus(ModelBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes
    ----------
    swagger_types: dict[str, str]
        The key is attribute name and the value is attribute type.
    attribute_map: dict[str, str]
        The key is attribute name and the value is json key in definition.
    subtype_mapping: dict[str, str]
        The key is the unmangled property name and the value is the corresponding type.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "errored_databases": "dict(str, str)",
        "loaded_database_index_statuses": "dict(str, GsaSearchIndexStatus)",
        "loaded_databases": "list[str]",
        "loading_databases": "list[str]",
        "not_loaded_databases": "list[str]",
        "records_that_failed_to_index": "list[GsaIndexRecordFailure]",
        "search_index_in_sync": "bool",
        "search_index_is_read_only": "bool",
        "search_index_location": "str",
        "search_index_out_of_date_duration": "str",
        "search_index_unavailable": "bool",
        "search_index_up_to_date": "bool",
    }

    attribute_map: dict[str, str] = {
        "errored_databases": "erroredDatabases",
        "loaded_database_index_statuses": "loadedDatabaseIndexStatuses",
        "loaded_databases": "loadedDatabases",
        "loading_databases": "loadingDatabases",
        "not_loaded_databases": "notLoadedDatabases",
        "records_that_failed_to_index": "recordsThatFailedToIndex",
        "search_index_in_sync": "searchIndexInSync",
        "search_index_is_read_only": "searchIndexIsReadOnly",
        "search_index_location": "searchIndexLocation",
        "search_index_out_of_date_duration": "searchIndexOutOfDateDuration",
        "search_index_unavailable": "searchIndexUnavailable",
        "search_index_up_to_date": "searchIndexUpToDate",
    }

    subtype_mapping: dict[str, str] = {
        "loadedDatabaseIndexStatuses": "GsaSearchIndexStatus",
        "recordsThatFailedToIndex": "GsaIndexRecordFailure",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        errored_databases: "Union[dict[str, str], None, Unset_Type]" = Unset,
        loaded_database_index_statuses: "Union[dict[str, GsaSearchIndexStatus], None, Unset_Type]" = Unset,
        loaded_databases: "Union[list[str], None, Unset_Type]" = Unset,
        loading_databases: "Union[list[str], None, Unset_Type]" = Unset,
        not_loaded_databases: "Union[list[str], None, Unset_Type]" = Unset,
        records_that_failed_to_index: "Union[list[GsaIndexRecordFailure], None, Unset_Type]" = Unset,
        search_index_in_sync: "Union[bool, Unset_Type]" = Unset,
        search_index_is_read_only: "Union[bool, None, Unset_Type]" = Unset,
        search_index_location: "Union[str, None, Unset_Type]" = Unset,
        search_index_out_of_date_duration: "Union[str, None, Unset_Type]" = Unset,
        search_index_unavailable: "Union[bool, None, Unset_Type]" = Unset,
        search_index_up_to_date: "Union[bool, Unset_Type]" = Unset,
    ) -> None:
        """GsaIntegrationSchemaStatus - a model defined in Swagger

        Parameters
        ----------
        errored_databases: dict[str, str], optional
        loaded_database_index_statuses: dict[str, GsaSearchIndexStatus], optional
        loaded_databases: list[str], optional
        loading_databases: list[str], optional
        not_loaded_databases: list[str], optional
        records_that_failed_to_index: list[GsaIndexRecordFailure], optional
        search_index_in_sync: bool, optional
        search_index_is_read_only: bool, optional
        search_index_location: str, optional
        search_index_out_of_date_duration: str, optional
        search_index_unavailable: bool, optional
        search_index_up_to_date: bool, optional
        """
        self._loaded_databases: Union[list[str], None, Unset_Type] = Unset
        self._loading_databases: Union[list[str], None, Unset_Type] = Unset
        self._not_loaded_databases: Union[list[str], None, Unset_Type] = Unset
        self._errored_databases: Union[dict[str, str], None, Unset_Type] = Unset
        self._loaded_database_index_statuses: Union[
            dict[str, GsaSearchIndexStatus], None, Unset_Type
        ] = Unset
        self._search_index_up_to_date: Union[bool, Unset_Type] = Unset
        self._search_index_out_of_date_duration: Union[str, None, Unset_Type] = Unset
        self._search_index_in_sync: Union[bool, Unset_Type] = Unset
        self._search_index_location: Union[str, None, Unset_Type] = Unset
        self._search_index_is_read_only: Union[bool, None, Unset_Type] = Unset
        self._search_index_unavailable: Union[bool, None, Unset_Type] = Unset
        self._records_that_failed_to_index: Union[list[GsaIndexRecordFailure], None, Unset_Type] = (
            Unset
        )

        if loaded_databases is not Unset:
            self.loaded_databases = loaded_databases
        if loading_databases is not Unset:
            self.loading_databases = loading_databases
        if not_loaded_databases is not Unset:
            self.not_loaded_databases = not_loaded_databases
        if errored_databases is not Unset:
            self.errored_databases = errored_databases
        if loaded_database_index_statuses is not Unset:
            self.loaded_database_index_statuses = loaded_database_index_statuses
        if search_index_up_to_date is not Unset:
            self.search_index_up_to_date = search_index_up_to_date
        if search_index_out_of_date_duration is not Unset:
            self.search_index_out_of_date_duration = search_index_out_of_date_duration
        if search_index_in_sync is not Unset:
            self.search_index_in_sync = search_index_in_sync
        if search_index_location is not Unset:
            self.search_index_location = search_index_location
        if search_index_is_read_only is not Unset:
            self.search_index_is_read_only = search_index_is_read_only
        if search_index_unavailable is not Unset:
            self.search_index_unavailable = search_index_unavailable
        if records_that_failed_to_index is not Unset:
            self.records_that_failed_to_index = records_that_failed_to_index

    @property
    def loaded_databases(self) -> "Union[list[str], None, Unset_Type]":
        """Gets the loaded_databases of this GsaIntegrationSchemaStatus.
        Loaded databases have been successfully indexed into the integration schema.

        Returns
        -------
        Union[list[str], None, Unset_Type]
            The loaded_databases of this GsaIntegrationSchemaStatus.
        """
        return self._loaded_databases

    @loaded_databases.setter
    def loaded_databases(self, loaded_databases: "Union[list[str], None, Unset_Type]") -> None:
        """Sets the loaded_databases of this GsaIntegrationSchemaStatus.
        Loaded databases have been successfully indexed into the integration schema.

        Parameters
        ----------
        loaded_databases: Union[list[str], None, Unset_Type]
            The loaded_databases of this GsaIntegrationSchemaStatus.
        """
        self._loaded_databases = loaded_databases

    @property
    def loading_databases(self) -> "Union[list[str], None, Unset_Type]":
        """Gets the loading_databases of this GsaIntegrationSchemaStatus.
        Databases which are in the process of loading.

        Returns
        -------
        Union[list[str], None, Unset_Type]
            The loading_databases of this GsaIntegrationSchemaStatus.
        """
        return self._loading_databases

    @loading_databases.setter
    def loading_databases(self, loading_databases: "Union[list[str], None, Unset_Type]") -> None:
        """Sets the loading_databases of this GsaIntegrationSchemaStatus.
        Databases which are in the process of loading.

        Parameters
        ----------
        loading_databases: Union[list[str], None, Unset_Type]
            The loading_databases of this GsaIntegrationSchemaStatus.
        """
        self._loading_databases = loading_databases

    @property
    def not_loaded_databases(self) -> "Union[list[str], None, Unset_Type]":
        """Gets the not_loaded_databases of this GsaIntegrationSchemaStatus.
        Databases that are referenced in the schema but that are not yet loaded. This could be because they are still queued for  load in the MI system, or because they have not yet been added.

        Returns
        -------
        Union[list[str], None, Unset_Type]
            The not_loaded_databases of this GsaIntegrationSchemaStatus.
        """
        return self._not_loaded_databases

    @not_loaded_databases.setter
    def not_loaded_databases(
        self, not_loaded_databases: "Union[list[str], None, Unset_Type]"
    ) -> None:
        """Sets the not_loaded_databases of this GsaIntegrationSchemaStatus.
        Databases that are referenced in the schema but that are not yet loaded. This could be because they are still queued for  load in the MI system, or because they have not yet been added.

        Parameters
        ----------
        not_loaded_databases: Union[list[str], None, Unset_Type]
            The not_loaded_databases of this GsaIntegrationSchemaStatus.
        """
        self._not_loaded_databases = not_loaded_databases

    @property
    def errored_databases(self) -> "Union[dict[str, str], None, Unset_Type]":
        """Gets the errored_databases of this GsaIntegrationSchemaStatus.
        Databases that encountered an error while loading. These databases will not be available for searches.

        Returns
        -------
        Union[dict[str, str], None, Unset_Type]
            The errored_databases of this GsaIntegrationSchemaStatus.
        """
        return self._errored_databases

    @errored_databases.setter
    def errored_databases(
        self, errored_databases: "Union[dict[str, str], None, Unset_Type]"
    ) -> None:
        """Sets the errored_databases of this GsaIntegrationSchemaStatus.
        Databases that encountered an error while loading. These databases will not be available for searches.

        Parameters
        ----------
        errored_databases: Union[dict[str, str], None, Unset_Type]
            The errored_databases of this GsaIntegrationSchemaStatus.
        """
        self._errored_databases = errored_databases

    @property
    def loaded_database_index_statuses(
        self,
    ) -> "Union[dict[str, GsaSearchIndexStatus], None, Unset_Type]":
        """Gets the loaded_database_index_statuses of this GsaIntegrationSchemaStatus.
        Index information about all loaded databases, including the out of sync status.

        Returns
        -------
        Union[dict[str, GsaSearchIndexStatus], None, Unset_Type]
            The loaded_database_index_statuses of this GsaIntegrationSchemaStatus.
        """
        return self._loaded_database_index_statuses

    @loaded_database_index_statuses.setter
    def loaded_database_index_statuses(
        self,
        loaded_database_index_statuses: "Union[dict[str, GsaSearchIndexStatus], None, Unset_Type]",
    ) -> None:
        """Sets the loaded_database_index_statuses of this GsaIntegrationSchemaStatus.
        Index information about all loaded databases, including the out of sync status.

        Parameters
        ----------
        loaded_database_index_statuses: Union[dict[str, GsaSearchIndexStatus], None, Unset_Type]
            The loaded_database_index_statuses of this GsaIntegrationSchemaStatus.
        """
        self._loaded_database_index_statuses = loaded_database_index_statuses

    @property
    def search_index_up_to_date(self) -> "Union[bool, Unset_Type]":
        """Gets the search_index_up_to_date of this GsaIntegrationSchemaStatus.
        Whether all changes up to and including the most recent database revision have been sent to the search index. This will return true  even if some of those revisions could not be indexed

        Returns
        -------
        Union[bool, Unset_Type]
            The search_index_up_to_date of this GsaIntegrationSchemaStatus.
        """
        return self._search_index_up_to_date

    @search_index_up_to_date.setter
    def search_index_up_to_date(self, search_index_up_to_date: "Union[bool, Unset_Type]") -> None:
        """Sets the search_index_up_to_date of this GsaIntegrationSchemaStatus.
        Whether all changes up to and including the most recent database revision have been sent to the search index. This will return true  even if some of those revisions could not be indexed

        Parameters
        ----------
        search_index_up_to_date: Union[bool, Unset_Type]
            The search_index_up_to_date of this GsaIntegrationSchemaStatus.
        """
        # Field is not nullable
        if search_index_up_to_date is None:
            raise ValueError("Invalid value for 'search_index_up_to_date', must not be 'None'")
        self._search_index_up_to_date = search_index_up_to_date

    @property
    def search_index_out_of_date_duration(self) -> "Union[str, None, Unset_Type]":
        """Gets the search_index_out_of_date_duration of this GsaIntegrationSchemaStatus.
        How long has the index been out of date.  Specifically the duration between the first non-indexed revision and the current time.

        Returns
        -------
        Union[str, None, Unset_Type]
            The search_index_out_of_date_duration of this GsaIntegrationSchemaStatus.
        """
        return self._search_index_out_of_date_duration

    @search_index_out_of_date_duration.setter
    def search_index_out_of_date_duration(
        self, search_index_out_of_date_duration: "Union[str, None, Unset_Type]"
    ) -> None:
        """Sets the search_index_out_of_date_duration of this GsaIntegrationSchemaStatus.
        How long has the index been out of date.  Specifically the duration between the first non-indexed revision and the current time.

        Parameters
        ----------
        search_index_out_of_date_duration: Union[str, None, Unset_Type]
            The search_index_out_of_date_duration of this GsaIntegrationSchemaStatus.
        """
        self._search_index_out_of_date_duration = search_index_out_of_date_duration

    @property
    def search_index_in_sync(self) -> "Union[bool, Unset_Type]":
        """Gets the search_index_in_sync of this GsaIntegrationSchemaStatus.
        Returns false if the search index is out of sync with the database (i.e. because changes were made that could not be indexed)

        Returns
        -------
        Union[bool, Unset_Type]
            The search_index_in_sync of this GsaIntegrationSchemaStatus.
        """
        return self._search_index_in_sync

    @search_index_in_sync.setter
    def search_index_in_sync(self, search_index_in_sync: "Union[bool, Unset_Type]") -> None:
        """Sets the search_index_in_sync of this GsaIntegrationSchemaStatus.
        Returns false if the search index is out of sync with the database (i.e. because changes were made that could not be indexed)

        Parameters
        ----------
        search_index_in_sync: Union[bool, Unset_Type]
            The search_index_in_sync of this GsaIntegrationSchemaStatus.
        """
        # Field is not nullable
        if search_index_in_sync is None:
            raise ValueError("Invalid value for 'search_index_in_sync', must not be 'None'")
        self._search_index_in_sync = search_index_in_sync

    @property
    def search_index_location(self) -> "Union[str, None, Unset_Type]":
        """Gets the search_index_location of this GsaIntegrationSchemaStatus.
        The location of the index.

        Returns
        -------
        Union[str, None, Unset_Type]
            The search_index_location of this GsaIntegrationSchemaStatus.
        """
        return self._search_index_location

    @search_index_location.setter
    def search_index_location(self, search_index_location: "Union[str, None, Unset_Type]") -> None:
        """Sets the search_index_location of this GsaIntegrationSchemaStatus.
        The location of the index.

        Parameters
        ----------
        search_index_location: Union[str, None, Unset_Type]
            The search_index_location of this GsaIntegrationSchemaStatus.
        """
        self._search_index_location = search_index_location

    @property
    def search_index_is_read_only(self) -> "Union[bool, None, Unset_Type]":
        """Gets the search_index_is_read_only of this GsaIntegrationSchemaStatus.
        True if the index is read only.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The search_index_is_read_only of this GsaIntegrationSchemaStatus.
        """
        return self._search_index_is_read_only

    @search_index_is_read_only.setter
    def search_index_is_read_only(
        self, search_index_is_read_only: "Union[bool, None, Unset_Type]"
    ) -> None:
        """Sets the search_index_is_read_only of this GsaIntegrationSchemaStatus.
        True if the index is read only.

        Parameters
        ----------
        search_index_is_read_only: Union[bool, None, Unset_Type]
            The search_index_is_read_only of this GsaIntegrationSchemaStatus.
        """
        self._search_index_is_read_only = search_index_is_read_only

    @property
    def search_index_unavailable(self) -> "Union[bool, None, Unset_Type]":
        """Gets the search_index_unavailable of this GsaIntegrationSchemaStatus.
        True if the index could not be contacted.

        Returns
        -------
        Union[bool, None, Unset_Type]
            The search_index_unavailable of this GsaIntegrationSchemaStatus.
        """
        return self._search_index_unavailable

    @search_index_unavailable.setter
    def search_index_unavailable(
        self, search_index_unavailable: "Union[bool, None, Unset_Type]"
    ) -> None:
        """Sets the search_index_unavailable of this GsaIntegrationSchemaStatus.
        True if the index could not be contacted.

        Parameters
        ----------
        search_index_unavailable: Union[bool, None, Unset_Type]
            The search_index_unavailable of this GsaIntegrationSchemaStatus.
        """
        self._search_index_unavailable = search_index_unavailable

    @property
    def records_that_failed_to_index(
        self,
    ) -> "Union[list[GsaIndexRecordFailure], None, Unset_Type]":
        """Gets the records_that_failed_to_index of this GsaIntegrationSchemaStatus.
        Details of any records that failed to index.

        Returns
        -------
        Union[list[GsaIndexRecordFailure], None, Unset_Type]
            The records_that_failed_to_index of this GsaIntegrationSchemaStatus.
        """
        return self._records_that_failed_to_index

    @records_that_failed_to_index.setter
    def records_that_failed_to_index(
        self, records_that_failed_to_index: "Union[list[GsaIndexRecordFailure], None, Unset_Type]"
    ) -> None:
        """Sets the records_that_failed_to_index of this GsaIntegrationSchemaStatus.
        Details of any records that failed to index.

        Parameters
        ----------
        records_that_failed_to_index: Union[list[GsaIndexRecordFailure], None, Unset_Type]
            The records_that_failed_to_index of this GsaIntegrationSchemaStatus.
        """
        self._records_that_failed_to_index = records_that_failed_to_index

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
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
        if not isinstance(other, GsaIntegrationSchemaStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
