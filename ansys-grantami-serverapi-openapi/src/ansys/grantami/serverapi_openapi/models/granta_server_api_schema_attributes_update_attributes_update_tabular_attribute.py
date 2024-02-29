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
from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_attributes_update_attributes_update_attribute import (
    GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute(
    GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute
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
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "axis_name": "str",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "display_full_table": "bool",
        "display_summary_row_inline": "bool",
        "guid": "str",
        "help_path": "str",
        "hide_unlinked_rows": "bool",
        "name": "str",
        "tabular_columns": "list[GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn]",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "about_attribute": "aboutAttribute",
        "axis_name": "axisName",
        "default_threshold_type": "defaultThresholdType",
        "display_full_table": "displayFullTable",
        "display_summary_row_inline": "displaySummaryRowInline",
        "guid": "guid",
        "help_path": "helpPath",
        "hide_unlinked_rows": "hideUnlinkedRows",
        "name": "name",
        "tabular_columns": "tabularColumns",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {
        "tabularColumns": "GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        about_attribute: "Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]" = Unset,
        axis_name: "Union[str, None, Unset_Type]" = Unset,
        default_threshold_type: "Union[GrantaServerApiSchemaAttributesAttributeThresholdType, Unset_Type]" = Unset,
        display_full_table: "Union[bool, Unset_Type]" = Unset,
        display_summary_row_inline: "Union[bool, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
        help_path: "Union[str, None, Unset_Type]" = Unset,
        hide_unlinked_rows: "Union[bool, Unset_Type]" = Unset,
        name: "Union[str, Unset_Type]" = Unset,
        tabular_columns: "Union[List[GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn], None, Unset_Type]" = Unset,
        type: "str" = "link",
    ) -> None:
        """GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute - a model defined in Swagger

        Parameters
        ----------
        about_attribute: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
        axis_name: str, optional
        default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType, optional
        display_full_table: bool, optional
        display_summary_row_inline: bool, optional
        guid: str, optional
        help_path: str, optional
        hide_unlinked_rows: bool, optional
        name: str, optional
        tabular_columns: List[GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn], optional
        type: str
        """
        super().__init__(
            about_attribute=about_attribute,
            axis_name=axis_name,
            default_threshold_type=default_threshold_type,
            guid=guid,
            help_path=help_path,
            name=name,
        )
        self._type: str
        self._display_full_table: Union[bool, Unset_Type] = Unset
        self._display_summary_row_inline: Union[bool, Unset_Type] = Unset
        self._hide_unlinked_rows: Union[bool, Unset_Type] = Unset
        self._tabular_columns: Union[
            List[
                GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn
            ],
            None,
            Unset_Type,
        ] = Unset

        self.type = type
        if display_full_table is not Unset:
            self.display_full_table = display_full_table
        if display_summary_row_inline is not Unset:
            self.display_summary_row_inline = display_summary_row_inline
        if hide_unlinked_rows is not Unset:
            self.hide_unlinked_rows = hide_unlinked_rows
        if tabular_columns is not Unset:
            self.tabular_columns = tabular_columns

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @property
    def display_full_table(self) -> "Union[bool, Unset_Type]":
        """Gets the display_full_table of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.

        Returns
        -------
        Union[bool, Unset_Type]
            The display_full_table of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.
        """
        return self._display_full_table

    @display_full_table.setter
    def display_full_table(self, display_full_table: "Union[bool, Unset_Type]") -> None:
        """Sets the display_full_table of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.

        Parameters
        ----------
        display_full_table: Union[bool, Unset_Type]
            The display_full_table of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.
        """
        # Field is not nullable
        if display_full_table is None:
            raise ValueError(
                "Invalid value for 'display_full_table', must not be 'None'"
            )
        self._display_full_table = display_full_table

    @property
    def display_summary_row_inline(self) -> "Union[bool, Unset_Type]":
        """Gets the display_summary_row_inline of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.

        Returns
        -------
        Union[bool, Unset_Type]
            The display_summary_row_inline of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.
        """
        return self._display_summary_row_inline

    @display_summary_row_inline.setter
    def display_summary_row_inline(
        self, display_summary_row_inline: "Union[bool, Unset_Type]"
    ) -> None:
        """Sets the display_summary_row_inline of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.

        Parameters
        ----------
        display_summary_row_inline: Union[bool, Unset_Type]
            The display_summary_row_inline of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.
        """
        # Field is not nullable
        if display_summary_row_inline is None:
            raise ValueError(
                "Invalid value for 'display_summary_row_inline', must not be 'None'"
            )
        self._display_summary_row_inline = display_summary_row_inline

    @property
    def hide_unlinked_rows(self) -> "Union[bool, Unset_Type]":
        """Gets the hide_unlinked_rows of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.

        Returns
        -------
        Union[bool, Unset_Type]
            The hide_unlinked_rows of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.
        """
        return self._hide_unlinked_rows

    @hide_unlinked_rows.setter
    def hide_unlinked_rows(self, hide_unlinked_rows: "Union[bool, Unset_Type]") -> None:
        """Sets the hide_unlinked_rows of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.

        Parameters
        ----------
        hide_unlinked_rows: Union[bool, Unset_Type]
            The hide_unlinked_rows of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.
        """
        # Field is not nullable
        if hide_unlinked_rows is None:
            raise ValueError(
                "Invalid value for 'hide_unlinked_rows', must not be 'None'"
            )
        self._hide_unlinked_rows = hide_unlinked_rows

    @property
    def tabular_columns(
        self,
    ) -> "Union[List[GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn], None, Unset_Type]":
        """Gets the tabular_columns of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.

        Returns
        -------
        Union[List[GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn], None, Unset_Type]
            The tabular_columns of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.
        """
        return self._tabular_columns

    @tabular_columns.setter
    def tabular_columns(
        self,
        tabular_columns: "Union[List[GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn], None, Unset_Type]",
    ) -> None:
        """Sets the tabular_columns of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.

        Parameters
        ----------
        tabular_columns: Union[List[GrantaServerApiSchemaTabularColumnsUpdateTabularColumnsUpdateTabularColumn], None, Unset_Type]
            The tabular_columns of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute.
        """
        self._tabular_columns = tabular_columns

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
        if not isinstance(
            other, GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
