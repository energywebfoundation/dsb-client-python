# dsb-client
Python client for use with the Energy Web DSB Message Broker. Some understanding
of the DSB is required (DID-based authentication via Energy Web Switchboard) and
can be found in the documentation on https://github.com/energywebfoundation/dsb.

This client was generated from the DSB Message Broker's Swagger documentation available here [schema](https://github.com/energywebfoundation/dsb/blob/master/specs/schema.yaml)

To get started with the client:
```sh
git clone {this_repo}
cd {this_repo}
python3 -m venv venv # substitute with your preferred method
source ./venv/bin/activate
python setup.py install
```

In case `python setup.py install` fails, please install dependencies using `pip install -r requirements.txt`

An example usage of the client has been provided in [examples](./examples). We
will be adding additional examples as we develop the DSB.

To run the example (while still in your virtual env):
```
python examples/login_and_get_messages.py
```

In the example, a private key is provided, which already has the user role. You
will need to substitute this for your own private key. See the DSB Message Broker
for more information about using your private key to obtain a Decentralized
Identifier (DID) and enrol as a user of the EW Distributed Service Bus.

The client will also be distributed via PyPI in the near future.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1
- Package version: 1.2.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/energywebfoundation/dsb-client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/energywebfoundation/dsb-client-python.git`)

Then import the package:
```python
import dsb_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import dsb_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import dsb_client
from pprint import pprint
from dsb_client.api import auth_api
from dsb_client.model.login_data_dto import LoginDataDTO
from dsb_client.model.login_return_data_dto import LoginReturnDataDTO
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dsb_client.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with dsb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    login_data_dto = LoginDataDTO(
        identity_token="identity_token_example",
    ) # LoginDataDTO |

    try:
        api_response = api_instance.auth_controller_login(login_data_dto)
        pprint(api_response)
    except dsb_client.ApiException as e:
        print("Exception when calling AuthApi->auth_controller_login: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**auth_controller_login**](docs/AuthApi.md#auth_controller_login) | **POST** /auth/login |
*ChannelApi* | [**channel_controller_create_channel**](docs/ChannelApi.md#channel_controller_create_channel) | **POST** /channel |
*ChannelApi* | [**channel_controller_get_accessible_channels**](docs/ChannelApi.md#channel_controller_get_accessible_channels) | **GET** /channel/pubsub |
*ChannelApi* | [**channel_controller_get_channel**](docs/ChannelApi.md#channel_controller_get_channel) | **GET** /channel/{fqcn} |
*ChannelApi* | [**channel_controller_remove_channel**](docs/ChannelApi.md#channel_controller_remove_channel) | **DELETE** /channel/{fqcn} |
*ChannelApi* | [**channel_controller_update_channel**](docs/ChannelApi.md#channel_controller_update_channel) | **PATCH** /channel |
*HealthApi* | [**health_controller_check**](docs/HealthApi.md#health_controller_check) | **GET** /health |
*MessageApi* | [**message_controller_get_new_from_channel**](docs/MessageApi.md#message_controller_get_new_from_channel) | **GET** /message |
*MessageApi* | [**message_controller_publish**](docs/MessageApi.md#message_controller_publish) | **POST** /message |


## Documentation For Models

 - [CreateChannelDto](docs/CreateChannelDto.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse503](docs/InlineResponse503.md)
 - [LoginDataDTO](docs/LoginDataDTO.md)
 - [LoginReturnDataDTO](docs/LoginReturnDataDTO.md)
 - [MessageDto](docs/MessageDto.md)
 - [PublishMessageDto](docs/PublishMessageDto.md)
 - [UpdateChannelDto](docs/UpdateChannelDto.md)


## Documentation For Authorization


## access-token

- **Type**: Bearer authentication (JWT)


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in dsb_client.apis and dsb_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from dsb_client.api.default_api import DefaultApi`
- `from dsb_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import dsb_client
from dsb_client.apis import *
from dsb_client.models import *
```
