# dsb_client.MessageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**message_controller_get_new_from_channel**](MessageApi.md#message_controller_get_new_from_channel) | **GET** /message |
[**message_controller_publish**](MessageApi.md#message_controller_publish) | **POST** /message |


# **message_controller_get_new_from_channel**
> [MessageDto] message_controller_get_new_from_channel(fqcn)



Pulls new messages from the channel.

### Example

* Bearer (JWT) Authentication (access-token):
```python
import time
import dsb_client
from dsb_client.api import message_api
from dsb_client.model.message_dto import MessageDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dsb_client.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with dsb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    fqcn = "testChannel.channels.dsb.apps.energyweb.iam.ewc" # str | Fully Qualified Channel Name (fqcn)
    amount = "100" # str | Amount of messages to be returned in the request, default value is 100 (optional)
    _from = "2021-09-06T00:00:00Z" # str | Rewinds the channel and retruns messages from given point in time (optional)
    client_id = "default" # str | Id of the persistent client, default value is `` (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.message_controller_get_new_from_channel(fqcn)
        pprint(api_response)
    except dsb_client.ApiException as e:
        print("Exception when calling MessageApi->message_controller_get_new_from_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.message_controller_get_new_from_channel(fqcn, amount=amount, _from=_from, client_id=client_id)
        pprint(api_response)
    except dsb_client.ApiException as e:
        print("Exception when calling MessageApi->message_controller_get_new_from_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqcn** | **str**| Fully Qualified Channel Name (fqcn) |
 **amount** | **str**| Amount of messages to be returned in the request, default value is 100 | [optional]
 **_from** | **str**| Rewinds the channel and retruns messages from given point in time | [optional]
 **client_id** | **str**| Id of the persistent client, default value is &#x60;&#x60; | [optional]

### Return type

[**[MessageDto]**](MessageDto.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of pulled messages from a given channel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_controller_publish**
> str message_controller_publish(publish_message_dto)



Pushes a message to a topic in a channel.

### Example

* Bearer (JWT) Authentication (access-token):
```python
import time
import dsb_client
from dsb_client.api import message_api
from dsb_client.model.publish_message_dto import PublishMessageDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dsb_client.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with dsb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    publish_message_dto = PublishMessageDto(
        fqcn="testChannel.channels.dsb.apps.energyweb.iam.ewc",
        topic="testTopic",
        correlation_id="b5e2eece-b39f-486d-9513-4cadc9a59a18",
        payload="{"data": "testData"}",
        signature="signature_example",
    ) # PublishMessageDto |

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.message_controller_publish(publish_message_dto)
        pprint(api_response)
    except dsb_client.ApiException as e:
        print("Exception when calling MessageApi->message_controller_publish: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_message_dto** | [**PublishMessageDto**](PublishMessageDto.md)|  |

### Return type

**str**

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Published message ID in the specified channel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
