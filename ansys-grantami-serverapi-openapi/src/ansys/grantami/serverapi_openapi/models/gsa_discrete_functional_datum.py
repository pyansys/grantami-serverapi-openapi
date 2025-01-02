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

from ansys.grantami.serverapi_openapi.models.gsa_applicable_datum import (  # noqa: F401
    GsaApplicableDatum,
)
from ansys.grantami.serverapi_openapi.models.gsa_datum_type import GsaDatumType

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaDiscreteFunctionalDatum(GsaApplicableDatum):
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
        "datum_type": "GsaDatumType",
        "graph_type": "GsaGraphType",
        "not_applicable": "str",
        "parameter_settings": "list[GsaFunctionalParameterSetting]",
    }

    attribute_map: dict[str, str] = {
        "datum_type": "datumType",
        "graph_type": "graphType",
        "not_applicable": "notApplicable",
        "parameter_settings": "parameterSettings",
    }

    subtype_mapping: dict[str, str] = {
        "graphType": "GsaGraphType",
        "parameterSettings": "GsaFunctionalParameterSetting",
    }

    discriminator_value_class_map = {
        "series".lower(): "#/components/schemas/GsaDiscreteFunctionalSeriesDatum",
        "grid".lower(): "#/components/schemas/GsaDiscreteFunctionalGridDatum",
    }

    discriminator: Optional[str] = "graph_type"

    def __init__(
        self,
        *,
        datum_type: "GsaDatumType" = GsaDatumType.DISCRETEFUNCTIONAL,
        graph_type: "GsaGraphType",
        not_applicable: "str" = "applicable",
        parameter_settings: "list[GsaFunctionalParameterSetting]",
    ) -> None:
        """GsaDiscreteFunctionalDatum - a model defined in Swagger

        Parameters
        ----------
        datum_type: GsaDatumType
        graph_type: GsaGraphType
        not_applicable: str
        parameter_settings: list[GsaFunctionalParameterSetting]
        """
        super().__init__(datum_type=datum_type, not_applicable=not_applicable)
        self._graph_type: GsaGraphType
        self._parameter_settings: list[GsaFunctionalParameterSetting]

        self.graph_type = graph_type
        self.parameter_settings = parameter_settings

    @property
    def graph_type(self) -> "GsaGraphType":
        """Gets the graph_type of this GsaDiscreteFunctionalDatum.

        Returns
        -------
        GsaGraphType
            The graph_type of this GsaDiscreteFunctionalDatum.
        """
        return self._graph_type

    @graph_type.setter
    def graph_type(self, graph_type: "GsaGraphType") -> None:
        """Sets the graph_type of this GsaDiscreteFunctionalDatum.

        Parameters
        ----------
        graph_type: GsaGraphType
            The graph_type of this GsaDiscreteFunctionalDatum.
        """
        # Field is not nullable
        if graph_type is None:
            raise ValueError("Invalid value for 'graph_type', must not be 'None'")
        # Field is required
        if graph_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'graph_type', must not be 'Unset'")
        self._graph_type = graph_type

    @property
    def parameter_settings(self) -> "list[GsaFunctionalParameterSetting]":
        """Gets the parameter_settings of this GsaDiscreteFunctionalDatum.

        Returns
        -------
        list[GsaFunctionalParameterSetting]
            The parameter_settings of this GsaDiscreteFunctionalDatum.
        """
        return self._parameter_settings

    @parameter_settings.setter
    def parameter_settings(self, parameter_settings: "list[GsaFunctionalParameterSetting]") -> None:
        """Sets the parameter_settings of this GsaDiscreteFunctionalDatum.

        Parameters
        ----------
        parameter_settings: list[GsaFunctionalParameterSetting]
            The parameter_settings of this GsaDiscreteFunctionalDatum.
        """
        # Field is not nullable
        if parameter_settings is None:
            raise ValueError("Invalid value for 'parameter_settings', must not be 'None'")
        # Field is required
        if parameter_settings is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'parameter_settings', must not be 'Unset'")
        self._parameter_settings = parameter_settings

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
        if not isinstance(other, GsaDiscreteFunctionalDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
