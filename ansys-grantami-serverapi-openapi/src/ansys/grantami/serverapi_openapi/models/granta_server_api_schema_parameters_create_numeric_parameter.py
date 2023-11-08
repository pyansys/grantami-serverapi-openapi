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

from ansys.grantami.serverapi_openapi.models.granta_server_api_schema_parameters_create_parameter import (
    GrantaServerApiSchemaParametersCreateParameter,
)  # noqa: F401

if TYPE_CHECKING:
    from . import *


class GrantaServerApiSchemaParametersCreateNumericParameter(
    GrantaServerApiSchemaParametersCreateParameter
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
    swagger_types = {
        "default_parameter_value_index": "int",
        "interpolation_type": "GrantaServerApiSchemaParametersParameterInterpolationType",
        "is_restricted": "bool",
        "name": "str",
        "scale_type": "GrantaServerApiSchemaParametersParameterScaleType",
        "values": "list[GrantaServerApiSchemaParametersCreateNumericParameterValue]",
        "guid": "str",
        "help_path": "str",
        "type": "str",
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
    }

    attribute_map = {
        "default_parameter_value_index": "defaultParameterValueIndex",
        "interpolation_type": "interpolationType",
        "is_restricted": "isRestricted",
        "name": "name",
        "scale_type": "scaleType",
        "values": "values",
        "guid": "guid",
        "help_path": "helpPath",
        "type": "type",
        "unit": "unit",
    }

    subtype_mapping = {
        "unit": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
        "values": "GrantaServerApiSchemaParametersCreateNumericParameterValue",
        "interpolationType": "GrantaServerApiSchemaParametersParameterInterpolationType",
        "scaleType": "GrantaServerApiSchemaParametersParameterScaleType",
    }

    discriminator = None

    def __init__(
        self,
        *,
        default_parameter_value_index: "int",
        interpolation_type: "GrantaServerApiSchemaParametersParameterInterpolationType",
        is_restricted: "bool",
        name: "str",
        scale_type: "GrantaServerApiSchemaParametersParameterScaleType",
        values: "List[GrantaServerApiSchemaParametersCreateNumericParameterValue]",
        guid: "Optional[str]" = None,
        help_path: "Optional[str]" = None,
        type: "str" = "numeric",
        unit: "Optional[GrantaServerApiSchemaSlimEntitiesSlimEntity]" = None,
    ) -> None:
        """GrantaServerApiSchemaParametersCreateNumericParameter - a model defined in Swagger

        Parameters
        ----------
            default_parameter_value_index: int
            interpolation_type: GrantaServerApiSchemaParametersParameterInterpolationType
            is_restricted: bool
            name: str
            scale_type: GrantaServerApiSchemaParametersParameterScaleType
            values: List[GrantaServerApiSchemaParametersCreateNumericParameterValue]
            guid: str, optional
            help_path: str, optional
            type: str
            unit: GrantaServerApiSchemaSlimEntitiesSlimEntity, optional
        """
        super().__init__(
            default_parameter_value_index=default_parameter_value_index,
            name=name,
            guid=guid,
            help_path=help_path,
        )
        self._type = None
        self._is_restricted = None
        self._unit = None
        self._values = None
        self._interpolation_type = None
        self._scale_type = None

        self.type = type
        self.is_restricted = is_restricted
        if unit is not None:
            self.unit = unit
        self.values = values
        self.interpolation_type = interpolation_type
        self.scale_type = scale_type

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSchemaParametersCreateNumericParameter.

        Returns
        -------
        str
            The type of this GrantaServerApiSchemaParametersCreateNumericParameter.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSchemaParametersCreateNumericParameter.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSchemaParametersCreateNumericParameter.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    @property
    def is_restricted(self) -> "bool":
        """Gets the is_restricted of this GrantaServerApiSchemaParametersCreateNumericParameter.

        Returns
        -------
        bool
            The is_restricted of this GrantaServerApiSchemaParametersCreateNumericParameter.
        """
        return self._is_restricted

    @is_restricted.setter
    def is_restricted(self, is_restricted: "bool") -> None:
        """Sets the is_restricted of this GrantaServerApiSchemaParametersCreateNumericParameter.

        Parameters
        ----------
        is_restricted: bool
            The is_restricted of this GrantaServerApiSchemaParametersCreateNumericParameter.
        """
        if is_restricted is None:
            raise ValueError("Invalid value for 'is_restricted', must not be 'None'")
        self._is_restricted = is_restricted

    @property
    def unit(self) -> "GrantaServerApiSchemaSlimEntitiesSlimEntity":
        """Gets the unit of this GrantaServerApiSchemaParametersCreateNumericParameter.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimEntity
            The unit of this GrantaServerApiSchemaParametersCreateNumericParameter.
        """
        return self._unit

    @unit.setter
    def unit(self, unit: "GrantaServerApiSchemaSlimEntitiesSlimEntity") -> None:
        """Sets the unit of this GrantaServerApiSchemaParametersCreateNumericParameter.

        Parameters
        ----------
        unit: GrantaServerApiSchemaSlimEntitiesSlimEntity
            The unit of this GrantaServerApiSchemaParametersCreateNumericParameter.
        """
        self._unit = unit

    @property
    def values(
        self,
    ) -> "list[GrantaServerApiSchemaParametersCreateNumericParameterValue]":
        """Gets the values of this GrantaServerApiSchemaParametersCreateNumericParameter.

        Returns
        -------
        list[GrantaServerApiSchemaParametersCreateNumericParameterValue]
            The values of this GrantaServerApiSchemaParametersCreateNumericParameter.
        """
        return self._values

    @values.setter
    def values(
        self, values: "list[GrantaServerApiSchemaParametersCreateNumericParameterValue]"
    ) -> None:
        """Sets the values of this GrantaServerApiSchemaParametersCreateNumericParameter.

        Parameters
        ----------
        values: list[GrantaServerApiSchemaParametersCreateNumericParameterValue]
            The values of this GrantaServerApiSchemaParametersCreateNumericParameter.
        """
        if values is None:
            raise ValueError("Invalid value for 'values', must not be 'None'")
        self._values = values

    @property
    def interpolation_type(
        self,
    ) -> "GrantaServerApiSchemaParametersParameterInterpolationType":
        """Gets the interpolation_type of this GrantaServerApiSchemaParametersCreateNumericParameter.

        Returns
        -------
        GrantaServerApiSchemaParametersParameterInterpolationType
            The interpolation_type of this GrantaServerApiSchemaParametersCreateNumericParameter.
        """
        return self._interpolation_type

    @interpolation_type.setter
    def interpolation_type(
        self,
        interpolation_type: "GrantaServerApiSchemaParametersParameterInterpolationType",
    ) -> None:
        """Sets the interpolation_type of this GrantaServerApiSchemaParametersCreateNumericParameter.

        Parameters
        ----------
        interpolation_type: GrantaServerApiSchemaParametersParameterInterpolationType
            The interpolation_type of this GrantaServerApiSchemaParametersCreateNumericParameter.
        """
        if interpolation_type is None:
            raise ValueError(
                "Invalid value for 'interpolation_type', must not be 'None'"
            )
        self._interpolation_type = interpolation_type

    @property
    def scale_type(self) -> "GrantaServerApiSchemaParametersParameterScaleType":
        """Gets the scale_type of this GrantaServerApiSchemaParametersCreateNumericParameter.

        Returns
        -------
        GrantaServerApiSchemaParametersParameterScaleType
            The scale_type of this GrantaServerApiSchemaParametersCreateNumericParameter.
        """
        return self._scale_type

    @scale_type.setter
    def scale_type(
        self, scale_type: "GrantaServerApiSchemaParametersParameterScaleType"
    ) -> None:
        """Sets the scale_type of this GrantaServerApiSchemaParametersCreateNumericParameter.

        Parameters
        ----------
        scale_type: GrantaServerApiSchemaParametersParameterScaleType
            The scale_type of this GrantaServerApiSchemaParametersCreateNumericParameter.
        """
        if scale_type is None:
            raise ValueError("Invalid value for 'scale_type', must not be 'None'")
        self._scale_type = scale_type

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
        if issubclass(GrantaServerApiSchemaParametersCreateNumericParameter, dict):
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
        if not isinstance(other, GrantaServerApiSchemaParametersCreateNumericParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
