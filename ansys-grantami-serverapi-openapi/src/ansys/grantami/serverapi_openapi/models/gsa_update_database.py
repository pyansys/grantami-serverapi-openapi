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


class GsaUpdateDatabase(ModelBase):
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
        "additional_sql_parameters": "str",
        "author": "str",
        "company": "str",
        "currency_code": "str",
        "data_source": "str",
        "database_key": "str",
        "guid": "str",
        "initial_catalog": "str",
        "is_read_only": "bool",
        "language": "str",
        "loading_order": "int",
        "name": "str",
        "notes": "str",
        "sql_password": "str",
        "sql_user_name": "str",
        "use_integrated_security": "bool",
        "version_guid": "str",
    }

    attribute_map: Dict[str, str] = {
        "additional_sql_parameters": "additionalSqlParameters",
        "author": "author",
        "company": "company",
        "currency_code": "currencyCode",
        "data_source": "dataSource",
        "database_key": "databaseKey",
        "guid": "guid",
        "initial_catalog": "initialCatalog",
        "is_read_only": "isReadOnly",
        "language": "language",
        "loading_order": "loadingOrder",
        "name": "name",
        "notes": "notes",
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
        additional_sql_parameters: "Union[str, None, Unset_Type]" = Unset,
        author: "Union[str, None, Unset_Type]" = Unset,
        company: "Union[str, None, Unset_Type]" = Unset,
        currency_code: "Union[str, None, Unset_Type]" = Unset,
        data_source: "Union[str, None, Unset_Type]" = Unset,
        database_key: "Union[str, None, Unset_Type]" = Unset,
        guid: "Union[str, Unset_Type]" = Unset,
        initial_catalog: "Union[str, None, Unset_Type]" = Unset,
        is_read_only: "Union[bool, Unset_Type]" = Unset,
        language: "Union[str, None, Unset_Type]" = Unset,
        loading_order: "Union[int, Unset_Type]" = Unset,
        name: "Union[str, Unset_Type]" = Unset,
        notes: "Union[str, None, Unset_Type]" = Unset,
        sql_password: "Union[str, None, Unset_Type]" = Unset,
        sql_user_name: "Union[str, None, Unset_Type]" = Unset,
        use_integrated_security: "Union[bool, None, Unset_Type]" = Unset,
        version_guid: "Union[str, Unset_Type]" = Unset,
    ) -> None:
        """GsaUpdateDatabase - a model defined in Swagger

        Parameters
        ----------
        additional_sql_parameters: str, optional
        author: str, optional
        company: str, optional
        currency_code: str, optional
        data_source: str, optional
        database_key: str, optional
        guid: str, optional
        initial_catalog: str, optional
        is_read_only: bool, optional
        language: str, optional
        loading_order: int, optional
        name: str, optional
        notes: str, optional
        sql_password: str, optional
        sql_user_name: str, optional
        use_integrated_security: bool, optional
        version_guid: str, optional
        """
        self._author: Union[str, None, Unset_Type] = Unset
        self._company: Union[str, None, Unset_Type] = Unset
        self._notes: Union[str, None, Unset_Type] = Unset
        self._currency_code: Union[str, None, Unset_Type] = Unset
        self._version_guid: Union[str, Unset_Type] = Unset
        self._guid: Union[str, Unset_Type] = Unset
        self._name: Union[str, Unset_Type] = Unset
        self._is_read_only: Union[bool, Unset_Type] = Unset
        self._language: Union[str, None, Unset_Type] = Unset
        self._database_key: Union[str, None, Unset_Type] = Unset
        self._data_source: Union[str, None, Unset_Type] = Unset
        self._use_integrated_security: Union[bool, None, Unset_Type] = Unset
        self._sql_user_name: Union[str, None, Unset_Type] = Unset
        self._sql_password: Union[str, None, Unset_Type] = Unset
        self._initial_catalog: Union[str, None, Unset_Type] = Unset
        self._additional_sql_parameters: Union[str, None, Unset_Type] = Unset
        self._loading_order: Union[int, Unset_Type] = Unset

        if author is not Unset:
            self.author = author
        if company is not Unset:
            self.company = company
        if notes is not Unset:
            self.notes = notes
        if currency_code is not Unset:
            self.currency_code = currency_code
        if version_guid is not Unset:
            self.version_guid = version_guid
        if guid is not Unset:
            self.guid = guid
        if name is not Unset:
            self.name = name
        if is_read_only is not Unset:
            self.is_read_only = is_read_only
        if language is not Unset:
            self.language = language
        if database_key is not Unset:
            self.database_key = database_key
        if data_source is not Unset:
            self.data_source = data_source
        if use_integrated_security is not Unset:
            self.use_integrated_security = use_integrated_security
        if sql_user_name is not Unset:
            self.sql_user_name = sql_user_name
        if sql_password is not Unset:
            self.sql_password = sql_password
        if initial_catalog is not Unset:
            self.initial_catalog = initial_catalog
        if additional_sql_parameters is not Unset:
            self.additional_sql_parameters = additional_sql_parameters
        if loading_order is not Unset:
            self.loading_order = loading_order

    @property
    def author(self) -> "Union[str, None, Unset_Type]":
        """Gets the author of this GsaUpdateDatabase.
        The author of the database. Can only be edited by a database data administrator

        Returns
        -------
        Union[str, None, Unset_Type]
            The author of this GsaUpdateDatabase.
        """
        return self._author

    @author.setter
    def author(self, author: "Union[str, None, Unset_Type]") -> None:
        """Sets the author of this GsaUpdateDatabase.
        The author of the database. Can only be edited by a database data administrator

        Parameters
        ----------
        author: Union[str, None, Unset_Type]
            The author of this GsaUpdateDatabase.
        """
        self._author = author

    @property
    def company(self) -> "Union[str, None, Unset_Type]":
        """Gets the company of this GsaUpdateDatabase.
        The company on the database. Can only be edited by a database data administrator

        Returns
        -------
        Union[str, None, Unset_Type]
            The company of this GsaUpdateDatabase.
        """
        return self._company

    @company.setter
    def company(self, company: "Union[str, None, Unset_Type]") -> None:
        """Sets the company of this GsaUpdateDatabase.
        The company on the database. Can only be edited by a database data administrator

        Parameters
        ----------
        company: Union[str, None, Unset_Type]
            The company of this GsaUpdateDatabase.
        """
        self._company = company

    @property
    def notes(self) -> "Union[str, None, Unset_Type]":
        """Gets the notes of this GsaUpdateDatabase.
        The notes for the database. Can only be edited by a database data administrator

        Returns
        -------
        Union[str, None, Unset_Type]
            The notes of this GsaUpdateDatabase.
        """
        return self._notes

    @notes.setter
    def notes(self, notes: "Union[str, None, Unset_Type]") -> None:
        """Sets the notes of this GsaUpdateDatabase.
        The notes for the database. Can only be edited by a database data administrator

        Parameters
        ----------
        notes: Union[str, None, Unset_Type]
            The notes of this GsaUpdateDatabase.
        """
        self._notes = notes

    @property
    def currency_code(self) -> "Union[str, None, Unset_Type]":
        """Gets the currency_code of this GsaUpdateDatabase.
        The currency code on the database. Can only be edited by a database data administrator

        Returns
        -------
        Union[str, None, Unset_Type]
            The currency_code of this GsaUpdateDatabase.
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code: "Union[str, None, Unset_Type]") -> None:
        """Sets the currency_code of this GsaUpdateDatabase.
        The currency code on the database. Can only be edited by a database data administrator

        Parameters
        ----------
        currency_code: Union[str, None, Unset_Type]
            The currency_code of this GsaUpdateDatabase.
        """
        self._currency_code = currency_code

    @property
    def version_guid(self) -> "Union[str, Unset_Type]":
        """Gets the version_guid of this GsaUpdateDatabase.
        The version guid of the database. Can be edited by a database data administrator or a system administrator

        Returns
        -------
        Union[str, Unset_Type]
            The version_guid of this GsaUpdateDatabase.
        """
        return self._version_guid

    @version_guid.setter
    def version_guid(self, version_guid: "Union[str, Unset_Type]") -> None:
        """Sets the version_guid of this GsaUpdateDatabase.
        The version guid of the database. Can be edited by a database data administrator or a system administrator

        Parameters
        ----------
        version_guid: Union[str, Unset_Type]
            The version_guid of this GsaUpdateDatabase.
        """
        # Field is not nullable
        if version_guid is None:
            raise ValueError("Invalid value for 'version_guid', must not be 'None'")
        self._version_guid = version_guid

    @property
    def guid(self) -> "Union[str, Unset_Type]":
        """Gets the guid of this GsaUpdateDatabase.
        The unique identifier of the database. Can only be edited by a system administrator

        Returns
        -------
        Union[str, Unset_Type]
            The guid of this GsaUpdateDatabase.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "Union[str, Unset_Type]") -> None:
        """Sets the guid of this GsaUpdateDatabase.
        The unique identifier of the database. Can only be edited by a system administrator

        Parameters
        ----------
        guid: Union[str, Unset_Type]
            The guid of this GsaUpdateDatabase.
        """
        # Field is not nullable
        if guid is None:
            raise ValueError("Invalid value for 'guid', must not be 'None'")
        self._guid = guid

    @property
    def name(self) -> "Union[str, Unset_Type]":
        """Gets the name of this GsaUpdateDatabase.
        The name of the database. Can only be edited by a database data administrator

        Returns
        -------
        Union[str, Unset_Type]
            The name of this GsaUpdateDatabase.
        """
        return self._name

    @name.setter
    def name(self, name: "Union[str, Unset_Type]") -> None:
        """Sets the name of this GsaUpdateDatabase.
        The name of the database. Can only be edited by a database data administrator

        Parameters
        ----------
        name: Union[str, Unset_Type]
            The name of this GsaUpdateDatabase.
        """
        # Field is not nullable
        if name is None:
            raise ValueError("Invalid value for 'name', must not be 'None'")
        self._name = name

    @property
    def is_read_only(self) -> "Union[bool, Unset_Type]":
        """Gets the is_read_only of this GsaUpdateDatabase.
        True if the database should be set to read only. Can only be edited by a system administrator

        Returns
        -------
        Union[bool, Unset_Type]
            The is_read_only of this GsaUpdateDatabase.
        """
        return self._is_read_only

    @is_read_only.setter
    def is_read_only(self, is_read_only: "Union[bool, Unset_Type]") -> None:
        """Sets the is_read_only of this GsaUpdateDatabase.
        True if the database should be set to read only. Can only be edited by a system administrator

        Parameters
        ----------
        is_read_only: Union[bool, Unset_Type]
            The is_read_only of this GsaUpdateDatabase.
        """
        # Field is not nullable
        if is_read_only is None:
            raise ValueError("Invalid value for 'is_read_only', must not be 'None'")
        self._is_read_only = is_read_only

    @property
    def language(self) -> "Union[str, None, Unset_Type]":
        """Gets the language of this GsaUpdateDatabase.
        The language of the database, used when indexing the database. Can only be edited by a system administrator

        Returns
        -------
        Union[str, None, Unset_Type]
            The language of this GsaUpdateDatabase.
        """
        return self._language

    @language.setter
    def language(self, language: "Union[str, None, Unset_Type]") -> None:
        """Sets the language of this GsaUpdateDatabase.
        The language of the database, used when indexing the database. Can only be edited by a system administrator

        Parameters
        ----------
        language: Union[str, None, Unset_Type]
            The language of this GsaUpdateDatabase.
        """
        self._language = language

    @property
    def database_key(self) -> "Union[str, None, Unset_Type]":
        """Gets the database_key of this GsaUpdateDatabase.
        The unique key of the database. Can only be edited by a system administrator

        Returns
        -------
        Union[str, None, Unset_Type]
            The database_key of this GsaUpdateDatabase.
        """
        return self._database_key

    @database_key.setter
    def database_key(self, database_key: "Union[str, None, Unset_Type]") -> None:
        """Sets the database_key of this GsaUpdateDatabase.
        The unique key of the database. Can only be edited by a system administrator

        Parameters
        ----------
        database_key: Union[str, None, Unset_Type]
            The database_key of this GsaUpdateDatabase.
        """
        self._database_key = database_key

    @property
    def data_source(self) -> "Union[str, None, Unset_Type]":
        """Gets the data_source of this GsaUpdateDatabase.
        The SQL server data source. Can only be edited by a system administrator

        Returns
        -------
        Union[str, None, Unset_Type]
            The data_source of this GsaUpdateDatabase.
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source: "Union[str, None, Unset_Type]") -> None:
        """Sets the data_source of this GsaUpdateDatabase.
        The SQL server data source. Can only be edited by a system administrator

        Parameters
        ----------
        data_source: Union[str, None, Unset_Type]
            The data_source of this GsaUpdateDatabase.
        """
        self._data_source = data_source

    @property
    def use_integrated_security(self) -> "Union[bool, None, Unset_Type]":
        """Gets the use_integrated_security of this GsaUpdateDatabase.
        Set to true if the SQL connection to the database should use Windows authentication. Can only be edited by a system administrator

        Returns
        -------
        Union[bool, None, Unset_Type]
            The use_integrated_security of this GsaUpdateDatabase.
        """
        return self._use_integrated_security

    @use_integrated_security.setter
    def use_integrated_security(
        self, use_integrated_security: "Union[bool, None, Unset_Type]"
    ) -> None:
        """Sets the use_integrated_security of this GsaUpdateDatabase.
        Set to true if the SQL connection to the database should use Windows authentication. Can only be edited by a system administrator

        Parameters
        ----------
        use_integrated_security: Union[bool, None, Unset_Type]
            The use_integrated_security of this GsaUpdateDatabase.
        """
        self._use_integrated_security = use_integrated_security

    @property
    def sql_user_name(self) -> "Union[str, None, Unset_Type]":
        """Gets the sql_user_name of this GsaUpdateDatabase.
        The user name to use if the database should use SQL authentication. The password must also be provided. Can only be edited by a system administrator

        Returns
        -------
        Union[str, None, Unset_Type]
            The sql_user_name of this GsaUpdateDatabase.
        """
        return self._sql_user_name

    @sql_user_name.setter
    def sql_user_name(self, sql_user_name: "Union[str, None, Unset_Type]") -> None:
        """Sets the sql_user_name of this GsaUpdateDatabase.
        The user name to use if the database should use SQL authentication. The password must also be provided. Can only be edited by a system administrator

        Parameters
        ----------
        sql_user_name: Union[str, None, Unset_Type]
            The sql_user_name of this GsaUpdateDatabase.
        """
        self._sql_user_name = sql_user_name

    @property
    def sql_password(self) -> "Union[str, None, Unset_Type]":
        """Gets the sql_password of this GsaUpdateDatabase.
        The password name to use if the database should use SQL authentication. Can only be edited by a system administrator

        Returns
        -------
        Union[str, None, Unset_Type]
            The sql_password of this GsaUpdateDatabase.
        """
        return self._sql_password

    @sql_password.setter
    def sql_password(self, sql_password: "Union[str, None, Unset_Type]") -> None:
        """Sets the sql_password of this GsaUpdateDatabase.
        The password name to use if the database should use SQL authentication. Can only be edited by a system administrator

        Parameters
        ----------
        sql_password: Union[str, None, Unset_Type]
            The sql_password of this GsaUpdateDatabase.
        """
        self._sql_password = sql_password

    @property
    def initial_catalog(self) -> "Union[str, None, Unset_Type]":
        """Gets the initial_catalog of this GsaUpdateDatabase.
        The name of the database in SQL server. Can only be edited by a system administrator

        Returns
        -------
        Union[str, None, Unset_Type]
            The initial_catalog of this GsaUpdateDatabase.
        """
        return self._initial_catalog

    @initial_catalog.setter
    def initial_catalog(self, initial_catalog: "Union[str, None, Unset_Type]") -> None:
        """Sets the initial_catalog of this GsaUpdateDatabase.
        The name of the database in SQL server. Can only be edited by a system administrator

        Parameters
        ----------
        initial_catalog: Union[str, None, Unset_Type]
            The initial_catalog of this GsaUpdateDatabase.
        """
        self._initial_catalog = initial_catalog

    @property
    def additional_sql_parameters(self) -> "Union[str, None, Unset_Type]":
        """Gets the additional_sql_parameters of this GsaUpdateDatabase.
        Any additional parameters that will be added to the SQL connection string for the database. Must be a valid SQL connection string format. Can only be edited by a system administrator

        Returns
        -------
        Union[str, None, Unset_Type]
            The additional_sql_parameters of this GsaUpdateDatabase.
        """
        return self._additional_sql_parameters

    @additional_sql_parameters.setter
    def additional_sql_parameters(
        self, additional_sql_parameters: "Union[str, None, Unset_Type]"
    ) -> None:
        """Sets the additional_sql_parameters of this GsaUpdateDatabase.
        Any additional parameters that will be added to the SQL connection string for the database. Must be a valid SQL connection string format. Can only be edited by a system administrator

        Parameters
        ----------
        additional_sql_parameters: Union[str, None, Unset_Type]
            The additional_sql_parameters of this GsaUpdateDatabase.
        """
        self._additional_sql_parameters = additional_sql_parameters

    @property
    def loading_order(self) -> "Union[int, Unset_Type]":
        """Gets the loading_order of this GsaUpdateDatabase.
        The MI loading order for the database. Can only be edited by a system administrator

        Returns
        -------
        Union[int, Unset_Type]
            The loading_order of this GsaUpdateDatabase.
        """
        return self._loading_order

    @loading_order.setter
    def loading_order(self, loading_order: "Union[int, Unset_Type]") -> None:
        """Sets the loading_order of this GsaUpdateDatabase.
        The MI loading order for the database. Can only be edited by a system administrator

        Parameters
        ----------
        loading_order: Union[int, Unset_Type]
            The loading_order of this GsaUpdateDatabase.
        """
        # Field is not nullable
        if loading_order is None:
            raise ValueError("Invalid value for 'loading_order', must not be 'None'")
        self._loading_order = loading_order

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
        if not isinstance(other, GsaUpdateDatabase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
