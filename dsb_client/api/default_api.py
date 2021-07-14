"""
    Origin Organization I-REC API

    Swagger documentation for the DSB  # noqa: E501

    The version of the OpenAPI document: 0.1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from dsb_client.api_client import ApiClient, Endpoint as _Endpoint
from dsb_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from dsb_client.model.create_channel_dto import CreateChannelDto
from dsb_client.model.message_dto import MessageDTO
from dsb_client.model.publish_message_dto import PublishMessageDto


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __channel_controller_create(
            self,
            create_channel_dto,
            **kwargs
        ):
            """channel_controller_create  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.channel_controller_create(create_channel_dto, async_req=True)
            >>> result = thread.get()

            Args:
                create_channel_dto (CreateChannelDto):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                str
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['create_channel_dto'] = \
                create_channel_dto
            return self.call_with_http_info(**kwargs)

        self.channel_controller_create = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [],
                'endpoint_path': '/channel',
                'operation_id': 'channel_controller_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'create_channel_dto',
                ],
                'required': [
                    'create_channel_dto',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'create_channel_dto':
                        (CreateChannelDto,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'create_channel_dto': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__channel_controller_create
        )

        def __message_controller_get_new_from_channel(
            self,
            fqcn,
            **kwargs
        ):
            """message_controller_get_new_from_channel  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.message_controller_get_new_from_channel(fqcn, async_req=True)
            >>> result = thread.get()

            Args:
                fqcn (str): Fully qualified channel name (fqcn)

            Keyword Args:
                amount (str): Amount of messages to be returned in the request, default value is 100. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [MessageDTO]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['fqcn'] = \
                fqcn
            return self.call_with_http_info(**kwargs)

        self.message_controller_get_new_from_channel = _Endpoint(
            settings={
                'response_type': ([MessageDTO],),
                'auth': [],
                'endpoint_path': '/message',
                'operation_id': 'message_controller_get_new_from_channel',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'fqcn',
                    'amount',
                ],
                'required': [
                    'fqcn',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'fqcn':
                        (str,),
                    'amount':
                        (str,),
                },
                'attribute_map': {
                    'fqcn': 'fqcn',
                    'amount': 'amount',
                },
                'location_map': {
                    'fqcn': 'query',
                    'amount': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__message_controller_get_new_from_channel
        )

        def __message_controller_publish(
            self,
            publish_message_dto,
            **kwargs
        ):
            """message_controller_publish  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.message_controller_publish(publish_message_dto, async_req=True)
            >>> result = thread.get()

            Args:
                publish_message_dto (PublishMessageDto):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                str
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['publish_message_dto'] = \
                publish_message_dto
            return self.call_with_http_info(**kwargs)

        self.message_controller_publish = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [],
                'endpoint_path': '/message',
                'operation_id': 'message_controller_publish',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'publish_message_dto',
                ],
                'required': [
                    'publish_message_dto',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'publish_message_dto':
                        (PublishMessageDto,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'publish_message_dto': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__message_controller_publish
        )