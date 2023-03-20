# coding: utf-8

"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401
from . import ModelBase

from ansys.grantami.serverapi_openapi.models.granta_server_api_data_export_datums_applicable_datum import GrantaServerApiDataExportDatumsApplicableDatum  # noqa: F401,E501

class GrantaServerApiDataExportDatumsFunctionalDatum(GrantaServerApiDataExportDatumsApplicableDatum):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'datum_type': 'str',
        'unit_symbol': 'str',
        'x_axis_parameter': 'GrantaServerApiFunctionalDatumParameterInfo',
        'parameters': 'list[GrantaServerApiFunctionalDatumParameterInfo]',
        'is_estimated': 'bool'
    }
    if hasattr(GrantaServerApiDataExportDatumsApplicableDatum, "swagger_types"):
        swagger_types.update(GrantaServerApiDataExportDatumsApplicableDatum.swagger_types)

    attribute_map = {
        'datum_type': 'datumType',
        'unit_symbol': 'unitSymbol',
        'x_axis_parameter': 'xAxisParameter',
        'parameters': 'parameters',
        'is_estimated': 'isEstimated'
    }
    if hasattr(GrantaServerApiDataExportDatumsApplicableDatum, "attribute_map"):
        attribute_map.update(GrantaServerApiDataExportDatumsApplicableDatum.attribute_map)

    subtype_mapping = {
        'xAxisParameter': 'GrantaServerApiFunctionalDatumParameterInfo',
        'parameters': 'GrantaServerApiFunctionalDatumParameterInfo',
    }

    discriminator_value_class_map = {
        'grid'.lower(): '#/components/schemas/GrantaServerApiDataExportDatumsFunctionalGridDatum',
        'series'.lower(): '#/components/schemas/GrantaServerApiDataExportDatumsFunctionalSeriesDatum',
    }

    def __init__(self, datum_type='floatFunctional', unit_symbol=None, x_axis_parameter=None, parameters=None, is_estimated=None, *args, **kwargs):  # noqa: E501
        """GrantaServerApiDataExportDatumsFunctionalDatum - a model defined in Swagger"""  # noqa: E501
        GrantaServerApiDataExportDatumsApplicableDatum.__init__(self, *args, **kwargs)
        self._datum_type = None
        self._unit_symbol = None
        self._x_axis_parameter = None
        self._parameters = None
        self._is_estimated = None
        self.discriminator = 'graph_type'
        self.datum_type = datum_type
        if unit_symbol is not None:
            self.unit_symbol = unit_symbol
        if x_axis_parameter is not None:
            self.x_axis_parameter = x_axis_parameter
        if parameters is not None:
            self.parameters = parameters
        if is_estimated is not None:
            self.is_estimated = is_estimated

    @property
    def datum_type(self):
        """Gets the datum_type of this GrantaServerApiDataExportDatumsFunctionalDatum.  # noqa: E501

        :return: The datum_type of this GrantaServerApiDataExportDatumsFunctionalDatum.  # noqa: E501
        :rtype: str
        """
        return self._datum_type

    @datum_type.setter
    def datum_type(self, datum_type):
        """Sets the datum_type of this GrantaServerApiDataExportDatumsFunctionalDatum.

        :param datum_type: The datum_type of this GrantaServerApiDataExportDatumsFunctionalDatum.  # noqa: E501
        :type: str
        """
        if datum_type is None:
            raise ValueError("Invalid value for `datum_type`, must not be `None`")  # noqa: E501
        self._datum_type = datum_type

    @property
    def unit_symbol(self):
        """Gets the unit_symbol of this GrantaServerApiDataExportDatumsFunctionalDatum.  # noqa: E501

        :return: The unit_symbol of this GrantaServerApiDataExportDatumsFunctionalDatum.  # noqa: E501
        :rtype: str
        """
        return self._unit_symbol

    @unit_symbol.setter
    def unit_symbol(self, unit_symbol):
        """Sets the unit_symbol of this GrantaServerApiDataExportDatumsFunctionalDatum.

        :param unit_symbol: The unit_symbol of this GrantaServerApiDataExportDatumsFunctionalDatum.  # noqa: E501
        :type: str
        """
        self._unit_symbol = unit_symbol

    @property
    def x_axis_parameter(self):
        """Gets the x_axis_parameter of this GrantaServerApiDataExportDatumsFunctionalDatum.  # noqa: E501

        :return: The x_axis_parameter of this GrantaServerApiDataExportDatumsFunctionalDatum.  # noqa: E501
        :rtype: GrantaServerApiFunctionalDatumParameterInfo
        """
        return self._x_axis_parameter

    @x_axis_parameter.setter
    def x_axis_parameter(self, x_axis_parameter):
        """Sets the x_axis_parameter of this GrantaServerApiDataExportDatumsFunctionalDatum.

        :param x_axis_parameter: The x_axis_parameter of this GrantaServerApiDataExportDatumsFunctionalDatum.  # noqa: E501
        :type: GrantaServerApiFunctionalDatumParameterInfo
        """
        self._x_axis_parameter = x_axis_parameter

    @property
    def parameters(self):
        """Gets the parameters of this GrantaServerApiDataExportDatumsFunctionalDatum.  # noqa: E501

        :return: The parameters of this GrantaServerApiDataExportDatumsFunctionalDatum.  # noqa: E501
        :rtype: list[GrantaServerApiFunctionalDatumParameterInfo]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this GrantaServerApiDataExportDatumsFunctionalDatum.

        :param parameters: The parameters of this GrantaServerApiDataExportDatumsFunctionalDatum.  # noqa: E501
        :type: list[GrantaServerApiFunctionalDatumParameterInfo]
        """
        self._parameters = parameters

    @property
    def is_estimated(self):
        """Gets the is_estimated of this GrantaServerApiDataExportDatumsFunctionalDatum.  # noqa: E501

        :return: The is_estimated of this GrantaServerApiDataExportDatumsFunctionalDatum.  # noqa: E501
        :rtype: bool
        """
        return self._is_estimated

    @is_estimated.setter
    def is_estimated(self, is_estimated):
        """Sets the is_estimated of this GrantaServerApiDataExportDatumsFunctionalDatum.

        :param is_estimated: The is_estimated of this GrantaServerApiDataExportDatumsFunctionalDatum.  # noqa: E501
        :type: bool
        """
        self._is_estimated = is_estimated

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = str(data[self._get_discriminator_field_name()]).lower()
        # The actual class name is not available in swagger-codegen, 
        # so we have to extract it from the JSON reference
        return self.discriminator_value_class_map.get(discriminator_value).rsplit("/", 1)[-1]

    def _get_discriminator_field_name(self):
        name_tokens = self.discriminator.split("_")
        later_tokens = [element.capitalize() for element in name_tokens[1:]]
        return "".join([name_tokens[0], *later_tokens])

    def to_dict(self):
        """Returns the model properties as a dict"""
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
        if issubclass(GrantaServerApiDataExportDatumsFunctionalDatum, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiDataExportDatumsFunctionalDatum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
