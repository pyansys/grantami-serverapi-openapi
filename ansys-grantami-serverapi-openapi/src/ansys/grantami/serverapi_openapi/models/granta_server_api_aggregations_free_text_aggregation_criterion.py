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

class GrantaServerApiAggregationsFreeTextAggregationCriterion(GrantaServerApiAggregationsAggregationCriterion):
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
        'criterion_guid': 'str',
        'identities': 'list[int]',
        'number_of_terms': 'int',
        'prefix': 'str',
        'type': 'str'
    }
    if hasattr(GrantaServerApiAggregationsAggregationCriterion, "swagger_types"):
        swagger_types.update(GrantaServerApiAggregationsAggregationCriterion.swagger_types)

    attribute_map = {
        'criterion_guid': 'criterionGuid',
        'identities': 'identities',
        'number_of_terms': 'numberOfTerms',
        'prefix': 'prefix',
        'type': 'type'
    }
    if hasattr(GrantaServerApiAggregationsAggregationCriterion, "attribute_map"):
        attribute_map.update(GrantaServerApiAggregationsAggregationCriterion.attribute_map)

    subtype_mapping = {
    }


    def __init__(self, criterion_guid=None, identities=None, number_of_terms=None, prefix=None, type='text', *args, **kwargs):  # noqa: E501
        """GrantaServerApiAggregationsFreeTextAggregationCriterion - a model defined in Swagger"""  # noqa: E501
        GrantaServerApiAggregationsAggregationCriterion.__init__(self, *args, **kwargs)
        self._criterion_guid = None
        self._identities = None
        self._number_of_terms = None
        self._prefix = None
        self._type = None
        self.discriminator = None
        if criterion_guid is not None:
            self.criterion_guid = criterion_guid
        if identities is not None:
            self.identities = identities
        if number_of_terms is not None:
            self.number_of_terms = number_of_terms
        if prefix is not None:
            self.prefix = prefix
        self.type = type

    @property
    def criterion_guid(self):
        """Gets the criterion_guid of this GrantaServerApiAggregationsFreeTextAggregationCriterion.  # noqa: E501
        A GUID to identify this free-text criterion, so that its results can be determined in the output.  For each input free-text aggregation criterion, there will be a free-text aggregation in the output  with a matching GUID.  # noqa: E501

        :return: The criterion_guid of this GrantaServerApiAggregationsFreeTextAggregationCriterion.  # noqa: E501
        :rtype: str
        """
        return self._criterion_guid

    @criterion_guid.setter
    def criterion_guid(self, criterion_guid):
        """Sets the criterion_guid of this GrantaServerApiAggregationsFreeTextAggregationCriterion.
        A GUID to identify this free-text criterion, so that its results can be determined in the output.  For each input free-text aggregation criterion, there will be a free-text aggregation in the output  with a matching GUID.  # noqa: E501

        :param criterion_guid: The criterion_guid of this GrantaServerApiAggregationsFreeTextAggregationCriterion.  # noqa: E501
        :type: str
        """
        self._criterion_guid = criterion_guid

    @property
    def identities(self):
        """Gets the identities of this GrantaServerApiAggregationsFreeTextAggregationCriterion.  # noqa: E501

        :return: The identities of this GrantaServerApiAggregationsFreeTextAggregationCriterion.  # noqa: E501
        :rtype: list[int]
        """
        return self._identities

    @identities.setter
    def identities(self, identities):
        """Sets the identities of this GrantaServerApiAggregationsFreeTextAggregationCriterion.

        :param identities: The identities of this GrantaServerApiAggregationsFreeTextAggregationCriterion.  # noqa: E501
        :type: list[int]
        """
        self._identities = identities

    @property
    def number_of_terms(self):
        """Gets the number_of_terms of this GrantaServerApiAggregationsFreeTextAggregationCriterion.  # noqa: E501

        :return: The number_of_terms of this GrantaServerApiAggregationsFreeTextAggregationCriterion.  # noqa: E501
        :rtype: int
        """
        return self._number_of_terms

    @number_of_terms.setter
    def number_of_terms(self, number_of_terms):
        """Sets the number_of_terms of this GrantaServerApiAggregationsFreeTextAggregationCriterion.

        :param number_of_terms: The number_of_terms of this GrantaServerApiAggregationsFreeTextAggregationCriterion.  # noqa: E501
        :type: int
        """
        self._number_of_terms = number_of_terms

    @property
    def prefix(self):
        """Gets the prefix of this GrantaServerApiAggregationsFreeTextAggregationCriterion.  # noqa: E501

        :return: The prefix of this GrantaServerApiAggregationsFreeTextAggregationCriterion.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this GrantaServerApiAggregationsFreeTextAggregationCriterion.

        :param prefix: The prefix of this GrantaServerApiAggregationsFreeTextAggregationCriterion.  # noqa: E501
        :type: str
        """
        self._prefix = prefix

    @property
    def type(self):
        """Gets the type of this GrantaServerApiAggregationsFreeTextAggregationCriterion.  # noqa: E501

        :return: The type of this GrantaServerApiAggregationsFreeTextAggregationCriterion.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GrantaServerApiAggregationsFreeTextAggregationCriterion.

        :param type: The type of this GrantaServerApiAggregationsFreeTextAggregationCriterion.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self._type = type

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
        if issubclass(GrantaServerApiAggregationsFreeTextAggregationCriterion, dict):
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
        if not isinstance(other, GrantaServerApiAggregationsFreeTextAggregationCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
