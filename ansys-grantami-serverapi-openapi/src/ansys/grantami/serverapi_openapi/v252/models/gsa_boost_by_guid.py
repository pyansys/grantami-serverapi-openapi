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


class GsaBoostByGuid(ModelBase):
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
        "boost_factor": "float",
        "guid": "str",
    }

    attribute_map: dict[str, str] = {
        "boost_factor": "boostFactor",
        "guid": "guid",
    }

    subtype_mapping: dict[str, str] = {
    }

    discriminator: Optional[str] = None

    def __init__(self, *, boost_factor: "Union[float, Unset_Type]" = Unset, guid: "Union[str, Unset_Type]" = Unset,) -> None:
        """GsaBoostByGuid - a model defined in Swagger

        Parameters
        ----------
        boost_factor: float, optional
        guid: str, optional
        """
        self._guid: Union[str, Unset_Type] = Unset
        self._boost_factor: Union[float, Unset_Type] = Unset

        if guid is not Unset:
            self.guid = guid
        if boost_factor is not Unset:
            self.boost_factor = boost_factor

    @property
    def guid(self) -> "Union[str, Unset_Type]":
        """Gets the guid of this GsaBoostByGuid.

        Returns
        -------
        Union[str, Unset_Type]
            The guid of this GsaBoostByGuid.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, Unset_Type]") -> None:
        """Sets the guid of this GsaBoostByGuid.

        Parameters
        ----------
        guid: Union[str, Unset_Type]
            The guid of this GsaBoostByGuid.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        self._guid = guid

    @property
    def boost_factor(self) -> "Union[float, Unset_Type]":
        """Gets the boost_factor of this GsaBoostByGuid.

        Returns
        -------
        Union[float, Unset_Type]
            The boost_factor of this GsaBoostByGuid.
        """
        return self._boost_factor

    @boost_factor.setter
    def boost_factor(self, boost_factor: "Union[float, Unset_Type]") -> None:
        """Sets the boost_factor of this GsaBoostByGuid.

        Parameters
        ----------
        boost_factor: Union[float, Unset_Type]
            The boost_factor of this GsaBoostByGuid.
        """
        # Field is not nullable
        if boost_factor is None:
            raise ValueError("Invalid value for 'boost_factor', must not be 'None'")
        self._boost_factor = boost_factor

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
        if not isinstance(other, GsaBoostByGuid):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

