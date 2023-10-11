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

from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_properties_property import GrantaServerApiDataExportPropertiesProperty  # noqa: F401

if TYPE_CHECKING:
    from . import *

class GrantaServerApiDataExportPropertiesCreatedByUserProperty(GrantaServerApiDataExportPropertiesProperty):
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
        "created_by_user": "str",
        "property_name": "str",
    }

    attribute_map = {
        "created_by_user": "createdByUser",
        "property_name": "propertyName",
    }

    subtype_mapping = {
    }

    def __init__(self, *, created_by_user: "Optional[str]" = None, property_name: "str" = 'createdByUser',) -> None:
        """GrantaServerApiDataExportPropertiesCreatedByUserProperty - a model defined in Swagger

        Parameters
        ----------
            created_by_user: str, optional
            property_name: str
        """
        super().__init__()
        self._property_name = None
        self._created_by_user = None
        self.discriminator = None
        self.property_name = property_name
        if created_by_user is not None:
            self.created_by_user = created_by_user

    @property
    def property_name(self) -> "str":
        """Gets the property_name of this GrantaServerApiDataExportPropertiesCreatedByUserProperty.

        Returns
        -------
        str
            The property_name of this GrantaServerApiDataExportPropertiesCreatedByUserProperty.
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name: "str") -> None:
        """Sets the property_name of this GrantaServerApiDataExportPropertiesCreatedByUserProperty.

        Parameters
        ----------
        property_name: str
            The property_name of this GrantaServerApiDataExportPropertiesCreatedByUserProperty.
        """
        if property_name is None:
            raise ValueError("Invalid value for 'property_name', must not be 'None'")
        self._property_name = property_name

    @property
    def created_by_user(self) -> "str":
        """Gets the created_by_user of this GrantaServerApiDataExportPropertiesCreatedByUserProperty.

        Returns
        -------
        str
            The created_by_user of this GrantaServerApiDataExportPropertiesCreatedByUserProperty.
        """
        return self._created_by_user

    @created_by_user.setter
    def created_by_user(self, created_by_user: "str") -> None:
        """Sets the created_by_user of this GrantaServerApiDataExportPropertiesCreatedByUserProperty.

        Parameters
        ----------
        created_by_user: str
            The created_by_user of this GrantaServerApiDataExportPropertiesCreatedByUserProperty.
        """
        self._created_by_user = created_by_user

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
        if issubclass(GrantaServerApiDataExportPropertiesCreatedByUserProperty, dict):
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
        if not isinstance(other, GrantaServerApiDataExportPropertiesCreatedByUserProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
