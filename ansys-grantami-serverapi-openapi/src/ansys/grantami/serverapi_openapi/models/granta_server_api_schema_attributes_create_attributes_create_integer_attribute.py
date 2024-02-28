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
from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_attributes_create_attributes_create_attribute import (
    GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaAttributesCreateAttributesCreateIntegerAttribute(
    GrantaServerApiSchemaAttributesCreateAttributesCreateAttribute
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
        "name": "str",
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "axis_name": "str",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "guid": "str",
        "help_path": "str",
        "is_unique": "bool",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "name": "name",
        "about_attribute": "aboutAttribute",
        "axis_name": "axisName",
        "default_threshold_type": "defaultThresholdType",
        "guid": "guid",
        "help_path": "helpPath",
        "is_unique": "isUnique",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        name: "str",
        about_attribute: "Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]" = Unset,
        axis_name: "Union[str, None, Unset_Type]" = Unset,
        default_threshold_type: "Union[GrantaServerApiSchemaAttributesAttributeThresholdType, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
        help_path: "Union[str, None, Unset_Type]" = Unset,
        is_unique: "Union[bool, Unset_Type]" = Unset,
        type: "str" = "integer",
    ) -> None:
        """GrantaServerApiSchemaAttributesCreateAttributesCreateIntegerAttribute - a model defined in Swagger

        Parameters
        ----------
        name: str
        about_attribute: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
        axis_name: str, optional
        default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType, optional
        guid: str, optional
        help_path: str, optional
        is_unique: bool, optional
        type: str
        """
        super().__init__(
            name=name,
            about_attribute=about_attribute,
            default_threshold_type=default_threshold_type,
            guid=guid,
            help_path=help_path,
        )
        self._type: str
        self._is_unique: Union[bool, Unset_Type] = Unset
        self._axis_name: Union[str, None, Unset_Type] = Unset

        self.type = type
        if is_unique is not Unset:
            self.is_unique = is_unique
        if axis_name is not Unset:
            self.axis_name = axis_name

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaAttributesCreateAttributesCreateIntegerAttribute.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaAttributesCreateAttributesCreateIntegerAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaAttributesCreateAttributesCreateIntegerAttribute.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaAttributesCreateAttributesCreateIntegerAttribute.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @property
    def is_unique(self) -> "Union[bool, Unset_Type]":
        """Gets the is_unique of this GrantaServerApiSchemaAttributesCreateAttributesCreateIntegerAttribute.
        Whether or not the attribute is constrained to contain a unique value

        Returns
        -------
        Union[bool, Unset_Type]
            The is_unique of this GrantaServerApiSchemaAttributesCreateAttributesCreateIntegerAttribute.
        """
        return self._is_unique

    @is_unique.setter
    def is_unique(self, is_unique: "Union[bool, Unset_Type]") -> None:
        """Sets the is_unique of this GrantaServerApiSchemaAttributesCreateAttributesCreateIntegerAttribute.
        Whether or not the attribute is constrained to contain a unique value

        Parameters
        ----------
        is_unique: Union[bool, Unset_Type]
            The is_unique of this GrantaServerApiSchemaAttributesCreateAttributesCreateIntegerAttribute.
        """
        # Field is not nullable
        if is_unique is None:
            raise ValueError("Invalid value for 'is_unique', must not be 'None'")
        self._is_unique = is_unique

    @property
    def axis_name(self) -> "Union[str, None, Unset_Type]":
        """Gets the axis_name of this GrantaServerApiSchemaAttributesCreateAttributesCreateIntegerAttribute.

        Returns
        -------
        Union[str, None, Unset_Type]
            The axis_name of this GrantaServerApiSchemaAttributesCreateAttributesCreateIntegerAttribute.
        """
        return self._axis_name

    @axis_name.setter
    def axis_name(self, axis_name: "Union[str, None, Unset_Type]") -> None:
        """Sets the axis_name of this GrantaServerApiSchemaAttributesCreateAttributesCreateIntegerAttribute.

        Parameters
        ----------
        axis_name: Union[str, None, Unset_Type]
            The axis_name of this GrantaServerApiSchemaAttributesCreateAttributesCreateIntegerAttribute.
        """
        self._axis_name = axis_name

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
        if not isinstance(
            other, GrantaServerApiSchemaAttributesCreateAttributesCreateIntegerAttribute
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
