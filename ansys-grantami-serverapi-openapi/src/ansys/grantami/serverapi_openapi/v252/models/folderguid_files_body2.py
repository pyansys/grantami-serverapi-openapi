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


class FolderguidFilesBody2(ModelBase):
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
        "description": "str",
        "file": "str",
    }

    attribute_map: dict[str, str] = {
        "description": "description",
        "file": "file",
    }

    subtype_mapping: dict[str, str] = {
    }

    discriminator: Optional[str] = None

    def __init__(self, *, description: "Union[str, Unset_Type]" = Unset, file: "Union[Union[BinaryIO, pathlib.Path], Unset_Type]" = Unset,) -> None:
        """FolderguidFilesBody2 - a model defined in Swagger

        Parameters
        ----------
        description: str, optional
        file: Union[BinaryIO, pathlib.Path], optional
        """
        self._file: Union[Union[BinaryIO, pathlib.Path], Unset_Type] = Unset
        self._description: Union[str, Unset_Type] = Unset

        if file is not Unset:
            self.file = file
        if description is not Unset:
            self.description = description

    @property
    def file(self) -> "Union[Union[BinaryIO, pathlib.Path], Unset_Type]":
        """Gets the file of this FolderguidFilesBody2.

        Returns
        -------
        Union[Union[BinaryIO, pathlib.Path], Unset_Type]
            The file of this FolderguidFilesBody2.
        """
        return self._file

    @file.setter
    def file(self, file: "Union[Union[BinaryIO, pathlib.Path], Unset_Type]") -> None:
        """Sets the file of this FolderguidFilesBody2.

        Parameters
        ----------
        file: Union[Union[BinaryIO, pathlib.Path], Unset_Type]
            The file of this FolderguidFilesBody2.
        """
        # Field is not nullable
        if file is None:
            raise ValueError("Invalid value for 'file', must not be 'None'")
        self._file = file

    @property
    def description(self) -> "Union[str, Unset_Type]":
        """Gets the description of this FolderguidFilesBody2.

        Returns
        -------
        Union[str, Unset_Type]
            The description of this FolderguidFilesBody2.
        """
        return self._description

    @description.setter
    def description(self, description: "Union[str, Unset_Type]") -> None:
        """Sets the description of this FolderguidFilesBody2.

        Parameters
        ----------
        description: Union[str, Unset_Type]
            The description of this FolderguidFilesBody2.
        """
        # Field is not nullable
        if description is None:
            raise ValueError("Invalid value for 'description', must not be 'None'")
        self._description = description

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
        if not isinstance(other, FolderguidFilesBody2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

