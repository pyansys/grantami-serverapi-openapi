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

from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_datums_applicable_datum import (  # noqa: F401
    GrantaServerApiDataExportDatumsApplicableDatum,
)

from . import ModelBase

if TYPE_CHECKING:
    from . import *


class GrantaServerApiDataExportDatumsRangeDatum(GrantaServerApiDataExportDatumsApplicableDatum):
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
        "datum_type": "str",
        "datum_value": "GrantaServerApiDataExportDatumsRange",
        "is_estimated": "bool",
        "meta_datums": "list[GrantaServerApiDataExportDatumsDatum]",
        "not_applicable": "str",
        "unit": "str",
    }

    attribute_map = {
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "datum_type": "datumType",
        "datum_value": "datumValue",
        "is_estimated": "isEstimated",
        "meta_datums": "metaDatums",
        "not_applicable": "notApplicable",
        "unit": "unit",
    }

    subtype_mapping = {
        "datumValue": "GrantaServerApiDataExportDatumsRange",
    }

    discriminator = None

    def __init__(
        self,
        *,
        attribute_guid: "Optional[str]" = None,
        attribute_identity: "Optional[int]" = None,
        datum_type: "str" = "range",
        datum_value: "Optional[GrantaServerApiDataExportDatumsRange]" = None,
        is_estimated: "Optional[bool]" = None,
        meta_datums: "Optional[List[GrantaServerApiDataExportDatumsDatum]]" = None,
        not_applicable: "str" = "applicable",
        unit: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiDataExportDatumsRangeDatum - a model defined in Swagger

        Parameters
        ----------
            attribute_guid: str, optional
            attribute_identity: int, optional
            datum_type: str
            datum_value: GrantaServerApiDataExportDatumsRange, optional
            is_estimated: bool, optional
            meta_datums: List[GrantaServerApiDataExportDatumsDatum], optional
            not_applicable: str
            unit: str, optional
        """
        super().__init__(
            attribute_guid=attribute_guid,
            attribute_identity=attribute_identity,
            meta_datums=meta_datums,
            not_applicable=not_applicable,
        )
        self._datum_type = None
        self._datum_value = None
        self._is_estimated = None
        self._unit = None

        self.datum_type = datum_type
        if datum_value is not None:
            self.datum_value = datum_value
        if is_estimated is not None:
            self.is_estimated = is_estimated
        if unit is not None:
            self.unit = unit

    @property
    def datum_type(self) -> "str":
        """Gets the datum_type of this GrantaServerApiDataExportDatumsRangeDatum.

        Returns
        -------
        str
            The datum_type of this GrantaServerApiDataExportDatumsRangeDatum.
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type: "str") -> None:
        """Sets the datum_type of this GrantaServerApiDataExportDatumsRangeDatum.

        Parameters
        ----------
        datum_type: str
            The datum_type of this GrantaServerApiDataExportDatumsRangeDatum.
        """
        if datum_type is None:
            raise ValueError("Invalid value for 'datum_type', must not be 'None'")
        self._datum_type = datum_type

    @property
    def datum_value(self) -> "GrantaServerApiDataExportDatumsRange":
        """Gets the datum_value of this GrantaServerApiDataExportDatumsRangeDatum.

        Returns
        -------
        GrantaServerApiDataExportDatumsRange
            The datum_value of this GrantaServerApiDataExportDatumsRangeDatum.
        """
        return self._datum_value

    @datum_value.setter
    def datum_value(self, datum_value: "GrantaServerApiDataExportDatumsRange") -> None:
        """Sets the datum_value of this GrantaServerApiDataExportDatumsRangeDatum.

        Parameters
        ----------
        datum_value: GrantaServerApiDataExportDatumsRange
            The datum_value of this GrantaServerApiDataExportDatumsRangeDatum.
        """
        self._datum_value = datum_value

    @property
    def is_estimated(self) -> "bool":
        """Gets the is_estimated of this GrantaServerApiDataExportDatumsRangeDatum.

        Returns
        -------
        bool
            The is_estimated of this GrantaServerApiDataExportDatumsRangeDatum.
        """
        return self._is_estimated

    @is_estimated.setter
    def is_estimated(self, is_estimated: "bool") -> None:
        """Sets the is_estimated of this GrantaServerApiDataExportDatumsRangeDatum.

        Parameters
        ----------
        is_estimated: bool
            The is_estimated of this GrantaServerApiDataExportDatumsRangeDatum.
        """
        self._is_estimated = is_estimated

    @property
    def unit(self) -> "str":
        """Gets the unit of this GrantaServerApiDataExportDatumsRangeDatum.

        Returns
        -------
        str
            The unit of this GrantaServerApiDataExportDatumsRangeDatum.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "str") -> None:
        """Sets the unit of this GrantaServerApiDataExportDatumsRangeDatum.

        Parameters
        ----------
        unit: str
            The unit of this GrantaServerApiDataExportDatumsRangeDatum.
        """
        self._unit = unit

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
        if not isinstance(other, GrantaServerApiDataExportDatumsRangeDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
