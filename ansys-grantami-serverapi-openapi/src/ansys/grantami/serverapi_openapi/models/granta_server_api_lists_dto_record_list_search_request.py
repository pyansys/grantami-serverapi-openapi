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


class GrantaServerApiListsDtoRecordListSearchRequest(ModelBase):
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
        "paging_options": "GrantaServerApiListsDtoPagingOptions",
        "response_options": "GrantaServerApiListsDtoResponseOptions",
        "search_criterion": "GrantaServerApiListsDtoListCriterion",
    }

    attribute_map = {
        "paging_options": "pagingOptions",
        "response_options": "responseOptions",
        "search_criterion": "searchCriterion",
    }

    subtype_mapping = {
        "searchCriterion": "GrantaServerApiListsDtoListCriterion",
        "pagingOptions": "GrantaServerApiListsDtoPagingOptions",
        "responseOptions": "GrantaServerApiListsDtoResponseOptions",
    }

    discriminator = None

    def __init__(
        self,
        *,
        paging_options: "Optional[GrantaServerApiListsDtoPagingOptions]" = None,
        response_options: "Optional[GrantaServerApiListsDtoResponseOptions]" = None,
        search_criterion: "Optional[GrantaServerApiListsDtoListCriterion]" = None,
    ) -> None:
        """GrantaServerApiListsDtoRecordListSearchRequest - a model defined in Swagger

        Parameters
        ----------
            paging_options: GrantaServerApiListsDtoPagingOptions, optional
            response_options: GrantaServerApiListsDtoResponseOptions, optional
            search_criterion: GrantaServerApiListsDtoListCriterion, optional
        """
        self._search_criterion = None
        self._paging_options = None
        self._response_options = None

        if search_criterion is not None:
            self.search_criterion = search_criterion
        if paging_options is not None:
            self.paging_options = paging_options
        if response_options is not None:
            self.response_options = response_options

    @property
    def search_criterion(self) -> "GrantaServerApiListsDtoListCriterion":
        """Gets the search_criterion of this GrantaServerApiListsDtoRecordListSearchRequest.

        Returns
        -------
        GrantaServerApiListsDtoListCriterion
            The search_criterion of this GrantaServerApiListsDtoRecordListSearchRequest.
        """
        return self._search_criterion

    @search_criterion.setter
    def search_criterion(
        self, search_criterion: "GrantaServerApiListsDtoListCriterion"
    ) -> None:
        """Sets the search_criterion of this GrantaServerApiListsDtoRecordListSearchRequest.

        Parameters
        ----------
        search_criterion: GrantaServerApiListsDtoListCriterion
            The search_criterion of this GrantaServerApiListsDtoRecordListSearchRequest.
        """
        self._search_criterion = search_criterion

    @property
    def paging_options(self) -> "GrantaServerApiListsDtoPagingOptions":
        """Gets the paging_options of this GrantaServerApiListsDtoRecordListSearchRequest.

        Returns
        -------
        GrantaServerApiListsDtoPagingOptions
            The paging_options of this GrantaServerApiListsDtoRecordListSearchRequest.
        """
        return self._paging_options

    @paging_options.setter
    def paging_options(
        self, paging_options: "GrantaServerApiListsDtoPagingOptions"
    ) -> None:
        """Sets the paging_options of this GrantaServerApiListsDtoRecordListSearchRequest.

        Parameters
        ----------
        paging_options: GrantaServerApiListsDtoPagingOptions
            The paging_options of this GrantaServerApiListsDtoRecordListSearchRequest.
        """
        self._paging_options = paging_options

    @property
    def response_options(self) -> "GrantaServerApiListsDtoResponseOptions":
        """Gets the response_options of this GrantaServerApiListsDtoRecordListSearchRequest.

        Returns
        -------
        GrantaServerApiListsDtoResponseOptions
            The response_options of this GrantaServerApiListsDtoRecordListSearchRequest.
        """
        return self._response_options

    @response_options.setter
    def response_options(
        self, response_options: "GrantaServerApiListsDtoResponseOptions"
    ) -> None:
        """Sets the response_options of this GrantaServerApiListsDtoRecordListSearchRequest.

        Parameters
        ----------
        response_options: GrantaServerApiListsDtoResponseOptions
            The response_options of this GrantaServerApiListsDtoRecordListSearchRequest.
        """
        self._response_options = response_options

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
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(GrantaServerApiListsDtoRecordListSearchRequest, dict):
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
        if not isinstance(other, GrantaServerApiListsDtoRecordListSearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
