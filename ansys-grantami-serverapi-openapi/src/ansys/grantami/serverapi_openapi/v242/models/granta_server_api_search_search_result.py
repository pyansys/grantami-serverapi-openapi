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


class GrantaServerApiSearchSearchResult(ModelBase):
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
        "cubic_spline_status": "str",
        "database_key": "str",
        "parent_identity": "int",
        "record_color": "str",
        "record_guid": "str",
        "record_history_guid": "str",
        "record_history_identity": "int",
        "record_identity": "int",
        "record_name": "str",
        "score": "float",
        "sorting_value": "GrantaServerApiSearchSortingValue",
        "table_guid": "str",
        "table_identity": "int",
        "tree_name": "str",
        "type": "GrantaServerApiRecordType",
        "version_control_state": "str",
        "version_number": "int",
    }

    attribute_map: Dict[str, str] = {
        "cubic_spline_status": "cubicSplineStatus",
        "database_key": "databaseKey",
        "parent_identity": "parentIdentity",
        "record_color": "recordColor",
        "record_guid": "recordGuid",
        "record_history_guid": "recordHistoryGuid",
        "record_history_identity": "recordHistoryIdentity",
        "record_identity": "recordIdentity",
        "record_name": "recordName",
        "score": "score",
        "sorting_value": "sortingValue",
        "table_guid": "tableGuid",
        "table_identity": "tableIdentity",
        "tree_name": "treeName",
        "type": "type",
        "version_control_state": "versionControlState",
        "version_number": "versionNumber",
    }

    subtype_mapping: Dict[str, str] = {
        "type": "GrantaServerApiRecordType",
        "sortingValue": "GrantaServerApiSearchSortingValue",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        cubic_spline_status: "Union[str, None, Unset_Type]" = Unset,
        database_key: "Union[str, None, Unset_Type]" = Unset,
        parent_identity: "Union[int, None, Unset_Type]" = Unset,
        record_color: "Union[str, None, Unset_Type]" = Unset,
        record_guid: "Union[str, None, Unset_Type]" = Unset,
        record_history_guid: "Union[str, None, Unset_Type]" = Unset,
        record_history_identity: "Union[int, Unset_Type]" = Unset,
        record_identity: "Union[int, Unset_Type]" = Unset,
        record_name: "Union[str, None, Unset_Type]" = Unset,
        score: "Union[float, None, Unset_Type]" = Unset,
        sorting_value: "Union[GrantaServerApiSearchSortingValue, Unset_Type]" = Unset,
        table_guid: "Union[str, Unset_Type]" = Unset,
        table_identity: "Union[int, Unset_Type]" = Unset,
        tree_name: "Union[str, None, Unset_Type]" = Unset,
        type: "Union[GrantaServerApiRecordType, Unset_Type]" = Unset,
        version_control_state: "Union[str, None, Unset_Type]" = Unset,
        version_number: "Union[int, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSearchSearchResult - a model defined in Swagger

        Parameters
        ----------
        cubic_spline_status: str, optional
        database_key: str, optional
        parent_identity: int, optional
        record_color: str, optional
        record_guid: str, optional
        record_history_guid: str, optional
        record_history_identity: int, optional
        record_identity: int, optional
        record_name: str, optional
        score: float, optional
        sorting_value: GrantaServerApiSearchSortingValue, optional
        table_guid: str, optional
        table_identity: int, optional
        tree_name: str, optional
        type: GrantaServerApiRecordType, optional
        version_control_state: str, optional
        version_number: int, optional
        """
        self._database_key: Union[str, None, Unset_Type] = Unset
        self._record_history_identity: Union[int, Unset_Type] = Unset
        self._record_identity: Union[int, Unset_Type] = Unset
        self._record_history_guid: Union[str, None, Unset_Type] = Unset
        self._record_guid: Union[str, None, Unset_Type] = Unset
        self._record_name: Union[str, None, Unset_Type] = Unset
        self._tree_name: Union[str, None, Unset_Type] = Unset
        self._record_color: Union[str, None, Unset_Type] = Unset
        self._table_identity: Union[int, Unset_Type] = Unset
        self._table_guid: Union[str, Unset_Type] = Unset
        self._cubic_spline_status: Union[str, None, Unset_Type] = Unset
        self._version_control_state: Union[str, None, Unset_Type] = Unset
        self._version_number: Union[int, Unset_Type] = Unset
        self._parent_identity: Union[int, None, Unset_Type] = Unset
        self._type: Union[GrantaServerApiRecordType, Unset_Type] = Unset
        self._score: Union[float, None, Unset_Type] = Unset
        self._sorting_value: Union[GrantaServerApiSearchSortingValue, Unset_Type] = Unset

        if database_key is not Unset:
            self.database_key = database_key
        if record_history_identity is not Unset:
            self.record_history_identity = record_history_identity
        if record_identity is not Unset:
            self.record_identity = record_identity
        if record_history_guid is not Unset:
            self.record_history_guid = record_history_guid
        if record_guid is not Unset:
            self.record_guid = record_guid
        if record_name is not Unset:
            self.record_name = record_name
        if tree_name is not Unset:
            self.tree_name = tree_name
        if record_color is not Unset:
            self.record_color = record_color
        if table_identity is not Unset:
            self.table_identity = table_identity
        if table_guid is not Unset:
            self.table_guid = table_guid
        if cubic_spline_status is not Unset:
            self.cubic_spline_status = cubic_spline_status
        if version_control_state is not Unset:
            self.version_control_state = version_control_state
        if version_number is not Unset:
            self.version_number = version_number
        if parent_identity is not Unset:
            self.parent_identity = parent_identity
        if type is not Unset:
            self.type = type
        if score is not Unset:
            self.score = score
        if sorting_value is not Unset:
            self.sorting_value = sorting_value

    @property
    def database_key(self) -> "Union[str, None, Unset_Type]":
        """Gets the database_key of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        Union[str, None, Unset_Type]
            The database_key of this GrantaServerApiSearchSearchResult.
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key: "Union[str, None, Unset_Type]") -> None:
        """Sets the database_key of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        database_key: Union[str, None, Unset_Type]
            The database_key of this GrantaServerApiSearchSearchResult.
        """
        self._database_key = database_key

    @property
    def record_history_identity(self) -> "Union[int, Unset_Type]":
        """Gets the record_history_identity of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        Union[int, Unset_Type]
            The record_history_identity of this GrantaServerApiSearchSearchResult.
        """
        return self._record_history_identity

    @record_history_identity.setter
    def record_history_identity(self, record_history_identity: "Union[int, Unset_Type]") -> None:
        """Sets the record_history_identity of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        record_history_identity: Union[int, Unset_Type]
            The record_history_identity of this GrantaServerApiSearchSearchResult.
        """
        # Field is not nullable
        if record_history_identity is None:
            raise ValueError("Invalid value for 'record_history_identity', must not be 'None'")
        self._record_history_identity = record_history_identity

    @property
    def record_identity(self) -> "Union[int, Unset_Type]":
        """Gets the record_identity of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        Union[int, Unset_Type]
            The record_identity of this GrantaServerApiSearchSearchResult.
        """
        return self._record_identity

    @record_identity.setter
    def record_identity(self, record_identity: "Union[int, Unset_Type]") -> None:
        """Sets the record_identity of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        record_identity: Union[int, Unset_Type]
            The record_identity of this GrantaServerApiSearchSearchResult.
        """
        # Field is not nullable
        if record_identity is None:
            raise ValueError("Invalid value for 'record_identity', must not be 'None'")
        self._record_identity = record_identity

    @property
    def record_history_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the record_history_guid of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        Union[str, None, Unset_Type]
            The record_history_guid of this GrantaServerApiSearchSearchResult.
        """
        return self._record_history_guid

    @record_history_guid.setter
    def record_history_guid(self, record_history_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the record_history_guid of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        record_history_guid: Union[str, None, Unset_Type]
            The record_history_guid of this GrantaServerApiSearchSearchResult.
        """
        self._record_history_guid = record_history_guid

    @property
    def record_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the record_guid of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        Union[str, None, Unset_Type]
            The record_guid of this GrantaServerApiSearchSearchResult.
        """
        return self._record_guid

    @record_guid.setter
    def record_guid(self, record_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the record_guid of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        record_guid: Union[str, None, Unset_Type]
            The record_guid of this GrantaServerApiSearchSearchResult.
        """
        self._record_guid = record_guid

    @property
    def record_name(self) -> "Union[str, None, Unset_Type]":
        """Gets the record_name of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        Union[str, None, Unset_Type]
            The record_name of this GrantaServerApiSearchSearchResult.
        """
        return self._record_name

    @record_name.setter
    def record_name(self, record_name: "Union[str, None, Unset_Type]") -> None:
        """Sets the record_name of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        record_name: Union[str, None, Unset_Type]
            The record_name of this GrantaServerApiSearchSearchResult.
        """
        self._record_name = record_name

    @property
    def tree_name(self) -> "Union[str, None, Unset_Type]":
        """Gets the tree_name of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        Union[str, None, Unset_Type]
            The tree_name of this GrantaServerApiSearchSearchResult.
        """
        return self._tree_name

    @tree_name.setter
    def tree_name(self, tree_name: "Union[str, None, Unset_Type]") -> None:
        """Sets the tree_name of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        tree_name: Union[str, None, Unset_Type]
            The tree_name of this GrantaServerApiSearchSearchResult.
        """
        self._tree_name = tree_name

    @property
    def record_color(self) -> "Union[str, None, Unset_Type]":
        """Gets the record_color of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        Union[str, None, Unset_Type]
            The record_color of this GrantaServerApiSearchSearchResult.
        """
        return self._record_color

    @record_color.setter
    def record_color(self, record_color: "Union[str, None, Unset_Type]") -> None:
        """Sets the record_color of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        record_color: Union[str, None, Unset_Type]
            The record_color of this GrantaServerApiSearchSearchResult.
        """
        self._record_color = record_color

    @property
    def table_identity(self) -> "Union[int, Unset_Type]":
        """Gets the table_identity of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        Union[int, Unset_Type]
            The table_identity of this GrantaServerApiSearchSearchResult.
        """
        return self._table_identity

    @table_identity.setter
    def table_identity(self, table_identity: "Union[int, Unset_Type]") -> None:
        """Sets the table_identity of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        table_identity: Union[int, Unset_Type]
            The table_identity of this GrantaServerApiSearchSearchResult.
        """
        # Field is not nullable
        if table_identity is None:
            raise ValueError("Invalid value for 'table_identity', must not be 'None'")
        self._table_identity = table_identity

    @property
    def table_guid(self) -> "Union[str, Unset_Type]":
        """Gets the table_guid of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        Union[str, Unset_Type]
            The table_guid of this GrantaServerApiSearchSearchResult.
        """
        return self._table_guid

    @table_guid.setter
    def table_guid(self, table_guid: "Union[str, Unset_Type]") -> None:
        """Sets the table_guid of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        table_guid: Union[str, Unset_Type]
            The table_guid of this GrantaServerApiSearchSearchResult.
        """
        # Field is not nullable
        if table_guid is None:
            raise ValueError("Invalid value for 'table_guid', must not be 'None'")
        self._table_guid = table_guid

    @property
    def cubic_spline_status(self) -> "Union[str, None, Unset_Type]":
        """Gets the cubic_spline_status of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        Union[str, None, Unset_Type]
            The cubic_spline_status of this GrantaServerApiSearchSearchResult.
        """
        return self._cubic_spline_status

    @cubic_spline_status.setter
    def cubic_spline_status(self, cubic_spline_status: "Union[str, None, Unset_Type]") -> None:
        """Sets the cubic_spline_status of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        cubic_spline_status: Union[str, None, Unset_Type]
            The cubic_spline_status of this GrantaServerApiSearchSearchResult.
        """
        self._cubic_spline_status = cubic_spline_status

    @property
    def version_control_state(self) -> "Union[str, None, Unset_Type]":
        """Gets the version_control_state of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        Union[str, None, Unset_Type]
            The version_control_state of this GrantaServerApiSearchSearchResult.
        """
        return self._version_control_state

    @version_control_state.setter
    def version_control_state(self, version_control_state: "Union[str, None, Unset_Type]") -> None:
        """Sets the version_control_state of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        version_control_state: Union[str, None, Unset_Type]
            The version_control_state of this GrantaServerApiSearchSearchResult.
        """
        self._version_control_state = version_control_state

    @property
    def version_number(self) -> "Union[int, Unset_Type]":
        """Gets the version_number of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        Union[int, Unset_Type]
            The version_number of this GrantaServerApiSearchSearchResult.
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number: "Union[int, Unset_Type]") -> None:
        """Sets the version_number of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        version_number: Union[int, Unset_Type]
            The version_number of this GrantaServerApiSearchSearchResult.
        """
        # Field is not nullable
        if version_number is None:
            raise ValueError("Invalid value for 'version_number', must not be 'None'")
        self._version_number = version_number

    @property
    def parent_identity(self) -> "Union[int, None, Unset_Type]":
        """Gets the parent_identity of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        Union[int, None, Unset_Type]
            The parent_identity of this GrantaServerApiSearchSearchResult.
        """
        return self._parent_identity

    @parent_identity.setter
    def parent_identity(self, parent_identity: "Union[int, None, Unset_Type]") -> None:
        """Sets the parent_identity of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        parent_identity: Union[int, None, Unset_Type]
            The parent_identity of this GrantaServerApiSearchSearchResult.
        """
        self._parent_identity = parent_identity

    @property
    def type(self) -> "Union[GrantaServerApiRecordType, Unset_Type]":
        """Gets the type of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        Union[GrantaServerApiRecordType, Unset_Type]
            The type of this GrantaServerApiSearchSearchResult.
        """
        return self._type

    @type.setter
    def type(self, type: "Union[GrantaServerApiRecordType, Unset_Type]") -> None:
        """Sets the type of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        type: Union[GrantaServerApiRecordType, Unset_Type]
            The type of this GrantaServerApiSearchSearchResult.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @property
    def score(self) -> "Union[float, None, Unset_Type]":
        """Gets the score of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        Union[float, None, Unset_Type]
            The score of this GrantaServerApiSearchSearchResult.
        """
        return self._score

    @score.setter
    def score(self, score: "Union[float, None, Unset_Type]") -> None:
        """Sets the score of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        score: Union[float, None, Unset_Type]
            The score of this GrantaServerApiSearchSearchResult.
        """
        self._score = score

    @property
    def sorting_value(self) -> "Union[GrantaServerApiSearchSortingValue, Unset_Type]":
        """Gets the sorting_value of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        Union[GrantaServerApiSearchSortingValue, Unset_Type]
            The sorting_value of this GrantaServerApiSearchSearchResult.
        """
        return self._sorting_value

    @sorting_value.setter
    def sorting_value(
        self, sorting_value: "Union[GrantaServerApiSearchSortingValue, Unset_Type]"
    ) -> None:
        """Sets the sorting_value of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        sorting_value: Union[GrantaServerApiSearchSortingValue, Unset_Type]
            The sorting_value of this GrantaServerApiSearchSearchResult.
        """
        # Field is not nullable
        if sorting_value is None:
            raise ValueError("Invalid value for 'sorting_value', must not be 'None'")
        self._sorting_value = sorting_value

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
        if not isinstance(other, GrantaServerApiSearchSearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
