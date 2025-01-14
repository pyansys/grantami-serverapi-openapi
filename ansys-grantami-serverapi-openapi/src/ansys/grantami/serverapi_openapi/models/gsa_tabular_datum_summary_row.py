"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaTabularDatumSummaryRow(ModelBase):
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
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "cells": "list[GsaTabularDatumRollupCell]",
    }

    attribute_map: dict[str, str] = {
        "cells": "cells",
    }

    subtype_mapping: dict[str, str] = {
        "cells": "GsaTabularDatumRollupCell",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, cells: "list[GsaTabularDatumRollupCell]",) -> None:
        """GsaTabularDatumSummaryRow - a model defined in Swagger

        Parameters
        ----------
        cells: list[GsaTabularDatumRollupCell]
        """
        self._cells: list[GsaTabularDatumRollupCell]

        self.cells = cells

    @property
    def cells(self) -> "list[GsaTabularDatumRollupCell]":
        """Gets the cells of this GsaTabularDatumSummaryRow.

        Returns
        -------
        list[GsaTabularDatumRollupCell]
            The cells of this GsaTabularDatumSummaryRow.
        """
        return self._cells

    @cells.setter
    def cells(self, cells: "list[GsaTabularDatumRollupCell]") -> None:
        """Sets the cells of this GsaTabularDatumSummaryRow.

        Parameters
        ----------
        cells: list[GsaTabularDatumRollupCell]
            The cells of this GsaTabularDatumSummaryRow.
        """
        # Field is not nullable
        if cells is None:
            raise ValueError("Invalid value for 'cells', must not be 'None'")
        # Field is required
        if cells is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'cells', must not be 'Unset'")
        self._cells = cells

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
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
        if not isinstance(other, GsaTabularDatumSummaryRow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

