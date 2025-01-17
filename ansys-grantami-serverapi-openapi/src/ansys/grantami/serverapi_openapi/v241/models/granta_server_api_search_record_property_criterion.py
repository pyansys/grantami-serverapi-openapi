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

from ansys.grantami.serverapi_openapi.models.granta_server_api_search_criterion import (  # noqa: F401
    GrantaServerApiSearchCriterion,
)

from . import ModelBase

if TYPE_CHECKING:
    from . import *


class GrantaServerApiSearchRecordPropertyCriterion(GrantaServerApiSearchCriterion):
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
        "_property": "GrantaServerApiSearchSearchableRecordProperty",
        "inner_criterion": "GrantaServerApiSearchDatumCriterion",
        "type": "str",
    }

    attribute_map = {
        "_property": "property",
        "inner_criterion": "innerCriterion",
        "type": "type",
    }

    subtype_mapping = {
        "property": "GrantaServerApiSearchSearchableRecordProperty",
        "innerCriterion": "GrantaServerApiSearchDatumCriterion",
    }

    discriminator = None

    def __init__(
        self,
        *,
        _property: "Optional[GrantaServerApiSearchSearchableRecordProperty]" = None,
        inner_criterion: "Optional[GrantaServerApiSearchDatumCriterion]" = None,
        type: "str" = "recordProperty",
    ) -> None:
        """GrantaServerApiSearchRecordPropertyCriterion - a model defined in Swagger

        Parameters
        ----------
            _property: GrantaServerApiSearchSearchableRecordProperty, optional
            inner_criterion: GrantaServerApiSearchDatumCriterion, optional
            type: str
        """
        super().__init__()
        self.__property = None
        self._inner_criterion = None
        self._type = None

        if _property is not None:
            self._property = _property
        if inner_criterion is not None:
            self.inner_criterion = inner_criterion
        self.type = type

    @property
    def _property(self) -> "GrantaServerApiSearchSearchableRecordProperty":
        """Gets the _property of this GrantaServerApiSearchRecordPropertyCriterion.

        Returns
        -------
        GrantaServerApiSearchSearchableRecordProperty
            The _property of this GrantaServerApiSearchRecordPropertyCriterion.
        """
        return self.__property

    @_property.setter
    def _property(self, _property: "GrantaServerApiSearchSearchableRecordProperty") -> None:
        """Sets the _property of this GrantaServerApiSearchRecordPropertyCriterion.

        Parameters
        ----------
        _property: GrantaServerApiSearchSearchableRecordProperty
            The _property of this GrantaServerApiSearchRecordPropertyCriterion.
        """
        self.__property = _property

    @property
    def inner_criterion(self) -> "GrantaServerApiSearchDatumCriterion":
        """Gets the inner_criterion of this GrantaServerApiSearchRecordPropertyCriterion.

        Returns
        -------
        GrantaServerApiSearchDatumCriterion
            The inner_criterion of this GrantaServerApiSearchRecordPropertyCriterion.
        """
        return self._inner_criterion

    @inner_criterion.setter
    def inner_criterion(self, inner_criterion: "GrantaServerApiSearchDatumCriterion") -> None:
        """Sets the inner_criterion of this GrantaServerApiSearchRecordPropertyCriterion.

        Parameters
        ----------
        inner_criterion: GrantaServerApiSearchDatumCriterion
            The inner_criterion of this GrantaServerApiSearchRecordPropertyCriterion.
        """
        self._inner_criterion = inner_criterion

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchRecordPropertyCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchRecordPropertyCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchRecordPropertyCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchRecordPropertyCriterion.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

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
        if not isinstance(other, GrantaServerApiSearchRecordPropertyCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
