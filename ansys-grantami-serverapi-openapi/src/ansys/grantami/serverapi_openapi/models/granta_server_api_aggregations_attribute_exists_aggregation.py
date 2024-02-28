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
from ansys.grantami.serverapi_openapi.models.granta_server_api_aggregations_attribute_aggregation import (
    GrantaServerApiAggregationsAttributeAggregation,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiAggregationsAttributeExistsAggregation(
    GrantaServerApiAggregationsAttributeAggregation
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
        "attribute_aggregation_type": "str",
        "attribute_guid": "str",
        "attribute_identity": "int",
        "count": "int",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "attribute_aggregation_type": "attributeAggregationType",
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "count": "count",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_aggregation_type: "str" = "exists",
        attribute_guid: "Union[str, None, Unset_Type]" = Unset,
        attribute_identity: "Union[int, None, Unset_Type]" = Unset,
        count: "Union[int, Unset_Type]" = Unset,
        type: "str" = "attribute",
    ) -> None:
        """GrantaServerApiAggregationsAttributeExistsAggregation - a model defined in Swagger

        Parameters
        ----------
        attribute_aggregation_type: str
        attribute_guid: str, optional
        attribute_identity: int, optional
        count: int, optional
        type: str
        """
        super().__init__(
            attribute_guid=attribute_guid,
            attribute_identity=attribute_identity,
            count=count,
            type=type,
        )
        self._attribute_aggregation_type: str

        self.attribute_aggregation_type = attribute_aggregation_type

    @property
    def attribute_aggregation_type(self) -> "str":
        """Gets the attribute_aggregation_type of this GrantaServerApiAggregationsAttributeExistsAggregation.

        Returns
        -------
        str
            The attribute_aggregation_type of this GrantaServerApiAggregationsAttributeExistsAggregation.
        """
        return self._attribute_aggregation_type

    @attribute_aggregation_type.setter
    def attribute_aggregation_type(self, attribute_aggregation_type: "str") -> None:
        """Sets the attribute_aggregation_type of this GrantaServerApiAggregationsAttributeExistsAggregation.

        Parameters
        ----------
        attribute_aggregation_type: str
            The attribute_aggregation_type of this GrantaServerApiAggregationsAttributeExistsAggregation.
        """
        # Field is not nullable
        if attribute_aggregation_type is None:
            raise ValueError(
                "Invalid value for 'attribute_aggregation_type', must not be 'None'"
            )
        # Field is required
        if attribute_aggregation_type is Unset:  # type: ignore[comparison-overlap]
            raise ValueError(
                "Invalid value for 'attribute_aggregation_type', must not be 'Unset'"
            )
        self._attribute_aggregation_type = attribute_aggregation_type

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
        if not isinstance(other, GrantaServerApiAggregationsAttributeExistsAggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
