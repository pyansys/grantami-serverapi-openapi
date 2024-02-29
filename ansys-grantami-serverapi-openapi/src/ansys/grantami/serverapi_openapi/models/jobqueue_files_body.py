"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import (
    TYPE_CHECKING,
    Any,
    BinaryIO,
    Dict,
    List,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase, Unset, Unset_Type


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
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
    swagger_types: Dict[str, str] = {
        "file": "str",
    }

    attribute_map: Dict[str, str] = {
        "file": "file",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        file: "Union[Union[BinaryIO, pathlib.Path], Unset_Type]" = Unset,
    ) -> None:
        """JobqueueFilesBody - a model defined in Swagger

        Parameters
        ----------
        file: Union[BinaryIO, pathlib.Path], optional
        """
        self._file: Union[Union[BinaryIO, pathlib.Path], Unset_Type] = Unset

        if file is not Unset:
            self.file = file

    @property
    def file(self) -> "Union[Union[BinaryIO, pathlib.Path], Unset_Type]":
        """Gets the file of this JobqueueFilesBody.

        Returns
        -------
        Union[Union[BinaryIO, pathlib.Path], Unset_Type]
            The file of this JobqueueFilesBody.
        """
        return self._file

    @file.setter
    def file(self, file: "Union[Union[BinaryIO, pathlib.Path], Unset_Type]") -> None:
        """Sets the file of this JobqueueFilesBody.

        Parameters
        ----------
        file: Union[Union[BinaryIO, pathlib.Path], Unset_Type]
            The file of this JobqueueFilesBody.
        """
        # Field is not nullable
        if file is None:
            raise ValueError("Invalid value for 'file', must not be 'None'")
        self._file = file

    @classmethod
    def get_real_child_model(cls, data: Dict[str, str]) -> str:
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
