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


class GrantaServerApiDataExportExportFailuresExportFailure(ModelBase):
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
    swagger_types = {
        "failure_details": "str",
        "failure_reason": "str",
    }

    attribute_map = {
        "failure_details": "failureDetails",
        "failure_reason": "failureReason",
    }

    subtype_mapping = {}

    discriminator_value_class_map = {
        "record".lower(): "#/components/schemas/GrantaServerApiDataExportExportFailuresRecordExportFailure",
        "link".lower(): "#/components/schemas/GrantaServerApiDataExportExportFailuresLinkExportFailure",
        "attribute".lower(): "#/components/schemas/GrantaServerApiDataExportExportFailuresAttributeExportFailure",
        "datum".lower(): "#/components/schemas/GrantaServerApiDataExportExportFailuresDatumExportFailure",
        "rollup".lower(): "#/components/schemas/GrantaServerApiDataExportExportFailuresRollupExportFailure",
    }

    discriminator = "type"

    def __init__(
        self,
        *,
        failure_details: "str",
        failure_reason: "str",
    ) -> None:
        """GrantaServerApiDataExportExportFailuresExportFailure - a model defined in Swagger

        Parameters
        ----------
            failure_details: str
            failure_reason: str
        """
        self._failure_details = None
        self._failure_reason = None

        self.failure_details = failure_details
        self.failure_reason = failure_reason

    @property
    def failure_details(self) -> "str":
        """Gets the failure_details of this GrantaServerApiDataExportExportFailuresExportFailure.

        Returns
        -------
        str
            The failure_details of this GrantaServerApiDataExportExportFailuresExportFailure.
        """
        return self._failure_details

    @failure_details.setter
    def failure_details(self, failure_details: "str") -> None:
        """Sets the failure_details of this GrantaServerApiDataExportExportFailuresExportFailure.

        Parameters
        ----------
        failure_details: str
            The failure_details of this GrantaServerApiDataExportExportFailuresExportFailure.
        """
        if failure_details is None:
            raise ValueError("Invalid value for 'failure_details', must not be 'None'")
        self._failure_details = failure_details

    @property
    def failure_reason(self) -> "str":
        """Gets the failure_reason of this GrantaServerApiDataExportExportFailuresExportFailure.

        Returns
        -------
        str
            The failure_reason of this GrantaServerApiDataExportExportFailuresExportFailure.
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason: "str") -> None:
        """Sets the failure_reason of this GrantaServerApiDataExportExportFailuresExportFailure.

        Parameters
        ----------
        failure_reason: str
            The failure_reason of this GrantaServerApiDataExportExportFailuresExportFailure.
        """
        if failure_reason is None:
            raise ValueError("Invalid value for 'failure_reason', must not be 'None'")
        self._failure_reason = failure_reason

    @classmethod
    def get_real_child_model(cls, data: ModelBase) -> str:
        """Returns the real base class as determined by the discriminator

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class
        """
        discriminator_value = str(data[cls._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen,
        # so we have to extract it from the JSON reference
        return cls.discriminator_value_class_map.get(discriminator_value).rsplit(
            "/", 1
        )[-1]

    @classmethod
    def _get_discriminator_field_name(cls) -> str:
        name_tokens = cls.discriminator.split("_")
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
        if issubclass(GrantaServerApiDataExportExportFailuresExportFailure, dict):
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
        if not isinstance(other, GrantaServerApiDataExportExportFailuresExportFailure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
