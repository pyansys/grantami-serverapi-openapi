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
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSelectionSearchesSelectionSearch(ModelBase):
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
        "created_timestamp": "datetime",
        "created_user_or_group": "GrantaServerApiSelectionSearchesUserOrGroup",
        "criteria": "str",
        "current_user_access_info": "dict(str, dict(str, bool))",
        "description": "str",
        "explore_config": "str",
        "last_modified_timestamp": "datetime",
        "last_modified_user_or_group": "GrantaServerApiSelectionSearchesUserOrGroup",
        "name": "str",
        "notes": "str",
        "search_identifier": "str",
    }

    attribute_map: Dict[str, str] = {
        "created_timestamp": "createdTimestamp",
        "created_user_or_group": "createdUserOrGroup",
        "criteria": "criteria",
        "current_user_access_info": "currentUserAccessInfo",
        "description": "description",
        "explore_config": "exploreConfig",
        "last_modified_timestamp": "lastModifiedTimestamp",
        "last_modified_user_or_group": "lastModifiedUserOrGroup",
        "name": "name",
        "notes": "notes",
        "search_identifier": "searchIdentifier",
    }

    subtype_mapping: Dict[str, str] = {
        "createdUserOrGroup": "GrantaServerApiSelectionSearchesUserOrGroup",
        "lastModifiedUserOrGroup": "GrantaServerApiSelectionSearchesUserOrGroup",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        created_timestamp: "Union[datetime, Unset_Type]" = Unset,
        created_user_or_group: "Union[GrantaServerApiSelectionSearchesUserOrGroup, Unset_Type]" = Unset,
        criteria: "Union[str, None, Unset_Type]" = Unset,
        current_user_access_info: "Union[Dict[str, Dict[str, bool]], None, Unset_Type]" = Unset,
        description: "Union[str, None, Unset_Type]" = Unset,
        explore_config: "Union[str, None, Unset_Type]" = Unset,
        last_modified_timestamp: "Union[datetime, Unset_Type]" = Unset,
        last_modified_user_or_group: "Union[GrantaServerApiSelectionSearchesUserOrGroup, Unset_Type]" = Unset,
        name: "Union[str, None, Unset_Type]" = Unset,
        notes: "Union[str, None, Unset_Type]" = Unset,
        search_identifier: "Union[str, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSelectionSearchesSelectionSearch - a model defined in Swagger

        Parameters
        ----------
        created_timestamp: datetime, optional
        created_user_or_group: GrantaServerApiSelectionSearchesUserOrGroup, optional
        criteria: str, optional
        current_user_access_info: Dict[str, Dict[str, bool]], optional
        description: str, optional
        explore_config: str, optional
        last_modified_timestamp: datetime, optional
        last_modified_user_or_group: GrantaServerApiSelectionSearchesUserOrGroup, optional
        name: str, optional
        notes: str, optional
        search_identifier: str, optional
        """
        self._search_identifier: Union[str, Unset_Type] = Unset
        self._name: Union[str, None, Unset_Type] = Unset
        self._description: Union[str, None, Unset_Type] = Unset
        self._notes: Union[str, None, Unset_Type] = Unset
        self._current_user_access_info: Union[
            Dict[str, Dict[str, bool]], None, Unset_Type
        ] = Unset
        self._criteria: Union[str, None, Unset_Type] = Unset
        self._explore_config: Union[str, None, Unset_Type] = Unset
        self._created_timestamp: Union[datetime, Unset_Type] = Unset
        self._created_user_or_group: Union[
            GrantaServerApiSelectionSearchesUserOrGroup, Unset_Type
        ] = Unset
        self._last_modified_timestamp: Union[datetime, Unset_Type] = Unset
        self._last_modified_user_or_group: Union[
            GrantaServerApiSelectionSearchesUserOrGroup, Unset_Type
        ] = Unset

        if search_identifier is not Unset:
            self.search_identifier = search_identifier
        if name is not Unset:
            self.name = name
        if description is not Unset:
            self.description = description
        if notes is not Unset:
            self.notes = notes
        if current_user_access_info is not Unset:
            self.current_user_access_info = current_user_access_info
        if criteria is not Unset:
            self.criteria = criteria
        if explore_config is not Unset:
            self.explore_config = explore_config
        if created_timestamp is not Unset:
            self.created_timestamp = created_timestamp
        if created_user_or_group is not Unset:
            self.created_user_or_group = created_user_or_group
        if last_modified_timestamp is not Unset:
            self.last_modified_timestamp = last_modified_timestamp
        if last_modified_user_or_group is not Unset:
            self.last_modified_user_or_group = last_modified_user_or_group

    @property
    def search_identifier(self) -> "Union[str, Unset_Type]":
        """Gets the search_identifier of this GrantaServerApiSelectionSearchesSelectionSearch.

        Returns
        -------
        Union[str, Unset_Type]
            The search_identifier of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        return self._search_identifier

    @search_identifier.setter
    def search_identifier(self, search_identifier: "Union[str, Unset_Type]") -> None:
        """Sets the search_identifier of this GrantaServerApiSelectionSearchesSelectionSearch.

        Parameters
        ----------
        search_identifier: Union[str, Unset_Type]
            The search_identifier of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        # Field is not nullable
        if search_identifier is None:
            raise ValueError(
                "Invalid value for 'search_identifier', must not be 'None'"
            )
        self._search_identifier = search_identifier

    @property
    def name(self) -> "Union[str, None, Unset_Type]":
        """Gets the name of this GrantaServerApiSelectionSearchesSelectionSearch.

        Returns
        -------
        Union[str, None, Unset_Type]
            The name of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, None, Unset_Type]") -> None:
        """Sets the name of this GrantaServerApiSelectionSearchesSelectionSearch.

        Parameters
        ----------
        name: Union[str, None, Unset_Type]
            The name of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        self._name = name

    @property
    def description(self) -> "Union[str, None, Unset_Type]":
        """Gets the description of this GrantaServerApiSelectionSearchesSelectionSearch.

        Returns
        -------
        Union[str, None, Unset_Type]
            The description of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        return self._description

    @description.setter
    def description(self, description: "Union[str, None, Unset_Type]") -> None:
        """Sets the description of this GrantaServerApiSelectionSearchesSelectionSearch.

        Parameters
        ----------
        description: Union[str, None, Unset_Type]
            The description of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        self._description = description

    @property
    def notes(self) -> "Union[str, None, Unset_Type]":
        """Gets the notes of this GrantaServerApiSelectionSearchesSelectionSearch.

        Returns
        -------
        Union[str, None, Unset_Type]
            The notes of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        return self._notes

    @notes.setter
    def notes(self, notes: "Union[str, None, Unset_Type]") -> None:
        """Sets the notes of this GrantaServerApiSelectionSearchesSelectionSearch.

        Parameters
        ----------
        notes: Union[str, None, Unset_Type]
            The notes of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        self._notes = notes

    @property
    def current_user_access_info(
        self,
    ) -> "Union[Dict[str, Dict[str, bool]], None, Unset_Type]":
        """Gets the current_user_access_info of this GrantaServerApiSelectionSearchesSelectionSearch.

        Returns
        -------
        Union[Dict[str, Dict[str, bool]], None, Unset_Type]
            The current_user_access_info of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        return self._current_user_access_info

    @current_user_access_info.setter
    def current_user_access_info(
        self,
        current_user_access_info: "Union[Dict[str, Dict[str, bool]], None, Unset_Type]",
    ) -> None:
        """Sets the current_user_access_info of this GrantaServerApiSelectionSearchesSelectionSearch.

        Parameters
        ----------
        current_user_access_info: Union[Dict[str, Dict[str, bool]], None, Unset_Type]
            The current_user_access_info of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        self._current_user_access_info = current_user_access_info

    @property
    def criteria(self) -> "Union[str, None, Unset_Type]":
        """Gets the criteria of this GrantaServerApiSelectionSearchesSelectionSearch.

        Returns
        -------
        Union[str, None, Unset_Type]
            The criteria of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria: "Union[str, None, Unset_Type]") -> None:
        """Sets the criteria of this GrantaServerApiSelectionSearchesSelectionSearch.

        Parameters
        ----------
        criteria: Union[str, None, Unset_Type]
            The criteria of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        self._criteria = criteria

    @property
    def explore_config(self) -> "Union[str, None, Unset_Type]":
        """Gets the explore_config of this GrantaServerApiSelectionSearchesSelectionSearch.

        Returns
        -------
        Union[str, None, Unset_Type]
            The explore_config of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        return self._explore_config

    @explore_config.setter
    def explore_config(self, explore_config: "Union[str, None, Unset_Type]") -> None:
        """Sets the explore_config of this GrantaServerApiSelectionSearchesSelectionSearch.

        Parameters
        ----------
        explore_config: Union[str, None, Unset_Type]
            The explore_config of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        self._explore_config = explore_config

    @property
    def created_timestamp(self) -> "Union[datetime, Unset_Type]":
        """Gets the created_timestamp of this GrantaServerApiSelectionSearchesSelectionSearch.

        Returns
        -------
        Union[datetime, Unset_Type]
            The created_timestamp of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        return self._created_timestamp

    @created_timestamp.setter
    def created_timestamp(
        self, created_timestamp: "Union[datetime, Unset_Type]"
    ) -> None:
        """Sets the created_timestamp of this GrantaServerApiSelectionSearchesSelectionSearch.

        Parameters
        ----------
        created_timestamp: Union[datetime, Unset_Type]
            The created_timestamp of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        # Field is not nullable
        if created_timestamp is None:
            raise ValueError(
                "Invalid value for 'created_timestamp', must not be 'None'"
            )
        self._created_timestamp = created_timestamp

    @property
    def created_user_or_group(
        self,
    ) -> "Union[GrantaServerApiSelectionSearchesUserOrGroup, Unset_Type]":
        """Gets the created_user_or_group of this GrantaServerApiSelectionSearchesSelectionSearch.

        Returns
        -------
        Union[GrantaServerApiSelectionSearchesUserOrGroup, Unset_Type]
            The created_user_or_group of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        return self._created_user_or_group

    @created_user_or_group.setter
    def created_user_or_group(
        self,
        created_user_or_group: "Union[GrantaServerApiSelectionSearchesUserOrGroup, Unset_Type]",
    ) -> None:
        """Sets the created_user_or_group of this GrantaServerApiSelectionSearchesSelectionSearch.

        Parameters
        ----------
        created_user_or_group: Union[GrantaServerApiSelectionSearchesUserOrGroup, Unset_Type]
            The created_user_or_group of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        # Field is not nullable
        if created_user_or_group is None:
            raise ValueError(
                "Invalid value for 'created_user_or_group', must not be 'None'"
            )
        self._created_user_or_group = created_user_or_group

    @property
    def last_modified_timestamp(self) -> "Union[datetime, Unset_Type]":
        """Gets the last_modified_timestamp of this GrantaServerApiSelectionSearchesSelectionSearch.

        Returns
        -------
        Union[datetime, Unset_Type]
            The last_modified_timestamp of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        return self._last_modified_timestamp

    @last_modified_timestamp.setter
    def last_modified_timestamp(
        self, last_modified_timestamp: "Union[datetime, Unset_Type]"
    ) -> None:
        """Sets the last_modified_timestamp of this GrantaServerApiSelectionSearchesSelectionSearch.

        Parameters
        ----------
        last_modified_timestamp: Union[datetime, Unset_Type]
            The last_modified_timestamp of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        # Field is not nullable
        if last_modified_timestamp is None:
            raise ValueError(
                "Invalid value for 'last_modified_timestamp', must not be 'None'"
            )
        self._last_modified_timestamp = last_modified_timestamp

    @property
    def last_modified_user_or_group(
        self,
    ) -> "Union[GrantaServerApiSelectionSearchesUserOrGroup, Unset_Type]":
        """Gets the last_modified_user_or_group of this GrantaServerApiSelectionSearchesSelectionSearch.

        Returns
        -------
        Union[GrantaServerApiSelectionSearchesUserOrGroup, Unset_Type]
            The last_modified_user_or_group of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        return self._last_modified_user_or_group

    @last_modified_user_or_group.setter
    def last_modified_user_or_group(
        self,
        last_modified_user_or_group: "Union[GrantaServerApiSelectionSearchesUserOrGroup, Unset_Type]",
    ) -> None:
        """Sets the last_modified_user_or_group of this GrantaServerApiSelectionSearchesSelectionSearch.

        Parameters
        ----------
        last_modified_user_or_group: Union[GrantaServerApiSelectionSearchesUserOrGroup, Unset_Type]
            The last_modified_user_or_group of this GrantaServerApiSelectionSearchesSelectionSearch.
        """
        # Field is not nullable
        if last_modified_user_or_group is None:
            raise ValueError(
                "Invalid value for 'last_modified_user_or_group', must not be 'None'"
            )
        self._last_modified_user_or_group = last_modified_user_or_group

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
        if not isinstance(other, GrantaServerApiSelectionSearchesSelectionSearch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
