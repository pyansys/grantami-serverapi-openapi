# coding: utf-8

"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from . import ModelBase

from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_properties_property import GrantaServerApiDataExportPropertiesProperty  # noqa: F401,E501

class GrantaServerApiDataExportPropertiesDatabaseKeyProperty(GrantaServerApiDataExportPropertiesProperty):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'property_name': 'str',
        'database_key': 'str'
    }
    if hasattr(GrantaServerApiDataExportPropertiesProperty, "swagger_types"):
        swagger_types.update(GrantaServerApiDataExportPropertiesProperty.swagger_types)

    attribute_map = {
        'property_name': 'propertyName',
        'database_key': 'databaseKey'
    }
    if hasattr(GrantaServerApiDataExportPropertiesProperty, "attribute_map"):
        attribute_map.update(GrantaServerApiDataExportPropertiesProperty.attribute_map)

    subtype_mapping = {
    }


    def __init__(self, property_name='databaseKey', database_key=None, *args, **kwargs):  # noqa: E501
        """GrantaServerApiDataExportPropertiesDatabaseKeyProperty - a model defined in Swagger"""  # noqa: E501
        self._property_name = None
        self._database_key = None
        self.discriminator = None
        self.property_name = property_name
        if database_key is not None:
            self.database_key = database_key
        GrantaServerApiDataExportPropertiesProperty.__init__(self, *args, **kwargs)

    @property
    def property_name(self):
        """Gets the property_name of this GrantaServerApiDataExportPropertiesDatabaseKeyProperty.  # noqa: E501

        :return: The property_name of this GrantaServerApiDataExportPropertiesDatabaseKeyProperty.  # noqa: E501
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """Sets the property_name of this GrantaServerApiDataExportPropertiesDatabaseKeyProperty.

        :param property_name: The property_name of this GrantaServerApiDataExportPropertiesDatabaseKeyProperty.  # noqa: E501
        :type: str
        """
        if property_name is None:
            raise ValueError("Invalid value for `property_name`, must not be `None`")  # noqa: E501
        self._property_name = property_name

    @property
    def database_key(self):
        """Gets the database_key of this GrantaServerApiDataExportPropertiesDatabaseKeyProperty.  # noqa: E501

        :return: The database_key of this GrantaServerApiDataExportPropertiesDatabaseKeyProperty.  # noqa: E501
        :rtype: str
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key):
        """Sets the database_key of this GrantaServerApiDataExportPropertiesDatabaseKeyProperty.

        :param database_key: The database_key of this GrantaServerApiDataExportPropertiesDatabaseKeyProperty.  # noqa: E501
        :type: str
        """
        self._database_key = database_key

    def get_real_child_model(self, data):
        """Raises a NotImplementedError for a type without a discriminator defined."""
        raise NotImplementedError()

    def to_dict(self):
        """Returns the model properties as a dict"""
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
        if issubclass(GrantaServerApiDataExportPropertiesDatabaseKeyProperty, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiDataExportPropertiesDatabaseKeyProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
