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
from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_parameters_update_parameter_value import (
    GrantaServerApiSchemaParametersUpdateParameterValue,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSchemaParametersUpdateNumericParameterValue(
    GrantaServerApiSchemaParametersUpdateParameterValue
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
        "guid": "str",
        "name": "str",
        "type": "str",
        "value": "float",
    }

    attribute_map: Dict[str, str] = {
        "guid": "guid",
        "name": "name",
        "type": "type",
        "value": "value",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        guid: "Union[str, Unset_Type]" = Unset,
        name: "Union[str, None, Unset_Type]" = Unset,
        type: "str" = "numeric",
        value: "Union[float, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaParametersUpdateNumericParameterValue - a model defined in Swagger

        Parameters
        ----------
        guid: str, optional
        name: str, optional
        type: str
        value: float, optional
        """
        super().__init__(guid=guid)
        self._value: Union[float, Unset_Type] = Unset
        self._type: str
        self._name: Union[str, None, Unset_Type] = Unset

        if value is not Unset:
            self.value = value
        self.type = type
        if name is not Unset:
            self.name = name

    @property
    def value(self) -> "Union[float, Unset_Type]":
        """Gets the value of this GrantaServerApiSchemaParametersUpdateNumericParameterValue.

        Returns
        -------
        Union[float, Unset_Type]
            The value of this GrantaServerApiSchemaParametersUpdateNumericParameterValue.
        """
        return self._value

    @value.setter
    def value(self, value: "Union[float, Unset_Type]") -> None:
        """Sets the value of this GrantaServerApiSchemaParametersUpdateNumericParameterValue.

        Parameters
        ----------
        value: Union[float, Unset_Type]
            The value of this GrantaServerApiSchemaParametersUpdateNumericParameterValue.
        """
        # Field is not nullable
        if value is None:
            raise ValueError("Invalid value for 'value', must not be 'None'")
        self._value = value

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaParametersUpdateNumericParameterValue.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaParametersUpdateNumericParameterValue.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaParametersUpdateNumericParameterValue.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaParametersUpdateNumericParameterValue.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @property
    def name(self) -> "Union[str, None, Unset_Type]":
        """Gets the name of this GrantaServerApiSchemaParametersUpdateNumericParameterValue.

        Returns
        -------
        Union[str, None, Unset_Type]
            The name of this GrantaServerApiSchemaParametersUpdateNumericParameterValue.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, None, Unset_Type]") -> None:
        """Sets the name of this GrantaServerApiSchemaParametersUpdateNumericParameterValue.

        Parameters
        ----------
        name: Union[str, None, Unset_Type]
            The name of this GrantaServerApiSchemaParametersUpdateNumericParameterValue.
        """
        self._name = name

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
            other, GrantaServerApiSchemaParametersUpdateNumericParameterValue
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
