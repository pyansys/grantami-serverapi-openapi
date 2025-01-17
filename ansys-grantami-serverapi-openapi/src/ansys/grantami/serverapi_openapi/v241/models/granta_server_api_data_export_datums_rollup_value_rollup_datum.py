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

from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_datums_rollup_rollup_datum import (  # noqa: F401
    GrantaServerApiDataExportDatumsRollupRollupDatum,
)

from . import ModelBase

if TYPE_CHECKING:
    from . import *


class GrantaServerApiDataExportDatumsRollupValueRollupDatum(
    GrantaServerApiDataExportDatumsRollupRollupDatum
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
    swagger_types = {
        "attribute_guid": "str",
        "attribute_identity": "int",
        "database_key": "str",
        "roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "type": "str",
        "value": "object",
    }

    attribute_map = {
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "database_key": "databaseKey",
        "roll_up_type": "rollUpType",
        "type": "type",
        "value": "value",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        attribute_guid: "Optional[str]" = None,
        attribute_identity: "Optional[int]" = None,
        database_key: "Optional[str]" = None,
        roll_up_type: "Optional[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType]" = None,
        type: "str" = "valueRollup",
        value: "Optional[object]" = None,
    ) -> None:
        """GrantaServerApiDataExportDatumsRollupValueRollupDatum - a model defined in Swagger

        Parameters
        ----------
            attribute_guid: str, optional
            attribute_identity: int, optional
            database_key: str, optional
            roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, optional
            type: str
            value: object, optional
        """
        super().__init__(
            attribute_guid=attribute_guid,
            attribute_identity=attribute_identity,
            database_key=database_key,
            roll_up_type=roll_up_type,
        )
        self._value = None
        self._type = None

        if value is not None:
            self.value = value
        self.type = type

    @property
    def value(self) -> "object":
        """Gets the value of this GrantaServerApiDataExportDatumsRollupValueRollupDatum.

        Returns
        -------
        object
            The value of this GrantaServerApiDataExportDatumsRollupValueRollupDatum.
        """
        return self._value

    @value.setter
    def value(self, value: "object") -> None:
        """Sets the value of this GrantaServerApiDataExportDatumsRollupValueRollupDatum.

        Parameters
        ----------
        value: object
            The value of this GrantaServerApiDataExportDatumsRollupValueRollupDatum.
        """
        self._value = value

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiDataExportDatumsRollupValueRollupDatum.

        Returns
        -------
        str
            The type of this GrantaServerApiDataExportDatumsRollupValueRollupDatum.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiDataExportDatumsRollupValueRollupDatum.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiDataExportDatumsRollupValueRollupDatum.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

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
        if not isinstance(other, GrantaServerApiDataExportDatumsRollupValueRollupDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
