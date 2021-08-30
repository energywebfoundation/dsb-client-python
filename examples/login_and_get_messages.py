import time
import dsb_client
from pprint import pprint
from dsb_client.api import auth_api
from dsb_client.api import crypto
from dsb_client.model.login_data_dto import LoginDataDTO
from dsb_client.model.login_return_data_dto import LoginReturnDataDTO
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dsb_client.Configuration(
    host="http://localhost:3001"
)

# Enter a context with an instance of the API client
with dsb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)

    crypto_instance = crypto.Crypto()

    # sign proof of DID ownership
    # note! the DID should already have enroled in Switchboard to the "user" role
    # see documentation about enrolment on https://github.com/energywebfoundation/dsb
    identity_token = crypto_instance.get_identity_token(
        did="did:ethr:0x37d37b10d1186aE41737D38b2dBC5C88316c9FBd",
        private_key='0xe2caca2e7c22fc5bf985cc6838e152753c52b925620bf2449e388c90e3d853f7')

    login_data_dto = LoginDataDTO(
        identity_token=identity_token,
    )  # LoginDataDTO |

    try:
        api_response = api_instance.auth_controller_login(login_data_dto)
        pprint(api_response)
    except dsb_client.ApiException as e:
        print("Exception when calling AuthApi->auth_controller_login: %s\n" % e)
