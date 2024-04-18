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


class GrantaServerApiDataExportExportFailuresDatumReference(ModelBase):
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
        "attribute_identity": "int",
        "database_key": "str",
        "record_history_identity": "int",
        "attribute_guid": "str",
    }

    attribute_map: Dict[str, str] = {
        "attribute_identity": "attributeIdentity",
        "database_key": "databaseKey",
        "record_history_identity": "recordHistoryIdentity",
        "attribute_guid": "attributeGuid",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_identity: "int",
        database_key: "str",
        record_history_identity: "int",
        attribute_guid: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiDataExportExportFailuresDatumReference - a model defined in Swagger

        Parameters
        ----------
        attribute_identity: int
        database_key: str
        record_history_identity: int
        attribute_guid: str, optional
        """
        self._database_key: str
        self._record_history_identity: int
        self._attribute_identity: int
        self._attribute_guid: Union[str, None, Unset_Type] = Unset

        self.database_key = database_key
        self.record_history_identity = record_history_identity
        self.attribute_identity = attribute_identity
        if attribute_guid is not Unset:
            self.attribute_guid = attribute_guid

    @property
    def database_key(self) -> "str":
        """Gets the database_key of this GrantaServerApiDataExportExportFailuresDatumReference.

        Returns
        -------
        str
            The database_key of this GrantaServerApiDataExportExportFailuresDatumReference.
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key: "str") -> None:
        """Sets the database_key of this GrantaServerApiDataExportExportFailuresDatumReference.

        Parameters
        ----------
        database_key: str
            The database_key of this GrantaServerApiDataExportExportFailuresDatumReference.
        """
        # Field is not nullable
        if database_key is None:
            raise ValueError("Invalid value for 'database_key', must not be 'None'")
        # Field is required
        if database_key is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'database_key', must not be 'Unset'")
        self._database_key = database_key

    @property
    def record_history_identity(self) -> "int":
        """Gets the record_history_identity of this GrantaServerApiDataExportExportFailuresDatumReference.

        Returns
        -------
        int
            The record_history_identity of this GrantaServerApiDataExportExportFailuresDatumReference.
        """
        return self._record_history_identity

    @record_history_identity.setter
    def record_history_identity(self, record_history_identity: "int") -> None:
        """Sets the record_history_identity of this GrantaServerApiDataExportExportFailuresDatumReference.

        Parameters
        ----------
        record_history_identity: int
            The record_history_identity of this GrantaServerApiDataExportExportFailuresDatumReference.
        """
        # Field is not nullable
        if record_history_identity is None:
            raise ValueError(
                "Invalid value for 'record_history_identity', must not be 'None'"
            )
        # Field is required
        if record_history_identity is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'record_history_identity', must not be 'Unset'"
            )
        self._record_history_identity = record_history_identity

    @property
    def attribute_identity(self) -> "int":
        """Gets the attribute_identity of this GrantaServerApiDataExportExportFailuresDatumReference.

        Returns
        -------
        int
            The attribute_identity of this GrantaServerApiDataExportExportFailuresDatumReference.
        """
        return self._attribute_identity

    @attribute_identity.setter
    def attribute_identity(self, attribute_identity: "int") -> None:
        """Sets the attribute_identity of this GrantaServerApiDataExportExportFailuresDatumReference.

        Parameters
        ----------
        attribute_identity: int
            The attribute_identity of this GrantaServerApiDataExportExportFailuresDatumReference.
        """
        # Field is not nullable
        if attribute_identity is None:
            raise ValueError(
                "Invalid value for 'attribute_identity', must not be 'None'"
            )
        # Field is required
        if attribute_identity is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'attribute_identity', must not be 'Unset'"
            )
        self._attribute_identity = attribute_identity

    @property
    def attribute_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the attribute_guid of this GrantaServerApiDataExportExportFailuresDatumReference.

        Returns
        -------
        Union[str, None, Unset_Type]
            The attribute_guid of this GrantaServerApiDataExportExportFailuresDatumReference.
        """
        return self._attribute_guid

    @attribute_guid.setter
    def attribute_guid(self, attribute_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the attribute_guid of this GrantaServerApiDataExportExportFailuresDatumReference.

        Parameters
        ----------
        attribute_guid: Union[str, None, Unset_Type]
            The attribute_guid of this GrantaServerApiDataExportExportFailuresDatumReference.
        """
        self._attribute_guid = attribute_guid

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
        if not isinstance(other, GrantaServerApiDataExportExportFailuresDatumReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
