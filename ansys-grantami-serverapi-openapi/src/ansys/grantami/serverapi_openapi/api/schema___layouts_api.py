# coding: utf-8

"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from . import ApiBase


class SchemaLayoutsApi(ApiBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def v1alpha_databases_database_key_tables_table_guid_layouts_get(self, database_key, table_guid, **kwargs):  # noqa: E501
        """Get all layouts for table  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str table_guid: (required)
        :param str mode: The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the header.
        :param str x_ansys_vc_mode: The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the query string.
        :return: GrantaServerApiSchemaLayoutsLayoutsInfo
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_databases_database_key_tables_table_guid_layouts_get_with_http_info(database_key, table_guid, **kwargs)  # noqa: E501
        return data

    def v1alpha_databases_database_key_tables_table_guid_layouts_get_with_http_info(self, database_key, table_guid, **kwargs):  # noqa: E501
        """Get all layouts for table  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str table_guid: (required)
        :param str mode: The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the header.
        :param str x_ansys_vc_mode: The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the query string.
        :return: GrantaServerApiSchemaLayoutsLayoutsInfo
        """

        all_params = ['database_key', 'table_guid', 'mode', 'x_ansys_vc_mode']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_databases_database_key_tables_table_guid_layouts_get".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_key' is set
        if ('database_key' not in params or
                params['database_key'] is None):
            raise ValueError("Missing the required parameter `database_key` when calling `v1alpha_databases_database_key_tables_table_guid_layouts_get`")  # noqa: E501
        # verify the required parameter 'table_guid' is set
        if ('table_guid' not in params or
                params['table_guid'] is None):
            raise ValueError("Missing the required parameter `table_guid` when calling `v1alpha_databases_database_key_tables_table_guid_layouts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_key' in params:
            path_params['database-key'] = params['database_key']  # noqa: E501
        if 'table_guid' in params:
            path_params['table-guid'] = params['table_guid']  # noqa: E501

        query_params = []
        if 'mode' in params:
            query_params.append(('mode', params['mode']))  # noqa: E501

        header_params = {}
        if 'x_ansys_vc_mode' in params:
            header_params['X-Ansys-VC-Mode'] = params['x_ansys_vc_mode']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/databases/{database-key}/tables/{table-guid}/layouts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GrantaServerApiSchemaLayoutsLayoutsInfo',  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1alpha_databases_database_key_tables_table_guid_layouts_layout_guid_delete(self, database_key, table_guid, layout_guid, **kwargs):  # noqa: E501
        """Delete a layout.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str table_guid: (required)
        :param str layout_guid: (required)
        :return: None
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_databases_database_key_tables_table_guid_layouts_layout_guid_delete_with_http_info(database_key, table_guid, layout_guid, **kwargs)  # noqa: E501
        return data

    def v1alpha_databases_database_key_tables_table_guid_layouts_layout_guid_delete_with_http_info(self, database_key, table_guid, layout_guid, **kwargs):  # noqa: E501
        """Delete a layout.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str table_guid: (required)
        :param str layout_guid: (required)
        :return: None
        """

        all_params = ['database_key', 'table_guid', 'layout_guid']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_databases_database_key_tables_table_guid_layouts_layout_guid_delete".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_key' is set
        if ('database_key' not in params or
                params['database_key'] is None):
            raise ValueError("Missing the required parameter `database_key` when calling `v1alpha_databases_database_key_tables_table_guid_layouts_layout_guid_delete`")  # noqa: E501
        # verify the required parameter 'table_guid' is set
        if ('table_guid' not in params or
                params['table_guid'] is None):
            raise ValueError("Missing the required parameter `table_guid` when calling `v1alpha_databases_database_key_tables_table_guid_layouts_layout_guid_delete`")  # noqa: E501
        # verify the required parameter 'layout_guid' is set
        if ('layout_guid' not in params or
                params['layout_guid'] is None):
            raise ValueError("Missing the required parameter `layout_guid` when calling `v1alpha_databases_database_key_tables_table_guid_layouts_layout_guid_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_key' in params:
            path_params['database-key'] = params['database_key']  # noqa: E501
        if 'table_guid' in params:
            path_params['table-guid'] = params['table_guid']  # noqa: E501
        if 'layout_guid' in params:
            path_params['layout-guid'] = params['layout_guid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/databases/{database-key}/tables/{table-guid}/layouts/{layout-guid}', 'DELETE',
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

    def v1alpha_databases_database_key_tables_table_guid_layouts_layout_guid_get(self, database_key, table_guid, layout_guid, **kwargs):  # noqa: E501
        """Get a layout with a specified guid for a given database and table.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str table_guid: (required)
        :param str layout_guid: (required)
        :param bool show_full_detail:
        :param str mode: The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the header.
        :param str x_ansys_vc_mode: The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the query string.
        :return: GrantaServerApiSchemaLayoutsLayout
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_databases_database_key_tables_table_guid_layouts_layout_guid_get_with_http_info(database_key, table_guid, layout_guid, **kwargs)  # noqa: E501
        return data

    def v1alpha_databases_database_key_tables_table_guid_layouts_layout_guid_get_with_http_info(self, database_key, table_guid, layout_guid, **kwargs):  # noqa: E501
        """Get a layout with a specified guid for a given database and table.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str table_guid: (required)
        :param str layout_guid: (required)
        :param bool show_full_detail:
        :param str mode: The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the header.
        :param str x_ansys_vc_mode: The version control mode. If not provided, defaults to write mode if the user is allowed to see that. Can also be set in the query string.
        :return: GrantaServerApiSchemaLayoutsLayout
        """

        all_params = ['database_key', 'table_guid', 'layout_guid', 'show_full_detail', 'mode', 'x_ansys_vc_mode']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_databases_database_key_tables_table_guid_layouts_layout_guid_get".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_key' is set
        if ('database_key' not in params or
                params['database_key'] is None):
            raise ValueError("Missing the required parameter `database_key` when calling `v1alpha_databases_database_key_tables_table_guid_layouts_layout_guid_get`")  # noqa: E501
        # verify the required parameter 'table_guid' is set
        if ('table_guid' not in params or
                params['table_guid'] is None):
            raise ValueError("Missing the required parameter `table_guid` when calling `v1alpha_databases_database_key_tables_table_guid_layouts_layout_guid_get`")  # noqa: E501
        # verify the required parameter 'layout_guid' is set
        if ('layout_guid' not in params or
                params['layout_guid'] is None):
            raise ValueError("Missing the required parameter `layout_guid` when calling `v1alpha_databases_database_key_tables_table_guid_layouts_layout_guid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_key' in params:
            path_params['database-key'] = params['database_key']  # noqa: E501
        if 'table_guid' in params:
            path_params['table-guid'] = params['table_guid']  # noqa: E501
        if 'layout_guid' in params:
            path_params['layout-guid'] = params['layout_guid']  # noqa: E501

        query_params = []
        if 'show_full_detail' in params:
            query_params.append(('showFullDetail', params['show_full_detail']))  # noqa: E501
        if 'mode' in params:
            query_params.append(('mode', params['mode']))  # noqa: E501

        header_params = {}
        if 'x_ansys_vc_mode' in params:
            header_params['X-Ansys-VC-Mode'] = params['x_ansys_vc_mode']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1alpha/databases/{database-key}/tables/{table-guid}/layouts/{layout-guid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GrantaServerApiSchemaLayoutsLayout',  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1alpha_databases_database_key_tables_table_guid_layouts_layout_guid_patch(self, database_key, table_guid, layout_guid, **kwargs):  # noqa: E501
        """Update a layout.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str table_guid: (required)
        :param str layout_guid: (required)
        :param GrantaServerApiSchemaLayoutsLayout body:
        :return: GrantaServerApiSchemaLayoutsLayout
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_databases_database_key_tables_table_guid_layouts_layout_guid_patch_with_http_info(database_key, table_guid, layout_guid, **kwargs)  # noqa: E501
        return data

    def v1alpha_databases_database_key_tables_table_guid_layouts_layout_guid_patch_with_http_info(self, database_key, table_guid, layout_guid, **kwargs):  # noqa: E501
        """Update a layout.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str table_guid: (required)
        :param str layout_guid: (required)
        :param GrantaServerApiSchemaLayoutsLayout body:
        :return: GrantaServerApiSchemaLayoutsLayout
        """

        all_params = ['database_key', 'table_guid', 'layout_guid', 'body']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_databases_database_key_tables_table_guid_layouts_layout_guid_patch".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_key' is set
        if ('database_key' not in params or
                params['database_key'] is None):
            raise ValueError("Missing the required parameter `database_key` when calling `v1alpha_databases_database_key_tables_table_guid_layouts_layout_guid_patch`")  # noqa: E501
        # verify the required parameter 'table_guid' is set
        if ('table_guid' not in params or
                params['table_guid'] is None):
            raise ValueError("Missing the required parameter `table_guid` when calling `v1alpha_databases_database_key_tables_table_guid_layouts_layout_guid_patch`")  # noqa: E501
        # verify the required parameter 'layout_guid' is set
        if ('layout_guid' not in params or
                params['layout_guid'] is None):
            raise ValueError("Missing the required parameter `layout_guid` when calling `v1alpha_databases_database_key_tables_table_guid_layouts_layout_guid_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_key' in params:
            path_params['database-key'] = params['database_key']  # noqa: E501
        if 'table_guid' in params:
            path_params['table-guid'] = params['table_guid']  # noqa: E501
        if 'layout_guid' in params:
            path_params['layout-guid'] = params['layout_guid']  # noqa: E501

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
            '/v1alpha/databases/{database-key}/tables/{table-guid}/layouts/{layout-guid}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GrantaServerApiSchemaLayoutsLayout',  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1alpha_databases_database_key_tables_table_guid_layouts_post(self, database_key, table_guid, **kwargs):  # noqa: E501
        """Create a new layout.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str table_guid: (required)
        :param GrantaServerApiSchemaSlimEntitiesSlimLayout body:
        :return: GrantaServerApiSchemaSlimEntitiesSlimLayout
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.v1alpha_databases_database_key_tables_table_guid_layouts_post_with_http_info(database_key, table_guid, **kwargs)  # noqa: E501
        return data

    def v1alpha_databases_database_key_tables_table_guid_layouts_post_with_http_info(self, database_key, table_guid, **kwargs):  # noqa: E501
        """Create a new layout.  # noqa: E501

        This method makes a synchronous HTTP request.

        :param str database_key: (required)
        :param str table_guid: (required)
        :param GrantaServerApiSchemaSlimEntitiesSlimLayout body:
        :return: GrantaServerApiSchemaSlimEntitiesSlimLayout
        """

        all_params = ['database_key', 'table_guid', 'body']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '{}' to method v1alpha_databases_database_key_tables_table_guid_layouts_post".format(key)
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_key' is set
        if ('database_key' not in params or
                params['database_key'] is None):
            raise ValueError("Missing the required parameter `database_key` when calling `v1alpha_databases_database_key_tables_table_guid_layouts_post`")  # noqa: E501
        # verify the required parameter 'table_guid' is set
        if ('table_guid' not in params or
                params['table_guid'] is None):
            raise ValueError("Missing the required parameter `table_guid` when calling `v1alpha_databases_database_key_tables_table_guid_layouts_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'database_key' in params:
            path_params['database-key'] = params['database_key']  # noqa: E501
        if 'table_guid' in params:
            path_params['table-guid'] = params['table_guid']  # noqa: E501

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
            '/v1alpha/databases/{database-key}/tables/{table-guid}/layouts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GrantaServerApiSchemaSlimEntitiesSlimLayout',  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
