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


class GrantaServerApiSelectionSearchesCreateSearchRequest(ModelBase):
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
        "detail": "GrantaServerApiSelectionSearchesSearchDetail",
        "search_config": "str",
    }

    attribute_map = {
        "detail": "detail",
        "search_config": "searchConfig",
    }

    subtype_mapping = {
        "detail": "GrantaServerApiSelectionSearchesSearchDetail",
    }

    discriminator = None

    def __init__(
        self,
        *,
        detail: "Optional[GrantaServerApiSelectionSearchesSearchDetail]" = None,
        search_config: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiSelectionSearchesCreateSearchRequest - a model defined in Swagger

        Parameters
        ----------
            detail: GrantaServerApiSelectionSearchesSearchDetail, optional
            search_config: str, optional
        """
        self._search_config = None
        self._detail = None

        if search_config is not None:
            self.search_config = search_config
        if detail is not None:
            self.detail = detail

    @property
    def search_config(self) -> "str":
        """Gets the search_config of this GrantaServerApiSelectionSearchesCreateSearchRequest.

        Returns
        -------
        str
            The search_config of this GrantaServerApiSelectionSearchesCreateSearchRequest.
        """
        return self._search_config

    @search_config.setter
    def search_config(self, search_config: "str") -> None:
        """Sets the search_config of this GrantaServerApiSelectionSearchesCreateSearchRequest.

        Parameters
        ----------
        search_config: str
            The search_config of this GrantaServerApiSelectionSearchesCreateSearchRequest.
        """
        self._search_config = search_config

    @property
    def detail(self) -> "GrantaServerApiSelectionSearchesSearchDetail":
        """Gets the detail of this GrantaServerApiSelectionSearchesCreateSearchRequest.

        Returns
        -------
        GrantaServerApiSelectionSearchesSearchDetail
            The detail of this GrantaServerApiSelectionSearchesCreateSearchRequest.
        """
        return self._detail

    @detail.setter
    def detail(self, detail: "GrantaServerApiSelectionSearchesSearchDetail") -> None:
        """Sets the detail of this GrantaServerApiSelectionSearchesCreateSearchRequest.

        Parameters
        ----------
        detail: GrantaServerApiSelectionSearchesSearchDetail
            The detail of this GrantaServerApiSelectionSearchesCreateSearchRequest.
        """
        self._detail = detail

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
        if not isinstance(other, GrantaServerApiSelectionSearchesCreateSearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
