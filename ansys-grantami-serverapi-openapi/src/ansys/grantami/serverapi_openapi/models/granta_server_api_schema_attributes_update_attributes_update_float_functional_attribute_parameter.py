# Copyright (C) 2023 - 2024 ANSYS, Inc. and/or its affiliates.
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
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSchemaAttributesUpdateAttributesUpdateFloatFunctionalAttributeParameter(
    ModelBase
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
        "default_value": "float",
        "interpolation_method": "GrantaServerApiSchemaAttributesAttributeInterpolationMethod",
        "parameter_guid": "str",
        "scale_type": "GrantaServerApiSchemaAttributesAttributeScaleType",
    }

    attribute_map: Dict[str, str] = {
        "default_value": "defaultValue",
        "interpolation_method": "interpolationMethod",
        "parameter_guid": "parameterGuid",
        "scale_type": "scaleType",
    }

    subtype_mapping: Dict[str, str] = {
        "interpolationMethod": "GrantaServerApiSchemaAttributesAttributeInterpolationMethod",
        "scaleType": "GrantaServerApiSchemaAttributesAttributeScaleType",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        default_value: "Union[float, None, Unset_Type]" = Unset,
        interpolation_method: "Union[GrantaServerApiSchemaAttributesAttributeInterpolationMethod, Unset_Type]" = Unset,
        parameter_guid: "Union[str, Unset_Type]" = Unset,
        scale_type: "Union[GrantaServerApiSchemaAttributesAttributeScaleType, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaAttributesUpdateAttributesUpdateFloatFunctionalAttributeParameter - a model defined in Swagger

        Parameters
        ----------
        default_value: float, optional
        interpolation_method: GrantaServerApiSchemaAttributesAttributeInterpolationMethod, optional
        parameter_guid: str, optional
        scale_type: GrantaServerApiSchemaAttributesAttributeScaleType, optional
        """
        self._parameter_guid: Union[str, Unset_Type] = Unset
        self._default_value: Union[float, None, Unset_Type] = Unset
        self._interpolation_method: Union[
            GrantaServerApiSchemaAttributesAttributeInterpolationMethod, Unset_Type
        ] = Unset
        self._scale_type: Union[
            GrantaServerApiSchemaAttributesAttributeScaleType, Unset_Type
        ] = Unset

        if parameter_guid is not Unset:
            self.parameter_guid = parameter_guid
        if default_value is not Unset:
            self.default_value = default_value
        if interpolation_method is not Unset:
            self.interpolation_method = interpolation_method
        if scale_type is not Unset:
            self.scale_type = scale_type

    @property
    def parameter_guid(self) -> "Union[str, Unset_Type]":
        """Gets the parameter_guid of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateFloatFunctionalAttributeParameter.

        Returns
        -------
        Union[str, Unset_Type]
            The parameter_guid of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateFloatFunctionalAttributeParameter.
        """
        return self._parameter_guid

    @parameter_guid.setter
    def parameter_guid(self, parameter_guid: "Union[str, Unset_Type]") -> None:
        """Sets the parameter_guid of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateFloatFunctionalAttributeParameter.

        Parameters
        ----------
        parameter_guid: Union[str, Unset_Type]
            The parameter_guid of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateFloatFunctionalAttributeParameter.
        """
        # Field is not nullable
        if parameter_guid is None:
            raise ValueError("Invalid value for 'parameter_guid', must not be 'None'")
        self._parameter_guid = parameter_guid

    @property
    def default_value(self) -> "Union[float, None, Unset_Type]":
        """Gets the default_value of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateFloatFunctionalAttributeParameter.

        Returns
        -------
        Union[float, None, Unset_Type]
            The default_value of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateFloatFunctionalAttributeParameter.
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value: "Union[float, None, Unset_Type]") -> None:
        """Sets the default_value of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateFloatFunctionalAttributeParameter.

        Parameters
        ----------
        default_value: Union[float, None, Unset_Type]
            The default_value of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateFloatFunctionalAttributeParameter.
        """
        self._default_value = default_value

    @property
    def interpolation_method(
        self,
    ) -> (
        "Union[GrantaServerApiSchemaAttributesAttributeInterpolationMethod, Unset_Type]"
    ):
        """Gets the interpolation_method of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateFloatFunctionalAttributeParameter.

        Returns
        -------
        Union[GrantaServerApiSchemaAttributesAttributeInterpolationMethod, Unset_Type]
            The interpolation_method of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateFloatFunctionalAttributeParameter.
        """
        return self._interpolation_method

    @interpolation_method.setter
    def interpolation_method(
        self,
        interpolation_method: "Union[GrantaServerApiSchemaAttributesAttributeInterpolationMethod, Unset_Type]",
    ) -> None:
        """Sets the interpolation_method of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateFloatFunctionalAttributeParameter.

        Parameters
        ----------
        interpolation_method: Union[GrantaServerApiSchemaAttributesAttributeInterpolationMethod, Unset_Type]
            The interpolation_method of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateFloatFunctionalAttributeParameter.
        """
        # Field is not nullable
        if interpolation_method is None:
            raise ValueError(
                "Invalid value for 'interpolation_method', must not be 'None'"
            )
        self._interpolation_method = interpolation_method

    @property
    def scale_type(
        self,
    ) -> "Union[GrantaServerApiSchemaAttributesAttributeScaleType, Unset_Type]":
        """Gets the scale_type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateFloatFunctionalAttributeParameter.

        Returns
        -------
        Union[GrantaServerApiSchemaAttributesAttributeScaleType, Unset_Type]
            The scale_type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateFloatFunctionalAttributeParameter.
        """
        return self._scale_type

    @scale_type.setter
    def scale_type(
        self,
        scale_type: "Union[GrantaServerApiSchemaAttributesAttributeScaleType, Unset_Type]",
    ) -> None:
        """Sets the scale_type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateFloatFunctionalAttributeParameter.

        Parameters
        ----------
        scale_type: Union[GrantaServerApiSchemaAttributesAttributeScaleType, Unset_Type]
            The scale_type of this GrantaServerApiSchemaAttributesUpdateAttributesUpdateFloatFunctionalAttributeParameter.
        """
        # Field is not nullable
        if scale_type is None:
            raise ValueError("Invalid value for 'scale_type', must not be 'None'")
        self._scale_type = scale_type

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
            GrantaServerApiSchemaAttributesUpdateAttributesUpdateFloatFunctionalAttributeParameter,
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
