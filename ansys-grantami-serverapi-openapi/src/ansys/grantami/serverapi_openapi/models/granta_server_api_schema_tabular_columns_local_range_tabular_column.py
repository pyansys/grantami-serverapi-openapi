"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase
from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_tabular_columns_tabular_column import (
    GrantaServerApiSchemaTabularColumnsTabularColumn,
)  # noqa: F401


if TYPE_CHECKING:
    from . import *


class GrantaServerApiSchemaTabularColumnsLocalRangeTabularColumn(
    GrantaServerApiSchemaTabularColumnsTabularColumn
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
    swagger_types = {
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "display_names": "dict(str, str)",
        "guid": "str",
        "name": "str",
        "roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "show_as_link": "bool",
        "summary_row_enabled": "bool",
        "summary_row_roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "summary_row_text": "str",
        "column_type": "str",
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimUnit",
    }

    attribute_map = {
        "default_threshold_type": "defaultThresholdType",
        "display_names": "displayNames",
        "guid": "guid",
        "name": "name",
        "roll_up_type": "rollUpType",
        "show_as_link": "showAsLink",
        "summary_row_enabled": "summaryRowEnabled",
        "summary_row_roll_up_type": "summaryRowRollUpType",
        "summary_row_text": "summaryRowText",
        "column_type": "columnType",
        "unit": "unit",
    }

    subtype_mapping = {
        "defaultThresholdType": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimUnit",
    }

    discriminator = None

    def __init__(
        self,
        *,
        default_threshold_type: "GrantaServerApiSchemaAttributesAttributeThresholdType",
        display_names: "Dict[str, str]",
        guid: "str",
        name: "str",
        roll_up_type: "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        show_as_link: "bool",
        summary_row_enabled: "bool",
        summary_row_roll_up_type: "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        summary_row_text: "str",
        column_type: "str" = "localRange",
        unit: "Optional[GrantaServerApiSchemaSlimEntitiesSlimUnit]" = None,
    ) -> None:
        """GrantaServerApiSchemaTabularColumnsLocalRangeTabularColumn - a model defined in Swagger

        Parameters
        ----------
            default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType
            display_names: Dict[str, str]
            guid: str
            name: str
            roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
            show_as_link: bool
            summary_row_enabled: bool
            summary_row_roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
            summary_row_text: str
            column_type: str
            unit: GrantaServerApiSchemaSlimEntitiesSlimUnit, optional
        """
        super().__init__(
            display_names=display_names,
            guid=guid,
            name=name,
            roll_up_type=roll_up_type,
            show_as_link=show_as_link,
            summary_row_enabled=summary_row_enabled,
            summary_row_roll_up_type=summary_row_roll_up_type,
            summary_row_text=summary_row_text,
        )
        self._column_type = None
        self._default_threshold_type = None
        self._unit = None

        self.column_type = column_type
        self.default_threshold_type = default_threshold_type
        if unit is not None:
            self.unit = unit

    @property
    def column_type(self) -> "str":
        """Gets the column_type of this GrantaServerApiSchemaTabularColumnsLocalRangeTabularColumn.

        Returns
        -------
        str
            The column_type of this GrantaServerApiSchemaTabularColumnsLocalRangeTabularColumn.
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type: "str") -> None:
        """Sets the column_type of this GrantaServerApiSchemaTabularColumnsLocalRangeTabularColumn.

        Parameters
        ----------
        column_type: str
            The column_type of this GrantaServerApiSchemaTabularColumnsLocalRangeTabularColumn.
        """
        if column_type is None:
            raise ValueError("Invalid value for 'column_type', must not be 'None'")
        self._column_type = column_type

    @property
    def default_threshold_type(
        self,
    ) -> "GrantaServerApiSchemaAttributesAttributeThresholdType":
        """Gets the default_threshold_type of this GrantaServerApiSchemaTabularColumnsLocalRangeTabularColumn.

        Returns
        -------
        GrantaServerApiSchemaAttributesAttributeThresholdType
            The default_threshold_type of this GrantaServerApiSchemaTabularColumnsLocalRangeTabularColumn.
        """
        return self._default_threshold_type

    @default_threshold_type.setter
    def default_threshold_type(
        self,
        default_threshold_type: "GrantaServerApiSchemaAttributesAttributeThresholdType",
    ) -> None:
        """Sets the default_threshold_type of this GrantaServerApiSchemaTabularColumnsLocalRangeTabularColumn.

        Parameters
        ----------
        default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType
            The default_threshold_type of this GrantaServerApiSchemaTabularColumnsLocalRangeTabularColumn.
        """
        if default_threshold_type is None:
            raise ValueError(
                "Invalid value for 'default_threshold_type', must not be 'None'"
            )
        self._default_threshold_type = default_threshold_type

    @property
    def unit(self) -> "GrantaServerApiSchemaSlimEntitiesSlimUnit":
        """Gets the unit of this GrantaServerApiSchemaTabularColumnsLocalRangeTabularColumn.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimUnit
            The unit of this GrantaServerApiSchemaTabularColumnsLocalRangeTabularColumn.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "GrantaServerApiSchemaSlimEntitiesSlimUnit") -> None:
        """Sets the unit of this GrantaServerApiSchemaTabularColumnsLocalRangeTabularColumn.

        Parameters
        ----------
        unit: GrantaServerApiSchemaSlimEntitiesSlimUnit
            The unit of this GrantaServerApiSchemaTabularColumnsLocalRangeTabularColumn.
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
        if not isinstance(
            other, GrantaServerApiSchemaTabularColumnsLocalRangeTabularColumn
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
