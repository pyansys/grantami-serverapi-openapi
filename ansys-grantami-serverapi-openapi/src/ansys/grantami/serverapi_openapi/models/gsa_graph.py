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


class GsaGraph(ModelBase):
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
    discriminator_class_map: dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "graph_type": "GsaGraphType",
    }

    attribute_map: dict[str, str] = {
        "graph_type": "graphType",
    }

    subtype_mapping: dict[str, str] = {
        "graphType": "GsaGraphType",
    }

    discriminator_value_class_map = {
        "series".lower(): "#/components/schemas/GsaSeriesGraph",
        "grid".lower(): "#/components/schemas/GsaGridGraph",
    }

    discriminator: Optional[str] = "graphType"

    def __init__(self, *, graph_type: "GsaGraphType",) -> None:
        """GsaGraph - a model defined in Swagger

        Parameters
        ----------
        graph_type: GsaGraphType
        """
        self._graph_type: GsaGraphType

        self.graph_type = graph_type

    @property
    def graph_type(self) -> "GsaGraphType":
        """Gets the graph_type of this GsaGraph.

        Returns
        -------
        GsaGraphType
            The graph_type of this GsaGraph.
        """
        return self._graph_type

    @graph_type.setter
    def graph_type(self, graph_type: "GsaGraphType") -> None:
        """Sets the graph_type of this GsaGraph.

        Parameters
        ----------
        graph_type: GsaGraphType
            The graph_type of this GsaGraph.
        """
        # Field is not nullable
        if graph_type is None:
            raise ValueError("Invalid value for 'graph_type', must not be 'None'")
        # Field is required
        if graph_type is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'graph_type', must not be 'Unset'")
        self._graph_type = graph_type

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[cls._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen,
        # so we have to extract it from the JSON reference
        return cls.discriminator_value_class_map[discriminator_value].rsplit("/", 1)[-1]

    @classmethod
    def _get_discriminator_field_name(cls) -> str:
        assert cls.discriminator
        name_tokens = cls.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GsaGraph):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

