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

from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_parameters_parameter import (  # noqa: F401
    GrantaServerApiSchemaParametersParameter,
)

from . import ModelBase

if TYPE_CHECKING:
    from . import *


class GrantaServerApiSchemaParametersDiscreteParameter(GrantaServerApiSchemaParametersParameter):
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
        "default_parameter_value_guid": "str",
        "display_names": "dict(str, str)",
        "guid": "str",
        "name": "str",
        "values": "list[GrantaServerApiSchemaParametersDiscreteParameterValue]",
        "help_path": "str",
        "type": "str",
    }

    attribute_map = {
        "default_parameter_value_guid": "defaultParameterValueGuid",
        "display_names": "displayNames",
        "guid": "guid",
        "name": "name",
        "values": "values",
        "help_path": "helpPath",
        "type": "type",
    }

    subtype_mapping = {
        "values": "GrantaServerApiSchemaParametersDiscreteParameterValue",
    }

    discriminator = None

    def __init__(
        self,
        *,
        default_parameter_value_guid: "str",
        display_names: "Dict[str, str]",
        guid: "str",
        name: "str",
        values: "List[GrantaServerApiSchemaParametersDiscreteParameterValue]",
        help_path: "Optional[str]" = None,
        type: "str" = "discrete",
    ) -> None:
        """GrantaServerApiSchemaParametersDiscreteParameter - a model defined in Swagger

        Parameters
        ----------
            default_parameter_value_guid: str
            display_names: Dict[str, str]
            guid: str
            name: str
            values: List[GrantaServerApiSchemaParametersDiscreteParameterValue]
            help_path: str, optional
            type: str
        """
        super().__init__(
            default_parameter_value_guid=default_parameter_value_guid,
            display_names=display_names,
            guid=guid,
            name=name,
            help_path=help_path,
        )
        self._type = None
        self._values = None

        self.type = type
        self.values = values

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaParametersDiscreteParameter.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaParametersDiscreteParameter.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaParametersDiscreteParameter.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaParametersDiscreteParameter.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @property
    def values(self) -> "list[GrantaServerApiSchemaParametersDiscreteParameterValue]":
        """Gets the values of this GrantaServerApiSchemaParametersDiscreteParameter.

        Returns
        -------
        list[GrantaServerApiSchemaParametersDiscreteParameterValue]
            The values of this GrantaServerApiSchemaParametersDiscreteParameter.
        """
        return self._values

    @values.setter
    def values(self, values: "list[GrantaServerApiSchemaParametersDiscreteParameterValue]") -> None:
        """Sets the values of this GrantaServerApiSchemaParametersDiscreteParameter.

        Parameters
        ----------
        values: list[GrantaServerApiSchemaParametersDiscreteParameterValue]
            The values of this GrantaServerApiSchemaParametersDiscreteParameter.
        """
        if values is None:
            raise ValueError("Invalid value for 'values', must not be 'None'")
        self._values = values

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
        if not isinstance(other, GrantaServerApiSchemaParametersDiscreteParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
