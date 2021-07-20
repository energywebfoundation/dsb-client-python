# dsb_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channel_controller_create**](DefaultApi.md#channel_controller_create) | **POST** /channel | 
[**message_controller_get_new_from_channel**](DefaultApi.md#message_controller_get_new_from_channel) | **GET** /message | 
[**message_controller_publish**](DefaultApi.md#message_controller_publish) | **POST** /message | 


# **channel_controller_create**
> str channel_controller_create(create_channel_dto)



### Example

```python
import time
import dsb_client
from dsb_client.api import default_api
from dsb_client.model.create_channel_dto import CreateChannelDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dsb_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with dsb_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    create_channel_dto = CreateChannelDto(
        fqcn="test.channels.testapp.apps.testorganization.iam.ewc",
    ) # CreateChannelDto | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.channel_controller_create(create_channel_dto)
        pprint(api_response)
    except dsb_client.ApiException as e:
        print("Exception when calling DefaultApi->channel_controller_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_channel_dto** | [**CreateChannelDto**](CreateChannelDto.md)|  |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Creates a channel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_controller_get_new_from_channel**
> [MessageDTO] message_controller_get_new_from_channel(fqcn)



### Example

```python
import time
import dsb_client
from dsb_client.api import default_api
from dsb_client.model.message_dto import MessageDTO
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dsb_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with dsb_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    fqcn = "test.channels.testapp.apps.testorganization.iam.ewc" # str | Fully qualified channel name (fqcn)
    amount = "1000" # str | Amount of messages to be returned in the request, default value is 100 (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.message_controller_get_new_from_channel(fqcn)
        pprint(api_response)
    except dsb_client.ApiException as e:
        print("Exception when calling DefaultApi->message_controller_get_new_from_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.message_controller_get_new_from_channel(fqcn, amount=amount)
        pprint(api_response)
    except dsb_client.ApiException as e:
        print("Exception when calling DefaultApi->message_controller_get_new_from_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqcn** | **str**| Fully qualified channel name (fqcn) |
 **amount** | **str**| Amount of messages to be returned in the request, default value is 100 | [optional]

### Return type

[**[MessageDTO]**](MessageDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pull and returns messages from given channel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_controller_publish**
> str message_controller_publish(publish_message_dto)



### Example

```python
import time
import dsb_client
from dsb_client.api import default_api
from dsb_client.model.publish_message_dto import PublishMessageDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dsb_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with dsb_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    publish_message_dto = PublishMessageDto(
        fqcn="test.channels.testapp.apps.testorganization.iam.ewc",
        payload="{"data": "test"}",
        signature="signature_example",
    ) # PublishMessageDto | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.message_controller_publish(publish_message_dto)
        pprint(api_response)
    except dsb_client.ApiException as e:
        print("Exception when calling DefaultApi->message_controller_publish: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_message_dto** | [**PublishMessageDto**](PublishMessageDto.md)|  |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Message id that is local to fqcn |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

