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


class GrantaServerApiSchemaConfigurationsCreateConfiguration(ModelBase):
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
        "value": "str",
        "description": "str",
        "guid": "str",
    }

    attribute_map = {
        "name": "name",
        "value": "value",
        "description": "description",
        "guid": "guid",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        name: "str",
        value: "str",
        description: "Optional[str]" = None,
        guid: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiSchemaConfigurationsCreateConfiguration - a model defined in Swagger

        Parameters
        ----------
            name: str
            value: str
            description: str, optional
            guid: str, optional
        """
        self._description = None
        self._value = None
        self._name = None
        self._guid = None

        if description is not None:
            self.description = description
        self.value = value
        self.name = name
        if guid is not None:
            self.guid = guid

    @property
    def description(self) -> "str":
        """Gets the description of this GrantaServerApiSchemaConfigurationsCreateConfiguration.

        Returns
        -------
        str
            The description of this GrantaServerApiSchemaConfigurationsCreateConfiguration.
        """
        return self._description

    @description.setter
    def description(self, description: "str") -> None:
        """Sets the description of this GrantaServerApiSchemaConfigurationsCreateConfiguration.

        Parameters
        ----------
        description: str
            The description of this GrantaServerApiSchemaConfigurationsCreateConfiguration.
        """
        self._description = description

    @property
    def value(self) -> "str":
        """Gets the value of this GrantaServerApiSchemaConfigurationsCreateConfiguration.

        Returns
        -------
        str
            The value of this GrantaServerApiSchemaConfigurationsCreateConfiguration.
        """
        return self._value

    @value.setter
    def value(self, value: "str") -> None:
        """Sets the value of this GrantaServerApiSchemaConfigurationsCreateConfiguration.

        Parameters
        ----------
        value: str
            The value of this GrantaServerApiSchemaConfigurationsCreateConfiguration.
        """
        if value is None:
            raise ValueError("Invalid value for 'value', must not be 'None'")
        self._value = value

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiSchemaConfigurationsCreateConfiguration.

        Returns
        -------
        str
            The name of this GrantaServerApiSchemaConfigurationsCreateConfiguration.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiSchemaConfigurationsCreateConfiguration.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiSchemaConfigurationsCreateConfiguration.
        """
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSchemaConfigurationsCreateConfiguration.

        Returns
        -------
        str
            The guid of this GrantaServerApiSchemaConfigurationsCreateConfiguration.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSchemaConfigurationsCreateConfiguration.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSchemaConfigurationsCreateConfiguration.
        """
        self._guid = guid

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
        if issubclass(GrantaServerApiSchemaConfigurationsCreateConfiguration, dict):
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
            other, GrantaServerApiSchemaConfigurationsCreateConfiguration
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
