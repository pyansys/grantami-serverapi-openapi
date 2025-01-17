"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type
from ansys.grantami.serverapi_openapi.v252.models.gsa_criterion import GsaCriterion  # noqa: F401
from ansys.grantami.serverapi_openapi.v252.models.gsa_criterion_type import GsaCriterionType


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaRecordSubsetCriterion(GsaCriterion):
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
        "type": "GsaCriterionType",
        "subset_guid": "str",
        "subset_identity": "int",
    }

    attribute_map: dict[str, str] = {
        "type": "type",
        "subset_guid": "subsetGuid",
        "subset_identity": "subsetIdentity",
    }

    subtype_mapping: dict[str, str] = {
    }

    discriminator: Optional[str] = None

    def __init__(self, *, type: "GsaCriterionType" = GsaCriterionType.SUBSET, subset_guid: "Union[str, None, Unset_Type]" = Unset, subset_identity: "Union[int, None, Unset_Type]" = Unset,) -> None:
        """GsaRecordSubsetCriterion - a model defined in Swagger

        Parameters
        ----------
        type: GsaCriterionType
        subset_guid: str, optional
        subset_identity: int, optional
        """
        super().__init__(type=type)
        self._subset_identity: Union[int, None, Unset_Type] = Unset
        self._subset_guid: Union[str, None, Unset_Type] = Unset

        if subset_identity is not Unset:
            self.subset_identity = subset_identity
        if subset_guid is not Unset:
            self.subset_guid = subset_guid

    @property
    def subset_identity(self) -> "Union[int, None, Unset_Type]":
        """Gets the subset_identity of this GsaRecordSubsetCriterion.

        Returns
        -------
        Union[int, None, Unset_Type]
            The subset_identity of this GsaRecordSubsetCriterion.
        """
        return self._subset_identity

    @subset_identity.setter
    def subset_identity(self, subset_identity: "Union[int, None, Unset_Type]") -> None:
        """Sets the subset_identity of this GsaRecordSubsetCriterion.

        Parameters
        ----------
        subset_identity: Union[int, None, Unset_Type]
            The subset_identity of this GsaRecordSubsetCriterion.
        """
        self._subset_identity = subset_identity

    @property
    def subset_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the subset_guid of this GsaRecordSubsetCriterion.

        Returns
        -------
        Union[str, None, Unset_Type]
            The subset_guid of this GsaRecordSubsetCriterion.
        """
        return self._subset_guid

    @subset_guid.setter
    def subset_guid(self, subset_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the subset_guid of this GsaRecordSubsetCriterion.

        Parameters
        ----------
        subset_guid: Union[str, None, Unset_Type]
            The subset_guid of this GsaRecordSubsetCriterion.
        """
        self._subset_guid = subset_guid

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
        if not isinstance(other, GsaRecordSubsetCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

