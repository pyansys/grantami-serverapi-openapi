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

from ansys.grantami.serverapi_openapi.v252.models.gsa_attribute_type import GsaAttributeType
from ansys.grantami.serverapi_openapi.v252.models.gsa_create_attribute import (  # noqa: F401
    GsaCreateAttribute,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaCreateDiscreteFunctionalAttribute(GsaCreateAttribute):
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
        "attribute_parameters": "list[GsaCreateDiscreteFunctionalAttributeParameter]",
        "discrete_type": "GsaSlimEntity",
        "name": "str",
        "type": "GsaAttributeType",
        "default_threshold_type": "GsaAttributeThresholdType",
        "guid": "str",
        "help_path": "str",
        "is_hidden_from_search_criteria": "bool",
    }

    attribute_map: dict[str, str] = {
        "attribute_parameters": "attributeParameters",
        "discrete_type": "discreteType",
        "name": "name",
        "type": "type",
        "default_threshold_type": "defaultThresholdType",
        "guid": "guid",
        "help_path": "helpPath",
        "is_hidden_from_search_criteria": "isHiddenFromSearchCriteria",
    }

    subtype_mapping: dict[str, str] = {
        "discreteType": "GsaSlimEntity",
        "attributeParameters": "GsaCreateDiscreteFunctionalAttributeParameter",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_parameters: "list[GsaCreateDiscreteFunctionalAttributeParameter]",
        discrete_type: "GsaSlimEntity",
        name: "str",
        type: "GsaAttributeType" = GsaAttributeType.DISCRETEFUNCTIONAL,
        default_threshold_type: "Union[GsaAttributeThresholdType, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
        help_path: "Union[str, None, Unset_Type]" = Unset,
        is_hidden_from_search_criteria: "Union[bool, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaCreateDiscreteFunctionalAttribute - a model defined in Swagger

        Parameters
        ----------
        attribute_parameters: list[GsaCreateDiscreteFunctionalAttributeParameter]
        discrete_type: GsaSlimEntity
        name: str
        type: GsaAttributeType
        default_threshold_type: GsaAttributeThresholdType, optional
        guid: str, optional
        help_path: str, optional
        is_hidden_from_search_criteria: bool, optional
        """
        super().__init__(
            name=name,
            type=type,
            default_threshold_type=default_threshold_type,
            guid=guid,
            help_path=help_path,
            is_hidden_from_search_criteria=is_hidden_from_search_criteria,
        )
        self._discrete_type: GsaSlimEntity
        self._attribute_parameters: list[GsaCreateDiscreteFunctionalAttributeParameter]

        self.discrete_type = discrete_type
        self.attribute_parameters = attribute_parameters

    @property
    def discrete_type(self) -> "GsaSlimEntity":
        """Gets the discrete_type of this GsaCreateDiscreteFunctionalAttribute.

        Returns
        -------
        GsaSlimEntity
            The discrete_type of this GsaCreateDiscreteFunctionalAttribute.
        """
        return self._discrete_type

    @discrete_type.setter
    def discrete_type(self, discrete_type: "GsaSlimEntity") -> None:
        """Sets the discrete_type of this GsaCreateDiscreteFunctionalAttribute.

        Parameters
        ----------
        discrete_type: GsaSlimEntity
            The discrete_type of this GsaCreateDiscreteFunctionalAttribute.
        """
        # Field is not nullable
        if discrete_type is None:
            raise ValueError("Invalid value for 'discrete_type', must not be 'None'")
        # Field is required
        if discrete_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'discrete_type', must not be 'Unset'")
        self._discrete_type = discrete_type

    @property
    def attribute_parameters(self) -> "list[GsaCreateDiscreteFunctionalAttributeParameter]":
        """Gets the attribute_parameters of this GsaCreateDiscreteFunctionalAttribute.

        Returns
        -------
        list[GsaCreateDiscreteFunctionalAttributeParameter]
            The attribute_parameters of this GsaCreateDiscreteFunctionalAttribute.
        """
        return self._attribute_parameters

    @attribute_parameters.setter
    def attribute_parameters(
        self, attribute_parameters: "list[GsaCreateDiscreteFunctionalAttributeParameter]"
    ) -> None:
        """Sets the attribute_parameters of this GsaCreateDiscreteFunctionalAttribute.

        Parameters
        ----------
        attribute_parameters: list[GsaCreateDiscreteFunctionalAttributeParameter]
            The attribute_parameters of this GsaCreateDiscreteFunctionalAttribute.
        """
        # Field is not nullable
        if attribute_parameters is None:
            raise ValueError("Invalid value for 'attribute_parameters', must not be 'None'")
        # Field is required
        if attribute_parameters is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'attribute_parameters', must not be 'Unset'")
        self._attribute_parameters = attribute_parameters

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
        if not isinstance(other, GsaCreateDiscreteFunctionalAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
