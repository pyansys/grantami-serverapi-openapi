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


class GrantaServerApiSchemaSubsetsAddRecordHistoryToSubset(ModelBase):
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
        "recurse_children": "bool",
    }

    attribute_map: Dict[str, str] = {
        "record_history_guid": "recordHistoryGuid",
        "recurse_children": "recurseChildren",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        record_history_guid: "str",
        recurse_children: "Union[bool, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaSubsetsAddRecordHistoryToSubset - a model defined in Swagger

        Parameters
        ----------
        record_history_guid: str
        recurse_children: bool, optional
        """
        self._record_history_guid: str
        self._recurse_children: Union[bool, Unset_Type] = Unset

        self.record_history_guid = record_history_guid
        if recurse_children is not Unset:
            self.recurse_children = recurse_children

    @property
    def record_history_guid(self) -> "str":
        """Gets the record_history_guid of this GrantaServerApiSchemaSubsetsAddRecordHistoryToSubset.

        Returns
        -------
        str
            The record_history_guid of this GrantaServerApiSchemaSubsetsAddRecordHistoryToSubset.
        """
        return self._record_history_guid

    @record_history_guid.setter
    def record_history_guid(self, record_history_guid: "str") -> None:
        """Sets the record_history_guid of this GrantaServerApiSchemaSubsetsAddRecordHistoryToSubset.

        Parameters
        ----------
        record_history_guid: str
            The record_history_guid of this GrantaServerApiSchemaSubsetsAddRecordHistoryToSubset.
        """
        # Field is not nullable
        if record_history_guid is None:
            raise ValueError(
                "Invalid value for 'record_history_guid', must not be 'None'"
            )
        # Field is required
        if record_history_guid is Unset:  # type: ignore[comparison-overlap]
            raise ValueError(
                "Invalid value for 'record_history_guid', must not be 'Unset'"
            )
        self._record_history_guid = record_history_guid

    @property
    def recurse_children(self) -> "Union[bool, Unset_Type]":
        """Gets the recurse_children of this GrantaServerApiSchemaSubsetsAddRecordHistoryToSubset.

        Returns
        -------
        Union[bool, Unset_Type]
            The recurse_children of this GrantaServerApiSchemaSubsetsAddRecordHistoryToSubset.
        """
        return self._recurse_children

    @recurse_children.setter
    def recurse_children(self, recurse_children: "Union[bool, Unset_Type]") -> None:
        """Sets the recurse_children of this GrantaServerApiSchemaSubsetsAddRecordHistoryToSubset.

        Parameters
        ----------
        recurse_children: Union[bool, Unset_Type]
            The recurse_children of this GrantaServerApiSchemaSubsetsAddRecordHistoryToSubset.
        """
        # Field is not nullable
        if recurse_children is None:
            raise ValueError("Invalid value for 'recurse_children', must not be 'None'")
        self._recurse_children = recurse_children

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
        if not isinstance(other, GrantaServerApiSchemaSubsetsAddRecordHistoryToSubset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
