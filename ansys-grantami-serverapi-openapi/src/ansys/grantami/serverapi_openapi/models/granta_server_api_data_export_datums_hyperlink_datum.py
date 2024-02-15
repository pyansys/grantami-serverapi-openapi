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
from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_datums_applicable_datum import (
    GrantaServerApiDataExportDatumsApplicableDatum,
)  # noqa: F401


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GrantaServerApiDataExportDatumsHyperlinkDatum(
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
    swagger_types: Dict[str, str] = {
        "attribute_guid": "str",
        "attribute_identity": "int",
        "datum_type": "str",
        "datum_value": "GrantaServerApiDataExportDatumsHyperlink",
        "meta_datums": "list[GrantaServerApiDataExportDatumsDatum]",
        "not_applicable": "str",
    }

    attribute_map: Dict[str, str] = {
        "attribute_guid": "attributeGuid",
        "attribute_identity": "attributeIdentity",
        "datum_type": "datumType",
        "datum_value": "datumValue",
        "meta_datums": "metaDatums",
        "not_applicable": "notApplicable",
    }

    subtype_mapping: Dict[str, str] = {
        "datumValue": "GrantaServerApiDataExportDatumsHyperlink",
    }

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        attribute_guid: "Optional[str]" = None,
        attribute_identity: "Optional[int]" = None,
        datum_type: "str" = "hyperlink",
        datum_value: "Optional[GrantaServerApiDataExportDatumsHyperlink]" = None,
        meta_datums: "Optional[List[GrantaServerApiDataExportDatumsDatum]]" = None,
        not_applicable: "str" = "applicable",
    ) -> None:
        """GrantaServerApiDataExportDatumsHyperlinkDatum - a model defined in Swagger

        Parameters
        ----------
            attribute_guid: str, optional
            attribute_identity: int, optional
            datum_type: str
            datum_value: GrantaServerApiDataExportDatumsHyperlink, optional
            meta_datums: List[GrantaServerApiDataExportDatumsDatum], optional
            not_applicable: str
        """
        super().__init__(
            attribute_guid=attribute_guid,
            attribute_identity=attribute_identity,
            meta_datums=meta_datums,
            not_applicable=not_applicable,
        )
        self._datum_type: str = None  # type: ignore[assignment]
        self._datum_value = None

        self.datum_type = datum_type
        if datum_value is not None:
            self.datum_value = datum_value

    @property
    def datum_type(self) -> "str":
        """Gets the datum_type of this GrantaServerApiDataExportDatumsHyperlinkDatum.

        Returns
        -------
        str
            The datum_type of this GrantaServerApiDataExportDatumsHyperlinkDatum.
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type: "str") -> None:
        """Sets the datum_type of this GrantaServerApiDataExportDatumsHyperlinkDatum.

        Parameters
        ----------
        datum_type: str
            The datum_type of this GrantaServerApiDataExportDatumsHyperlinkDatum.
        """
        if datum_type is None:
            raise ValueError("Invalid value for 'datum_type', must not be 'None'")
        self._datum_type = datum_type

    @property
    def datum_value(self) -> "Optional[GrantaServerApiDataExportDatumsHyperlink]":
        """Gets the datum_value of this GrantaServerApiDataExportDatumsHyperlinkDatum.

        Returns
        -------
        GrantaServerApiDataExportDatumsHyperlink
            The datum_value of this GrantaServerApiDataExportDatumsHyperlinkDatum.
        """
        return self._datum_value

    @datum_value.setter
    def datum_value(
        self, datum_value: "Optional[GrantaServerApiDataExportDatumsHyperlink]"
    ) -> None:
        """Sets the datum_value of this GrantaServerApiDataExportDatumsHyperlinkDatum.

        Parameters
        ----------
        datum_value: GrantaServerApiDataExportDatumsHyperlink
            The datum_value of this GrantaServerApiDataExportDatumsHyperlinkDatum.
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

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()  # type: ignore[no-any-return]

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiDataExportDatumsHyperlinkDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
