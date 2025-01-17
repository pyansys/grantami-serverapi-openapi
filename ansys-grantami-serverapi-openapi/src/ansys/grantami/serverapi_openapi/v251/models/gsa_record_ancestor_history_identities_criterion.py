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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from ansys.grantami.serverapi_openapi.models.gsa_criterion import GsaCriterion  # noqa: F401
from ansys.grantami.serverapi_openapi.models.gsa_criterion_type import GsaCriterionType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaRecordAncestorHistoryIdentitiesCriterion(GsaCriterion):
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
        "type": "GsaCriterionType",
        "ancestor_history_identities": "list[int]",
        "database_key": "str",
    }

    attribute_map: dict[str, str] = {
        "type": "type",
        "ancestor_history_identities": "ancestorHistoryIdentities",
        "database_key": "databaseKey",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        type: "GsaCriterionType" = GsaCriterionType.RECORDANCESTORIDENTITIES,
        ancestor_history_identities: "Union[list[int], None, Unset_Type]" = Unset,
        database_key: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaRecordAncestorHistoryIdentitiesCriterion - a model defined in Swagger

        Parameters
        ----------
        type: GsaCriterionType
        ancestor_history_identities: list[int], optional
        database_key: str, optional
        """
        super().__init__(type=type)
        self._ancestor_history_identities: Union[list[int], None, Unset_Type] = Unset
        self._database_key: Union[str, None, Unset_Type] = Unset

        if ancestor_history_identities is not Unset:
            self.ancestor_history_identities = ancestor_history_identities
        if database_key is not Unset:
            self.database_key = database_key

    @property
    def ancestor_history_identities(self) -> "Union[list[int], None, Unset_Type]":
        """Gets the ancestor_history_identities of this GsaRecordAncestorHistoryIdentitiesCriterion.

        Returns
        -------
        Union[list[int], None, Unset_Type]
            The ancestor_history_identities of this GsaRecordAncestorHistoryIdentitiesCriterion.
        """
        return self._ancestor_history_identities

    @ancestor_history_identities.setter
    def ancestor_history_identities(
        self, ancestor_history_identities: "Union[list[int], None, Unset_Type]"
    ) -> None:
        """Sets the ancestor_history_identities of this GsaRecordAncestorHistoryIdentitiesCriterion.

        Parameters
        ----------
        ancestor_history_identities: Union[list[int], None, Unset_Type]
            The ancestor_history_identities of this GsaRecordAncestorHistoryIdentitiesCriterion.
        """
        self._ancestor_history_identities = ancestor_history_identities

    @property
    def database_key(self) -> "Union[str, None, Unset_Type]":
        """Gets the database_key of this GsaRecordAncestorHistoryIdentitiesCriterion.

        Returns
        -------
        Union[str, None, Unset_Type]
            The database_key of this GsaRecordAncestorHistoryIdentitiesCriterion.
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key: "Union[str, None, Unset_Type]") -> None:
        """Sets the database_key of this GsaRecordAncestorHistoryIdentitiesCriterion.

        Parameters
        ----------
        database_key: Union[str, None, Unset_Type]
            The database_key of this GsaRecordAncestorHistoryIdentitiesCriterion.
        """
        self._database_key = database_key

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
        if not isinstance(other, GsaRecordAncestorHistoryIdentitiesCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
