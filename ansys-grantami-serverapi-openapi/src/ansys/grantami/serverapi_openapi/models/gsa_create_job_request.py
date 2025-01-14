"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type


if TYPE_CHECKING:
    from datetime import datetime
    import pathlib
    from . import *


class GsaCreateJobRequest(ModelBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes
    ----------
    swagger_types: dict[str, str]
        The key is attribute name and the value is attribute type.
    attribute_map: dict[str, str]
        The key is attribute name and the value is json key in definition.
    subtype_mapping: dict[str, str]
        The key is the unmangled property name and the value is the corresponding type.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types: dict[str, str] = {
        "culture": "str",
        "description": "str",
        "input_file_ids": "list[str]",
        "name": "str",
        "parameters": "str",
        "scheduled_execution_date": "datetime",
        "type": "str",
        "version": "int",
    }

    attribute_map: dict[str, str] = {
        "culture": "culture",
        "description": "description",
        "input_file_ids": "inputFileIds",
        "name": "name",
        "parameters": "parameters",
        "scheduled_execution_date": "scheduledExecutionDate",
        "type": "type",
        "version": "version",
    }

    subtype_mapping: dict[str, str] = {
    }

    discriminator: Optional[str] = None

    def __init__(self, *, culture: "Union[str, None, Unset_Type]" = Unset, description: "Union[str, None, Unset_Type]" = Unset, input_file_ids: "Union[list[str], None, Unset_Type]" = Unset, name: "Union[str, None, Unset_Type]" = Unset, parameters: "Union[str, None, Unset_Type]" = Unset, scheduled_execution_date: "Union[datetime, None, Unset_Type]" = Unset, type: "Union[str, None, Unset_Type]" = Unset, version: "Union[int, Unset_Type]" = Unset,) -> None:
        """GsaCreateJobRequest - a model defined in Swagger

        Parameters
        ----------
        culture: str, optional
        description: str, optional
        input_file_ids: list[str], optional
        name: str, optional
        parameters: str, optional
        scheduled_execution_date: datetime, optional
        type: str, optional
        version: int, optional
        """
        self._name: Union[str, None, Unset_Type] = Unset
        self._description: Union[str, None, Unset_Type] = Unset
        self._culture: Union[str, None, Unset_Type] = Unset
        self._type: Union[str, None, Unset_Type] = Unset
        self._version: Union[int, Unset_Type] = Unset
        self._scheduled_execution_date: Union[datetime, None, Unset_Type] = Unset
        self._input_file_ids: Union[list[str], None, Unset_Type] = Unset
        self._parameters: Union[str, None, Unset_Type] = Unset

        if name is not Unset:
            self.name = name
        if description is not Unset:
            self.description = description
        if culture is not Unset:
            self.culture = culture
        if type is not Unset:
            self.type = type
        if version is not Unset:
            self.version = version
        if scheduled_execution_date is not Unset:
            self.scheduled_execution_date = scheduled_execution_date
        if input_file_ids is not Unset:
            self.input_file_ids = input_file_ids
        if parameters is not Unset:
            self.parameters = parameters

    @property
    def name(self) -> "Union[str, None, Unset_Type]":
        """Gets the name of this GsaCreateJobRequest.

        Returns
        -------
        Union[str, None, Unset_Type]
            The name of this GsaCreateJobRequest.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, None, Unset_Type]") -> None:
        """Sets the name of this GsaCreateJobRequest.

        Parameters
        ----------
        name: Union[str, None, Unset_Type]
            The name of this GsaCreateJobRequest.
        """
        self._name = name

    @property
    def description(self) -> "Union[str, None, Unset_Type]":
        """Gets the description of this GsaCreateJobRequest.

        Returns
        -------
        Union[str, None, Unset_Type]
            The description of this GsaCreateJobRequest.
        """
        return self._description

    @description.setter
    def description(self, description: "Union[str, None, Unset_Type]") -> None:
        """Sets the description of this GsaCreateJobRequest.

        Parameters
        ----------
        description: Union[str, None, Unset_Type]
            The description of this GsaCreateJobRequest.
        """
        self._description = description

    @property
    def culture(self) -> "Union[str, None, Unset_Type]":
        """Gets the culture of this GsaCreateJobRequest.

        Returns
        -------
        Union[str, None, Unset_Type]
            The culture of this GsaCreateJobRequest.
        """
        return self._culture

    @culture.setter
    def culture(self, culture: "Union[str, None, Unset_Type]") -> None:
        """Sets the culture of this GsaCreateJobRequest.

        Parameters
        ----------
        culture: Union[str, None, Unset_Type]
            The culture of this GsaCreateJobRequest.
        """
        self._culture = culture

    @property
    def type(self) -> "Union[str, None, Unset_Type]":
        """Gets the type of this GsaCreateJobRequest.

        Returns
        -------
        Union[str, None, Unset_Type]
            The type of this GsaCreateJobRequest.
        """
        return self._type

    @type.setter
    def type(self, type: "Union[str, None, Unset_Type]") -> None:
        """Sets the type of this GsaCreateJobRequest.

        Parameters
        ----------
        type: Union[str, None, Unset_Type]
            The type of this GsaCreateJobRequest.
        """
        self._type = type

    @property
    def version(self) -> "Union[int, Unset_Type]":
        """Gets the version of this GsaCreateJobRequest.

        Returns
        -------
        Union[int, Unset_Type]
            The version of this GsaCreateJobRequest.
        """
        return self._version

    @version.setter
    def version(self, version: "Union[int, Unset_Type]") -> None:
        """Sets the version of this GsaCreateJobRequest.

        Parameters
        ----------
        version: Union[int, Unset_Type]
            The version of this GsaCreateJobRequest.
        """
        # Field is not nullable
        if version is None:
            raise ValueError("Invalid value for 'version', must not be 'None'")
        self._version = version

    @property
    def scheduled_execution_date(self) -> "Union[datetime, None, Unset_Type]":
        """Gets the scheduled_execution_date of this GsaCreateJobRequest.

        Returns
        -------
        Union[datetime, None, Unset_Type]
            The scheduled_execution_date of this GsaCreateJobRequest.
        """
        return self._scheduled_execution_date

    @scheduled_execution_date.setter
    def scheduled_execution_date(self, scheduled_execution_date: "Union[datetime, None, Unset_Type]") -> None:
        """Sets the scheduled_execution_date of this GsaCreateJobRequest.

        Parameters
        ----------
        scheduled_execution_date: Union[datetime, None, Unset_Type]
            The scheduled_execution_date of this GsaCreateJobRequest.
        """
        self._scheduled_execution_date = scheduled_execution_date

    @property
    def input_file_ids(self) -> "Union[list[str], None, Unset_Type]":
        """Gets the input_file_ids of this GsaCreateJobRequest.
        Names of temporary input files that were uploaded prior to creating this job.

        Returns
        -------
        Union[list[str], None, Unset_Type]
            The input_file_ids of this GsaCreateJobRequest.
        """
        return self._input_file_ids

    @input_file_ids.setter
    def input_file_ids(self, input_file_ids: "Union[list[str], None, Unset_Type]") -> None:
        """Sets the input_file_ids of this GsaCreateJobRequest.
        Names of temporary input files that were uploaded prior to creating this job.

        Parameters
        ----------
        input_file_ids: Union[list[str], None, Unset_Type]
            The input_file_ids of this GsaCreateJobRequest.
        """
        self._input_file_ids = input_file_ids

    @property
    def parameters(self) -> "Union[str, None, Unset_Type]":
        """Gets the parameters of this GsaCreateJobRequest.

        Returns
        -------
        Union[str, None, Unset_Type]
            The parameters of this GsaCreateJobRequest.
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters: "Union[str, None, Unset_Type]") -> None:
        """Sets the parameters of this GsaCreateJobRequest.

        Parameters
        ----------
        parameters: Union[str, None, Unset_Type]
            The parameters of this GsaCreateJobRequest.
        """
        self._parameters = parameters

    @classmethod
    def get_real_child_model(cls, data: dict[str, str]) -> str:
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
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GsaCreateJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other

