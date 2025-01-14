"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.models.gsa_list_criterion import GsaListCriterion  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaListBooleanCriterion(GsaListCriterion):
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
        "type": "str",
        "match_all": "list[GsaListCriterion]",
        "match_any": "list[GsaListCriterion]",
    }

    attribute_map: dict[str, str] = {
        "type": "type",
        "match_all": "matchAll",
        "match_any": "matchAny",
    }

    subtype_mapping: dict[str, str] = {
        "matchAny": "GsaListCriterion",
        "matchAll": "GsaListCriterion",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, type: "str" = "listBoolean", match_all: "Union[list[GsaListCriterion], None, Unset_Type]" = Unset, match_any: "Union[list[GsaListCriterion], None, Unset_Type]" = Unset,) -> None:
        """GsaListBooleanCriterion - a model defined in Swagger

        Parameters
        ----------
        type: str
        match_all: list[GsaListCriterion], optional
        match_any: list[GsaListCriterion], optional
        """
        super().__init__(type=type)
        self._match_any: Union[list[GsaListCriterion], None, Unset_Type] = Unset
        self._match_all: Union[list[GsaListCriterion], None, Unset_Type] = Unset

        if match_any is not Unset:
            self.match_any = match_any
        if match_all is not Unset:
            self.match_all = match_all

    @property
    def match_any(self) -> "Union[list[GsaListCriterion], None, Unset_Type]":
        """Gets the match_any of this GsaListBooleanCriterion.

        Returns
        -------
        Union[list[GsaListCriterion], None, Unset_Type]
            The match_any of this GsaListBooleanCriterion.
        """
        return self._match_any

    @match_any.setter
    def match_any(self, match_any: "Union[list[GsaListCriterion], None, Unset_Type]") -> None:
        """Sets the match_any of this GsaListBooleanCriterion.

        Parameters
        ----------
        match_any: Union[list[GsaListCriterion], None, Unset_Type]
            The match_any of this GsaListBooleanCriterion.
        """
        self._match_any = match_any

    @property
    def match_all(self) -> "Union[list[GsaListCriterion], None, Unset_Type]":
        """Gets the match_all of this GsaListBooleanCriterion.

        Returns
        -------
        Union[list[GsaListCriterion], None, Unset_Type]
            The match_all of this GsaListBooleanCriterion.
        """
        return self._match_all

    @match_all.setter
    def match_all(self, match_all: "Union[list[GsaListCriterion], None, Unset_Type]") -> None:
        """Sets the match_all of this GsaListBooleanCriterion.

        Parameters
        ----------
        match_all: Union[list[GsaListCriterion], None, Unset_Type]
            The match_all of this GsaListBooleanCriterion.
        """
        self._match_all = match_all

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
        if not isinstance(other, GsaListBooleanCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

