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

class GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier(ModelBase):
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
        "source": "GrantaServerApiObjectIdentifier",
        "target_identity": "int",
        "parameter_mappings": "list[GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier]",
        "link_source_type": "GrantaServerApiIntegrationSchemaLinkSourceType",
    }

    attribute_map = {
        "source": "source",
        "target_identity": "targetIdentity",
        "parameter_mappings": "parameterMappings",
        "link_source_type": "linkSourceType",
    }

    subtype_mapping = {
        "source": "GrantaServerApiObjectIdentifier",
        "parameterMappings": "GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier",
        "linkSourceType": "GrantaServerApiIntegrationSchemaLinkSourceType",
    }

    def __init__(self, *, link_source_type: "Optional[GrantaServerApiIntegrationSchemaLinkSourceType]" = None, parameter_mappings: "Optional[List[GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier]]" = None, source: "Optional[GrantaServerApiObjectIdentifier]" = None, target_identity: "Optional[int]" = None) -> None:
        """GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier - a model defined in Swagger

        Parameters
        ----------
            link_source_type: GrantaServerApiIntegrationSchemaLinkSourceType, optional
            parameter_mappings: List[GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier], optional
            source: GrantaServerApiObjectIdentifier, optional
            target_identity: int, optional
        """
        self._source = None
        self._target_identity = None
        self._parameter_mappings = None
        self._link_source_type = None
        self.discriminator = None
        if source is not None:
            self.source = source
        if target_identity is not None:
            self.target_identity = target_identity
        if parameter_mappings is not None:
            self.parameter_mappings = parameter_mappings
        if link_source_type is not None:
            self.link_source_type = link_source_type

    @property
    def source(self) -> "GrantaServerApiObjectIdentifier":
        """Gets the source of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        GrantaServerApiObjectIdentifier
            The source of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        """
        return self._source

    @source.setter
    def source(self, source: "GrantaServerApiObjectIdentifier") -> None:
        """Sets the source of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        source: GrantaServerApiObjectIdentifier
            The source of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        """
        self._source = source

    @property
    def target_identity(self) -> "int":
        """Gets the target_identity of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        The identity of the integration schema attribute

        Returns
        -------
        int
            The target_identity of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        """
        return self._target_identity

    @target_identity.setter
    def target_identity(self, target_identity: "int") -> None:
        """Sets the target_identity of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        The identity of the integration schema attribute

        Parameters
        ----------
        target_identity: int
            The target_identity of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        """
        self._target_identity = target_identity

    @property
    def parameter_mappings(self) -> "list[GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier]":
        """Gets the parameter_mappings of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        Any mapped parameters (float functional attributes only). The target parameters must be defined on the target integration attribute.  Not every parameters from the source database needs to be mapped for each attribute.

        Returns
        -------
        list[GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier]
            The parameter_mappings of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        """
        return self._parameter_mappings

    @parameter_mappings.setter
    def parameter_mappings(self, parameter_mappings: "list[GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier]") -> None:
        """Sets the parameter_mappings of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        Any mapped parameters (float functional attributes only). The target parameters must be defined on the target integration attribute.  Not every parameters from the source database needs to be mapped for each attribute.

        Parameters
        ----------
        parameter_mappings: list[GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier]
            The parameter_mappings of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        """
        self._parameter_mappings = parameter_mappings

    @property
    def link_source_type(self) -> "GrantaServerApiIntegrationSchemaLinkSourceType":
        """Gets the link_source_type of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.

        Returns
        -------
        GrantaServerApiIntegrationSchemaLinkSourceType
            The link_source_type of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        """
        return self._link_source_type

    @link_source_type.setter
    def link_source_type(self, link_source_type: "GrantaServerApiIntegrationSchemaLinkSourceType") -> None:
        """Sets the link_source_type of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.

        Parameters
        ----------
        link_source_type: GrantaServerApiIntegrationSchemaLinkSourceType
            The link_source_type of this GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier.
        """
        self._link_source_type = link_source_type

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
        if issubclass(GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier, dict):
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
        if not isinstance(other, GrantaServerApiIntegrationSchemaMappingOfGrantaServerApiObjectIdentifier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
