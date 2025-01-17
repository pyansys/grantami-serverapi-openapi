"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase


if TYPE_CHECKING:
    from . import *


class GrantaServerApiSchemaLayoutsReorderSectionsInfo(ModelBase):
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
        "layout_sections": "list[GrantaServerApiSchemaSlimEntitiesSlimEntity]",
    }

    attribute_map = {
        "layout_sections": "layoutSections",
    }

    subtype_mapping = {
        "layoutSections": "GrantaServerApiSchemaSlimEntitiesSlimEntity",
    }

    discriminator = None

    def __init__(
        self,
        *,
        layout_sections: "List[GrantaServerApiSchemaSlimEntitiesSlimEntity]",
    ) -> None:
        """GrantaServerApiSchemaLayoutsReorderSectionsInfo - a model defined in Swagger

        Parameters
        ----------
            layout_sections: List[GrantaServerApiSchemaSlimEntitiesSlimEntity]
        """
        self._layout_sections = None

        self.layout_sections = layout_sections

    @property
    def layout_sections(self) -> "list[GrantaServerApiSchemaSlimEntitiesSlimEntity]":
        """Gets the layout_sections of this GrantaServerApiSchemaLayoutsReorderSectionsInfo.

        Returns
        -------
        list[GrantaServerApiSchemaSlimEntitiesSlimEntity]
            The layout_sections of this GrantaServerApiSchemaLayoutsReorderSectionsInfo.
        """
        return self._layout_sections

    @layout_sections.setter
    def layout_sections(
        self, layout_sections: "list[GrantaServerApiSchemaSlimEntitiesSlimEntity]"
    ) -> None:
        """Sets the layout_sections of this GrantaServerApiSchemaLayoutsReorderSectionsInfo.

        Parameters
        ----------
        layout_sections: list[GrantaServerApiSchemaSlimEntitiesSlimEntity]
            The layout_sections of this GrantaServerApiSchemaLayoutsReorderSectionsInfo.
        """
        if layout_sections is None:
            raise ValueError("Invalid value for 'layout_sections', must not be 'None'")
        self._layout_sections = layout_sections

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

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiSchemaLayoutsReorderSectionsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
