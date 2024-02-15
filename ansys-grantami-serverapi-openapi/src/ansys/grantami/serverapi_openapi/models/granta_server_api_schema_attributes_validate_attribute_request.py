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
    Dict,
    List,
    BinaryIO,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaAttributesValidateAttributeRequest(ModelBase):  # type: ignore[misc]
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
        "record_history_guid": "str",
        "value": "str",
    }

    attribute_map: Dict[str, str] = {
        "record_history_guid": "recordHistoryGuid",
        "value": "value",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        record_history_guid: "Optional[str]" = None,
        value: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiSchemaAttributesValidateAttributeRequest - a model defined in Swagger

        Parameters
        ----------
            record_history_guid: str, optional
            value: str, optional
        """
        self._value = None
        self._record_history_guid = None

        if value is not None:
            self.value = value
        if record_history_guid is not None:
            self.record_history_guid = record_history_guid

    @property
    def value(self) -> "Optional[str]":
        """Gets the value of this GrantaServerApiSchemaAttributesValidateAttributeRequest.
        The value to check an attributes data validation rules against

        Returns
        -------
        str
            The value of this GrantaServerApiSchemaAttributesValidateAttributeRequest.
        """
        return self._value

    @value.setter
    def value(self, value: "Optional[str]") -> None:
        """Sets the value of this GrantaServerApiSchemaAttributesValidateAttributeRequest.
        The value to check an attributes data validation rules against

        Parameters
        ----------
        value: str
            The value of this GrantaServerApiSchemaAttributesValidateAttributeRequest.
        """
        self._value = value

    @property
    def record_history_guid(self) -> "Optional[str]":
        """Gets the record_history_guid of this GrantaServerApiSchemaAttributesValidateAttributeRequest.
        The record you want to check the value against to see if the value has changed as well as being valid

        Returns
        -------
        str
            The record_history_guid of this GrantaServerApiSchemaAttributesValidateAttributeRequest.
        """
        return self._record_history_guid

    @record_history_guid.setter
    def record_history_guid(self, record_history_guid: "Optional[str]") -> None:
        """Sets the record_history_guid of this GrantaServerApiSchemaAttributesValidateAttributeRequest.
        The record you want to check the value against to see if the value has changed as well as being valid

        Parameters
        ----------
        record_history_guid: str
            The record_history_guid of this GrantaServerApiSchemaAttributesValidateAttributeRequest.
        """
        self._record_history_guid = record_history_guid

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
        return self.to_str()  # type: ignore[no-any-return]

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(
            other, GrantaServerApiSchemaAttributesValidateAttributeRequest
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
