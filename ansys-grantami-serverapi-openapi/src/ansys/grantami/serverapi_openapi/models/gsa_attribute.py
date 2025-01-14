"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaAttribute(ModelBase):
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
    discriminator_class_map: dict[str, str]
        They key is discriminator value and the value is associated subtype.
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
    }

    subtype_mapping: dict[str, str] = {
        "defaultThresholdType": "GsaAttributeThresholdType",
        "axisName": "GsaAxisName",
        "info": "GsaAttributeInfo",
        "type": "GsaAttributeType",
        "aboutAttribute": "GsaSlimTypedAttribute",
        "table": "GsaSlimEntity",
    }

    discriminator_value_class_map = {
        "point".lower(): "#/components/schemas/GsaPointAttribute",
        "integer".lower(): "#/components/schemas/GsaIntegerAttribute",
        "range".lower(): "#/components/schemas/GsaRangeAttribute",
        "logical".lower(): "#/components/schemas/GsaLogicalAttribute",
        "shortText".lower(): "#/components/schemas/GsaShortTextAttribute",
        "longText".lower(): "#/components/schemas/GsaLongTextAttribute",
        "dateTime".lower(): "#/components/schemas/GsaDateTimeAttribute",
        "discrete".lower(): "#/components/schemas/GsaDiscreteAttribute",
        "hyperlink".lower(): "#/components/schemas/GsaHyperlinkAttribute",
        "file".lower(): "#/components/schemas/GsaFileAttribute",
        "picture".lower(): "#/components/schemas/GsaPictureAttribute",
        "link".lower(): "#/components/schemas/GsaTabularAttribute",
        "floatFunctional".lower(): "#/components/schemas/GsaFloatFunctionalAttribute",
        "discreteFunctional".lower(): "#/components/schemas/GsaDiscreteFunctionalAttribute",
        "mathsFunctional".lower(): "#/components/schemas/GsaMathsFunctionalAttribute",
    }

    discriminator: Optional[str] = "type"

    def __init__(self, *, default_threshold_type: "GsaAttributeThresholdType", display_names: "dict[str, str]", guid: "str", info: "GsaAttributeInfo", is_hidden_from_search_criteria: "bool", name: "str", table: "GsaSlimEntity", type: "GsaAttributeType", about_attribute: "Union[GsaSlimTypedAttribute, Unset_Type]" = Unset, axis_name: "Union[GsaAxisName, Unset_Type]" = Unset, help_path: "Union[str, None, Unset_Type]" = Unset,) -> None:
        """GsaAttribute - a model defined in Swagger

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
        """
        self._default_threshold_type: GsaAttributeThresholdType
        self._axis_name: Union[GsaAxisName, Unset_Type] = Unset
        self._help_path: Union[str, None, Unset_Type] = Unset
        self._info: GsaAttributeInfo
        self._type: GsaAttributeType
        self._about_attribute: Union[GsaSlimTypedAttribute, Unset_Type] = Unset
        self._is_hidden_from_search_criteria: bool
        self._table: GsaSlimEntity
        self._display_names: dict[str, str]
        self._name: str
        self._guid: str

        self.default_threshold_type = default_threshold_type
        if axis_name is not Unset:
            self.axis_name = axis_name
        if help_path is not Unset:
            self.help_path = help_path
        self.info = info
        self.type = type
        if about_attribute is not Unset:
            self.about_attribute = about_attribute
        self.is_hidden_from_search_criteria = is_hidden_from_search_criteria
        self.table = table
        self.display_names = display_names
        self.name = name
        self.guid = guid

    @property
    def default_threshold_type(self) -> "GsaAttributeThresholdType":
        """Gets the default_threshold_type of this GsaAttribute.

        Returns
        -------
        GsaAttributeThresholdType
            The default_threshold_type of this GsaAttribute.
        """
        return self._default_threshold_type

    @default_threshold_type.setter
    def default_threshold_type(self, default_threshold_type: "GsaAttributeThresholdType") -> None:
        """Sets the default_threshold_type of this GsaAttribute.

        Parameters
        ----------
        default_threshold_type: GsaAttributeThresholdType
            The default_threshold_type of this GsaAttribute.
        """
        # Field is not nullable
        if default_threshold_type is None:
            raise ValueError("Invalid value for 'default_threshold_type', must not be 'None'")
        # Field is required
        if default_threshold_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'default_threshold_type', must not be 'Unset'")
        self._default_threshold_type = default_threshold_type

    @property
    def axis_name(self) -> "Union[GsaAxisName, Unset_Type]":
        """Gets the axis_name of this GsaAttribute.

        Returns
        -------
        Union[GsaAxisName, Unset_Type]
            The axis_name of this GsaAttribute.
        """
        return self._axis_name

    @axis_name.setter
    def axis_name(self, axis_name: "Union[GsaAxisName, Unset_Type]") -> None:
        """Sets the axis_name of this GsaAttribute.

        Parameters
        ----------
        axis_name: Union[GsaAxisName, Unset_Type]
            The axis_name of this GsaAttribute.
        """
        # Field is not nullable
        if axis_name is None:
            raise ValueError("Invalid value for 'axis_name', must not be 'None'")
        self._axis_name = axis_name

    @property
    def help_path(self) -> "Union[str, None, Unset_Type]":
        """Gets the help_path of this GsaAttribute.

        Returns
        -------
        Union[str, None, Unset_Type]
            The help_path of this GsaAttribute.
        """
        return self._help_path

    @help_path.setter
    def help_path(self, help_path: "Union[str, None, Unset_Type]") -> None:
        """Sets the help_path of this GsaAttribute.

        Parameters
        ----------
        help_path: Union[str, None, Unset_Type]
            The help_path of this GsaAttribute.
        """
        self._help_path = help_path

    @property
    def info(self) -> "GsaAttributeInfo":
        """Gets the info of this GsaAttribute.

        Returns
        -------
        GsaAttributeInfo
            The info of this GsaAttribute.
        """
        return self._info

    @info.setter
    def info(self, info: "GsaAttributeInfo") -> None:
        """Sets the info of this GsaAttribute.

        Parameters
        ----------
        info: GsaAttributeInfo
            The info of this GsaAttribute.
        """
        # Field is not nullable
        if info is None:
            raise ValueError("Invalid value for 'info', must not be 'None'")
        # Field is required
        if info is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'info', must not be 'Unset'")
        self._info = info

    @property
    def type(self) -> "GsaAttributeType":
        """Gets the type of this GsaAttribute.

        Returns
        -------
        GsaAttributeType
            The type of this GsaAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "GsaAttributeType") -> None:
        """Sets the type of this GsaAttribute.

        Parameters
        ----------
        type: GsaAttributeType
            The type of this GsaAttribute.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @property
    def about_attribute(self) -> "Union[GsaSlimTypedAttribute, Unset_Type]":
        """Gets the about_attribute of this GsaAttribute.

        Returns
        -------
        Union[GsaSlimTypedAttribute, Unset_Type]
            The about_attribute of this GsaAttribute.
        """
        return self._about_attribute

    @about_attribute.setter
    def about_attribute(self, about_attribute: "Union[GsaSlimTypedAttribute, Unset_Type]") -> None:
        """Sets the about_attribute of this GsaAttribute.

        Parameters
        ----------
        about_attribute: Union[GsaSlimTypedAttribute, Unset_Type]
            The about_attribute of this GsaAttribute.
        """
        # Field is not nullable
        if about_attribute is None:
            raise ValueError("Invalid value for 'about_attribute', must not be 'None'")
        self._about_attribute = about_attribute

    @property
    def is_hidden_from_search_criteria(self) -> "bool":
        """Gets the is_hidden_from_search_criteria of this GsaAttribute.
        If true, the attribute should not be shown in search UIs.  It will still be included in text searches.

        Returns
        -------
        bool
            The is_hidden_from_search_criteria of this GsaAttribute.
        """
        return self._is_hidden_from_search_criteria

    @is_hidden_from_search_criteria.setter
    def is_hidden_from_search_criteria(self, is_hidden_from_search_criteria: "bool") -> None:
        """Sets the is_hidden_from_search_criteria of this GsaAttribute.
        If true, the attribute should not be shown in search UIs.  It will still be included in text searches.

        Parameters
        ----------
        is_hidden_from_search_criteria: bool
            The is_hidden_from_search_criteria of this GsaAttribute.
        """
        # Field is not nullable
        if is_hidden_from_search_criteria is None:
            raise ValueError("Invalid value for 'is_hidden_from_search_criteria', must not be 'None'")
        # Field is required
        if is_hidden_from_search_criteria is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'is_hidden_from_search_criteria', must not be 'Unset'")
        self._is_hidden_from_search_criteria = is_hidden_from_search_criteria

    @property
    def table(self) -> "GsaSlimEntity":
        """Gets the table of this GsaAttribute.

        Returns
        -------
        GsaSlimEntity
            The table of this GsaAttribute.
        """
        return self._table

    @table.setter
    def table(self, table: "GsaSlimEntity") -> None:
        """Sets the table of this GsaAttribute.

        Parameters
        ----------
        table: GsaSlimEntity
            The table of this GsaAttribute.
        """
        # Field is not nullable
        if table is None:
            raise ValueError("Invalid value for 'table', must not be 'None'")
        # Field is required
        if table is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'table', must not be 'Unset'")
        self._table = table

    @property
    def display_names(self) -> "dict[str, str]":
        """Gets the display_names of this GsaAttribute.

        Returns
        -------
        dict[str, str]
            The display_names of this GsaAttribute.
        """
        return self._display_names

    @display_names.setter
    def display_names(self, display_names: "dict[str, str]") -> None:
        """Sets the display_names of this GsaAttribute.

        Parameters
        ----------
        display_names: dict[str, str]
            The display_names of this GsaAttribute.
        """
        # Field is not nullable
        if display_names is None:
            raise ValueError("Invalid value for 'display_names', must not be 'None'")
        # Field is required
        if display_names is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'display_names', must not be 'Unset'")
        self._display_names = display_names

    @property
    def name(self) -> "str":
        """Gets the name of this GsaAttribute.

        Returns
        -------
        str
            The name of this GsaAttribute.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GsaAttribute.

        Parameters
        ----------
        name: str
            The name of this GsaAttribute.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        # Field is required
        if name is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'name', must not be 'Unset'")
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GsaAttribute.

        Returns
        -------
        str
            The guid of this GsaAttribute.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GsaAttribute.

        Parameters
        ----------
        guid: str
            The guid of this GsaAttribute.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        # Field is required
        if guid is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'guid', must not be 'Unset'")
        self._guid = guid

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
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
        if not isinstance(other, GsaAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

