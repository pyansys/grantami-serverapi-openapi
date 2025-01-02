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


class GsaIntegrationDataExportRequest(ModelBase):
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
        "attribute_identities": "list[int]",
        "record_references": "list[GsaRecordReference]",
    }

    attribute_map: dict[str, str] = {
        "attribute_identities": "attributeIdentities",
        "record_references": "recordReferences",
    }

    subtype_mapping: dict[str, str] = {
        "recordReferences": "GsaRecordReference",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_identities: "list[int]",
        record_references: "list[GsaRecordReference]",
    ) -> None:
        """GsaIntegrationDataExportRequest - a model defined in Swagger

        Parameters
        ----------
        attribute_identities: list[int]
        record_references: list[GsaRecordReference]
        """
        self._record_references: list[GsaRecordReference]
        self._attribute_identities: list[int]

        self.record_references = record_references
        self.attribute_identities = attribute_identities

    @property
    def record_references(self) -> "list[GsaRecordReference]":
        """Gets the record_references of this GsaIntegrationDataExportRequest.
        A list of records to export. These are references to the underlying records in the source database

        Returns
        -------
        list[GsaRecordReference]
            The record_references of this GsaIntegrationDataExportRequest.
        """
        return self._record_references

    @record_references.setter
    def record_references(self, record_references: "list[GsaRecordReference]") -> None:
        """Sets the record_references of this GsaIntegrationDataExportRequest.
        A list of records to export. These are references to the underlying records in the source database

        Parameters
        ----------
        record_references: list[GsaRecordReference]
            The record_references of this GsaIntegrationDataExportRequest.
        """
        # Field is not nullable
        if record_references is None:
            raise ValueError("Invalid value for 'record_references', must not be 'None'")
        # Field is required
        if record_references is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'record_references', must not be 'Unset'")
        self._record_references = record_references

    @property
    def attribute_identities(self) -> "list[int]":
        """Gets the attribute_identities of this GsaIntegrationDataExportRequest.
        A list of attribute to export. These are the attribute identities from the integration schema.

        Returns
        -------
        list[int]
            The attribute_identities of this GsaIntegrationDataExportRequest.
        """
        return self._attribute_identities

    @attribute_identities.setter
    def attribute_identities(self, attribute_identities: "list[int]") -> None:
        """Sets the attribute_identities of this GsaIntegrationDataExportRequest.
        A list of attribute to export. These are the attribute identities from the integration schema.

        Parameters
        ----------
        attribute_identities: list[int]
            The attribute_identities of this GsaIntegrationDataExportRequest.
        """
        # Field is not nullable
        if attribute_identities is None:
            raise ValueError("Invalid value for 'attribute_identities', must not be 'None'")
        # Field is required
        if attribute_identities is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'attribute_identities', must not be 'Unset'")
        self._attribute_identities = attribute_identities

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
        if not isinstance(other, GsaIntegrationDataExportRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
