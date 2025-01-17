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

from ansys.grantami.serverapi_openapi.models.granta_server_api_search_datum_criterion import (  # noqa: F401
    GrantaServerApiSearchDatumCriterion,
)

from . import ModelBase

if TYPE_CHECKING:
    from . import *


class GrantaServerApiSearchDiscreteIdentityValuesDatumCriterion(
    GrantaServerApiSearchDatumCriterion
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
    swagger_types = {
        "_none": "list[int]",
        "all": "list[int]",
        "any": "list[int]",
        "type": "str",
    }

    attribute_map = {
        "_none": "none",
        "all": "all",
        "any": "any",
        "type": "type",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        _none: "Optional[List[int]]" = None,
        all: "Optional[List[int]]" = None,
        any: "Optional[List[int]]" = None,
        type: "str" = "discreteIdentityValues",
    ) -> None:
        """GrantaServerApiSearchDiscreteIdentityValuesDatumCriterion - a model defined in Swagger

        Parameters
        ----------
            _none: List[int], optional
            all: List[int], optional
            any: List[int], optional
            type: str
        """
        super().__init__()
        self._all = None
        self._any = None
        self.__none = None
        self._type = None

        if all is not None:
            self.all = all
        if any is not None:
            self.any = any
        if _none is not None:
            self._none = _none
        self.type = type

    @property
    def all(self) -> "list[int]":
        """Gets the all of this GrantaServerApiSearchDiscreteIdentityValuesDatumCriterion.
        Match all of these discrete value identities

        Returns
        -------
        list[int]
            The all of this GrantaServerApiSearchDiscreteIdentityValuesDatumCriterion.
        """
        return self._all

    @all.setter
    def all(self, all: "list[int]") -> None:
        """Sets the all of this GrantaServerApiSearchDiscreteIdentityValuesDatumCriterion.
        Match all of these discrete value identities

        Parameters
        ----------
        all: list[int]
            The all of this GrantaServerApiSearchDiscreteIdentityValuesDatumCriterion.
        """
        self._all = all

    @property
    def any(self) -> "list[int]":
        """Gets the any of this GrantaServerApiSearchDiscreteIdentityValuesDatumCriterion.
        Match any of these discrete type identities

        Returns
        -------
        list[int]
            The any of this GrantaServerApiSearchDiscreteIdentityValuesDatumCriterion.
        """
        return self._any

    @any.setter
    def any(self, any: "list[int]") -> None:
        """Sets the any of this GrantaServerApiSearchDiscreteIdentityValuesDatumCriterion.
        Match any of these discrete type identities

        Parameters
        ----------
        any: list[int]
            The any of this GrantaServerApiSearchDiscreteIdentityValuesDatumCriterion.
        """
        self._any = any

    @property
    def _none(self) -> "list[int]":
        """Gets the _none of this GrantaServerApiSearchDiscreteIdentityValuesDatumCriterion.
        Match none of the discrete type identities

        Returns
        -------
        list[int]
            The _none of this GrantaServerApiSearchDiscreteIdentityValuesDatumCriterion.
        """
        return self.__none

    @_none.setter
    def _none(self, _none: "list[int]") -> None:
        """Sets the _none of this GrantaServerApiSearchDiscreteIdentityValuesDatumCriterion.
        Match none of the discrete type identities

        Parameters
        ----------
        _none: list[int]
            The _none of this GrantaServerApiSearchDiscreteIdentityValuesDatumCriterion.
        """
        self.__none = _none

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchDiscreteIdentityValuesDatumCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchDiscreteIdentityValuesDatumCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchDiscreteIdentityValuesDatumCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchDiscreteIdentityValuesDatumCriterion.
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
        if not isinstance(other, GrantaServerApiSearchDiscreteIdentityValuesDatumCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
