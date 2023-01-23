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


class GrantaServerApiExceptionsConstantDeletionException(ModelBase):
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
        'message': 'str',
        'code': 'SystemNetHttpStatusCode',
        'errors': 'list[GrantaServerApiExceptionsErrorDetail]'
    }

    attribute_map = {
        'message': 'message',
        'code': 'code',
        'errors': 'errors'
    }

    subtype_mapping = {
        'code': 'SystemNetHttpStatusCode',
        'errors': 'GrantaServerApiExceptionsErrorDetail'
    }


    def __init__(self, message=None, code=None, errors=None):  # noqa: E501
        """GrantaServerApiExceptionsConstantDeletionException - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self._code = None
        self._errors = None
        self.discriminator = None
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
        if errors is not None:
            self.errors = errors

    @property
    def message(self):
        """Gets the message of this GrantaServerApiExceptionsConstantDeletionException.  # noqa: E501

        :return: The message of this GrantaServerApiExceptionsConstantDeletionException.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this GrantaServerApiExceptionsConstantDeletionException.

        :param message: The message of this GrantaServerApiExceptionsConstantDeletionException.  # noqa: E501
        :type: str
        """
        self._message = message

    @property
    def code(self):
        """Gets the code of this GrantaServerApiExceptionsConstantDeletionException.  # noqa: E501

        :return: The code of this GrantaServerApiExceptionsConstantDeletionException.  # noqa: E501
        :rtype: SystemNetHttpStatusCode
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this GrantaServerApiExceptionsConstantDeletionException.

        :param code: The code of this GrantaServerApiExceptionsConstantDeletionException.  # noqa: E501
        :type: SystemNetHttpStatusCode
        """
        self._code = code

    @property
    def errors(self):
        """Gets the errors of this GrantaServerApiExceptionsConstantDeletionException.  # noqa: E501

        :return: The errors of this GrantaServerApiExceptionsConstantDeletionException.  # noqa: E501
        :rtype: list[GrantaServerApiExceptionsErrorDetail]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this GrantaServerApiExceptionsConstantDeletionException.

        :param errors: The errors of this GrantaServerApiExceptionsConstantDeletionException.  # noqa: E501
        :type: list[GrantaServerApiExceptionsErrorDetail]
        """
        self._errors = errors

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
        if issubclass(GrantaServerApiExceptionsConstantDeletionException, dict):
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
        if not isinstance(other, GrantaServerApiExceptionsConstantDeletionException):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
