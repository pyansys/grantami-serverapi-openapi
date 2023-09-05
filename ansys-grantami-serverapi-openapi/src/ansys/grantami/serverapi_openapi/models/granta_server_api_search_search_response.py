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

class GrantaServerApiSearchSearchResponse(ModelBase):
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
        "search_identifier": "str",
        "total_result_count": "int",
        "results": "list[GrantaServerApiSearchSearchResult]",
    }

    attribute_map = {
        "search_identifier": "searchIdentifier",
        "total_result_count": "totalResultCount",
        "results": "results",
    }

    subtype_mapping = {
        "results": "GrantaServerApiSearchSearchResult",
    }

    def __init__(self, *, results: "Optional[List[GrantaServerApiSearchSearchResult]]" = None, search_identifier: "Optional[str]" = None, total_result_count: "Optional[int]" = None) -> None:
        """GrantaServerApiSearchSearchResponse - a model defined in Swagger

        Parameters
        ----------
            results: List[GrantaServerApiSearchSearchResult], optional
            search_identifier: str, optional
            total_result_count: int, optional
        """
        self._search_identifier = None
        self._total_result_count = None
        self._results = None
        self.discriminator = None
        if search_identifier is not None:
            self.search_identifier = search_identifier
        if total_result_count is not None:
            self.total_result_count = total_result_count
        if results is not None:
            self.results = results

    @property
    def search_identifier(self) -> "str":
        """Gets the search_identifier of this GrantaServerApiSearchSearchResponse.
        If the search request had paging options specified, this will return an identifier that can be used to get the rest of the results

        Returns
        -------
        str
            The search_identifier of this GrantaServerApiSearchSearchResponse.
        """
        return self._search_identifier

    @search_identifier.setter
    def search_identifier(self, search_identifier: "str") -> None:
        """Sets the search_identifier of this GrantaServerApiSearchSearchResponse.
        If the search request had paging options specified, this will return an identifier that can be used to get the rest of the results

        Parameters
        ----------
        search_identifier: str
            The search_identifier of this GrantaServerApiSearchSearchResponse.
        """
        self._search_identifier = search_identifier

    @property
    def total_result_count(self) -> "int":
        """Gets the total_result_count of this GrantaServerApiSearchSearchResponse.

        Returns
        -------
        int
            The total_result_count of this GrantaServerApiSearchSearchResponse.
        """
        return self._total_result_count

    @total_result_count.setter
    def total_result_count(self, total_result_count: "int") -> None:
        """Sets the total_result_count of this GrantaServerApiSearchSearchResponse.

        Parameters
        ----------
        total_result_count: int
            The total_result_count of this GrantaServerApiSearchSearchResponse.
        """
        self._total_result_count = total_result_count

    @property
    def results(self) -> "list[GrantaServerApiSearchSearchResult]":
        """Gets the results of this GrantaServerApiSearchSearchResponse.

        Returns
        -------
        list[GrantaServerApiSearchSearchResult]
            The results of this GrantaServerApiSearchSearchResponse.
        """
        return self._results

    @results.setter
    def results(self, results: "list[GrantaServerApiSearchSearchResult]") -> None:
        """Sets the results of this GrantaServerApiSearchSearchResponse.

        Parameters
        ----------
        results: list[GrantaServerApiSearchSearchResult]
            The results of this GrantaServerApiSearchSearchResponse.
        """
        self._results = results

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
        if issubclass(GrantaServerApiSearchSearchResponse, dict):
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
        if not isinstance(other, GrantaServerApiSearchSearchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
