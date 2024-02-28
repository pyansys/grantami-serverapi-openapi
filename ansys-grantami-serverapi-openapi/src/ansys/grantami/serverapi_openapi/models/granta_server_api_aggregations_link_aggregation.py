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
from ansys.grantami.serverapi_openapi.models.granta_server_api_aggregations_aggregation_datum import (
    GrantaServerApiAggregationsAggregationDatum,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiAggregationsLinkAggregation(
    GrantaServerApiAggregationsAggregationDatum
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
        "datum_type": "str",
        "local_aggregations": "list[GrantaServerApiAggregationsLocalColumnAggregation]",
    }

    attribute_map: Dict[str, str] = {
        "datum_type": "datumType",
        "local_aggregations": "localAggregations",
    }

    subtype_mapping: Dict[str, str] = {
        "localAggregations": "GrantaServerApiAggregationsLocalColumnAggregation",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        datum_type: "str" = "link",
        local_aggregations: "Union[List[GrantaServerApiAggregationsLocalColumnAggregation], None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiAggregationsLinkAggregation - a model defined in Swagger

        Parameters
        ----------
        datum_type: str
        local_aggregations: List[GrantaServerApiAggregationsLocalColumnAggregation], optional
        """
        super().__init__()
        self._local_aggregations: Union[
            List[GrantaServerApiAggregationsLocalColumnAggregation], None, Unset_Type
        ] = Unset
        self._datum_type: str

        if local_aggregations is not Unset:
            self.local_aggregations = local_aggregations
        self.datum_type = datum_type

    @property
    def local_aggregations(
        self,
    ) -> "Union[List[GrantaServerApiAggregationsLocalColumnAggregation], None, Unset_Type]":
        """Gets the local_aggregations of this GrantaServerApiAggregationsLinkAggregation.

        Returns
        -------
        Union[List[GrantaServerApiAggregationsLocalColumnAggregation], None, Unset_Type]
            The local_aggregations of this GrantaServerApiAggregationsLinkAggregation.
        """
        return self._local_aggregations

    @local_aggregations.setter
    def local_aggregations(
        self,
        local_aggregations: "Union[List[GrantaServerApiAggregationsLocalColumnAggregation], None, Unset_Type]",
    ) -> None:
        """Sets the local_aggregations of this GrantaServerApiAggregationsLinkAggregation.

        Parameters
        ----------
        local_aggregations: Union[List[GrantaServerApiAggregationsLocalColumnAggregation], None, Unset_Type]
            The local_aggregations of this GrantaServerApiAggregationsLinkAggregation.
        """
        self._local_aggregations = local_aggregations

    @property
    def datum_type(self) -> "str":
        """Gets the datum_type of this GrantaServerApiAggregationsLinkAggregation.

        Returns
        -------
        str
            The datum_type of this GrantaServerApiAggregationsLinkAggregation.
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type: "str") -> None:
        """Sets the datum_type of this GrantaServerApiAggregationsLinkAggregation.

        Parameters
        ----------
        datum_type: str
            The datum_type of this GrantaServerApiAggregationsLinkAggregation.
        """
        # Field is not nullable
        if datum_type is None:
            raise ValueError("Invalid value for 'datum_type', must not be 'None'")
        # Field is required
        if datum_type is Unset:  # type: ignore[comparison-overlap]
            raise ValueError("Invalid value for 'datum_type', must not be 'Unset'")
        self._datum_type = datum_type

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
        if not isinstance(other, GrantaServerApiAggregationsLinkAggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
