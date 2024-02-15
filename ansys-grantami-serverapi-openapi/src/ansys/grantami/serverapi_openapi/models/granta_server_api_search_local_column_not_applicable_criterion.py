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
    Dict,
    List,
    BinaryIO,
    Optional,
    Union,
)  # noqa: F401

from . import ModelBase
from ansys.grantami.serverapi_openapi.models.granta_server_api_search_local_column_criterion import (
    GrantaServerApiSearchLocalColumnCriterion,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSearchLocalColumnNotApplicableCriterion(
    GrantaServerApiSearchLocalColumnCriterion
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
    swagger_types: Dict[str, str] = {
        "guid": "str",
        "identity": "int",
        "local_column_criterion_type": "str",
        "type": "str",
    }

    attribute_map: Dict[str, str] = {
        "guid": "guid",
        "identity": "identity",
        "local_column_criterion_type": "localColumnCriterionType",
        "type": "type",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        guid: "Optional[str]" = None,
        identity: "Optional[int]" = None,
        local_column_criterion_type: "str" = "notApplicable",
        type: "str" = "localColumn",
    ) -> None:
        """GrantaServerApiSearchLocalColumnNotApplicableCriterion - a model defined in Swagger

        Parameters
        ----------
            guid: str, optional
            identity: int, optional
            local_column_criterion_type: str
            type: str
        """
        super().__init__(guid=guid, identity=identity, type=type)
        self._local_column_criterion_type: str = None  # type: ignore[assignment]

        self.local_column_criterion_type = local_column_criterion_type

    @property
    def local_column_criterion_type(self) -> "str":
        """Gets the local_column_criterion_type of this GrantaServerApiSearchLocalColumnNotApplicableCriterion.

        Returns
        -------
        str
            The local_column_criterion_type of this GrantaServerApiSearchLocalColumnNotApplicableCriterion.
        """
        return self._local_column_criterion_type

    @local_column_criterion_type.setter
    def local_column_criterion_type(self, local_column_criterion_type: "str") -> None:
        """Sets the local_column_criterion_type of this GrantaServerApiSearchLocalColumnNotApplicableCriterion.

        Parameters
        ----------
        local_column_criterion_type: str
            The local_column_criterion_type of this GrantaServerApiSearchLocalColumnNotApplicableCriterion.
        """
        if local_column_criterion_type is None:
            raise ValueError(
                "Invalid value for 'local_column_criterion_type', must not be 'None'"
            )
        self._local_column_criterion_type = local_column_criterion_type

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
        return self.to_str()  # type: ignore[no-any-return]

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(
            other, GrantaServerApiSearchLocalColumnNotApplicableCriterion
        ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
