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

from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_tabular_columns_tabular_column import GrantaServerApiSchemaTabularColumnsTabularColumn  # noqa: F401,E501

class GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn(GrantaServerApiSchemaTabularColumnsTabularColumn):
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
        'column_type': 'str',
        'default_threshold_type': 'GrantaServerApiSchemaAttributesAttributeThresholdType',
        'discrete_type': 'GrantaServerApiSchemaSlimEntitiesSlimNamedEntity'
    }
    if hasattr(GrantaServerApiSchemaTabularColumnsTabularColumn, "swagger_types"):
        swagger_types.update(GrantaServerApiSchemaTabularColumnsTabularColumn.swagger_types)

    attribute_map = {
        'column_type': 'columnType',
        'default_threshold_type': 'defaultThresholdType',
        'discrete_type': 'discreteType'
    }
    if hasattr(GrantaServerApiSchemaTabularColumnsTabularColumn, "attribute_map"):
        attribute_map.update(GrantaServerApiSchemaTabularColumnsTabularColumn.attribute_map)

    subtype_mapping = {
        'defaultThresholdType': 'GrantaServerApiSchemaAttributesAttributeThresholdType',
        'discreteType': 'GrantaServerApiSchemaSlimEntitiesSlimNamedEntity'
    }


    def __init__(self, column_type='localDiscrete', default_threshold_type=None, discrete_type=None, *args, **kwargs):  # noqa: E501
        """GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn - a model defined in Swagger"""  # noqa: E501
        GrantaServerApiSchemaTabularColumnsTabularColumn.__init__(self, *args, **kwargs)
        self._column_type = None
        self._default_threshold_type = None
        self._discrete_type = None
        self.discriminator = None
        self.column_type = column_type
        if default_threshold_type is not None:
            self.default_threshold_type = default_threshold_type
        if discrete_type is not None:
            self.discrete_type = discrete_type

    @property
    def column_type(self):
        """Gets the column_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.  # noqa: E501

        :return: The column_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.  # noqa: E501
        :rtype: str
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type):
        """Sets the column_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.

        :param column_type: The column_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.  # noqa: E501
        :type: str
        """
        if column_type is None:
            raise ValueError("Invalid value for `column_type`, must not be `None`")  # noqa: E501
        self._column_type = column_type

    @property
    def default_threshold_type(self):
        """Gets the default_threshold_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.  # noqa: E501

        :return: The default_threshold_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.  # noqa: E501
        :rtype: GrantaServerApiSchemaAttributesAttributeThresholdType
        """
        return self._default_threshold_type

    @default_threshold_type.setter
    def default_threshold_type(self, default_threshold_type):
        """Sets the default_threshold_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.

        :param default_threshold_type: The default_threshold_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.  # noqa: E501
        :type: GrantaServerApiSchemaAttributesAttributeThresholdType
        """
        self._default_threshold_type = default_threshold_type

    @property
    def discrete_type(self):
        """Gets the discrete_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.  # noqa: E501

        :return: The discrete_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.  # noqa: E501
        :rtype: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
        """
        return self._discrete_type

    @discrete_type.setter
    def discrete_type(self, discrete_type):
        """Sets the discrete_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.

        :param discrete_type: The discrete_type of this GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn.  # noqa: E501
        :type: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
        """
        self._discrete_type = discrete_type

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
        if issubclass(GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn, dict):
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
        if not isinstance(other, GrantaServerApiSchemaTabularColumnsLocalDiscreteTabularColumn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
