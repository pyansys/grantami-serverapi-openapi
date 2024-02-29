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


class GrantaServerApiParameterInfo(ModelBase):
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
        "default_value": "GrantaServerApiDataExportDatumsParameterValue",
        "identity": "int",
        "interpolation_type": "GrantaServerApiParameterInfoInterpolationType",
        "name": "str",
        "parameter_type": "GrantaServerApiParameterInfoParameterType",
        "scale_type": "GrantaServerApiParameterInfoScaleType",
        "unit_symbol": "str",
    }

    attribute_map: Dict[str, str] = {
        "default_value": "defaultValue",
        "identity": "identity",
        "interpolation_type": "interpolationType",
        "name": "name",
        "parameter_type": "parameterType",
        "scale_type": "scaleType",
        "unit_symbol": "unitSymbol",
    }

    subtype_mapping: Dict[str, str] = {
        "scaleType": "GrantaServerApiParameterInfoScaleType",
        "interpolationType": "GrantaServerApiParameterInfoInterpolationType",
        "parameterType": "GrantaServerApiParameterInfoParameterType",
        "defaultValue": "GrantaServerApiDataExportDatumsParameterValue",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        default_value: "Union[GrantaServerApiDataExportDatumsParameterValue, Unset_Type]" = Unset,
        identity: "Union[int, Unset_Type]" = Unset,
        interpolation_type: "Union[GrantaServerApiParameterInfoInterpolationType, Unset_Type]" = Unset,
        name: "Union[str, None, Unset_Type]" = Unset,
        parameter_type: "Union[GrantaServerApiParameterInfoParameterType, Unset_Type]" = Unset,
        scale_type: "Union[GrantaServerApiParameterInfoScaleType, Unset_Type]" = Unset,
        unit_symbol: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiParameterInfo - a model defined in Swagger

        Parameters
        ----------
        default_value: GrantaServerApiDataExportDatumsParameterValue, optional
        identity: int, optional
        interpolation_type: GrantaServerApiParameterInfoInterpolationType, optional
        name: str, optional
        parameter_type: GrantaServerApiParameterInfoParameterType, optional
        scale_type: GrantaServerApiParameterInfoScaleType, optional
        unit_symbol: str, optional
        """
        self._name: Union[str, None, Unset_Type] = Unset
        self._identity: Union[int, Unset_Type] = Unset
        self._unit_symbol: Union[str, None, Unset_Type] = Unset
        self._scale_type: Union[GrantaServerApiParameterInfoScaleType, Unset_Type] = (
            Unset
        )
        self._interpolation_type: Union[
            GrantaServerApiParameterInfoInterpolationType, Unset_Type
        ] = Unset
        self._parameter_type: Union[
            GrantaServerApiParameterInfoParameterType, Unset_Type
        ] = Unset
        self._default_value: Union[
            GrantaServerApiDataExportDatumsParameterValue, Unset_Type
        ] = Unset

        if name is not Unset:
            self.name = name
        if identity is not Unset:
            self.identity = identity
        if unit_symbol is not Unset:
            self.unit_symbol = unit_symbol
        if scale_type is not Unset:
            self.scale_type = scale_type
        if interpolation_type is not Unset:
            self.interpolation_type = interpolation_type
        if parameter_type is not Unset:
            self.parameter_type = parameter_type
        if default_value is not Unset:
            self.default_value = default_value

    @property
    def name(self) -> "Union[str, None, Unset_Type]":
        """Gets the name of this GrantaServerApiParameterInfo.

        Returns
        -------
        Union[str, None, Unset_Type]
            The name of this GrantaServerApiParameterInfo.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, None, Unset_Type]") -> None:
        """Sets the name of this GrantaServerApiParameterInfo.

        Parameters
        ----------
        name: Union[str, None, Unset_Type]
            The name of this GrantaServerApiParameterInfo.
        """
        self._name = name

    @property
    def identity(self) -> "Union[int, Unset_Type]":
        """Gets the identity of this GrantaServerApiParameterInfo.

        Returns
        -------
        Union[int, Unset_Type]
            The identity of this GrantaServerApiParameterInfo.
        """
        return self._identity

    @identity.setter
    def identity(self, identity: "Union[int, Unset_Type]") -> None:
        """Sets the identity of this GrantaServerApiParameterInfo.

        Parameters
        ----------
        identity: Union[int, Unset_Type]
            The identity of this GrantaServerApiParameterInfo.
        """
        # Field is not nullable
        if identity is None:
            raise ValueError("Invalid value for 'identity', must not be 'None'")
        self._identity = identity

    @property
    def unit_symbol(self) -> "Union[str, None, Unset_Type]":
        """Gets the unit_symbol of this GrantaServerApiParameterInfo.

        Returns
        -------
        Union[str, None, Unset_Type]
            The unit_symbol of this GrantaServerApiParameterInfo.
        """
        return self._unit_symbol

    @unit_symbol.setter
    def unit_symbol(self, unit_symbol: "Union[str, None, Unset_Type]") -> None:
        """Sets the unit_symbol of this GrantaServerApiParameterInfo.

        Parameters
        ----------
        unit_symbol: Union[str, None, Unset_Type]
            The unit_symbol of this GrantaServerApiParameterInfo.
        """
        self._unit_symbol = unit_symbol

    @property
    def scale_type(self) -> "Union[GrantaServerApiParameterInfoScaleType, Unset_Type]":
        """Gets the scale_type of this GrantaServerApiParameterInfo.

        Returns
        -------
        Union[GrantaServerApiParameterInfoScaleType, Unset_Type]
            The scale_type of this GrantaServerApiParameterInfo.
        """
        return self._scale_type

    @scale_type.setter
    def scale_type(
        self, scale_type: "Union[GrantaServerApiParameterInfoScaleType, Unset_Type]"
    ) -> None:
        """Sets the scale_type of this GrantaServerApiParameterInfo.

        Parameters
        ----------
        scale_type: Union[GrantaServerApiParameterInfoScaleType, Unset_Type]
            The scale_type of this GrantaServerApiParameterInfo.
        """
        # Field is not nullable
        if scale_type is None:
            raise ValueError("Invalid value for 'scale_type', must not be 'None'")
        self._scale_type = scale_type

    @property
    def interpolation_type(
        self,
    ) -> "Union[GrantaServerApiParameterInfoInterpolationType, Unset_Type]":
        """Gets the interpolation_type of this GrantaServerApiParameterInfo.

        Returns
        -------
        Union[GrantaServerApiParameterInfoInterpolationType, Unset_Type]
            The interpolation_type of this GrantaServerApiParameterInfo.
        """
        return self._interpolation_type

    @interpolation_type.setter
    def interpolation_type(
        self,
        interpolation_type: "Union[GrantaServerApiParameterInfoInterpolationType, Unset_Type]",
    ) -> None:
        """Sets the interpolation_type of this GrantaServerApiParameterInfo.

        Parameters
        ----------
        interpolation_type: Union[GrantaServerApiParameterInfoInterpolationType, Unset_Type]
            The interpolation_type of this GrantaServerApiParameterInfo.
        """
        # Field is not nullable
        if interpolation_type is None:
            raise ValueError(
                "Invalid value for 'interpolation_type', must not be 'None'"
            )
        self._interpolation_type = interpolation_type

    @property
    def parameter_type(
        self,
    ) -> "Union[GrantaServerApiParameterInfoParameterType, Unset_Type]":
        """Gets the parameter_type of this GrantaServerApiParameterInfo.

        Returns
        -------
        Union[GrantaServerApiParameterInfoParameterType, Unset_Type]
            The parameter_type of this GrantaServerApiParameterInfo.
        """
        return self._parameter_type

    @parameter_type.setter
    def parameter_type(
        self,
        parameter_type: "Union[GrantaServerApiParameterInfoParameterType, Unset_Type]",
    ) -> None:
        """Sets the parameter_type of this GrantaServerApiParameterInfo.

        Parameters
        ----------
        parameter_type: Union[GrantaServerApiParameterInfoParameterType, Unset_Type]
            The parameter_type of this GrantaServerApiParameterInfo.
        """
        # Field is not nullable
        if parameter_type is None:
            raise ValueError("Invalid value for 'parameter_type', must not be 'None'")
        self._parameter_type = parameter_type

    @property
    def default_value(
        self,
    ) -> "Union[GrantaServerApiDataExportDatumsParameterValue, Unset_Type]":
        """Gets the default_value of this GrantaServerApiParameterInfo.

        Returns
        -------
        Union[GrantaServerApiDataExportDatumsParameterValue, Unset_Type]
            The default_value of this GrantaServerApiParameterInfo.
        """
        return self._default_value

    @default_value.setter
    def default_value(
        self,
        default_value: "Union[GrantaServerApiDataExportDatumsParameterValue, Unset_Type]",
    ) -> None:
        """Sets the default_value of this GrantaServerApiParameterInfo.

        Parameters
        ----------
        default_value: Union[GrantaServerApiDataExportDatumsParameterValue, Unset_Type]
            The default_value of this GrantaServerApiParameterInfo.
        """
        # Field is not nullable
        if default_value is None:
            raise ValueError("Invalid value for 'default_value', must not be 'None'")
        self._default_value = default_value

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
        if not isinstance(other, GrantaServerApiParameterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
