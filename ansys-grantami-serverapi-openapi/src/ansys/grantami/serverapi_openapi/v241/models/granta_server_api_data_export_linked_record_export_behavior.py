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


class GrantaServerApiDataExportLinkedRecordExportBehavior(ModelBase):
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
        "linked_records_criterion": "GrantaServerApiSearchCriterion",
        "summary_roll_up_type": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "tabular_row_behavior": "GrantaServerApiDataExportTabularRowExportBehaviour",
    }

    attribute_map = {
        "linked_records_criterion": "linkedRecordsCriterion",
        "summary_roll_up_type": "summaryRollUpType",
        "tabular_row_behavior": "tabularRowBehavior",
    }

    subtype_mapping = {
        "tabularRowBehavior": "GrantaServerApiDataExportTabularRowExportBehaviour",
        "summaryRollUpType": "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
        "linkedRecordsCriterion": "GrantaServerApiSearchCriterion",
    }

    discriminator = None

    def __init__(
        self,
        *,
        linked_records_criterion: "Optional[GrantaServerApiSearchCriterion]" = None,
        summary_roll_up_type: "Optional[GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType]" = None,
        tabular_row_behavior: "Optional[GrantaServerApiDataExportTabularRowExportBehaviour]" = None,
    ) -> None:
        """GrantaServerApiDataExportLinkedRecordExportBehavior - a model defined in Swagger

        Parameters
        ----------
            linked_records_criterion: GrantaServerApiSearchCriterion, optional
            summary_roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType, optional
            tabular_row_behavior: GrantaServerApiDataExportTabularRowExportBehaviour, optional
        """
        self._tabular_row_behavior = None
        self._summary_roll_up_type = None
        self._linked_records_criterion = None

        if tabular_row_behavior is not None:
            self.tabular_row_behavior = tabular_row_behavior
        if summary_roll_up_type is not None:
            self.summary_roll_up_type = summary_roll_up_type
        if linked_records_criterion is not None:
            self.linked_records_criterion = linked_records_criterion

    @property
    def tabular_row_behavior(
        self,
    ) -> "GrantaServerApiDataExportTabularRowExportBehaviour":
        """Gets the tabular_row_behavior of this GrantaServerApiDataExportLinkedRecordExportBehavior.

        Returns
        -------
        GrantaServerApiDataExportTabularRowExportBehaviour
            The tabular_row_behavior of this GrantaServerApiDataExportLinkedRecordExportBehavior.
        """
        return self._tabular_row_behavior

    @tabular_row_behavior.setter
    def tabular_row_behavior(
        self, tabular_row_behavior: "GrantaServerApiDataExportTabularRowExportBehaviour"
    ) -> None:
        """Sets the tabular_row_behavior of this GrantaServerApiDataExportLinkedRecordExportBehavior.

        Parameters
        ----------
        tabular_row_behavior: GrantaServerApiDataExportTabularRowExportBehaviour
            The tabular_row_behavior of this GrantaServerApiDataExportLinkedRecordExportBehavior.
        """
        self._tabular_row_behavior = tabular_row_behavior

    @property
    def summary_roll_up_type(
        self,
    ) -> "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType":
        """Gets the summary_roll_up_type of this GrantaServerApiDataExportLinkedRecordExportBehavior.

        Returns
        -------
        GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
            The summary_roll_up_type of this GrantaServerApiDataExportLinkedRecordExportBehavior.
        """
        return self._summary_roll_up_type

    @summary_roll_up_type.setter
    def summary_roll_up_type(
        self,
        summary_roll_up_type: "GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType",
    ) -> None:
        """Sets the summary_roll_up_type of this GrantaServerApiDataExportLinkedRecordExportBehavior.

        Parameters
        ----------
        summary_roll_up_type: GrantaServerApiSchemaTabularColumnsTabularColumnRollUpType
            The summary_roll_up_type of this GrantaServerApiDataExportLinkedRecordExportBehavior.
        """
        self._summary_roll_up_type = summary_roll_up_type

    @property
    def linked_records_criterion(self) -> "GrantaServerApiSearchCriterion":
        """Gets the linked_records_criterion of this GrantaServerApiDataExportLinkedRecordExportBehavior.

        Returns
        -------
        GrantaServerApiSearchCriterion
            The linked_records_criterion of this GrantaServerApiDataExportLinkedRecordExportBehavior.
        """
        return self._linked_records_criterion

    @linked_records_criterion.setter
    def linked_records_criterion(
        self, linked_records_criterion: "GrantaServerApiSearchCriterion"
    ) -> None:
        """Sets the linked_records_criterion of this GrantaServerApiDataExportLinkedRecordExportBehavior.

        Parameters
        ----------
        linked_records_criterion: GrantaServerApiSearchCriterion
            The linked_records_criterion of this GrantaServerApiDataExportLinkedRecordExportBehavior.
        """
        self._linked_records_criterion = linked_records_criterion

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
        if not isinstance(other, GrantaServerApiDataExportLinkedRecordExportBehavior):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
