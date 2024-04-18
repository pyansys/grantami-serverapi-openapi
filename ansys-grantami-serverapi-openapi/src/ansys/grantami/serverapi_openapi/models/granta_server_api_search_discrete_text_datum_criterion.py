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
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, Union  # noqa: F401

from ansys.grantami.serverapi_openapi.models.granta_server_api_search_datum_criterion import (  # noqa: F401
    GrantaServerApiSearchDatumCriterion,
)

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GrantaServerApiSearchDiscreteTextDatumCriterion(GrantaServerApiSearchDatumCriterion):
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
        "text_match_behavior": "GrantaServerApiSearchTextMatchBehavior",
        "type": "str",
        "value": "str",
    }

    attribute_map: Dict[str, str] = {
        "text_match_behavior": "textMatchBehavior",
        "type": "type",
        "value": "value",
    }

    subtype_mapping: Dict[str, str] = {
        "textMatchBehavior": "GrantaServerApiSearchTextMatchBehavior",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        text_match_behavior: "Union[GrantaServerApiSearchTextMatchBehavior, Unset_Type]" = Unset,
        type: "str" = "discreteText",
        value: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSearchDiscreteTextDatumCriterion - a model defined in Swagger

        Parameters
        ----------
        text_match_behavior: GrantaServerApiSearchTextMatchBehavior, optional
        type: str
        value: str, optional
        """
        super().__init__()
        self._value: Union[str, None, Unset_Type] = Unset
        self._text_match_behavior: Union[GrantaServerApiSearchTextMatchBehavior, Unset_Type] = Unset
        self._type: str

        if value is not Unset:
            self.value = value
        if text_match_behavior is not Unset:
            self.text_match_behavior = text_match_behavior
        self.type = type

    @property
    def value(self) -> "Union[str, None, Unset_Type]":
        """Gets the value of this GrantaServerApiSearchDiscreteTextDatumCriterion.

        Returns
        -------
        Union[str, None, Unset_Type]
            The value of this GrantaServerApiSearchDiscreteTextDatumCriterion.
        """
        return self._value

    @value.setter
    def value(self, value: "Union[str, None, Unset_Type]") -> None:
        """Sets the value of this GrantaServerApiSearchDiscreteTextDatumCriterion.

        Parameters
        ----------
        value: Union[str, None, Unset_Type]
            The value of this GrantaServerApiSearchDiscreteTextDatumCriterion.
        """
        self._value = value

    @property
    def text_match_behavior(self) -> "Union[GrantaServerApiSearchTextMatchBehavior, Unset_Type]":
        """Gets the text_match_behavior of this GrantaServerApiSearchDiscreteTextDatumCriterion.

        Returns
        -------
        Union[GrantaServerApiSearchTextMatchBehavior, Unset_Type]
            The text_match_behavior of this GrantaServerApiSearchDiscreteTextDatumCriterion.
        """
        return self._text_match_behavior

    @text_match_behavior.setter
    def text_match_behavior(
        self, text_match_behavior: "Union[GrantaServerApiSearchTextMatchBehavior, Unset_Type]"
    ) -> None:
        """Sets the text_match_behavior of this GrantaServerApiSearchDiscreteTextDatumCriterion.

        Parameters
        ----------
        text_match_behavior: Union[GrantaServerApiSearchTextMatchBehavior, Unset_Type]
            The text_match_behavior of this GrantaServerApiSearchDiscreteTextDatumCriterion.
        """
        # Field is not nullable
        if text_match_behavior is None:
            raise ValueError("Invalid value for 'text_match_behavior', must not be 'None'")
        self._text_match_behavior = text_match_behavior

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchDiscreteTextDatumCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchDiscreteTextDatumCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchDiscreteTextDatumCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchDiscreteTextDatumCriterion.
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
        if not isinstance(other, GrantaServerApiSearchDiscreteTextDatumCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
