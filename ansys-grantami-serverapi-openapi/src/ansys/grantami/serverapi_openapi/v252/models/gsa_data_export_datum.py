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

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaDataExportDatum(ModelBase):
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
        "attribute_guid": "str",
        "attribute_identity": "int",
        "not_applicable": "str",
        "meta_datums": "list[GsaDataExportDatum]",
    }

    attribute_map: dict[str, str] = {
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "not_applicable": "notApplicable",
        "meta_datums": "metaDatums",
    }

    subtype_mapping: dict[str, str] = {
        "metaDatums": "GsaDataExportDatum",
    }

    discriminator_value_class_map = {
        "notApplicable".lower(): "#/components/schemas/GsaDataExportNotApplicableDatum",
        "applicable".lower(): "#/components/schemas/GsaDataExportApplicableDatum",
        "unknown".lower(): "#/components/schemas/GsaDataExportUnknownDatum",
    }

    discriminator: Optional[str] = "notApplicable"

    def __init__(
        self,
        *,
        attribute_guid: "str",
        attribute_identity: "int",
        not_applicable: "str",
        meta_datums: "Union[list[GsaDataExportDatum], None, Unset_Type]" = Unset,
    ) -> None:
        """GsaDataExportDatum - a model defined in Swagger

        Parameters
        ----------
        attribute_guid: str
        attribute_identity: int
        not_applicable: str
        meta_datums: list[GsaDataExportDatum], optional
        """
        self._attribute_identity: int
        self._attribute_guid: str
        self._meta_datums: Union[list[GsaDataExportDatum], None, Unset_Type] = Unset
        self._not_applicable: str

        self.attribute_identity = attribute_identity
        self.attribute_guid = attribute_guid
        if meta_datums is not Unset:
            self.meta_datums = meta_datums
        self.not_applicable = not_applicable

    @property
    def attribute_identity(self) -> "int":
        """Gets the attribute_identity of this GsaDataExportDatum.

        Returns
        -------
        int
            The attribute_identity of this GsaDataExportDatum.
        """
        return self._attribute_identity

    @attribute_identity.setter
    def attribute_identity(self, attribute_identity: "int") -> None:
        """Sets the attribute_identity of this GsaDataExportDatum.

        Parameters
        ----------
        attribute_identity: int
            The attribute_identity of this GsaDataExportDatum.
        """
        # Field is not nullable
        if attribute_identity is None:
            raise ValueError("Invalid value for 'attribute_identity', must not be 'None'")
        # Field is required
        if attribute_identity is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'attribute_identity', must not be 'Unset'")
        self._attribute_identity = attribute_identity

    @property
    def attribute_guid(self) -> "str":
        """Gets the attribute_guid of this GsaDataExportDatum.

        Returns
        -------
        str
            The attribute_guid of this GsaDataExportDatum.
        """
        return self._attribute_guid

    @attribute_guid.setter
    def attribute_guid(self, attribute_guid: "str") -> None:
        """Sets the attribute_guid of this GsaDataExportDatum.

        Parameters
        ----------
        attribute_guid: str
            The attribute_guid of this GsaDataExportDatum.
        """
        # Field is not nullable
        if attribute_guid is None:
            raise ValueError("Invalid value for 'attribute_guid', must not be 'None'")
        # Field is required
        if attribute_guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'attribute_guid', must not be 'Unset'")
        self._attribute_guid = attribute_guid

    @property
    def meta_datums(self) -> "Union[list[GsaDataExportDatum], None, Unset_Type]":
        """Gets the meta_datums of this GsaDataExportDatum.

        Returns
        -------
        Union[list[GsaDataExportDatum], None, Unset_Type]
            The meta_datums of this GsaDataExportDatum.
        """
        return self._meta_datums

    @meta_datums.setter
    def meta_datums(self, meta_datums: "Union[list[GsaDataExportDatum], None, Unset_Type]") -> None:
        """Sets the meta_datums of this GsaDataExportDatum.

        Parameters
        ----------
        meta_datums: Union[list[GsaDataExportDatum], None, Unset_Type]
            The meta_datums of this GsaDataExportDatum.
        """
        self._meta_datums = meta_datums

    @property
    def not_applicable(self) -> "str":
        """Gets the not_applicable of this GsaDataExportDatum.

        Returns
        -------
        str
            The not_applicable of this GsaDataExportDatum.
        """
        return self._not_applicable

    @not_applicable.setter
    def not_applicable(self, not_applicable: "str") -> None:
        """Sets the not_applicable of this GsaDataExportDatum.

        Parameters
        ----------
        not_applicable: str
            The not_applicable of this GsaDataExportDatum.
        """
        # Field is not nullable
        if not_applicable is None:
            raise ValueError("Invalid value for 'not_applicable', must not be 'None'")
        # Field is required
        if not_applicable is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'not_applicable', must not be 'Unset'")
        self._not_applicable = not_applicable

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
        if not isinstance(other, GsaDataExportDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
