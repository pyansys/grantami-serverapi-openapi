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
    Dict,
    List,
    BinaryIO,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiAggregationsLocalColumnAggregationCriterion(ModelBase):  # type: ignore[misc]
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
    discriminator_class_map: Dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: Dict[str, str] = {
        "guid": "str",
        "identity": "int",
    }

    attribute_map: Dict[str, str] = {
        "guid": "guid",
        "identity": "identity",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator_value_class_map = {
        "value".lower(): "#/components/schemas/GrantaServerApiAggregationsLocalColumnAggregationValueCriterion",
        "exists".lower(): "#/components/schemas/GrantaServerApiAggregationsLocalColumnAggregationExistsCriterion",
    }

    discriminator: Optional[str] = "local_column_aggregation_criterion_type"

    def __init__(
        self,
        *,
        guid: "Optional[str]" = None,
        identity: "Optional[int]" = None,
    ) -> None:
        """GrantaServerApiAggregationsLocalColumnAggregationCriterion - a model defined in Swagger

        Parameters
        ----------
            guid: str, optional
            identity: int, optional
        """
        self._identity = None
        self._guid = None

        if identity is not None:
            self.identity = identity
        if guid is not None:
            self.guid = guid

    @property
    def identity(self) -> "Optional[int]":
        """Gets the identity of this GrantaServerApiAggregationsLocalColumnAggregationCriterion.

        Returns
        -------
        int
            The identity of this GrantaServerApiAggregationsLocalColumnAggregationCriterion.
        """
        return self._identity

    @identity.setter
    def identity(self, identity: "Optional[int]") -> None:
        """Sets the identity of this GrantaServerApiAggregationsLocalColumnAggregationCriterion.

        Parameters
        ----------
        identity: int
            The identity of this GrantaServerApiAggregationsLocalColumnAggregationCriterion.
        """
        self._identity = identity

    @property
    def guid(self) -> "Optional[str]":
        """Gets the guid of this GrantaServerApiAggregationsLocalColumnAggregationCriterion.

        Returns
        -------
        str
            The guid of this GrantaServerApiAggregationsLocalColumnAggregationCriterion.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Optional[str]") -> None:
        """Sets the guid of this GrantaServerApiAggregationsLocalColumnAggregationCriterion.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiAggregationsLocalColumnAggregationCriterion.
        """
        self._guid = guid

    @classmethod
    def get_real_child_model(cls, data: ModelBase) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[cls._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen,
        # so we have to extract it from the JSON reference
        return cls.discriminator_value_class_map[discriminator_value].rsplit("/", 1)[-1]

    @classmethod
    def _get_discriminator_field_name(cls) -> str:
        assert cls.discriminator
        name_tokens = cls.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()  # type: ignore[no-any-return]

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(
            other, GrantaServerApiAggregationsLocalColumnAggregationCriterion
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
