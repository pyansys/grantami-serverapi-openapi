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

from ansys.grantami.serverapi_openapi.models.gsa_attribute_type import GsaAttributeType
from ansys.grantami.serverapi_openapi.models.gsa_data_export_applicable_datum import (  # noqa: F401
    GsaDataExportApplicableDatum,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaDataExportLinkDatum(GsaDataExportApplicableDatum):
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
    discriminator_class_map: dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "datum_type": "GsaAttributeType",
        "link_datum_type": "str",
        "not_applicable": "str",
        "attribute_guid": "str",
        "attribute_identity": "int",
        "meta_datums": "list[GsaDataExportDatum]",
    }

    attribute_map: dict[str, str] = {
        "datum_type": "datumType",
        "link_datum_type": "linkDatumType",
        "not_applicable": "notApplicable",
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "meta_datums": "metaDatums",
    }

    subtype_mapping: dict[str, str] = {}

    discriminator_value_class_map = {
        "linkGroup".lower(): "#/components/schemas/GsaDataExportLinkedRecordsDatum",
        "tabular".lower(): "#/components/schemas/GsaDataExportTabularDatum",
    }

    discriminator: Optional[str] = "link_datum_type"

    def __init__(
        self,
        *,
        datum_type: "GsaAttributeType" = GsaAttributeType.LINK,
        link_datum_type: "str",
        not_applicable: "str" = "applicable",
        attribute_guid: "Union[str, Unset_Type]" = Unset,
        attribute_identity: "Union[int, Unset_Type]" = Unset,
        meta_datums: "Union[list[GsaDataExportDatum], None, Unset_Type]" = Unset,
    ) -> None:
        """GsaDataExportLinkDatum - a model defined in Swagger

        Parameters
        ----------
        datum_type: GsaAttributeType
        link_datum_type: str
        not_applicable: str
        attribute_guid: str, optional
        attribute_identity: int, optional
        meta_datums: list[GsaDataExportDatum], optional
        """
        super().__init__(
            datum_type=datum_type,
            not_applicable=not_applicable,
            attribute_guid=attribute_guid,
            attribute_identity=attribute_identity,
            meta_datums=meta_datums,
        )
        self._link_datum_type: str

        self.link_datum_type = link_datum_type

    @property
    def link_datum_type(self) -> "str":
        """Gets the link_datum_type of this GsaDataExportLinkDatum.

        Returns
        -------
        str
            The link_datum_type of this GsaDataExportLinkDatum.
        """
        return self._link_datum_type

    @link_datum_type.setter
    def link_datum_type(self, link_datum_type: "str") -> None:
        """Sets the link_datum_type of this GsaDataExportLinkDatum.

        Parameters
        ----------
        link_datum_type: str
            The link_datum_type of this GsaDataExportLinkDatum.
        """
        # Field is required
        if link_datum_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'link_datum_type', must not be 'Unset'")
        self._link_datum_type = link_datum_type

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
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
        if not isinstance(other, GsaDataExportLinkDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
