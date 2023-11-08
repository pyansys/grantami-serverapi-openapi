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


class GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute(ModelBase):
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
    swagger_types = {
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "axis_name": "str",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "guid": "str",
        "help_path": "str",
        "name": "str",
    }

    attribute_map = {
        "about_attribute": "aboutAttribute",
        "axis_name": "axisName",
        "default_threshold_type": "defaultThresholdType",
        "guid": "guid",
        "help_path": "helpPath",
        "name": "name",
    }

    subtype_mapping = {
        "defaultThresholdType": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "aboutAttribute": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
    }

    discriminator_value_class_map = {
        "point".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesUpdateAttributesUpdatePointAttribute",
        "integer".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesUpdateAttributesUpdateIntegerAttribute",
        "range".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesUpdateAttributesUpdateRangeAttribute",
        "logical".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesUpdateAttributesUpdateLogicalAttribute",
        "shortText".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesUpdateAttributesUpdateShortTextAttribute",
        "longText".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesUpdateAttributesUpdateLongTextAttribute",
        "dateTime".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesUpdateAttributesUpdateDateTimeAttribute",
        "discrete".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteAttribute",
        "hyperlink".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesUpdateAttributesUpdateHyperlinkAttribute",
        "file".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesUpdateAttributesUpdateFileAttribute",
        "picture".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesUpdateAttributesUpdatePictureAttribute",
        "link".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesUpdateAttributesUpdateTabularAttribute",
        "floatFunctional".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesUpdateAttributesUpdateFloatFunctionalAttribute",
        "discreteFunctional".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteFunctionalAttribute",
        "mathsFunctional".lower(): "#/components/schemas/GrantaServerApiSchemaAttributesUpdateAttributesUpdateMathsFunctionalAttribute",
    }

    discriminator = "type"

    def __init__(
        self,
        *,
        about_attribute: "Optional[GrantaServerApiSchemaSlimEntitiesSlimEntity]" = None,
        axis_name: "Optional[str]" = None,
        default_threshold_type: "Optional[GrantaServerApiSchemaAttributesAttributeThresholdType]" = None,
        guid: "Optional[str]" = None,
        help_path: "Optional[str]" = None,
        name: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute - a model defined in Swagger

        Parameters
        ----------
            about_attribute: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
            axis_name: str, optional
            default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType, optional
            guid: str, optional
            help_path: str, optional
            name: str, optional
        """
        self._default_threshold_type = None
        self._axis_name = None
        self._help_path = None
        self._about_attribute = None
        self._name = None
        self._guid = None

        if default_threshold_type is not None:
            self.default_threshold_type = default_threshold_type
        if axis_name is not None:
            self.axis_name = axis_name
        if help_path is not None:
            self.help_path = help_path
        if about_attribute is not None:
            self.about_attribute = about_attribute
        if name is not None:
            self.name = name
        if guid is not None:
            self.guid = guid

    @property
    def default_threshold_type(
        self,
    ) -> "GrantaServerApiSchemaAttributesAttributeThresholdType":
        """Gets the default_threshold_type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.

        Returns
        -------
        GrantaServerApiSchemaAttributesAttributeThresholdType
            The default_threshold_type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.
        """
        return self._default_threshold_type

    @default_threshold_type.setter
    def default_threshold_type(
        self,
        default_threshold_type: "GrantaServerApiSchemaAttributesAttributeThresholdType",
    ) -> None:
        """Sets the default_threshold_type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.

        Parameters
        ----------
        default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType
            The default_threshold_type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.
        """
        self._default_threshold_type = default_threshold_type

    @property
    def axis_name(self) -> "str":
        """Gets the axis_name of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.

        Returns
        -------
        str
            The axis_name of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.
        """
        return self._axis_name

    @axis_name.setter
    def axis_name(self, axis_name: "str") -> None:
        """Sets the axis_name of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.

        Parameters
        ----------
        axis_name: str
            The axis_name of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.
        """
        self._axis_name = axis_name

    @property
    def help_path(self) -> "str":
        """Gets the help_path of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.

        Returns
        -------
        str
            The help_path of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.
        """
        return self._help_path

    @help_path.setter
    def help_path(self, help_path: "str") -> None:
        """Sets the help_path of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.

        Parameters
        ----------
        help_path: str
            The help_path of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.
        """
        self._help_path = help_path

    @property
    def about_attribute(self) -> "GrantaServerApiSchemaSlimEntitiesSlimEntity":
        """Gets the about_attribute of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimEntity
            The about_attribute of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.
        """
        return self._about_attribute

    @about_attribute.setter
    def about_attribute(
        self, about_attribute: "GrantaServerApiSchemaSlimEntitiesSlimEntity"
    ) -> None:
        """Sets the about_attribute of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.

        Parameters
        ----------
        about_attribute: GrantaServerApiSchemaSlimEntitiesSlimEntity
            The about_attribute of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.
        """
        self._about_attribute = about_attribute

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.
        """
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute.
        """
        self._guid = guid

    @classmethod
    def get_real_child_model(cls, data: ModelBase) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[cls._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen,
        # so we have to extract it from the JSON reference
        return cls.discriminator_value_class_map.get(discriminator_value).rsplit(
            "/", 1
        )[-1]

    @classmethod
    def _get_discriminator_field_name(cls) -> str:
        name_tokens = cls.discriminator.split("_")
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
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(
            GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute, dict
        ):
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
        if not isinstance(
            other, GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
