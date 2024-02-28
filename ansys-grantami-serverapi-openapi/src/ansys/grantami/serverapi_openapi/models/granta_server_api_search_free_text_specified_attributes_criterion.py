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
from ansys.grantami.serverapi_openapi.models.granta_server_api_search_free_text_criterion import (
    GrantaServerApiSearchFreeTextCriterion,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion(
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
    swagger_types: Dict[str, str] = {
        "free_text_criterion_type": "str",
        "guids": "list[str]",
        "guids_to_boost": "list[GrantaServerApiSearchBoostByGuid]",
        "identities": "list[int]",
        "identities_to_boost": "list[GrantaServerApiSearchBoostByIdentity]",
        "type": "str",
        "value": "str",
    }

    attribute_map: Dict[str, str] = {
        "free_text_criterion_type": "freeTextCriterionType",
        "guids": "guids",
        "guids_to_boost": "guidsToBoost",
        "identities": "identities",
        "identities_to_boost": "identitiesToBoost",
        "type": "type",
        "value": "value",
    }

    subtype_mapping: Dict[str, str] = {
        "identitiesToBoost": "GrantaServerApiSearchBoostByIdentity",
        "guidsToBoost": "GrantaServerApiSearchBoostByGuid",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        free_text_criterion_type: "str" = "specifiedAttributes",
        guids: "Union[List[str], None, Unset_Type]" = Unset,
        guids_to_boost: "Union[List[GrantaServerApiSearchBoostByGuid], None, Unset_Type]" = Unset,
        identities: "Union[List[int], None, Unset_Type]" = Unset,
        identities_to_boost: "Union[List[GrantaServerApiSearchBoostByIdentity], None, Unset_Type]" = Unset,
        type: "str" = "text",
        value: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion - a model defined in Swagger

        Parameters
        ----------
        free_text_criterion_type: str
        guids: List[str], optional
        guids_to_boost: List[GrantaServerApiSearchBoostByGuid], optional
        identities: List[int], optional
        identities_to_boost: List[GrantaServerApiSearchBoostByIdentity], optional
        type: str
        value: str, optional
        """
        super().__init__(type=type, value=value)
        self._identities: Union[List[int], None, Unset_Type] = Unset
        self._identities_to_boost: Union[
            List[GrantaServerApiSearchBoostByIdentity], None, Unset_Type
        ] = Unset
        self._guids: Union[List[str], None, Unset_Type] = Unset
        self._guids_to_boost: Union[
            List[GrantaServerApiSearchBoostByGuid], None, Unset_Type
        ] = Unset
        self._free_text_criterion_type: str

        if identities is not Unset:
            self.identities = identities
        if identities_to_boost is not Unset:
            self.identities_to_boost = identities_to_boost
        if guids is not Unset:
            self.guids = guids
        if guids_to_boost is not Unset:
            self.guids_to_boost = guids_to_boost
        self.free_text_criterion_type = free_text_criterion_type

    @property
    def identities(self) -> "Union[List[int], None, Unset_Type]":
        """Gets the identities of this GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion.

        Returns
        -------
        Union[List[int], None, Unset_Type]
            The identities of this GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion.
        """
        return self._identities

    @identities.setter
    def identities(self, identities: "Union[List[int], None, Unset_Type]") -> None:
        """Sets the identities of this GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion.

        Parameters
        ----------
        identities: Union[List[int], None, Unset_Type]
            The identities of this GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion.
        """
        self._identities = identities

    @property
    def identities_to_boost(
        self,
    ) -> "Union[List[GrantaServerApiSearchBoostByIdentity], None, Unset_Type]":
        """Gets the identities_to_boost of this GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion.

        Returns
        -------
        Union[List[GrantaServerApiSearchBoostByIdentity], None, Unset_Type]
            The identities_to_boost of this GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion.
        """
        return self._identities_to_boost

    @identities_to_boost.setter
    def identities_to_boost(
        self,
        identities_to_boost: "Union[List[GrantaServerApiSearchBoostByIdentity], None, Unset_Type]",
    ) -> None:
        """Sets the identities_to_boost of this GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion.

        Parameters
        ----------
        identities_to_boost: Union[List[GrantaServerApiSearchBoostByIdentity], None, Unset_Type]
            The identities_to_boost of this GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion.
        """
        self._identities_to_boost = identities_to_boost

    @property
    def guids(self) -> "Union[List[str], None, Unset_Type]":
        """Gets the guids of this GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion.

        Returns
        -------
        Union[List[str], None, Unset_Type]
            The guids of this GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion.
        """
        return self._guids

    @guids.setter
    def guids(self, guids: "Union[List[str], None, Unset_Type]") -> None:
        """Sets the guids of this GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion.

        Parameters
        ----------
        guids: Union[List[str], None, Unset_Type]
            The guids of this GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion.
        """
        self._guids = guids

    @property
    def guids_to_boost(
        self,
    ) -> "Union[List[GrantaServerApiSearchBoostByGuid], None, Unset_Type]":
        """Gets the guids_to_boost of this GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion.

        Returns
        -------
        Union[List[GrantaServerApiSearchBoostByGuid], None, Unset_Type]
            The guids_to_boost of this GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion.
        """
        return self._guids_to_boost

    @guids_to_boost.setter
    def guids_to_boost(
        self,
        guids_to_boost: "Union[List[GrantaServerApiSearchBoostByGuid], None, Unset_Type]",
    ) -> None:
        """Sets the guids_to_boost of this GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion.

        Parameters
        ----------
        guids_to_boost: Union[List[GrantaServerApiSearchBoostByGuid], None, Unset_Type]
            The guids_to_boost of this GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion.
        """
        self._guids_to_boost = guids_to_boost

    @property
    def free_text_criterion_type(self) -> "str":
        """Gets the free_text_criterion_type of this GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion.

        Returns
        -------
        str
            The free_text_criterion_type of this GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion.
        """
        return self._free_text_criterion_type

    @free_text_criterion_type.setter
    def free_text_criterion_type(self, free_text_criterion_type: "str") -> None:
        """Sets the free_text_criterion_type of this GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion.

        Parameters
        ----------
        free_text_criterion_type: str
            The free_text_criterion_type of this GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion.
        """
        # Field is not nullable
        if free_text_criterion_type is None:
            raise ValueError(
                "Invalid value for 'free_text_criterion_type', must not be 'None'"
            )
        # Field is required
        if free_text_criterion_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'free_text_criterion_type', must not be 'Unset'"
            )
        self._free_text_criterion_type = free_text_criterion_type

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
        if not isinstance(
            other, GrantaServerApiSearchFreeTextSpecifiedAttributesCriterion
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
