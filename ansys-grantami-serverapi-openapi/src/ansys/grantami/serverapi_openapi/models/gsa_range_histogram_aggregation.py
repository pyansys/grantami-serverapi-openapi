"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.models.gsa_aggregation_datum import GsaAggregationDatum  # noqa: F401
from ansys.grantami.serverapi_openapi.models.gsa_aggregation_datum_type import GsaAggregationDatumType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaRangeHistogramAggregation(GsaAggregationDatum):
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
        "histogram": "GsaHistogram",
    }

    attribute_map: dict[str, str] = {
        "datum_type": "datumType",
        "histogram": "histogram",
    }

    subtype_mapping: dict[str, str] = {
        "histogram": "GsaHistogram",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, datum_type: "GsaAggregationDatumType" = GsaAggregationDatumType.RANGEHISTOGRAM, histogram: "Union[GsaHistogram, Unset_Type]" = Unset,) -> None:
        """GsaRangeHistogramAggregation - a model defined in Swagger

        Parameters
        ----------
        datum_type: GsaAggregationDatumType
        histogram: GsaHistogram, optional
        """
        super().__init__(datum_type=datum_type)
        self._histogram: Union[GsaHistogram, Unset_Type] = Unset

        if histogram is not Unset:
            self.histogram = histogram

    @property
    def histogram(self) -> "Union[GsaHistogram, Unset_Type]":
        """Gets the histogram of this GsaRangeHistogramAggregation.

        Returns
        -------
        Union[GsaHistogram, Unset_Type]
            The histogram of this GsaRangeHistogramAggregation.
        """
        return self._histogram

    @histogram.setter
    def histogram(self, histogram: "Union[GsaHistogram, Unset_Type]") -> None:
        """Sets the histogram of this GsaRangeHistogramAggregation.

        Parameters
        ----------
        histogram: Union[GsaHistogram, Unset_Type]
            The histogram of this GsaRangeHistogramAggregation.
        """
        # Field is not nullable
        if histogram is None:
            raise ValueError("Invalid value for 'histogram', must not be 'None'")
        self._histogram = histogram

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
        if not isinstance(other, GsaRangeHistogramAggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

