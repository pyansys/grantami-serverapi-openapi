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
from ansys.grantami.serverapi_openapi.models.granta_server_api_search_criterion import (
    GrantaServerApiSearchCriterion,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSearchRecordPropertyCriterion(GrantaServerApiSearchCriterion):
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
        "_property": "GrantaServerApiSearchSearchableRecordProperty",
        "inner_criterion": "GrantaServerApiSearchDatumCriterion",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "_property": "property",
        "inner_criterion": "innerCriterion",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {
        "property": "GrantaServerApiSearchSearchableRecordProperty",
        "innerCriterion": "GrantaServerApiSearchDatumCriterion",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        _property: "Union[GrantaServerApiSearchSearchableRecordProperty, Unset_Type]" = Unset,
        inner_criterion: "Union[GrantaServerApiSearchDatumCriterion, Unset_Type]" = Unset,
        type: "str" = "recordProperty",
    ) -> None:
        """GrantaServerApiSearchRecordPropertyCriterion - a model defined in Swagger

        Parameters
        ----------
        _property: GrantaServerApiSearchSearchableRecordProperty, optional
        inner_criterion: GrantaServerApiSearchDatumCriterion, optional
        type: str
        """
        super().__init__()
        self.__property: Union[
            GrantaServerApiSearchSearchableRecordProperty, Unset_Type
        ] = Unset
        self._inner_criterion: Union[
            GrantaServerApiSearchDatumCriterion, Unset_Type
        ] = Unset
        self._type: str

        if _property is not Unset:
            self._property = _property
        if inner_criterion is not Unset:
            self.inner_criterion = inner_criterion
        self.type = type

    @property
    def _property(
        self,
    ) -> "Union[GrantaServerApiSearchSearchableRecordProperty, Unset_Type]":
        """Gets the _property of this GrantaServerApiSearchRecordPropertyCriterion.

        Returns
        -------
        Union[GrantaServerApiSearchSearchableRecordProperty, Unset_Type]
            The _property of this GrantaServerApiSearchRecordPropertyCriterion.
        """
        return self.__property

    @_property.setter
    def _property(
        self,
        _property: "Union[GrantaServerApiSearchSearchableRecordProperty, Unset_Type]",
    ) -> None:
        """Sets the _property of this GrantaServerApiSearchRecordPropertyCriterion.

        Parameters
        ----------
        _property: Union[GrantaServerApiSearchSearchableRecordProperty, Unset_Type]
            The _property of this GrantaServerApiSearchRecordPropertyCriterion.
        """
        # Field is not nullable
        if _property is None:
            raise ValueError("Invalid value for '_property', must not be 'None'")
        self.__property = _property

    @property
    def inner_criterion(
        self,
    ) -> "Union[GrantaServerApiSearchDatumCriterion, Unset_Type]":
        """Gets the inner_criterion of this GrantaServerApiSearchRecordPropertyCriterion.

        Returns
        -------
        Union[GrantaServerApiSearchDatumCriterion, Unset_Type]
            The inner_criterion of this GrantaServerApiSearchRecordPropertyCriterion.
        """
        return self._inner_criterion

    @inner_criterion.setter
    def inner_criterion(
        self, inner_criterion: "Union[GrantaServerApiSearchDatumCriterion, Unset_Type]"
    ) -> None:
        """Sets the inner_criterion of this GrantaServerApiSearchRecordPropertyCriterion.

        Parameters
        ----------
        inner_criterion: Union[GrantaServerApiSearchDatumCriterion, Unset_Type]
            The inner_criterion of this GrantaServerApiSearchRecordPropertyCriterion.
        """
        # Field is not nullable
        if inner_criterion is None:
            raise ValueError("Invalid value for 'inner_criterion', must not be 'None'")
        self._inner_criterion = inner_criterion

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchRecordPropertyCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchRecordPropertyCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchRecordPropertyCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchRecordPropertyCriterion.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

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
        if not isinstance(other, GrantaServerApiSearchRecordPropertyCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
