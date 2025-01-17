"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.v252.models.gsa_aggregation_datum import GsaAggregationDatum  # noqa: F401
from ansys.grantami.serverapi_openapi.v252.models.gsa_aggregation_datum_type import GsaAggregationDatumType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaShortTextAggregation(GsaAggregationDatum):
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
        "datum_type": "GsaAggregationDatumType",
        "terms": "list[GsaTermWithCount]",
    }

    attribute_map: dict[str, str] = {
        "datum_type": "datumType",
        "terms": "terms",
    }

    subtype_mapping: dict[str, str] = {
        "terms": "GsaTermWithCount",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, datum_type: "GsaAggregationDatumType" = GsaAggregationDatumType.SHORTTEXT, terms: "Union[list[GsaTermWithCount], None, Unset_Type]" = Unset,) -> None:
        """GsaShortTextAggregation - a model defined in Swagger

        Parameters
        ----------
        datum_type: GsaAggregationDatumType
        terms: list[GsaTermWithCount], optional
        """
        super().__init__(datum_type=datum_type)
        self._terms: Union[list[GsaTermWithCount], None, Unset_Type] = Unset

        if terms is not Unset:
            self.terms = terms

    @property
    def terms(self) -> "Union[list[GsaTermWithCount], None, Unset_Type]":
        """Gets the terms of this GsaShortTextAggregation.

        Returns
        -------
        Union[list[GsaTermWithCount], None, Unset_Type]
            The terms of this GsaShortTextAggregation.
        """
        return self._terms

    @terms.setter
    def terms(self, terms: "Union[list[GsaTermWithCount], None, Unset_Type]") -> None:
        """Sets the terms of this GsaShortTextAggregation.

        Parameters
        ----------
        terms: Union[list[GsaTermWithCount], None, Unset_Type]
            The terms of this GsaShortTextAggregation.
        """
        self._terms = terms

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
        if not isinstance(other, GsaShortTextAggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

