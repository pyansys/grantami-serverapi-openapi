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

from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_attributes_attribute import GrantaServerApiSchemaAttributesAttribute  # noqa: F401,E501

class GrantaServerApiSchemaAttributesFloatFunctionalAttribute(GrantaServerApiSchemaAttributesAttribute):
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
        'type': 'str',
        'unit': 'GrantaServerApiSchemaSlimEntitiesSlimUnit',
        'parameters': 'list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]'
    }
    if hasattr(GrantaServerApiSchemaAttributesAttribute, "swagger_types"):
        swagger_types.update(GrantaServerApiSchemaAttributesAttribute.swagger_types)

    attribute_map = {
        'type': 'type',
        'unit': 'unit',
        'parameters': 'parameters'
    }
    if hasattr(GrantaServerApiSchemaAttributesAttribute, "attribute_map"):
        attribute_map.update(GrantaServerApiSchemaAttributesAttribute.attribute_map)

    subtype_mapping = {
        'unit': 'GrantaServerApiSchemaSlimEntitiesSlimUnit',
        'parameters': 'GrantaServerApiSchemaSlimEntitiesSlimNamedEntity'
    }


    def __init__(self, type='floatFunctional', unit=None, parameters=None, *args, **kwargs):  # noqa: E501
        """GrantaServerApiSchemaAttributesFloatFunctionalAttribute - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._unit = None
        self._parameters = None
        self.discriminator = None
        self.type = type
        if unit is not None:
            self.unit = unit
        if parameters is not None:
            self.parameters = parameters
        GrantaServerApiSchemaAttributesAttribute.__init__(self, *args, **kwargs)

    @property
    def type(self):
        """Gets the type of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.  # noqa: E501

        :return: The type of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.

        :param type: The type of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type

    @property
    def unit(self):
        """Gets the unit of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.  # noqa: E501

        :return: The unit of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.  # noqa: E501
        :rtype: GrantaServerApiSchemaSlimEntitiesSlimUnit
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.

        :param unit: The unit of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.  # noqa: E501
        :type: GrantaServerApiSchemaSlimEntitiesSlimUnit
        """
        self._unit = unit

    @property
    def parameters(self):
        """Gets the parameters of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.  # noqa: E501

        :return: The parameters of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.  # noqa: E501
        :rtype: list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.

        :param parameters: The parameters of this GrantaServerApiSchemaAttributesFloatFunctionalAttribute.  # noqa: E501
        :type: list[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]
        """
        self._parameters = parameters

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
        if issubclass(GrantaServerApiSchemaAttributesFloatFunctionalAttribute, dict):
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
        if not isinstance(other, GrantaServerApiSchemaAttributesFloatFunctionalAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
