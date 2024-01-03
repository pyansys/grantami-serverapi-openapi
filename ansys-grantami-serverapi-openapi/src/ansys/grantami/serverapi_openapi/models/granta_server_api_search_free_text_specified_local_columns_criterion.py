"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase
from ansys.grantami.serverapi_openapi.models.granta_server_api_search_free_text_criterion import (
    GrantaServerApiSearchFreeTextCriterion,
)  # noqa: F401


if TYPE_CHECKING:
    from . import *


class GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion(
    GrantaServerApiSearchFreeTextCriterion
):
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
        "column_guids": "list[str]",
        "column_guids_to_boost": "list[GrantaServerApiSearchBoostByGuid]",
        "column_identities": "list[int]",
        "column_identities_to_boost": "list[GrantaServerApiSearchBoostByIdentity]",
        "free_text_criterion_type": "str",
        "type": "str",
        "value": "str",
    }

    attribute_map = {
        "column_guids": "columnGuids",
        "column_guids_to_boost": "columnGuidsToBoost",
        "column_identities": "columnIdentities",
        "column_identities_to_boost": "columnIdentitiesToBoost",
        "free_text_criterion_type": "freeTextCriterionType",
        "type": "type",
        "value": "value",
    }

    subtype_mapping = {
        "columnIdentitiesToBoost": "GrantaServerApiSearchBoostByIdentity",
        "columnGuidsToBoost": "GrantaServerApiSearchBoostByGuid",
    }

    discriminator = None

    def __init__(
        self,
        *,
        column_guids: "Optional[List[str]]" = None,
        column_guids_to_boost: "Optional[List[GrantaServerApiSearchBoostByGuid]]" = None,
        column_identities: "Optional[List[int]]" = None,
        column_identities_to_boost: "Optional[List[GrantaServerApiSearchBoostByIdentity]]" = None,
        free_text_criterion_type: "str" = "specifiedLocalColumns",
        type: "str" = "text",
        value: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion - a model defined in Swagger

        Parameters
        ----------
            column_guids: List[str], optional
            column_guids_to_boost: List[GrantaServerApiSearchBoostByGuid], optional
            column_identities: List[int], optional
            column_identities_to_boost: List[GrantaServerApiSearchBoostByIdentity], optional
            free_text_criterion_type: str
            type: str
            value: str, optional
        """
        super().__init__(type=type, value=value)
        self._column_identities = None
        self._column_identities_to_boost = None
        self._column_guids = None
        self._column_guids_to_boost = None
        self._free_text_criterion_type = None

        if column_identities is not None:
            self.column_identities = column_identities
        if column_identities_to_boost is not None:
            self.column_identities_to_boost = column_identities_to_boost
        if column_guids is not None:
            self.column_guids = column_guids
        if column_guids_to_boost is not None:
            self.column_guids_to_boost = column_guids_to_boost
        self.free_text_criterion_type = free_text_criterion_type

    @property
    def column_identities(self) -> "list[int]":
        """Gets the column_identities of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.

        Returns
        -------
        list[int]
            The column_identities of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.
        """
        return self._column_identities

    @column_identities.setter
    def column_identities(self, column_identities: "list[int]") -> None:
        """Sets the column_identities of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.

        Parameters
        ----------
        column_identities: list[int]
            The column_identities of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.
        """
        self._column_identities = column_identities

    @property
    def column_identities_to_boost(
        self,
    ) -> "list[GrantaServerApiSearchBoostByIdentity]":
        """Gets the column_identities_to_boost of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.

        Returns
        -------
        list[GrantaServerApiSearchBoostByIdentity]
            The column_identities_to_boost of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.
        """
        return self._column_identities_to_boost

    @column_identities_to_boost.setter
    def column_identities_to_boost(
        self, column_identities_to_boost: "list[GrantaServerApiSearchBoostByIdentity]"
    ) -> None:
        """Sets the column_identities_to_boost of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.

        Parameters
        ----------
        column_identities_to_boost: list[GrantaServerApiSearchBoostByIdentity]
            The column_identities_to_boost of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.
        """
        self._column_identities_to_boost = column_identities_to_boost

    @property
    def column_guids(self) -> "list[str]":
        """Gets the column_guids of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.

        Returns
        -------
        list[str]
            The column_guids of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.
        """
        return self._column_guids

    @column_guids.setter
    def column_guids(self, column_guids: "list[str]") -> None:
        """Sets the column_guids of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.

        Parameters
        ----------
        column_guids: list[str]
            The column_guids of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.
        """
        self._column_guids = column_guids

    @property
    def column_guids_to_boost(self) -> "list[GrantaServerApiSearchBoostByGuid]":
        """Gets the column_guids_to_boost of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.

        Returns
        -------
        list[GrantaServerApiSearchBoostByGuid]
            The column_guids_to_boost of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.
        """
        return self._column_guids_to_boost

    @column_guids_to_boost.setter
    def column_guids_to_boost(
        self, column_guids_to_boost: "list[GrantaServerApiSearchBoostByGuid]"
    ) -> None:
        """Sets the column_guids_to_boost of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.

        Parameters
        ----------
        column_guids_to_boost: list[GrantaServerApiSearchBoostByGuid]
            The column_guids_to_boost of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.
        """
        self._column_guids_to_boost = column_guids_to_boost

    @property
    def free_text_criterion_type(self) -> "str":
        """Gets the free_text_criterion_type of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.

        Returns
        -------
        str
            The free_text_criterion_type of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.
        """
        return self._free_text_criterion_type

    @free_text_criterion_type.setter
    def free_text_criterion_type(self, free_text_criterion_type: "str") -> None:
        """Sets the free_text_criterion_type of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.

        Parameters
        ----------
        free_text_criterion_type: str
            The free_text_criterion_type of this GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion.
        """
        if free_text_criterion_type is None:
            raise ValueError(
                "Invalid value for 'free_text_criterion_type', must not be 'None'"
            )
        self._free_text_criterion_type = free_text_criterion_type

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
        if not isinstance(
            other, GrantaServerApiSearchFreeTextSpecifiedLocalColumnsCriterion
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
