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


class GrantaServerApiDataExportRecordWithData(ModelBase):
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
        'database_key': 'str',
        'record_history_identity': 'int',
        'data': 'list[GrantaServerApiDataExportDatumsDatum]',
        'properties': 'list[GrantaServerApiDataExportPropertiesProperty]'
    }

    attribute_map = {
        'database_key': 'databaseKey',
        'record_history_identity': 'recordHistoryIdentity',
        'data': 'data',
        'properties': 'properties'
    }

    subtype_mapping = {
        'data': 'GrantaServerApiDataExportDatumsDatum',
        'properties': 'GrantaServerApiDataExportPropertiesProperty'
    }


    def __init__(self, database_key=None, record_history_identity=None, data=None, properties=None):  # noqa: E501
        """GrantaServerApiDataExportRecordWithData - a model defined in Swagger"""  # noqa: E501
        self._database_key = None
        self._record_history_identity = None
        self._data = None
        self._properties = None
        self.discriminator = None
        if database_key is not None:
            self.database_key = database_key
        if record_history_identity is not None:
            self.record_history_identity = record_history_identity
        if data is not None:
            self.data = data
        if properties is not None:
            self.properties = properties

    @property
    def database_key(self):
        """Gets the database_key of this GrantaServerApiDataExportRecordWithData.  # noqa: E501

        :return: The database_key of this GrantaServerApiDataExportRecordWithData.  # noqa: E501
        :rtype: str
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key):
        """Sets the database_key of this GrantaServerApiDataExportRecordWithData.

        :param database_key: The database_key of this GrantaServerApiDataExportRecordWithData.  # noqa: E501
        :type: str
        """
        self._database_key = database_key

    @property
    def record_history_identity(self):
        """Gets the record_history_identity of this GrantaServerApiDataExportRecordWithData.  # noqa: E501

        :return: The record_history_identity of this GrantaServerApiDataExportRecordWithData.  # noqa: E501
        :rtype: int
        """
        return self._record_history_identity

    @record_history_identity.setter
    def record_history_identity(self, record_history_identity):
        """Sets the record_history_identity of this GrantaServerApiDataExportRecordWithData.

        :param record_history_identity: The record_history_identity of this GrantaServerApiDataExportRecordWithData.  # noqa: E501
        :type: int
        """
        self._record_history_identity = record_history_identity

    @property
    def data(self):
        """Gets the data of this GrantaServerApiDataExportRecordWithData.  # noqa: E501

        :return: The data of this GrantaServerApiDataExportRecordWithData.  # noqa: E501
        :rtype: list[GrantaServerApiDataExportDatumsDatum]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this GrantaServerApiDataExportRecordWithData.

        :param data: The data of this GrantaServerApiDataExportRecordWithData.  # noqa: E501
        :type: list[GrantaServerApiDataExportDatumsDatum]
        """
        self._data = data

    @property
    def properties(self):
        """Gets the properties of this GrantaServerApiDataExportRecordWithData.  # noqa: E501

        :return: The properties of this GrantaServerApiDataExportRecordWithData.  # noqa: E501
        :rtype: list[GrantaServerApiDataExportPropertiesProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this GrantaServerApiDataExportRecordWithData.

        :param properties: The properties of this GrantaServerApiDataExportRecordWithData.  # noqa: E501
        :type: list[GrantaServerApiDataExportPropertiesProperty]
        """
        self._properties = properties

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
        if issubclass(GrantaServerApiDataExportRecordWithData, dict):
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
        if not isinstance(other, GrantaServerApiDataExportRecordWithData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
