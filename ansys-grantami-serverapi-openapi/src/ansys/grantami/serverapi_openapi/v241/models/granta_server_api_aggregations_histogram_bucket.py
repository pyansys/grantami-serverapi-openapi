"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
    from . import *


class GrantaServerApiAggregationsHistogramBucket(ModelBase):
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
        "count": "int",
        "lower": "float",
        "upper": "float",
    }

    attribute_map = {
        "count": "count",
        "lower": "lower",
        "upper": "upper",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        count: "Optional[int]" = None,
        lower: "Optional[float]" = None,
        upper: "Optional[float]" = None,
    ) -> None:
        """GrantaServerApiAggregationsHistogramBucket - a model defined in Swagger

        Parameters
        ----------
            count: int, optional
            lower: float, optional
            upper: float, optional
        """
        self._lower = None
        self._upper = None
        self._count = None

        if lower is not None:
            self.lower = lower
        if upper is not None:
            self.upper = upper
        if count is not None:
            self.count = count

    @property
    def lower(self) -> "float":
        """Gets the lower of this GrantaServerApiAggregationsHistogramBucket.

        Returns
        -------
        float
            The lower of this GrantaServerApiAggregationsHistogramBucket.
        """
        return self._lower

    @lower.setter
    def lower(self, lower: "float") -> None:
        """Sets the lower of this GrantaServerApiAggregationsHistogramBucket.

        Parameters
        ----------
        lower: float
            The lower of this GrantaServerApiAggregationsHistogramBucket.
        """
        self._lower = lower

    @property
    def upper(self) -> "float":
        """Gets the upper of this GrantaServerApiAggregationsHistogramBucket.

        Returns
        -------
        float
            The upper of this GrantaServerApiAggregationsHistogramBucket.
        """
        return self._upper

    @upper.setter
    def upper(self, upper: "float") -> None:
        """Sets the upper of this GrantaServerApiAggregationsHistogramBucket.

        Parameters
        ----------
        upper: float
            The upper of this GrantaServerApiAggregationsHistogramBucket.
        """
        self._upper = upper

    @property
    def count(self) -> "int":
        """Gets the count of this GrantaServerApiAggregationsHistogramBucket.

        Returns
        -------
        int
            The count of this GrantaServerApiAggregationsHistogramBucket.
        """
        return self._count

    @count.setter
    def count(self, count: "int") -> None:
        """Sets the count of this GrantaServerApiAggregationsHistogramBucket.

        Parameters
        ----------
        count: int
            The count of this GrantaServerApiAggregationsHistogramBucket.
        """
        self._count = count

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
        if not isinstance(other, GrantaServerApiAggregationsHistogramBucket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
