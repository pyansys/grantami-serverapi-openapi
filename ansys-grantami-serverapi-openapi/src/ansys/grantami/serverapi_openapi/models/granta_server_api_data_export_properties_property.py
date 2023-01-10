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


class GrantaServerApiDataExportPropertiesProperty(ModelBase):
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
        'createdByUser'.lower(): '#/components/schemas/GrantaServerApiDataExportPropertiesCreatedByUserProperty',
        'createdDate'.lower(): '#/components/schemas/GrantaServerApiDataExportPropertiesCreatedDateProperty',
        'databaseKey'.lower(): '#/components/schemas/GrantaServerApiDataExportPropertiesDatabaseKeyProperty',
        'fullName'.lower(): '#/components/schemas/GrantaServerApiDataExportPropertiesFullNameProperty',
        'lastModifiedDate'.lower(): '#/components/schemas/GrantaServerApiDataExportPropertiesLastModifiedDateProperty',
        'lastModifiedByUser'.lower(): '#/components/schemas/GrantaServerApiDataExportPropertiesLastModifiedByUserProperty',
        'recordColor'.lower(): '#/components/schemas/GrantaServerApiDataExportPropertiesRecordColorProperty',
        'recordGuid'.lower(): '#/components/schemas/GrantaServerApiDataExportPropertiesRecordGuidProperty',
        'recordIdentity'.lower(): '#/components/schemas/GrantaServerApiDataExportPropertiesRecordIdentityProperty',
        'recordHistoryGuid'.lower(): '#/components/schemas/GrantaServerApiDataExportPropertiesRecordHistoryGuidProperty',
        'recordHistoryIdentity'.lower(): '#/components/schemas/GrantaServerApiDataExportPropertiesRecordHistoryIdentityProperty',
        'recordType'.lower(): '#/components/schemas/GrantaServerApiDataExportPropertiesRecordTypeProperty',
        'releasedDate'.lower(): '#/components/schemas/GrantaServerApiDataExportPropertiesReleasedDateProperty',
        'shortName'.lower(): '#/components/schemas/GrantaServerApiDataExportPropertiesShortNameProperty',
        'tableGuid'.lower(): '#/components/schemas/GrantaServerApiDataExportPropertiesTableGuidProperty',
        'tableIdentity'.lower(): '#/components/schemas/GrantaServerApiDataExportPropertiesTableIdentityProperty',
        'tableName'.lower(): '#/components/schemas/GrantaServerApiDataExportPropertiesTableNameProperty',
        'versionNumber'.lower(): '#/components/schemas/GrantaServerApiDataExportPropertiesVersionNumberProperty',
        'versionState'.lower(): '#/components/schemas/GrantaServerApiDataExportPropertiesVersionStateProperty',
    }

    def __init__(self):  # noqa: E501
        """GrantaServerApiDataExportPropertiesProperty - a model defined in Swagger"""  # noqa: E501
        self.discriminator = 'property_name'


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
        if issubclass(GrantaServerApiDataExportPropertiesProperty, dict):
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
        if not isinstance(other, GrantaServerApiDataExportPropertiesProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
