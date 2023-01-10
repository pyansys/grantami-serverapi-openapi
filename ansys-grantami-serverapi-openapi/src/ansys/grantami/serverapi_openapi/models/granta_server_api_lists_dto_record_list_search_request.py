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


class GrantaServerApiListsDtoRecordListSearchRequest(ModelBase):
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
        'search_criterion': 'GrantaServerApiListsDtoListCriterion',
        'paging_options': 'GrantaServerApiListsDtoPagingOptions',
        'response_options': 'GrantaServerApiListsDtoResponseOptions'
    }

    attribute_map = {
        'search_criterion': 'searchCriterion',
        'paging_options': 'pagingOptions',
        'response_options': 'responseOptions'
    }

    subtype_mapping = {
        'searchCriterion': 'GrantaServerApiListsDtoListCriterion',
        'pagingOptions': 'GrantaServerApiListsDtoPagingOptions',
        'responseOptions': 'GrantaServerApiListsDtoResponseOptions'
    }


    def __init__(self, search_criterion=None, paging_options=None, response_options=None):  # noqa: E501
        """GrantaServerApiListsDtoRecordListSearchRequest - a model defined in Swagger"""  # noqa: E501
        self._search_criterion = None
        self._paging_options = None
        self._response_options = None
        self.discriminator = None
        if search_criterion is not None:
            self.search_criterion = search_criterion
        if paging_options is not None:
            self.paging_options = paging_options
        if response_options is not None:
            self.response_options = response_options

    @property
    def search_criterion(self):
        """Gets the search_criterion of this GrantaServerApiListsDtoRecordListSearchRequest.  # noqa: E501

        :return: The search_criterion of this GrantaServerApiListsDtoRecordListSearchRequest.  # noqa: E501
        :rtype: GrantaServerApiListsDtoListCriterion
        """
        return self._search_criterion

    @search_criterion.setter
    def search_criterion(self, search_criterion):
        """Sets the search_criterion of this GrantaServerApiListsDtoRecordListSearchRequest.

        :param search_criterion: The search_criterion of this GrantaServerApiListsDtoRecordListSearchRequest.  # noqa: E501
        :type: GrantaServerApiListsDtoListCriterion
        """
        self._search_criterion = search_criterion

    @property
    def paging_options(self):
        """Gets the paging_options of this GrantaServerApiListsDtoRecordListSearchRequest.  # noqa: E501

        :return: The paging_options of this GrantaServerApiListsDtoRecordListSearchRequest.  # noqa: E501
        :rtype: GrantaServerApiListsDtoPagingOptions
        """
        return self._paging_options

    @paging_options.setter
    def paging_options(self, paging_options):
        """Sets the paging_options of this GrantaServerApiListsDtoRecordListSearchRequest.

        :param paging_options: The paging_options of this GrantaServerApiListsDtoRecordListSearchRequest.  # noqa: E501
        :type: GrantaServerApiListsDtoPagingOptions
        """
        self._paging_options = paging_options

    @property
    def response_options(self):
        """Gets the response_options of this GrantaServerApiListsDtoRecordListSearchRequest.  # noqa: E501

        :return: The response_options of this GrantaServerApiListsDtoRecordListSearchRequest.  # noqa: E501
        :rtype: GrantaServerApiListsDtoResponseOptions
        """
        return self._response_options

    @response_options.setter
    def response_options(self, response_options):
        """Sets the response_options of this GrantaServerApiListsDtoRecordListSearchRequest.

        :param response_options: The response_options of this GrantaServerApiListsDtoRecordListSearchRequest.  # noqa: E501
        :type: GrantaServerApiListsDtoResponseOptions
        """
        self._response_options = response_options

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
        if issubclass(GrantaServerApiListsDtoRecordListSearchRequest, dict):
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
        if not isinstance(other, GrantaServerApiListsDtoRecordListSearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
