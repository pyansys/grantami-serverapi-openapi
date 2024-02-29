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


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
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
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: Dict[str, str] = {
        "parameter_contents": "list[GrantaServerApiSchemaParametersParameterContent]",
        "transpose_axes": "bool",
        "use_logarithmic_scale": "bool",
        "curve_label": "str",
        "expression": "GrantaServerApiSchemaSlimEntitiesSlimExpression",
        "free_parameter": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
    }

    attribute_map: Dict[str, str] = {
        "parameter_contents": "parameterContents",
        "transpose_axes": "transposeAxes",
        "use_logarithmic_scale": "useLogarithmicScale",
        "curve_label": "curveLabel",
        "expression": "expression",
        "free_parameter": "freeParameter",
    }

    subtype_mapping: Dict[str, str] = {
        "expression": "GrantaServerApiSchemaSlimEntitiesSlimExpression",
        "freeParameter": "GrantaServerApiSchemaSlimEntitiesSlimNamedEntity",
        "parameterContents": "GrantaServerApiSchemaParametersParameterContent",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        parameter_contents: "List[GrantaServerApiSchemaParametersParameterContent]",
        transpose_axes: "bool",
        use_logarithmic_scale: "bool",
        curve_label: "Union[str, None, Unset_Type]" = Unset,
        expression: "Union[GrantaServerApiSchemaSlimEntitiesSlimExpression, Unset_Type]" = Unset,
        free_parameter: "Union[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, Unset_Type]" = Unset,
    ) -> None:
        """GrantaServerApiSchemaAttributesMathsContent - a model defined in Swagger

        Parameters
        ----------
        parameter_contents: List[GrantaServerApiSchemaParametersParameterContent]
        transpose_axes: bool
        use_logarithmic_scale: bool
        curve_label: str, optional
        expression: GrantaServerApiSchemaSlimEntitiesSlimExpression, optional
        free_parameter: GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, optional
        """
        self._curve_label: Union[str, None, Unset_Type] = Unset
        self._transpose_axes: bool
        self._use_logarithmic_scale: bool
        self._expression: Union[
            GrantaServerApiSchemaSlimEntitiesSlimExpression, Unset_Type
        ] = Unset
        self._free_parameter: Union[
            GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, Unset_Type
        ] = Unset
        self._parameter_contents: List[GrantaServerApiSchemaParametersParameterContent]

        if curve_label is not Unset:
            self.curve_label = curve_label
        self.transpose_axes = transpose_axes
        self.use_logarithmic_scale = use_logarithmic_scale
        if expression is not Unset:
            self.expression = expression
        if free_parameter is not Unset:
            self.free_parameter = free_parameter
        self.parameter_contents = parameter_contents

    @property
    def curve_label(self) -> "Union[str, None, Unset_Type]":
        """Gets the curve_label of this GrantaServerApiSchemaAttributesMathsContent.

        Returns
        -------
        Union[str, None, Unset_Type]
            The curve_label of this GrantaServerApiSchemaAttributesMathsContent.
        """
        return self._curve_label

    @curve_label.setter
    def curve_label(self, curve_label: "Union[str, None, Unset_Type]") -> None:
        """Sets the curve_label of this GrantaServerApiSchemaAttributesMathsContent.

        Parameters
        ----------
        curve_label: Union[str, None, Unset_Type]
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
        # Field is not nullable
        if transpose_axes is None:
            raise ValueError("Invalid value for 'transpose_axes', must not be 'None'")
        # Field is required
        if transpose_axes is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'transpose_axes', must not be 'Unset'")
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
        # Field is not nullable
        if use_logarithmic_scale is None:
            raise ValueError(
                "Invalid value for 'use_logarithmic_scale', must not be 'None'"
            )
        # Field is required
        if use_logarithmic_scale is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'use_logarithmic_scale', must not be 'Unset'"
            )
        self._use_logarithmic_scale = use_logarithmic_scale

    @property
    def expression(
        self,
    ) -> "Union[GrantaServerApiSchemaSlimEntitiesSlimExpression, Unset_Type]":
        """Gets the expression of this GrantaServerApiSchemaAttributesMathsContent.

        Returns
        -------
        Union[GrantaServerApiSchemaSlimEntitiesSlimExpression, Unset_Type]
            The expression of this GrantaServerApiSchemaAttributesMathsContent.
        """
        return self._expression

    @expression.setter
    def expression(
        self,
        expression: "Union[GrantaServerApiSchemaSlimEntitiesSlimExpression, Unset_Type]",
    ) -> None:
        """Sets the expression of this GrantaServerApiSchemaAttributesMathsContent.

        Parameters
        ----------
        expression: Union[GrantaServerApiSchemaSlimEntitiesSlimExpression, Unset_Type]
            The expression of this GrantaServerApiSchemaAttributesMathsContent.
        """
        # Field is not nullable
        if expression is None:
            raise ValueError("Invalid value for 'expression', must not be 'None'")
        self._expression = expression

    @property
    def free_parameter(
        self,
    ) -> "Union[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, Unset_Type]":
        """Gets the free_parameter of this GrantaServerApiSchemaAttributesMathsContent.

        Returns
        -------
        Union[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, Unset_Type]
            The free_parameter of this GrantaServerApiSchemaAttributesMathsContent.
        """
        return self._free_parameter

    @free_parameter.setter
    def free_parameter(
        self,
        free_parameter: "Union[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, Unset_Type]",
    ) -> None:
        """Sets the free_parameter of this GrantaServerApiSchemaAttributesMathsContent.

        Parameters
        ----------
        free_parameter: Union[GrantaServerApiSchemaSlimEntitiesSlimNamedEntity, Unset_Type]
            The free_parameter of this GrantaServerApiSchemaAttributesMathsContent.
        """
        # Field is not nullable
        if free_parameter is None:
            raise ValueError("Invalid value for 'free_parameter', must not be 'None'")
        self._free_parameter = free_parameter

    @property
    def parameter_contents(
        self,
    ) -> "List[GrantaServerApiSchemaParametersParameterContent]":
        """Gets the parameter_contents of this GrantaServerApiSchemaAttributesMathsContent.

        Returns
        -------
        List[GrantaServerApiSchemaParametersParameterContent]
            The parameter_contents of this GrantaServerApiSchemaAttributesMathsContent.
        """
        return self._parameter_contents

    @parameter_contents.setter
    def parameter_contents(
        self,
        parameter_contents: "List[GrantaServerApiSchemaParametersParameterContent]",
    ) -> None:
        """Sets the parameter_contents of this GrantaServerApiSchemaAttributesMathsContent.

        Parameters
        ----------
        parameter_contents: List[GrantaServerApiSchemaParametersParameterContent]
            The parameter_contents of this GrantaServerApiSchemaAttributesMathsContent.
        """
        # Field is not nullable
        if parameter_contents is None:
            raise ValueError(
                "Invalid value for 'parameter_contents', must not be 'None'"
            )
        # Field is required
        if parameter_contents is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError(
                "Invalid value for 'parameter_contents', must not be 'Unset'"
            )
        self._parameter_contents = parameter_contents

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
        if not isinstance(other, GrantaServerApiSchemaAttributesMathsContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
