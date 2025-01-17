"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase
from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_attributes_create_attributes_create_attribute import (
    GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute,
)  # noqa: F401


if TYPE_CHECKING:
    from . import *


class GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute(
    GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute
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
        "name": "str",
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "attribute_parameters": "list[GrantaServerApiSchemaSlimEntitiesSlimEntity]",
        "axis_name": "str",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "guid": "str",
        "help_path": "str",
        "is_multi_valued": "bool",
        "type": "str",
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
    }

    attribute_map = {
        "name": "name",
        "about_attribute": "aboutAttribute",
        "attribute_parameters": "attributeParameters",
        "axis_name": "axisName",
        "default_threshold_type": "defaultThresholdType",
        "guid": "guid",
        "help_path": "helpPath",
        "is_multi_valued": "isMultiValued",
        "type": "type",
        "unit": "unit",
    }

    subtype_mapping = {
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "attributeParameters": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
    }

    discriminator = None

    def __init__(
        self,
        *,
        name: "str",
        about_attribute: "Optional[GrantaServerApiSchemaSlimEntitiesSlimEntity]" = None,
        attribute_parameters: "Optional[List[GrantaServerApiSchemaSlimEntitiesSlimEntity]]" = None,
        axis_name: "Optional[str]" = None,
        default_threshold_type: "Optional[GrantaServerApiSchemaAttributesAttributeThresholdType]" = None,
        guid: "Optional[str]" = None,
        help_path: "Optional[str]" = None,
        is_multi_valued: "Optional[bool]" = None,
        type: "str" = "point",
        unit: "Optional[GrantaServerApiSchemaSlimEntitiesSlimEntity]" = None,
    ) -> None:
        """GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute - a model defined in Swagger

        Parameters
        ----------
            name: str
            about_attribute: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
            attribute_parameters: List[GrantaServerApiSchemaSlimEntitiesSlimEntity], optional
            axis_name: str, optional
            default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType, optional
            guid: str, optional
            help_path: str, optional
            is_multi_valued: bool, optional
            type: str
            unit: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
        """
        super().__init__(
            name=name,
            about_attribute=about_attribute,
            default_threshold_type=default_threshold_type,
            guid=guid,
            help_path=help_path,
        )
        self._type = None
        self._is_multi_valued = None
        self._unit = None
        self._axis_name = None
        self._attribute_parameters = None

        self.type = type
        if is_multi_valued is not None:
            self.is_multi_valued = is_multi_valued
        if unit is not None:
            self.unit = unit
        if axis_name is not None:
            self.axis_name = axis_name
        if attribute_parameters is not None:
            self.attribute_parameters = attribute_parameters

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @property
    def is_multi_valued(self) -> "bool":
        """Gets the is_multi_valued of this GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute.

        Returns
        -------
        bool
            The is_multi_valued of this GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute.
        """
        return self._is_multi_valued

    @is_multi_valued.setter
    def is_multi_valued(self, is_multi_valued: "bool") -> None:
        """Sets the is_multi_valued of this GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute.

        Parameters
        ----------
        is_multi_valued: bool
            The is_multi_valued of this GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute.
        """
        self._is_multi_valued = is_multi_valued

    @property
    def unit(self) -> "GrantaServerApiSchemaSlimEntitiesSlimEntity":
        """Gets the unit of this GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimEntity
            The unit of this GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "GrantaServerApiSchemaSlimEntitiesSlimEntity") -> None:
        """Sets the unit of this GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute.

        Parameters
        ----------
        unit: GrantaServerApiSchemaSlimEntitiesSlimEntity
            The unit of this GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute.
        """
        self._unit = unit

    @property
    def axis_name(self) -> "str":
        """Gets the axis_name of this GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute.

        Returns
        -------
        str
            The axis_name of this GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute.
        """
        return self._axis_name

    @axis_name.setter
    def axis_name(self, axis_name: "str") -> None:
        """Sets the axis_name of this GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute.

        Parameters
        ----------
        axis_name: str
            The axis_name of this GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute.
        """
        self._axis_name = axis_name

    @property
    def attribute_parameters(
        self,
    ) -> "list[GrantaServerApiSchemaSlimEntitiesSlimEntity]":
        """Gets the attribute_parameters of this GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimEntity]
            The attribute_parameters of this GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute.
        """
        return self._attribute_parameters

    @attribute_parameters.setter
    def attribute_parameters(
        self, attribute_parameters: "list[GrantaServerApiSchemaSlimEntitiesSlimEntity]"
    ) -> None:
        """Sets the attribute_parameters of this GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute.

        Parameters
        ----------
        attribute_parameters: list[GrantaServerApiSchemaSlimEntitiesSlimEntity]
            The attribute_parameters of this GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute.
        """
        self._attribute_parameters = attribute_parameters

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
            other, GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
