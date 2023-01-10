# coding: utf-8

"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from . import ApiBase


class SchemaDiscreteTypesApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def v1alpha_databases_database_key_discrete_types_discrete_type_guid_delete(self, database_key, discrete_type_guid, **kwargs):  # noqa: E501
        """Delete discrete type, including all of its discrete values.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str discrete_type_guid: (required)
        :return: None
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_databases_database_key_discrete_types_discrete_type_guid_delete_with_http_info(database_key, discrete_type_guid, **kwargs)  # noqa: E501
        return data

    def v1alpha_databases_database_key_discrete_types_discrete_type_guid_delete_with_http_info(self, database_key, discrete_type_guid, **kwargs):  # noqa: E501
        """Delete discrete type, including all of its discrete values.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str discrete_type_guid: (required)
        :return: None
        """

        all_params = ['database_key', 'discrete_type_guid']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_databases_database_key_discrete_types_discrete_type_guid_delete".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_key' is set
        if ('database_key' not in params or
                params['database_key'] is None):
            raise ValueError("Missing the required parameter `database_key` when calling `v1alpha_databases_database_key_discrete_types_discrete_type_guid_delete`")  # noqa: E501
        # verify the required parameter 'discrete_type_guid' is set
        if ('discrete_type_guid' not in params or
                params['discrete_type_guid'] is None):
            raise ValueError("Missing the required parameter `discrete_type_guid` when calling `v1alpha_databases_database_key_discrete_types_discrete_type_guid_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_key' in params:
            path_params['database-key'] = params['database_key']  # noqa: E501
        if 'discrete_type_guid' in params:
            path_params['discrete-type-guid'] = params['discrete_type_guid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/databases/{database-key}/discrete-types/{discrete-type-guid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1alpha_databases_database_key_discrete_types_discrete_type_guid_get(self, database_key, discrete_type_guid, **kwargs):  # noqa: E501
        """Gets a single discrete type.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str discrete_type_guid: (required)
        :return: GrantaServerApiSchemaDiscreteType
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_databases_database_key_discrete_types_discrete_type_guid_get_with_http_info(database_key, discrete_type_guid, **kwargs)  # noqa: E501
        return data

    def v1alpha_databases_database_key_discrete_types_discrete_type_guid_get_with_http_info(self, database_key, discrete_type_guid, **kwargs):  # noqa: E501
        """Gets a single discrete type.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str discrete_type_guid: (required)
        :return: GrantaServerApiSchemaDiscreteType
        """

        all_params = ['database_key', 'discrete_type_guid']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_databases_database_key_discrete_types_discrete_type_guid_get".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_key' is set
        if ('database_key' not in params or
                params['database_key'] is None):
            raise ValueError("Missing the required parameter `database_key` when calling `v1alpha_databases_database_key_discrete_types_discrete_type_guid_get`")  # noqa: E501
        # verify the required parameter 'discrete_type_guid' is set
        if ('discrete_type_guid' not in params or
                params['discrete_type_guid'] is None):
            raise ValueError("Missing the required parameter `discrete_type_guid` when calling `v1alpha_databases_database_key_discrete_types_discrete_type_guid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_key' in params:
            path_params['database-key'] = params['database_key']  # noqa: E501
        if 'discrete_type_guid' in params:
            path_params['discrete-type-guid'] = params['discrete_type_guid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/databases/{database-key}/discrete-types/{discrete-type-guid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GrantaServerApiSchemaDiscreteType',  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1alpha_databases_database_key_discrete_types_discrete_type_guid_patch(self, database_key, discrete_type_guid, **kwargs):  # noqa: E501
        """Update discrete type.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str discrete_type_guid: (required)
        :param GrantaServerApiSchemaDiscreteType body:
        :return: GrantaServerApiSchemaDiscreteType
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_databases_database_key_discrete_types_discrete_type_guid_patch_with_http_info(database_key, discrete_type_guid, **kwargs)  # noqa: E501
        return data

    def v1alpha_databases_database_key_discrete_types_discrete_type_guid_patch_with_http_info(self, database_key, discrete_type_guid, **kwargs):  # noqa: E501
        """Update discrete type.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str discrete_type_guid: (required)
        :param GrantaServerApiSchemaDiscreteType body:
        :return: GrantaServerApiSchemaDiscreteType
        """

        all_params = ['database_key', 'discrete_type_guid', 'body']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_databases_database_key_discrete_types_discrete_type_guid_patch".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_key' is set
        if ('database_key' not in params or
                params['database_key'] is None):
            raise ValueError("Missing the required parameter `database_key` when calling `v1alpha_databases_database_key_discrete_types_discrete_type_guid_patch`")  # noqa: E501
        # verify the required parameter 'discrete_type_guid' is set
        if ('discrete_type_guid' not in params or
                params['discrete_type_guid'] is None):
            raise ValueError("Missing the required parameter `discrete_type_guid` when calling `v1alpha_databases_database_key_discrete_types_discrete_type_guid_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_key' in params:
            path_params['database-key'] = params['database_key']  # noqa: E501
        if 'discrete_type_guid' in params:
            path_params['discrete-type-guid'] = params['discrete_type_guid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/databases/{database-key}/discrete-types/{discrete-type-guid}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GrantaServerApiSchemaDiscreteType',  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1alpha_databases_database_key_discrete_types_discrete_type_guidusages_get(self, database_key, discrete_type_guid, **kwargs):  # noqa: E501
        """Gets objects that are using this discrete type.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str discrete_type_guid: (required)
        :return: GrantaServerApiSchemaSlimEntitiesSlimObjects
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_databases_database_key_discrete_types_discrete_type_guidusages_get_with_http_info(database_key, discrete_type_guid, **kwargs)  # noqa: E501
        return data

    def v1alpha_databases_database_key_discrete_types_discrete_type_guidusages_get_with_http_info(self, database_key, discrete_type_guid, **kwargs):  # noqa: E501
        """Gets objects that are using this discrete type.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str discrete_type_guid: (required)
        :return: GrantaServerApiSchemaSlimEntitiesSlimObjects
        """

        all_params = ['database_key', 'discrete_type_guid']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_databases_database_key_discrete_types_discrete_type_guidusages_get".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_key' is set
        if ('database_key' not in params or
                params['database_key'] is None):
            raise ValueError("Missing the required parameter `database_key` when calling `v1alpha_databases_database_key_discrete_types_discrete_type_guidusages_get`")  # noqa: E501
        # verify the required parameter 'discrete_type_guid' is set
        if ('discrete_type_guid' not in params or
                params['discrete_type_guid'] is None):
            raise ValueError("Missing the required parameter `discrete_type_guid` when calling `v1alpha_databases_database_key_discrete_types_discrete_type_guidusages_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_key' in params:
            path_params['database-key'] = params['database_key']  # noqa: E501
        if 'discrete_type_guid' in params:
            path_params['discrete-type-guid'] = params['discrete_type_guid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/databases/{database-key}/discrete-types/{discrete-type-guid}:usages', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GrantaServerApiSchemaSlimEntitiesSlimObjects',  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1alpha_databases_database_key_discrete_types_get(self, database_key, **kwargs):  # noqa: E501
        """Gets all discrete types for a given database.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :return: list[GrantaServerApiSchemaDiscreteType]
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_databases_database_key_discrete_types_get_with_http_info(database_key, **kwargs)  # noqa: E501
        return data

    def v1alpha_databases_database_key_discrete_types_get_with_http_info(self, database_key, **kwargs):  # noqa: E501
        """Gets all discrete types for a given database.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :return: list[GrantaServerApiSchemaDiscreteType]
        """

        all_params = ['database_key']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_databases_database_key_discrete_types_get".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_key' is set
        if ('database_key' not in params or
                params['database_key'] is None):
            raise ValueError("Missing the required parameter `database_key` when calling `v1alpha_databases_database_key_discrete_types_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_key' in params:
            path_params['database-key'] = params['database_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/databases/{database-key}/discrete-types', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GrantaServerApiSchemaDiscreteType]',  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1alpha_databases_database_key_discrete_types_post(self, database_key, **kwargs):  # noqa: E501
        """Create a new discrete type.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param GrantaServerApiSchemaDiscreteType body:
        :return: None
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_databases_database_key_discrete_types_post_with_http_info(database_key, **kwargs)  # noqa: E501
        return data

    def v1alpha_databases_database_key_discrete_types_post_with_http_info(self, database_key, **kwargs):  # noqa: E501
        """Create a new discrete type.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param GrantaServerApiSchemaDiscreteType body:
        :return: None
        """

        all_params = ['database_key', 'body']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_databases_database_key_discrete_types_post".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_key' is set
        if ('database_key' not in params or
                params['database_key'] is None):
            raise ValueError("Missing the required parameter `database_key` when calling `v1alpha_databases_database_key_discrete_types_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_key' in params:
            path_params['database-key'] = params['database_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/databases/{database-key}/discrete-types', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
