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


if TYPE_CHECKING:
    from . import *


class GrantaServerApiDataExportDatumsBinaryData(ModelBase):
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

    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types = {
        "content_type": "str",
        "data": "str",
        "description": "str",
        "name": "str",
    }

    attribute_map = {
        "content_type": "contentType",
        "data": "data",
        "description": "description",
        "name": "name",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        content_type: "Optional[str]" = None,
        data: "Optional[str]" = None,
        description: "Optional[str]" = None,
        name: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiDataExportDatumsBinaryData - a model defined in Swagger

        Parameters
        ----------
            content_type: str, optional
            data: str, optional
            description: str, optional
            name: str, optional
        """
        self._name = None
        self._description = None
        self._content_type = None
        self._data = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if content_type is not None:
            self.content_type = content_type
        if data is not None:
            self.data = data

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiDataExportDatumsBinaryData.

        Returns
        -------
        str
            The name of this GrantaServerApiDataExportDatumsBinaryData.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiDataExportDatumsBinaryData.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiDataExportDatumsBinaryData.
        """
        self._name = name

    @property
    def description(self) -> "str":
        """Gets the description of this GrantaServerApiDataExportDatumsBinaryData.

        Returns
        -------
        str
            The description of this GrantaServerApiDataExportDatumsBinaryData.
        """
        return self._description

    @description.setter
    def description(self, description: "str") -> None:
        """Sets the description of this GrantaServerApiDataExportDatumsBinaryData.

        Parameters
        ----------
        description: str
            The description of this GrantaServerApiDataExportDatumsBinaryData.
        """
        self._description = description

    @property
    def content_type(self) -> "str":
        """Gets the content_type of this GrantaServerApiDataExportDatumsBinaryData.

        Returns
        -------
        str
            The content_type of this GrantaServerApiDataExportDatumsBinaryData.
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type: "str") -> None:
        """Sets the content_type of this GrantaServerApiDataExportDatumsBinaryData.

        Parameters
        ----------
        content_type: str
            The content_type of this GrantaServerApiDataExportDatumsBinaryData.
        """
        self._content_type = content_type

    @property
    def data(self) -> "str":
        """Gets the data of this GrantaServerApiDataExportDatumsBinaryData.

        Returns
        -------
        str
            The data of this GrantaServerApiDataExportDatumsBinaryData.
        """
        return self._data

    @data.setter
    def data(self, data: "str") -> None:
        """Sets the data of this GrantaServerApiDataExportDatumsBinaryData.

        Parameters
        ----------
        data: str
            The data of this GrantaServerApiDataExportDatumsBinaryData.
        """
        self._data = data

    @classmethod
    def get_real_child_model(cls, data: ModelBase) -> str:
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
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(GrantaServerApiDataExportDatumsBinaryData, dict):
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
        if not isinstance(other, GrantaServerApiDataExportDatumsBinaryData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
