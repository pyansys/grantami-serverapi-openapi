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
from ansys.grantami.serverapi_openapi.models.granta_server_api_search_parameter_constraint import (
    GrantaServerApiSearchParameterConstraint,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSearchDiscreteParameterValueConstraint(
    GrantaServerApiSearchParameterConstraint
):
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
        "_none": "list[float]",
        "any": "list[float]",
        "parameter": "GrantaServerApiObjectIdentifier",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "_none": "none",
        "any": "any",
        "parameter": "parameter",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        _none: "Union[List[float], None, Unset_Type]" = Unset,
        any: "Union[List[float], None, Unset_Type]" = Unset,
        parameter: "Union[GrantaServerApiObjectIdentifier, Unset_Type]" = Unset,
        type: "str" = "discreteValue",
    ) -> None:
        """GrantaServerApiSearchDiscreteParameterValueConstraint - a model defined in Swagger

        Parameters
        ----------
        _none: List[float], optional
        any: List[float], optional
        parameter: GrantaServerApiObjectIdentifier, optional
        type: str
        """
        super().__init__(parameter=parameter)
        self._any: Union[List[float], None, Unset_Type] = Unset
        self.__none: Union[List[float], None, Unset_Type] = Unset
        self._type: str

        if any is not Unset:
            self.any = any
        if _none is not Unset:
            self._none = _none
        self.type = type

    @property
    def any(self) -> "Union[List[float], None, Unset_Type]":
        """Gets the any of this GrantaServerApiSearchDiscreteParameterValueConstraint.

        Returns
        -------
        Union[List[float], None, Unset_Type]
            The any of this GrantaServerApiSearchDiscreteParameterValueConstraint.
        """
        return self._any

    @any.setter
    def any(self, any: "Union[List[float], None, Unset_Type]") -> None:
        """Sets the any of this GrantaServerApiSearchDiscreteParameterValueConstraint.

        Parameters
        ----------
        any: Union[List[float], None, Unset_Type]
            The any of this GrantaServerApiSearchDiscreteParameterValueConstraint.
        """
        self._any = any

    @property
    def _none(self) -> "Union[List[float], None, Unset_Type]":
        """Gets the _none of this GrantaServerApiSearchDiscreteParameterValueConstraint.

        Returns
        -------
        Union[List[float], None, Unset_Type]
            The _none of this GrantaServerApiSearchDiscreteParameterValueConstraint.
        """
        return self.__none

    @_none.setter
    def _none(self, _none: "Union[List[float], None, Unset_Type]") -> None:
        """Sets the _none of this GrantaServerApiSearchDiscreteParameterValueConstraint.

        Parameters
        ----------
        _none: Union[List[float], None, Unset_Type]
            The _none of this GrantaServerApiSearchDiscreteParameterValueConstraint.
        """
        self.__none = _none

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchDiscreteParameterValueConstraint.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchDiscreteParameterValueConstraint.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchDiscreteParameterValueConstraint.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchDiscreteParameterValueConstraint.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

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
        if not isinstance(other, GrantaServerApiSearchDiscreteParameterValueConstraint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
