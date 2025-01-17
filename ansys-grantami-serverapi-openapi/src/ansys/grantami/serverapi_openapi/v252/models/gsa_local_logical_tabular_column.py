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

from ansys.grantami.serverapi_openapi.v252.models.gsa_tabular_column import (  # noqa: F401
    GsaTabularColumn,
)
from ansys.grantami.serverapi_openapi.v252.models.gsa_tabular_column_dto_type import (
    GsaTabularColumnDtoType,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaLocalLogicalTabularColumn(GsaTabularColumn):
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
        "column_type": "GsaTabularColumnDtoType",
        "default_threshold_type": "GsaAttributeThresholdType",
        "display_names": "dict(str, str)",
        "guid": "str",
        "name": "str",
        "roll_up_type": "GsaTabularColumnRollUpType",
        "show_as_link": "bool",
        "summary_row_enabled": "bool",
        "summary_row_roll_up_type": "GsaTabularColumnRollUpType",
        "summary_row_text": "str",
    }

    attribute_map: dict[str, str] = {
        "column_type": "columnType",
        "default_threshold_type": "defaultThresholdType",
        "display_names": "displayNames",
        "guid": "guid",
        "name": "name",
        "roll_up_type": "rollUpType",
        "show_as_link": "showAsLink",
        "summary_row_enabled": "summaryRowEnabled",
        "summary_row_roll_up_type": "summaryRowRollUpType",
        "summary_row_text": "summaryRowText",
    }

    subtype_mapping: dict[str, str] = {
        "defaultThresholdType": "GsaAttributeThresholdType",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        column_type: "GsaTabularColumnDtoType" = GsaTabularColumnDtoType.LOCALLOGICAL,
        default_threshold_type: "GsaAttributeThresholdType",
        display_names: "dict[str, str]",
        guid: "str",
        name: "str",
        roll_up_type: "GsaTabularColumnRollUpType",
        show_as_link: "bool",
        summary_row_enabled: "bool",
        summary_row_roll_up_type: "GsaTabularColumnRollUpType",
        summary_row_text: "str",
    ) -> None:
        """GsaLocalLogicalTabularColumn - a model defined in Swagger

        Parameters
        ----------
        column_type: GsaTabularColumnDtoType
        default_threshold_type: GsaAttributeThresholdType
        display_names: dict[str, str]
        guid: str
        name: str
        roll_up_type: GsaTabularColumnRollUpType
        show_as_link: bool
        summary_row_enabled: bool
        summary_row_roll_up_type: GsaTabularColumnRollUpType
        summary_row_text: str
        """
        super().__init__(
            column_type=column_type,
            display_names=display_names,
            guid=guid,
            name=name,
            roll_up_type=roll_up_type,
            show_as_link=show_as_link,
            summary_row_enabled=summary_row_enabled,
            summary_row_roll_up_type=summary_row_roll_up_type,
            summary_row_text=summary_row_text,
        )
        self._default_threshold_type: GsaAttributeThresholdType

        self.default_threshold_type = default_threshold_type

    @property
    def default_threshold_type(self) -> "GsaAttributeThresholdType":
        """Gets the default_threshold_type of this GsaLocalLogicalTabularColumn.

        Returns
        -------
        GsaAttributeThresholdType
            The default_threshold_type of this GsaLocalLogicalTabularColumn.
        """
        return self._default_threshold_type

    @default_threshold_type.setter
    def default_threshold_type(self, default_threshold_type: "GsaAttributeThresholdType") -> None:
        """Sets the default_threshold_type of this GsaLocalLogicalTabularColumn.

        Parameters
        ----------
        default_threshold_type: GsaAttributeThresholdType
            The default_threshold_type of this GsaLocalLogicalTabularColumn.
        """
        # Field is not nullable
        if default_threshold_type is None:
            raise ValueError("Invalid value for 'default_threshold_type', must not be 'None'")
        # Field is required
        if default_threshold_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'default_threshold_type', must not be 'Unset'")
        self._default_threshold_type = default_threshold_type

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
        if not isinstance(other, GsaLocalLogicalTabularColumn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
