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
from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_attribute_to_export import (
    GrantaServerApiDataExportAttributeToExport,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiDataExportLinkAttributeToExport(
    GrantaServerApiDataExportAttributeToExport
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
        "attribute_type": "str",
        "attributes": "list[GrantaServerApiDataExportAttributeToExport]",
        "export_in_reversed_direction": "bool",
        "guid": "str",
        "identity": "int",
        "indirect_links_behavior": "GrantaServerApiIndirectLinks",
        "link_attribute_type": "GrantaServerApiLinkAttributeType",
        "linked_records_export_behavior": "GrantaServerApiDataExportLinkedRecordExportBehavior",
        "local_data": "list[GrantaServerApiDataExportSimpleAttributeToExport]",
        "record_properties": "list[GrantaServerApiRecordProperty]",
        "target_attribute_guid": "str",
        "target_database_guid": "str",
        "target_table_guid": "str",
    }

    attribute_map: Dict[str, str] = {
        "attribute_type": "attributeType",
        "attributes": "attributes",
        "export_in_reversed_direction": "exportInReversedDirection",
        "guid": "guid",
        "identity": "identity",
        "indirect_links_behavior": "indirectLinksBehavior",
        "link_attribute_type": "linkAttributeType",
        "linked_records_export_behavior": "linkedRecordsExportBehavior",
        "local_data": "localData",
        "record_properties": "recordProperties",
        "target_attribute_guid": "targetAttributeGuid",
        "target_database_guid": "targetDatabaseGuid",
        "target_table_guid": "targetTableGuid",
    }

    subtype_mapping: Dict[str, str] = {
        "localData": "GrantaServerApiDataExportSimpleAttributeToExport",
        "linkAttributeType": "GrantaServerApiLinkAttributeType",
        "recordProperties": "GrantaServerApiRecordProperty",
        "attributes": "GrantaServerApiDataExportAttributeToExport",
        "linkedRecordsExportBehavior": "GrantaServerApiDataExportLinkedRecordExportBehavior",
        "indirectLinksBehavior": "GrantaServerApiIndirectLinks",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_type: "str" = "link",
        attributes: "Union[List[GrantaServerApiDataExportAttributeToExport], None, Unset_Type]" = Unset,
        export_in_reversed_direction: "Union[bool, Unset_Type]" = Unset,
        guid: "Union[str, None, Unset_Type]" = Unset,
        identity: "Union[int, None, Unset_Type]" = Unset,
        indirect_links_behavior: "Union[GrantaServerApiIndirectLinks, Unset_Type]" = Unset,
        link_attribute_type: "Union[GrantaServerApiLinkAttributeType, Unset_Type]" = Unset,
        linked_records_export_behavior: "Union[GrantaServerApiDataExportLinkedRecordExportBehavior, Unset_Type]" = Unset,
        local_data: "Union[List[GrantaServerApiDataExportSimpleAttributeToExport], None, Unset_Type]" = Unset,
        record_properties: "Union[List[GrantaServerApiRecordProperty], None, Unset_Type]" = Unset,
        target_attribute_guid: "Union[str, None, Unset_Type]" = Unset,
        target_database_guid: "Union[str, None, Unset_Type]" = Unset,
        target_table_guid: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiDataExportLinkAttributeToExport - a model defined in Swagger

        Parameters
        ----------
        attribute_type: str
        attributes: List[GrantaServerApiDataExportAttributeToExport], optional
        export_in_reversed_direction: bool, optional
        guid: str, optional
        identity: int, optional
        indirect_links_behavior: GrantaServerApiIndirectLinks, optional
        link_attribute_type: GrantaServerApiLinkAttributeType, optional
        linked_records_export_behavior: GrantaServerApiDataExportLinkedRecordExportBehavior, optional
        local_data: List[GrantaServerApiDataExportSimpleAttributeToExport], optional
        record_properties: List[GrantaServerApiRecordProperty], optional
        target_attribute_guid: str, optional
        target_database_guid: str, optional
        target_table_guid: str, optional
        """
        super().__init__(guid=guid, identity=identity)
        self._local_data: Union[
            List[GrantaServerApiDataExportSimpleAttributeToExport], None, Unset_Type
        ] = Unset
        self._target_table_guid: Union[str, None, Unset_Type] = Unset
        self._target_database_guid: Union[str, None, Unset_Type] = Unset
        self._target_attribute_guid: Union[str, None, Unset_Type] = Unset
        self._attribute_type: str
        self._link_attribute_type: Union[
            GrantaServerApiLinkAttributeType, Unset_Type
        ] = Unset
        self._export_in_reversed_direction: Union[bool, Unset_Type] = Unset
        self._record_properties: Union[
            List[GrantaServerApiRecordProperty], None, Unset_Type
        ] = Unset
        self._attributes: Union[
            List[GrantaServerApiDataExportAttributeToExport], None, Unset_Type
        ] = Unset
        self._linked_records_export_behavior: Union[
            GrantaServerApiDataExportLinkedRecordExportBehavior, Unset_Type
        ] = Unset
        self._indirect_links_behavior: Union[
            GrantaServerApiIndirectLinks, Unset_Type
        ] = Unset

        if local_data is not Unset:
            self.local_data = local_data
        if target_table_guid is not Unset:
            self.target_table_guid = target_table_guid
        if target_database_guid is not Unset:
            self.target_database_guid = target_database_guid
        if target_attribute_guid is not Unset:
            self.target_attribute_guid = target_attribute_guid
        self.attribute_type = attribute_type
        if link_attribute_type is not Unset:
            self.link_attribute_type = link_attribute_type
        if export_in_reversed_direction is not Unset:
            self.export_in_reversed_direction = export_in_reversed_direction
        if record_properties is not Unset:
            self.record_properties = record_properties
        if attributes is not Unset:
            self.attributes = attributes
        if linked_records_export_behavior is not Unset:
            self.linked_records_export_behavior = linked_records_export_behavior
        if indirect_links_behavior is not Unset:
            self.indirect_links_behavior = indirect_links_behavior

    @property
    def local_data(
        self,
    ) -> "Union[List[GrantaServerApiDataExportSimpleAttributeToExport], None, Unset_Type]":
        """Gets the local_data of this GrantaServerApiDataExportLinkAttributeToExport.
        The local columns to export. Reuse the attribute object here - but the 'attribute id' is now the column id.

        Returns
        -------
        Union[List[GrantaServerApiDataExportSimpleAttributeToExport], None, Unset_Type]
            The local_data of this GrantaServerApiDataExportLinkAttributeToExport.
        """
        return self._local_data

    @local_data.setter
    def local_data(
        self,
        local_data: "Union[List[GrantaServerApiDataExportSimpleAttributeToExport], None, Unset_Type]",
    ) -> None:
        """Sets the local_data of this GrantaServerApiDataExportLinkAttributeToExport.
        The local columns to export. Reuse the attribute object here - but the 'attribute id' is now the column id.

        Parameters
        ----------
        local_data: Union[List[GrantaServerApiDataExportSimpleAttributeToExport], None, Unset_Type]
            The local_data of this GrantaServerApiDataExportLinkAttributeToExport.
        """
        self._local_data = local_data

    @property
    def target_table_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the target_table_guid of this GrantaServerApiDataExportLinkAttributeToExport.
        Table containing the linked records

        Returns
        -------
        Union[str, None, Unset_Type]
            The target_table_guid of this GrantaServerApiDataExportLinkAttributeToExport.
        """
        return self._target_table_guid

    @target_table_guid.setter
    def target_table_guid(
        self, target_table_guid: "Union[str, None, Unset_Type]"
    ) -> None:
        """Sets the target_table_guid of this GrantaServerApiDataExportLinkAttributeToExport.
        Table containing the linked records

        Parameters
        ----------
        target_table_guid: Union[str, None, Unset_Type]
            The target_table_guid of this GrantaServerApiDataExportLinkAttributeToExport.
        """
        self._target_table_guid = target_table_guid

    @property
    def target_database_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the target_database_guid of this GrantaServerApiDataExportLinkAttributeToExport.
        Database containing the linked records. For reverse cross database links, this is the database where the link is defined.  This is not required for cross-database link groups that don't have a target database.

        Returns
        -------
        Union[str, None, Unset_Type]
            The target_database_guid of this GrantaServerApiDataExportLinkAttributeToExport.
        """
        return self._target_database_guid

    @target_database_guid.setter
    def target_database_guid(
        self, target_database_guid: "Union[str, None, Unset_Type]"
    ) -> None:
        """Sets the target_database_guid of this GrantaServerApiDataExportLinkAttributeToExport.
        Database containing the linked records. For reverse cross database links, this is the database where the link is defined.  This is not required for cross-database link groups that don't have a target database.

        Parameters
        ----------
        target_database_guid: Union[str, None, Unset_Type]
            The target_database_guid of this GrantaServerApiDataExportLinkAttributeToExport.
        """
        self._target_database_guid = target_database_guid

    @property
    def target_attribute_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the target_attribute_guid of this GrantaServerApiDataExportLinkAttributeToExport.
        For tabular searching: this is the identifier of the short-text linking attribute.  Otherwise null.

        Returns
        -------
        Union[str, None, Unset_Type]
            The target_attribute_guid of this GrantaServerApiDataExportLinkAttributeToExport.
        """
        return self._target_attribute_guid

    @target_attribute_guid.setter
    def target_attribute_guid(
        self, target_attribute_guid: "Union[str, None, Unset_Type]"
    ) -> None:
        """Sets the target_attribute_guid of this GrantaServerApiDataExportLinkAttributeToExport.
        For tabular searching: this is the identifier of the short-text linking attribute.  Otherwise null.

        Parameters
        ----------
        target_attribute_guid: Union[str, None, Unset_Type]
            The target_attribute_guid of this GrantaServerApiDataExportLinkAttributeToExport.
        """
        self._target_attribute_guid = target_attribute_guid

    @property
    def attribute_type(self) -> "str":
        """Gets the attribute_type of this GrantaServerApiDataExportLinkAttributeToExport.

        Returns
        -------
        str
            The attribute_type of this GrantaServerApiDataExportLinkAttributeToExport.
        """
        return self._attribute_type

    @attribute_type.setter
    def attribute_type(self, attribute_type: "str") -> None:
        """Sets the attribute_type of this GrantaServerApiDataExportLinkAttributeToExport.

        Parameters
        ----------
        attribute_type: str
            The attribute_type of this GrantaServerApiDataExportLinkAttributeToExport.
        """
        # Field is not nullable
        if attribute_type is None:
            raise ValueError("Invalid value for 'attribute_type', must not be 'None'")
        # Field is required
        if attribute_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'attribute_type', must not be 'Unset'")
        self._attribute_type = attribute_type

    @property
    def link_attribute_type(
        self,
    ) -> "Union[GrantaServerApiLinkAttributeType, Unset_Type]":
        """Gets the link_attribute_type of this GrantaServerApiDataExportLinkAttributeToExport.

        Returns
        -------
        Union[GrantaServerApiLinkAttributeType, Unset_Type]
            The link_attribute_type of this GrantaServerApiDataExportLinkAttributeToExport.
        """
        return self._link_attribute_type

    @link_attribute_type.setter
    def link_attribute_type(
        self, link_attribute_type: "Union[GrantaServerApiLinkAttributeType, Unset_Type]"
    ) -> None:
        """Sets the link_attribute_type of this GrantaServerApiDataExportLinkAttributeToExport.

        Parameters
        ----------
        link_attribute_type: Union[GrantaServerApiLinkAttributeType, Unset_Type]
            The link_attribute_type of this GrantaServerApiDataExportLinkAttributeToExport.
        """
        # Field is not nullable
        if link_attribute_type is None:
            raise ValueError(
                "Invalid value for 'link_attribute_type', must not be 'None'"
            )
        self._link_attribute_type = link_attribute_type

    @property
    def export_in_reversed_direction(self) -> "Union[bool, Unset_Type]":
        """Gets the export_in_reversed_direction of this GrantaServerApiDataExportLinkAttributeToExport.

        Returns
        -------
        Union[bool, Unset_Type]
            The export_in_reversed_direction of this GrantaServerApiDataExportLinkAttributeToExport.
        """
        return self._export_in_reversed_direction

    @export_in_reversed_direction.setter
    def export_in_reversed_direction(
        self, export_in_reversed_direction: "Union[bool, Unset_Type]"
    ) -> None:
        """Sets the export_in_reversed_direction of this GrantaServerApiDataExportLinkAttributeToExport.

        Parameters
        ----------
        export_in_reversed_direction: Union[bool, Unset_Type]
            The export_in_reversed_direction of this GrantaServerApiDataExportLinkAttributeToExport.
        """
        # Field is not nullable
        if export_in_reversed_direction is None:
            raise ValueError(
                "Invalid value for 'export_in_reversed_direction', must not be 'None'"
            )
        self._export_in_reversed_direction = export_in_reversed_direction

    @property
    def record_properties(
        self,
    ) -> "Union[List[GrantaServerApiRecordProperty], None, Unset_Type]":
        """Gets the record_properties of this GrantaServerApiDataExportLinkAttributeToExport.
        The properties to export on any linked records.

        Returns
        -------
        Union[List[GrantaServerApiRecordProperty], None, Unset_Type]
            The record_properties of this GrantaServerApiDataExportLinkAttributeToExport.
        """
        return self._record_properties

    @record_properties.setter
    def record_properties(
        self,
        record_properties: "Union[List[GrantaServerApiRecordProperty], None, Unset_Type]",
    ) -> None:
        """Sets the record_properties of this GrantaServerApiDataExportLinkAttributeToExport.
        The properties to export on any linked records.

        Parameters
        ----------
        record_properties: Union[List[GrantaServerApiRecordProperty], None, Unset_Type]
            The record_properties of this GrantaServerApiDataExportLinkAttributeToExport.
        """
        self._record_properties = record_properties

    @property
    def attributes(
        self,
    ) -> "Union[List[GrantaServerApiDataExportAttributeToExport], None, Unset_Type]":
        """Gets the attributes of this GrantaServerApiDataExportLinkAttributeToExport.
        The attributes to export on any linked records.

        Returns
        -------
        Union[List[GrantaServerApiDataExportAttributeToExport], None, Unset_Type]
            The attributes of this GrantaServerApiDataExportLinkAttributeToExport.
        """
        return self._attributes

    @attributes.setter
    def attributes(
        self,
        attributes: "Union[List[GrantaServerApiDataExportAttributeToExport], None, Unset_Type]",
    ) -> None:
        """Sets the attributes of this GrantaServerApiDataExportLinkAttributeToExport.
        The attributes to export on any linked records.

        Parameters
        ----------
        attributes: Union[List[GrantaServerApiDataExportAttributeToExport], None, Unset_Type]
            The attributes of this GrantaServerApiDataExportLinkAttributeToExport.
        """
        self._attributes = attributes

    @property
    def linked_records_export_behavior(
        self,
    ) -> "Union[GrantaServerApiDataExportLinkedRecordExportBehavior, Unset_Type]":
        """Gets the linked_records_export_behavior of this GrantaServerApiDataExportLinkAttributeToExport.

        Returns
        -------
        Union[GrantaServerApiDataExportLinkedRecordExportBehavior, Unset_Type]
            The linked_records_export_behavior of this GrantaServerApiDataExportLinkAttributeToExport.
        """
        return self._linked_records_export_behavior

    @linked_records_export_behavior.setter
    def linked_records_export_behavior(
        self,
        linked_records_export_behavior: "Union[GrantaServerApiDataExportLinkedRecordExportBehavior, Unset_Type]",
    ) -> None:
        """Sets the linked_records_export_behavior of this GrantaServerApiDataExportLinkAttributeToExport.

        Parameters
        ----------
        linked_records_export_behavior: Union[GrantaServerApiDataExportLinkedRecordExportBehavior, Unset_Type]
            The linked_records_export_behavior of this GrantaServerApiDataExportLinkAttributeToExport.
        """
        # Field is not nullable
        if linked_records_export_behavior is None:
            raise ValueError(
                "Invalid value for 'linked_records_export_behavior', must not be 'None'"
            )
        self._linked_records_export_behavior = linked_records_export_behavior

    @property
    def indirect_links_behavior(
        self,
    ) -> "Union[GrantaServerApiIndirectLinks, Unset_Type]":
        """Gets the indirect_links_behavior of this GrantaServerApiDataExportLinkAttributeToExport.

        Returns
        -------
        Union[GrantaServerApiIndirectLinks, Unset_Type]
            The indirect_links_behavior of this GrantaServerApiDataExportLinkAttributeToExport.
        """
        return self._indirect_links_behavior

    @indirect_links_behavior.setter
    def indirect_links_behavior(
        self, indirect_links_behavior: "Union[GrantaServerApiIndirectLinks, Unset_Type]"
    ) -> None:
        """Sets the indirect_links_behavior of this GrantaServerApiDataExportLinkAttributeToExport.

        Parameters
        ----------
        indirect_links_behavior: Union[GrantaServerApiIndirectLinks, Unset_Type]
            The indirect_links_behavior of this GrantaServerApiDataExportLinkAttributeToExport.
        """
        # Field is not nullable
        if indirect_links_behavior is None:
            raise ValueError(
                "Invalid value for 'indirect_links_behavior', must not be 'None'"
            )
        self._indirect_links_behavior = indirect_links_behavior

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
        if not isinstance(other, GrantaServerApiDataExportLinkAttributeToExport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
