"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase

from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_properties_property import GrantaServerApiDataExportPropertiesProperty  # noqa: F401

if TYPE_CHECKING:
    from . import *

class GrantaServerApiDataExportPropertiesRecordTypeProperty(GrantaServerApiDataExportPropertiesProperty):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes
    ----------
    swagger_types: Dict[str, str]
        The key is attribute name and the value is attribute type.
    attribute_map: Dict[str, str]
        The key is attribute name and the value is json key in definition.
    subtype_mapping: Dict[str, str]
        The key is the unmangled property name and the value is the corresponding type.

    """
    swagger_types = {
        "property_name": "str",
        "record_type": "GrantaServerApiRecordType",
    }

    attribute_map = {
        "property_name": "propertyName",
        "record_type": "recordType",
    }

    subtype_mapping = {
        "recordType": "GrantaServerApiRecordType",
    }

    def __init__(self, *, property_name: "str" = 'recordType', record_type: "Optional[GrantaServerApiRecordType]" = None,) -> None:
        """GrantaServerApiDataExportPropertiesRecordTypeProperty - a model defined in Swagger

        Parameters
        ----------
            property_name: str
            record_type: GrantaServerApiRecordType, optional
        """
        super().__init__()
        self._property_name = None
        self._record_type = None
        self.discriminator = None
        self.property_name = property_name
        if record_type is not None:
            self.record_type = record_type

    @property
    def property_name(self) -> "str":
        """Gets the property_name of this GrantaServerApiDataExportPropertiesRecordTypeProperty.

        Returns
        -------
        str
            The property_name of this GrantaServerApiDataExportPropertiesRecordTypeProperty.
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name: "str") -> None:
        """Sets the property_name of this GrantaServerApiDataExportPropertiesRecordTypeProperty.

        Parameters
        ----------
        property_name: str
            The property_name of this GrantaServerApiDataExportPropertiesRecordTypeProperty.
        """
        if property_name is None:
            raise ValueError("Invalid value for 'property_name', must not be 'None'")
        self._property_name = property_name

    @property
    def record_type(self) -> "GrantaServerApiRecordType":
        """Gets the record_type of this GrantaServerApiDataExportPropertiesRecordTypeProperty.

        Returns
        -------
        GrantaServerApiRecordType
            The record_type of this GrantaServerApiDataExportPropertiesRecordTypeProperty.
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type: "GrantaServerApiRecordType") -> None:
        """Sets the record_type of this GrantaServerApiDataExportPropertiesRecordTypeProperty.

        Parameters
        ----------
        record_type: GrantaServerApiRecordType
            The record_type of this GrantaServerApiDataExportPropertiesRecordTypeProperty.
        """
        self._record_type = record_type

    def get_real_child_model(self, data: ModelBase) -> str:
        """Raises a NotImplementedError for a type without a discriminator defined.

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class

        Raises
        ------
        NotImplementedError
            This class has no discriminator, and hence no subclasses
        """
        raise NotImplementedError()

    def to_dict(self) -> Dict:
        """Returns the model properties as a dict

        Returns
        -------
        Dict
            Dictionary indexed by property name containing all the model properties
        """
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
        if issubclass(GrantaServerApiDataExportPropertiesRecordTypeProperty, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model

        Returns
        -------
        str
            String representation of the model as a dictionary
        """
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiDataExportPropertiesRecordTypeProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
