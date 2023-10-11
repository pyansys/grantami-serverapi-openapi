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

from ansys.grantami.serverapi_openapi.models.granta_server_api_aggregations_attribute_value_aggregation import GrantaServerApiAggregationsAttributeValueAggregation  # noqa: F401

if TYPE_CHECKING:
    from . import *

class GrantaServerApiAggregationsPointAttributeHistogramAggregation(GrantaServerApiAggregationsAttributeValueAggregation):
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
        "attribute_aggregation_type": "str",
        "attribute_guid": "str",
        "attribute_identity": "int",
        "count": "int",
        "datum_type": "str",
        "histogram": "GrantaServerApiAggregationsHistogram",
        "type": "str",
    }

    attribute_map = {
        "attribute_aggregation_type": "attributeAggregationType",
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "count": "count",
        "datum_type": "datumType",
        "histogram": "histogram",
        "type": "type",
    }

    subtype_mapping = {
        "histogram": "GrantaServerApiAggregationsHistogram",
    }

    def __init__(self, *, attribute_aggregation_type: "str" = 'value', attribute_guid: "Optional[str]" = None, attribute_identity: "Optional[int]" = None, count: "Optional[int]" = None, datum_type: "str" = 'pointHistogram', histogram: "Optional[GrantaServerApiAggregationsHistogram]" = None, type: "str" = 'attribute',) -> None:
        """GrantaServerApiAggregationsPointAttributeHistogramAggregation - a model defined in Swagger

        Parameters
        ----------
            attribute_aggregation_type: str
            attribute_guid: str, optional
            attribute_identity: int, optional
            count: int, optional
            datum_type: str
            histogram: GrantaServerApiAggregationsHistogram, optional
            type: str
        """
        super().__init__(attribute_aggregation_type=attribute_aggregation_type, attribute_guid=attribute_guid, attribute_identity=attribute_identity, count=count, type=type)
        self._histogram = None
        self._datum_type = None
        self.discriminator = None
        if histogram is not None:
            self.histogram = histogram
        self.datum_type = datum_type

    @property
    def histogram(self) -> "GrantaServerApiAggregationsHistogram":
        """Gets the histogram of this GrantaServerApiAggregationsPointAttributeHistogramAggregation.

        Returns
        -------
        GrantaServerApiAggregationsHistogram
            The histogram of this GrantaServerApiAggregationsPointAttributeHistogramAggregation.
        """
        return self._histogram

    @histogram.setter
    def histogram(self, histogram: "GrantaServerApiAggregationsHistogram") -> None:
        """Sets the histogram of this GrantaServerApiAggregationsPointAttributeHistogramAggregation.

        Parameters
        ----------
        histogram: GrantaServerApiAggregationsHistogram
            The histogram of this GrantaServerApiAggregationsPointAttributeHistogramAggregation.
        """
        self._histogram = histogram

    @property
    def datum_type(self) -> "str":
        """Gets the datum_type of this GrantaServerApiAggregationsPointAttributeHistogramAggregation.

        Returns
        -------
        str
            The datum_type of this GrantaServerApiAggregationsPointAttributeHistogramAggregation.
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type: "str") -> None:
        """Sets the datum_type of this GrantaServerApiAggregationsPointAttributeHistogramAggregation.

        Parameters
        ----------
        datum_type: str
            The datum_type of this GrantaServerApiAggregationsPointAttributeHistogramAggregation.
        """
        if datum_type is None:
            raise ValueError("Invalid value for 'datum_type', must not be 'None'")
        self._datum_type = datum_type

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
        if issubclass(GrantaServerApiAggregationsPointAttributeHistogramAggregation, dict):
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
        if not isinstance(other, GrantaServerApiAggregationsPointAttributeHistogramAggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
