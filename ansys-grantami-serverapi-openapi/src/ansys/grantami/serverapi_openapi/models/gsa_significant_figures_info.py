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


class GsaSignificantFiguresInfo(ModelBase):
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
        "entered_value": "float",
        "significant_figures": "int",
        "entered_unit": "GsaSlimUnit",
    }

    attribute_map: dict[str, str] = {
        "entered_value": "enteredValue",
        "significant_figures": "significantFigures",
        "entered_unit": "enteredUnit",
    }

    subtype_mapping: dict[str, str] = {
        "enteredUnit": "GsaSlimUnit",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, entered_value: "float", significant_figures: "int", entered_unit: "Union[GsaSlimUnit, Unset_Type]" = Unset,) -> None:
        """GsaSignificantFiguresInfo - a model defined in Swagger

        Parameters
        ----------
        entered_value: float
        significant_figures: int
        entered_unit: GsaSlimUnit, optional
        """
        self._significant_figures: int
        self._entered_value: float
        self._entered_unit: Union[GsaSlimUnit, Unset_Type] = Unset

        self.significant_figures = significant_figures
        self.entered_value = entered_value
        if entered_unit is not Unset:
            self.entered_unit = entered_unit

    @property
    def significant_figures(self) -> "int":
        """Gets the significant_figures of this GsaSignificantFiguresInfo.

        Returns
        -------
        int
            The significant_figures of this GsaSignificantFiguresInfo.
        """
        return self._significant_figures

    @significant_figures.setter
    def significant_figures(self, significant_figures: "int") -> None:
        """Sets the significant_figures of this GsaSignificantFiguresInfo.

        Parameters
        ----------
        significant_figures: int
            The significant_figures of this GsaSignificantFiguresInfo.
        """
        # Field is not nullable
        if significant_figures is None:
            raise ValueError("Invalid value for 'significant_figures', must not be 'None'")
        # Field is required
        if significant_figures is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'significant_figures', must not be 'Unset'")
        self._significant_figures = significant_figures

    @property
    def entered_value(self) -> "float":
        """Gets the entered_value of this GsaSignificantFiguresInfo.

        Returns
        -------
        float
            The entered_value of this GsaSignificantFiguresInfo.
        """
        return self._entered_value

    @entered_value.setter
    def entered_value(self, entered_value: "float") -> None:
        """Sets the entered_value of this GsaSignificantFiguresInfo.

        Parameters
        ----------
        entered_value: float
            The entered_value of this GsaSignificantFiguresInfo.
        """
        # Field is not nullable
        if entered_value is None:
            raise ValueError("Invalid value for 'entered_value', must not be 'None'")
        # Field is required
        if entered_value is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'entered_value', must not be 'Unset'")
        self._entered_value = entered_value

    @property
    def entered_unit(self) -> "Union[GsaSlimUnit, Unset_Type]":
        """Gets the entered_unit of this GsaSignificantFiguresInfo.

        Returns
        -------
        Union[GsaSlimUnit, Unset_Type]
            The entered_unit of this GsaSignificantFiguresInfo.
        """
        return self._entered_unit

    @entered_unit.setter
    def entered_unit(self, entered_unit: "Union[GsaSlimUnit, Unset_Type]") -> None:
        """Sets the entered_unit of this GsaSignificantFiguresInfo.

        Parameters
        ----------
        entered_unit: Union[GsaSlimUnit, Unset_Type]
            The entered_unit of this GsaSignificantFiguresInfo.
        """
        # Field is not nullable
        if entered_unit is None:
            raise ValueError("Invalid value for 'entered_unit', must not be 'None'")
        self._entered_unit = entered_unit

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
        if not isinstance(other, GsaSignificantFiguresInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

