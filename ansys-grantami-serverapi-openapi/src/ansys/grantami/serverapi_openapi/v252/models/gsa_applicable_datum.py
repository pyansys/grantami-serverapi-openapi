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

from ansys.grantami.serverapi_openapi.v252.models.gsa_datum import GsaDatum  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaApplicableDatum(GsaDatum):
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
        "datum_type": "GsaDatumType",
        "not_applicable": "str",
    }

    attribute_map: dict[str, str] = {
        "datum_type": "datumType",
        "not_applicable": "notApplicable",
    }

    subtype_mapping: dict[str, str] = {
        "datumType": "GsaDatumType",
    }

    discriminator_value_class_map = {
        "integer".lower(): "#/components/schemas/GsaIntegerDatum",
        "logical".lower(): "#/components/schemas/GsaLogicalDatum",
        "shortText".lower(): "#/components/schemas/GsaShortTextDatum",
        "longText".lower(): "#/components/schemas/GsaLongTextDatum",
        "hyperlink".lower(): "#/components/schemas/GsaHyperlinkDatum",
        "dateTime".lower(): "#/components/schemas/GsaDateTimeDatum",
        "discrete".lower(): "#/components/schemas/GsaDiscreteDatum",
        "range".lower(): "#/components/schemas/GsaRangeDatum",
        "point".lower(): "#/components/schemas/GsaPointDatum",
        "picture".lower(): "#/components/schemas/GsaPictureDatum",
        "file".lower(): "#/components/schemas/GsaFileDatum",
        "floatFunctional".lower(): "#/components/schemas/GsaFloatFunctionalDatum",
        "discreteFunctional".lower(): "#/components/schemas/GsaDiscreteFunctionalDatum",
        "tabular".lower(): "#/components/schemas/GsaTabularDatum",
    }

    discriminator: Optional[str] = "datum_type"

    def __init__(
        self,
        *,
        datum_type: "GsaDatumType",
        not_applicable: "str" = "applicable",
    ) -> None:
        """GsaApplicableDatum - a model defined in Swagger

        Parameters
        ----------
        datum_type: GsaDatumType
        not_applicable: str
        """
        super().__init__(not_applicable=not_applicable)
        self._datum_type: GsaDatumType

        self.datum_type = datum_type

    @property
    def datum_type(self) -> "GsaDatumType":
        """Gets the datum_type of this GsaApplicableDatum.

        Returns
        -------
        GsaDatumType
            The datum_type of this GsaApplicableDatum.
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type: "GsaDatumType") -> None:
        """Sets the datum_type of this GsaApplicableDatum.

        Parameters
        ----------
        datum_type: GsaDatumType
            The datum_type of this GsaApplicableDatum.
        """
        # Field is not nullable
        if datum_type is None:
            raise ValueError("Invalid value for 'datum_type', must not be 'None'")
        # Field is required
        if datum_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'datum_type', must not be 'Unset'")
        self._datum_type = datum_type

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
        if not isinstance(other, GsaApplicableDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
