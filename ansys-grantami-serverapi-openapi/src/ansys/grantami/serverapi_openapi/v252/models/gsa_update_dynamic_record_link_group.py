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

from ansys.grantami.serverapi_openapi.v252.models.gsa_record_link_group_type import (
    GsaRecordLinkGroupType,
)
from ansys.grantami.serverapi_openapi.v252.models.gsa_update_record_link_group import (  # noqa: F401
    GsaUpdateRecordLinkGroup,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaUpdateDynamicRecordLinkGroup(GsaUpdateRecordLinkGroup):
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
        "type": "GsaRecordLinkGroupType",
        "attribute_pairs": "list[GsaCreateAttributeLinkPair]",
        "forbid_orphans": "bool",
        "guid": "str",
        "name": "str",
        "referential_integrity_model": "GsaReferentialIntegrityModel",
        "reverse_name": "str",
    }

    attribute_map: dict[str, str] = {
        "type": "type",
        "attribute_pairs": "attributePairs",
        "forbid_orphans": "forbidOrphans",
        "guid": "guid",
        "name": "name",
        "referential_integrity_model": "referentialIntegrityModel",
        "reverse_name": "reverseName",
    }

    subtype_mapping: dict[str, str] = {
        "referentialIntegrityModel": "GsaReferentialIntegrityModel",
        "attributePairs": "GsaCreateAttributeLinkPair",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        type: "GsaRecordLinkGroupType" = GsaRecordLinkGroupType.DYNAMIC,
        attribute_pairs: "Union[list[GsaCreateAttributeLinkPair], Unset_Type]" = Unset,
        forbid_orphans: "Union[bool, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
        name: "Union[str, Unset_Type]" = Unset,
        referential_integrity_model: "Union[GsaReferentialIntegrityModel, Unset_Type]" = Unset,
        reverse_name: "Union[str, Unset_Type]" = Unset,
    ) -> None:
        """GsaUpdateDynamicRecordLinkGroup - a model defined in Swagger

        Parameters
        ----------
        type: GsaRecordLinkGroupType
        attribute_pairs: list[GsaCreateAttributeLinkPair], optional
        forbid_orphans: bool, optional
        guid: str, optional
        name: str, optional
        referential_integrity_model: GsaReferentialIntegrityModel, optional
        reverse_name: str, optional
        """
        super().__init__(type=type, guid=guid, name=name, reverse_name=reverse_name)
        self._forbid_orphans: Union[bool, Unset_Type] = Unset
        self._referential_integrity_model: Union[GsaReferentialIntegrityModel, Unset_Type] = Unset
        self._attribute_pairs: Union[list[GsaCreateAttributeLinkPair], Unset_Type] = Unset

        if forbid_orphans is not Unset:
            self.forbid_orphans = forbid_orphans
        if referential_integrity_model is not Unset:
            self.referential_integrity_model = referential_integrity_model
        if attribute_pairs is not Unset:
            self.attribute_pairs = attribute_pairs

    @property
    def forbid_orphans(self) -> "Union[bool, Unset_Type]":
        """Gets the forbid_orphans of this GsaUpdateDynamicRecordLinkGroup.

        Returns
        -------
        Union[bool, Unset_Type]
            The forbid_orphans of this GsaUpdateDynamicRecordLinkGroup.
        """
        return self._forbid_orphans

    @forbid_orphans.setter
    def forbid_orphans(self, forbid_orphans: "Union[bool, Unset_Type]") -> None:
        """Sets the forbid_orphans of this GsaUpdateDynamicRecordLinkGroup.

        Parameters
        ----------
        forbid_orphans: Union[bool, Unset_Type]
            The forbid_orphans of this GsaUpdateDynamicRecordLinkGroup.
        """
        # Field is not nullable
        if forbid_orphans is None:
            raise ValueError("Invalid value for 'forbid_orphans', must not be 'None'")
        self._forbid_orphans = forbid_orphans

    @property
    def referential_integrity_model(self) -> "Union[GsaReferentialIntegrityModel, Unset_Type]":
        """Gets the referential_integrity_model of this GsaUpdateDynamicRecordLinkGroup.

        Returns
        -------
        Union[GsaReferentialIntegrityModel, Unset_Type]
            The referential_integrity_model of this GsaUpdateDynamicRecordLinkGroup.
        """
        return self._referential_integrity_model

    @referential_integrity_model.setter
    def referential_integrity_model(
        self, referential_integrity_model: "Union[GsaReferentialIntegrityModel, Unset_Type]"
    ) -> None:
        """Sets the referential_integrity_model of this GsaUpdateDynamicRecordLinkGroup.

        Parameters
        ----------
        referential_integrity_model: Union[GsaReferentialIntegrityModel, Unset_Type]
            The referential_integrity_model of this GsaUpdateDynamicRecordLinkGroup.
        """
        # Field is not nullable
        if referential_integrity_model is None:
            raise ValueError("Invalid value for 'referential_integrity_model', must not be 'None'")
        self._referential_integrity_model = referential_integrity_model

    @property
    def attribute_pairs(self) -> "Union[list[GsaCreateAttributeLinkPair], Unset_Type]":
        """Gets the attribute_pairs of this GsaUpdateDynamicRecordLinkGroup.

        Returns
        -------
        Union[list[GsaCreateAttributeLinkPair], Unset_Type]
            The attribute_pairs of this GsaUpdateDynamicRecordLinkGroup.
        """
        return self._attribute_pairs

    @attribute_pairs.setter
    def attribute_pairs(
        self, attribute_pairs: "Union[list[GsaCreateAttributeLinkPair], Unset_Type]"
    ) -> None:
        """Sets the attribute_pairs of this GsaUpdateDynamicRecordLinkGroup.

        Parameters
        ----------
        attribute_pairs: Union[list[GsaCreateAttributeLinkPair], Unset_Type]
            The attribute_pairs of this GsaUpdateDynamicRecordLinkGroup.
        """
        # Field is not nullable
        if attribute_pairs is None:
            raise ValueError("Invalid value for 'attribute_pairs', must not be 'None'")
        self._attribute_pairs = attribute_pairs

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
        if not isinstance(other, GsaUpdateDynamicRecordLinkGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
