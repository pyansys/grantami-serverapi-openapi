"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.v252.models.gsa_criterion import GsaCriterion  # noqa: F401
from ansys.grantami.serverapi_openapi.v252.models.gsa_criterion_type import GsaCriterionType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaTabularLinkingValueCriterion(GsaCriterion):
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
        "type": "GsaCriterionType",
        "values": "list[str]",
        "linking_value_match_behavior": "GsaLinkingValueMatchBehavior",
    }

    attribute_map: dict[str, str] = {
        "type": "type",
        "values": "values",
        "linking_value_match_behavior": "linkingValueMatchBehavior",
    }

    subtype_mapping: dict[str, str] = {
        "linkingValueMatchBehavior": "GsaLinkingValueMatchBehavior",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, type: "GsaCriterionType" = GsaCriterionType.TABULARLINKINGVALUE, values: "list[str]", linking_value_match_behavior: "Union[GsaLinkingValueMatchBehavior, Unset_Type]" = Unset,) -> None:
        """GsaTabularLinkingValueCriterion - a model defined in Swagger

        Parameters
        ----------
        type: GsaCriterionType
        values: list[str]
        linking_value_match_behavior: GsaLinkingValueMatchBehavior, optional
        """
        super().__init__(type=type)
        self._values: list[str]
        self._linking_value_match_behavior: Union[GsaLinkingValueMatchBehavior, Unset_Type] = Unset

        self.values = values
        if linking_value_match_behavior is not Unset:
            self.linking_value_match_behavior = linking_value_match_behavior

    @property
    def values(self) -> "list[str]":
        """Gets the values of this GsaTabularLinkingValueCriterion.

        Returns
        -------
        list[str]
            The values of this GsaTabularLinkingValueCriterion.
        """
        return self._values

    @values.setter
    def values(self, values: "list[str]") -> None:
        """Sets the values of this GsaTabularLinkingValueCriterion.

        Parameters
        ----------
        values: list[str]
            The values of this GsaTabularLinkingValueCriterion.
        """
        # Field is not nullable
        if values is None:
            raise ValueError("Invalid value for 'values', must not be 'None'")
        # Field is required
        if values is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'values', must not be 'Unset'")
        self._values = values

    @property
    def linking_value_match_behavior(self) -> "Union[GsaLinkingValueMatchBehavior, Unset_Type]":
        """Gets the linking_value_match_behavior of this GsaTabularLinkingValueCriterion.

        Returns
        -------
        Union[GsaLinkingValueMatchBehavior, Unset_Type]
            The linking_value_match_behavior of this GsaTabularLinkingValueCriterion.
        """
        return self._linking_value_match_behavior

    @linking_value_match_behavior.setter
    def linking_value_match_behavior(self, linking_value_match_behavior: "Union[GsaLinkingValueMatchBehavior, Unset_Type]") -> None:
        """Sets the linking_value_match_behavior of this GsaTabularLinkingValueCriterion.

        Parameters
        ----------
        linking_value_match_behavior: Union[GsaLinkingValueMatchBehavior, Unset_Type]
            The linking_value_match_behavior of this GsaTabularLinkingValueCriterion.
        """
        # Field is not nullable
        if linking_value_match_behavior is None:
            raise ValueError("Invalid value for 'linking_value_match_behavior', must not be 'None'")
        self._linking_value_match_behavior = linking_value_match_behavior

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
        if not isinstance(other, GsaTabularLinkingValueCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

