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


class JobqueueFilesBody(ModelBase):
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
        "content_disposition": "str",
        "content_type": "str",
        "file_name": "str",
        "headers": "dict(str, list[str])",
        "length": "int",
        "name": "str",
    }

    attribute_map = {
        "content_disposition": "ContentDisposition",
        "content_type": "ContentType",
        "file_name": "FileName",
        "headers": "Headers",
        "length": "Length",
        "name": "Name",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        content_disposition: "Optional[str]" = None,
        content_type: "Optional[str]" = None,
        file_name: "Optional[str]" = None,
        headers: "Optional[Dict[str, List[str]]]" = None,
        length: "Optional[int]" = None,
        name: "Optional[str]" = None,
    ) -> None:
        """JobqueueFilesBody - a model defined in Swagger

        Parameters
        ----------
            content_disposition: str, optional
            content_type: str, optional
            file_name: str, optional
            headers: Dict[str, List[str]], optional
            length: int, optional
            name: str, optional
        """
        self._content_type = None
        self._content_disposition = None
        self._headers = None
        self._length = None
        self._name = None
        self._file_name = None

        if content_type is not None:
            self.content_type = content_type
        if content_disposition is not None:
            self.content_disposition = content_disposition
        if headers is not None:
            self.headers = headers
        if length is not None:
            self.length = length
        if name is not None:
            self.name = name
        if file_name is not None:
            self.file_name = file_name

    @property
    def content_type(self) -> "str":
        """Gets the content_type of this JobqueueFilesBody.

        Returns
        -------
        str
            The content_type of this JobqueueFilesBody.
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type: "str") -> None:
        """Sets the content_type of this JobqueueFilesBody.

        Parameters
        ----------
        content_type: str
            The content_type of this JobqueueFilesBody.
        """
        self._content_type = content_type

    @property
    def content_disposition(self) -> "str":
        """Gets the content_disposition of this JobqueueFilesBody.

        Returns
        -------
        str
            The content_disposition of this JobqueueFilesBody.
        """
        return self._content_disposition

    @content_disposition.setter
    def content_disposition(self, content_disposition: "str") -> None:
        """Sets the content_disposition of this JobqueueFilesBody.

        Parameters
        ----------
        content_disposition: str
            The content_disposition of this JobqueueFilesBody.
        """
        self._content_disposition = content_disposition

    @property
    def headers(self) -> "dict(str, list[str])":
        """Gets the headers of this JobqueueFilesBody.

        Returns
        -------
        dict(str, list[str])
            The headers of this JobqueueFilesBody.
        """
        return self._headers

    @headers.setter
    def headers(self, headers: "dict(str, list[str])") -> None:
        """Sets the headers of this JobqueueFilesBody.

        Parameters
        ----------
        headers: dict(str, list[str])
            The headers of this JobqueueFilesBody.
        """
        self._headers = headers

    @property
    def length(self) -> "int":
        """Gets the length of this JobqueueFilesBody.

        Returns
        -------
        int
            The length of this JobqueueFilesBody.
        """
        return self._length

    @length.setter
    def length(self, length: "int") -> None:
        """Sets the length of this JobqueueFilesBody.

        Parameters
        ----------
        length: int
            The length of this JobqueueFilesBody.
        """
        self._length = length

    @property
    def name(self) -> "str":
        """Gets the name of this JobqueueFilesBody.

        Returns
        -------
        str
            The name of this JobqueueFilesBody.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this JobqueueFilesBody.

        Parameters
        ----------
        name: str
            The name of this JobqueueFilesBody.
        """
        self._name = name

    @property
    def file_name(self) -> "str":
        """Gets the file_name of this JobqueueFilesBody.

        Returns
        -------
        str
            The file_name of this JobqueueFilesBody.
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name: "str") -> None:
        """Sets the file_name of this JobqueueFilesBody.

        Parameters
        ----------
        file_name: str
            The file_name of this JobqueueFilesBody.
        """
        self._file_name = file_name

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
        if issubclass(JobqueueFilesBody, dict):
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
        if not isinstance(other, JobqueueFilesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
