"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase
from ansys.grantami.serverapi_openapi.models.granta_server_api_search_attribute_criterion import (
    GrantaServerApiSearchAttributeCriterion,
)  # noqa: F401


if TYPE_CHECKING:
    from . import *


class GrantaServerApiSearchAttributeNotApplicableCriterion(
    GrantaServerApiSearchAttributeCriterion
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
    swagger_types = {
        "attribute_criterion_type": "str",
        "guid": "str",
        "identity": "int",
        "is_meta_attribute": "bool",
        "type": "str",
    }

    attribute_map = {
        "attribute_criterion_type": "attributeCriterionType",
        "guid": "guid",
        "identity": "identity",
        "is_meta_attribute": "isMetaAttribute",
        "type": "type",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        attribute_criterion_type: "str" = "notApplicable",
        guid: "Optional[str]" = None,
        identity: "Optional[int]" = None,
        is_meta_attribute: "Optional[bool]" = None,
        type: "str" = "attribute",
    ) -> None:
        """GrantaServerApiSearchAttributeNotApplicableCriterion - a model defined in Swagger

        Parameters
        ----------
            attribute_criterion_type: str
            guid: str, optional
            identity: int, optional
            is_meta_attribute: bool, optional
            type: str
        """
        super().__init__(
            guid=guid, identity=identity, is_meta_attribute=is_meta_attribute, type=type
        )
        self._attribute_criterion_type = None

        self.attribute_criterion_type = attribute_criterion_type

    @property
    def attribute_criterion_type(self) -> "str":
        """Gets the attribute_criterion_type of this GrantaServerApiSearchAttributeNotApplicableCriterion.

        Returns
        -------
        str
            The attribute_criterion_type of this GrantaServerApiSearchAttributeNotApplicableCriterion.
        """
        return self._attribute_criterion_type

    @attribute_criterion_type.setter
    def attribute_criterion_type(self, attribute_criterion_type: "str") -> None:
        """Sets the attribute_criterion_type of this GrantaServerApiSearchAttributeNotApplicableCriterion.

        Parameters
        ----------
        attribute_criterion_type: str
            The attribute_criterion_type of this GrantaServerApiSearchAttributeNotApplicableCriterion.
        """
        if attribute_criterion_type is None:
            raise ValueError(
                "Invalid value for 'attribute_criterion_type', must not be 'None'"
            )
        self._attribute_criterion_type = attribute_criterion_type

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
        if not isinstance(other, GrantaServerApiSearchAttributeNotApplicableCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
