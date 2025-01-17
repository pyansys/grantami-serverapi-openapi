"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
    from . import *


class GrantaServerApiExceptionsAttributeDeletionException(ModelBase):
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
        "code": "SystemNetHttpStatusCode",
        "errors": "list[GrantaServerApiExceptionsErrorDetail]",
        "message": "str",
    }

    attribute_map = {
        "code": "code",
        "errors": "errors",
        "message": "message",
    }

    subtype_mapping = {
        "code": "SystemNetHttpStatusCode",
        "errors": "GrantaServerApiExceptionsErrorDetail",
    }

    discriminator = None

    def __init__(
        self,
        *,
        code: "Optional[SystemNetHttpStatusCode]" = None,
        errors: "Optional[List[GrantaServerApiExceptionsErrorDetail]]" = None,
        message: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiExceptionsAttributeDeletionException - a model defined in Swagger

        Parameters
        ----------
            code: SystemNetHttpStatusCode, optional
            errors: List[GrantaServerApiExceptionsErrorDetail], optional
            message: str, optional
        """
        self._message = None
        self._code = None
        self._errors = None

        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
        if errors is not None:
            self.errors = errors

    @property
    def message(self) -> "str":
        """Gets the message of this GrantaServerApiExceptionsAttributeDeletionException.

        Returns
        -------
        str
            The message of this GrantaServerApiExceptionsAttributeDeletionException.
        """
        return self._message

    @message.setter
    def message(self, message: "str") -> None:
        """Sets the message of this GrantaServerApiExceptionsAttributeDeletionException.

        Parameters
        ----------
        message: str
            The message of this GrantaServerApiExceptionsAttributeDeletionException.
        """
        self._message = message

    @property
    def code(self) -> "SystemNetHttpStatusCode":
        """Gets the code of this GrantaServerApiExceptionsAttributeDeletionException.

        Returns
        -------
        SystemNetHttpStatusCode
            The code of this GrantaServerApiExceptionsAttributeDeletionException.
        """
        return self._code

    @code.setter
    def code(self, code: "SystemNetHttpStatusCode") -> None:
        """Sets the code of this GrantaServerApiExceptionsAttributeDeletionException.

        Parameters
        ----------
        code: SystemNetHttpStatusCode
            The code of this GrantaServerApiExceptionsAttributeDeletionException.
        """
        self._code = code

    @property
    def errors(self) -> "list[GrantaServerApiExceptionsErrorDetail]":
        """Gets the errors of this GrantaServerApiExceptionsAttributeDeletionException.

        Returns
        -------
        list[GrantaServerApiExceptionsErrorDetail]
            The errors of this GrantaServerApiExceptionsAttributeDeletionException.
        """
        return self._errors

    @errors.setter
    def errors(self, errors: "list[GrantaServerApiExceptionsErrorDetail]") -> None:
        """Sets the errors of this GrantaServerApiExceptionsAttributeDeletionException.

        Parameters
        ----------
        errors: list[GrantaServerApiExceptionsErrorDetail]
            The errors of this GrantaServerApiExceptionsAttributeDeletionException.
        """
        self._errors = errors

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

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiExceptionsAttributeDeletionException):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
