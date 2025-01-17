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
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase

if TYPE_CHECKING:
    from . import *


class GrantaServerApiIntegrationSchemaIntegrationParameterInfo(ModelBase):
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
        "default_value": "GrantaServerApiDataExportDatumsParameterValue",
        "guid": "str",
        "identity": "int",
        "interpolation_type": "GrantaServerApiParameterInfoInterpolationType",
        "name": "str",
        "parameter_type": "GrantaServerApiParameterInfoParameterType",
        "scale_type": "GrantaServerApiParameterInfoScaleType",
        "unit_symbol": "str",
    }

    attribute_map = {
        "default_value": "defaultValue",
        "guid": "guid",
        "identity": "identity",
        "interpolation_type": "interpolationType",
        "name": "name",
        "parameter_type": "parameterType",
        "scale_type": "scaleType",
        "unit_symbol": "unitSymbol",
    }

    subtype_mapping = {
        "scaleType": "GrantaServerApiParameterInfoScaleType",
        "interpolationType": "GrantaServerApiParameterInfoInterpolationType",
        "parameterType": "GrantaServerApiParameterInfoParameterType",
        "defaultValue": "GrantaServerApiDataExportDatumsParameterValue",
    }

    discriminator = None

    def __init__(
        self,
        *,
        default_value: "Optional[GrantaServerApiDataExportDatumsParameterValue]" = None,
        guid: "Optional[str]" = None,
        identity: "Optional[int]" = None,
        interpolation_type: "Optional[GrantaServerApiParameterInfoInterpolationType]" = None,
        name: "Optional[str]" = None,
        parameter_type: "Optional[GrantaServerApiParameterInfoParameterType]" = None,
        scale_type: "Optional[GrantaServerApiParameterInfoScaleType]" = None,
        unit_symbol: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiIntegrationSchemaIntegrationParameterInfo - a model defined in Swagger

        Parameters
        ----------
            default_value: GrantaServerApiDataExportDatumsParameterValue, optional
            guid: str, optional
            identity: int, optional
            interpolation_type: GrantaServerApiParameterInfoInterpolationType, optional
            name: str, optional
            parameter_type: GrantaServerApiParameterInfoParameterType, optional
            scale_type: GrantaServerApiParameterInfoScaleType, optional
            unit_symbol: str, optional
        """
        self._name = None
        self._identity = None
        self._guid = None
        self._unit_symbol = None
        self._scale_type = None
        self._interpolation_type = None
        self._parameter_type = None
        self._default_value = None

        if name is not None:
            self.name = name
        if identity is not None:
            self.identity = identity
        if guid is not None:
            self.guid = guid
        if unit_symbol is not None:
            self.unit_symbol = unit_symbol
        if scale_type is not None:
            self.scale_type = scale_type
        if interpolation_type is not None:
            self.interpolation_type = interpolation_type
        if parameter_type is not None:
            self.parameter_type = parameter_type
        if default_value is not None:
            self.default_value = default_value

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.

        Returns
        -------
        str
            The name of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.
        """
        self._name = name

    @property
    def identity(self) -> "int":
        """Gets the identity of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.

        Returns
        -------
        int
            The identity of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.
        """
        return self._identity

    @identity.setter
    def identity(self, identity: "int") -> None:
        """Sets the identity of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.

        Parameters
        ----------
        identity: int
            The identity of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.
        """
        self._identity = identity

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.

        Returns
        -------
        str
            The guid of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.
        """
        self._guid = guid

    @property
    def unit_symbol(self) -> "str":
        """Gets the unit_symbol of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.

        Returns
        -------
        str
            The unit_symbol of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.
        """
        return self._unit_symbol

    @unit_symbol.setter
    def unit_symbol(self, unit_symbol: "str") -> None:
        """Sets the unit_symbol of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.

        Parameters
        ----------
        unit_symbol: str
            The unit_symbol of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.
        """
        self._unit_symbol = unit_symbol

    @property
    def scale_type(self) -> "GrantaServerApiParameterInfoScaleType":
        """Gets the scale_type of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.

        Returns
        -------
        GrantaServerApiParameterInfoScaleType
            The scale_type of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.
        """
        return self._scale_type

    @scale_type.setter
    def scale_type(self, scale_type: "GrantaServerApiParameterInfoScaleType") -> None:
        """Sets the scale_type of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.

        Parameters
        ----------
        scale_type: GrantaServerApiParameterInfoScaleType
            The scale_type of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.
        """
        self._scale_type = scale_type

    @property
    def interpolation_type(self) -> "GrantaServerApiParameterInfoInterpolationType":
        """Gets the interpolation_type of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.

        Returns
        -------
        GrantaServerApiParameterInfoInterpolationType
            The interpolation_type of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.
        """
        return self._interpolation_type

    @interpolation_type.setter
    def interpolation_type(
        self, interpolation_type: "GrantaServerApiParameterInfoInterpolationType"
    ) -> None:
        """Sets the interpolation_type of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.

        Parameters
        ----------
        interpolation_type: GrantaServerApiParameterInfoInterpolationType
            The interpolation_type of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.
        """
        self._interpolation_type = interpolation_type

    @property
    def parameter_type(self) -> "GrantaServerApiParameterInfoParameterType":
        """Gets the parameter_type of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.

        Returns
        -------
        GrantaServerApiParameterInfoParameterType
            The parameter_type of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.
        """
        return self._parameter_type

    @parameter_type.setter
    def parameter_type(self, parameter_type: "GrantaServerApiParameterInfoParameterType") -> None:
        """Sets the parameter_type of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.

        Parameters
        ----------
        parameter_type: GrantaServerApiParameterInfoParameterType
            The parameter_type of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.
        """
        self._parameter_type = parameter_type

    @property
    def default_value(self) -> "GrantaServerApiDataExportDatumsParameterValue":
        """Gets the default_value of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.

        Returns
        -------
        GrantaServerApiDataExportDatumsParameterValue
            The default_value of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value: "GrantaServerApiDataExportDatumsParameterValue") -> None:
        """Sets the default_value of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.

        Parameters
        ----------
        default_value: GrantaServerApiDataExportDatumsParameterValue
            The default_value of this GrantaServerApiIntegrationSchemaIntegrationParameterInfo.
        """
        self._default_value = default_value

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
        if not isinstance(other, GrantaServerApiIntegrationSchemaIntegrationParameterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
