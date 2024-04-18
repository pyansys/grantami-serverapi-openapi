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
from typing import (
    TYPE_CHECKING,
    Any,
    BinaryIO,
    Dict,
    List,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_datums_datum import (
    GrantaServerApiDataExportDatumsDatum,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiDataExportDatumsApplicableDatum(
    GrantaServerApiDataExportDatumsDatum
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
    discriminator_class_map: Dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: Dict[str, str] = {
        "attribute_guid": "str",
        "attribute_identity": "int",
        "meta_datums": "list[GrantaServerApiDataExportDatumsDatum]",
        "not_applicable": "str",
    }

    attribute_map: Dict[str, str] = {
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "meta_datums": "metaDatums",
        "not_applicable": "notApplicable",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator_value_class_map = {
        "logical".lower(): "#/components/schemas/GrantaServerApiDataExportDatumsBooleanDatum",
        "dateTime".lower(): "#/components/schemas/GrantaServerApiDataExportDatumsDateTimeDatum",
        "discrete".lower(): "#/components/schemas/GrantaServerApiDataExportDatumsDiscreteDatum",
        "file".lower(): "#/components/schemas/GrantaServerApiDataExportDatumsFileDatum",
        "floatFunctional".lower(): "#/components/schemas/GrantaServerApiDataExportDatumsFloatFunctionalDatum",
        "discreteFunctional".lower(): "#/components/schemas/GrantaServerApiDataExportDatumsDiscreteFunctionalDatum",
        "hyperlink".lower(): "#/components/schemas/GrantaServerApiDataExportDatumsHyperlinkDatum",
        "link".lower(): "#/components/schemas/GrantaServerApiDataExportDatumsLinkDatum",
        "longText".lower(): "#/components/schemas/GrantaServerApiDataExportDatumsLongTextDatum",
        "integer".lower(): "#/components/schemas/GrantaServerApiDataExportDatumsNumericDatum",
        "picture".lower(): "#/components/schemas/GrantaServerApiDataExportDatumsPictureDatum",
        "point".lower(): "#/components/schemas/GrantaServerApiDataExportDatumsPointDatum",
        "range".lower(): "#/components/schemas/GrantaServerApiDataExportDatumsRangeDatum",
        "shortText".lower(): "#/components/schemas/GrantaServerApiDataExportDatumsShortTextDatum",
    }

    discriminator: Optional[str] = "datum_type"

    def __init__(
        self,
        *,
        attribute_guid: "Union[str, Unset_Type]" = Unset,
        attribute_identity: "Union[int, Unset_Type]" = Unset,
        meta_datums: "Union[List[GrantaServerApiDataExportDatumsDatum], None, Unset_Type]" = Unset,
        not_applicable: "str" = "applicable",
    ) -> None:
        """GrantaServerApiDataExportDatumsApplicableDatum - a model defined in Swagger

        Parameters
        ----------
        attribute_guid: str, optional
        attribute_identity: int, optional
        meta_datums: List[GrantaServerApiDataExportDatumsDatum], optional
        not_applicable: str
        """
        super().__init__(
            attribute_guid=attribute_guid,
            attribute_identity=attribute_identity,
            meta_datums=meta_datums,
        )
        self._not_applicable: str

        self.not_applicable = not_applicable

    @property
    def not_applicable(self) -> "str":
        """Gets the not_applicable of this GrantaServerApiDataExportDatumsApplicableDatum.

        Returns
        -------
        str
            The not_applicable of this GrantaServerApiDataExportDatumsApplicableDatum.
        """
        return self._not_applicable

    @not_applicable.setter
    def not_applicable(self, not_applicable: "str") -> None:
        """Sets the not_applicable of this GrantaServerApiDataExportDatumsApplicableDatum.

        Parameters
        ----------
        not_applicable: str
            The not_applicable of this GrantaServerApiDataExportDatumsApplicableDatum.
        """
        # Field is not nullable
        if not_applicable is None:
            raise ValueError("Invalid value for 'not_applicable', must not be 'None'")
        # Field is required
        if not_applicable is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'not_applicable', must not be 'Unset'")
        self._not_applicable = not_applicable

    @classmethod
    def get_real_child_model(cls, data: Dict[str, str]) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[cls._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen,
        # so we have to extract it from the JSON reference
        return cls.discriminator_value_class_map[discriminator_value].rsplit("/", 1)[-1]

    @classmethod
    def _get_discriminator_field_name(cls) -> str:
        assert cls.discriminator
        name_tokens = cls.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiDataExportDatumsApplicableDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
