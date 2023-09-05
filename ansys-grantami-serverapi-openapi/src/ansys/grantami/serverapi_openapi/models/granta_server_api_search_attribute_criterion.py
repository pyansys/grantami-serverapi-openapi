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

from ansys.grantami.serverapi_openapi.models.granta_server_api_search_criterion import GrantaServerApiSearchCriterion  # noqa: F401

if TYPE_CHECKING:
    from . import *

class GrantaServerApiSearchAttributeCriterion(GrantaServerApiSearchCriterion):
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
    """
    swagger_types = {
        "identity": "int",
        "guid": "str",
        "is_meta_attribute": "bool",
        "type": "str",
    }

    attribute_map = {
        "identity": "identity",
        "guid": "guid",
        "is_meta_attribute": "isMetaAttribute",
        "type": "type",
    }

    subtype_mapping = {
    }

    discriminator_value_class_map = {
        "matches".lower(): "#/components/schemas/GrantaServerApiSearchAttributeMatchesCriterion",
        "exists".lower(): "#/components/schemas/GrantaServerApiSearchAttributeExistsCriterion",
        "notApplicable".lower(): "#/components/schemas/GrantaServerApiSearchAttributeNotApplicableCriterion",
    }

    def __init__(self, *, guid: "Optional[str]" = None, identity: "Optional[int]" = None, is_meta_attribute: "Optional[bool]" = None, type: "str" = 'attribute') -> None:
        """GrantaServerApiSearchAttributeCriterion - a model defined in Swagger

        Parameters
        ----------
            guid: str, optional
            identity: int, optional
            is_meta_attribute: bool, optional
            type: str
        """
        super().__init__()
        self._identity = None
        self._guid = None
        self._is_meta_attribute = None
        self._type = None
        self.discriminator = "attribute_criterion_type"
        if identity is not None:
            self.identity = identity
        if guid is not None:
            self.guid = guid
        if is_meta_attribute is not None:
            self.is_meta_attribute = is_meta_attribute
        self.type = type

    @property
    def identity(self) -> "int":
        """Gets the identity of this GrantaServerApiSearchAttributeCriterion.

        Returns
        -------
        int
            The identity of this GrantaServerApiSearchAttributeCriterion.
        """
        return self._identity

    @identity.setter
    def identity(self, identity: "int") -> None:
        """Sets the identity of this GrantaServerApiSearchAttributeCriterion.

        Parameters
        ----------
        identity: int
            The identity of this GrantaServerApiSearchAttributeCriterion.
        """
        self._identity = identity

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiSearchAttributeCriterion.

        Returns
        -------
        str
            The guid of this GrantaServerApiSearchAttributeCriterion.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiSearchAttributeCriterion.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiSearchAttributeCriterion.
        """
        self._guid = guid

    @property
    def is_meta_attribute(self) -> "bool":
        """Gets the is_meta_attribute of this GrantaServerApiSearchAttributeCriterion.

        Returns
        -------
        bool
            The is_meta_attribute of this GrantaServerApiSearchAttributeCriterion.
        """
        return self._is_meta_attribute

    @is_meta_attribute.setter
    def is_meta_attribute(self, is_meta_attribute: "bool") -> None:
        """Sets the is_meta_attribute of this GrantaServerApiSearchAttributeCriterion.

        Parameters
        ----------
        is_meta_attribute: bool
            The is_meta_attribute of this GrantaServerApiSearchAttributeCriterion.
        """
        self._is_meta_attribute = is_meta_attribute

    @property
    def type(self) -> "str":
        """Gets the type of this GrantaServerApiSearchAttributeCriterion.

        Returns
        -------
        str
            The type of this GrantaServerApiSearchAttributeCriterion.
        """
        return self._type

    @type.setter
    def type(self, type: "str") -> None:
        """Sets the type of this GrantaServerApiSearchAttributeCriterion.

        Parameters
        ----------
        type: str
            The type of this GrantaServerApiSearchAttributeCriterion.
        """
        if type is None:
            raise ValueError("Invalid value for 'type', must not be 'None'")
        self._type = type

    def get_real_child_model(self, data: ModelBase) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[self._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen, 
        # so we have to extract it from the JSON reference
        return self.discriminator_value_class_map.get(discriminator_value).rsplit("/", 1)[-1]

    def _get_discriminator_field_name(self) -> str:
        name_tokens = self.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

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
        if issubclass(GrantaServerApiSearchAttributeCriterion, dict):
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
        if not isinstance(other, GrantaServerApiSearchAttributeCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
