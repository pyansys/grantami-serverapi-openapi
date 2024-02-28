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
from ansys.grantami.serverapi_openapi.models.granta_server_api_search_criterion import (
    GrantaServerApiSearchCriterion,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSearchLocalColumnCriterion(GrantaServerApiSearchCriterion):
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
    discriminator_class_map: Dict[str, str]
        They key is discriminator value and the value is associated subtype.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: Dict[str, str] = {
        "guid": "str",
        "identity": "int",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "guid": "guid",
        "identity": "identity",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator_value_class_map = {
        "matches".lower(): "#/components/schemas/GrantaServerApiSearchLocalColumnMatchesCriterion",
        "exists".lower(): "#/components/schemas/GrantaServerApiSearchLocalColumnExistsCriterion",
        "notApplicable".lower(): "#/components/schemas/GrantaServerApiSearchLocalColumnNotApplicableCriterion",
    }

    discriminator: Optional[str] = "local_column_criterion_type"

    def __init__(
        self,
        *,
        guid: "Union[str, None, Unset_Type]" = Unset,
        identity: "Union[int, None, Unset_Type]" = Unset,
        type: "str" = "localColumn",
    ) -> None:
        """GrantaServerApiSearchLocalColumnCriterion - a model defined in Swagger

        Parameters
        ----------
        guid: str, optional
        identity: int, optional
        type: str
        """
        super().__init__()
        self._identity: Union[int, None, Unset_Type] = Unset
        self._guid: Union[str, None, Unset_Type] = Unset
        self._type: str

        if identity is not Unset:
            self.identity = identity
        if guid is not Unset:
            self.guid = guid
        self.type = type

    @property
    def identity(self) -> "Union[int, None, Unset_Type]":
        """Gets the identity of this GrantaServerApiSearchLocalColumnCriterion.

        Returns
        -------
        Union[int, None, Unset_Type]
            The identity of this GrantaServerApiSearchLocalColumnCriterion.
        """
        return self._identity

    @identity.setter
    def identity(self, identity: "Union[int, None, Unset_Type]") -> None:
        """Sets the identity of this GrantaServerApiSearchLocalColumnCriterion.

        Parameters
        ----------
        identity: Union[int, None, Unset_Type]
            The identity of this GrantaServerApiSearchLocalColumnCriterion.
        """
        self._identity = identity

    @property
    def guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the guid of this GrantaServerApiSearchLocalColumnCriterion.

        Returns
        -------
        Union[str, None, Unset_Type]
            The guid of this GrantaServerApiSearchLocalColumnCriterion.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the guid of this GrantaServerApiSearchLocalColumnCriterion.

        Parameters
        ----------
        guid: Union[str, None, Unset_Type]
            The guid of this GrantaServerApiSearchLocalColumnCriterion.
        """
        self._guid = guid

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchLocalColumnCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchLocalColumnCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchLocalColumnCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchLocalColumnCriterion.
        """
        # Field is not nullable
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        # Field is required
        if type is Unset:  # type: ignore[comparison-overlap]
            raise ValueError("Invalid value for 'type', must not be 'Unset'")
        self._type = type

    @classmethod
    def get_real_child_model(cls, data: Dict[str, str]) -> str:
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
        if not isinstance(other, GrantaServerApiSearchLocalColumnCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
