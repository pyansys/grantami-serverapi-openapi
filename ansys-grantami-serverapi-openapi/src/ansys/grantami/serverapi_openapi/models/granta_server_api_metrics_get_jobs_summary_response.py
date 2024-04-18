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


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiMetricsGetJobsSummaryResponse(ModelBase):
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
        "jobs": "list[GrantaServerApiMetricsJobTypeAndStatus]",
    }

    attribute_map: Dict[str, str] = {
        "jobs": "jobs",
    }

    subtype_mapping: Dict[str, str] = {
        "jobs": "GrantaServerApiMetricsJobTypeAndStatus",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        jobs: "Union[List[GrantaServerApiMetricsJobTypeAndStatus], None, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiMetricsGetJobsSummaryResponse - a model defined in Swagger

        Parameters
        ----------
        jobs: List[GrantaServerApiMetricsJobTypeAndStatus], optional
        """
        self._jobs: Union[
            List[GrantaServerApiMetricsJobTypeAndStatus], None, Unset_Type
        ] = Unset

        if jobs is not Unset:
            self.jobs = jobs

    @property
    def jobs(
        self,
    ) -> "Union[List[GrantaServerApiMetricsJobTypeAndStatus], None, Unset_Type]":
        """Gets the jobs of this GrantaServerApiMetricsGetJobsSummaryResponse.

        Returns
        -------
        Union[List[GrantaServerApiMetricsJobTypeAndStatus], None, Unset_Type]
            The jobs of this GrantaServerApiMetricsGetJobsSummaryResponse.
        """
        return self._jobs

    @jobs.setter
    def jobs(
        self,
        jobs: "Union[List[GrantaServerApiMetricsJobTypeAndStatus], None, Unset_Type]",
    ) -> None:
        """Sets the jobs of this GrantaServerApiMetricsGetJobsSummaryResponse.

        Parameters
        ----------
        jobs: Union[List[GrantaServerApiMetricsJobTypeAndStatus], None, Unset_Type]
            The jobs of this GrantaServerApiMetricsGetJobsSummaryResponse.
        """
        self._jobs = jobs

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
        if not isinstance(other, GrantaServerApiMetricsGetJobsSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
