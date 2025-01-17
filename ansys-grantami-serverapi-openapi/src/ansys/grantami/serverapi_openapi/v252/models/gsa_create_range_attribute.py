"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.v252.models.gsa_create_attribute import GsaCreateAttribute  # noqa: F401
from ansys.grantami.serverapi_openapi.v252.models.gsa_attribute_type import GsaAttributeType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaCreateRangeAttribute(GsaCreateAttribute):
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
        "name": "str",
        "type": "GsaAttributeType",
        "axis_name": "GsaCreateAxisName",
        "default_threshold_type": "GsaAttributeThresholdType",
        "guid": "str",
        "help_path": "str",
        "is_hidden_from_search_criteria": "bool",
        "unit": "GsaSlimEntity",
    }

    attribute_map: dict[str, str] = {
        "name": "name",
        "type": "type",
        "axis_name": "axisName",
        "default_threshold_type": "defaultThresholdType",
        "guid": "guid",
        "help_path": "helpPath",
        "is_hidden_from_search_criteria": "isHiddenFromSearchCriteria",
        "unit": "unit",
    }

    subtype_mapping: dict[str, str] = {
        "unit": "GsaSlimEntity",
        "axisName": "GsaCreateAxisName",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, name: "str", type: "GsaAttributeType" = GsaAttributeType.RANGE, axis_name: "Union[GsaCreateAxisName, Unset_Type]" = Unset, default_threshold_type: "Union[GsaAttributeThresholdType, Unset_Type]" = Unset, guid: "Union[str, Unset_Type]" = Unset, help_path: "Union[str, None, Unset_Type]" = Unset, is_hidden_from_search_criteria: "Union[bool, None, Unset_Type]" = Unset, unit: "Union[GsaSlimEntity, Unset_Type]" = Unset,) -> None:
        """GsaCreateRangeAttribute - a model defined in Swagger

        Parameters
        ----------
        name: str
        type: GsaAttributeType
        axis_name: GsaCreateAxisName, optional
        default_threshold_type: GsaAttributeThresholdType, optional
        guid: str, optional
        help_path: str, optional
        is_hidden_from_search_criteria: bool, optional
        unit: GsaSlimEntity, optional
        """
        super().__init__(name=name, type=type, default_threshold_type=default_threshold_type, guid=guid, help_path=help_path, is_hidden_from_search_criteria=is_hidden_from_search_criteria)
        self._unit: Union[GsaSlimEntity, Unset_Type] = Unset
        self._axis_name: Union[GsaCreateAxisName, Unset_Type] = Unset

        if unit is not Unset:
            self.unit = unit
        if axis_name is not Unset:
            self.axis_name = axis_name

    @property
    def unit(self) -> "Union[GsaSlimEntity, Unset_Type]":
        """Gets the unit of this GsaCreateRangeAttribute.

        Returns
        -------
        Union[GsaSlimEntity, Unset_Type]
            The unit of this GsaCreateRangeAttribute.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "Union[GsaSlimEntity, Unset_Type]") -> None:
        """Sets the unit of this GsaCreateRangeAttribute.

        Parameters
        ----------
        unit: Union[GsaSlimEntity, Unset_Type]
            The unit of this GsaCreateRangeAttribute.
        """
        # Field is not nullable
        if unit is None:
            raise ValueError("Invalid value for 'unit', must not be 'None'")
        self._unit = unit

    @property
    def axis_name(self) -> "Union[GsaCreateAxisName, Unset_Type]":
        """Gets the axis_name of this GsaCreateRangeAttribute.

        Returns
        -------
        Union[GsaCreateAxisName, Unset_Type]
            The axis_name of this GsaCreateRangeAttribute.
        """
        return self._axis_name

    @axis_name.setter
    def axis_name(self, axis_name: "Union[GsaCreateAxisName, Unset_Type]") -> None:
        """Sets the axis_name of this GsaCreateRangeAttribute.

        Parameters
        ----------
        axis_name: Union[GsaCreateAxisName, Unset_Type]
            The axis_name of this GsaCreateRangeAttribute.
        """
        # Field is not nullable
        if axis_name is None:
            raise ValueError("Invalid value for 'axis_name', must not be 'None'")
        self._axis_name = axis_name

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
        if not isinstance(other, GsaCreateRangeAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

