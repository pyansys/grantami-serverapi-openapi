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


class GrantaServerApiSchemaDatabase(ModelBase):
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
        'author': 'str',
        'company': 'str',
        'notes': 'str',
        'currency_code': 'str',
        'is_access_controlled': 'bool',
        'key': 'str',
        'version_guid': 'str',
        'status': 'GrantaServerApiSchemaDatabaseStatus',
        'is_read_only': 'bool',
        'is_locked': 'bool',
        'index_in_sync': 'bool',
        'schema_version': 'str',
        'name': 'str',
        'guid': 'str'
    }

    attribute_map = {
        'author': 'author',
        'company': 'company',
        'notes': 'notes',
        'currency_code': 'currencyCode',
        'is_access_controlled': 'isAccessControlled',
        'key': 'key',
        'version_guid': 'versionGuid',
        'status': 'status',
        'is_read_only': 'isReadOnly',
        'is_locked': 'isLocked',
        'index_in_sync': 'indexInSync',
        'schema_version': 'schemaVersion',
        'name': 'name',
        'guid': 'guid'
    }

    subtype_mapping = {
        'status': 'GrantaServerApiSchemaDatabaseStatus',
    }


    def __init__(self, author=None, company=None, notes=None, currency_code=None, is_access_controlled=None, key=None, version_guid=None, status=None, is_read_only=None, is_locked=None, index_in_sync=None, schema_version=None, name=None, guid=None):  # noqa: E501
        """GrantaServerApiSchemaDatabase - a model defined in Swagger"""  # noqa: E501
        self._author = None
        self._company = None
        self._notes = None
        self._currency_code = None
        self._is_access_controlled = None
        self._key = None
        self._version_guid = None
        self._status = None
        self._is_read_only = None
        self._is_locked = None
        self._index_in_sync = None
        self._schema_version = None
        self._name = None
        self._guid = None
        self.discriminator = None
        if author is not None:
            self.author = author
        if company is not None:
            self.company = company
        if notes is not None:
            self.notes = notes
        if currency_code is not None:
            self.currency_code = currency_code
        if is_access_controlled is not None:
            self.is_access_controlled = is_access_controlled
        if key is not None:
            self.key = key
        if version_guid is not None:
            self.version_guid = version_guid
        if status is not None:
            self.status = status
        if is_read_only is not None:
            self.is_read_only = is_read_only
        if is_locked is not None:
            self.is_locked = is_locked
        if index_in_sync is not None:
            self.index_in_sync = index_in_sync
        if schema_version is not None:
            self.schema_version = schema_version
        if name is not None:
            self.name = name
        if guid is not None:
            self.guid = guid

    @property
    def author(self):
        """Gets the author of this GrantaServerApiSchemaDatabase.  # noqa: E501

        :return: The author of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this GrantaServerApiSchemaDatabase.

        :param author: The author of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :type: str
        """
        self._author = author

    @property
    def company(self):
        """Gets the company of this GrantaServerApiSchemaDatabase.  # noqa: E501

        :return: The company of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this GrantaServerApiSchemaDatabase.

        :param company: The company of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :type: str
        """
        self._company = company

    @property
    def notes(self):
        """Gets the notes of this GrantaServerApiSchemaDatabase.  # noqa: E501

        :return: The notes of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this GrantaServerApiSchemaDatabase.

        :param notes: The notes of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :type: str
        """
        self._notes = notes

    @property
    def currency_code(self):
        """Gets the currency_code of this GrantaServerApiSchemaDatabase.  # noqa: E501

        :return: The currency_code of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this GrantaServerApiSchemaDatabase.

        :param currency_code: The currency_code of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :type: str
        """
        self._currency_code = currency_code

    @property
    def is_access_controlled(self):
        """Gets the is_access_controlled of this GrantaServerApiSchemaDatabase.  # noqa: E501

        :return: The is_access_controlled of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :rtype: bool
        """
        return self._is_access_controlled

    @is_access_controlled.setter
    def is_access_controlled(self, is_access_controlled):
        """Sets the is_access_controlled of this GrantaServerApiSchemaDatabase.

        :param is_access_controlled: The is_access_controlled of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :type: bool
        """
        self._is_access_controlled = is_access_controlled

    @property
    def key(self):
        """Gets the key of this GrantaServerApiSchemaDatabase.  # noqa: E501

        :return: The key of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this GrantaServerApiSchemaDatabase.

        :param key: The key of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :type: str
        """
        self._key = key

    @property
    def version_guid(self):
        """Gets the version_guid of this GrantaServerApiSchemaDatabase.  # noqa: E501

        :return: The version_guid of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :rtype: str
        """
        return self._version_guid

    @version_guid.setter
    def version_guid(self, version_guid):
        """Sets the version_guid of this GrantaServerApiSchemaDatabase.

        :param version_guid: The version_guid of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :type: str
        """
        self._version_guid = version_guid

    @property
    def status(self):
        """Gets the status of this GrantaServerApiSchemaDatabase.  # noqa: E501

        :return: The status of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :rtype: GrantaServerApiSchemaDatabaseStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GrantaServerApiSchemaDatabase.

        :param status: The status of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :type: GrantaServerApiSchemaDatabaseStatus
        """
        self._status = status

    @property
    def is_read_only(self):
        """Gets the is_read_only of this GrantaServerApiSchemaDatabase.  # noqa: E501

        :return: The is_read_only of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :rtype: bool
        """
        return self._is_read_only

    @is_read_only.setter
    def is_read_only(self, is_read_only):
        """Sets the is_read_only of this GrantaServerApiSchemaDatabase.

        :param is_read_only: The is_read_only of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :type: bool
        """
        self._is_read_only = is_read_only

    @property
    def is_locked(self):
        """Gets the is_locked of this GrantaServerApiSchemaDatabase.  # noqa: E501

        :return: The is_locked of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :rtype: bool
        """
        return self._is_locked

    @is_locked.setter
    def is_locked(self, is_locked):
        """Sets the is_locked of this GrantaServerApiSchemaDatabase.

        :param is_locked: The is_locked of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :type: bool
        """
        self._is_locked = is_locked

    @property
    def index_in_sync(self):
        """Gets the index_in_sync of this GrantaServerApiSchemaDatabase.  # noqa: E501

        :return: The index_in_sync of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :rtype: bool
        """
        return self._index_in_sync

    @index_in_sync.setter
    def index_in_sync(self, index_in_sync):
        """Sets the index_in_sync of this GrantaServerApiSchemaDatabase.

        :param index_in_sync: The index_in_sync of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :type: bool
        """
        self._index_in_sync = index_in_sync

    @property
    def schema_version(self):
        """Gets the schema_version of this GrantaServerApiSchemaDatabase.  # noqa: E501

        :return: The schema_version of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :rtype: str
        """
        return self._schema_version

    @schema_version.setter
    def schema_version(self, schema_version):
        """Sets the schema_version of this GrantaServerApiSchemaDatabase.

        :param schema_version: The schema_version of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :type: str
        """
        self._schema_version = schema_version

    @property
    def name(self):
        """Gets the name of this GrantaServerApiSchemaDatabase.  # noqa: E501

        :return: The name of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GrantaServerApiSchemaDatabase.

        :param name: The name of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :type: str
        """
        self._name = name

    @property
    def guid(self):
        """Gets the guid of this GrantaServerApiSchemaDatabase.  # noqa: E501

        :return: The guid of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this GrantaServerApiSchemaDatabase.

        :param guid: The guid of this GrantaServerApiSchemaDatabase.  # noqa: E501
        :type: str
        """
        self._guid = guid

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
        if issubclass(GrantaServerApiSchemaDatabase, dict):
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
        if not isinstance(other, GrantaServerApiSchemaDatabase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
