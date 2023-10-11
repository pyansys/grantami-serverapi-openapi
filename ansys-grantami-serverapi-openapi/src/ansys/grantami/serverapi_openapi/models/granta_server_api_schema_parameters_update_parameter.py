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

class GrantaServerApiSchemaParametersUpdateParameter(ModelBase):
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
        "display_names": "dict(str, str)",
        "guid": "str",
        "help_path": "str",
        "name": "str",
    }

    attribute_map = {
        "display_names": "displayNames",
        "guid": "guid",
        "help_path": "helpPath",
        "name": "name",
    }

    subtype_mapping = {
    }

    discriminator_value_class_map = {
        "discrete".lower(): "#/components/schemas/GrantaServerApiSchemaParametersUpdateDiscreteParameter",
        "numeric".lower(): "#/components/schemas/GrantaServerApiSchemaParametersUpdateNumericParameter",
    }

    def __init__(self, *, display_names: "Optional[Dict[str, str]]" = None, guid: "Optional[str]" = None, help_path: "Optional[str]" = None, name: "Optional[str]" = None,) -> None:
        """GrantaServerApiSchemaParametersUpdateParameter - a model defined in Swagger

        Parameters
        ----------
            display_names: Dict[str, str], optional
            guid: str, optional
            help_path: str, optional
            name: str, optional
        """
        self._help_path = None
        self._display_names = None
        self._name = None
        self._guid = None
        self.discriminator = "type"
        if help_path is not None:
            self.help_path = help_path
        if display_names is not None:
            self.display_names = display_names
        if name is not None:
            self.name = name
        if guid is not None:
            self.guid = guid

    @property
    def help_path(self) -> "str":
        """Gets the help_path of this GrantaServerApiSchemaParametersUpdateParameter.

        Returns
        -------
        str
            The help_path of this GrantaServerApiSchemaParametersUpdateParameter.
        """
        return self._help_path

    @help_path.setter
    def help_path(self, help_path: "str") -> None:
        """Sets the help_path of this GrantaServerApiSchemaParametersUpdateParameter.

        Parameters
        ----------
        help_path: str
            The help_path of this GrantaServerApiSchemaParametersUpdateParameter.
        """
        self._help_path = help_path

    @property
    def display_names(self) -> "dict(str, str)":
        """Gets the display_names of this GrantaServerApiSchemaParametersUpdateParameter.

        Returns
        -------
        dict(str, str)
            The display_names of this GrantaServerApiSchemaParametersUpdateParameter.
        """
        return self._display_names

    @display_names.setter
    def display_names(self, display_names: "dict(str, str)") -> None:
        """Sets the display_names of this GrantaServerApiSchemaParametersUpdateParameter.

        Parameters
        ----------
        display_names: dict(str, str)
            The display_names of this GrantaServerApiSchemaParametersUpdateParameter.
        """
        self._display_names = display_names

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaParametersUpdateParameter.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaParametersUpdateParameter.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaParametersUpdateParameter.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaParametersUpdateParameter.
        """
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaParametersUpdateParameter.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaParametersUpdateParameter.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaParametersUpdateParameter.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaParametersUpdateParameter.
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
        if issubclass(GrantaServerApiSchemaParametersUpdateParameter, dict):
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
        if not isinstance(other, GrantaServerApiSchemaParametersUpdateParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
