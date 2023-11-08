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


if TYPE_CHECKING:
    from . import *


class GrantaServerApiSchemaUnitsUnitMapping(ModelBase):
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
        "equivalent_unit": "GrantaServerApiSchemaSlimEntitiesSlimUnit",
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimUnit",
    }

    attribute_map = {
        "equivalent_unit": "equivalentUnit",
        "unit": "unit",
    }

    subtype_mapping = {
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimUnit",
        "equivalentUnit": "GrantaServerApiSchemaSlimEntitiesSlimUnit",
    }

    discriminator = None

    def __init__(
        self,
        *,
        equivalent_unit: "GrantaServerApiSchemaSlimEntitiesSlimUnit",
        unit: "GrantaServerApiSchemaSlimEntitiesSlimUnit",
    ) -> None:
        """GrantaServerApiSchemaUnitsUnitMapping - a model defined in Swagger

        Parameters
        ----------
            equivalent_unit: GrantaServerApiSchemaSlimEntitiesSlimUnit
            unit: GrantaServerApiSchemaSlimEntitiesSlimUnit
        """
        self._unit = None
        self._equivalent_unit = None

        self.unit = unit
        self.equivalent_unit = equivalent_unit

    @property
    def unit(self) -> "GrantaServerApiSchemaSlimEntitiesSlimUnit":
        """Gets the unit of this GrantaServerApiSchemaUnitsUnitMapping.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimUnit
            The unit of this GrantaServerApiSchemaUnitsUnitMapping.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "GrantaServerApiSchemaSlimEntitiesSlimUnit") -> None:
        """Sets the unit of this GrantaServerApiSchemaUnitsUnitMapping.

        Parameters
        ----------
        unit: GrantaServerApiSchemaSlimEntitiesSlimUnit
            The unit of this GrantaServerApiSchemaUnitsUnitMapping.
        """
        if unit is None:
            raise ValueError("Invalid value for 'unit', must not be 'None'")
        self._unit = unit

    @property
    def equivalent_unit(self) -> "GrantaServerApiSchemaSlimEntitiesSlimUnit":
        """Gets the equivalent_unit of this GrantaServerApiSchemaUnitsUnitMapping.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimUnit
            The equivalent_unit of this GrantaServerApiSchemaUnitsUnitMapping.
        """
        return self._equivalent_unit

    @equivalent_unit.setter
    def equivalent_unit(
        self, equivalent_unit: "GrantaServerApiSchemaSlimEntitiesSlimUnit"
    ) -> None:
        """Sets the equivalent_unit of this GrantaServerApiSchemaUnitsUnitMapping.

        Parameters
        ----------
        equivalent_unit: GrantaServerApiSchemaSlimEntitiesSlimUnit
            The equivalent_unit of this GrantaServerApiSchemaUnitsUnitMapping.
        """
        if equivalent_unit is None:
            raise ValueError("Invalid value for 'equivalent_unit', must not be 'None'")
        self._equivalent_unit = equivalent_unit

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
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(GrantaServerApiSchemaUnitsUnitMapping, dict):
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
        if not isinstance(other, GrantaServerApiSchemaUnitsUnitMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
