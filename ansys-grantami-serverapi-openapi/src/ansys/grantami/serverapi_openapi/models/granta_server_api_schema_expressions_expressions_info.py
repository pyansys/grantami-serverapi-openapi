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


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaExpressionsExpressionsInfo(ModelBase):
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
        "expressions": "list[GrantaServerApiSchemaSlimEntitiesSlimExpression]",
    }

    attribute_map: Dict[str, str] = {
        "expressions": "expressions",
    }

    subtype_mapping: Dict[str, str] = {
        "expressions": "GrantaServerApiSchemaSlimEntitiesSlimExpression",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        expressions: "Union[List[GrantaServerApiSchemaSlimEntitiesSlimExpression], None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaExpressionsExpressionsInfo - a model defined in Swagger

        Parameters
        ----------
        expressions: List[GrantaServerApiSchemaSlimEntitiesSlimExpression], optional
        """
        self._expressions: Union[
            List[GrantaServerApiSchemaSlimEntitiesSlimExpression], None, Unset_Type
        ] = Unset

        if expressions is not Unset:
            self.expressions = expressions

    @property
    def expressions(
        self,
    ) -> (
        "Union[List[GrantaServerApiSchemaSlimEntitiesSlimExpression], None, Unset_Type]"
    ):
        """Gets the expressions of this GrantaServerApiSchemaExpressionsExpressionsInfo.

        Returns
        -------
        Union[List[GrantaServerApiSchemaSlimEntitiesSlimExpression], None, Unset_Type]
            The expressions of this GrantaServerApiSchemaExpressionsExpressionsInfo.
        """
        return self._expressions

    @expressions.setter
    def expressions(
        self,
        expressions: "Union[List[GrantaServerApiSchemaSlimEntitiesSlimExpression], None, Unset_Type]",
    ) -> None:
        """Sets the expressions of this GrantaServerApiSchemaExpressionsExpressionsInfo.

        Parameters
        ----------
        expressions: Union[List[GrantaServerApiSchemaSlimEntitiesSlimExpression], None, Unset_Type]
            The expressions of this GrantaServerApiSchemaExpressionsExpressionsInfo.
        """
        self._expressions = expressions

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
        if not isinstance(other, GrantaServerApiSchemaExpressionsExpressionsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
