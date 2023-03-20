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


class GrantaServerApiSchemaDataRulesInfo(ModelBase):
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
        'data_rules': 'list[GrantaServerApiSchemaDataRule]'
    }

    attribute_map = {
        'data_rules': 'dataRules'
    }

    subtype_mapping = {
        'dataRules': 'GrantaServerApiSchemaDataRule'
    }


    def __init__(self, data_rules=None):  # noqa: E501
        """GrantaServerApiSchemaDataRulesInfo - a model defined in Swagger"""  # noqa: E501
        self._data_rules = None
        self.discriminator = None
        if data_rules is not None:
            self.data_rules = data_rules

    @property
    def data_rules(self):
        """Gets the data_rules of this GrantaServerApiSchemaDataRulesInfo.  # noqa: E501

        :return: The data_rules of this GrantaServerApiSchemaDataRulesInfo.  # noqa: E501
        :rtype: list[GrantaServerApiSchemaDataRule]
        """
        return self._data_rules

    @data_rules.setter
    def data_rules(self, data_rules):
        """Sets the data_rules of this GrantaServerApiSchemaDataRulesInfo.

        :param data_rules: The data_rules of this GrantaServerApiSchemaDataRulesInfo.  # noqa: E501
        :type: list[GrantaServerApiSchemaDataRule]
        """
        self._data_rules = data_rules

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
        if issubclass(GrantaServerApiSchemaDataRulesInfo, dict):
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
        if not isinstance(other, GrantaServerApiSchemaDataRulesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
