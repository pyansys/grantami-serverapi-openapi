"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.v252.models.gsa_usage_data_modification_error_detail import GsaUsageDataModificationErrorDetail  # noqa: F401
from ansys.grantami.serverapi_openapi.v252.models.gsa_referenced_by_type import GsaReferencedByType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaDynamicLinkGroupUsageDataModificationErrorDetail(GsaUsageDataModificationErrorDetail):
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
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "message": "str",
        "reason": "str",
        "referenced_by_type": "GsaReferencedByType",
        "referenced_by": "list[GsaSlimNamedEntity]",
    }

    attribute_map: dict[str, str] = {
        "message": "message",
        "reason": "reason",
        "referenced_by_type": "referencedByType",
        "referenced_by": "referencedBy",
    }

    subtype_mapping: dict[str, str] = {
        "referencedBy": "GsaSlimNamedEntity",
    }

    discriminator: Optional[str] = None

    def __init__(self, *, message: "str", reason: "str" = "usage", referenced_by_type: "GsaReferencedByType" = GsaReferencedByType.DYNAMICLINKGROUP, referenced_by: "Union[list[GsaSlimNamedEntity], None, Unset_Type]" = Unset,) -> None:
        """GsaDynamicLinkGroupUsageDataModificationErrorDetail - a model defined in Swagger

        Parameters
        ----------
        message: str
        reason: str
        referenced_by_type: GsaReferencedByType
        referenced_by: list[GsaSlimNamedEntity], optional
        """
        super().__init__(message=message, reason=reason, referenced_by_type=referenced_by_type)
        self._referenced_by: Union[list[GsaSlimNamedEntity], None, Unset_Type] = Unset

        if referenced_by is not Unset:
            self.referenced_by = referenced_by

    @property
    def referenced_by(self) -> "Union[list[GsaSlimNamedEntity], None, Unset_Type]":
        """Gets the referenced_by of this GsaDynamicLinkGroupUsageDataModificationErrorDetail.

        Returns
        -------
        Union[list[GsaSlimNamedEntity], None, Unset_Type]
            The referenced_by of this GsaDynamicLinkGroupUsageDataModificationErrorDetail.
        """
        return self._referenced_by

    @referenced_by.setter
    def referenced_by(self, referenced_by: "Union[list[GsaSlimNamedEntity], None, Unset_Type]") -> None:
        """Sets the referenced_by of this GsaDynamicLinkGroupUsageDataModificationErrorDetail.

        Parameters
        ----------
        referenced_by: Union[list[GsaSlimNamedEntity], None, Unset_Type]
            The referenced_by of this GsaDynamicLinkGroupUsageDataModificationErrorDetail.
        """
        self._referenced_by = referenced_by

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
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
        if not isinstance(other, GsaDynamicLinkGroupUsageDataModificationErrorDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

