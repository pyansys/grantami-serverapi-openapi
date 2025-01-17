"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.v252.models.gsa_set_datum import GsaSetDatum  # noqa: F401
from ansys.grantami.serverapi_openapi.v252.models.gsa_set_datum_type import GsaSetDatumType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaSetDiscreteDatum(GsaSetDatum):
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
        "discrete_values": "list[GsaSlimEntity]",
        "set_datum_type": "GsaSetDatumType",
    }

    attribute_map: dict[str, str] = {
        "discrete_values": "discreteValues",
        "set_datum_type": "setDatumType",
    }

    subtype_mapping: dict[str, str] = {
        "discreteValues": "GsaSlimEntity",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, discrete_values: "list[GsaSlimEntity]", set_datum_type: "GsaSetDatumType" = GsaSetDatumType.DISCRETE,) -> None:
        """GsaSetDiscreteDatum - a model defined in Swagger

        Parameters
        ----------
        discrete_values: list[GsaSlimEntity]
        set_datum_type: GsaSetDatumType
        """
        super().__init__(set_datum_type=set_datum_type)
        self._discrete_values: list[GsaSlimEntity]

        self.discrete_values = discrete_values

    @property
    def discrete_values(self) -> "list[GsaSlimEntity]":
        """Gets the discrete_values of this GsaSetDiscreteDatum.

        Returns
        -------
        list[GsaSlimEntity]
            The discrete_values of this GsaSetDiscreteDatum.
        """
        return self._discrete_values

    @discrete_values.setter
    def discrete_values(self, discrete_values: "list[GsaSlimEntity]") -> None:
        """Sets the discrete_values of this GsaSetDiscreteDatum.

        Parameters
        ----------
        discrete_values: list[GsaSlimEntity]
            The discrete_values of this GsaSetDiscreteDatum.
        """
        # Field is not nullable
        if discrete_values is None:
            raise ValueError("Invalid value for 'discrete_values', must not be 'None'")
        # Field is required
        if discrete_values is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'discrete_values', must not be 'Unset'")
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
        if not isinstance(other, GsaSetDiscreteDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

