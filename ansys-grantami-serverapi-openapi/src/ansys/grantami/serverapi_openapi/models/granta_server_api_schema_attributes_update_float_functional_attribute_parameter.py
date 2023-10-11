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

class GrantaServerApiSchemaAttributesUpdateFloatFunctionalAttributeParameter(ModelBase):
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
        "default_value": "float",
        "interpolation_method": "GrantaServerApiSchemaAttributesAttributeInterpolationMethod",
        "parameter_guid": "str",
        "scale_type": "GrantaServerApiSchemaAttributesAttributeScaleType",
    }

    attribute_map = {
        "default_value": "defaultValue",
        "interpolation_method": "interpolationMethod",
        "parameter_guid": "parameterGuid",
        "scale_type": "scaleType",
    }

    subtype_mapping = {
        "interpolationMethod": "GrantaServerApiSchemaAttributesAttributeInterpolationMethod",
        "scaleType": "GrantaServerApiSchemaAttributesAttributeScaleType",
    }

    def __init__(self, *, default_value: "Optional[float]" = None, interpolation_method: "Optional[GrantaServerApiSchemaAttributesAttributeInterpolationMethod]" = None, parameter_guid: "Optional[str]" = None, scale_type: "Optional[GrantaServerApiSchemaAttributesAttributeScaleType]" = None,) -> None:
        """GrantaServerApiSchemaAttributesUpdateFloatFunctionalAttributeParameter - a model defined in Swagger

        Parameters
        ----------
            default_value: float, optional
            interpolation_method: GrantaServerApiSchemaAttributesAttributeInterpolationMethod, optional
            parameter_guid: str, optional
            scale_type: GrantaServerApiSchemaAttributesAttributeScaleType, optional
        """
        self._parameter_guid = None
        self._default_value = None
        self._interpolation_method = None
        self._scale_type = None
        self.discriminator = None
        if parameter_guid is not None:
            self.parameter_guid = parameter_guid
        if default_value is not None:
            self.default_value = default_value
        if interpolation_method is not None:
            self.interpolation_method = interpolation_method
        if scale_type is not None:
            self.scale_type = scale_type

    @property
    def parameter_guid(self) -> "str":
        """Gets the parameter_guid of this GrantaServerApiSchemaAttributesUpdateFloatFunctionalAttributeParameter.

        Returns
        -------
        str
            The parameter_guid of this GrantaServerApiSchemaAttributesUpdateFloatFunctionalAttributeParameter.
        """
        return self._parameter_guid

    @parameter_guid.setter
    def parameter_guid(self, parameter_guid: "str") -> None:
        """Sets the parameter_guid of this GrantaServerApiSchemaAttributesUpdateFloatFunctionalAttributeParameter.

        Parameters
        ----------
        parameter_guid: str
            The parameter_guid of this GrantaServerApiSchemaAttributesUpdateFloatFunctionalAttributeParameter.
        """
        self._parameter_guid = parameter_guid

    @property
    def default_value(self) -> "float":
        """Gets the default_value of this GrantaServerApiSchemaAttributesUpdateFloatFunctionalAttributeParameter.

        Returns
        -------
        float
            The default_value of this GrantaServerApiSchemaAttributesUpdateFloatFunctionalAttributeParameter.
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value: "float") -> None:
        """Sets the default_value of this GrantaServerApiSchemaAttributesUpdateFloatFunctionalAttributeParameter.

        Parameters
        ----------
        default_value: float
            The default_value of this GrantaServerApiSchemaAttributesUpdateFloatFunctionalAttributeParameter.
        """
        self._default_value = default_value

    @property
    def interpolation_method(self) -> "GrantaServerApiSchemaAttributesAttributeInterpolationMethod":
        """Gets the interpolation_method of this GrantaServerApiSchemaAttributesUpdateFloatFunctionalAttributeParameter.

        Returns
        -------
        GrantaServerApiSchemaAttributesAttributeInterpolationMethod
            The interpolation_method of this GrantaServerApiSchemaAttributesUpdateFloatFunctionalAttributeParameter.
        """
        return self._interpolation_method

    @interpolation_method.setter
    def interpolation_method(self, interpolation_method: "GrantaServerApiSchemaAttributesAttributeInterpolationMethod") -> None:
        """Sets the interpolation_method of this GrantaServerApiSchemaAttributesUpdateFloatFunctionalAttributeParameter.

        Parameters
        ----------
        interpolation_method: GrantaServerApiSchemaAttributesAttributeInterpolationMethod
            The interpolation_method of this GrantaServerApiSchemaAttributesUpdateFloatFunctionalAttributeParameter.
        """
        self._interpolation_method = interpolation_method

    @property
    def scale_type(self) -> "GrantaServerApiSchemaAttributesAttributeScaleType":
        """Gets the scale_type of this GrantaServerApiSchemaAttributesUpdateFloatFunctionalAttributeParameter.

        Returns
        -------
        GrantaServerApiSchemaAttributesAttributeScaleType
            The scale_type of this GrantaServerApiSchemaAttributesUpdateFloatFunctionalAttributeParameter.
        """
        return self._scale_type

    @scale_type.setter
    def scale_type(self, scale_type: "GrantaServerApiSchemaAttributesAttributeScaleType") -> None:
        """Sets the scale_type of this GrantaServerApiSchemaAttributesUpdateFloatFunctionalAttributeParameter.

        Parameters
        ----------
        scale_type: GrantaServerApiSchemaAttributesAttributeScaleType
            The scale_type of this GrantaServerApiSchemaAttributesUpdateFloatFunctionalAttributeParameter.
        """
        self._scale_type = scale_type

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
        if issubclass(GrantaServerApiSchemaAttributesUpdateFloatFunctionalAttributeParameter, dict):
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
        if not isinstance(other, GrantaServerApiSchemaAttributesUpdateFloatFunctionalAttributeParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
