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


class GsaLocalColumnAggregationCriterion(ModelBase):
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
    discriminator_class_map: dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "local_column_aggregation_criterion_type": "GsaLocalColumnAggregationType",
        "guid": "str",
        "identity": "int",
    }

    attribute_map: dict[str, str] = {
        "local_column_aggregation_criterion_type": "localColumnAggregationCriterionType",
        "guid": "guid",
        "identity": "identity",
    }

    subtype_mapping: dict[str, str] = {
        "localColumnAggregationCriterionType": "GsaLocalColumnAggregationType",
    }

    discriminator_value_class_map = {
        "value".lower(): "#/components/schemas/GsaLocalColumnAggregationValueCriterion",
        "exists".lower(): "#/components/schemas/GsaLocalColumnAggregationExistsCriterion",
    }

    discriminator: Optional[str] = "localColumnAggregationCriterionType"

    def __init__(
        self,
        *,
        local_column_aggregation_criterion_type: "GsaLocalColumnAggregationType",
        guid: "Union[str, None, Unset_Type]" = Unset,
        identity: "Union[int, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaLocalColumnAggregationCriterion - a model defined in Swagger

        Parameters
        ----------
        local_column_aggregation_criterion_type: GsaLocalColumnAggregationType
        guid: str, optional
        identity: int, optional
        """
        self._identity: Union[int, None, Unset_Type] = Unset
        self._guid: Union[str, None, Unset_Type] = Unset
        self._local_column_aggregation_criterion_type: GsaLocalColumnAggregationType

        if identity is not Unset:
            self.identity = identity
        if guid is not Unset:
            self.guid = guid
        self.local_column_aggregation_criterion_type = local_column_aggregation_criterion_type

    @property
    def identity(self) -> "Union[int, None, Unset_Type]":
        """Gets the identity of this GsaLocalColumnAggregationCriterion.

        Returns
        -------
        Union[int, None, Unset_Type]
            The identity of this GsaLocalColumnAggregationCriterion.
        """
        return self._identity

    @identity.setter
    def identity(self, identity: "Union[int, None, Unset_Type]") -> None:
        """Sets the identity of this GsaLocalColumnAggregationCriterion.

        Parameters
        ----------
        identity: Union[int, None, Unset_Type]
            The identity of this GsaLocalColumnAggregationCriterion.
        """
        self._identity = identity

    @property
    def guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the guid of this GsaLocalColumnAggregationCriterion.

        Returns
        -------
        Union[str, None, Unset_Type]
            The guid of this GsaLocalColumnAggregationCriterion.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the guid of this GsaLocalColumnAggregationCriterion.

        Parameters
        ----------
        guid: Union[str, None, Unset_Type]
            The guid of this GsaLocalColumnAggregationCriterion.
        """
        self._guid = guid

    @property
    def local_column_aggregation_criterion_type(self) -> "GsaLocalColumnAggregationType":
        """Gets the local_column_aggregation_criterion_type of this GsaLocalColumnAggregationCriterion.

        Returns
        -------
        GsaLocalColumnAggregationType
            The local_column_aggregation_criterion_type of this GsaLocalColumnAggregationCriterion.
        """
        return self._local_column_aggregation_criterion_type

    @local_column_aggregation_criterion_type.setter
    def local_column_aggregation_criterion_type(
        self, local_column_aggregation_criterion_type: "GsaLocalColumnAggregationType"
    ) -> None:
        """Sets the local_column_aggregation_criterion_type of this GsaLocalColumnAggregationCriterion.

        Parameters
        ----------
        local_column_aggregation_criterion_type: GsaLocalColumnAggregationType
            The local_column_aggregation_criterion_type of this GsaLocalColumnAggregationCriterion.
        """
        # Field is not nullable
        if local_column_aggregation_criterion_type is None:
            raise ValueError(
                "Invalid value for 'local_column_aggregation_criterion_type', must not be 'None'"
            )
        # Field is required
        if local_column_aggregation_criterion_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'local_column_aggregation_criterion_type', must not be 'Unset'"
            )
        self._local_column_aggregation_criterion_type = local_column_aggregation_criterion_type

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[cls._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen,
        # so we have to extract it from the JSON reference
        return cls.discriminator_value_class_map[discriminator_value].rsplit("/", 1)[-1]

    @classmethod
    def _get_discriminator_field_name(cls) -> str:
        assert cls.discriminator
        name_tokens = cls.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GsaLocalColumnAggregationCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
