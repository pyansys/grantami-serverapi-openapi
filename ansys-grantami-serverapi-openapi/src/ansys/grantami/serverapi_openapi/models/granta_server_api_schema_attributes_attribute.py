"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
    from . import *

class GrantaServerApiSchemaAttributesAttribute(ModelBase):
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
    """
    swagger_types = {
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "axis_name": "str",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "display_names": "dict(str, str)",
        "guid": "str",
        "help_path": "str",
        "info": "GrantaServerApiSchemaAttributesAttributeAttributeInfo",
        "name": "str",
    }

    attribute_map = {
        "about_attribute": "aboutAttribute",
        "axis_name": "axisName",
        "default_threshold_type": "defaultThresholdType",
        "display_names": "displayNames",
        "guid": "guid",
        "help_path": "helpPath",
        "info": "info",
        "name": "name",
    }

    subtype_mapping = {
        "defaultThresholdType": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "aboutAttribute": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "info": "GrantaServerApiSchemaAttributesAttributeAttributeInfo",
    }

    discriminator_value_class_map = {
        "point".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesPointAttribute",
        "integer".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesIntegerAttribute",
        "range".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesRangeAttribute",
        "logical".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesLogicalAttribute",
        "shortText".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesShortTextAttribute",
        "longText".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesLongTextAttribute",
        "dateTime".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesDateTimeAttribute",
        "discrete".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesDiscreteAttribute",
        "hyperlink".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesHyperlinkAttribute",
        "file".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesFileAttribute",
        "picture".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesPictureAttribute",
        "link".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesTabularAttribute",
        "floatFunctional".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesFloatFunctionalAttribute",
        "discreteFunctional".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesDiscreteFunctionalAttribute",
        "mathsFunctional".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesMathsFunctionalAttribute",
    }

    def __init__(self, *, about_attribute: "Optional[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]" = None, axis_name: "Optional[str]" = None, default_threshold_type: "Optional[GrantaServerApiSchemaAttributesAttributeThresholdType]" = None, display_names: "Optional[Dict[str, str]]" = None, guid: "Optional[str]" = None, help_path: "Optional[str]" = None, info: "Optional[GrantaServerApiSchemaAttributesAttributeAttributeInfo]" = None, name: "Optional[str]" = None,) -> None:
        """GrantaServerApiSchemaAttributesAttribute - a model defined in Swagger

        Parameters
        ----------
            about_attribute: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, optional
            axis_name: str, optional
            default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType, optional
            display_names: Dict[str, str], optional
            guid: str, optional
            help_path: str, optional
            info: GrantaServerApiSchemaAttributesAttributeAttributeInfo, optional
            name: str, optional
        """
        self._default_threshold_type = None
        self._axis_name = None
        self._help_path = None
        self._about_attribute = None
        self._info = None
        self._display_names = None
        self._name = None
        self._guid = None
        self.discriminator = "type"
        if default_threshold_type is not None:
            self.default_threshold_type = default_threshold_type
        if axis_name is not None:
            self.axis_name = axis_name
        if help_path is not None:
            self.help_path = help_path
        if about_attribute is not None:
            self.about_attribute = about_attribute
        if info is not None:
            self.info = info
        if display_names is not None:
            self.display_names = display_names
        if name is not None:
            self.name = name
        if guid is not None:
            self.guid = guid

    @property
    def default_threshold_type(self) -> "GrantaServerApiSchemaAttributesAttributeThresholdType":
        """Gets the default_threshold_type of this GrantaServerApiSchemaAttributesAttribute.

        Returns
        -------
        GrantaServerApiSchemaAttributesAttributeThresholdType
            The default_threshold_type of this GrantaServerApiSchemaAttributesAttribute.
        """
        return self._default_threshold_type

    @default_threshold_type.setter
    def default_threshold_type(self, default_threshold_type: "GrantaServerApiSchemaAttributesAttributeThresholdType") -> None:
        """Sets the default_threshold_type of this GrantaServerApiSchemaAttributesAttribute.

        Parameters
        ----------
        default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType
            The default_threshold_type of this GrantaServerApiSchemaAttributesAttribute.
        """
        self._default_threshold_type = default_threshold_type

    @property
    def axis_name(self) -> "str":
        """Gets the axis_name of this GrantaServerApiSchemaAttributesAttribute.

        Returns
        -------
        str
            The axis_name of this GrantaServerApiSchemaAttributesAttribute.
        """
        return self._axis_name

    @axis_name.setter
    def axis_name(self, axis_name: "str") -> None:
        """Sets the axis_name of this GrantaServerApiSchemaAttributesAttribute.

        Parameters
        ----------
        axis_name: str
            The axis_name of this GrantaServerApiSchemaAttributesAttribute.
        """
        self._axis_name = axis_name

    @property
    def help_path(self) -> "str":
        """Gets the help_path of this GrantaServerApiSchemaAttributesAttribute.

        Returns
        -------
        str
            The help_path of this GrantaServerApiSchemaAttributesAttribute.
        """
        return self._help_path

    @help_path.setter
    def help_path(self, help_path: "str") -> None:
        """Sets the help_path of this GrantaServerApiSchemaAttributesAttribute.

        Parameters
        ----------
        help_path: str
            The help_path of this GrantaServerApiSchemaAttributesAttribute.
        """
        self._help_path = help_path

    @property
    def about_attribute(self) -> "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity":
        """Gets the about_attribute of this GrantaServerApiSchemaAttributesAttribute.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
            The about_attribute of this GrantaServerApiSchemaAttributesAttribute.
        """
        return self._about_attribute

    @about_attribute.setter
    def about_attribute(self, about_attribute: "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity") -> None:
        """Sets the about_attribute of this GrantaServerApiSchemaAttributesAttribute.

        Parameters
        ----------
        about_attribute: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
            The about_attribute of this GrantaServerApiSchemaAttributesAttribute.
        """
        self._about_attribute = about_attribute

    @property
    def info(self) -> "GrantaServerApiSchemaAttributesAttributeAttributeInfo":
        """Gets the info of this GrantaServerApiSchemaAttributesAttribute.

        Returns
        -------
        GrantaServerApiSchemaAttributesAttributeAttributeInfo
            The info of this GrantaServerApiSchemaAttributesAttribute.
        """
        return self._info

    @info.setter
    def info(self, info: "GrantaServerApiSchemaAttributesAttributeAttributeInfo") -> None:
        """Sets the info of this GrantaServerApiSchemaAttributesAttribute.

        Parameters
        ----------
        info: GrantaServerApiSchemaAttributesAttributeAttributeInfo
            The info of this GrantaServerApiSchemaAttributesAttribute.
        """
        self._info = info

    @property
    def display_names(self) -> "dict(str, str)":
        """Gets the display_names of this GrantaServerApiSchemaAttributesAttribute.

        Returns
        -------
        dict(str, str)
            The display_names of this GrantaServerApiSchemaAttributesAttribute.
        """
        return self._display_names

    @display_names.setter
    def display_names(self, display_names: "dict(str, str)") -> None:
        """Sets the display_names of this GrantaServerApiSchemaAttributesAttribute.

        Parameters
        ----------
        display_names: dict(str, str)
            The display_names of this GrantaServerApiSchemaAttributesAttribute.
        """
        self._display_names = display_names

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaAttributesAttribute.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaAttributesAttribute.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaAttributesAttribute.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaAttributesAttribute.
        """
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaAttributesAttribute.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaAttributesAttribute.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaAttributesAttribute.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaAttributesAttribute.
        """
        self._guid = guid

    def get_real_child_model(self, data: ModelBase) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[self._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen, 
        # so we have to extract it from the JSON reference
        return self.discriminator_value_class_map.get(discriminator_value).rsplit("/", 1)[-1]

    def _get_discriminator_field_name(self) -> str:
        name_tokens = self.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

    def to_dict(self) -> Dict:
        """Returns the model properties as a dict

        Returns
        -------
        Dict
            Dictionary indexed by property name containing all the model properties
        """
        result = {}

        for attr in self.swagger_types.keys():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GrantaServerApiSchemaAttributesAttribute, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model

        Returns
        -------
        str
            String representation of the model as a dictionary
        """
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiSchemaAttributesAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
