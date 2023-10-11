"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase

from ansys.grantami.serverapi_openapi.models.granta_server_api_search_datum_criterion import GrantaServerApiSearchDatumCriterion  # noqa: F401

if TYPE_CHECKING:
    from . import *

class GrantaServerApiSearchFloatFunctionalDatumCriterion(GrantaServerApiSearchDatumCriterion):
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

    """
    swagger_types = {
        "constraints": "list[GrantaServerApiSearchParameterConstraint]",
        "gte": "float",
        "lte": "float",
        "type": "str",
        "unit": "str",
    }

    attribute_map = {
        "constraints": "constraints",
        "gte": "gte",
        "lte": "lte",
        "type": "type",
        "unit": "unit",
    }

    subtype_mapping = {
        "constraints": "GrantaServerApiSearchParameterConstraint",
    }

    def __init__(self, *, constraints: "Optional[List[GrantaServerApiSearchParameterConstraint]]" = None, gte: "Optional[float]" = None, lte: "Optional[float]" = None, type: "str" = 'floatFunctionalData', unit: "Optional[str]" = None,) -> None:
        """GrantaServerApiSearchFloatFunctionalDatumCriterion - a model defined in Swagger

        Parameters
        ----------
            constraints: List[GrantaServerApiSearchParameterConstraint], optional
            gte: float, optional
            lte: float, optional
            type: str
            unit: str, optional
        """
        super().__init__()
        self._type = None
        self._gte = None
        self._lte = None
        self._unit = None
        self._constraints = None
        self.discriminator = None
        self.type = type
        if gte is not None:
            self.gte = gte
        if lte is not None:
            self.lte = lte
        if unit is not None:
            self.unit = unit
        if constraints is not None:
            self.constraints = constraints

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchFloatFunctionalDatumCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchFloatFunctionalDatumCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchFloatFunctionalDatumCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchFloatFunctionalDatumCriterion.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @property
    def gte(self) -> "float":
        """Gets the gte of this GrantaServerApiSearchFloatFunctionalDatumCriterion.
        Greater than or equal to

        Returns
        -------
        float
            The gte of this GrantaServerApiSearchFloatFunctionalDatumCriterion.
        """
        return self._gte

    @gte.setter
    def gte(self, gte: "float") -> None:
        """Sets the gte of this GrantaServerApiSearchFloatFunctionalDatumCriterion.
        Greater than or equal to

        Parameters
        ----------
        gte: float
            The gte of this GrantaServerApiSearchFloatFunctionalDatumCriterion.
        """
        self._gte = gte

    @property
    def lte(self) -> "float":
        """Gets the lte of this GrantaServerApiSearchFloatFunctionalDatumCriterion.
        Less than or equal to

        Returns
        -------
        float
            The lte of this GrantaServerApiSearchFloatFunctionalDatumCriterion.
        """
        return self._lte

    @lte.setter
    def lte(self, lte: "float") -> None:
        """Sets the lte of this GrantaServerApiSearchFloatFunctionalDatumCriterion.
        Less than or equal to

        Parameters
        ----------
        lte: float
            The lte of this GrantaServerApiSearchFloatFunctionalDatumCriterion.
        """
        self._lte = lte

    @property
    def unit(self) -> "str":
        """Gets the unit of this GrantaServerApiSearchFloatFunctionalDatumCriterion.
        Optional unit string. If not included, the gte and lte values are assumed to be in database units.

        Returns
        -------
        str
            The unit of this GrantaServerApiSearchFloatFunctionalDatumCriterion.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "str") -> None:
        """Sets the unit of this GrantaServerApiSearchFloatFunctionalDatumCriterion.
        Optional unit string. If not included, the gte and lte values are assumed to be in database units.

        Parameters
        ----------
        unit: str
            The unit of this GrantaServerApiSearchFloatFunctionalDatumCriterion.
        """
        self._unit = unit

    @property
    def constraints(self) -> "list[GrantaServerApiSearchParameterConstraint]":
        """Gets the constraints of this GrantaServerApiSearchFloatFunctionalDatumCriterion.
        Constraints on the parameters of the attribute. Unspecified parameters will be assumed to be unconstrained.

        Returns
        -------
        list[GrantaServerApiSearchParameterConstraint]
            The constraints of this GrantaServerApiSearchFloatFunctionalDatumCriterion.
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints: "list[GrantaServerApiSearchParameterConstraint]") -> None:
        """Sets the constraints of this GrantaServerApiSearchFloatFunctionalDatumCriterion.
        Constraints on the parameters of the attribute. Unspecified parameters will be assumed to be unconstrained.

        Parameters
        ----------
        constraints: list[GrantaServerApiSearchParameterConstraint]
            The constraints of this GrantaServerApiSearchFloatFunctionalDatumCriterion.
        """
        self._constraints = constraints

    def get_real_child_model(self, data: ModelBase) -> str:
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

    def to_dict(self) -> Dict:
        """Returns the model properties as a dict

        Returns
        -------
        Dict
            Dictionary indexed by property name containing all the model properties
        """
        result = {}

        for attr in self.swagger_types.keys():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GrantaServerApiSearchFloatFunctionalDatumCriterion, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model

        Returns
        -------
        str
            String representation of the model as a dictionary
        """
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiSearchFloatFunctionalDatumCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
