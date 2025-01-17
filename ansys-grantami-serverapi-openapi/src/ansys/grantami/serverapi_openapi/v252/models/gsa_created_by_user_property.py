"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.v252.models.gsa_property import GsaProperty  # noqa: F401
from ansys.grantami.serverapi_openapi.v252.models.gsa_record_property import GsaRecordProperty


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaCreatedByUserProperty(GsaProperty):
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
        "property_name": "GsaRecordProperty",
        "created_by_user": "str",
    }

    attribute_map: dict[str, str] = {
        "property_name": "propertyName",
        "created_by_user": "createdByUser",
    }

    subtype_mapping: dict[str, str] = {
    }

    discriminator: Optional[str] = None

    def __init__(self, *, property_name: "GsaRecordProperty" = GsaRecordProperty.CREATEDBYUSER, created_by_user: "Union[str, None, Unset_Type]" = Unset,) -> None:
        """GsaCreatedByUserProperty - a model defined in Swagger

        Parameters
        ----------
        property_name: GsaRecordProperty
        created_by_user: str, optional
        """
        super().__init__(property_name=property_name)
        self._created_by_user: Union[str, None, Unset_Type] = Unset

        if created_by_user is not Unset:
            self.created_by_user = created_by_user

    @property
    def created_by_user(self) -> "Union[str, None, Unset_Type]":
        """Gets the created_by_user of this GsaCreatedByUserProperty.

        Returns
        -------
        Union[str, None, Unset_Type]
            The created_by_user of this GsaCreatedByUserProperty.
        """
        return self._created_by_user

    @created_by_user.setter
    def created_by_user(self, created_by_user: "Union[str, None, Unset_Type]") -> None:
        """Sets the created_by_user of this GsaCreatedByUserProperty.

        Parameters
        ----------
        created_by_user: Union[str, None, Unset_Type]
            The created_by_user of this GsaCreatedByUserProperty.
        """
        self._created_by_user = created_by_user

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
        if not isinstance(other, GsaCreatedByUserProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

