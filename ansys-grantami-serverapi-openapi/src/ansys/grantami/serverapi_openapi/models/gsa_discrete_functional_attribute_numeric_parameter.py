"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.models.gsa_discrete_functional_attribute_parameter import GsaDiscreteFunctionalAttributeParameter  # noqa: F401
from ansys.grantami.serverapi_openapi.models.gsa_parameter_type import GsaParameterType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaDiscreteFunctionalAttributeNumericParameter(GsaDiscreteFunctionalAttributeParameter):
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
        "parameter": "GsaSlimNamedEntity",
        "type": "GsaParameterType",
        "default_value": "float",
    }

    attribute_map: dict[str, str] = {
        "parameter": "parameter",
        "type": "type",
        "default_value": "defaultValue",
    }

    subtype_mapping: dict[str, str] = {
    }

    discriminator: Optional[str] = None

    def __init__(self, *, parameter: "GsaSlimNamedEntity", type: "GsaParameterType" = GsaParameterType.NUMERIC, default_value: "Union[float, None, Unset_Type]" = Unset,) -> None:
        """GsaDiscreteFunctionalAttributeNumericParameter - a model defined in Swagger

        Parameters
        ----------
        parameter: GsaSlimNamedEntity
        type: GsaParameterType
        default_value: float, optional
        """
        super().__init__(parameter=parameter, type=type)
        self._default_value: Union[float, None, Unset_Type] = Unset

        if default_value is not Unset:
            self.default_value = default_value

    @property
    def default_value(self) -> "Union[float, None, Unset_Type]":
        """Gets the default_value of this GsaDiscreteFunctionalAttributeNumericParameter.
        If there is no default value, fallback to the parameter default.

        Returns
        -------
        Union[float, None, Unset_Type]
            The default_value of this GsaDiscreteFunctionalAttributeNumericParameter.
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value: "Union[float, None, Unset_Type]") -> None:
        """Sets the default_value of this GsaDiscreteFunctionalAttributeNumericParameter.
        If there is no default value, fallback to the parameter default.

        Parameters
        ----------
        default_value: Union[float, None, Unset_Type]
            The default_value of this GsaDiscreteFunctionalAttributeNumericParameter.
        """
        self._default_value = default_value

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
        if not isinstance(other, GsaDiscreteFunctionalAttributeNumericParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

