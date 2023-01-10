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


class GrantaServerApiAggregationsAggregationDatumCriterion(ModelBase):
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
    }

    attribute_map = {
    }

    subtype_mapping = {
    }

    discriminator_value_class_map = {
        'dateTime'.lower(): '#/components/schemas/GrantaServerApiAggregationsDateTimeAggregationDatumCriterion',
        'discreteText'.lower(): '#/components/schemas/GrantaServerApiAggregationsDiscreteTextAggregationDatumCriterion',
        'integer'.lower(): '#/components/schemas/GrantaServerApiAggregationsIntegerAggregationDatumCriterion',
        'point'.lower(): '#/components/schemas/GrantaServerApiAggregationsPointAggregationDatumCriterion',
        'range'.lower(): '#/components/schemas/GrantaServerApiAggregationsRangeAggregationDatumCriterion',
        'shortText'.lower(): '#/components/schemas/GrantaServerApiAggregationsShortTextAggregationDatumCriterion',
        'link'.lower(): '#/components/schemas/GrantaServerApiAggregationsLinkAggregationDatumCriterion',
    }

    def __init__(self):  # noqa: E501
        """GrantaServerApiAggregationsAggregationDatumCriterion - a model defined in Swagger"""  # noqa: E501
        self.discriminator = 'type'

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        # The actual class name is not available in swagger-codegen, 
        # so we have to extract it from the JSON reference
        return self.discriminator_value_class_map.get(discriminator_value).rsplit("/", 1)[-1]

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
        if issubclass(GrantaServerApiAggregationsAggregationDatumCriterion, dict):
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
        if not isinstance(other, GrantaServerApiAggregationsAggregationDatumCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
