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

from ansys.grantami.serverapi_openapi.models.granta_server_api_aggregations_attribute_aggregation import GrantaServerApiAggregationsAttributeAggregation  # noqa: F401

if TYPE_CHECKING:
    from . import *

class GrantaServerApiAggregationsAttributeValueAggregation(GrantaServerApiAggregationsAttributeAggregation):
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
        "attribute_aggregation_type": "str",
    }

    attribute_map = {
        "attribute_aggregation_type": "attributeAggregationType",
    }

    subtype_mapping = {
    }

    discriminator_value_class_map = {
        "integer".lower(): "#/components/schemas/GrantaServerApiAggregationsIntegerAttributeAggregation",
        "point".lower(): "#/components/schemas/GrantaServerApiAggregationsPointAttributeAggregation",
        "range".lower(): "#/components/schemas/GrantaServerApiAggregationsRangeAttributeAggregation",
        "integerHistogram".lower(): "#/components/schemas/GrantaServerApiAggregationsIntegerAttributeHistogramAggregation",
        "pointHistogram".lower(): "#/components/schemas/GrantaServerApiAggregationsPointAttributeHistogramAggregation",
        "rangeHistogram".lower(): "#/components/schemas/GrantaServerApiAggregationsRangeAttributeHistogramAggregation",
        "dateTime".lower(): "#/components/schemas/GrantaServerApiAggregationsDateTimeAttributeAggregation",
        "dateTimeHistogram".lower(): "#/components/schemas/GrantaServerApiAggregationsDateTimeAttributeHistogramAggregation",
        "shortText".lower(): "#/components/schemas/GrantaServerApiAggregationsShortTextAttributeAggregation",
        "discreteText".lower(): "#/components/schemas/GrantaServerApiAggregationsDiscreteTextAttributeAggregation",
        "link".lower(): "#/components/schemas/GrantaServerApiAggregationsLinkAttributeAggregation",
        "logical".lower(): "#/components/schemas/GrantaServerApiAggregationsLogicalAttributeAggregation",
        "floatFunctionalGraph".lower(): "#/components/schemas/GrantaServerApiAggregationsFloatFunctionalAttributeAggregation",
    }

    def __init__(self, *, attribute_aggregation_type: "str" = 'value', attribute_guid: "Optional[str]" = None, attribute_identity: "Optional[int]" = None, count: "Optional[int]" = None, type: "str" = 'attribute') -> None:
        """GrantaServerApiAggregationsAttributeValueAggregation - a model defined in Swagger

        Parameters
        ----------
            attribute_aggregation_type: str
            attribute_guid: str, optional
            attribute_identity: int, optional
            count: int, optional
            type: str
        """
        super().__init__(attribute_guid=attribute_guid, attribute_identity=attribute_identity, count=count, type=type)
        self._attribute_aggregation_type = None
        self.discriminator = "datum_type"
        self.attribute_aggregation_type = attribute_aggregation_type

    @property
    def attribute_aggregation_type(self) -> "str":
        """Gets the attribute_aggregation_type of this GrantaServerApiAggregationsAttributeValueAggregation.

        Returns
        -------
        str
            The attribute_aggregation_type of this GrantaServerApiAggregationsAttributeValueAggregation.
        """
        return self._attribute_aggregation_type

    @attribute_aggregation_type.setter
    def attribute_aggregation_type(self, attribute_aggregation_type: "str") -> None:
        """Sets the attribute_aggregation_type of this GrantaServerApiAggregationsAttributeValueAggregation.

        Parameters
        ----------
        attribute_aggregation_type: str
            The attribute_aggregation_type of this GrantaServerApiAggregationsAttributeValueAggregation.
        """
        if attribute_aggregation_type is None:
            raise ValueError("Invalid value for 'attribute_aggregation_type', must not be 'None'")
        self._attribute_aggregation_type = attribute_aggregation_type

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
        if issubclass(GrantaServerApiAggregationsAttributeValueAggregation, dict):
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
        if not isinstance(other, GrantaServerApiAggregationsAttributeValueAggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
