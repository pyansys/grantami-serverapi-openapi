# Copyright (C) 2023 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaIntegrationParameterInfo(ModelBase):
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
        "default_value": "GsaDataExportParameterValue",
        "guid": "str",
        "identity": "int",
        "interpolation_type": "GsaParameterInfoInterpolationType",
        "name": "str",
        "parameter_type": "GsaParameterInfoParameterType",
        "scale_type": "GsaParameterInfoScaleType",
        "unit_symbol": "str",
    }

    attribute_map: dict[str, str] = {
        "default_value": "defaultValue",
        "guid": "guid",
        "identity": "identity",
        "interpolation_type": "interpolationType",
        "name": "name",
        "parameter_type": "parameterType",
        "scale_type": "scaleType",
        "unit_symbol": "unitSymbol",
    }

    subtype_mapping: dict[str, str] = {
        "scaleType": "GsaParameterInfoScaleType",
        "interpolationType": "GsaParameterInfoInterpolationType",
        "parameterType": "GsaParameterInfoParameterType",
        "defaultValue": "GsaDataExportParameterValue",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        default_value: "Union[GsaDataExportParameterValue, Unset_Type]" = Unset,
        guid: "Union[str, None, Unset_Type]" = Unset,
        identity: "Union[int, Unset_Type]" = Unset,
        interpolation_type: "Union[GsaParameterInfoInterpolationType, Unset_Type]" = Unset,
        name: "Union[str, None, Unset_Type]" = Unset,
        parameter_type: "Union[GsaParameterInfoParameterType, Unset_Type]" = Unset,
        scale_type: "Union[GsaParameterInfoScaleType, Unset_Type]" = Unset,
        unit_symbol: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaIntegrationParameterInfo - a model defined in Swagger

        Parameters
        ----------
        default_value: GsaDataExportParameterValue, optional
        guid: str, optional
        identity: int, optional
        interpolation_type: GsaParameterInfoInterpolationType, optional
        name: str, optional
        parameter_type: GsaParameterInfoParameterType, optional
        scale_type: GsaParameterInfoScaleType, optional
        unit_symbol: str, optional
        """
        self._name: Union[str, None, Unset_Type] = Unset
        self._identity: Union[int, Unset_Type] = Unset
        self._guid: Union[str, None, Unset_Type] = Unset
        self._unit_symbol: Union[str, None, Unset_Type] = Unset
        self._scale_type: Union[GsaParameterInfoScaleType, Unset_Type] = Unset
        self._interpolation_type: Union[GsaParameterInfoInterpolationType, Unset_Type] = Unset
        self._parameter_type: Union[GsaParameterInfoParameterType, Unset_Type] = Unset
        self._default_value: Union[GsaDataExportParameterValue, Unset_Type] = Unset

        if name is not Unset:
            self.name = name
        if identity is not Unset:
            self.identity = identity
        if guid is not Unset:
            self.guid = guid
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
        """Gets the name of this GsaIntegrationParameterInfo.

        Returns
        -------
        Union[str, None, Unset_Type]
            The name of this GsaIntegrationParameterInfo.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, None, Unset_Type]") -> None:
        """Sets the name of this GsaIntegrationParameterInfo.

        Parameters
        ----------
        name: Union[str, None, Unset_Type]
            The name of this GsaIntegrationParameterInfo.
        """
        self._name = name

    @property
    def identity(self) -> "Union[int, Unset_Type]":
        """Gets the identity of this GsaIntegrationParameterInfo.

        Returns
        -------
        Union[int, Unset_Type]
            The identity of this GsaIntegrationParameterInfo.
        """
        return self._identity

    @identity.setter
    def identity(self, identity: "Union[int, Unset_Type]") -> None:
        """Sets the identity of this GsaIntegrationParameterInfo.

        Parameters
        ----------
        identity: Union[int, Unset_Type]
            The identity of this GsaIntegrationParameterInfo.
        """
        # Field is not nullable
        if identity is None:
            raise ValueError("Invalid value for 'identity', must not be 'None'")
        self._identity = identity

    @property
    def guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the guid of this GsaIntegrationParameterInfo.

        Returns
        -------
        Union[str, None, Unset_Type]
            The guid of this GsaIntegrationParameterInfo.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the guid of this GsaIntegrationParameterInfo.

        Parameters
        ----------
        guid: Union[str, None, Unset_Type]
            The guid of this GsaIntegrationParameterInfo.
        """
        self._guid = guid

    @property
    def unit_symbol(self) -> "Union[str, None, Unset_Type]":
        """Gets the unit_symbol of this GsaIntegrationParameterInfo.

        Returns
        -------
        Union[str, None, Unset_Type]
            The unit_symbol of this GsaIntegrationParameterInfo.
        """
        return self._unit_symbol

    @unit_symbol.setter
    def unit_symbol(self, unit_symbol: "Union[str, None, Unset_Type]") -> None:
        """Sets the unit_symbol of this GsaIntegrationParameterInfo.

        Parameters
        ----------
        unit_symbol: Union[str, None, Unset_Type]
            The unit_symbol of this GsaIntegrationParameterInfo.
        """
        self._unit_symbol = unit_symbol

    @property
    def scale_type(self) -> "Union[GsaParameterInfoScaleType, Unset_Type]":
        """Gets the scale_type of this GsaIntegrationParameterInfo.

        Returns
        -------
        Union[GsaParameterInfoScaleType, Unset_Type]
            The scale_type of this GsaIntegrationParameterInfo.
        """
        return self._scale_type

    @scale_type.setter
    def scale_type(self, scale_type: "Union[GsaParameterInfoScaleType, Unset_Type]") -> None:
        """Sets the scale_type of this GsaIntegrationParameterInfo.

        Parameters
        ----------
        scale_type: Union[GsaParameterInfoScaleType, Unset_Type]
            The scale_type of this GsaIntegrationParameterInfo.
        """
        # Field is not nullable
        if scale_type is None:
            raise ValueError("Invalid value for 'scale_type', must not be 'None'")
        self._scale_type = scale_type

    @property
    def interpolation_type(self) -> "Union[GsaParameterInfoInterpolationType, Unset_Type]":
        """Gets the interpolation_type of this GsaIntegrationParameterInfo.

        Returns
        -------
        Union[GsaParameterInfoInterpolationType, Unset_Type]
            The interpolation_type of this GsaIntegrationParameterInfo.
        """
        return self._interpolation_type

    @interpolation_type.setter
    def interpolation_type(
        self, interpolation_type: "Union[GsaParameterInfoInterpolationType, Unset_Type]"
    ) -> None:
        """Sets the interpolation_type of this GsaIntegrationParameterInfo.

        Parameters
        ----------
        interpolation_type: Union[GsaParameterInfoInterpolationType, Unset_Type]
            The interpolation_type of this GsaIntegrationParameterInfo.
        """
        # Field is not nullable
        if interpolation_type is None:
            raise ValueError("Invalid value for 'interpolation_type', must not be 'None'")
        self._interpolation_type = interpolation_type

    @property
    def parameter_type(self) -> "Union[GsaParameterInfoParameterType, Unset_Type]":
        """Gets the parameter_type of this GsaIntegrationParameterInfo.

        Returns
        -------
        Union[GsaParameterInfoParameterType, Unset_Type]
            The parameter_type of this GsaIntegrationParameterInfo.
        """
        return self._parameter_type

    @parameter_type.setter
    def parameter_type(
        self, parameter_type: "Union[GsaParameterInfoParameterType, Unset_Type]"
    ) -> None:
        """Sets the parameter_type of this GsaIntegrationParameterInfo.

        Parameters
        ----------
        parameter_type: Union[GsaParameterInfoParameterType, Unset_Type]
            The parameter_type of this GsaIntegrationParameterInfo.
        """
        # Field is not nullable
        if parameter_type is None:
            raise ValueError("Invalid value for 'parameter_type', must not be 'None'")
        self._parameter_type = parameter_type

    @property
    def default_value(self) -> "Union[GsaDataExportParameterValue, Unset_Type]":
        """Gets the default_value of this GsaIntegrationParameterInfo.

        Returns
        -------
        Union[GsaDataExportParameterValue, Unset_Type]
            The default_value of this GsaIntegrationParameterInfo.
        """
        return self._default_value

    @default_value.setter
    def default_value(
        self, default_value: "Union[GsaDataExportParameterValue, Unset_Type]"
    ) -> None:
        """Sets the default_value of this GsaIntegrationParameterInfo.

        Parameters
        ----------
        default_value: Union[GsaDataExportParameterValue, Unset_Type]
            The default_value of this GsaIntegrationParameterInfo.
        """
        # Field is not nullable
        if default_value is None:
            raise ValueError("Invalid value for 'default_value', must not be 'None'")
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
        if not isinstance(other, GsaIntegrationParameterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
