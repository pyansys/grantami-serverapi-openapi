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

from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_datums_applicable_datum import (
    GrantaServerApiDataExportDatumsApplicableDatum,
)  # noqa: F401

if TYPE_CHECKING:
    from . import *


class GrantaServerApiDataExportDatumsShortTextDatum(
    GrantaServerApiDataExportDatumsApplicableDatum
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
    swagger_types = {
        "attribute_guid": "str",
        "attribute_identity": "int",
        "datum_type": "str",
        "datum_value": "str",
        "meta_datums": "list[GrantaServerApiDataExportDatumsDatum]",
        "not_applicable": "str",
    }

    attribute_map = {
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "datum_type": "datumType",
        "datum_value": "datumValue",
        "meta_datums": "metaDatums",
        "not_applicable": "notApplicable",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        attribute_guid: "Optional[str]" = None,
        attribute_identity: "Optional[int]" = None,
        datum_type: "str" = "shortText",
        datum_value: "Optional[str]" = None,
        meta_datums: "Optional[List[GrantaServerApiDataExportDatumsDatum]]" = None,
        not_applicable: "str" = "applicable",
    ) -> None:
        """GrantaServerApiDataExportDatumsShortTextDatum - a model defined in Swagger

        Parameters
        ----------
            attribute_guid: str, optional
            attribute_identity: int, optional
            datum_type: str
            datum_value: str, optional
            meta_datums: List[GrantaServerApiDataExportDatumsDatum], optional
            not_applicable: str
        """
        super().__init__(
            attribute_guid=attribute_guid,
            attribute_identity=attribute_identity,
            meta_datums=meta_datums,
            not_applicable=not_applicable,
        )
        self._datum_type = None
        self._datum_value = None

        self.datum_type = datum_type
        if datum_value is not None:
            self.datum_value = datum_value

    @property
    def datum_type(self) -> "str":
        """Gets the datum_type of this GrantaServerApiDataExportDatumsShortTextDatum.

        Returns
        -------
        str
            The datum_type of this GrantaServerApiDataExportDatumsShortTextDatum.
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type: "str") -> None:
        """Sets the datum_type of this GrantaServerApiDataExportDatumsShortTextDatum.

        Parameters
        ----------
        datum_type: str
            The datum_type of this GrantaServerApiDataExportDatumsShortTextDatum.
        """
        if datum_type is None:
            raise ValueError("Invalid value for 'datum_type', must not be 'None'")
        self._datum_type = datum_type

    @property
    def datum_value(self) -> "str":
        """Gets the datum_value of this GrantaServerApiDataExportDatumsShortTextDatum.

        Returns
        -------
        str
            The datum_value of this GrantaServerApiDataExportDatumsShortTextDatum.
        """
        return self._datum_value

    @datum_value.setter
    def datum_value(self, datum_value: "str") -> None:
        """Sets the datum_value of this GrantaServerApiDataExportDatumsShortTextDatum.

        Parameters
        ----------
        datum_value: str
            The datum_value of this GrantaServerApiDataExportDatumsShortTextDatum.
        """
        self._datum_value = datum_value

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
        if issubclass(GrantaServerApiDataExportDatumsShortTextDatum, dict):
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
        if not isinstance(other, GrantaServerApiDataExportDatumsShortTextDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
