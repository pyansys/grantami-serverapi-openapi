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

from ansys.grantami.serverapi_openapi.models.gsa_datum_criterion import (  # noqa: F401
    GsaDatumCriterion,
)
from ansys.grantami.serverapi_openapi.models.gsa_datum_criterion_type import GsaDatumCriterionType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaLinkingValueExistsDatumCriterion(GsaDatumCriterion):
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
        "type": "GsaDatumCriterionType",
        "attribute_type": "GsaAttributeType",
        "inner_hits_identifier": "str",
    }

    attribute_map: dict[str, str] = {
        "type": "type",
        "attribute_type": "attributeType",
        "inner_hits_identifier": "innerHitsIdentifier",
    }

    subtype_mapping: dict[str, str] = {
        "attributeType": "GsaAttributeType",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        type: "GsaDatumCriterionType" = GsaDatumCriterionType.DYNAMICLINKINGVALUE,
        attribute_type: "Union[GsaAttributeType, Unset_Type]" = Unset,
        inner_hits_identifier: "Union[str, Unset_Type]" = Unset,
    ) -> None:
        """GsaLinkingValueExistsDatumCriterion - a model defined in Swagger

        Parameters
        ----------
        type: GsaDatumCriterionType
        attribute_type: GsaAttributeType, optional
        inner_hits_identifier: str, optional
        """
        super().__init__(type=type)
        self._attribute_type: Union[GsaAttributeType, Unset_Type] = Unset
        self._inner_hits_identifier: Union[str, Unset_Type] = Unset

        if attribute_type is not Unset:
            self.attribute_type = attribute_type
        if inner_hits_identifier is not Unset:
            self.inner_hits_identifier = inner_hits_identifier

    @property
    def attribute_type(self) -> "Union[GsaAttributeType, Unset_Type]":
        """Gets the attribute_type of this GsaLinkingValueExistsDatumCriterion.

        Returns
        -------
        Union[GsaAttributeType, Unset_Type]
            The attribute_type of this GsaLinkingValueExistsDatumCriterion.
        """
        return self._attribute_type

    @attribute_type.setter
    def attribute_type(self, attribute_type: "Union[GsaAttributeType, Unset_Type]") -> None:
        """Sets the attribute_type of this GsaLinkingValueExistsDatumCriterion.

        Parameters
        ----------
        attribute_type: Union[GsaAttributeType, Unset_Type]
            The attribute_type of this GsaLinkingValueExistsDatumCriterion.
        """
        # Field is not nullable
        if attribute_type is None:
            raise ValueError("Invalid value for 'attribute_type', must not be 'None'")
        self._attribute_type = attribute_type

    @property
    def inner_hits_identifier(self) -> "Union[str, Unset_Type]":
        """Gets the inner_hits_identifier of this GsaLinkingValueExistsDatumCriterion.

        Returns
        -------
        Union[str, Unset_Type]
            The inner_hits_identifier of this GsaLinkingValueExistsDatumCriterion.
        """
        return self._inner_hits_identifier

    @inner_hits_identifier.setter
    def inner_hits_identifier(self, inner_hits_identifier: "Union[str, Unset_Type]") -> None:
        """Sets the inner_hits_identifier of this GsaLinkingValueExistsDatumCriterion.

        Parameters
        ----------
        inner_hits_identifier: Union[str, Unset_Type]
            The inner_hits_identifier of this GsaLinkingValueExistsDatumCriterion.
        """
        # Field is not nullable
        if inner_hits_identifier is None:
            raise ValueError("Invalid value for 'inner_hits_identifier', must not be 'None'")
        self._inner_hits_identifier = inner_hits_identifier

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
        if not isinstance(other, GsaLinkingValueExistsDatumCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
