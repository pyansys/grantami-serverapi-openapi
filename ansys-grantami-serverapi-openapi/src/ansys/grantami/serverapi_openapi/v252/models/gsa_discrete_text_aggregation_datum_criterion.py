"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.v252.models.gsa_aggregation_datum_criterion import GsaAggregationDatumCriterion  # noqa: F401
from ansys.grantami.serverapi_openapi.v252.models.gsa_aggregation_datum_criterion_type import GsaAggregationDatumCriterionType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaDiscreteTextAggregationDatumCriterion(GsaAggregationDatumCriterion):
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
        "type": "GsaAggregationDatumCriterionType",
        "number_of_terms": "int",
        "prefix": "str",
    }

    attribute_map: dict[str, str] = {
        "type": "type",
        "number_of_terms": "numberOfTerms",
        "prefix": "prefix",
    }

    subtype_mapping: dict[str, str] = {
    }

    discriminator: Optional[str] = None

    def __init__(self, *, type: "GsaAggregationDatumCriterionType" = GsaAggregationDatumCriterionType.DISCRETETEXT, number_of_terms: "Union[int, Unset_Type]" = Unset, prefix: "Union[str, None, Unset_Type]" = Unset,) -> None:
        """GsaDiscreteTextAggregationDatumCriterion - a model defined in Swagger

        Parameters
        ----------
        type: GsaAggregationDatumCriterionType
        number_of_terms: int, optional
        prefix: str, optional
        """
        super().__init__(type=type)
        self._number_of_terms: Union[int, Unset_Type] = Unset
        self._prefix: Union[str, None, Unset_Type] = Unset

        if number_of_terms is not Unset:
            self.number_of_terms = number_of_terms
        if prefix is not Unset:
            self.prefix = prefix

    @property
    def number_of_terms(self) -> "Union[int, Unset_Type]":
        """Gets the number_of_terms of this GsaDiscreteTextAggregationDatumCriterion.
        The maximum number of terms to return in this aggregation.

        Returns
        -------
        Union[int, Unset_Type]
            The number_of_terms of this GsaDiscreteTextAggregationDatumCriterion.
        """
        return self._number_of_terms

    @number_of_terms.setter
    def number_of_terms(self, number_of_terms: "Union[int, Unset_Type]") -> None:
        """Sets the number_of_terms of this GsaDiscreteTextAggregationDatumCriterion.
        The maximum number of terms to return in this aggregation.

        Parameters
        ----------
        number_of_terms: Union[int, Unset_Type]
            The number_of_terms of this GsaDiscreteTextAggregationDatumCriterion.
        """
        # Field is not nullable
        if number_of_terms is None:
            raise ValueError("Invalid value for 'number_of_terms', must not be 'None'")
        self._number_of_terms = number_of_terms

    @property
    def prefix(self) -> "Union[str, None, Unset_Type]":
        """Gets the prefix of this GsaDiscreteTextAggregationDatumCriterion.
        An optional textual prefix. If provided, only terms that start with this prefix will be  considered in the aggregation.

        Returns
        -------
        Union[str, None, Unset_Type]
            The prefix of this GsaDiscreteTextAggregationDatumCriterion.
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix: "Union[str, None, Unset_Type]") -> None:
        """Sets the prefix of this GsaDiscreteTextAggregationDatumCriterion.
        An optional textual prefix. If provided, only terms that start with this prefix will be  considered in the aggregation.

        Parameters
        ----------
        prefix: Union[str, None, Unset_Type]
            The prefix of this GsaDiscreteTextAggregationDatumCriterion.
        """
        self._prefix = prefix

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
        if not isinstance(other, GsaDiscreteTextAggregationDatumCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

