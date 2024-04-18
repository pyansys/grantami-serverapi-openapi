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

from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_datums_link_datum import (  # noqa: F401
    GrantaServerApiDataExportDatumsLinkDatum,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiDataExportDatumsTabularDatum(GrantaServerApiDataExportDatumsLinkDatum):
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
        "attribute_guid": "str",
        "attribute_identity": "int",
        "attribute_name": "str",
        "datum_type": "str",
        "link_datum_type": "str",
        "meta_datums": "list[GrantaServerApiDataExportDatumsDatum]",
        "not_applicable": "str",
        "summary_row": "list[GrantaServerApiDataExportDatumsRollupRollupDatum]",
        "tabular_rows": "list[GrantaServerApiDataExportDatumsTabularRow]",
    }

    attribute_map: Dict[str, str] = {
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "attribute_name": "attributeName",
        "datum_type": "datumType",
        "link_datum_type": "linkDatumType",
        "meta_datums": "metaDatums",
        "not_applicable": "notApplicable",
        "summary_row": "summaryRow",
        "tabular_rows": "tabularRows",
    }

    subtype_mapping: Dict[str, str] = {
        "tabularRows": "GrantaServerApiDataExportDatumsTabularRow",
        "summaryRow": "GrantaServerApiDataExportDatumsRollupRollupDatum",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_guid: "Union[str, Unset_Type]" = Unset,
        attribute_identity: "Union[int, Unset_Type]" = Unset,
        attribute_name: "Union[str, None, Unset_Type]" = Unset,
        datum_type: "str" = "link",
        link_datum_type: "str" = "tabular",
        meta_datums: "Union[List[GrantaServerApiDataExportDatumsDatum], None, Unset_Type]" = Unset,
        not_applicable: "str" = "applicable",
        summary_row: "Union[List[GrantaServerApiDataExportDatumsRollupRollupDatum], None, Unset_Type]" = Unset,
        tabular_rows: "Union[List[GrantaServerApiDataExportDatumsTabularRow], None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiDataExportDatumsTabularDatum - a model defined in Swagger

        Parameters
        ----------
        attribute_guid: str, optional
        attribute_identity: int, optional
        attribute_name: str, optional
        datum_type: str
        link_datum_type: str
        meta_datums: List[GrantaServerApiDataExportDatumsDatum], optional
        not_applicable: str
        summary_row: List[GrantaServerApiDataExportDatumsRollupRollupDatum], optional
        tabular_rows: List[GrantaServerApiDataExportDatumsTabularRow], optional
        """
        super().__init__(
            attribute_guid=attribute_guid,
            attribute_identity=attribute_identity,
            datum_type=datum_type,
            meta_datums=meta_datums,
            not_applicable=not_applicable,
        )
        self._attribute_name: Union[str, None, Unset_Type] = Unset
        self._tabular_rows: Union[
            List[GrantaServerApiDataExportDatumsTabularRow], None, Unset_Type
        ] = Unset
        self._summary_row: Union[
            List[GrantaServerApiDataExportDatumsRollupRollupDatum], None, Unset_Type
        ] = Unset
        self._link_datum_type: str

        if attribute_name is not Unset:
            self.attribute_name = attribute_name
        if tabular_rows is not Unset:
            self.tabular_rows = tabular_rows
        if summary_row is not Unset:
            self.summary_row = summary_row
        self.link_datum_type = link_datum_type

    @property
    def attribute_name(self) -> "Union[str, None, Unset_Type]":
        """Gets the attribute_name of this GrantaServerApiDataExportDatumsTabularDatum.

        Returns
        -------
        Union[str, None, Unset_Type]
            The attribute_name of this GrantaServerApiDataExportDatumsTabularDatum.
        """
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, attribute_name: "Union[str, None, Unset_Type]") -> None:
        """Sets the attribute_name of this GrantaServerApiDataExportDatumsTabularDatum.

        Parameters
        ----------
        attribute_name: Union[str, None, Unset_Type]
            The attribute_name of this GrantaServerApiDataExportDatumsTabularDatum.
        """
        self._attribute_name = attribute_name

    @property
    def tabular_rows(
        self,
    ) -> "Union[List[GrantaServerApiDataExportDatumsTabularRow], None, Unset_Type]":
        """Gets the tabular_rows of this GrantaServerApiDataExportDatumsTabularDatum.

        Returns
        -------
        Union[List[GrantaServerApiDataExportDatumsTabularRow], None, Unset_Type]
            The tabular_rows of this GrantaServerApiDataExportDatumsTabularDatum.
        """
        return self._tabular_rows

    @tabular_rows.setter
    def tabular_rows(
        self,
        tabular_rows: "Union[List[GrantaServerApiDataExportDatumsTabularRow], None, Unset_Type]",
    ) -> None:
        """Sets the tabular_rows of this GrantaServerApiDataExportDatumsTabularDatum.

        Parameters
        ----------
        tabular_rows: Union[List[GrantaServerApiDataExportDatumsTabularRow], None, Unset_Type]
            The tabular_rows of this GrantaServerApiDataExportDatumsTabularDatum.
        """
        self._tabular_rows = tabular_rows

    @property
    def summary_row(
        self,
    ) -> "Union[List[GrantaServerApiDataExportDatumsRollupRollupDatum], None, Unset_Type]":
        """Gets the summary_row of this GrantaServerApiDataExportDatumsTabularDatum.

        Returns
        -------
        Union[List[GrantaServerApiDataExportDatumsRollupRollupDatum], None, Unset_Type]
            The summary_row of this GrantaServerApiDataExportDatumsTabularDatum.
        """
        return self._summary_row

    @summary_row.setter
    def summary_row(
        self,
        summary_row: "Union[List[GrantaServerApiDataExportDatumsRollupRollupDatum], None, Unset_Type]",
    ) -> None:
        """Sets the summary_row of this GrantaServerApiDataExportDatumsTabularDatum.

        Parameters
        ----------
        summary_row: Union[List[GrantaServerApiDataExportDatumsRollupRollupDatum], None, Unset_Type]
            The summary_row of this GrantaServerApiDataExportDatumsTabularDatum.
        """
        self._summary_row = summary_row

    @property
    def link_datum_type(self) -> "str":
        """Gets the link_datum_type of this GrantaServerApiDataExportDatumsTabularDatum.

        Returns
        -------
        str
            The link_datum_type of this GrantaServerApiDataExportDatumsTabularDatum.
        """
        return self._link_datum_type

    @link_datum_type.setter
    def link_datum_type(self, link_datum_type: "str") -> None:
        """Sets the link_datum_type of this GrantaServerApiDataExportDatumsTabularDatum.

        Parameters
        ----------
        link_datum_type: str
            The link_datum_type of this GrantaServerApiDataExportDatumsTabularDatum.
        """
        # Field is not nullable
        if link_datum_type is None:
            raise ValueError("Invalid value for 'link_datum_type', must not be 'None'")
        # Field is required
        if link_datum_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'link_datum_type', must not be 'Unset'")
        self._link_datum_type = link_datum_type

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
        if not isinstance(other, GrantaServerApiDataExportDatumsTabularDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
