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

from ansys.grantami.serverapi_openapi.models.granta_server_api_aggregations_aggregation_criterion import GrantaServerApiAggregationsAggregationCriterion  # noqa: F401,E501

class GrantaServerApiAggregationsAttributeAggregationCriterion(GrantaServerApiAggregationsAggregationCriterion):
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
        'identity': 'int',
        'name': 'str',
        'is_meta_attribute': 'bool',
        'type': 'str'
    }
    if hasattr(GrantaServerApiAggregationsAggregationCriterion, "swagger_types"):
        swagger_types.update(GrantaServerApiAggregationsAggregationCriterion.swagger_types)

    attribute_map = {
        'identity': 'identity',
        'name': 'name',
        'is_meta_attribute': 'isMetaAttribute',
        'type': 'type'
    }
    if hasattr(GrantaServerApiAggregationsAggregationCriterion, "attribute_map"):
        attribute_map.update(GrantaServerApiAggregationsAggregationCriterion.attribute_map)

    subtype_mapping = {
    }

    discriminator_value_class_map = {
        'value'.lower(): '#/components/schemas/GrantaServerApiAggregationsAttributeAggregationValueCriterion',
        'exists'.lower(): '#/components/schemas/GrantaServerApiAggregationsAttributeAggregationExistsCriterion',
    }

    def __init__(self, identity=None, name=None, is_meta_attribute=None, type='attribute', *args, **kwargs):  # noqa: E501
        """GrantaServerApiAggregationsAttributeAggregationCriterion - a model defined in Swagger"""  # noqa: E501
        self._identity = None
        self._name = None
        self._is_meta_attribute = None
        self._type = None
        self.discriminator = 'attribute_aggregation_criterion_type'
        if identity is not None:
            self.identity = identity
        if name is not None:
            self.name = name
        if is_meta_attribute is not None:
            self.is_meta_attribute = is_meta_attribute
        self.type = type
        GrantaServerApiAggregationsAggregationCriterion.__init__(self, *args, **kwargs)

    @property
    def identity(self):
        """Gets the identity of this GrantaServerApiAggregationsAttributeAggregationCriterion.  # noqa: E501

        :return: The identity of this GrantaServerApiAggregationsAttributeAggregationCriterion.  # noqa: E501
        :rtype: int
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this GrantaServerApiAggregationsAttributeAggregationCriterion.

        :param identity: The identity of this GrantaServerApiAggregationsAttributeAggregationCriterion.  # noqa: E501
        :type: int
        """
        self._identity = identity

    @property
    def name(self):
        """Gets the name of this GrantaServerApiAggregationsAttributeAggregationCriterion.  # noqa: E501

        :return: The name of this GrantaServerApiAggregationsAttributeAggregationCriterion.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GrantaServerApiAggregationsAttributeAggregationCriterion.

        :param name: The name of this GrantaServerApiAggregationsAttributeAggregationCriterion.  # noqa: E501
        :type: str
        """
        self._name = name

    @property
    def is_meta_attribute(self):
        """Gets the is_meta_attribute of this GrantaServerApiAggregationsAttributeAggregationCriterion.  # noqa: E501

        :return: The is_meta_attribute of this GrantaServerApiAggregationsAttributeAggregationCriterion.  # noqa: E501
        :rtype: bool
        """
        return self._is_meta_attribute

    @is_meta_attribute.setter
    def is_meta_attribute(self, is_meta_attribute):
        """Sets the is_meta_attribute of this GrantaServerApiAggregationsAttributeAggregationCriterion.

        :param is_meta_attribute: The is_meta_attribute of this GrantaServerApiAggregationsAttributeAggregationCriterion.  # noqa: E501
        :type: bool
        """
        self._is_meta_attribute = is_meta_attribute

    @property
    def type(self):
        """Gets the type of this GrantaServerApiAggregationsAttributeAggregationCriterion.  # noqa: E501

        :return: The type of this GrantaServerApiAggregationsAttributeAggregationCriterion.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GrantaServerApiAggregationsAttributeAggregationCriterion.

        :param type: The type of this GrantaServerApiAggregationsAttributeAggregationCriterion.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type

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
        if issubclass(GrantaServerApiAggregationsAttributeAggregationCriterion, dict):
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
        if not isinstance(other, GrantaServerApiAggregationsAttributeAggregationCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
