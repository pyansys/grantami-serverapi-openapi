"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.v252.models.gsa_data_export_rollup_datum import GsaDataExportRollupDatum  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaDataExportCountRollupDatum(GsaDataExportRollupDatum):
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
        "type": "str",
        "attribute_guid": "str",
        "attribute_identity": "int",
        "count": "int",
        "database_key": "str",
        "roll_up_type": "GsaTabularColumnRollUpType",
    }

    attribute_map: dict[str, str] = {
        "type": "type",
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "count": "count",
        "database_key": "databaseKey",
        "roll_up_type": "rollUpType",
    }

    subtype_mapping: dict[str, str] = {
    }

    discriminator: Optional[str] = None

    def __init__(self, *, type: "str" = "countRollup", attribute_guid: "Union[str, None, Unset_Type]" = Unset, attribute_identity: "Union[int, None, Unset_Type]" = Unset, count: "Union[int, Unset_Type]" = Unset, database_key: "Union[str, None, Unset_Type]" = Unset, roll_up_type: "Union[GsaTabularColumnRollUpType, Unset_Type]" = Unset,) -> None:
        """GsaDataExportCountRollupDatum - a model defined in Swagger

        Parameters
        ----------
        type: str
        attribute_guid: str, optional
        attribute_identity: int, optional
        count: int, optional
        database_key: str, optional
        roll_up_type: GsaTabularColumnRollUpType, optional
        """
        super().__init__(type=type, attribute_guid=attribute_guid, attribute_identity=attribute_identity, database_key=database_key, roll_up_type=roll_up_type)
        self._count: Union[int, Unset_Type] = Unset

        if count is not Unset:
            self.count = count

    @property
    def count(self) -> "Union[int, Unset_Type]":
        """Gets the count of this GsaDataExportCountRollupDatum.

        Returns
        -------
        Union[int, Unset_Type]
            The count of this GsaDataExportCountRollupDatum.
        """
        return self._count

    @count.setter
    def count(self, count: "Union[int, Unset_Type]") -> None:
        """Sets the count of this GsaDataExportCountRollupDatum.

        Parameters
        ----------
        count: Union[int, Unset_Type]
            The count of this GsaDataExportCountRollupDatum.
        """
        # Field is not nullable
        if count is None:
            raise ValueError("Invalid value for 'count', must not be 'None'")
        self._count = count

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
        if not isinstance(other, GsaDataExportCountRollupDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

