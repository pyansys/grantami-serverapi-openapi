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
from ansys.grantami.serverapi_openapi.models.granta_server_api_search_parameter_constraint import (
    GrantaServerApiSearchParameterConstraint,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSearchNumericParameterConstraint(
    GrantaServerApiSearchParameterConstraint
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
        "gte": "float",
        "interpolation_type": "str",
        "lte": "float",
        "parameter": "GrantaServerApiObjectIdentifier",
        "scale_type": "str",
        "significant_figures": "int",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "gte": "gte",
        "interpolation_type": "interpolationType",
        "lte": "lte",
        "parameter": "parameter",
        "scale_type": "scaleType",
        "significant_figures": "significantFigures",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        gte: "Union[float, None, Unset_Type]" = Unset,
        interpolation_type: "Union[str, None, Unset_Type]" = Unset,
        lte: "Union[float, None, Unset_Type]" = Unset,
        parameter: "Union[GrantaServerApiObjectIdentifier, Unset_Type]" = Unset,
        scale_type: "Union[str, None, Unset_Type]" = Unset,
        significant_figures: "Union[int, None, Unset_Type]" = Unset,
        type: "str" = "numeric",
    ) -> None:
        """GrantaServerApiSearchNumericParameterConstraint - a model defined in Swagger

        Parameters
        ----------
        gte: float, optional
        interpolation_type: str, optional
        lte: float, optional
        parameter: GrantaServerApiObjectIdentifier, optional
        scale_type: str, optional
        significant_figures: int, optional
        type: str
        """
        super().__init__(parameter=parameter)
        self._gte: Union[float, None, Unset_Type] = Unset
        self._lte: Union[float, None, Unset_Type] = Unset
        self._scale_type: Union[str, None, Unset_Type] = Unset
        self._interpolation_type: Union[str, None, Unset_Type] = Unset
        self._significant_figures: Union[int, None, Unset_Type] = Unset
        self._type: str

        if gte is not Unset:
            self.gte = gte
        if lte is not Unset:
            self.lte = lte
        if scale_type is not Unset:
            self.scale_type = scale_type
        if interpolation_type is not Unset:
            self.interpolation_type = interpolation_type
        if significant_figures is not Unset:
            self.significant_figures = significant_figures
        self.type = type

    @property
    def gte(self) -> "Union[float, None, Unset_Type]":
        """Gets the gte of this GrantaServerApiSearchNumericParameterConstraint.

        Returns
        -------
        Union[float, None, Unset_Type]
            The gte of this GrantaServerApiSearchNumericParameterConstraint.
        """
        return self._gte

    @gte.setter
    def gte(self, gte: "Union[float, None, Unset_Type]") -> None:
        """Sets the gte of this GrantaServerApiSearchNumericParameterConstraint.

        Parameters
        ----------
        gte: Union[float, None, Unset_Type]
            The gte of this GrantaServerApiSearchNumericParameterConstraint.
        """
        self._gte = gte

    @property
    def lte(self) -> "Union[float, None, Unset_Type]":
        """Gets the lte of this GrantaServerApiSearchNumericParameterConstraint.

        Returns
        -------
        Union[float, None, Unset_Type]
            The lte of this GrantaServerApiSearchNumericParameterConstraint.
        """
        return self._lte

    @lte.setter
    def lte(self, lte: "Union[float, None, Unset_Type]") -> None:
        """Sets the lte of this GrantaServerApiSearchNumericParameterConstraint.

        Parameters
        ----------
        lte: Union[float, None, Unset_Type]
            The lte of this GrantaServerApiSearchNumericParameterConstraint.
        """
        self._lte = lte

    @property
    def scale_type(self) -> "Union[str, None, Unset_Type]":
        """Gets the scale_type of this GrantaServerApiSearchNumericParameterConstraint.
        Optionally, override the scale type of the parameter. Can be Linear or Log

        Returns
        -------
        Union[str, None, Unset_Type]
            The scale_type of this GrantaServerApiSearchNumericParameterConstraint.
        """
        return self._scale_type

    @scale_type.setter
    def scale_type(self, scale_type: "Union[str, None, Unset_Type]") -> None:
        """Sets the scale_type of this GrantaServerApiSearchNumericParameterConstraint.
        Optionally, override the scale type of the parameter. Can be Linear or Log

        Parameters
        ----------
        scale_type: Union[str, None, Unset_Type]
            The scale_type of this GrantaServerApiSearchNumericParameterConstraint.
        """
        self._scale_type = scale_type

    @property
    def interpolation_type(self) -> "Union[str, None, Unset_Type]":
        """Gets the interpolation_type of this GrantaServerApiSearchNumericParameterConstraint.
        Optionally, override the interpolation type of the parameter. Can be Auto, None, Linear or CubicSpline

        Returns
        -------
        Union[str, None, Unset_Type]
            The interpolation_type of this GrantaServerApiSearchNumericParameterConstraint.
        """
        return self._interpolation_type

    @interpolation_type.setter
    def interpolation_type(
        self, interpolation_type: "Union[str, None, Unset_Type]"
    ) -> None:
        """Sets the interpolation_type of this GrantaServerApiSearchNumericParameterConstraint.
        Optionally, override the interpolation type of the parameter. Can be Auto, None, Linear or CubicSpline

        Parameters
        ----------
        interpolation_type: Union[str, None, Unset_Type]
            The interpolation_type of this GrantaServerApiSearchNumericParameterConstraint.
        """
        self._interpolation_type = interpolation_type

    @property
    def significant_figures(self) -> "Union[int, None, Unset_Type]":
        """Gets the significant_figures of this GrantaServerApiSearchNumericParameterConstraint.

        Returns
        -------
        Union[int, None, Unset_Type]
            The significant_figures of this GrantaServerApiSearchNumericParameterConstraint.
        """
        return self._significant_figures

    @significant_figures.setter
    def significant_figures(
        self, significant_figures: "Union[int, None, Unset_Type]"
    ) -> None:
        """Sets the significant_figures of this GrantaServerApiSearchNumericParameterConstraint.

        Parameters
        ----------
        significant_figures: Union[int, None, Unset_Type]
            The significant_figures of this GrantaServerApiSearchNumericParameterConstraint.
        """
        self._significant_figures = significant_figures

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchNumericParameterConstraint.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchNumericParameterConstraint.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchNumericParameterConstraint.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchNumericParameterConstraint.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

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
        if not isinstance(other, GrantaServerApiSearchNumericParameterConstraint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
