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


class GrantaServerApiSchemaProfilesAllProfilesInfo(ModelBase):
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
        "default_profile": "GrantaServerApiSchemaSlimEntitiesSlimProfile",
        "profiles": "list[GrantaServerApiSchemaSlimEntitiesSlimProfile]",
    }

    attribute_map = {
        "default_profile": "defaultProfile",
        "profiles": "profiles",
    }

    subtype_mapping = {
        "profiles": "GrantaServerApiSchemaSlimEntitiesSlimProfile",
        "defaultProfile": "GrantaServerApiSchemaSlimEntitiesSlimProfile",
    }

    discriminator = None

    def __init__(
        self,
        *,
        default_profile: "Optional[GrantaServerApiSchemaSlimEntitiesSlimProfile]" = None,
        profiles: "Optional[List[GrantaServerApiSchemaSlimEntitiesSlimProfile]]" = None,
    ) -> None:
        """GrantaServerApiSchemaProfilesAllProfilesInfo - a model defined in Swagger

        Parameters
        ----------
            default_profile: GrantaServerApiSchemaSlimEntitiesSlimProfile, optional
            profiles: List[GrantaServerApiSchemaSlimEntitiesSlimProfile], optional
        """
        self._profiles = None
        self._default_profile = None

        if profiles is not None:
            self.profiles = profiles
        if default_profile is not None:
            self.default_profile = default_profile

    @property
    def profiles(self) -> "list[GrantaServerApiSchemaSlimEntitiesSlimProfile]":
        """Gets the profiles of this GrantaServerApiSchemaProfilesAllProfilesInfo.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimProfile]
            The profiles of this GrantaServerApiSchemaProfilesAllProfilesInfo.
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles: "list[GrantaServerApiSchemaSlimEntitiesSlimProfile]") -> None:
        """Sets the profiles of this GrantaServerApiSchemaProfilesAllProfilesInfo.

        Parameters
        ----------
        profiles: list[GrantaServerApiSchemaSlimEntitiesSlimProfile]
            The profiles of this GrantaServerApiSchemaProfilesAllProfilesInfo.
        """
        self._profiles = profiles

    @property
    def default_profile(self) -> "GrantaServerApiSchemaSlimEntitiesSlimProfile":
        """Gets the default_profile of this GrantaServerApiSchemaProfilesAllProfilesInfo.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimProfile
            The default_profile of this GrantaServerApiSchemaProfilesAllProfilesInfo.
        """
        return self._default_profile

    @default_profile.setter
    def default_profile(
        self, default_profile: "GrantaServerApiSchemaSlimEntitiesSlimProfile"
    ) -> None:
        """Sets the default_profile of this GrantaServerApiSchemaProfilesAllProfilesInfo.

        Parameters
        ----------
        default_profile: GrantaServerApiSchemaSlimEntitiesSlimProfile
            The default_profile of this GrantaServerApiSchemaProfilesAllProfilesInfo.
        """
        self._default_profile = default_profile

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
        if not isinstance(other, GrantaServerApiSchemaProfilesAllProfilesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
