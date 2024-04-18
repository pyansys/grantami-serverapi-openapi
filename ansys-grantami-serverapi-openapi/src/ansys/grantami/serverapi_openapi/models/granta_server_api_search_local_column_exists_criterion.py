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

from ansys.grantami.serverapi_openapi.models.granta_server_api_search_local_column_criterion import (  # noqa: F401
    GrantaServerApiSearchLocalColumnCriterion,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSearchLocalColumnExistsCriterion(
    GrantaServerApiSearchLocalColumnCriterion
):
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
        "inner_criterion": "GrantaServerApiSearchDatumExistsCriterion",
        "guid": "str",
        "identity": "int",
        "local_column_criterion_type": "str",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "inner_criterion": "innerCriterion",
        "guid": "guid",
        "identity": "identity",
        "local_column_criterion_type": "localColumnCriterionType",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {
        "innerCriterion": "GrantaServerApiSearchDatumExistsCriterion",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        inner_criterion: "GrantaServerApiSearchDatumExistsCriterion",
        guid: "Union[str, None, Unset_Type]" = Unset,
        identity: "Union[int, None, Unset_Type]" = Unset,
        local_column_criterion_type: "str" = "exists",
        type: "str" = "localColumn",
    ) -> None:
        """GrantaServerApiSearchLocalColumnExistsCriterion - a model defined in Swagger

        Parameters
        ----------
        inner_criterion: GrantaServerApiSearchDatumExistsCriterion
        guid: str, optional
        identity: int, optional
        local_column_criterion_type: str
        type: str
        """
        super().__init__(guid=guid, identity=identity, type=type)
        self._inner_criterion: GrantaServerApiSearchDatumExistsCriterion
        self._local_column_criterion_type: str

        self.inner_criterion = inner_criterion
        self.local_column_criterion_type = local_column_criterion_type

    @property
    def inner_criterion(self) -> "GrantaServerApiSearchDatumExistsCriterion":
        """Gets the inner_criterion of this GrantaServerApiSearchLocalColumnExistsCriterion.

        Returns
        -------
        GrantaServerApiSearchDatumExistsCriterion
            The inner_criterion of this GrantaServerApiSearchLocalColumnExistsCriterion.
        """
        return self._inner_criterion

    @inner_criterion.setter
    def inner_criterion(
        self, inner_criterion: "GrantaServerApiSearchDatumExistsCriterion"
    ) -> None:
        """Sets the inner_criterion of this GrantaServerApiSearchLocalColumnExistsCriterion.

        Parameters
        ----------
        inner_criterion: GrantaServerApiSearchDatumExistsCriterion
            The inner_criterion of this GrantaServerApiSearchLocalColumnExistsCriterion.
        """
        # Field is not nullable
        if inner_criterion is None:
            raise ValueError("Invalid value for 'inner_criterion', must not be 'None'")
        # Field is required
        if inner_criterion is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'inner_criterion', must not be 'Unset'")
        self._inner_criterion = inner_criterion

    @property
    def local_column_criterion_type(self) -> "str":
        """Gets the local_column_criterion_type of this GrantaServerApiSearchLocalColumnExistsCriterion.

        Returns
        -------
        str
            The local_column_criterion_type of this GrantaServerApiSearchLocalColumnExistsCriterion.
        """
        return self._local_column_criterion_type

    @local_column_criterion_type.setter
    def local_column_criterion_type(self, local_column_criterion_type: "str") -> None:
        """Sets the local_column_criterion_type of this GrantaServerApiSearchLocalColumnExistsCriterion.

        Parameters
        ----------
        local_column_criterion_type: str
            The local_column_criterion_type of this GrantaServerApiSearchLocalColumnExistsCriterion.
        """
        # Field is not nullable
        if local_column_criterion_type is None:
            raise ValueError(
                "Invalid value for 'local_column_criterion_type', must not be 'None'"
            )
        # Field is required
        if local_column_criterion_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'local_column_criterion_type', must not be 'Unset'"
            )
        self._local_column_criterion_type = local_column_criterion_type

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
        if not isinstance(other, GrantaServerApiSearchLocalColumnExistsCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
