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
from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_attributes_update_attributes_update_attribute import (
    GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteFunctionalAttribute(
    GrantaServerApiSchemaAttributesUpdateAttributesUpdateAttribute
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
        "about_attribute": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "attribute_parameters": "list[GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteFunctionalAttributeParameter]",
        "axis_name": "str",
        "default_threshold_type": "GrantaServerApiSchemaAttributesAttributeThresholdType",
        "guid": "str",
        "help_path": "str",
        "name": "str",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "about_attribute": "aboutAttribute",
        "attribute_parameters": "attributeParameters",
        "axis_name": "axisName",
        "default_threshold_type": "defaultThresholdType",
        "guid": "guid",
        "help_path": "helpPath",
        "name": "name",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {
        "attributeParameters": "GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteFunctionalAttributeParameter",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        about_attribute: "Union[GrantaServerApiSchemaSlimEntitiesSlimEntity, Unset_Type]" = Unset,
        attribute_parameters: "Union[List[GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteFunctionalAttributeParameter], Unset_Type]" = Unset,
        axis_name: "Union[str, None, Unset_Type]" = Unset,
        default_threshold_type: "Union[GrantaServerApiSchemaAttributesAttributeThresholdType, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
        help_path: "Union[str, None, Unset_Type]" = Unset,
        name: "Union[str, Unset_Type]" = Unset,
        type: "str" = "discreteFunctional",
    ) -> None:
        """GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteFunctionalAttribute - a model defined in Swagger

        Parameters
        ----------
        about_attribute: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
        attribute_parameters: List[GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteFunctionalAttributeParameter], optional
        axis_name: str, optional
        default_threshold_type: GrantaServerApiSchemaAttributesAttributeThresholdType, optional
        guid: str, optional
        help_path: str, optional
        name: str, optional
        type: str
        """
        super().__init__(
            about_attribute=about_attribute,
            axis_name=axis_name,
            default_threshold_type=default_threshold_type,
            guid=guid,
            help_path=help_path,
            name=name,
        )
        self._type: str
        self._attribute_parameters: Union[
            List[
                GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteFunctionalAttributeParameter
            ],
            Unset_Type,
        ] = Unset

        self.type = type
        if attribute_parameters is not Unset:
            self.attribute_parameters = attribute_parameters

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteFunctionalAttribute.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteFunctionalAttribute.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteFunctionalAttribute.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteFunctionalAttribute.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @property
    def attribute_parameters(
        self,
    ) -> "Union[List[GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteFunctionalAttributeParameter], Unset_Type]":
        """Gets the attribute_parameters of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteFunctionalAttribute.

        Returns
        -------
        Union[List[GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteFunctionalAttributeParameter], Unset_Type]
            The attribute_parameters of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteFunctionalAttribute.
        """
        return self._attribute_parameters

    @attribute_parameters.setter
    def attribute_parameters(
        self,
        attribute_parameters: "Union[List[GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteFunctionalAttributeParameter], Unset_Type]",
    ) -> None:
        """Sets the attribute_parameters of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteFunctionalAttribute.

        Parameters
        ----------
        attribute_parameters: Union[List[GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteFunctionalAttributeParameter], Unset_Type]
            The attribute_parameters of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteFunctionalAttribute.
        """
        # Field is not nullable
        if attribute_parameters is None:
            raise ValueError(
                "Invalid value for 'attribute_parameters', must not be 'None'"
            )
        self._attribute_parameters = attribute_parameters

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
            other,
            GrantaServerApiSchemaAttributesUpdateAttributesUpdateDiscreteFunctionalAttribute,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
