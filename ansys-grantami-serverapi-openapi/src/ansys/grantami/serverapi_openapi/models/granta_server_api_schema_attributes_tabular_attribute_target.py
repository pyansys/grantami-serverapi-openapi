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

class GrantaServerApiSchemaAttributesTabularAttributeTarget(ModelBase):
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

    """
    swagger_types = {
        "target_attribute_guid": "str",
        "target_database_guid": "str",
        "target_database_version_guid": "str",
        "target_table_guid": "str",
    }

    attribute_map = {
        "target_attribute_guid": "targetAttributeGuid",
        "target_database_guid": "targetDatabaseGuid",
        "target_database_version_guid": "targetDatabaseVersionGuid",
        "target_table_guid": "targetTableGuid",
    }

    subtype_mapping = {
    }

    def __init__(self, *, target_attribute_guid: "Optional[str]" = None, target_database_guid: "Optional[str]" = None, target_database_version_guid: "Optional[str]" = None, target_table_guid: "Optional[str]" = None,) -> None:
        """GrantaServerApiSchemaAttributesTabularAttributeTarget - a model defined in Swagger

        Parameters
        ----------
            target_attribute_guid: str, optional
            target_database_guid: str, optional
            target_database_version_guid: str, optional
            target_table_guid: str, optional
        """
        self._target_database_guid = None
        self._target_database_version_guid = None
        self._target_table_guid = None
        self._target_attribute_guid = None
        self.discriminator = None
        if target_database_guid is not None:
            self.target_database_guid = target_database_guid
        if target_database_version_guid is not None:
            self.target_database_version_guid = target_database_version_guid
        if target_table_guid is not None:
            self.target_table_guid = target_table_guid
        if target_attribute_guid is not None:
            self.target_attribute_guid = target_attribute_guid

    @property
    def target_database_guid(self) -> "str":
        """Gets the target_database_guid of this GrantaServerApiSchemaAttributesTabularAttributeTarget.

        Returns
        -------
        str
            The target_database_guid of this GrantaServerApiSchemaAttributesTabularAttributeTarget.
        """
        return self._target_database_guid

    @target_database_guid.setter
    def target_database_guid(self, target_database_guid: "str") -> None:
        """Sets the target_database_guid of this GrantaServerApiSchemaAttributesTabularAttributeTarget.

        Parameters
        ----------
        target_database_guid: str
            The target_database_guid of this GrantaServerApiSchemaAttributesTabularAttributeTarget.
        """
        self._target_database_guid = target_database_guid

    @property
    def target_database_version_guid(self) -> "str":
        """Gets the target_database_version_guid of this GrantaServerApiSchemaAttributesTabularAttributeTarget.

        Returns
        -------
        str
            The target_database_version_guid of this GrantaServerApiSchemaAttributesTabularAttributeTarget.
        """
        return self._target_database_version_guid

    @target_database_version_guid.setter
    def target_database_version_guid(self, target_database_version_guid: "str") -> None:
        """Sets the target_database_version_guid of this GrantaServerApiSchemaAttributesTabularAttributeTarget.

        Parameters
        ----------
        target_database_version_guid: str
            The target_database_version_guid of this GrantaServerApiSchemaAttributesTabularAttributeTarget.
        """
        self._target_database_version_guid = target_database_version_guid

    @property
    def target_table_guid(self) -> "str":
        """Gets the target_table_guid of this GrantaServerApiSchemaAttributesTabularAttributeTarget.

        Returns
        -------
        str
            The target_table_guid of this GrantaServerApiSchemaAttributesTabularAttributeTarget.
        """
        return self._target_table_guid

    @target_table_guid.setter
    def target_table_guid(self, target_table_guid: "str") -> None:
        """Sets the target_table_guid of this GrantaServerApiSchemaAttributesTabularAttributeTarget.

        Parameters
        ----------
        target_table_guid: str
            The target_table_guid of this GrantaServerApiSchemaAttributesTabularAttributeTarget.
        """
        self._target_table_guid = target_table_guid

    @property
    def target_attribute_guid(self) -> "str":
        """Gets the target_attribute_guid of this GrantaServerApiSchemaAttributesTabularAttributeTarget.

        Returns
        -------
        str
            The target_attribute_guid of this GrantaServerApiSchemaAttributesTabularAttributeTarget.
        """
        return self._target_attribute_guid

    @target_attribute_guid.setter
    def target_attribute_guid(self, target_attribute_guid: "str") -> None:
        """Sets the target_attribute_guid of this GrantaServerApiSchemaAttributesTabularAttributeTarget.

        Parameters
        ----------
        target_attribute_guid: str
            The target_attribute_guid of this GrantaServerApiSchemaAttributesTabularAttributeTarget.
        """
        self._target_attribute_guid = target_attribute_guid

    def get_real_child_model(self, data: ModelBase) -> str:
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
        if issubclass(GrantaServerApiSchemaAttributesTabularAttributeTarget, dict):
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
        if not isinstance(other, GrantaServerApiSchemaAttributesTabularAttributeTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
