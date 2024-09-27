# Copyright (C) 2023 - 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, Union  # noqa: F401

from . import ModelBase, Unset, Unset_Type

if TYPE_CHECKING:
    from datetime import datetime
    import pathlib

    from . import *


class GsaAddDatabase(ModelBase):
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
        "data_source": "str",
        "database_key": "str",
        "initial_catalog": "str",
        "additional_sql_parameters": "str",
        "is_read_only": "bool",
        "language": "str",
        "loading_order": "int",
        "sql_password": "str",
        "sql_user_name": "str",
        "use_integrated_security": "bool",
        "version_guid": "str",
    }

    attribute_map: Dict[str, str] = {
        "data_source": "dataSource",
        "database_key": "databaseKey",
        "initial_catalog": "initialCatalog",
        "additional_sql_parameters": "additionalSqlParameters",
        "is_read_only": "isReadOnly",
        "language": "language",
        "loading_order": "loadingOrder",
        "sql_password": "sqlPassword",
        "sql_user_name": "sqlUserName",
        "use_integrated_security": "useIntegratedSecurity",
        "version_guid": "versionGuid",
    }

    subtype_mapping: Dict[str, str] = {}

    discriminator: Optional[str] = None

    def __init__(
        self,
        *,
        data_source: "str",
        database_key: "str",
        initial_catalog: "str",
        additional_sql_parameters: "Union[str, None, Unset_Type]" = Unset,
        is_read_only: "Union[bool, None, Unset_Type]" = Unset,
        language: "Union[str, None, Unset_Type]" = Unset,
        loading_order: "Union[int, None, Unset_Type]" = Unset,
        sql_password: "Union[str, None, Unset_Type]" = Unset,
        sql_user_name: "Union[str, None, Unset_Type]" = Unset,
        use_integrated_security: "Union[bool, None, Unset_Type]" = Unset,
        version_guid: "Union[str, None, Unset_Type]" = Unset,
    ) -> None:
        """GsaAddDatabase - a model defined in Swagger

        Parameters
        ----------
        data_source: str
        database_key: str
        initial_catalog: str
        additional_sql_parameters: str, optional
        is_read_only: bool, optional
        language: str, optional
        loading_order: int, optional
        sql_password: str, optional
        sql_user_name: str, optional
        use_integrated_security: bool, optional
        version_guid: str, optional
        """
        self._database_key: str
        self._data_source: str
        self._use_integrated_security: Union[bool, None, Unset_Type] = Unset
        self._sql_user_name: Union[str, None, Unset_Type] = Unset
        self._sql_password: Union[str, None, Unset_Type] = Unset
        self._initial_catalog: str
        self._additional_sql_parameters: Union[str, None, Unset_Type] = Unset
        self._is_read_only: Union[bool, None, Unset_Type] = Unset
        self._loading_order: Union[int, None, Unset_Type] = Unset
        self._language: Union[str, None, Unset_Type] = Unset
        self._version_guid: Union[str, None, Unset_Type] = Unset

        self.database_key = database_key
        self.data_source = data_source
        if use_integrated_security is not Unset:
            self.use_integrated_security = use_integrated_security
        if sql_user_name is not Unset:
            self.sql_user_name = sql_user_name
        if sql_password is not Unset:
            self.sql_password = sql_password
        self.initial_catalog = initial_catalog
        if additional_sql_parameters is not Unset:
            self.additional_sql_parameters = additional_sql_parameters
        if is_read_only is not Unset:
            self.is_read_only = is_read_only
        if loading_order is not Unset:
            self.loading_order = loading_order
        if language is not Unset:
            self.language = language
        if version_guid is not Unset:
            self.version_guid = version_guid

    @property
    def database_key(self) -> "str":
        """Gets the database_key of this GsaAddDatabase.

        Returns
        -------
        str
            The database_key of this GsaAddDatabase.
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key: "str") -> None:
        """Sets the database_key of this GsaAddDatabase.

        Parameters
        ----------
        database_key: str
            The database_key of this GsaAddDatabase.
        """
        # Field is not nullable
        if database_key is None:
            raise ValueError("Invalid value for 'database_key', must not be 'None'")
        # Field is required
        if database_key is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'database_key', must not be 'Unset'")
        self._database_key = database_key

    @property
    def data_source(self) -> "str":
        """Gets the data_source of this GsaAddDatabase.
        The SQL server data source

        Returns
        -------
        str
            The data_source of this GsaAddDatabase.
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source: "str") -> None:
        """Sets the data_source of this GsaAddDatabase.
        The SQL server data source

        Parameters
        ----------
        data_source: str
            The data_source of this GsaAddDatabase.
        """
        # Field is not nullable
        if data_source is None:
            raise ValueError("Invalid value for 'data_source', must not be 'None'")
        # Field is required
        if data_source is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'data_source', must not be 'Unset'")
        self._data_source = data_source

    @property
    def use_integrated_security(self) -> "Union[bool, None, Unset_Type]":
        """Gets the use_integrated_security of this GsaAddDatabase.
        Set to true if the SQL connection to the new database should use Windows authentication

        Returns
        -------
        Union[bool, None, Unset_Type]
            The use_integrated_security of this GsaAddDatabase.
        """
        return self._use_integrated_security

    @use_integrated_security.setter
    def use_integrated_security(
        self, use_integrated_security: "Union[bool, None, Unset_Type]"
    ) -> None:
        """Sets the use_integrated_security of this GsaAddDatabase.
        Set to true if the SQL connection to the new database should use Windows authentication

        Parameters
        ----------
        use_integrated_security: Union[bool, None, Unset_Type]
            The use_integrated_security of this GsaAddDatabase.
        """
        self._use_integrated_security = use_integrated_security

    @property
    def sql_user_name(self) -> "Union[str, None, Unset_Type]":
        """Gets the sql_user_name of this GsaAddDatabase.
        The user name to use if the new database should use SQL authentication. The password must also be provided.

        Returns
        -------
        Union[str, None, Unset_Type]
            The sql_user_name of this GsaAddDatabase.
        """
        return self._sql_user_name

    @sql_user_name.setter
    def sql_user_name(self, sql_user_name: "Union[str, None, Unset_Type]") -> None:
        """Sets the sql_user_name of this GsaAddDatabase.
        The user name to use if the new database should use SQL authentication. The password must also be provided.

        Parameters
        ----------
        sql_user_name: Union[str, None, Unset_Type]
            The sql_user_name of this GsaAddDatabase.
        """
        self._sql_user_name = sql_user_name

    @property
    def sql_password(self) -> "Union[str, None, Unset_Type]":
        """Gets the sql_password of this GsaAddDatabase.

        Returns
        -------
        Union[str, None, Unset_Type]
            The sql_password of this GsaAddDatabase.
        """
        return self._sql_password

    @sql_password.setter
    def sql_password(self, sql_password: "Union[str, None, Unset_Type]") -> None:
        """Sets the sql_password of this GsaAddDatabase.

        Parameters
        ----------
        sql_password: Union[str, None, Unset_Type]
            The sql_password of this GsaAddDatabase.
        """
        self._sql_password = sql_password

    @property
    def initial_catalog(self) -> "str":
        """Gets the initial_catalog of this GsaAddDatabase.
        The name of the database in SQL server

        Returns
        -------
        str
            The initial_catalog of this GsaAddDatabase.
        """
        return self._initial_catalog

    @initial_catalog.setter
    def initial_catalog(self, initial_catalog: "str") -> None:
        """Sets the initial_catalog of this GsaAddDatabase.
        The name of the database in SQL server

        Parameters
        ----------
        initial_catalog: str
            The initial_catalog of this GsaAddDatabase.
        """
        # Field is not nullable
        if initial_catalog is None:
            raise ValueError("Invalid value for 'initial_catalog', must not be 'None'")
        # Field is required
        if initial_catalog is Unset:  # type: ignore[comparison-overlap, unused-ignore]
            raise ValueError("Invalid value for 'initial_catalog', must not be 'Unset'")
        self._initial_catalog = initial_catalog

    @property
    def additional_sql_parameters(self) -> "Union[str, None, Unset_Type]":
        """Gets the additional_sql_parameters of this GsaAddDatabase.
        (Optional) Any additional parameters that will be added to the SQL connection string for the database. Must be a valid SQL connection string format.

        Returns
        -------
        Union[str, None, Unset_Type]
            The additional_sql_parameters of this GsaAddDatabase.
        """
        return self._additional_sql_parameters

    @additional_sql_parameters.setter
    def additional_sql_parameters(
        self, additional_sql_parameters: "Union[str, None, Unset_Type]"
    ) -> None:
        """Sets the additional_sql_parameters of this GsaAddDatabase.
        (Optional) Any additional parameters that will be added to the SQL connection string for the database. Must be a valid SQL connection string format.

        Parameters
        ----------
        additional_sql_parameters: Union[str, None, Unset_Type]
            The additional_sql_parameters of this GsaAddDatabase.
        """
        self._additional_sql_parameters = additional_sql_parameters

    @property
    def is_read_only(self) -> "Union[bool, None, Unset_Type]":
        """Gets the is_read_only of this GsaAddDatabase.
        (Optional) True if the database should be set to read only after adding

        Returns
        -------
        Union[bool, None, Unset_Type]
            The is_read_only of this GsaAddDatabase.
        """
        return self._is_read_only

    @is_read_only.setter
    def is_read_only(self, is_read_only: "Union[bool, None, Unset_Type]") -> None:
        """Sets the is_read_only of this GsaAddDatabase.
        (Optional) True if the database should be set to read only after adding

        Parameters
        ----------
        is_read_only: Union[bool, None, Unset_Type]
            The is_read_only of this GsaAddDatabase.
        """
        self._is_read_only = is_read_only

    @property
    def loading_order(self) -> "Union[int, None, Unset_Type]":
        """Gets the loading_order of this GsaAddDatabase.
        (Optional) The MI loading order for the database

        Returns
        -------
        Union[int, None, Unset_Type]
            The loading_order of this GsaAddDatabase.
        """
        return self._loading_order

    @loading_order.setter
    def loading_order(self, loading_order: "Union[int, None, Unset_Type]") -> None:
        """Sets the loading_order of this GsaAddDatabase.
        (Optional) The MI loading order for the database

        Parameters
        ----------
        loading_order: Union[int, None, Unset_Type]
            The loading_order of this GsaAddDatabase.
        """
        self._loading_order = loading_order

    @property
    def language(self) -> "Union[str, None, Unset_Type]":
        """Gets the language of this GsaAddDatabase.
        (Optional) The language of the database, used when indexing the database. Currently \"english\" is the only supported value.

        Returns
        -------
        Union[str, None, Unset_Type]
            The language of this GsaAddDatabase.
        """
        return self._language

    @language.setter
    def language(self, language: "Union[str, None, Unset_Type]") -> None:
        """Sets the language of this GsaAddDatabase.
        (Optional) The language of the database, used when indexing the database. Currently \"english\" is the only supported value.

        Parameters
        ----------
        language: Union[str, None, Unset_Type]
            The language of this GsaAddDatabase.
        """
        self._language = language

    @property
    def version_guid(self) -> "Union[str, None, Unset_Type]":
        """Gets the version_guid of this GsaAddDatabase.
        (Optional) Overrides the database version guid stored in the database. This must be unique across all the loaded databases.

        Returns
        -------
        Union[str, None, Unset_Type]
            The version_guid of this GsaAddDatabase.
        """
        return self._version_guid

    @version_guid.setter
    def version_guid(self, version_guid: "Union[str, None, Unset_Type]") -> None:
        """Sets the version_guid of this GsaAddDatabase.
        (Optional) Overrides the database version guid stored in the database. This must be unique across all the loaded databases.

        Parameters
        ----------
        version_guid: Union[str, None, Unset_Type]
            The version_guid of this GsaAddDatabase.
        """
        self._version_guid = version_guid

    @classmethod
    def get_real_child_model(cls, data: Dict[str, str]) -> str:
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
        if not isinstance(other, GsaAddDatabase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
