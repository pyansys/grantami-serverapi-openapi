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


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiSearchDatumCriterion(ModelBase):  # type: ignore[misc]
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
    swagger_types: Dict[str, str] = {}

    attribute_map: Dict[str, str] = {}

    subtype_mapping: Dict[str, str] = {}

    discriminator_value_class_map = {
        "dateTime".lower(): "#/components/schemas/GrantaServerApiSearchDateTimeDatumCriterion",
        "discreteFunctionalRange".lower(): "#/components/schemas/GrantaServerApiSearchDiscreteFunctionalRangeDatumCriterion",
        "discreteFunctionalValues".lower(): "#/components/schemas/GrantaServerApiSearchDiscreteFunctionalValuesDatumCriterion",
        "discreteIdentity".lower(): "#/components/schemas/GrantaServerApiSearchDiscreteIdentityDatumCriterion",
        "discreteIdentityValues".lower(): "#/components/schemas/GrantaServerApiSearchDiscreteIdentityValuesDatumCriterion",
        "discreteGuid".lower(): "#/components/schemas/GrantaServerApiSearchDiscreteGuidDatumCriterion",
        "discreteGuidValues".lower(): "#/components/schemas/GrantaServerApiSearchDiscreteGuidValuesDatumCriterion",
        "discreteRange".lower(): "#/components/schemas/GrantaServerApiSearchDiscreteRangeDatumCriterion",
        "discreteText".lower(): "#/components/schemas/GrantaServerApiSearchDiscreteTextDatumCriterion",
        "discreteTextValues".lower(): "#/components/schemas/GrantaServerApiSearchDiscreteTextValuesDatumCriterion",
        "file".lower(): "#/components/schemas/GrantaServerApiSearchFileDatumCriterion",
        "floatFunctionalData".lower(): "#/components/schemas/GrantaServerApiSearchFloatFunctionalDatumCriterion",
        "floatFunctionalGraph".lower(): "#/components/schemas/GrantaServerApiSearchFloatFunctionalGraphDatumCriterion",
        "hyperlink".lower(): "#/components/schemas/GrantaServerApiSearchHyperlinkDatumCriterion",
        "integer".lower(): "#/components/schemas/GrantaServerApiSearchIntegerDatumCriterion",
        "link".lower(): "#/components/schemas/GrantaServerApiSearchLinkDatumCriterion",
        "logical".lower(): "#/components/schemas/GrantaServerApiSearchLogicalDatumCriterion",
        "longText".lower(): "#/components/schemas/GrantaServerApiSearchLongTextDatumCriterion",
        "mathsFunctional".lower(): "#/components/schemas/GrantaServerApiSearchMathsFunctionalDatumCriterion",
        "picture".lower(): "#/components/schemas/GrantaServerApiSearchPictureDatumCriterion",
        "point".lower(): "#/components/schemas/GrantaServerApiSearchPointDatumCriterion",
        "range".lower(): "#/components/schemas/GrantaServerApiSearchRangeDatumCriterion",
        "shortText".lower(): "#/components/schemas/GrantaServerApiSearchShortTextDatumCriterion",
    }

    discriminator: Optional[str] = "type"

    def __init__(
        self,
    ) -> None:
        """GrantaServerApiSearchDatumCriterion - a model defined in Swagger"""

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
        return cls.discriminator_value_class_map[discriminator_value].rsplit("/", 1)[-1]

    @classmethod
    def _get_discriminator_field_name(cls) -> str:
        assert cls.discriminator
        name_tokens = cls.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()  # type: ignore[no-any-return]

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiSearchDatumCriterion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
