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
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from ansys.grantami.serverapi_openapi.models.gsa_aggregation import GsaAggregation  # noqa: F401
from ansys.grantami.serverapi_openapi.models.gsa_aggregation_type import GsaAggregationType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaAttributeAggregation(GsaAggregation):
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
        "attribute_aggregation_type": "GsaAttributeAggregationType",
        "type": "GsaAggregationType",
        "attribute_guid": "str",
        "attribute_identity": "int",
        "count": "int",
    }

    attribute_map: dict[str, str] = {
        "attribute_aggregation_type": "attributeAggregationType",
        "type": "type",
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "count": "count",
    }

    subtype_mapping: dict[str, str] = {
        "attributeAggregationType": "GsaAttributeAggregationType",
    }

    discriminator_value_class_map = {
        "value".lower(): "#/components/schemas/GsaAttributeValueAggregation",
        "exists".lower(): "#/components/schemas/GsaAttributeExistsAggregation",
    }

    discriminator: Optional[str] = "attribute_aggregation_type"

    def __init__(
        self,
        *,
        attribute_aggregation_type: "GsaAttributeAggregationType",
        type: "GsaAggregationType" = GsaAggregationType.ATTRIBUTE,
        attribute_guid: "Union[str, None, Unset_Type]" = Unset,
        attribute_identity: "Union[int, None, Unset_Type]" = Unset,
        count: "Union[int, Unset_Type]" = Unset,
    ) -> None:
        """GsaAttributeAggregation - a model defined in Swagger

        Parameters
        ----------
        attribute_aggregation_type: GsaAttributeAggregationType
        type: GsaAggregationType
        attribute_guid: str, optional
        attribute_identity: int, optional
        count: int, optional
        """
        super().__init__(type=type)
        self._attribute_identity: Union[int, None, Unset_Type] = Unset
        self._attribute_guid: Union[str, None, Unset_Type] = Unset
        self._attribute_aggregation_type: GsaAttributeAggregationType
        self._count: Union[int, Unset_Type] = Unset

        if attribute_identity is not Unset:
            self.attribute_identity = attribute_identity
        if attribute_guid is not Unset:
            self.attribute_guid = attribute_guid
        self.attribute_aggregation_type = attribute_aggregation_type
        if count is not Unset:
            self.count = count

    @property
    def attribute_identity(self) -> "Union[int, None, Unset_Type]":
        """Gets the attribute_identity of this GsaAttributeAggregation.
        The identity of the attribute that was aggregated over.

        Returns
        -------
        Union[int, None, Unset_Type]
            The attribute_identity of this GsaAttributeAggregation.
        """
        return self._attribute_identity

    @attribute_identity.setter
    def attribute_identity(self, attribute_identity: "Union[int, None, Unset_Type]") -> None:
        """Sets the attribute_identity of this GsaAttributeAggregation.
        The identity of the attribute that was aggregated over.

        Parameters
        ----------
        attribute_identity: Union[int, None, Unset_Type]
            The attribute_identity of this GsaAttributeAggregation.
        """
        self._attribute_identity = attribute_identity

    @property
    def attribute_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the attribute_guid of this GsaAttributeAggregation.
        The GUID of the attribute that was aggregated over.

        Returns
        -------
        Union[str, None, Unset_Type]
            The attribute_guid of this GsaAttributeAggregation.
        """
        return self._attribute_guid

    @attribute_guid.setter
    def attribute_guid(self, attribute_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the attribute_guid of this GsaAttributeAggregation.
        The GUID of the attribute that was aggregated over.

        Parameters
        ----------
        attribute_guid: Union[str, None, Unset_Type]
            The attribute_guid of this GsaAttributeAggregation.
        """
        self._attribute_guid = attribute_guid

    @property
    def attribute_aggregation_type(self) -> "GsaAttributeAggregationType":
        """Gets the attribute_aggregation_type of this GsaAttributeAggregation.

        Returns
        -------
        GsaAttributeAggregationType
            The attribute_aggregation_type of this GsaAttributeAggregation.
        """
        return self._attribute_aggregation_type

    @attribute_aggregation_type.setter
    def attribute_aggregation_type(
        self, attribute_aggregation_type: "GsaAttributeAggregationType"
    ) -> None:
        """Sets the attribute_aggregation_type of this GsaAttributeAggregation.

        Parameters
        ----------
        attribute_aggregation_type: GsaAttributeAggregationType
            The attribute_aggregation_type of this GsaAttributeAggregation.
        """
        # Field is not nullable
        if attribute_aggregation_type is None:
            raise ValueError("Invalid value for 'attribute_aggregation_type', must not be 'None'")
        # Field is required
        if attribute_aggregation_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'attribute_aggregation_type', must not be 'Unset'")
        self._attribute_aggregation_type = attribute_aggregation_type

    @property
    def count(self) -> "Union[int, Unset_Type]":
        """Gets the count of this GsaAttributeAggregation.
        The number of records that have a populated (applicable) value for this attribute.  (For multi-valued attributes: the number of records that have one or more populated  (applicable) values for this attribute.)                For a tabular attribute, this will be the number of records that have at least one  tabular row in this attribute, even if those rows might be filtered out from users'  views in some clients.

        Returns
        -------
        Union[int, Unset_Type]
            The count of this GsaAttributeAggregation.
        """
        return self._count

    @count.setter
    def count(self, count: "Union[int, Unset_Type]") -> None:
        """Sets the count of this GsaAttributeAggregation.
        The number of records that have a populated (applicable) value for this attribute.  (For multi-valued attributes: the number of records that have one or more populated  (applicable) values for this attribute.)                For a tabular attribute, this will be the number of records that have at least one  tabular row in this attribute, even if those rows might be filtered out from users'  views in some clients.

        Parameters
        ----------
        count: Union[int, Unset_Type]
            The count of this GsaAttributeAggregation.
        """
        # Field is not nullable
        if count is None:
            raise ValueError("Invalid value for 'count', must not be 'None'")
        self._count = count

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
        if not isinstance(other, GsaAttributeAggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
