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
from ansys.grantami.serverapi_openapi.models.granta_server_api_search_criterion import (
    GrantaServerApiSearchCriterion,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSearchRecordAncestorCriterion(GrantaServerApiSearchCriterion):
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
        "ancestor_identity": "int",
        "direct_parent_only": "bool",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "ancestor_identity": "ancestorIdentity",
        "direct_parent_only": "directParentOnly",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        ancestor_identity: "Optional[int]" = None,
        direct_parent_only: "Optional[bool]" = None,
        type: "str" = "recordAncestor",
    ) -> None:
        """GrantaServerApiSearchRecordAncestorCriterion - a model defined in Swagger

        Parameters
        ----------
            ancestor_identity: int, optional
            direct_parent_only: bool, optional
            type: str
        """
        super().__init__()
        self._ancestor_identity = None
        self._direct_parent_only = None
        self._type: str = None  # type: ignore[assignment]

        if ancestor_identity is not None:
            self.ancestor_identity = ancestor_identity
        if direct_parent_only is not None:
            self.direct_parent_only = direct_parent_only
        self.type = type

    @property
    def ancestor_identity(self) -> "Optional[int]":
        """Gets the ancestor_identity of this GrantaServerApiSearchRecordAncestorCriterion.

        Returns
        -------
        int
            The ancestor_identity of this GrantaServerApiSearchRecordAncestorCriterion.
        """
        return self._ancestor_identity

    @ancestor_identity.setter
    def ancestor_identity(self, ancestor_identity: "Optional[int]") -> None:
        """Sets the ancestor_identity of this GrantaServerApiSearchRecordAncestorCriterion.

        Parameters
        ----------
        ancestor_identity: int
            The ancestor_identity of this GrantaServerApiSearchRecordAncestorCriterion.
        """
        self._ancestor_identity = ancestor_identity

    @property
    def direct_parent_only(self) -> "Optional[bool]":
        """Gets the direct_parent_only of this GrantaServerApiSearchRecordAncestorCriterion.

        Returns
        -------
        bool
            The direct_parent_only of this GrantaServerApiSearchRecordAncestorCriterion.
        """
        return self._direct_parent_only

    @direct_parent_only.setter
    def direct_parent_only(self, direct_parent_only: "Optional[bool]") -> None:
        """Sets the direct_parent_only of this GrantaServerApiSearchRecordAncestorCriterion.

        Parameters
        ----------
        direct_parent_only: bool
            The direct_parent_only of this GrantaServerApiSearchRecordAncestorCriterion.
        """
        self._direct_parent_only = direct_parent_only

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchRecordAncestorCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchRecordAncestorCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchRecordAncestorCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchRecordAncestorCriterion.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

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
        if not isinstance(other, GrantaServerApiSearchRecordAncestorCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
