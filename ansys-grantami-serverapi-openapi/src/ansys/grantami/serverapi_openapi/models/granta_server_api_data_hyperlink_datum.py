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
from typing import (
    TYPE_CHECKING,
    Any,
    BinaryIO,
    Dict,
    List,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.models.granta_server_api_data_applicable_datum import (
    GrantaServerApiDataApplicableDatum,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiDataHyperlinkDatum(GrantaServerApiDataApplicableDatum):
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
        "address": "str",
        "description": "str",
        "target": "GrantaServerApiDataHyperlinkTarget",
        "datum_type": "str",
        "not_applicable": "str",
    }

    attribute_map: Dict[str, str] = {
        "address": "address",
        "description": "description",
        "target": "target",
        "datum_type": "datumType",
        "not_applicable": "notApplicable",
    }

    subtype_mapping: Dict[str, str] = {
        "target": "GrantaServerApiDataHyperlinkTarget",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        address: "str",
        description: "str",
        target: "GrantaServerApiDataHyperlinkTarget",
        datum_type: "str" = "hyperlink",
        not_applicable: "str" = "applicable",
    ) -> None:
        """GrantaServerApiDataHyperlinkDatum - a model defined in Swagger

        Parameters
        ----------
        address: str
        description: str
        target: GrantaServerApiDataHyperlinkTarget
        datum_type: str
        not_applicable: str
        """
        super().__init__(not_applicable=not_applicable)
        self._datum_type: str
        self._address: str
        self._description: str
        self._target: GrantaServerApiDataHyperlinkTarget

        self.datum_type = datum_type
        self.address = address
        self.description = description
        self.target = target

    @property
    def datum_type(self) -> "str":
        """Gets the datum_type of this GrantaServerApiDataHyperlinkDatum.

        Returns
        -------
        str
            The datum_type of this GrantaServerApiDataHyperlinkDatum.
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type: "str") -> None:
        """Sets the datum_type of this GrantaServerApiDataHyperlinkDatum.

        Parameters
        ----------
        datum_type: str
            The datum_type of this GrantaServerApiDataHyperlinkDatum.
        """
        # Field is not nullable
        if datum_type is None:
            raise ValueError("Invalid value for 'datum_type', must not be 'None'")
        # Field is required
        if datum_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'datum_type', must not be 'Unset'")
        self._datum_type = datum_type

    @property
    def address(self) -> "str":
        """Gets the address of this GrantaServerApiDataHyperlinkDatum.

        Returns
        -------
        str
            The address of this GrantaServerApiDataHyperlinkDatum.
        """
        return self._address

    @address.setter
    def address(self, address: "str") -> None:
        """Sets the address of this GrantaServerApiDataHyperlinkDatum.

        Parameters
        ----------
        address: str
            The address of this GrantaServerApiDataHyperlinkDatum.
        """
        # Field is not nullable
        if address is None:
            raise ValueError("Invalid value for 'address', must not be 'None'")
        # Field is required
        if address is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'address', must not be 'Unset'")
        self._address = address

    @property
    def description(self) -> "str":
        """Gets the description of this GrantaServerApiDataHyperlinkDatum.

        Returns
        -------
        str
            The description of this GrantaServerApiDataHyperlinkDatum.
        """
        return self._description

    @description.setter
    def description(self, description: "str") -> None:
        """Sets the description of this GrantaServerApiDataHyperlinkDatum.

        Parameters
        ----------
        description: str
            The description of this GrantaServerApiDataHyperlinkDatum.
        """
        # Field is not nullable
        if description is None:
            raise ValueError("Invalid value for 'description', must not be 'None'")
        # Field is required
        if description is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'description', must not be 'Unset'")
        self._description = description

    @property
    def target(self) -> "GrantaServerApiDataHyperlinkTarget":
        """Gets the target of this GrantaServerApiDataHyperlinkDatum.

        Returns
        -------
        GrantaServerApiDataHyperlinkTarget
            The target of this GrantaServerApiDataHyperlinkDatum.
        """
        return self._target

    @target.setter
    def target(self, target: "GrantaServerApiDataHyperlinkTarget") -> None:
        """Sets the target of this GrantaServerApiDataHyperlinkDatum.

        Parameters
        ----------
        target: GrantaServerApiDataHyperlinkTarget
            The target of this GrantaServerApiDataHyperlinkDatum.
        """
        # Field is not nullable
        if target is None:
            raise ValueError("Invalid value for 'target', must not be 'None'")
        # Field is required
        if target is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'target', must not be 'Unset'")
        self._target = target

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
        if not isinstance(other, GrantaServerApiDataHyperlinkDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
