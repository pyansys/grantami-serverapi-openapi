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

class GrantaServerApiSchemaAttributesMathsContent(ModelBase):
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
        "curve_label": "str",
        "expression": "GrantaServerApiSchemaSlimEntitiesSlimExpression",
        "free_parameter": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "parameter_contents": "list[GrantaServerApiSchemaParametersParameterContent]",
        "transpose_axes": "bool",
        "use_logarithmic_scale": "bool",
    }

    attribute_map = {
        "curve_label": "curveLabel",
        "expression": "expression",
        "free_parameter": "freeParameter",
        "parameter_contents": "parameterContents",
        "transpose_axes": "transposeAxes",
        "use_logarithmic_scale": "useLogarithmicScale",
    }

    subtype_mapping = {
        "expression": "GrantaServerApiSchemaSlimEntitiesSlimExpression",
        "freeParameter": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "parameterContents": "GrantaServerApiSchemaParametersParameterContent",
    }

    def __init__(self, *, curve_label: "Optional[str]" = None, expression: "Optional[GrantaServerApiSchemaSlimEntitiesSlimExpression]" = None, free_parameter: "Optional[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity]" = None, parameter_contents: "Optional[List[GrantaServerApiSchemaParametersParameterContent]]" = None, transpose_axes: "Optional[bool]" = None, use_logarithmic_scale: "Optional[bool]" = None,) -> None:
        """GrantaServerApiSchemaAttributesMathsContent - a model defined in Swagger

        Parameters
        ----------
            curve_label: str, optional
            expression: GrantaServerApiSchemaSlimEntitiesSlimExpression, optional
            free_parameter: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, optional
            parameter_contents: List[GrantaServerApiSchemaParametersParameterContent], optional
            transpose_axes: bool, optional
            use_logarithmic_scale: bool, optional
        """
        self._curve_label = None
        self._transpose_axes = None
        self._use_logarithmic_scale = None
        self._expression = None
        self._free_parameter = None
        self._parameter_contents = None
        self.discriminator = None
        if curve_label is not None:
            self.curve_label = curve_label
        if transpose_axes is not None:
            self.transpose_axes = transpose_axes
        if use_logarithmic_scale is not None:
            self.use_logarithmic_scale = use_logarithmic_scale
        if expression is not None:
            self.expression = expression
        if free_parameter is not None:
            self.free_parameter = free_parameter
        if parameter_contents is not None:
            self.parameter_contents = parameter_contents

    @property
    def curve_label(self) -> "str":
        """Gets the curve_label of this GrantaServerApiSchemaAttributesMathsContent.

        Returns
        -------
        str
            The curve_label of this GrantaServerApiSchemaAttributesMathsContent.
        """
        return self._curve_label

    @curve_label.setter
    def curve_label(self, curve_label: "str") -> None:
        """Sets the curve_label of this GrantaServerApiSchemaAttributesMathsContent.

        Parameters
        ----------
        curve_label: str
            The curve_label of this GrantaServerApiSchemaAttributesMathsContent.
        """
        self._curve_label = curve_label

    @property
    def transpose_axes(self) -> "bool":
        """Gets the transpose_axes of this GrantaServerApiSchemaAttributesMathsContent.

        Returns
        -------
        bool
            The transpose_axes of this GrantaServerApiSchemaAttributesMathsContent.
        """
        return self._transpose_axes

    @transpose_axes.setter
    def transpose_axes(self, transpose_axes: "bool") -> None:
        """Sets the transpose_axes of this GrantaServerApiSchemaAttributesMathsContent.

        Parameters
        ----------
        transpose_axes: bool
            The transpose_axes of this GrantaServerApiSchemaAttributesMathsContent.
        """
        self._transpose_axes = transpose_axes

    @property
    def use_logarithmic_scale(self) -> "bool":
        """Gets the use_logarithmic_scale of this GrantaServerApiSchemaAttributesMathsContent.

        Returns
        -------
        bool
            The use_logarithmic_scale of this GrantaServerApiSchemaAttributesMathsContent.
        """
        return self._use_logarithmic_scale

    @use_logarithmic_scale.setter
    def use_logarithmic_scale(self, use_logarithmic_scale: "bool") -> None:
        """Sets the use_logarithmic_scale of this GrantaServerApiSchemaAttributesMathsContent.

        Parameters
        ----------
        use_logarithmic_scale: bool
            The use_logarithmic_scale of this GrantaServerApiSchemaAttributesMathsContent.
        """
        self._use_logarithmic_scale = use_logarithmic_scale

    @property
    def expression(self) -> "GrantaServerApiSchemaSlimEntitiesSlimExpression":
        """Gets the expression of this GrantaServerApiSchemaAttributesMathsContent.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimExpression
            The expression of this GrantaServerApiSchemaAttributesMathsContent.
        """
        return self._expression

    @expression.setter
    def expression(self, expression: "GrantaServerApiSchemaSlimEntitiesSlimExpression") -> None:
        """Sets the expression of this GrantaServerApiSchemaAttributesMathsContent.

        Parameters
        ----------
        expression: GrantaServerApiSchemaSlimEntitiesSlimExpression
            The expression of this GrantaServerApiSchemaAttributesMathsContent.
        """
        self._expression = expression

    @property
    def free_parameter(self) -> "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity":
        """Gets the free_parameter of this GrantaServerApiSchemaAttributesMathsContent.

        Returns
        -------
        GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
            The free_parameter of this GrantaServerApiSchemaAttributesMathsContent.
        """
        return self._free_parameter

    @free_parameter.setter
    def free_parameter(self, free_parameter: "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity") -> None:
        """Sets the free_parameter of this GrantaServerApiSchemaAttributesMathsContent.

        Parameters
        ----------
        free_parameter: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity
            The free_parameter of this GrantaServerApiSchemaAttributesMathsContent.
        """
        self._free_parameter = free_parameter

    @property
    def parameter_contents(self) -> "list[GrantaServerApiSchemaParametersParameterContent]":
        """Gets the parameter_contents of this GrantaServerApiSchemaAttributesMathsContent.

        Returns
        -------
        list[GrantaServerApiSchemaParametersParameterContent]
            The parameter_contents of this GrantaServerApiSchemaAttributesMathsContent.
        """
        return self._parameter_contents

    @parameter_contents.setter
    def parameter_contents(self, parameter_contents: "list[GrantaServerApiSchemaParametersParameterContent]") -> None:
        """Sets the parameter_contents of this GrantaServerApiSchemaAttributesMathsContent.

        Parameters
        ----------
        parameter_contents: list[GrantaServerApiSchemaParametersParameterContent]
            The parameter_contents of this GrantaServerApiSchemaAttributesMathsContent.
        """
        self._parameter_contents = parameter_contents

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
        if issubclass(GrantaServerApiSchemaAttributesMathsContent, dict):
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
        if not isinstance(other, GrantaServerApiSchemaAttributesMathsContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
