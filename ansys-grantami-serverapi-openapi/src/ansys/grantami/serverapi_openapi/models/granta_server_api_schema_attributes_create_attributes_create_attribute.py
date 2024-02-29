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


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute(ModelBase):
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
    discriminator_class_map: Dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: Dict[str, str] = {
        "name": "str",
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "guid": "str",
        "help_path": "str",
    }

    attribute_map: Dict[str, str] = {
        "name": "name",
        "about_attribute": "aboutAttribute",
        "default_threshold_type": "defaultThresholdType",
        "guid": "guid",
        "help_path": "helpPath",
    }

    subtype_mapping: Dict[str, str] = {
        "defaultThresholdType": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "aboutAttribute": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
    }

    discriminator_value_class_map = {
        "point".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreatePointAttribute",
        "integer".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateIntegerAttribute",
        "range".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateRangeAttribute",
        "logical".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateLogicalAttribute",
        "shortText".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateShortTextAttribute",
        "longText".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateLongTextAttribute",
        "dateTime".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateDateTimeAttribute",
        "discrete".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteAttribute",
        "hyperlink".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateHyperlinkAttribute",
        "file".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateFileAttribute",
        "picture".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreatePictureAttribute",
        "link".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateTabularAttribute",
        "floatFunctional".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateFloatFunctionalAttribute",
        "discreteFunctional".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateDiscreteFunctionalAttribute",
        "mathsFunctional".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesCreateAttributesCreateMathsFunctionalAttribute",
    }

    discriminator: Optional[str] = "type"

    def __init__(
        self,
        *,
        name: "str",
        about_attribute: "Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]" = Unset,
        default_threshold_type: "Union[GrantaServerApiSchemaAttributesAttributeThresholdType, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
        help_path: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute - a model defined in Swagger

        Parameters
        ----------
        name: str
        about_attribute: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
        default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType, optional
        guid: str, optional
        help_path: str, optional
        """
        self._default_threshold_type: Union[
            GrantaServerApiSchemaAttributesAttributeThresholdType, Unset_Type
        ] = Unset
        self._help_path: Union[str, None, Unset_Type] = Unset
        self._about_attribute: Union[
            GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type
        ] = Unset
        self._name: str
        self._guid: Union[str, Unset_Type] = Unset

        if default_threshold_type is not Unset:
            self.default_threshold_type = default_threshold_type
        if help_path is not Unset:
            self.help_path = help_path
        if about_attribute is not Unset:
            self.about_attribute = about_attribute
        self.name = name
        if guid is not Unset:
            self.guid = guid

    @property
    def default_threshold_type(
        self,
    ) -> "Union[GrantaServerApiSchemaAttributesAttributeThresholdType, Unset_Type]":
        """Gets the default_threshold_type of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.

        Returns
        -------
        Union[GrantaServerApiSchemaAttributesAttributeThresholdType, Unset_Type]
            The default_threshold_type of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.
        """
        return self._default_threshold_type

    @default_threshold_type.setter
    def default_threshold_type(
        self,
        default_threshold_type: "Union[GrantaServerApiSchemaAttributesAttributeThresholdType, Unset_Type]",
    ) -> None:
        """Sets the default_threshold_type of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.

        Parameters
        ----------
        default_threshold_type: Union[GrantaServerApiSchemaAttributesAttributeThresholdType, Unset_Type]
            The default_threshold_type of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.
        """
        # Field is not nullable
        if default_threshold_type is None:
            raise ValueError(
                "Invalid value for 'default_threshold_type', must not be 'None'"
            )
        self._default_threshold_type = default_threshold_type

    @property
    def help_path(self) -> "Union[str, None, Unset_Type]":
        """Gets the help_path of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.

        Returns
        -------
        Union[str, None, Unset_Type]
            The help_path of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.
        """
        return self._help_path

    @help_path.setter
    def help_path(self, help_path: "Union[str, None, Unset_Type]") -> None:
        """Sets the help_path of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.

        Parameters
        ----------
        help_path: Union[str, None, Unset_Type]
            The help_path of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.
        """
        self._help_path = help_path

    @property
    def about_attribute(
        self,
    ) -> "Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]":
        """Gets the about_attribute of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.

        Returns
        -------
        Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]
            The about_attribute of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.
        """
        return self._about_attribute

    @about_attribute.setter
    def about_attribute(
        self,
        about_attribute: "Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]",
    ) -> None:
        """Sets the about_attribute of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.

        Parameters
        ----------
        about_attribute: Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]
            The about_attribute of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.
        """
        # Field is not nullable
        if about_attribute is None:
            raise ValueError("Invalid value for 'about_attribute', must not be 'None'")
        self._about_attribute = about_attribute

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
        self._name = name

    @property
    def guid(self) -> "Union[str, Unset_Type]":
        """Gets the guid of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.

        Returns
        -------
        Union[str, Unset_Type]
            The guid of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, Unset_Type]") -> None:
        """Sets the guid of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.

        Parameters
        ----------
        guid: Union[str, Unset_Type]
            The guid of this GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        self._guid = guid

    @classmethod
    def get_real_child_model(cls, data: Dict[str, str]) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[cls._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen,
        # so we have to extract it from the JSON reference
        return cls.discriminator_value_class_map[discriminator_value].rsplit("/", 1)[-1]

    @classmethod
    def _get_discriminator_field_name(cls) -> str:
        assert cls.discriminator
        name_tokens = cls.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(
            other, GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
