"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.v252.models.gsa_aggregation_criterion import GsaAggregationCriterion  # noqa: F401
from ansys.grantami.serverapi_openapi.v252.models.gsa_aggregation_type import GsaAggregationType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaFreeTextAggregationCriterion(GsaAggregationCriterion):
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
        "type": "GsaAggregationType",
        "attributes": "GsaValueSpecifier",
        "criterion_guid": "str",
        "local_columns": "GsaValueSpecifier",
        "number_of_terms": "int",
        "prefix": "str",
    }

    attribute_map: dict[str, str] = {
        "type": "type",
        "attributes": "attributes",
        "criterion_guid": "criterionGuid",
        "local_columns": "localColumns",
        "number_of_terms": "numberOfTerms",
        "prefix": "prefix",
    }

    subtype_mapping: dict[str, str] = {
        "attributes": "GsaValueSpecifier",
        "localColumns": "GsaValueSpecifier",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, type: "GsaAggregationType" = GsaAggregationType.TEXT, attributes: "Union[GsaValueSpecifier, Unset_Type]" = Unset, criterion_guid: "Union[str, Unset_Type]" = Unset, local_columns: "Union[GsaValueSpecifier, Unset_Type]" = Unset, number_of_terms: "Union[int, Unset_Type]" = Unset, prefix: "Union[str, None, Unset_Type]" = Unset,) -> None:
        """GsaFreeTextAggregationCriterion - a model defined in Swagger

        Parameters
        ----------
        type: GsaAggregationType
        attributes: GsaValueSpecifier, optional
        criterion_guid: str, optional
        local_columns: GsaValueSpecifier, optional
        number_of_terms: int, optional
        prefix: str, optional
        """
        super().__init__(type=type)
        self._criterion_guid: Union[str, Unset_Type] = Unset
        self._number_of_terms: Union[int, Unset_Type] = Unset
        self._prefix: Union[str, None, Unset_Type] = Unset
        self._attributes: Union[GsaValueSpecifier, Unset_Type] = Unset
        self._local_columns: Union[GsaValueSpecifier, Unset_Type] = Unset

        if criterion_guid is not Unset:
            self.criterion_guid = criterion_guid
        if number_of_terms is not Unset:
            self.number_of_terms = number_of_terms
        if prefix is not Unset:
            self.prefix = prefix
        if attributes is not Unset:
            self.attributes = attributes
        if local_columns is not Unset:
            self.local_columns = local_columns

    @property
    def criterion_guid(self) -> "Union[str, Unset_Type]":
        """Gets the criterion_guid of this GsaFreeTextAggregationCriterion.
        A GUID to identify this free-text criterion, so that its results can be determined in the output.  For each input free-text aggregation criterion, there will be a free-text aggregation in the output  with a matching GUID.

        Returns
        -------
        Union[str, Unset_Type]
            The criterion_guid of this GsaFreeTextAggregationCriterion.
        """
        return self._criterion_guid

    @criterion_guid.setter
    def criterion_guid(self, criterion_guid: "Union[str, Unset_Type]") -> None:
        """Sets the criterion_guid of this GsaFreeTextAggregationCriterion.
        A GUID to identify this free-text criterion, so that its results can be determined in the output.  For each input free-text aggregation criterion, there will be a free-text aggregation in the output  with a matching GUID.

        Parameters
        ----------
        criterion_guid: Union[str, Unset_Type]
            The criterion_guid of this GsaFreeTextAggregationCriterion.
        """
        # Field is not nullable
        if criterion_guid is None:
            raise ValueError("Invalid value for 'criterion_guid', must not be 'None'")
        self._criterion_guid = criterion_guid

    @property
    def number_of_terms(self) -> "Union[int, Unset_Type]":
        """Gets the number_of_terms of this GsaFreeTextAggregationCriterion.
        The number of terms that should be returned

        Returns
        -------
        Union[int, Unset_Type]
            The number_of_terms of this GsaFreeTextAggregationCriterion.
        """
        return self._number_of_terms

    @number_of_terms.setter
    def number_of_terms(self, number_of_terms: "Union[int, Unset_Type]") -> None:
        """Sets the number_of_terms of this GsaFreeTextAggregationCriterion.
        The number of terms that should be returned

        Parameters
        ----------
        number_of_terms: Union[int, Unset_Type]
            The number_of_terms of this GsaFreeTextAggregationCriterion.
        """
        # Field is not nullable
        if number_of_terms is None:
            raise ValueError("Invalid value for 'number_of_terms', must not be 'None'")
        self._number_of_terms = number_of_terms

    @property
    def prefix(self) -> "Union[str, None, Unset_Type]":
        """Gets the prefix of this GsaFreeTextAggregationCriterion.

        Returns
        -------
        Union[str, None, Unset_Type]
            The prefix of this GsaFreeTextAggregationCriterion.
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix: "Union[str, None, Unset_Type]") -> None:
        """Sets the prefix of this GsaFreeTextAggregationCriterion.

        Parameters
        ----------
        prefix: Union[str, None, Unset_Type]
            The prefix of this GsaFreeTextAggregationCriterion.
        """
        self._prefix = prefix

    @property
    def attributes(self) -> "Union[GsaValueSpecifier, Unset_Type]":
        """Gets the attributes of this GsaFreeTextAggregationCriterion.

        Returns
        -------
        Union[GsaValueSpecifier, Unset_Type]
            The attributes of this GsaFreeTextAggregationCriterion.
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes: "Union[GsaValueSpecifier, Unset_Type]") -> None:
        """Sets the attributes of this GsaFreeTextAggregationCriterion.

        Parameters
        ----------
        attributes: Union[GsaValueSpecifier, Unset_Type]
            The attributes of this GsaFreeTextAggregationCriterion.
        """
        # Field is not nullable
        if attributes is None:
            raise ValueError("Invalid value for 'attributes', must not be 'None'")
        self._attributes = attributes

    @property
    def local_columns(self) -> "Union[GsaValueSpecifier, Unset_Type]":
        """Gets the local_columns of this GsaFreeTextAggregationCriterion.

        Returns
        -------
        Union[GsaValueSpecifier, Unset_Type]
            The local_columns of this GsaFreeTextAggregationCriterion.
        """
        return self._local_columns

    @local_columns.setter
    def local_columns(self, local_columns: "Union[GsaValueSpecifier, Unset_Type]") -> None:
        """Sets the local_columns of this GsaFreeTextAggregationCriterion.

        Parameters
        ----------
        local_columns: Union[GsaValueSpecifier, Unset_Type]
            The local_columns of this GsaFreeTextAggregationCriterion.
        """
        # Field is not nullable
        if local_columns is None:
            raise ValueError("Invalid value for 'local_columns', must not be 'None'")
        self._local_columns = local_columns

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
        if not isinstance(other, GsaFreeTextAggregationCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

