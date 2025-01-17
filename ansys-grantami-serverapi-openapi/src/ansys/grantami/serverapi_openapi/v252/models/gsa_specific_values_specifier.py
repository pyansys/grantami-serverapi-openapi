"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.v252.models.gsa_value_specifier import GsaValueSpecifier  # noqa: F401
from ansys.grantami.serverapi_openapi.v252.models.gsa_value_specifier_type import GsaValueSpecifierType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaSpecificValuesSpecifier(GsaValueSpecifier):
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
        "filter_on": "GsaValueSpecifierType",
        "guids": "list[str]",
        "identities": "list[int]",
    }

    attribute_map: dict[str, str] = {
        "filter_on": "filterOn",
        "guids": "guids",
        "identities": "identities",
    }

    subtype_mapping: dict[str, str] = {
    }

    discriminator: Optional[str] = None

    def __init__(self, *, filter_on: "GsaValueSpecifierType" = GsaValueSpecifierType.SPECIFIC, guids: "Union[list[str], None, Unset_Type]" = Unset, identities: "Union[list[int], None, Unset_Type]" = Unset,) -> None:
        """GsaSpecificValuesSpecifier - a model defined in Swagger

        Parameters
        ----------
        filter_on: GsaValueSpecifierType
        guids: list[str], optional
        identities: list[int], optional
        """
        super().__init__(filter_on=filter_on)
        self._identities: Union[list[int], None, Unset_Type] = Unset
        self._guids: Union[list[str], None, Unset_Type] = Unset

        if identities is not Unset:
            self.identities = identities
        if guids is not Unset:
            self.guids = guids

    @property
    def identities(self) -> "Union[list[int], None, Unset_Type]":
        """Gets the identities of this GsaSpecificValuesSpecifier.

        Returns
        -------
        Union[list[int], None, Unset_Type]
            The identities of this GsaSpecificValuesSpecifier.
        """
        return self._identities

    @identities.setter
    def identities(self, identities: "Union[list[int], None, Unset_Type]") -> None:
        """Sets the identities of this GsaSpecificValuesSpecifier.

        Parameters
        ----------
        identities: Union[list[int], None, Unset_Type]
            The identities of this GsaSpecificValuesSpecifier.
        """
        self._identities = identities

    @property
    def guids(self) -> "Union[list[str], None, Unset_Type]":
        """Gets the guids of this GsaSpecificValuesSpecifier.

        Returns
        -------
        Union[list[str], None, Unset_Type]
            The guids of this GsaSpecificValuesSpecifier.
        """
        return self._guids

    @guids.setter
    def guids(self, guids: "Union[list[str], None, Unset_Type]") -> None:
        """Sets the guids of this GsaSpecificValuesSpecifier.

        Parameters
        ----------
        guids: Union[list[str], None, Unset_Type]
            The guids of this GsaSpecificValuesSpecifier.
        """
        self._guids = guids

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
        if not isinstance(other, GsaSpecificValuesSpecifier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

