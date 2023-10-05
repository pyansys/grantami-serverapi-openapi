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

class GrantaServerApiSearchBoostByIdentity(ModelBase):
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
        "attribute_identity": "int",
        "boost_factor": "float",
    }

    attribute_map = {
        "attribute_identity": "attributeIdentity",
        "boost_factor": "boostFactor",
    }

    subtype_mapping = {
    }

    def __init__(self, *, attribute_identity: "Optional[int]" = None, boost_factor: "Optional[float]" = None) -> None:
        """GrantaServerApiSearchBoostByIdentity - a model defined in Swagger

        Parameters
        ----------
            attribute_identity: int, optional
            boost_factor: float, optional
        """
        self._attribute_identity = None
        self._boost_factor = None
        self.discriminator = None
        if attribute_identity is not None:
            self.attribute_identity = attribute_identity
        if boost_factor is not None:
            self.boost_factor = boost_factor

    @property
    def attribute_identity(self) -> "int":
        """Gets the attribute_identity of this GrantaServerApiSearchBoostByIdentity.

        Returns
        -------
        int
            The attribute_identity of this GrantaServerApiSearchBoostByIdentity.
        """
        return self._attribute_identity

    @attribute_identity.setter
    def attribute_identity(self, attribute_identity: "int") -> None:
        """Sets the attribute_identity of this GrantaServerApiSearchBoostByIdentity.

        Parameters
        ----------
        attribute_identity: int
            The attribute_identity of this GrantaServerApiSearchBoostByIdentity.
        """
        self._attribute_identity = attribute_identity

    @property
    def boost_factor(self) -> "float":
        """Gets the boost_factor of this GrantaServerApiSearchBoostByIdentity.

        Returns
        -------
        float
            The boost_factor of this GrantaServerApiSearchBoostByIdentity.
        """
        return self._boost_factor

    @boost_factor.setter
    def boost_factor(self, boost_factor: "float") -> None:
        """Sets the boost_factor of this GrantaServerApiSearchBoostByIdentity.

        Parameters
        ----------
        boost_factor: float
            The boost_factor of this GrantaServerApiSearchBoostByIdentity.
        """
        self._boost_factor = boost_factor

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
        if issubclass(GrantaServerApiSearchBoostByIdentity, dict):
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
        if not isinstance(other, GrantaServerApiSearchBoostByIdentity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
