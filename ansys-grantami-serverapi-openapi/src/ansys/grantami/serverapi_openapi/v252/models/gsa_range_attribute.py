"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.v252.models.gsa_attribute import GsaAttribute  # noqa: F401
from ansys.grantami.serverapi_openapi.v252.models.gsa_attribute_type import GsaAttributeType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaRangeAttribute(GsaAttribute):
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
        "default_threshold_type": "GsaAttributeThresholdType",
        "display_names": "dict(str, str)",
        "guid": "str",
        "info": "GsaAttributeInfo",
        "is_hidden_from_search_criteria": "bool",
        "name": "str",
        "table": "GsaSlimEntity",
        "type": "GsaAttributeType",
        "about_attribute": "GsaSlimTypedAttribute",
        "axis_name": "GsaAxisName",
        "help_path": "str",
        "unit": "GsaSlimUnit",
    }

    attribute_map: dict[str, str] = {
        "default_threshold_type": "defaultThresholdType",
        "display_names": "displayNames",
        "guid": "guid",
        "info": "info",
        "is_hidden_from_search_criteria": "isHiddenFromSearchCriteria",
        "name": "name",
        "table": "table",
        "type": "type",
        "about_attribute": "aboutAttribute",
        "axis_name": "axisName",
        "help_path": "helpPath",
        "unit": "unit",
    }

    subtype_mapping: dict[str, str] = {
        "unit": "GsaSlimUnit",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, default_threshold_type: "GsaAttributeThresholdType", display_names: "dict[str, str]", guid: "str", info: "GsaAttributeInfo", is_hidden_from_search_criteria: "bool", name: "str", table: "GsaSlimEntity", type: "GsaAttributeType" = GsaAttributeType.RANGE, about_attribute: "Union[GsaSlimTypedAttribute, Unset_Type]" = Unset, axis_name: "Union[GsaAxisName, Unset_Type]" = Unset, help_path: "Union[str, None, Unset_Type]" = Unset, unit: "Union[GsaSlimUnit, Unset_Type]" = Unset,) -> None:
        """GsaRangeAttribute - a model defined in Swagger

        Parameters
        ----------
        default_threshold_type: GsaAttributeThresholdType
        display_names: dict[str, str]
        guid: str
        info: GsaAttributeInfo
        is_hidden_from_search_criteria: bool
        name: str
        table: GsaSlimEntity
        type: GsaAttributeType
        about_attribute: GsaSlimTypedAttribute, optional
        axis_name: GsaAxisName, optional
        help_path: str, optional
        unit: GsaSlimUnit, optional
        """
        super().__init__(default_threshold_type=default_threshold_type, display_names=display_names, guid=guid, info=info, is_hidden_from_search_criteria=is_hidden_from_search_criteria, name=name, table=table, type=type, about_attribute=about_attribute, axis_name=axis_name, help_path=help_path)
        self._unit: Union[GsaSlimUnit, Unset_Type] = Unset

        if unit is not Unset:
            self.unit = unit

    @property
    def unit(self) -> "Union[GsaSlimUnit, Unset_Type]":
        """Gets the unit of this GsaRangeAttribute.

        Returns
        -------
        Union[GsaSlimUnit, Unset_Type]
            The unit of this GsaRangeAttribute.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "Union[GsaSlimUnit, Unset_Type]") -> None:
        """Sets the unit of this GsaRangeAttribute.

        Parameters
        ----------
        unit: Union[GsaSlimUnit, Unset_Type]
            The unit of this GsaRangeAttribute.
        """
        # Field is not nullable
        if unit is None:
            raise ValueError("Invalid value for 'unit', must not be 'None'")
        self._unit = unit

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
        if not isinstance(other, GsaRangeAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

