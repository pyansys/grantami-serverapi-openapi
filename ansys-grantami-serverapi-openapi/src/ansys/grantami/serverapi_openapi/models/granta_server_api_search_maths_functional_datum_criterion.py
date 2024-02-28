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
from ansys.grantami.serverapi_openapi.models.granta_server_api_search_datum_criterion import (
    GrantaServerApiSearchDatumCriterion,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSearchMathsFunctionalDatumCriterion(
    GrantaServerApiSearchDatumCriterion
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
        "constraints": "list[GrantaServerApiSearchParameterConstraint]",
        "gte": "float",
        "lte": "float",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "constraints": "constraints",
        "gte": "gte",
        "lte": "lte",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {
        "constraints": "GrantaServerApiSearchParameterConstraint",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        constraints: "Union[List[GrantaServerApiSearchParameterConstraint], None, Unset_Type]" = Unset,
        gte: "Union[float, None, Unset_Type]" = Unset,
        lte: "Union[float, None, Unset_Type]" = Unset,
        type: "str" = "mathsFunctional",
    ) -> None:
        """GrantaServerApiSearchMathsFunctionalDatumCriterion - a model defined in Swagger

        Parameters
        ----------
        constraints: List[GrantaServerApiSearchParameterConstraint], optional
        gte: float, optional
        lte: float, optional
        type: str
        """
        super().__init__()
        self._type: str
        self._gte: Union[float, None, Unset_Type] = Unset
        self._lte: Union[float, None, Unset_Type] = Unset
        self._constraints: Union[
            List[GrantaServerApiSearchParameterConstraint], None, Unset_Type
        ] = Unset

        self.type = type
        if gte is not Unset:
            self.gte = gte
        if lte is not Unset:
            self.lte = lte
        if constraints is not Unset:
            self.constraints = constraints

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchMathsFunctionalDatumCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchMathsFunctionalDatumCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchMathsFunctionalDatumCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchMathsFunctionalDatumCriterion.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @property
    def gte(self) -> "Union[float, None, Unset_Type]":
        """Gets the gte of this GrantaServerApiSearchMathsFunctionalDatumCriterion.
        Greater than or equal to

        Returns
        -------
        Union[float, None, Unset_Type]
            The gte of this GrantaServerApiSearchMathsFunctionalDatumCriterion.
        """
        return self._gte

    @gte.setter
    def gte(self, gte: "Union[float, None, Unset_Type]") -> None:
        """Sets the gte of this GrantaServerApiSearchMathsFunctionalDatumCriterion.
        Greater than or equal to

        Parameters
        ----------
        gte: Union[float, None, Unset_Type]
            The gte of this GrantaServerApiSearchMathsFunctionalDatumCriterion.
        """
        self._gte = gte

    @property
    def lte(self) -> "Union[float, None, Unset_Type]":
        """Gets the lte of this GrantaServerApiSearchMathsFunctionalDatumCriterion.
        Less than or equal to

        Returns
        -------
        Union[float, None, Unset_Type]
            The lte of this GrantaServerApiSearchMathsFunctionalDatumCriterion.
        """
        return self._lte

    @lte.setter
    def lte(self, lte: "Union[float, None, Unset_Type]") -> None:
        """Sets the lte of this GrantaServerApiSearchMathsFunctionalDatumCriterion.
        Less than or equal to

        Parameters
        ----------
        lte: Union[float, None, Unset_Type]
            The lte of this GrantaServerApiSearchMathsFunctionalDatumCriterion.
        """
        self._lte = lte

    @property
    def constraints(
        self,
    ) -> "Union[List[GrantaServerApiSearchParameterConstraint], None, Unset_Type]":
        """Gets the constraints of this GrantaServerApiSearchMathsFunctionalDatumCriterion.
        Constraints on the parameters of the attribute. Unspecified parameters will be assumed to be unconstrained.

        Returns
        -------
        Union[List[GrantaServerApiSearchParameterConstraint], None, Unset_Type]
            The constraints of this GrantaServerApiSearchMathsFunctionalDatumCriterion.
        """
        return self._constraints

    @constraints.setter
    def constraints(
        self,
        constraints: "Union[List[GrantaServerApiSearchParameterConstraint], None, Unset_Type]",
    ) -> None:
        """Sets the constraints of this GrantaServerApiSearchMathsFunctionalDatumCriterion.
        Constraints on the parameters of the attribute. Unspecified parameters will be assumed to be unconstrained.

        Parameters
        ----------
        constraints: Union[List[GrantaServerApiSearchParameterConstraint], None, Unset_Type]
            The constraints of this GrantaServerApiSearchMathsFunctionalDatumCriterion.
        """
        self._constraints = constraints

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
        if not isinstance(other, GrantaServerApiSearchMathsFunctionalDatumCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
