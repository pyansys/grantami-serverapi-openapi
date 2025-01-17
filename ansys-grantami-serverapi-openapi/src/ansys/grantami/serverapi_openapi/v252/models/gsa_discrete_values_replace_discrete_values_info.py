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


class GsaDiscreteValuesReplaceDiscreteValuesInfo(ModelBase):
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
        "discrete_values": "list[GsaDiscreteValuesCreateDiscreteValue]",
    }

    attribute_map: dict[str, str] = {
        "discrete_values": "discreteValues",
    }

    subtype_mapping: dict[str, str] = {
        "discreteValues": "GsaDiscreteValuesCreateDiscreteValue",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, discrete_values: "Union[list[GsaDiscreteValuesCreateDiscreteValue], None, Unset_Type]" = Unset,) -> None:
        """GsaDiscreteValuesReplaceDiscreteValuesInfo - a model defined in Swagger

        Parameters
        ----------
        discrete_values: list[GsaDiscreteValuesCreateDiscreteValue], optional
        """
        self._discrete_values: Union[list[GsaDiscreteValuesCreateDiscreteValue], None, Unset_Type] = Unset

        if discrete_values is not Unset:
            self.discrete_values = discrete_values

    @property
    def discrete_values(self) -> "Union[list[GsaDiscreteValuesCreateDiscreteValue], None, Unset_Type]":
        """Gets the discrete_values of this GsaDiscreteValuesReplaceDiscreteValuesInfo.

        Returns
        -------
        Union[list[GsaDiscreteValuesCreateDiscreteValue], None, Unset_Type]
            The discrete_values of this GsaDiscreteValuesReplaceDiscreteValuesInfo.
        """
        return self._discrete_values

    @discrete_values.setter
    def discrete_values(self, discrete_values: "Union[list[GsaDiscreteValuesCreateDiscreteValue], None, Unset_Type]") -> None:
        """Sets the discrete_values of this GsaDiscreteValuesReplaceDiscreteValuesInfo.

        Parameters
        ----------
        discrete_values: Union[list[GsaDiscreteValuesCreateDiscreteValue], None, Unset_Type]
            The discrete_values of this GsaDiscreteValuesReplaceDiscreteValuesInfo.
        """
        self._discrete_values = discrete_values

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
        if not isinstance(other, GsaDiscreteValuesReplaceDiscreteValuesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

