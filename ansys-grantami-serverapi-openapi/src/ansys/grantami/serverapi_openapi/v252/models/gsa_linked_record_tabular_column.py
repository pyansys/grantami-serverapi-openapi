"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.v252.models.gsa_tabular_column import GsaTabularColumn  # noqa: F401
from ansys.grantami.serverapi_openapi.v252.models.gsa_tabular_column_dto_type import GsaTabularColumnDtoType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaLinkedRecordTabularColumn(GsaTabularColumn):
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
        "column_type": "GsaTabularColumnDtoType",
        "display_names": "dict(str, str)",
        "guid": "str",
        "name": "str",
        "roll_up_type": "GsaTabularColumnRollUpType",
        "show_as_link": "bool",
        "summary_row_enabled": "bool",
        "summary_row_roll_up_type": "GsaTabularColumnRollUpType",
        "summary_row_text": "str",
    }

    attribute_map: dict[str, str] = {
        "column_type": "columnType",
        "display_names": "displayNames",
        "guid": "guid",
        "name": "name",
        "roll_up_type": "rollUpType",
        "show_as_link": "showAsLink",
        "summary_row_enabled": "summaryRowEnabled",
        "summary_row_roll_up_type": "summaryRowRollUpType",
        "summary_row_text": "summaryRowText",
    }

    subtype_mapping: dict[str, str] = {
    }

    discriminator: Optional[str] = None

    def __init__(self, *, column_type: "GsaTabularColumnDtoType" = GsaTabularColumnDtoType.LINKEDRECORD, display_names: "dict[str, str]", guid: "str", name: "str", roll_up_type: "GsaTabularColumnRollUpType", show_as_link: "bool", summary_row_enabled: "bool", summary_row_roll_up_type: "GsaTabularColumnRollUpType", summary_row_text: "str",) -> None:
        """GsaLinkedRecordTabularColumn - a model defined in Swagger

        Parameters
        ----------
        column_type: GsaTabularColumnDtoType
        display_names: dict[str, str]
        guid: str
        name: str
        roll_up_type: GsaTabularColumnRollUpType
        show_as_link: bool
        summary_row_enabled: bool
        summary_row_roll_up_type: GsaTabularColumnRollUpType
        summary_row_text: str
        """
        super().__init__(column_type=column_type, display_names=display_names, guid=guid, name=name, roll_up_type=roll_up_type, show_as_link=show_as_link, summary_row_enabled=summary_row_enabled, summary_row_roll_up_type=summary_row_roll_up_type, summary_row_text=summary_row_text)


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
        if not isinstance(other, GsaLinkedRecordTabularColumn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

