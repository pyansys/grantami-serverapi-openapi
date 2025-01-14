"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaFilesInfo(ModelBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes
    ----------
    swagger_types: dict[str, str]
        The key is attribute name and the value is attribute type.
    attribute_map: dict[str, str]
        The key is attribute name and the value is json key in definition.
    subtype_mapping: dict[str, str]
        The key is the unmangled property name and the value is the corresponding type.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "files": "list[GsaSlimFile]",
    }

    attribute_map: dict[str, str] = {
        "files": "files",
    }

    subtype_mapping: dict[str, str] = {
        "files": "GsaSlimFile",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, files: "Union[list[GsaSlimFile], None, Unset_Type]" = Unset,) -> None:
        """GsaFilesInfo - a model defined in Swagger

        Parameters
        ----------
        files: list[GsaSlimFile], optional
        """
        self._files: Union[list[GsaSlimFile], None, Unset_Type] = Unset

        if files is not Unset:
            self.files = files

    @property
    def files(self) -> "Union[list[GsaSlimFile], None, Unset_Type]":
        """Gets the files of this GsaFilesInfo.

        Returns
        -------
        Union[list[GsaSlimFile], None, Unset_Type]
            The files of this GsaFilesInfo.
        """
        return self._files

    @files.setter
    def files(self, files: "Union[list[GsaSlimFile], None, Unset_Type]") -> None:
        """Sets the files of this GsaFilesInfo.

        Parameters
        ----------
        files: Union[list[GsaSlimFile], None, Unset_Type]
            The files of this GsaFilesInfo.
        """
        self._files = files

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
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
        if not isinstance(other, GsaFilesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

