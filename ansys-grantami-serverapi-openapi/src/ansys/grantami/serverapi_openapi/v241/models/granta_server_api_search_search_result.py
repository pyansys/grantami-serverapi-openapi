# Copyright (C) 2023 - 2025 ANSYS, Inc. and/or its affiliates.
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
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase

if TYPE_CHECKING:
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
    swagger_types = {
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

    attribute_map = {
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

    subtype_mapping = {
        "type": "GrantaServerApiRecordType",
        "sortingValue": "GrantaServerApiSearchSortingValue",
    }

    discriminator = None

    def __init__(
        self,
        *,
        cubic_spline_status: "Optional[str]" = None,
        database_key: "Optional[str]" = None,
        parent_identity: "Optional[int]" = None,
        record_color: "Optional[str]" = None,
        record_guid: "Optional[str]" = None,
        record_history_guid: "Optional[str]" = None,
        record_history_identity: "Optional[int]" = None,
        record_identity: "Optional[int]" = None,
        record_name: "Optional[str]" = None,
        score: "Optional[float]" = None,
        sorting_value: "Optional[GrantaServerApiSearchSortingValue]" = None,
        table_guid: "Optional[str]" = None,
        table_identity: "Optional[int]" = None,
        tree_name: "Optional[str]" = None,
        type: "Optional[GrantaServerApiRecordType]" = None,
        version_control_state: "Optional[str]" = None,
        version_number: "Optional[int]" = None,
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
        self._database_key = None
        self._record_history_identity = None
        self._record_identity = None
        self._record_history_guid = None
        self._record_guid = None
        self._record_name = None
        self._tree_name = None
        self._record_color = None
        self._table_identity = None
        self._table_guid = None
        self._cubic_spline_status = None
        self._version_control_state = None
        self._version_number = None
        self._parent_identity = None
        self._type = None
        self._score = None
        self._sorting_value = None

        if database_key is not None:
            self.database_key = database_key
        if record_history_identity is not None:
            self.record_history_identity = record_history_identity
        if record_identity is not None:
            self.record_identity = record_identity
        if record_history_guid is not None:
            self.record_history_guid = record_history_guid
        if record_guid is not None:
            self.record_guid = record_guid
        if record_name is not None:
            self.record_name = record_name
        if tree_name is not None:
            self.tree_name = tree_name
        if record_color is not None:
            self.record_color = record_color
        if table_identity is not None:
            self.table_identity = table_identity
        if table_guid is not None:
            self.table_guid = table_guid
        if cubic_spline_status is not None:
            self.cubic_spline_status = cubic_spline_status
        if version_control_state is not None:
            self.version_control_state = version_control_state
        if version_number is not None:
            self.version_number = version_number
        if parent_identity is not None:
            self.parent_identity = parent_identity
        if type is not None:
            self.type = type
        if score is not None:
            self.score = score
        if sorting_value is not None:
            self.sorting_value = sorting_value

    @property
    def database_key(self) -> "str":
        """Gets the database_key of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        str
            The database_key of this GrantaServerApiSearchSearchResult.
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key: "str") -> None:
        """Sets the database_key of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        database_key: str
            The database_key of this GrantaServerApiSearchSearchResult.
        """
        self._database_key = database_key

    @property
    def record_history_identity(self) -> "int":
        """Gets the record_history_identity of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        int
            The record_history_identity of this GrantaServerApiSearchSearchResult.
        """
        return self._record_history_identity

    @record_history_identity.setter
    def record_history_identity(self, record_history_identity: "int") -> None:
        """Sets the record_history_identity of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        record_history_identity: int
            The record_history_identity of this GrantaServerApiSearchSearchResult.
        """
        self._record_history_identity = record_history_identity

    @property
    def record_identity(self) -> "int":
        """Gets the record_identity of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        int
            The record_identity of this GrantaServerApiSearchSearchResult.
        """
        return self._record_identity

    @record_identity.setter
    def record_identity(self, record_identity: "int") -> None:
        """Sets the record_identity of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        record_identity: int
            The record_identity of this GrantaServerApiSearchSearchResult.
        """
        self._record_identity = record_identity

    @property
    def record_history_guid(self) -> "str":
        """Gets the record_history_guid of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        str
            The record_history_guid of this GrantaServerApiSearchSearchResult.
        """
        return self._record_history_guid

    @record_history_guid.setter
    def record_history_guid(self, record_history_guid: "str") -> None:
        """Sets the record_history_guid of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        record_history_guid: str
            The record_history_guid of this GrantaServerApiSearchSearchResult.
        """
        self._record_history_guid = record_history_guid

    @property
    def record_guid(self) -> "str":
        """Gets the record_guid of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        str
            The record_guid of this GrantaServerApiSearchSearchResult.
        """
        return self._record_guid

    @record_guid.setter
    def record_guid(self, record_guid: "str") -> None:
        """Sets the record_guid of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        record_guid: str
            The record_guid of this GrantaServerApiSearchSearchResult.
        """
        self._record_guid = record_guid

    @property
    def record_name(self) -> "str":
        """Gets the record_name of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        str
            The record_name of this GrantaServerApiSearchSearchResult.
        """
        return self._record_name

    @record_name.setter
    def record_name(self, record_name: "str") -> None:
        """Sets the record_name of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        record_name: str
            The record_name of this GrantaServerApiSearchSearchResult.
        """
        self._record_name = record_name

    @property
    def tree_name(self) -> "str":
        """Gets the tree_name of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        str
            The tree_name of this GrantaServerApiSearchSearchResult.
        """
        return self._tree_name

    @tree_name.setter
    def tree_name(self, tree_name: "str") -> None:
        """Sets the tree_name of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        tree_name: str
            The tree_name of this GrantaServerApiSearchSearchResult.
        """
        self._tree_name = tree_name

    @property
    def record_color(self) -> "str":
        """Gets the record_color of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        str
            The record_color of this GrantaServerApiSearchSearchResult.
        """
        return self._record_color

    @record_color.setter
    def record_color(self, record_color: "str") -> None:
        """Sets the record_color of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        record_color: str
            The record_color of this GrantaServerApiSearchSearchResult.
        """
        self._record_color = record_color

    @property
    def table_identity(self) -> "int":
        """Gets the table_identity of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        int
            The table_identity of this GrantaServerApiSearchSearchResult.
        """
        return self._table_identity

    @table_identity.setter
    def table_identity(self, table_identity: "int") -> None:
        """Sets the table_identity of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        table_identity: int
            The table_identity of this GrantaServerApiSearchSearchResult.
        """
        self._table_identity = table_identity

    @property
    def table_guid(self) -> "str":
        """Gets the table_guid of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        str
            The table_guid of this GrantaServerApiSearchSearchResult.
        """
        return self._table_guid

    @table_guid.setter
    def table_guid(self, table_guid: "str") -> None:
        """Sets the table_guid of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        table_guid: str
            The table_guid of this GrantaServerApiSearchSearchResult.
        """
        self._table_guid = table_guid

    @property
    def cubic_spline_status(self) -> "str":
        """Gets the cubic_spline_status of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        str
            The cubic_spline_status of this GrantaServerApiSearchSearchResult.
        """
        return self._cubic_spline_status

    @cubic_spline_status.setter
    def cubic_spline_status(self, cubic_spline_status: "str") -> None:
        """Sets the cubic_spline_status of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        cubic_spline_status: str
            The cubic_spline_status of this GrantaServerApiSearchSearchResult.
        """
        self._cubic_spline_status = cubic_spline_status

    @property
    def version_control_state(self) -> "str":
        """Gets the version_control_state of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        str
            The version_control_state of this GrantaServerApiSearchSearchResult.
        """
        return self._version_control_state

    @version_control_state.setter
    def version_control_state(self, version_control_state: "str") -> None:
        """Sets the version_control_state of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        version_control_state: str
            The version_control_state of this GrantaServerApiSearchSearchResult.
        """
        self._version_control_state = version_control_state

    @property
    def version_number(self) -> "int":
        """Gets the version_number of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        int
            The version_number of this GrantaServerApiSearchSearchResult.
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number: "int") -> None:
        """Sets the version_number of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        version_number: int
            The version_number of this GrantaServerApiSearchSearchResult.
        """
        self._version_number = version_number

    @property
    def parent_identity(self) -> "int":
        """Gets the parent_identity of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        int
            The parent_identity of this GrantaServerApiSearchSearchResult.
        """
        return self._parent_identity

    @parent_identity.setter
    def parent_identity(self, parent_identity: "int") -> None:
        """Sets the parent_identity of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        parent_identity: int
            The parent_identity of this GrantaServerApiSearchSearchResult.
        """
        self._parent_identity = parent_identity

    @property
    def type(self) -> "GrantaServerApiRecordType":
        """Gets the type of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        GrantaServerApiRecordType
            The type of this GrantaServerApiSearchSearchResult.
        """
        return self._type

    @type.setter
    def type(self, type: "GrantaServerApiRecordType") -> None:
        """Sets the type of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        type: GrantaServerApiRecordType
            The type of this GrantaServerApiSearchSearchResult.
        """
        self._type = type

    @property
    def score(self) -> "float":
        """Gets the score of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        float
            The score of this GrantaServerApiSearchSearchResult.
        """
        return self._score

    @score.setter
    def score(self, score: "float") -> None:
        """Sets the score of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        score: float
            The score of this GrantaServerApiSearchSearchResult.
        """
        self._score = score

    @property
    def sorting_value(self) -> "GrantaServerApiSearchSortingValue":
        """Gets the sorting_value of this GrantaServerApiSearchSearchResult.

        Returns
        -------
        GrantaServerApiSearchSortingValue
            The sorting_value of this GrantaServerApiSearchSearchResult.
        """
        return self._sorting_value

    @sorting_value.setter
    def sorting_value(self, sorting_value: "GrantaServerApiSearchSortingValue") -> None:
        """Sets the sorting_value of this GrantaServerApiSearchSearchResult.

        Parameters
        ----------
        sorting_value: GrantaServerApiSearchSortingValue
            The sorting_value of this GrantaServerApiSearchSearchResult.
        """
        self._sorting_value = sorting_value

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
        if not isinstance(other, GrantaServerApiSearchSearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
