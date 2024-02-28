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
from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_datums_link_datum import (
    GrantaServerApiDataExportDatumsLinkDatum,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiDataExportDatumsLinkedRecordsDatum(
    GrantaServerApiDataExportDatumsLinkDatum
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
        "attribute_guid": "str",
        "attribute_identity": "int",
        "datum_type": "str",
        "export_in_reversed_direction": "bool",
        "link_attribute_type": "GrantaServerApiLinkAttributeType",
        "link_datum_type": "str",
        "link_group_identities_by_database_key": "dict(str, int)",
        "link_group_name": "str",
        "link_group_names_by_database_key": "dict(str, str)",
        "linked_records": "list[GrantaServerApiDataExportRecordWithData]",
        "meta_datums": "list[GrantaServerApiDataExportDatumsDatum]",
        "not_applicable": "str",
        "rolled_up_data": "list[GrantaServerApiDataExportDatumsRollupRollupDatum]",
        "target_database_guid": "str",
    }

    attribute_map: Dict[str, str] = {
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "datum_type": "datumType",
        "export_in_reversed_direction": "exportInReversedDirection",
        "link_attribute_type": "linkAttributeType",
        "link_datum_type": "linkDatumType",
        "link_group_identities_by_database_key": "linkGroupIdentitiesByDatabaseKey",
        "link_group_name": "linkGroupName",
        "link_group_names_by_database_key": "linkGroupNamesByDatabaseKey",
        "linked_records": "linkedRecords",
        "meta_datums": "metaDatums",
        "not_applicable": "notApplicable",
        "rolled_up_data": "rolledUpData",
        "target_database_guid": "targetDatabaseGuid",
    }

    subtype_mapping: Dict[str, str] = {
        "linkAttributeType": "GrantaServerApiLinkAttributeType",
        "linkedRecords": "GrantaServerApiDataExportRecordWithData",
        "rolledUpData": "GrantaServerApiDataExportDatumsRollupRollupDatum",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_guid: "Union[str, Unset_Type]" = Unset,
        attribute_identity: "Union[int, Unset_Type]" = Unset,
        datum_type: "str" = "link",
        export_in_reversed_direction: "Union[bool, Unset_Type]" = Unset,
        link_attribute_type: "Union[GrantaServerApiLinkAttributeType, Unset_Type]" = Unset,
        link_datum_type: "str" = "linkGroup",
        link_group_identities_by_database_key: "Union[Dict[str, int], None, Unset_Type]" = Unset,
        link_group_name: "Union[str, None, Unset_Type]" = Unset,
        link_group_names_by_database_key: "Union[Dict[str, str], None, Unset_Type]" = Unset,
        linked_records: "Union[List[GrantaServerApiDataExportRecordWithData], None, Unset_Type]" = Unset,
        meta_datums: "Union[List[GrantaServerApiDataExportDatumsDatum], None, Unset_Type]" = Unset,
        not_applicable: "str" = "applicable",
        rolled_up_data: "Union[List[GrantaServerApiDataExportDatumsRollupRollupDatum], None, Unset_Type]" = Unset,
        target_database_guid: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiDataExportDatumsLinkedRecordsDatum - a model defined in Swagger

        Parameters
        ----------
        attribute_guid: str, optional
        attribute_identity: int, optional
        datum_type: str
        export_in_reversed_direction: bool, optional
        link_attribute_type: GrantaServerApiLinkAttributeType, optional
        link_datum_type: str
        link_group_identities_by_database_key: Dict[str, int], optional
        link_group_name: str, optional
        link_group_names_by_database_key: Dict[str, str], optional
        linked_records: List[GrantaServerApiDataExportRecordWithData], optional
        meta_datums: List[GrantaServerApiDataExportDatumsDatum], optional
        not_applicable: str
        rolled_up_data: List[GrantaServerApiDataExportDatumsRollupRollupDatum], optional
        target_database_guid: str, optional
        """
        super().__init__(
            attribute_guid=attribute_guid,
            attribute_identity=attribute_identity,
            datum_type=datum_type,
            meta_datums=meta_datums,
            not_applicable=not_applicable,
        )
        self._link_group_name: Union[str, None, Unset_Type] = Unset
        self._link_attribute_type: Union[
            GrantaServerApiLinkAttributeType, Unset_Type
        ] = Unset
        self._export_in_reversed_direction: Union[bool, Unset_Type] = Unset
        self._target_database_guid: Union[str, None, Unset_Type] = Unset
        self._linked_records: Union[
            List[GrantaServerApiDataExportRecordWithData], None, Unset_Type
        ] = Unset
        self._link_group_names_by_database_key: Union[
            Dict[str, str], None, Unset_Type
        ] = Unset
        self._link_group_identities_by_database_key: Union[
            Dict[str, int], None, Unset_Type
        ] = Unset
        self._rolled_up_data: Union[
            List[GrantaServerApiDataExportDatumsRollupRollupDatum], None, Unset_Type
        ] = Unset
        self._link_datum_type: str

        if link_group_name is not Unset:
            self.link_group_name = link_group_name
        if link_attribute_type is not Unset:
            self.link_attribute_type = link_attribute_type
        if export_in_reversed_direction is not Unset:
            self.export_in_reversed_direction = export_in_reversed_direction
        if target_database_guid is not Unset:
            self.target_database_guid = target_database_guid
        if linked_records is not Unset:
            self.linked_records = linked_records
        if link_group_names_by_database_key is not Unset:
            self.link_group_names_by_database_key = link_group_names_by_database_key
        if link_group_identities_by_database_key is not Unset:
            self.link_group_identities_by_database_key = (
                link_group_identities_by_database_key
            )
        if rolled_up_data is not Unset:
            self.rolled_up_data = rolled_up_data
        self.link_datum_type = link_datum_type

    @property
    def link_group_name(self) -> "Union[str, None, Unset_Type]":
        """Gets the link_group_name of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.

        Returns
        -------
        Union[str, None, Unset_Type]
            The link_group_name of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.
        """
        return self._link_group_name

    @link_group_name.setter
    def link_group_name(self, link_group_name: "Union[str, None, Unset_Type]") -> None:
        """Sets the link_group_name of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.

        Parameters
        ----------
        link_group_name: Union[str, None, Unset_Type]
            The link_group_name of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.
        """
        self._link_group_name = link_group_name

    @property
    def link_attribute_type(
        self,
    ) -> "Union[GrantaServerApiLinkAttributeType, Unset_Type]":
        """Gets the link_attribute_type of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.

        Returns
        -------
        Union[GrantaServerApiLinkAttributeType, Unset_Type]
            The link_attribute_type of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.
        """
        return self._link_attribute_type

    @link_attribute_type.setter
    def link_attribute_type(
        self, link_attribute_type: "Union[GrantaServerApiLinkAttributeType, Unset_Type]"
    ) -> None:
        """Sets the link_attribute_type of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.

        Parameters
        ----------
        link_attribute_type: Union[GrantaServerApiLinkAttributeType, Unset_Type]
            The link_attribute_type of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.
        """
        # Field is not nullable
        if link_attribute_type is None:
            raise ValueError(
                "Invalid value for 'link_attribute_type', must not be 'None'"
            )
        self._link_attribute_type = link_attribute_type

    @property
    def export_in_reversed_direction(self) -> "Union[bool, Unset_Type]":
        """Gets the export_in_reversed_direction of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.

        Returns
        -------
        Union[bool, Unset_Type]
            The export_in_reversed_direction of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.
        """
        return self._export_in_reversed_direction

    @export_in_reversed_direction.setter
    def export_in_reversed_direction(
        self, export_in_reversed_direction: "Union[bool, Unset_Type]"
    ) -> None:
        """Sets the export_in_reversed_direction of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.

        Parameters
        ----------
        export_in_reversed_direction: Union[bool, Unset_Type]
            The export_in_reversed_direction of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.
        """
        # Field is not nullable
        if export_in_reversed_direction is None:
            raise ValueError(
                "Invalid value for 'export_in_reversed_direction', must not be 'None'"
            )
        self._export_in_reversed_direction = export_in_reversed_direction

    @property
    def target_database_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the target_database_guid of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.

        Returns
        -------
        Union[str, None, Unset_Type]
            The target_database_guid of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.
        """
        return self._target_database_guid

    @target_database_guid.setter
    def target_database_guid(
        self, target_database_guid: "Union[str, None, Unset_Type]"
    ) -> None:
        """Sets the target_database_guid of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.

        Parameters
        ----------
        target_database_guid: Union[str, None, Unset_Type]
            The target_database_guid of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.
        """
        self._target_database_guid = target_database_guid

    @property
    def linked_records(
        self,
    ) -> "Union[List[GrantaServerApiDataExportRecordWithData], None, Unset_Type]":
        """Gets the linked_records of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.

        Returns
        -------
        Union[List[GrantaServerApiDataExportRecordWithData], None, Unset_Type]
            The linked_records of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.
        """
        return self._linked_records

    @linked_records.setter
    def linked_records(
        self,
        linked_records: "Union[List[GrantaServerApiDataExportRecordWithData], None, Unset_Type]",
    ) -> None:
        """Sets the linked_records of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.

        Parameters
        ----------
        linked_records: Union[List[GrantaServerApiDataExportRecordWithData], None, Unset_Type]
            The linked_records of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.
        """
        self._linked_records = linked_records

    @property
    def link_group_names_by_database_key(
        self,
    ) -> "Union[Dict[str, str], None, Unset_Type]":
        """Gets the link_group_names_by_database_key of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.

        Returns
        -------
        Union[Dict[str, str], None, Unset_Type]
            The link_group_names_by_database_key of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.
        """
        return self._link_group_names_by_database_key

    @link_group_names_by_database_key.setter
    def link_group_names_by_database_key(
        self,
        link_group_names_by_database_key: "Union[Dict[str, str], None, Unset_Type]",
    ) -> None:
        """Sets the link_group_names_by_database_key of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.

        Parameters
        ----------
        link_group_names_by_database_key: Union[Dict[str, str], None, Unset_Type]
            The link_group_names_by_database_key of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.
        """
        self._link_group_names_by_database_key = link_group_names_by_database_key

    @property
    def link_group_identities_by_database_key(
        self,
    ) -> "Union[Dict[str, int], None, Unset_Type]":
        """Gets the link_group_identities_by_database_key of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.

        Returns
        -------
        Union[Dict[str, int], None, Unset_Type]
            The link_group_identities_by_database_key of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.
        """
        return self._link_group_identities_by_database_key

    @link_group_identities_by_database_key.setter
    def link_group_identities_by_database_key(
        self,
        link_group_identities_by_database_key: "Union[Dict[str, int], None, Unset_Type]",
    ) -> None:
        """Sets the link_group_identities_by_database_key of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.

        Parameters
        ----------
        link_group_identities_by_database_key: Union[Dict[str, int], None, Unset_Type]
            The link_group_identities_by_database_key of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.
        """
        self._link_group_identities_by_database_key = (
            link_group_identities_by_database_key
        )

    @property
    def rolled_up_data(
        self,
    ) -> "Union[List[GrantaServerApiDataExportDatumsRollupRollupDatum], None, Unset_Type]":
        """Gets the rolled_up_data of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.

        Returns
        -------
        Union[List[GrantaServerApiDataExportDatumsRollupRollupDatum], None, Unset_Type]
            The rolled_up_data of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.
        """
        return self._rolled_up_data

    @rolled_up_data.setter
    def rolled_up_data(
        self,
        rolled_up_data: "Union[List[GrantaServerApiDataExportDatumsRollupRollupDatum], None, Unset_Type]",
    ) -> None:
        """Sets the rolled_up_data of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.

        Parameters
        ----------
        rolled_up_data: Union[List[GrantaServerApiDataExportDatumsRollupRollupDatum], None, Unset_Type]
            The rolled_up_data of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.
        """
        self._rolled_up_data = rolled_up_data

    @property
    def link_datum_type(self) -> "str":
        """Gets the link_datum_type of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.

        Returns
        -------
        str
            The link_datum_type of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.
        """
        return self._link_datum_type

    @link_datum_type.setter
    def link_datum_type(self, link_datum_type: "str") -> None:
        """Sets the link_datum_type of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.

        Parameters
        ----------
        link_datum_type: str
            The link_datum_type of this GrantaServerApiDataExportDatumsLinkedRecordsDatum.
        """
        # Field is not nullable
        if link_datum_type is None:
            raise ValueError("Invalid value for 'link_datum_type', must not be 'None'")
        # Field is required
        if link_datum_type is Unset:  # type: ignore[comparison-overlap]
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
        if not isinstance(other, GrantaServerApiDataExportDatumsLinkedRecordsDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
